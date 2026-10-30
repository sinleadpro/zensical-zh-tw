---
title: "Ship Store Pickup Orders"
description: "After a customer orders with Store Pickup, admins must ship the order in the admin. This guide walks you through the full process, from filtering orders and printing store pickup barcodes to handling returns."
created: 2026-04-24 14:00
last_modified: 2026-07-15 16:40
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 處理門市取貨訂單
  - 處理門市取貨退貨
features:
  - 到店條碼
  - 退回總倉
prerequisites:
  - "建立與管理門市"
  - "設定門市取貨服務"
related:
  - pos/orders/store-pickup-orders-inbound-and-pickup/
tags:
  - "Store Pickup"
  - "Shipping Process"
  - "Store Pickup Barcodes"
  - "Order Management"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 下載到店條碼並改為已出貨
  - 補印到店條碼單
  - 退回總倉
  - 退貨審查
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=10522
permalink: "https://help.cyberbiz.io/ec/orders/store-pickup-orders/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

# Ship Store Pickup Orders
After a customer orders with **Store Pickup**, admins must ship the order in the admin. This guide walks you through the full process, from filtering orders and printing store pickup barcodes to handling returns.
{ .subtitle }

[:lucide-layers:{ title="Available Products" }](../../resources/conventions#適用產品) | Brand Website
[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! tip "Scope and Related Docs"
    This article applies only to shipping **regular store orders**. For stock-in and pickup of **POS store orders**, see [POS Store Stock-In and Pickup](../../pos/orders/store-pickup-orders-inbound-and-pickup.md).

## Before You Start

- **Shipping limit**: Store pickup orders support only **full shipment**. **Partial shipment isn't supported**.
- **Plan limit**: This feature isn't available on the **Expert plan**.


## Steps

### Ship Orders

1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.

    > You can use the order filter and select `Store Pickup` under **Delivery Type** to find orders to process.

2. Select the orders to process (one order, or a batch of orders with the same delivery type).
3. Click **Select Action** in the upper-right corner and select **Shipped**.

    ![](../../assets/images/EC-後台-訂單-所有訂單-門市訂單出貨01.en.png){ .screenshot }

4. Based on the order's shipping progress, switch **Delivery Status** to **Arrived at Store > Received**.

    > Customers can check the order status in the member center, but the system doesn't notify them of status changes.

    ![](../../assets/images/EC-後台-訂單-所有訂單-門市訂單出貨02.en.png){ .screenshot }
    ![](../../assets/images/EC-後台-訂單-所有訂單-門市訂單出貨03.en.png){ .screenshot }



## Common Scenarios


### Cancel an Order

=== "Merchant"

    If the delivery status is `Unshipped`, admins can click **Cancel Order** in the order.

    ![](../../assets/images/EC-後台-訂單-門市訂單-取消訂單01.en.png){ .screenshot }

=== "Shopper"

    Shoppers can also click **Cancel Order** on the order details page on the storefront.

    ![](../../assets/images/EC-前台-訂單查詢-取消訂單01.en.png){ .screenshot }






