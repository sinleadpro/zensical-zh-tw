# IBP (Industry Best Practice) 慣例

本專案的所有文件與技能操作均遵循 **IBP (Industry Best Practice)** 規範。當提及「依 IBP 處理」、「符合 IBP」、「IBP 格式」等表述時，應遵守以下規則：

## 文件類型 frontmatter 規範

### Reference Doc
- Frontmatter **保持精簡**，僅保留對參考文件有意義的欄位
- **不包含**：`devices`、`ui_components`、`paths`、`difficulty`、`tnb`、`plans`、`intents`、`features`、`prerequisites`、`related`、`acoiv`、`apis`、`layouts`、`wp_url`、`ga_views`、`feedback`、`cyb_extensions`、`comments`、`search`
- Type: `reference`
- 適合：表格、對照表、規格、欄位定義、API 參數對照

### Tutorial Doc
- Frontmatter **包含完整操作性欄位**：`devices`、`intents`、`prerequisites`、`plans`、`ui_components`、`paths` 等
- **`icon` 不應留空**：教學文件需指定 Lucide 圖示（如 `lucide/file-spreadsheet`、`lucide/package`），以正確顯示於導覽與卡片
- Type: `tutorial`
- 適合：步驟流程、操作指南、設定教學

## Callout 格式規範 (next-stepper)
- 使用 `!!! tip "簡短標題"` + body 縮排
- 不要將整段文字塞入 title 位置

## 文件類型與內容配對
| 內容特徵 | 應用的文件類型 |
|:---|:---|
| 表格、對照表、規格、欄位定義 | `reference` |
| 數字步驟、按鈕操作、流程圖 | `tutorial` |

## 檔案路徑與命名慣例

### 文件命名
- 教學文件以 `setup-` 開頭（`setup-paypal.md`），參考文件以 `-reference` 結尾
- 中文檔名已陸續遷移至英文 kebab-case（`設定超商配送限制與物流排除.md` → `cvs-shipping-restrictions-exclusions.md`）

### 跨目錄檔案位置
| 檔案 | 實際目錄 |
|------|----------|
| `order-return-process.md`、`order-refund-process.md` | `docs/ec/orders/`（非 `returns-refunds/`） |
| `cvs-b2c-bulk-shipping.md`、`cvs-c2c-shipping.md` | `docs/ec/orders/cvs-shipping/` |
| `points-deposits.md`（Cyber 幣儲值中心） | `docs/ec/website-management/` |
| `cvs-shipping-restrictions-exclusions.md` | `docs/ec/products/shipping/` |
| `宅配貨到付款（黑貓宅配通新竹物流）.md` | ~~已刪除，重複於~~ `home-delivery-cash-on-delivery.md` |
| `建立宅配貨到不付款自訂物流.md` | ~~已刪除，重複於~~ `setup-home-delivery-non-cod-custom-logistics.md` |

### 圖片命名（新規範）
- 新圖片使用英文 kebab-case：`ec-{module}-{feature}-{action}.png`
- 範例：`ec-logistics-cvs-b2c-setup-page.png`

## 圖片規範
- 每張圖片必須有 TC alt text（3-8 字）及 `{ title="..." }` 屬性
- Hero images：`![alt](path){ title="alt" .hero-page }`
- 相對路徑：`docs/ec/{module}/`（depth 3）→ `../../assets/images/`

## 連結規範
- Grid card 連結需補 `{ title="目標頁面 title" }`
- `data-preview` 僅在目標含表格時保留，否則移除
- Anchor ID 使用英文 kebab-case：`#operate-{module}-{feature}-{section}`
- 所有 `.md` 連結需包含副檔名
- Frontmatter `related`/`prerequisites` wikilink 使用目標文件的英文檔名 stem（不含副檔名），例如 `"[[manage-product-tags]]"`，而非 `title:` 值或相對路徑

## 參考資料章節規範

- 從 `後續操作` grid cards 提取非操作類連結時，改置於文末 `## 參考資料`
- 參考資料使用純 bullet（非 grid card），無 icon、無 `__bold__`、無 `data-preview`、無描述文字
- 位置：文件最尾端（`## 常見問題` 之後）

## 禁止內容規範

以下資訊**不可寫入**教學或參考文件：

| 類型 | 說明 | 範例 |
|:-----|:-----|:-----|
| 收費資訊 | 任何費率、單價、計費標準、費用表格 | 「每封 NT$1」「1 Cyber 幣」「70 字計費」 |
| 運費資訊 | 運費數字、運費計算公式、含運費欄位的截圖 | 託運單確認視窗、單號使用紀錄截圖 |
| 內部資訊 | 僅供內部查看的方案差異、加值功能對照、API 細節 | `{% if is_internal %}` 區塊內容 |
| 私人通訊 | 客服對話、內部通訊內容 | Slack 訊息、客服回覆截圖 |
| 舊版方案名稱 | 已停用的方案命名 | 達人版、尊爵版、旗艦版、白金版 |

**允許保留的相關內容**：
- 操作前提（如「需先儲值 Cyber 幣」「PLUS/企業版不須額外儲值」）
- 字數限制與拆分機制等操作提醒（如「上限 70 字」「將拆分為多封」）
- UI 欄位說明（如紀錄頁的「費用」欄位名稱）
- 「客製化」作為操作動詞（如「客製化官網頁面」）

## 常見注意事項
- `last_modified` 於每次編輯後更新為 `YYYY-MM-DD HH:mm`
- `permalink` 預設為空，使用前需產生
- frontmatter `icon` 使用 `lucide/` 或 `simple/` 前綴

## Tabbed Content 與圖片慣例

### 其他版面設計 pattern
區塊設定中若有「其他版面設計」面板，應使用獨立 step 描述：

```markdown
2. 點擊 **其他版面設計**，設定以下項目：

    - **文字排版**：選擇文字對齊方式（靠左／置中／靠右）。
    - **文字**：設定文字顏色（點色塊選色）。
    - **背景**：設定區塊背景顏色。

    === "電腦版"

        - **版面左右外邊距**：設 0px 即滿版（預設 0px）。
        - **版面底部外邊距**：與下方區塊的距離（預設 0px）。

        ![電腦版-版面邊距](../../../assets/images/{filename})

    === "平板版、手機版"

        - **版面左右外邊距**：同電腦版（預設 0px）。
        - **版面底部外邊距**：同電腦版（預設 0px）。

        ![平板手機版-版面邊距](../../../assets/images/{filename})
```

### 圖片縮排規則
| 位置 | 縮排 |
|------|------|
| Tab 內圖片 | 8-space（tab 4 + content 4） |
| Bullet list 後圖片 | 4-space（list continuation） |
| Step 後圖片（非 nested） | 無縮排（頂層） |

### Simple Grid Card
簡單的 grid card 格式：icon 與 title 在同一行，無描述文字：

```markdown
<div class="grid cards" markdown>

- :lucide-icon:{ .lg } [__Title__](link.md){ title="Title" }

</div>
```
