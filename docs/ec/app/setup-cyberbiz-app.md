---
title: CYBERBIZ APP 建置與管理
description: CYBERBIZ APP 上架前的環境準備、官網預建置，以及門市地圖與推播通知的後台設定方式。
created: 2026-08-17 12:06
last_modified: 2026-08-17 12:06
lang: zh-TW
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
  - POS
modules: 
  - APP 功能
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 建置_CYBERBIZ_APP
  - 設定_APP_門市地圖
  - 設定_APP_推播通知
features: 
  - APP_門市列表
  - APP_推播通知
  - 通知樣板
  - 活動推播
prerequisites: 
  - ec/app/apply-apple-developer-account/
  - ec/app/cyberbiz-app-feature-overview/
  - ec/products/create-and-manage/create-update-products/
  - ec/marketing/
  - ec/website-appearance/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/payments-and-logistics/
  - ec/integrations/google/setup-google-quick-login/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/fb/setup-facebook-quick-login/
related:
  - ec/app/apply-apple-developer-account/
  - ec/products/create-and-manage/create-update-products/
  - ec/marketing/
  - ec/website-appearance/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/payments-and-logistics/
  - ec/integrations/google/setup-google-quick-login/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/fb/setup-facebook-quick-login/
tags: 
  - 門市地圖
  - 推播通知
  - CYBERBIZ APP
acoiv: configure
apis: []
devices: []
ui_components: 
  - APP門市列表
  - 新增門市
  - 通知樣板
  - 活動推播列表
  - 新增推播
paths: 
  - APP 功能 > APP門市列表
  - APP 功能 > APP推播通知設定 > 通知樣板
  - APP 功能 > APP推播通知設定 > 活動推播列表
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app/setup-cyberbiz-app/"
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---

# CYBERBIZ APP 建置與管理
CYBERBIZ APP 上架前的環境準備、官網預建置，以及門市地圖與推播通知的後台設定方式。
{ .subtitle }

[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions.md#適用擴充) | CYBERBIZ APP
{ .doc-badge }

## 使用須知

- 歡迎洽詢 CYBERBIZ 開店顧問，了解更多方案資訊。

## APP 環境準備
  
CYBERBIZ APP 支援上架於 Apple Store(iOS) 與 Google Play(Android)，請依上架需求進行環境設定。  
  

- **上架Apple Store**：請您[申請 Apple 開發者帳號，並授權 CYBERBIZ](apply-apple-developer-account/)。
- **上架Google Play**：由 CYBERBIZ 提供 Google開發者帳號，無需自行申請。


## 官網預建置
  
官網 App 將完整承襲網頁版的視覺設定與商品資料，在開啟 App 旅程前，請先確認您的網站已完成以下核心建置，以確保 App 在上架時即具備完整的購物功能：  
  

- [x] **[商品上架](../products/create-and-manage/create-update-products.md)**：確保店內已有豐富商品供消費者選購。
- [x] **[行銷機制](../marketing/index.md)**：完成紅利點數、優惠券(碼)等會員福利設定。
- [x] **[視覺介面](../website-appearance/index.md)**：建置並確認官網前台外觀佈局。
- [x] **動線規劃**：完成官網 [導覽列設定](../website-appearance/navigation/setup-menus-navigation.md)，確保導航流暢。
- [x] **[金物流啟用](../payments-and-logistics/index.md)**：確認支付與配送管道已完成串接並正式啟用。
- [x] **社群登入**：建立 [Google](../integrations/google/setup-google-quick-login.md)、[LINE](../integrations/line/account-integration/setup-line-quick-login.md)、[Meta](../integrations/fb/setup-facebook-quick-login.md) 快速登入，提供便捷的會員體驗。


## 建立 APP 門市地圖

  
登入電商官網後台，前往 **APP 功能 > APP門市列表** ，您可設定在 APP 中展示實體門市資訊，方便顧客查詢。  
  

1.  **啟用功能**：點擊 ON/OFF 按鈕。
2.  **新增門市**：於右上角點擊 **新增門市**。
3.  **選擇資料來源**：選擇 **自訂門市** 或 **POS 商店**。
    *   若您同步使用 CYBERBIZ POS 系統，可選擇 **POS 商店**，一鍵帶入門市資訊。
4.  **填寫門市資訊：**
    *   **門市電話**：輸入該門市的聯絡電話。
    *   **門市地址**：輸入完整地址，這將影響地圖定位的準確性。
    *   **備註**：可填寫營業時間或交通指南。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP門市列表-單筆新增門市01.png)

## 大量匯入門市名單

1.  **下載 Excel 範本**：點擊 **下載 Excel 範例**。
2.  **輸入門市資訊**：開啟範本檔案，新增門市資訊。
3.  **匯入檔案**：點擊 **匯入自訂店家**，上傳檔案。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP門市列表-批次匯入門市01.png)


## APP 預設通知開關

前往 **APP 功能 > APP推播通知設定 > 通知樣板**，您可設定系統自動觸發的通知（如訂單成立、出貨通知等）是否啟用。  
  

1.  **切換開關**：點擊右側的 ON/OFF 按鈕。當按鈕顯示為藍色 ON 時，系統將會在該事件觸發時自動發送推播給顧客。
    *   **訂單相關**：如 **訂單成立通知**、**付款成功通知** 等。
    *   **物流配送相關**：如 **貨物發送通知**、**貨物到店通知** 等。
    *   **顧客相關**：如 **會員生日紅利通知**、**優惠券即將到期通知** 等。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP推播通知設定-系統通知樣板01.png)



## 發送 APP 推播訊息

前往 **APP 功能 > APP推播通知設定 > 活動推播列表**，您可建立推播活動，自定義發送會員群體與發送時間 ，主動向 APP 使用者發送行銷或公告訊息。  
  
1.  **新增活動**：點擊 **新增推播**。
2.  **推播基本設定：**
    *   **推播標題**：輸入吸引人的標題
    *   **推播內容**：輸入詳細訊息內容
    *   **推播圖片**：點擊或拖拽上傳圖片
    *   **導向頁面**：選擇使用者點擊通知後要跳轉的位置。
3.  **選擇推播對象：**
    *   **全部會員**：將訊息發送給所有已註冊會員，適用於全站大型活動或重大系統公告。
    *   **會員分群**：依據您預先設定的會員分群進行推播，實現分眾精準行銷。
    *   **匯入 Excel 檔案**：若有特定名單或臨時性的名單需求，可上傳 Excel 檔，指定欲發送的會員對象。
4.  **設定發送時間：**
    *   **預約發送**：指定日期與時間。
    *   **立即發送**：推播建立後立即發送。
5.  **查看預覽效果**：可於右方預覽推播畫面。
    *   **系統推播**：手機鎖定螢幕桌布的彈窗通知
    *   **通知列表**：APP 小鈴鐺通知的動態快訊
    *   **推播導向**：點擊通知導往的落地頁面

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP推播通知設定-新增推播活動01.png)

從建立活動到發送後的管理，系統提供兩大核心工具幫助您優化流程：  
  
*   :lucide-send: **樣式預覽**：提供 **先行測試** 功能，讓您在正式推播前確認訊息外觀，確保內容精準傳達。
*   :lucide-copy: **活動複製**：支援 **一鍵複製** 現有活動，僅需微調資訊即可快速再次發布，大幅提升操作效率。


![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APP功能-APP推播通知設定-複製與測試推播活動01.png)