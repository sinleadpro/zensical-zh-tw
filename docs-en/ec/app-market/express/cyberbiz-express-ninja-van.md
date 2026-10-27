---
title: "CYBERBIZ EXPRESS Ninja Van Home Delivery (Singapore/Malaysia)"
description: "Learn how to turn on Ninja Van home delivery for Singapore and Malaysia, set up logistics, create consignment notes, print documents, and track shipments."
created: 2026-10-13 10:56
last_modified: 2026-10-13 10:56
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - APP MARKET
  - 訂單
sites: 
  - SG
  - MY
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans: 
  - global_advanced
plan_options: []
cyb_extensions: 
  - EXPRESS
intents: 
  - 設定_Ninja_Van_物流
  - 建立跨境託運單
  - 查詢跨境貨態
features: 
  - Ninja_Van_宅配
  - 新加坡跨境配送
  - 馬來西亞跨境配送
prerequisites: 
  - 需安裝 CYBERBIZ EXPRESS APP
related: 
  - ec/app-market/express/order-tracking-and-query/
tags: []
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 物流管理
  - 建立託運單
  - 補印託運單
  - 物流單號
paths: 
  - APP MARKET > 我的擴充服務 > CYBERBIZ EXPRESS > 物流管理
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/express/cyberbiz-express-ninja-van/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

# CYBERBIZ EXPRESS Ninja Van Home Delivery (Singapore/Malaysia)

Learn how to turn on Ninja Van home delivery in Singapore and Malaysia, complete the logistics settings, create consignment notes, print documents, and track shipments.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../../resources/conventions#適用產品) | Cross-Border E-Commerce (Singapore Local Edition/Malaysia Local Edition)<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../../resources/conventions#適用擴充) | CYBERBIZ EXPRESS
{ .doc-badge }


## Service Overview { #intro-ninja-van }

- **Delivery Areas**: Local delivery in Singapore and Malaysia.
- **Delivery Mode**: Home delivery without payment on delivery. Customers must pay online first.
- **Prohibited Items Compliance**: You must follow the shipping rules of Ninja Van and CYBERBIZ.

## Before You Start { #prerequisites-ninja-van }

- If you have not installed the CYBERBIZ EXPRESS app, contact your store consultant first to install it and set up logistics.
- When you create a consignment note, the sender and recipient must be in the same country.
- Ninja Van does not provide customer returns. If a customer needs to return an item, contact the customer and handle it yourself.

## Turn on Ninja Van Logistics { #operate-ninja-van }

### Open the Logistics Settings { #operate-ninja-van-entry }

1. Log in to the CYBERBIZ admin and go to **APP MARKET > My Apps > CYBERBIZ EXPRESS > 物流管理**.
2. Open the logistics settings.

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS啟用ninja物流01.en.png){ .screenshot }


### Complete the Basic Logistics Settings { #operate-ninja-van-settings }

1. Select the delivery area: **Singapore** or **Malaysia**.

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS啟用ninja物流02.en.png){ .screenshot }

2. Select the checkbox to agree to the **Ninja Van Service Agreement**.
3. Fill in all sender information fields, then click **Save**.

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS啟用ninja物流03.en.png){ .screenshot }

4. Turn on the matching logistics switch.

!!! warning "You Cannot Ship Until Setup Is Complete"
    If any field is incomplete or the logistics switch is off, the delivery method does not appear and you cannot create consignment notes.

## Create and Print Consignment Notes { #operate-ninja-van-waybill }

### Create Consignment Notes { #operate-ninja-van-create }

Before you create a consignment note, the order must meet all of these conditions:

- `付款狀態` is `已收到款項`.
- `Delivery Status` is `Unshipped`.
- `退貨狀態` is `不需退貨`.
- `配送方式` is `Ninjavan`

Steps:

1. Go to **Orders > All Orders**.
2. Select the eligible orders and click **更多操作 > 建立託運單**.

    ![](../../../assets/images/EC-後台-APPMARKET-建立ninja託運單01.en.png){ .screenshot }

3. Select the shipping area for the orders and make sure the sender and recipient are in the same country.

    ![](../../../assets/images/EC-後台-APPMARKET-建立ninja託運單03.en.png){ .small-image }

4. Choose how to send the parcels:

    === "Drop Off at a Store"

        ![](../../../assets/images/EC-後台-APPMARKET-建立ninja託運單04.en.png){ .small-image }

    === "Courier Pickup"

        If you choose **Courier Pickup**, enter the pickup date, time, and notes.

        ![](../../../assets/images/EC-後台-APPMARKET-建立ninja託運單05.en.png){ .small-image }

!!! note "Pickup Details Apply Only to the Current Orders"
    Changes to pickup details in the Create Consignment Note window apply only to the current operation and do not overwrite your basic logistics settings.

### Print Documents Directly { #operate-ninja-van-print }

1. In the Create Consignment Note window, select the documents to print.
2. Click **Print Now**.

    ![](../../../assets/images/EC-後台-APPMARKET-建立ninja託運單02.en.png){ .small-image }

3. The system opens the browser print preview with documents in this order:

    ![](../../../assets/images/EC-後台-APPMARKET-建立ninja託運單06.en.png){ .screenshot }

    1. Picking list summary.
    2. Consignment notes in order sequence.
    3. Order details for each order.
    4. Shipping details for each order.


Only if you select **Shipping Label** and the consignment note is generated successfully does the order's delivery status change to `Shipped` automatically.

### Download a ZIP File at the Same Time { #operate-ninja-van-download }

1. In the Create Consignment Note window, select the documents to generate.
2. Select **Download ZIP File at the Same Time**.
3. After the consignment notes are created, the system opens the print preview and downloads a ZIP file of the selected documents.

### Reprint Consignment Notes { #operate-ninja-van-reprint }

1. Go to **Orders > All Orders**.
2. Select orders with the delivery status `Shipped`.
3. Click **更多操作 > 補印託運單**.

![](../../../assets/images/EC-後台-訂單-所有訂單-補印EXPRESS託運單01.en.png){ .screenshot }

The system filters out orders that do not use EXPRESS logistics. If you also select orders with other logistics methods, the system shows a message and skips the ineligible orders.


## Fee Settlement { #specs-ninja-van }

- When you create a consignment note, the system deducts CYBER Coins in advance based on the parcel weight.
- The system reconciles on the 5th of each month and adjusts the deducted amount based on actual shipping fees.
- For Malaysia, different fee tiers apply to East and West Malaysia.


## Track Shipments { #operate-ninja-van-tracking }

<div class="grid cards" markdown>

- :lucide-truck:{ .lg }
  [__CYBERBIZ EXPRESS Shipment Tracking and Lookup__](order-tracking-and-query.md)
  See how merchants and customers can check shipment status and shipping fees.

</div>

