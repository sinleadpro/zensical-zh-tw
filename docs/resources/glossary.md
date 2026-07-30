---
title: 詞彙表
description: 收錄 CYBERBIZ 系統專業詞彙的定義與說明，涵蓋商品管理、訂單物流、行銷分析、平台方案等面向。每個詞彙附有英文註解與相關文件參閱連結。
icon: lucide/book-marked
last_modified: 2026-07-15 13:30
type: reference
author: Jase
tags:
  - EC
  - POS
  - WMS
  - SEO
  - GA4
  - Glossary
  - 詞彙表
  - 系統名詞
permalink: "https://help.cyberbiz.io/resources/glossary/"
---
<!-- [PDF :lucide-download:](#){ .md-button .md-button--primary } -->

## 商品

### 商品資訊

商品在系統中的所有設定屬性與內容，包含基本設定、圖片、影片與款式管理，用於前台展示、銷售與行銷應用。

- **參閱**：[使用商品管理介面管理商品](../ec/products/create-and-manage/product-management-interface.md){ title="使用商品管理介面管理商品" }

### 商品名稱

商品建立時的必要欄位之一，用於識別並展示商品的主要標題，會同步顯示於商品頁面、訂單明細、行銷活動與報表中。

- **參閱**：[新增與更新商品](../ec/products/create-and-manage/create-update-products.md){ title="新增與更新商品" }

### 商品標語

顯示於商品頁面的簡短文字，用於快速傳達商品賣點或活動訊息。

- **參閱**：[編輯商品簡述與商品標語](../ec/products/create-and-manage/edit-product-slogan-and-description.md){ title="編輯商品簡述與商品標語" }

### 商品簡述

顯示於商品頁面的說明文字，用於快速介紹商品重點、功能或特色，協助顧客在短時間內理解商品內容與價值。

- **參閱**：[編輯商品簡述與商品標語](../ec/products/create-and-manage/edit-product-slogan-and-description.md){ title="編輯商品簡述與商品標語" }

### 商品頁面

顧客於前台瀏覽單一商品詳細資訊的頁面，包含商品名稱、價格、圖片、規格、庫存狀態、配送方式與購買按鈕等內容。

- **參閱**：[編輯商品描述與商品設定](../ec/products/create-and-manage/edit-product-description-settings.md){ title="編輯商品描述與商品設定" }

### 商品網址

商品頁面的專屬網址，用於前台存取商品頁面與搜尋引擎索引。

### 商品連結

系統自動產生的唯一網址，可直接導向商品前台頁面，用於推廣、分享或在其他系統中快速存取指定商品。

### 圖床

用於儲存、管理並提供圖片存取連結的外部服務，讓使用者可透過網址在網站、文件或系統中引用圖片。

### 預購商品

當商品庫存歸零時，將「庫存不足時的處理」設為繼續銷售，該商品即可持續接受顧客下單，達到預購模式的效果，無需另建商品類型。

- **參閱**：[新增與更新商品](../ec/products/create-and-manage/create-update-products.md#setup-preorder-products){ title="預購商品設定" }

## 商品結構與規格

### 組合商品

由兩個或以上的子商品所組成，並以單一商品形式銷售的商品類型，具有獨立的組合售價。

- **參閱**：[新增與設定組合商品](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="新增與設定組合商品" }

### 子商品

構成組合商品的單一商品項目，具有獨立原價但在組合中不單獨販售。

- **參閱**：[組合商品](#組合商品) | [新增與設定組合商品](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="新增與設定組合商品" }

### 指定組合商品

由商家預先設定好固定組合的商品，顧客購買時無法更換組合內的項目。

- **參閱**：[組合商品](#組合商品) | [新增與設定組合商品](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="新增與設定組合商品" }

### 任選組合商品

由商家設定可選範圍的商品組合，購買者可以自由選擇組合內的子商品及數量。

- **參閱**：[組合商品](#組合商品) | [新增與設定組合商品](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="新增與設定組合商品" }

### 任選組合總數

任選組合商品中顧客需選購的子商品總數。

- **參閱**：[任選組合商品](#任選組合商品)

### 組合品價差

單個子商品因參與組合銷售而享有的價格折扣。

- **參閱**：[組合商品](#組合商品)

### 加購價格

當顧客購買符合條件的觸發商品時，可額外以此價格購買指定加價購商品。

### 規格

商品特性的分類標籤，用於區分商品的不同屬性，例如顏色、尺寸、容量、材質。

- **參閱**：[設定商品色票與款式圖片](../ec/products/create-and-manage/product-swatches-variant-images-default.md){ title="設定商品色票與款式圖片-預設版型" }

### 規格項目

特定規格下顧客可選擇的具體屬性值或選項。

- **參閱**：[規格](#規格)

### 款式

由多個規格項目組合而成的具體販售單位。

- **參閱**：[設定商品色票與款式圖片](../ec/products/create-and-manage/product-swatches-variant-images-default.md){ title="設定商品色票與款式圖片-預設版型" }

### 商品通路

用於定義商品履約來源的屬性，當同一商品需依不同倉庫、門市或供應商進行出貨時，系統可透過此設定區分對應的履約來源。

- **參閱**：[設定商品配送條件](../ec/products/shipping/setup-product-shipping-conditions.md){ title="設定商品配送條件（物流、溫層與出貨通路）" }

### 商品通路設定

定義商品的實際出貨來源或銷售通路。

- **參閱**：[商品通路](#商品通路)

### 商品關聯群組

商家可依照商品屬性或銷售策略手動設定商品之間的關聯性，以提升商品曝光與銷售效果。

- **參閱**：[新增與更新商品](../ec/products/create-and-manage/create-update-products.md#operate-product-edit-settings){ title="商品關聯群組設定" } | [商品頁面設定](../ec/website-appearance/theme-and-layout/setup-theme-page-settings.md#相關商品){ title="設定相關商品顯示" }

### Google 產品類別

指定 Google Merchant Center 動態產品饋給中的 Google 產品分類。

- **參閱**：[GMC](#gmc)

### SKU

**Stock Keeping Unit（存貨單位）**，用於識別產品的唯一代碼或編號，用於追蹤庫存、管理商品資料與銷售統計。

## 訂單、付款與物流

### 信用卡一次付清

顧客使用信用卡完成付款時，交易金額於單一帳單週期內全額請款。

### 3D 驗證

**3D Secure**，線上信用卡交易的額外身份驗證機制，持卡人在結帳時需透過簡訊一次性密碼（OTP）或銀行驗證頁面完成認證，以降低盜刷風險。

- **參閱**：[OTP](#otp)

### OTP

**One-Time Password（一次性密碼）**，由系統或銀行生成的臨時密碼，用於線上交易或身份驗證，僅可使用一次並在短時間內有效。

- **參閱**：[3D 驗證](#3d-驗證)

### COD

**Cash on Delivery（貨到付款）**，於收貨時完成付款，常見於宅配與快遞等物流配送服務。

### 配送條件

決定商品出貨與運費規則的屬性組合（如溫層、配送方式、出貨通路），影響訂單是否拆單與物流流程。

- **參閱**：[設定商品配送條件](../ec/products/shipping/setup-product-shipping-conditions.md){ title="設定商品配送條件（物流、溫層與出貨通路）" }

### 配送條件綁定

將商品明確設定為「可使用」或「僅能使用」特定的配送物流、配送溫層或出貨通路。

- **參閱**：[配送條件](#配送條件) | [設定商品配送條件](../ec/products/shipping/setup-product-shipping-conditions.md){ title="設定商品配送條件（物流、溫層與出貨通路）" }

### 配送溫層設定

定義商品可使用的配送溫層類型。

- **參閱**：[配送條件](#配送條件)

### 物流運費設定

定義系統可使用的配送物流與其運費規則。

### 正物流

商品從商家或倉儲中心配送至顧客端的物流過程，即一般出貨流程。

- **參閱**：[逆物流](#逆物流) | [訂單出貨流程](../ec/orders/basics/order-fulfillment-flow.md){ title="訂單出貨流程" }

### 逆物流

商品從顧客端回流至商家或倉儲中心的物流過程，通常包含退貨、換貨與維修等操作。

- **參閱**：[正物流](#正物流) | [訂單退貨流程](../ec/orders/order-return-process.md){ title="訂單退貨流程" }

### 退貨期限

商家規定顧客可申請退貨的最長時間範圍，自顧客收到商品起算。

- **參閱**：[處理超過退貨期限的訂單](../ec/orders/returns-refunds/overdue-return-handling.md){ title="處理超過退貨期限的訂單" }

### 上收服務

物流商根據訂單出貨需求，指派司機前往商家指定地點收取包裹的服務。

### 大宗寄倉

賣家不透過超商門市櫃台寄件，而是將整批包裹直接載往超商物流中心進行交寄的物流模式。

- **參閱**：[使用超商大宗寄倉（B2C）出貨](../ec/orders/cvs-shipping/cvs-b2c-bulk-shipping.md){ title="使用超商大宗寄倉（B2C）出貨" }

### WMS

**Warehouse Management System（倉儲管理系統）**，用於管理、控制與最佳化倉儲作業，涵蓋入庫、出庫、庫存管理、訂單揀貨與配送流程。

- **參閱**：[串倉](#串倉)

### 串倉

將電商平台（EC）與倉儲管理系統（WMS）進行串接整合的運作模式，使訂單資訊自動同步至倉儲端進行揀貨與出貨。

- **參閱**：[WMS](#wms)

### POS

**Point of Sale（銷售時點系統）**，門市進行交易時所使用的銷售作業系統，用於完成商品結帳、付款、開立收據，並同步記錄銷售資料、庫存變化與營收資訊。

## 行銷與成長

### 優惠券

一種歸戶型（會員專屬）行銷工具，系統將優惠憑證指派給特定會員帳戶，用於提供折扣、免運費或贈品等優惠。

- **參閱**：[優惠碼](#優惠碼)

### 優惠碼

一組可輸入的折扣序號，作為不歸戶型行銷工具，用於提供折扣、免運費或贈品等優惠。

- **參閱**：[優惠券](#優惠券)

### EDM

**Electronic Direct Mail（電子行銷郵件）**，許可式電子行銷郵件，商家向大量特定受眾發送具備精美排版與成效追蹤功能的行銷資訊。

- **參閱**：[設定與發送 EDM 電子報](../ec/notifications/send-edm-newsletters-v2.md){ title="設定與發送 EDM 電子報" }

### SEO

**Search Engine Optimization（搜尋引擎最佳化）**，用於提升網站在搜尋引擎中的可見度與排名。

### GA

**Google Analytics**，由 Google 提供的網站流量分析工具，用於追蹤與分析使用者在網站上的行為與互動情況。

- **參閱**：[GA4](#ga4)

### GA4

**Google Analytics 4**，Google Analytics 的最新版本，以事件為基礎的分析模型，可提供更強大的跨平台分析能力與隱私保護功能。

- **參閱**：[GA](#ga)

### GSC

**Google Search Console**，Google 提供的免費網站管理工具，用於監測網站在 Google 搜尋中的表現、檢視索引狀態並診斷 SEO 問題。

- **參閱**：[SEO](#seo)

### GMC

**Google Merchant Center**，Google 提供的商品資料管理平台，用於儲存、驗證並提交電商商品資料，讓商品顯示於 Google 生態系各項服務中。

- **參閱**：[Google 產品類別](#google-產品類別)

### MBE

**Meta Business Extension**，Meta 提供的商家整合工具，可一次串接 Facebook Conversions API、Pixel、商品目錄、Instagram Shopping 及 Facebook 粉絲專頁等資產。

### FBE

**Facebook Business Extension**，MBE 的舊稱。

- **參閱**：[MBE](#mbe)

### 分潤

商品或服務銷售後，平台或商家按事先設定的比例將收入分配給合作方或相關權益人。

- **參閱**：[了解分潤功能](../ec/profit-sharing/index.md){ title="了解分潤功能" }

### CTR

**Click-Through Rate（點擊率）**，看到網頁連結的人當中實際點擊進入網站的比例。

### SERP

**Search Engine Results Page（搜尋引擎結果頁）**，使用者在搜尋引擎輸入關鍵字後所看到的結果清單畫面。

- **參閱**：[SEO](#seo) | [GSC](#gsc)

### OG image

**Open Graph Image**，當網頁連結被分享到社交媒體平台時，該平台自動抓取並顯示的代表性圖片，用於吸引用戶注意並提高點擊率。

### LAP

**LINE Ads Platform**，LINE 提供的成效型廣告投放平台。

- **參閱**：[LINE OA](#line-oa)

### GTM

**Google Tag Manager**，免費的標籤管理系統，可在不更動網站原始碼的情況下快速部署與更新各類行銷追蹤標籤。

- **參閱**：[GA4](#ga4)

### CPA

**Cost Per Action**，廣告效益指標，計算方式為「廣告總花費 ÷ 轉換次數」。

### UTM

**Urchin Tracking Module**，在 URL 末端附加的追蹤參數，用於分析使用者進入網站的具體路徑與來源。

### ROAS

**Return on Ad Spend（廣告投資報酬率）**，衡量廣告投放效益的指標，數值越高代表廣告效益越好。

### LINE OA

**LINE Official Account（LINE 官方帳號）**，企業或品牌在 LINE 平台上開設的專屬帳號，用於與顧客互動、發送行銷訊息及提供客戶服務。

- **參閱**：[LAP](#lap)

### LIFF

**LINE Front-end Framework**，在 LINE APP 內運行網頁應用的框架。

- **參閱**：[LINE OA](#line-oa)

## 平台、方案與其他

### 一般版

專業、高手、進階方案版本。

- **參閱**：[PLUS版](#plus版)

### PLUS版

**PLUS Plan**，專業版、進階 PLUS 版、高手 PLUS 版方案。

- **參閱**：[一般版](#一般版)

### PLUS版以上

**PLUS Plan and above**，專業PLUS版、進階PLUS版、高手PLUS版、企業版及以上方案。

- **參閱**：[PLUS版](#plus版) | [高手版以上](#高手版以上)

### 高手版以上

高手版、專業PLUS版、進階PLUS版、高手PLUS版、企業版及以上方案。

- **參閱**：[PLUS版](#plus版) | [進階方案以上](#進階方案以上)

### 進階方案以上

包含進階、高手、專業PLUS、進階PLUS、高手PLUS 與企業方案。

- **參閱**：[一般版](#一般版) | [PLUS版](#plus版) | [高手版以上](#高手版以上)

### Cyber幣

**Cyber Coin**，CYBERBIZ 系統內用於支付金物流相關服務費用及特定系統功能的虛擬計費點數。

### EC

**E-commerce（電子商務）**，透過網際網路進行商品或服務的展示、交易、付款與出貨等商業活動的整體系統與營運模式。

### B2C

**Business to Consumer**，商家直接將商品或服務銷售給最終消費者的商業模式。

- **參閱**：[C2C](#c2c) | [EC](#ec)

### C2C

**Consumer to Consumer**，消費者之間進行商品或服務交易的商業模式。

- **參閱**：[B2C](#b2c) | [EC](#ec)

### 分票

將單一 QR Code 拆分為多個可獨立使用的票券，每張分出的票券皆可被單獨使用或轉贈他人。

### 註解程式碼

使被註解符號包覆的程式碼不會被執行，用於暫時停用功能、方便測試或調整，同時保留原始程式碼便於日後恢復。

### UID

**Unique Identifier（唯一識別碼）**，分配給單一實體（如使用者、裝置、訂單或檔案）的唯一字串或數字，用於確保精確識別而不產生歧義。

### 2FA

**Two-Factor Authentication（雙重驗證）**，一種安全驗證機制，除了密碼外還需提供第二層驗證資訊（通常為手機動態碼），以防止他人輕易登入。

### RWD

**Responsive Web Design（響應式網頁設計）**，讓網站能自動適應不同裝置的螢幕尺寸（桌機、平板、手機），提供一致且易於閱讀的操作體驗。

- **參閱**：[切換編輯頁面與預覽](../ec/website-appearance/theme-and-layout/theme-editor.md#operate-theme-editor-preview){ title="切換編輯頁面與預覽" }
