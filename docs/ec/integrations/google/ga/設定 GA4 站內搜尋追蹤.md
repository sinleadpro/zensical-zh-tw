---
title: 設定 GA4 站內搜尋追蹤
description: ""
created: 2026-03-24 20:05
last_modified:
lang: zh-TW
type: tutorial
status: ""
author: Jase
version: ""
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12099
  - https://www.cyberbiz.io/support/?p=28483
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/search-code
hide:
---

{ .subtitle }

{ .doc-badge }

{ .hero-page }

## GA4 站內追蹤說明

開啟 **Google Analytics 4 (GA4)** 的站內搜尋追蹤功能，可以協助商家觀察使用者在網站上輸入的關鍵字，進而了解消費者的資訊需求與查找意圖。

## GA4 站內搜尋設定步驟

請登入您的 Google Analytics 後台，並依循以下路徑操作：

1.  **進入設定頁面**：點選左下角「管理」→「資源設定」→「資料收集和修改」→「**資料串流**」，並選擇您官網綁定的串流。
2.  **開啟加強型評估**：在「事件」區塊中找到「**加強型評估**」，點擊右側的齒輪圖示 (⚙️) 進入設定。
3.  **啟用站內搜尋**：找到「**站內搜尋**」項目並將開關開啟。
4.  **設定查詢參數**：點擊「**顯示進階設定**」，在「搜尋字詞查詢參數」欄位中輸入：`q,s,search,query,keyword`（請以半形逗號分隔），完成後儲存設定。

## 如何查看追蹤成果

設定完成後（且有使用者執行搜尋動作），您可以在 GA4 報表中查看結果：

1.  **即時報表檢視**：前往「報表」→「即時」或「即時總覽」，在「**事件計數**」區塊中尋找 `view_search_results` 事件。
2.  **查看關鍵字內容**：點擊 `view_search_results` 事件後，再點擊 `search_term` 參數，即可瀏覽使用者在官網上曾查詢過的**關鍵字紀錄**與搜尋次數。

## 重要注意事項

*   **數據不回溯**：GA4 僅會從功能開啟後才開始記錄行為，無法追蹤串接或設定前的歷史紀錄。
*   **串接前提**：您的官網必須已正確串接 GA4 代碼（評估 ID），系統才能收集到數據。
*   **資料延遲**：若短時間內沒有人進行搜尋，該事件可能不會顯示資料；您可以自行在官網前台執行搜尋動作來進行測試。

您是否需要我為您說明，如何利用 GA4 的「**探索**」功能建立更詳細的自訂搜尋關鍵字報表？

## 後續操作

<div class="grid cards" markdown>

- :lucide-import:{ .lg }
  [____]()
  。

- :lucide-ban:{ .lg }
  [____]()
  。

</div>

## 常見問題

??? quote ""

