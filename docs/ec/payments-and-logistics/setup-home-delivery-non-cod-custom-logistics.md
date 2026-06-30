---
title: 建立宅配貨到不付款/自訂物流
description: 說明如何自行設定宅配物流選項、運費門檻與溫層配送，包含配送國家總開關、金額與重量運費設定，以及多溫層購物的處理邏輯。
created: 2026-06-04 10:02
last_modified: 2026-06-28 13:57
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 金物流
sites: 
  - TW
audiences: 
  - admin
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定自訂物流選項
  - 設定運費門檻
  - 配置溫層配送
  - 解決多溫層拆單問題
features: 
  - 自訂物流
  - 運費門檻
  - 多溫層配送
  - 配送國家設定
prerequisites: 
  - "需先完成金流串接設定"
related: 
  - "[[home-delivery-cash-on-delivery]]"
tags: 
  - 物流設定
  - 運費
  - 溫層
  - 配送地區
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 自訂物流列表
  - 配送國家設定
paths: 
  - 金物流 > 宅配物流 > 自訂物流
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=2746
  - https://www.cyberbiz.io/support/?p=10652
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---
# 建立宅配貨到不付款/自訂物流
「自訂物流」允許商家自行設定宅配選項與運費規則。您可以根據訂單金額或重量設定多階層運費，並支援常溫、冷藏、冷凍等不同溫層的配送需求。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 全方案適用
{ .doc-badge }


## 使用須知

**自訂物流** 介面讓商家設定「宅配貨到不付款物流」與「自訂物流」兩種選項。兩者的設定流程相同，主要差異在於訂單成立後的出貨操作方式。

下表比較兩者的功能與託運單建立方式，請根據營運需求選擇合適的物流類型。

| 物流類型 | 系統串接物流 | 說明 | 列印託運單方式 |
| ------- | ---- | ---- | ------------- |
| 宅配貨到不付款物流 | 黑貓<br>宅配通<br>順豐<br>新竹物流 | 此物流選項與系統串接，可自動更新訂單出貨後貨態 | **需使用系統託運單出貨**<br>[使用黑貓宅配出貨](../orders/home-delivery/tcat-home-delivery.md)<br>[使用宅配通出貨](../orders/home-delivery/pelican-shipping.md)<br>[使用順豐出貨](../orders/home-delivery/sf-express-shipping.md)<br>[使用新竹物流出貨](../orders/home-delivery/hct-shipping.md) | 
| 自訂物流 | - | 此物流不與系統串接，出貨後訂單貨態不予更新 | [使用自訂物流出貨](../orders/home-delivery/custom-logistic-shipping.md) | 

### 新竹物流貨到不付款場勘流程

=== "有 CYBERBIZ PAYMENTS"

    依 [新竹物流貨到付款開通申請](home-delivery-cash-on-delivery/#2-新竹物流) 流程設定。

=== "無 CYBERBIZ PAYMENTS"

    1. 前往 **金物流 > 自訂物流**，點擊 **新增自訂物流**。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-新增自訂物流01.png)

    2. 點擊 **填寫表單申請**。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-新增自訂物流02.png)

    3. 申請啟用物流。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-申請新竹物流貨到不付款01.png)

    4. 填寫申請表格並送出。
    
        - CYBERBIZ 客服人員將會通知新竹物流進行廠勘，廠勘完成後即會立刻進行開通。
        - 送出後若需要更改資料，請告知 CYBERBIZ 客服人員。
        - 開通成功後，您即可啟用物流選項並開始使用，CYBERBIZ 將會同步發送通知信告知（工作天約 7~10 天）。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-申請新竹物流貨到不付款02.png)

    !!! tip "下一步"
        啟用物流後，請依 [步驟二：新增自訂物流]()，建立一項自訂物流，可取名 **新竹物流貨到不付款**，並設定相關規則。

## 步驟一：配送國家設定（總開關）

在建立具體物流前，需先開啟目標地區的配送權限。


1. 登入電商後台，前往 **金物流 > 宅配物流 > 自訂物流**。
1. 在頁面最上方找到 **配送國家設定**。
2. 根據營運需求開啟 **台灣本島**、**台灣離島** 或 **海外**。

    > **注意**：若此處未開啟（如未開啟離島），即便下方物流設定了離島配送，顧客在結帳時仍無法選擇。

![](https://www.cyberbiz.io/support/wp-content/uploads/物流運費設定01.png){ .screenshot }



## 步驟二：新增自訂物流

點擊 **新增自訂物流** 進入設定頁面。

### 1. 基本設定

- **物流名稱**：自訂名稱（如：黑貓-常溫），名稱不得重複。
- **運送地區**：支援至「城市」階層。
- **付款方式**：勾選該物流支援付款選項。

### 2. 運費門檻設定

系統支援「訂單金額」與「訂單重量」兩種計費方式。

| 設定類型 | 說明 | 建議事項 |
| :--- | :--- | :--- |
| **訂單金額運費** | 依訂單總額設定不同區間的運費 | 建議起始金額設為 `0` 元，避免低額訂單無法結帳 |
| **訂單重量運費** | 依訂單總重量（含贈品）設定運費 | 需先在商品明細中填寫商品重量 |

!!! tip "擇優顯示原則"
    若同時設定金額與重量運費，系統會自動選擇對顧客 **最有利（收費較低）** 的方案。建議商家擇一設定以簡化管理。

![](https://www.cyberbiz.io/support/wp-content/uploads/物流運費設定03.png){ .screenshot }

## 步驟三：溫層配送配置

每個自訂物流選項僅能設定 **一個溫層**。若您有多溫層配送需求，需分別建立。

1. **建立多個物流選項**：
    - 例如：建立「自訂宅配-常溫」、「自訂宅配-冷凍」。
2. **設定商品溫層**：
    - 前往 **商品 > 所有商品 > [特定商品] > 設定**。
    - 在「溫層和物流配送設定」中勾選該商品適用的溫層。

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/物流運費設定08.png){ .screenshot }


## 多溫層購物的處理邏輯

當顧客的購物車中包含不同溫層的商品時，系統會嘗試尋找「共同溫層」以避免拆分購物車。

- **情境 A（可合併）**：
    - 商品 1：支援「常溫、冷藏」。
    - 商品 2：支援「冷藏」。
    - **結果**：系統會以「冷藏」運送，兩者放在同一個購物車。
- **情境 B（需拆分）**：
    - 商品 1：僅支援「常溫」。
    - 商品 2：僅支援「冷凍」。
    - **結果**：系統會將購物車拆分為兩個，分別計算運費。


## 常見問題

??? quote "為什麼我設定了運費，結帳時卻顯示免運？"
    請檢查是否開啟了「重量運費」但商品未設定重量（預設為 0），或運費區間設定有誤。

??? quote "為什麼新增了金流（如街口支付）後，自訂物流選不到？"
    新增金流後，必須回到 **自訂物流 > 編輯 > 付款方式** 中，將新增的項目勾選起來並儲存。

??? quote "自訂物流可以設定「不配送」特定地區嗎？"
    可以。在「運送地區」設定中，僅勾選欲配送的城市即可。未被勾選的地區，顧客在填寫地址後將無法選擇該物流。

