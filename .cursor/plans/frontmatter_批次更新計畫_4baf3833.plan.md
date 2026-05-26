---
name: Frontmatter 批次更新計畫
overview: 將 docs 中的 Markdown 文件 frontmatter 更新為符合 Zensical 新版結構描述的格式，並確保內容完整性與欄位提取準確。
todos:
  - id: wait-for-list
    content: 等待使用者提供文件清單
    status: completed
  - id: read-and-parse
    content: 逐一讀取並解析文件內容與舊版 frontmatter
    status: completed
  - id: transform-logic
    content: 執行欄位映射、提取與格式化邏輯
    status: completed
  - id: sync-and-write
    content: 同步 description 至正文位置並寫回文件
    status: completed
isProject: false
---

# Frontmatter 批次更新計畫

本計畫旨在將 `docs/` 資料夾中的文件 frontmatter 轉換為新版格式。我們將嚴格遵循 `reference/frontmatter-skill-reference.md` 與 `duckops/playbooks/frontmatter.md` 中的規範。

### 1. 核心轉換邏輯

針對每一份文件，我將執行以下轉換步驟：

- **基本欄位映射**：
    - `title`: 保留並確保為必填。
    - `description`: 保留，並確保同步至正文 `# Title` 下方。
    - `created`: 若缺失則補上當前時間 `2026-05-25 14:31`，若已有則保留。
    - `last_modified`: 更新為當前時間 `2026-05-25 14:31`。
    - `lang`: 統一設定為 `zh-TW`。
    - `permalink`: 若缺失則根據標題生成小寫、英數與連字號格式的 Slug。
- **欄位名稱更新**：
    - `product` -> `products` (轉為 Array)。
    - `module` -> `modules` (轉為 Array)。
    - `activ` -> `acoiv` (映射至 `activate`, `configure`, `operation`, `integration`)。
    - `tasks` -> `intents` (轉為 Array)。
- **內容提取與格式化**：
    - `features` & `intents`: 從內容提取，多詞組合使用底線 `_` 取代空格（例如：`Google_Analytics_4`）。
    - `related` & `prerequisites`: 格式化為 `"[[檔案名稱]]"`，不含 `.md`。
    - `cyb_extensions`: 僅在文中提及相關外掛（如 `AUTOMATION`, `NOW!`）時填寫，否則設為 `[]`。
- **補齊選填欄位**：
    - 補齊 `status`, `version`, `author`, `reviewers`, `notes`, `ga_views`, `feedback`, `sites`, `audiences`, `difficulty`, `tnb`, `plans`, `apis`, `devices`, `ui_components`, `paths`, `layouts`, `wp_url`, `comments`, `search`, `icon`, `hide` 等欄位，並賦予合理的預設值或從內容推斷。

### 2. 執行流程

1. **接收清單**：等待使用者提供欲轉換的文件路徑。
2. **逐一處理**：
    - 讀取文件全文。
    - 解析舊版 frontmatter 並提取內容特徵。
    - 生成符合新版 Schema 的 YAML 字串。
    - 檢查並同步 `description` 至正文位置。
    - 寫回文件。
3. **品質檢查**：確保所有必填欄位均已填寫，且格式符合 Zensical 規範。

### 3. 關鍵參考文件

- `[reference/frontmatter-skill-reference.md](reference/frontmatter-skill-reference.md)`：核心規範與最佳實踐。
- `[duckops/playbooks/frontmatter.md](duckops/playbooks/frontmatter.md)`：詳盡的 Schema 定義。
- `[AGENTS.md](AGENTS.md)`：專案通用規範。
