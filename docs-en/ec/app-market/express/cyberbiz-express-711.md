---
title: "CYBERBIZ EXPRESS 7-11 Cross-Border Store Pickup"
description: "Overseas merchants can offer Japan-to-Taiwan convenience store pickup without applying for a 7-11 cross-border account. Covers activation, order shipping, shipment tracking, and handling exception packages."
created: 2026-07-23 15:45
last_modified: 2026-08-06 15:20
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
  - 金物流
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
  - 設定 7-11 超取
  - 跨境出貨到 7-11
  - 處理超取未取包裹
features: 
  - 7-11 跨境超取
  - EZWAY 串接
  - 自動化貨態通知
prerequisites: 
  - 需向開店顧問團隊申請開通服務
  - 需安裝 CYBERBIZ EXPRESS APP
related:
  - ec/app-market/express/product-info-setting/
tags: 
  - 7-11
  - "Cross-Border Logistics"
  - "Convenience Store Pickup"
  - EXPRESS
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 建立託運單
  - 物流單號
  - 逾期處理
paths:
  - 金物流 > 物流設定 > 超商物流
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/express/cyberbiz-express-711/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---
# CYBERBIZ EXPRESS 7-11 Cross-Border Store Pickup

With the 7-11 cross-border store pickup service from CYBERBIZ EXPRESS, overseas merchants can offer Taiwan customers convenient "store pickup without payment" delivery without signing their own contract with 7-11.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (Japan to Taiwan)<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ EXPRESS
{ .doc-badge }

## Service Overview and Benefits { #overview-express-711 }

Overseas merchants can use CYBERBIZ EXPRESS for Japan-to-Taiwan store pickup delivery without a 7-11 customer account, and get these benefits:

- **No Contract Required**: You do not need to apply for a 7-11 customer account or handle complicated contract procedures.
- **Lower Logistics Costs**: Cross-border shipping rates are more competitive than EMS.
- **EZWAY Integration**: The system handles real-name verification data automatically, reducing customs clearance issues.
- **All-in-One Management**: Store selection on the storefront map, label printing, shipment tracking, and decisions on returned parcels are all handled in the CYBERBIZ admin.

## Before You Start { #prerequisites-express-711 }

- **Product Information Settings**: Products sold cross-border **must include customs information** (such as JANCODE, ingredients, and country of origin). For field details, see [Product Information Settings for Japan-to-Taiwan Cross-Border Sales](product-info-setting.md).
- **Shipping Fees**: When you create a consignment note, the system calculates the fee from the product weight and volume and deducts CYBER Coins in advance. On the 5th of each month, CYBER Coins are refunded or charged based on the actual shipping fees.


## Turn on the Feature { #operate-express-711 }

### Apply for Activation { #operate-express-711-application }

1. Contact your store consultant to apply for activation.
2. Go to **APP MARKET > My Apps > CYBERBIZ EXPRESS** and select **基本設定 > EXPRESS 超取**.

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS啟用超商物流01.en.png){ .screenshot }

3. Select the checkbox to agree to the **Cross-Border Shipping Service Agreement** and save the settings.
4. Turn on the **7-11 Store Pickup** switch and choose how to print consignment notes.
5. Enter your **shipping address in Japan**.
    - **We recommend entering it in Chinese** to make Taiwan customs review easier.
    - If you leave this address blank, the system cannot generate customs invoices or bill of lading lists.

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS啟用超商物流02.en.png){ .screenshot }


### Set up the Checkout Option { #operate-express-711-checkout-settings }

After turning on the logistics switch, enable the delivery method for checkout:

1. Go to **Payment and Logistics > 物流設定 > Convenience Store Logistics** and click the edit button for **7-11 B2C Store Pickup**.

    ![](../../../assets/images/EC-後台-金物流-超商物流-日到台超商物流01.en.png){ .screenshot }

2. Turn on **Enable Pickup Without Payment**, set the shipping fee rules, and save.

    ![](../../../assets/images/EC-後台-金物流-超商物流-日到台超商物流02.en.png){ .screenshot }

## Ship Orders { #operate-shipping }

When a customer places an order and chooses 7-11 store pickup, follow these steps to ship it.

### Create Consignment Notes { #operate-shipping-waybill-create }

To create a consignment note, the order must meet all of these conditions:

- The order status is `已收到款項`.
- The delivery status is `未出貨` / `準備出貨` / `部分出貨`.
- The return status is `不需退貨`.

**Steps:**

1. Go to **Orders > All Orders**.
2. Select the orders to ship and click **更多操作 > 建立託運單**.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單01.en.png){ .screenshot }

3. Based on what you selected (consignment notes, picking lists, order/shipping details), the system opens print preview tabs so you can print directly.

    > Click **Download all documents at the same time** to save the documents to your computer as a compressed file.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單04.en.png){ .small-image }

!!! note "When the Shipping Status Changes"
    Only after the **Shipping Label** is generated successfully does the order status change to `Shipped` automatically.

### Reprint Consignment Notes { #operate-shipping-reprint }

To reprint a consignment note, the order must meet this condition:

- The delivery status is `Shipped`

**Steps:**

Select the orders and click **更多操作 > 補印託運單**.

![](../../../assets/images/EC-後台-訂單-所有訂單-補印EXPRESS託運單01.en.png){ .screenshot }


!!! info "Automatic Detection and Error Prevention"
    If the selected orders include orders that do not use EXPRESS logistics, the system shows a message, skips them, and prints only the EXPRESS orders.

    ![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單05.en.png){ .small-image }


## Send Customs Documents { #reference-express-711 }

Before asking the carrier to pick up parcels, be sure to complete these steps:

1. Select the shipped orders and download the **bill of lading list**.
2. Email the file to `manifest_express@cyberbiz.io`.
    - **Email Subject**: [Cross-Border - Merchant Name] YYYY/MM/DD Shipping Data.


![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單03.en.png){ .screenshot }

## Download Customs Invoices { #operate-download }

If you need to apply for tax savings with the Japanese government, select the orders after shipping and download the **customs invoices**.

To download a customs invoice, the order must meet this condition:

- The delivery status is `Shipped`

![](../../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單03.en.png){ .screenshot }


## Handle Shipping Exceptions { #specs-express-711 }

### Uncollected Parcels { #specs-express-711-overdue }

1. If a customer does not pick up a parcel within 7 days, the parcel is returned and received by the Fengchao warehouse. You can check its status in the **EXPRESS tracking number list**, where the delivery status shows **Overdue**.
2. After Fengchao receives the parcel, the delivery status shows **Returned to Warehouse**, and a **Handle Overdue Parcel** button appears on the tracking number page.

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS-超商訂單逾期未取01.en.png){ .screenshot }

3. Choose how to handle the parcel:

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS-超商訂單逾期未取02.en.png){ .small-image }

    === "Ship Again"

        - **Delivery Limitation**: The parcel can only be sent back to the original store. The recipient address cannot be changed.
        - **Order Changes**: The original order's delivery status is marked **Invalid**, and the system creates a new consignment note automatically.
        - **Linked Information**:

            - The new consignment note number is recorded in the order **Memo** automatically.

            - The order details page shows both the **original consignment note** and the **new consignment note**.

                ![](../../../assets/images/EC-後台-訂單-所有訂單-EXPRESS超商訂單再寄一次明細01.en.png){ .screenshot }

        - **Shipment Tracking**: The order status is updated based on the new consignment note, and the delivery history is kept in the activity log.

            ![](../../../assets/images/EC-後台-訂單-所有訂單-EXPRESS超商訂單再寄一次明細02.en.png){ .screenshot }



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

    ![](../../../assets/images/EC-後台-APPMARKET-EXPRESS-超商訂單逾期未取04.en.png){ .screenshot }


### Expired Consignment Notes { #specs-express-711-waybill-expiry }

If a parcel reaches the consolidation warehouse more than 30 days after its consignment note was printed, the system marks the delivery status as **Shipping Exception** and does the following:

- **Automatic Reshipment**: After the Fengchao warehouse receives the parcel, the system creates a new consignment note and ships it again.
- **Status Change**: The original consignment note changes to **Invalid**, and the system records the new consignment note number automatically.
- **Merchant Tracking**: The system handles this automatically, so **you do not need to do anything**. Keep tracking the shipment with the new consignment note number.



### Store Closures and Relocations { #specs-express-711-store-closed }

If the pickup store closes or relocates, the system marks the delivery status as **Shipping Exception**.

![](../../../assets/images/EC-後台-APPMARKET-EXPRESS-門市關轉重選門市01.en.png){ .screenshot }


Select a new 7-11 store on the order details page within **2 business days**.

![](../../../assets/images/EC-後台-APPMARKET-EXPRESS-門市關轉重選門市02.en.png){ .screenshot }

> 

## Shipping Notifications { #intro-express-711 }

The system sends notifications to customers and merchants automatically so everyone stays up to date on shipment status:

| Scenario | Trigger | Recipient | Method | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Shipping Notification** | Consignment note created | Customer | Email | Includes an EZWAY real-name verification reminder |
| **Arrival Notification** | Parcel arrives at the store | Customer | SMS + Email | Sent on day 1 |
| **Pickup Reminder** | Not picked up by day 4 after arrival | Customer | SMS + Email | |
| **Store Closure/Relocation** | 讀取到關轉狀態 | 商家<br>消費者 | Email | **Merchant must update the store within 2 days** |
| **Returned After Store Closure Deadline** | The store closed or relocated, the merchant did not select a new store, and the parcel is returned | Merchant<br>Customer | Email | The merchant is notified separately after the warehouse receives the parcel |
| **Returned After Not Picked Up** | An uncollected parcel is returned | Merchant<br>Customer | Email | The merchant is notified separately after the warehouse receives the parcel |
| **Return Confirmation** | The warehouse receives the returned parcel | Merchant | Email | **Merchant must choose a handling method within 15 days**, or the parcel is discarded automatically |
| **Ship Again** | The warehouse ships with a new consignment note | Merchant<br>Customer | Email | |




