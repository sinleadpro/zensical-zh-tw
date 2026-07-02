---
title: 文字編輯器對照表
description: 彙整文字編輯器的斜線指令、YouTube 影片設定選項與圖片規格，供編輯內容時快速查閱。
created: 2026-06-30 15:19
last_modified: 2026-07-02 16:02
lang: zh-TW
type: reference
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans: []
cyb_extensions: []
feature_badges: []
intents: []
features: []
prerequisites: []
related:
  - "[[text-editor]]"
tags:
  - 文字編輯器
  - 斜線指令
  - YouTube
  - 圖片規格
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: https://help.cyberbiz.io/ec/website-appearance/references/text-editor-toolbar/
comments: false
search:
  exclude: false
icon: lucide/table
hide: []
---

本頁集中收錄文字編輯器的對照表，供「[文字編輯器](../code-customization/text-editor.md)」等內容編輯說明引用。

### 斜線指令對照表 { #reference-text-editor-slash-commands }

新版文字編輯器中，於內文輸入「/」即可叫出快捷選單，輸入關鍵字可快速篩選。

| 指令選項 | 用途 |
| :-- | :-- |
| 正文 | 將該段落改回一般內文樣式 |
| 標題 1 ～ 標題 6 | 套用不同層級的標題樣式 |
| 表格 | 插入表格，亦可直接輸入如 `3x4` 指定列數與行數 |
| 編號清單 | 插入有序號的清單 |
| 項目符號清單 | 插入無序號的條列清單 |
| 引用 | 插入引言區塊 |
| 水平線 | 插入一條分隔用的水平線 |
| 圖片 | 開啟圖片插入視窗 |
| YouTube 影片 | 開啟 YouTube 影片嵌入視窗 |
| 特殊符號 | 插入箭頭、貨幣、數學等特殊符號 |
| 表情符號 | 插入 emoji 表情符號 |

!!! note "註釋"
    * 此功能為新版文字編輯器專屬，舊版編輯器請改用上方工具列的對應按鈕。
    * 輸入「/」後可接著打字（例如輸入英文 `table`）快速篩選想要的指令。

### YouTube 影片設定對照表 { #reference-text-editor-youtube-options }

插入 YouTube 影片時可設定的選項：

| 選項 | 說明 |
| :-- | :-- |
| 貼上 Youtube 影片 URL | 影片來源連結，僅支援 YouTube 網址 |
| 寬度／高度 | 影片顯示的尺寸（未勾選自適應縮放時生效） |
| 開始時間 | 影片從指定時間點開始播放，格式為 `ss`、`mm:ss` 或 `hh:mm:ss` |
| 播放清單 ID | 嵌入整個播放清單時填入 |
| 使用自適應縮放模式 | 忽略設定的長寬，以寬度為基準自動縮放，手機等裝置上維持比例 |
| 自動播放 | 進入頁面時自動播放（需同時勾選「靜音」才會生效） |
| 循環播放 | 影片播畢後自動重播 |
| 靜音 | 影片預設靜音播放 |
| 顯示播放器控制 | 是否顯示播放／暫停等控制列 |
| 影片結束時顯示建議影片 | 播畢後是否顯示 YouTube 推薦影片 |
| 啟用加強隱私模式 | 以加強隱私模式嵌入影片 |

!!! note "註釋"
    * 依 YouTube 規範，「自動播放」必須搭配「靜音」才能成功觸發。
    * 勾選「自適應縮放」後，設定的固定寬高會被忽略，改以寬度為基準縮放。

### 圖片規格對照表 { #reference-text-editor-image-specs }

| 項目 | 規格 |
| :-- | :-- |
| 支援格式 | JPG、JPEG、PNG、GIF、TIFF、WebP |
| 尺寸上限 | 寬度 5000px、高度 7000px，超過無法上傳 |
| 自動最佳化 | 上傳後自動產生最寬 1280px 的版本以加速前台載入 |
| GIF 處理 | 維持原圖，不進行壓縮 |
| 儲存空間 | 受方案儲存空間限制，空間已滿時無法上傳 |

!!! note "註釋"
    * 圖片超過尺寸上限時，系統會顯示「圖片最大寬度為 5000px，最大高度為 7000px。」。
    * 製作長幅產品圖建議：單張長圖建議寬度 1000px、長度不限；多張拼接建議統一為 1000px × 1000px。
