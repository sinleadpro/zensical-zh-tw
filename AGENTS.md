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
