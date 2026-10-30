---
title: "Partial Delivery or Cancellation for Out-of-Stock Orders"
description: "When a Quick Delivery order has out-of-stock products or exceeds the size limit, this guide shows how to ship part of the order, refund the difference, or cancel the whole order."
created: 2026-02-06 00:00
last_modified: 2026-07-06 17:00
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
  - 金物流
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
plan_options: 
  - optional
cyb_extensions:
  - NOW!
intents:
  - 部分出貨
  - 取消訂單
  - 部分退款
features:
  - CYBERBIZ NOW
  - 部分出貨
  - 退款流程
prerequisites:
  - 訂單狀態為「準備出貨」
  - 已與消費者達成缺貨處理共識
related: []
tags: []
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 訂單詳情
  - 退貨管理
paths:
  - 訂單 > 門市訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=13193
  - https://www.cyberbiz.io/support/?p=13344
permalink: "https://help.cyberbiz.io/ec/orders/out-of-stock-partial-shipping-or-cancellation/"
comments: false
search:
  exclude: false
icon: lucide/package-x
hide: []
---
# Partial Delivery or Cancellation for Out-of-Stock Orders

When a Quick Delivery order has out-of-stock items or exceeds the size limit, this article shows how to ship part of the order, refund the difference, or cancel the whole order.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }


!!! tip "Use Cases"
	- **Some items out of stock**: Only some items in the order are out of stock, and after you contact the shopper, they agree that you ship the in-stock items first.
	- **All items out of stock**: The store can't supply any items in the order, so you cancel the order and refund the full amount.

---

## Before You Start

!!! danger "Key Limit: Partial Shipment Only Once"
    You can do a partial shipment of a Quick Delivery order **only once**. As soon as you confirm the shipment, the system calls a driver right away. Items you didn't select are treated as not delivered, and you can't call a driver for the order again.

- **Communicate first**: Before handling any out-of-stock situation (partial shipment or cancellation), we recommend calling the shopper to confirm, to avoid disputes or unnecessary reverse logistics fees.
- **Status requirements**:
    - **Partial shipment**: The order must first be changed to **Preparing** before you can ship part of it.
    - **Cancel order**: The order status must stay **Unshipped**. If the order is already **Preparing**, use **partial shipment** or **return handling** instead.
- **Refunds**: Quick Delivery orders are all prepaid. After cancellation or a return, the system automatically starts a refund to the original payment method (such as a credit card refund).


## Steps

### Task 1: Ship Part of the Order

When you decide to ship only some items in the order, follow these steps:

1. Go to **Orders > Branch Store Orders** and open the details of the order whose delivery status is **Preparing**.
2. In the product list, select the items and quantities you're actually shipping.
3. Double-check your selection (remember: you can't call a driver again for the unselected items).
4. Click **Confirm and ship**.
    ![](../../assets/images/EC-後台-訂單-門市訂單-部分出貨01.en.png){ .screenshot }
5. The system starts driver matching automatically, and the order's delivery status changes to **Partially Shipped**.

After the partial shipment, refund the items that weren't shipped:

1. Go to **Orders > Branch Store Orders** and change the order's delivery status to **Returning > Reviewing Return**.
    ![](../../assets/images/EC-後台-訂單-門市訂單-部分退貨01.en.png){ .screenshot }
2. In the **Partial Refund** section of the order details, select the items to refund and check the refund amount (calculated automatically; you can also adjust it manually).
    ![](../../assets/images/EC-後台-訂單-門市訂單-部分退款01.en.png){ .screenshot }
3. Click **Confirm refund**. The system automatically starts the payment refund.

### Task 2: Cancel the Whole Order (Reject the Order)

If you can't supply the order at all and need to cancel it:

1. **Before clicking "Preparing"**:
    - On the details page, click **Cancel Order**, choose a cancellation reason, and confirm.
      ![](../../assets/images/EC-後台-訂單-門市訂單-取消訂單01.en.png){ .screenshot }
2. **After clicking "Preparing" but before calling a driver**:
    - Select the order, change it to **Returning**, and then refund the full amount through the return process.
3. **After clicking "Shipped," while matching a driver**:
    - If the status is **Matching Driver**, try changing it to **Returning** to cancel matching.
    - If the cancellation succeeds, the status changes to **Shipping Exception**, and you need to check your email to confirm the result.
    - If it fails, the delivery status shows **Matching Can't Be Canceled**. The driver still comes to the store to pick up, and you pay the shipping fee.

## FAQ

??? quote "After a partial shipment, I found I missed an item. Can I ship it separately?"
    No. Quick Delivery orders use **one-time matching**: as soon as you confirm, the dispatch request goes to the delivery platform. If you missed an item, we recommend refunding it and asking the shopper to order again, or arranging with the shopper to send it by another shipping method (at your expense).

??? quote "How is the shipping fee calculated after a partial shipment?"
    Quick Delivery shipping fees are based on the estimated route when the order was placed. Even with a partial shipment, the fee you pay the delivery platform usually stays the same and doesn't go down because there are fewer items.

??? quote "Why did canceling matching fail?"
    If the delivery platform has already assigned a driver and the driver is close to the store, the system may not allow canceling. In that case, we recommend explaining to the driver when they arrive, and you pay the first-leg shipping fee (the driver's dispatch cost).

