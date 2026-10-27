---
title: "CYBERBIZ EXPRESS Japan-to-Taiwan Cross-Border Home Delivery"
description: "An all-in-one logistics service for direct cross-border delivery from Japan to Taiwan, covering activation, cross-border product customs information, and order shipping."
created: 2026-03-03 00:00
last_modified: 2026-10-13 10:40
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 跨境GL版本徽章
  - 內部連結：購物車相關設定、訂單相關設定
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - APP MARKET
  - 訂單
sites:
  - JP
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
  - 設定跨境出貨地址
  - 填寫跨境商品資訊
  - 建立跨境託運單
features:
  - 日到台跨境物流
  - "EZWAY Customs Declaration"
  - 跨境運費自動計算
prerequisites:
  - 需向開店顧問團隊申請開通服務
  - 需具備日本出貨地址 (倉庫或商家處)
related:
  - ec/app-market/express/product-info-setting/
tags:
  - "Cross-Border E-Commerce"
  - EZWAY 報關
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - APP MARKET > 我的擴充服務 > CYBERBIZ EXPRESS
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=51481
permalink: "https://help.cyberbiz.io/ec/app-market/express/cyberbiz-express-japan-to-taiwan-delivery/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# CYBERBIZ EXPRESS Japan-to-Taiwan Cross-Border Home Delivery

CYBERBIZ EXPRESS is an all-in-one cross-border logistics service designed for Japan–Taiwan e-commerce. Deliver Japanese products to customers in Taiwan easily, with EZWAY customs declaration and shipping fee reconciliation handled automatically.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (Japan to Taiwan)<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ EXPRESS
{ .doc-badge }

## Before You Start { #prerequisites-express-japan }

- **Product Information Settings**: Products sold cross-border must include customs information (such as JANCODE, ingredients, and country of origin). For field details, see [Product Information Settings for Japan-to-Taiwan Cross-Border Sales](product-info-setting.md).
- **Delivery Temperature**: Only **ambient** delivery is supported.
- **Payment Limitation**: Only **no payment on delivery** is supported (customers must pay online first).
- **Delivery Terms**: Uses **DDU (Delivered Duty Unpaid)**, so import taxes are paid by the recipient in Taiwan.
- **Pickup Options**: Supports both **pickup from your location** and **shipping to the Japan warehouse yourself**. Actual shipping fees vary by plan and pickup method.
- **Shipping Fees**: When you create a consignment note, the system calculates the fee from the product weight and volume and deducts CYBER Coins in advance. On the 5th of each month, CYBER Coins are refunded or charged based on the actual shipping fees.

## Cross-Border Shipping Process { #operate-express-japan }

Japan-to-Taiwan home delivery has five key stages. You need to send customs documents as part of the process:

1. **Pickup and Warehousing**: The carrier picks up parcels from your location or the Japan warehouse. Send the bill of lading list and invoices to `manifest_express@cyberbiz.io` in advance.
2. **Sorting and Consolidation**: Under customs rules, a consolidated bag is released only after all of its customers have confirmed their EZWAY declarations.
3. **Air Transport**: Parcels ship on the weekly flight schedule. Consolidation takes about 1 to 2 business days.

    >  The final delivery schedule depends on the flights confirmed for that week.

4. **Customs Clearance**: When a parcel enters customs clearance, the customer must **download the EZWAY app** and [**confirm the declaration**](https://web.customs.gov.tw/singlehtml/3150?cntId=cus1_3150_3150_1471).

    !!! warning "What If the Customer Never Confirms in EZWAY?"
        - **Late Declaration Fee**: If the declaration is not confirmed within 15 days, customs charges a late fee of **NT$200** per day starting on day 16.
        - **Auction of Goods**: If the declaration is still not confirmed after 20 days, [customs may auction the goods](https://web.customs.gov.tw/singlehtml/1207?cntId=cus1_93451_1207). Remind your customers to complete the declaration.

5. **Local Delivery**: After the parcel arrives in Taiwan, a local carrier delivers it to the customer.

    !!! warning "Duty Payment Reminder"
        If a single parcel is worth more than NT$2000, customs may charge duties and related taxes. The carrier collects these taxes from the recipient on delivery.

## Apply for Activation { #operate-apply-enable }

1. Contact your store consultant to apply for activation.
2. Go to **APP MARKET > My Apps > CYBERBIZ EXPRESS** and select **基本設定 > EXPRESS 宅配**.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-開始設定01.en.png){ .screenshot }

3. Select the checkbox to agree to the **Cross-Border Shipping Service Agreement**.

4. Choose how to print consignment notes.

5. Enter your **shipping address in Japan**.
    - **We recommend entering it in Chinese** to make Taiwan customs review easier.
    - If you leave this address blank, the system cannot generate customs invoices or bill of lading lists.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-開始設定02.en.png){ .screenshot }



## Ship Orders { #operate-shipping }

### Create and Print Consignment Notes { #operate-shipping-waybill }

1. Go to **Orders > All Orders**.
2. Select the orders to ship.
    - `付款狀態` must be `已收到款項`
    - `配送壯派` must be `未出貨`/`準備出貨`/`部分出貨`
    - `退貨狀態` must be `不需退貨`
3. Click **更多操作 > 建立託運單**.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單01.en.png){ .screenshot }

4. Select the delivery channel in the pop-up window.

    - **Preview and Print Documents**: Based on what you selected (see the list below), the system opens a web preview. Check it and then print.
        - **Shipping Label**
        - **Picking List**
        - **Order/Shipping Details**
    - **Bulk Download**: You can download all of the documents above at the same time.
    - **Automatic Sorting**: When you create notes in bulk, the system generates one PDF file with all order details, sorted by order number in ascending order.
    - **Real-Time Data Validation**: The system checks the fields of products in the order. If the weight or required cross-border product fields are missing, fill them in before shipping.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單02.en.png){ .small-image }

5. After the notes are created, the order status changes to `Shipped` automatically.

### Send Customs Documents { #operate-shipping-docs }

Before asking the carrier to pick up parcels, be sure to complete these steps:

1. Download and print the **bill of lading list** and **customs invoices**.

    - To make customs brokerage easier, product amounts in the bill of lading list are converted to TWD automatically at a fixed exchange rate.

        > JPY:TWD = 5:1

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單03.en.png){ .screenshot }

2. Before asking the carrier to pick up parcels, email the bill of lading list and customs invoice files for that day's orders to `manifest_express@cyberbiz.io`.

    - **Email Subject**: [Cross-Border - Merchant Name] YYYY/MM/DD Shipping Data.

## Reprint Consignment Notes { #intro-express-japan }

In the **order list**, select orders with the status `Shipped` and choose **Reprint Consignment Note** to download the documents again.

![](../../../assets/images/EC-後台-訂單-所有訂單-補印EXPRESS託運單01.en.png){ .screenshot }


## Handle Shipping Exceptions { #specs-express-japan }

When a delivery exception occurs, click **Handle Exception** in the **Actions** column and choose how to handle the parcel:

![](../../../assets/images/EC-後台-APPMARKET-EXPRESS-運送異常處理01.en.png){ .screenshot }

=== "Discard"

    - **Physical Handling**: The warehouse destroys the parcel.
    - **Order Changes**: The original order's delivery status is marked **Discarded**, and **Memo** notes **Merchant chose "Discard"**.

=== "Return to Merchant"

    - **Return Address**: Parcels are returned to the **Shipping Address** on the EXPRESS basic settings page.
    - **Order Changes**: The original order's delivery status is marked **Returned to Merchant**, and **Memo** notes **Merchant chose "Return to Merchant"**.
    - **Fees**: The system calculates only the fee for returning the parcel to the Fengchao warehouse. The international shipping fee for sending the parcel from the Fengchao warehouse back to you is not calculated or shown in the admin; the actual fee appears on your statement. Because several parcels may be packed and shipped together, the statement may show one combined fee for several parcels.


!!! warning "Parcel Handling Deadline and Fees"
    - **Deadline**: Choose a handling method **within 15 days**, or the system discards the parcel automatically.
    - **Billing**: Handling fees appear on each statement.

