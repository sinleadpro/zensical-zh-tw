---
title: 設定 Apple Pay
description: 透過 CYBERBIZ PAYMENTS 啟用並設定 Apple Pay 為支付選項，提供快速安全的交易。
created: 2026-01-26 00:00
last_modified: 2026-03-08 23:50
lang: zh-TW
type: tutorial
status:
version:
author:
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - payments-and-logisitcs
sites:
  - TW
audiences:
  - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions:
  - PAYMENTS
intents:
  - 如何設定 Apple Pay
  - Apple Pay 付款設定
features:
  - Apple Pay
  - CYBERBIZ PAYMENTS
  - 金流串接
prerequisites:
  - 已開通 CYBERBIZ PAYMENTS
related: []
tags:
  - Apple Pay
  - Payments
  - CYBERBIZ PAYMENTS
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=40622
permalink:
comments: false
search:
  exclude: false
icon: simple/applepay
hide: []
---

# 設定 Apple Pay
啟用 Apple Pay 支付選項，為顧客提供快速、安全且便捷的支付方式。
{ .subtitle }

[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | CYBERBIZ PAYMENTS
{ .doc-badge }

![](../../assets/images/ec-payments-apple-pay.zh-tw.png){ .hero-page }

## 為什麼使用 Apple Pay

- **加速結帳**：消費者無需手動輸入信用卡資訊，直接透過手機付款。
- **改善體驗**：降低結帳摩擦，提高轉換率。
- **強化安全性**：透過 Touch ID / Face ID 驗證交易。 
- **自動啟用**：開通 CYBERBIZ PAYMENTS 後自動啟用 Apple Pay。
- **費用透明**：費率與信用卡一次付清相同，無額外手續費。


## 前置條件

- [x] 已 [開通 **CYBERBIZ PAYMENTS**](申請 CYBERBIZ PAYMENTS)

## 使用須知

### 裝置與瀏覽器限制

- **必要條件**：Apple 裝置 + Safari 瀏覽器
    
- 不符合條件的裝置不會顯示 Apple Pay 選項
- 支援裝置清單：[Apple 官方文件 :lucide-external-link:](https://support.apple.com/zh-utw/102896)
    
### 付款限制

- **支援**：一次付清
- **不支援**：分期付款（需使用信用卡分期）
    
### 費用

- 與信用卡一次付清相同
- 無額外手續費或年費

### 退款

- 流程與信用卡相同

## 操作步驟

Apple Pay 通常隨 CYBERBIZ PAYMENTS 自動啟用，可在後台調整可用性與交易門檻。

1. 登入 CYBERBIZ 後台，前往 **金物流 > 金流設定**。
2. 在 CYBERBIZ PAYMENTS 區塊，點擊 **:material-file-document-edit-outline: 編輯** 進入編輯頁面。 
3. 在 Apple Pay 設定區塊：
    
    - **切換開啟/關閉** Apple Pay 
    - **設定金流門檻**：定義訂單最大/最小金額   
    
4. 儲存設定

![](../../assets/images/ec-金物流-設定 Apple Pay.gif)

## 後續步驟

<div class="grid cards" markdown>

- :lucide-shield-check:{ .lg }   
  [__設定 3D 驗證門檻__](設定信用卡 3D 驗證門檻)     
  設定交易金額門檻，設定哪些信用卡交易需要進行額外身份驗證機制，以提升交易安全。

- :lucide-ban:{ .lg }     
  [__物流限制與排除選項__](設定超商配送限制與物流排除.md)  
  設定商品的配送物流條件，限制特定物流方式於結帳流程中的顯示與使用。

</div>


## 常見問題

??? quote "Apple Pay 支援分期付款嗎？"
	不支援。Apple Pay 只能一次付清。如需分期，客戶必須選擇「信用卡分期」付款方式。

??? quote "開通 CYBERBIZ PAYMENTS 後需要另外申請 Apple Pay 嗎？"
	不需要。Apple Pay 會自動啟用，商家可在後台選擇開啟或關閉。

??? quote "為什麼客戶看不到 Apple Pay 選項？"
	可能原因：
	
	- 非 Apple 裝置
	- 非 Safari 瀏覽器
	- 後台已關閉 Apple Pay
	- 訂單金額超出設定的門檻範圍

??? quote "Apple Pay 的費率是多少？"
	與信用卡一次付清相同，依商家與 CYBERBIZ 的合約而定，無額外費用。

??? quote "可以設定訂單金額限制嗎？"
	可以。在後台設定最小/最大訂單金額。

??? quote "Apple Pay 退款要多久？"
	退款流程與時間同信用卡，通常 7-14 個工作天。