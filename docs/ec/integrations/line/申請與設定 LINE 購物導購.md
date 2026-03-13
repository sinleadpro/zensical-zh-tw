---
title: "申請與設定 LINE 購物導購"
description: "" 
created: "2026-03-13 10:46"
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
icon: lucide/shopping-bag
hide:
---

# 申請與設定 LINE 購物導購


{ .subtitle }

{ .doc-badge }

{ .hero-page }

## LINE 購物說明

**LINE 購物**是一個結合導購、點數回饋、比價的電商平台。透過將官網與 LINE 購物串接，商家可以利用 LINE 購物 APP 或其官方帳號入口，將顧客導購至官網下單。

以下為 LINE 購物的申請流程、後台設定及相關注意事項：

## 申請開通流程

1.  **填寫申請表**：商家需先填寫申請表以取得更多資訊，後續將有 LINE 專人聯繫說明。
2.  **資格審核**：由 LINE 進行前期接洽與資格審核，審核通過後 LINE 會通知 CYBERBIZ 開通資格。
3.  **開啟協助權限**：商家需在 CYBERBIZ 後台開啟協助權限，以便專員協助設定參數。
    *   **路徑**：「管理中心」>「網站權限/續約管理」>「管理者列表」。
4.  **填入參數**：CYBERBIZ 專員會協助將 LINE 提供之 **「SHOP_ID」** 與 **「AUTHKEY」** 填入系統中。
    *   **路徑**：「第三方整合」>「LINE購物設定」> 頁面上半區塊「LINE購物」。

## 商品串接邏輯與條件

商品必須同時符合以下三個條件，才會成功出現在產品目錄中：
*   **狀態為「公開」**。
*   **狀態為「已上架」**。
*   **標籤排除**：商品標籤內 **不得** 設有「贈品」或「排除product feed」之關鍵字。

## 目錄更新與同步時間

*   **自動更新**：CYBERBIZ 後台產品目錄於 **每日 4:45 AM 及 4:45 PM** 自動產出；LINE 則於 **每日 5:00 AM** 將資訊同步至其後台。
*   **手動更新**：若需即時同步修改的商品資訊，可至「LINE 購物設定」點擊 **「手動更新目錄」** 按鈕（每小時限點擊一次）。
*   **前置作業**：建議最晚於直播或活動 **一天前** 完成所有商品設定，以確保目錄能順利同步。

## 訂單查看與管理

*   **訂單歸類**：透過 LINE 購物導購完成的訂單，可於 **「訂單」>「LINE 購物訂單」** 中查看。
*   **導購來源追蹤**：商家也可在匯出的訂單報表中查看「導購來源」欄位，確認訂單是否來自 LINE 購物。

## 重要提醒

*   **適用版本**：此功能僅提供給 **PLUS 版及企業版** 用戶使用。
*   **開放平台性質**：LINE 購物為公開平台，消費者無須是商家的 LINE 官方帳號好友，也無須綁定 OA，即可進行下單。
*   **精準搜尋商品**：於 LINE 直播或相關後台搜尋商品時，建議使用 **Product ID (PID)** 最為精準。PID 可在商品編輯網址最後方的數字或匯出的商品報表中取得。


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

