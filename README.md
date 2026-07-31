# CYB DOC (zh-TW)

Documentation site for the CYB patform. 

## Information Architecture

``` mermaid
graph TD
    %% Top level: Product lines
    A[品牌官網] --> B1[商品管理]
    A --> B2[支付金流]
    A --> B3[會員管理]

    C[智慧倉儲] --> D1[倉儲管理]
    E[智能 POS] --> F1[POS 管理]
    G[門市助理] --> H1[門市管理]
    I[資源中心] --> 1[更新紀錄]
    I[資源中心] --> J2[詞彙表] 
    I[資源中心] --> J3[慣例] 

    %% Docs container under each module
    B1 --> B1_docs[文件]
    B2 --> B2_docs[文件]
    B3 --> B3_docs[文件]
    D1 --> D1_docs[文件]
    F1 --> F1_docs[文件]
    H1 --> H1_docs[文件]

    %% Individual doc categories under Docs container
    B1_docs --> B1_doc1[使用須知]
    B1_docs --> B1_doc2[操作流程]
    B1_docs --> B1_doc3[常見問題]
    B1_docs --> B1_doc4[延伸閱讀]

```

## Frontmatter (metadata)

每個 `.md` 文件的 YAML frontmatter 定義文件中繼資料。Schema 定義於 `frontmatter-schema.yaml`，包含所有欄位的名稱、型別、必填與合法值。

驗證指令：

```bash
# 檢查所有文件
python scripts/validate_docs.py

# 檢查單一文件
python scripts/validate_docs.py docs/ec/app-market/chatbox/connect-chat-box-to-facebook-page.md

# 檢查多個文件
python scripts/validate_docs.py docs/ec/app-market/**/*.md
```

Pre-commit hook 會在 `git commit` 時自動執行檢查，阻擋不符合 schema 的檔案。

## Environment Setup

```bash
# 1. Clone repo
git clone <repo-url>
cd zensical-zh-tw

# 2. Create venv
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install pre-commit hook
pip install pre-commit
pre-commit install

# 5. Start dev server (optional)
zensical serve -f zensical.toml -a 127.0.0.1:8000
```

Pre-commit hook 會在每次 `git commit` 時自動執行 `validate_docs.py`，若 frontmatter 不符 schema 則阻擋提交。

