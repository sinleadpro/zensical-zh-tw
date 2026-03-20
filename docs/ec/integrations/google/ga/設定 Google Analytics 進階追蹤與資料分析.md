---
title: "設定 Google Analytics 進階追蹤與資料分析"
description: "" 
created: "2026-03-20 17:50"
last_modified: 
lang: zh-TW
type: tutorial
status: ""
version: ""
author: Jase
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
tags: []
acoiv: ""
apis: []
devices: 
  - desktop 
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/chart-bar
hide:
---

# 設定 Google Analytics 進階追蹤與資料分析


{ .subtitle }

{ .doc-badge }

{ .hero-page }

## Google Analytics 進階資料分析說明

在完成 Google Analytics 4 (GA4) 與網站的基礎串接後，GA4 會開始記錄基本的流量資訊。若您希望深入分析網站流量與更精確的使用者輪廓，建議依照以下說明進行進階設定與調整。

以下為 **Google Analytics 進階資料分析設定** 的詳細教學：

## 加強型評估 (Enhanced Measurement)

這是 GA4 內建的自動追蹤功能，開啟後無需額外埋設程式碼，系統即可記錄使用者在網站上的多種互動行為。

*   **追蹤內容：** 包含網頁瀏覽、捲動頁面、點擊外部連結、站內搜尋、填寫表單、觀看影片及下載檔案。
*   **設定路徑：** 在 GA4 後台點選「管理」→「資料收集與修改」→「資料串流」→ 選擇您的串流 →「事件」→「加強型評估」開關開啟。
*   **進階設定：** 點擊齒輪圖示 (⚙️) 可依需求選擇要評估的特定事件。

## Google 信號 (Google Signals)

當使用者登入 Google 帳戶並開啟「廣告個人化」時，此功能可協助系統取得跨裝置、跨平台的使用行為資料，補足跨裝置的使用者視角。

*   **主要功能：** 性別、年齡、興趣等目標客群輪廓描繪，以及再行銷名單的建立。
*   **設定路徑：** 在 GA4 後台點選「管理」→「資源設定」→「資料收集與修改」→「資料收集」→ 在「Google 信號資料收集」區域點擊「啟用」。

## 資料保留 (Data Retention)

GA4 預設的資料保留期限僅有 2 個月，對於需要觀察長期趨勢或建立再行銷名單的商家來說較為不足。

*   **建議調整：** 將資料保留期限延長至 **14 個月**。
*   **設定路徑：** 在 GA4 後台點選「管理」→「資源設定」→「資料收集與修改」→「資料保留」進行更改。

## 報表識別資訊 (Reporting Identity)

此技術可協助商家排除重複計算的使用者，例如同一位顧客先用手機瀏覽再用電腦下單，GA4 可將其辨識為同一使用者。

*   **常用模式：**
    *   **混合 (Mixed)：** 綜合所有可用訊號（User ID、Google 信號、裝置 ID），提供最完整的分析。
    *   **已列為觀察項目 (Observed)：** 僅使用實際觀察到的裝置資訊，報表結果較為保守貼近原始紀錄。
*   **設定路徑：** 在 GA4 後台點選「管理」→「資源設定」→「資料顯示」→「報表識別資訊」。

## 數據準確度優化：排除內部流量與不適用連結

為了避免數據偏差，建議排除公司內部人員的瀏覽紀錄以及外部金物流網址的干擾。

*   **定義與排除內部流量：** 
    *   需先在「資料串流」中「進行代碼設定」下定義代表內部流程的 IP 位址。
    *   再前往「管理」→「資料收集與修改」→「資料篩選器」將預設的 Internal Traffic 狀態改為「有效」並儲存。
*   **列出不適用的參照連結網址：**
    *   將金物流服務商（如 `cyberbizpay.com`、`pay.ecpay.com.tw`、`web-pay.line.me`、超商地圖連結等）加入排除名單，以免轉換來源被誤判為這些第三方頁面。

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

