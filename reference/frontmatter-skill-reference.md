title: frontmatter
created: 2026-03-05 10:50
last_modified: 2026-03-23 18:45
---

## Frontmatter Schema

(Schema details remain unchanged...)

## 🤖 最佳實踐與學習筆記 (Agent Lessons Learnt)

### 1. 內容完整性
- **不可空值**：`title`, `description`, `lang`, `permalink` 必須填寫。
- **描述同步**：`description` 的文字必須同步填寫在正文 `# Title` 下方的 `{ .subtitle }` 之前一行。

### 2. 欄位提取規則 (Extraction Rules)
- **cyb_extensions**：僅在文中明確提到相關外掛（如 AUTOMATION, CHAT BOX）時才填寫。若文中無提及，應設為空陣列 `[]`。
- **intents & features**：必須從內容提取。多詞組合必須使用底線 `_` 取代空格（例如：`Google_Analytics_4`）。
- **related & prerequisites**：
    - 使用雙引號維基連結格式：`"[[檔案名稱]]"`。
    - 檔案名稱不含 `.md`。

### 3. 命名與格式
- **Permalink**：使用小寫、英文字母、數字與連字號 `-` 組成的 URL Slug。
- **Acoiv**：必須根據內容性質選擇：
    - `activate`: 開通/註冊。
    - `configure`: 設定/調整。
    - `operation`: 日常操作。
    - `integration`: 第三方串接。

### 4. 自動化建議
- 執行 `frontmatterer` 前，建議先執行 `glob` 或 `grep` 搜尋相關文件以補齊 `related` 欄位。
- 發現 `description` 缺失時，應主動提取首段摘要填入。
