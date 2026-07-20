import os
import re
import subprocess
from google.cloud import translate_v3 as translate

def get_changed_files():
    # 讀取 Actions 傳進來的目標分支名稱（通常是 main）
    base_branch = os.getenv("BASE_BRANCH", "main")
    
    # 確保虛擬機本地有 base 分支的資訊
    subprocess.run(["git", "fetch", "origin", base_branch], capture_output=True)
    
    # 【關鍵修改】：比對目前 PR 分支與遠端 main 分支的檔案差異
    result = subprocess.run(
        ["git", "diff", "--name-only", f"origin/{base_branch}...HEAD"],
        capture_output=True, text=True
    )
    files = result.stdout.splitlines()
    return [f for f in files if f.endswith('.md') and os.path.exists(f)]

def get_previous_version_content(file_path):
    """【關鍵修改】：從遠端 main 分支撈出還沒被你修改前的原始中文內容"""
    base_branch = os.getenv("BASE_BRANCH", "main")
    result = subprocess.run(
        ["git", "show", f"origin/{base_branch}:{file_path}"],
        capture_output=True, text=True, encoding='utf-8'
    )
    return result.stdout if result.returncode == 0 else ""

# ...（其餘 parse_markdown_by_headings、translate_block 等樂高積木重組邏輯完全不變，完美沿用！）