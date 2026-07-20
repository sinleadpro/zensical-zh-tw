"""依段落（H2~H5 標題）為單位，只翻譯「有變更的段落」，並把結果寫回對應的
語言版本檔案（<path>.<lang>.md），保留未變更段落原有的既有翻譯。

【稽核修正說明】原始版本只有 get_changed_files() / get_previous_version_content()
兩個輔助函式，段落切分、差異比對、呼叫 Google Cloud Translate、寫回檔案的核心
邏輯全部缺失（僅有一行註解占位）。本版本補上完整流程：

    1. get_changed_files()          找出這次 PR 有變更且存在的 .md 檔案（未變更）
    2. parse_markdown_by_headings() 依 H2~H5 標題切分成段落區塊（新增）
    3. match_blocks()                比對新舊版本段落，標記「新增/變更」或「未變更」（新增）
    4. translate_block()             只對「新增/變更」的段落呼叫 Google Cloud Translate（新增）
    5. process_file() / main()       未變更段落直接沿用既有翻譯，寫回語言版本檔案（新增）
"""

import os
import re
import sys
import subprocess

from google.cloud import translate_v3 as translate

# 依 repo 內既有的 `.nav.en.yml` 命名慣例，翻譯輸出採「同路徑 + 語言代碼」
# 後綴（例如 docs/ec/foo.md -> docs/ec/foo.en.md），與原始中文檔案並存。
HEADING_RE = re.compile(r"^(#{2,5})[ \t]+(.+?)[ \t]*$")
TRAILING_ATTR_RE = re.compile(r"(\s*\{[^{}]*\}\s*)$")

# 翻譯前先保護不該被翻譯機器改動的語法：程式碼區塊／行內程式碼／連結與圖片／
# HTML 標籤／attr_list 屬性區塊（例如 `{ .hero-page }`、`{: #anchor}`）。
_PROTECT_PATTERNS = [
    re.compile(r"```.*?```", re.DOTALL),
    re.compile(r"`[^`\n]+`"),
    re.compile(r"!?\[[^\]]*\]\([^)]+\)"),
    re.compile(r"<[^>]+>"),
    re.compile(r"\{[^{}]*\}"),
]
_TOKEN_OPEN, _TOKEN_CLOSE = "\uE000", "\uE001"


def get_changed_files():
    """找出這次 PR 相對於 base 分支有變更、且檔案目前仍存在的 .md 檔案。"""
    base_branch = os.getenv("BASE_BRANCH", "main")
    subprocess.run(["git", "fetch", "origin", base_branch], capture_output=True)

    result = subprocess.run(
        ["git", "diff", "--name-only", f"origin/{base_branch}...HEAD"],
        capture_output=True, text=True,
    )
    files = result.stdout.splitlines()
    return [f for f in files if f.endswith(".md") and os.path.exists(f)]


def get_previous_version_content(file_path):
    """從遠端 base 分支撈出這個檔案在修改前的原始內容；新檔案時回傳空字串。"""
    base_branch = os.getenv("BASE_BRANCH", "main")
    result = subprocess.run(
        ["git", "show", f"origin/{base_branch}:{file_path}"],
        capture_output=True, text=True, encoding="utf-8",
    )
    return result.stdout if result.returncode == 0 else ""


def parse_markdown_by_headings(content):
    """依 H2~H5 標題切分成段落區塊。

    H1、frontmatter、以及第一個 H2~H5 之前的開場文字，全部歸入索引 0 的
    「前言」區塊（level=0）。同一份文件中重複出現的標題文字，由呼叫端的
    match_blocks() 搭配出現次數做去重，避免互相覆蓋。
    """
    blocks = []
    current = {"level": 0, "heading": "", "lines": []}

    for line in content.splitlines(keepends=True):
        m = HEADING_RE.match(line)
        if m:
            if current["lines"]:
                blocks.append({
                    "level": current["level"],
                    "heading": current["heading"],
                    "text": "".join(current["lines"]),
                })
            current = {"level": len(m.group(1)), "heading": m.group(2).strip(), "lines": [line]}
        else:
            current["lines"].append(line)

    if current["lines"]:
        blocks.append({
            "level": current["level"],
            "heading": current["heading"],
            "text": "".join(current["lines"]),
        })
    return blocks


def _heading_keys(blocks):
    """把每個區塊轉成「層級::標題::第幾次出現」的唯一鍵，用來做新舊版本比對。"""
    seen = {}
    keys = []
    for b in blocks:
        base_key = f"{b['level']}::{b['heading']}"
        seen[base_key] = seen.get(base_key, 0) + 1
        keys.append(f"{base_key}::{seen[base_key]}")
    return keys


def match_blocks(old_blocks, new_blocks):
    """比對新舊版本的段落，回傳與 new_blocks 等長的清單：
    (new_block, 對應的 old_block 索引或 None, 是否有變更)。

    只有「新增的段落」或「內容真的不同的段落」才會標記為 changed=True，
    未變更的段落沿用舊版翻譯，不會被送去 Google Cloud 翻譯。
    """
    old_keys = _heading_keys(old_blocks)
    new_keys = _heading_keys(new_blocks)
    old_index_by_key = {key: i for i, key in enumerate(old_keys)}

    matches = []
    for key, new_block in zip(new_keys, new_blocks):
        old_idx = old_index_by_key.get(key)
        if old_idx is None:
            matches.append((new_block, None, True))
        else:
            # 用 rstrip 比較，避免區塊結尾的空行數量差異（純排版差異，
            # 常因為下一個標題前後有無空行造成）被誤判成「內容有變更」。
            changed = old_blocks[old_idx]["text"].rstrip() != new_block["text"].rstrip()
            matches.append((new_block, old_idx, changed))
    return matches


def _protect_non_translatable(text):
    """把程式碼／連結／HTML／attr_list 等語法暫時換成佔位符，避免被翻譯打散。"""
    tokens = {}
    counter = 0
    protected = text
    for pattern in _PROTECT_PATTERNS:
        def _replace(m, pattern=pattern):
            nonlocal counter
            token = f"{_TOKEN_OPEN}{counter}{_TOKEN_CLOSE}"
            tokens[token] = m.group(0)
            counter += 1
            return token
        protected = pattern.sub(_replace, protected)
    return protected, tokens


def _restore_non_translatable(text, tokens):
    restored = text
    for token, original in tokens.items():
        restored = restored.replace(token, original)
    return restored


def translate_text(client, parent, text, target_language, source_language):
    """呼叫 Google Cloud Translation v3，翻譯前後做語法保護／還原。"""
    if not text or not text.strip():
        return text
    protected, tokens = _protect_non_translatable(text)
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [protected],
            "mime_type": "text/plain",
            "source_language_code": source_language,
            "target_language_code": target_language,
        }
    )
    translated = response.translations[0].translated_text
    return _restore_non_translatable(translated, tokens)


def translate_block(client, parent, block, target_language, source_language):
    """翻譯單一段落：標題與內文分開送出，並保留標題後的 attr_list（如 {#anchor}）。"""
    if block["level"] == 0:
        return translate_text(client, parent, block["text"], target_language, source_language)

    text = block["text"]
    first_newline = text.find("\n")
    heading_line = text[: first_newline + 1] if first_newline != -1 else text
    body = text[first_newline + 1:] if first_newline != -1 else ""

    heading_text = block["heading"]
    attr_match = TRAILING_ATTR_RE.search(heading_text)
    trailing_attr = attr_match.group(1) if attr_match else ""
    heading_core = heading_text[: attr_match.start()] if attr_match else heading_text

    translated_heading_core = translate_text(client, parent, heading_core, target_language, source_language)
    translated_body = translate_text(client, parent, body, target_language, source_language) if body.strip() else body

    hashes = "#" * block["level"]
    line_ending = "\n" if heading_line.endswith("\n") else ""
    return f"{hashes} {translated_heading_core}{trailing_attr}{line_ending}{translated_body}"


def get_target_path(file_path, target_language):
    base, ext = os.path.splitext(file_path)
    return f"{base}.{target_language}{ext}"


def read_existing_target(file_path, target_language):
    """讀取既有的翻譯檔案：優先讀工作目錄，沒有的話回頭去 base 分支撈舊版。"""
    target_path = get_target_path(file_path, target_language)
    if os.path.exists(target_path):
        with open(target_path, "r", encoding="utf-8") as f:
            return f.read(), target_path

    base_branch = os.getenv("BASE_BRANCH", "main")
    result = subprocess.run(
        ["git", "show", f"origin/{base_branch}:{target_path}"],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode == 0:
        return result.stdout, target_path
    return "", target_path


def process_file(file_path, client, parent, target_language, source_language):
    """處理單一有變更的來源檔案：只翻譯變更段落，未變更段落沿用既有翻譯。"""
    with open(file_path, "r", encoding="utf-8") as f:
        new_source_content = f.read()
    old_source_content = get_previous_version_content(file_path)

    old_source_blocks = parse_markdown_by_headings(old_source_content)
    new_source_blocks = parse_markdown_by_headings(new_source_content)
    matches = match_blocks(old_source_blocks, new_source_blocks)

    existing_target_content, target_path = read_existing_target(file_path, target_language)
    old_target_blocks = parse_markdown_by_headings(existing_target_content)

    output_parts = []
    translated_count = 0
    reused_count = 0

    for new_block, old_idx, changed in matches:
        # 未變更、且舊版翻譯檔裡有對應區塊時，直接沿用既有翻譯——不呼叫 API。
        if not changed and old_idx is not None and old_idx < len(old_target_blocks):
            output_parts.append(old_target_blocks[old_idx]["text"])
            reused_count += 1
            continue

        try:
            output_parts.append(
                translate_block(client, parent, new_block, target_language, source_language)
            )
        except Exception as exc:  # 單一段落翻譯失敗不應中斷整份文件
            label = new_block["heading"] or "前言"
            print(f"[WARN] {file_path} 的「{label}」段落翻譯失敗，暫時保留原文：{exc}")
            output_parts.append(new_block["text"])
        translated_count += 1

    final_content = "".join(output_parts)
    target_dir = os.path.dirname(target_path)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    print(
        f"[INFO] {file_path} -> {target_path}："
        f"送出翻譯 {translated_count} 個段落，沿用既有翻譯 {reused_count} 個段落"
    )
    return translated_count, reused_count


def main():
    target_language = os.getenv("TARGET_LANGUAGE", "en")
    source_language = os.getenv("SOURCE_LANGUAGE", "zh-TW")
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("GCP_LOCATION", "global")

    if not project_id:
        print("[ERROR] 缺少環境變數 GCP_PROJECT_ID，無法呼叫 Google Cloud Translation。")
        sys.exit(1)

    changed_files = get_changed_files()
    if not changed_files:
        print("[INFO] 沒有偵測到任何 .md 檔案變更，不會呼叫 Google Cloud Translation。")
        return

    client = translate.TranslationServiceClient()
    parent = f"projects/{project_id}/locations/{location}"

    total_translated = 0
    total_reused = 0
    for file_path in changed_files:
        translated, reused = process_file(file_path, client, parent, target_language, source_language)
        total_translated += translated
        total_reused += reused

    print(
        f"[SUMMARY] 共處理 {len(changed_files)} 個檔案；"
        f"送出翻譯 {total_translated} 個段落、沿用既有翻譯 {total_reused} 個段落。"
    )


if __name__ == "__main__":
    main()
