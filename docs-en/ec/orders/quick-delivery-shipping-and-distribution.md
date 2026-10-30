---
title: "Quick Delivery Shipping and Delivery Tracking"
description: "Guides store staff to request shipping, get matched with a driver, hand over products, and track delivery status until the shopper receives the order."
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
difficulty: beginner
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
  - 呼叫司機
  - 出貨作業
  - 追蹤配送
features:
  - CYBERBIZ NOW
  - 快速到貨
  - 第三方配送
prerequisites:
  - 訂單狀態已變更為「準備出貨」
  - 商品已依材積規範完成打包
related:
  - ec/orders/pandago-delivery-exception-rules/
tags:
  - Pandago
  - UberDirect
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 訂單詳情
  - 物流訊息
paths:
  - 訂單 > 門市訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=13166
permalink: "https://help.cyberbiz.io/ec/orders/quick-delivery-shipping-and-distribution/"
comments: false
search:
  exclude: false
icon: lucide/zap
hide: []
---
# Quick Delivery Shipping and Delivery Tracking

This guide shows store staff how to start a shipment request, match a driver, hand over items, and track delivery status until the customer receives the order.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }


!!! tip "Use Cases"
	- **Call a driver**: The items are packed, and you need the delivery platform to send a driver to pick them up at the store.
	- **Delivery monitoring**: When a customer asks about order progress, check the driver's location and estimated arrival time in real time in the admin.


## Things to Know

- **Shipping is irreversible**: Once the status changes to **Shipped**, the system immediately sends a dispatch request to the delivery platform, and it can't be freely canceled.
- **Driver matching time**: Matching time depends on supply and demand on the delivery platform.

    > If Pandago takes a long time to match a driver, see the [Pandago Delivery Exception Rules](pandago-delivery-exception-rules.md) policy.

## Steps

### Step 1: Start Shipping and Match a Driver

1. Go to **Orders > Branch Store Orders** and find orders with the status **Preparing**.
2. Select the orders and choose **Shipped** in the menu above.
    ![](../../assets/images/EC-後台-訂單-門市訂單-已出貨01.en.png){ .screenshot }

3. The system immediately sends a dispatch request to the delivery platform (Pandago or Uber Direct).
4. Watch the status change in the **Shipping status** column:
    - `Matching Driver`: The system is looking for nearby couriers.
    - `Driver Matched`: A courier is confirmed, and the page shows the driver's name and contact information (depending on platform support).

### Step 2: Hand Over Items to the Driver

1. When the driver arrives at the store, ask which platform they're from and which order number they're picking up.
2. Check that the **tracking number** on the driver's phone matches the number shown in the order's **Delivery Status** in the admin.
    ![](../../assets/images/EC-後台-訂單-門市訂單-送貨狀態顯示託運單編號01.en.png){ .screenshot }
3. Hand the packed items to the driver.

### Step 3: Track Delivery Progress

1. Check the order's **Shipping status** for real-time delivery information:
    - **Driver location**: Some platforms provide a live map link.
    - **Status names**: Include **Driver Picked Up at Store** and **Order Delivered**.
2. After the driver delivers the items to the customer, the order's delivery status in the admin changes to **Received**.


## How Delivery Statuses Work

Quick Delivery statuses update automatically based on information from the delivery platform. The main stages are:

| Status | Trigger | Customer Experience |
| :--- | :--- | :--- |
| **Matching Driver** | After the merchant clicks **Shipped** | Receives a text saying a driver is being found |
| **Driver Matched** | After a driver accepts the order | Can see the driver's location and estimated arrival time |
| **Driver Picked Up at Store** | After the driver picks up the items at the store | Receives a text saying the driver picked up the order and delivery has started |
| **Order Delivered** | The driver completes the handover and marks it complete | Has received the package |

!!! note "Order Completion"
    When the delivery status changes to **Received**, the order automatically updates to **Completed**, so you don't need to complete it manually. If the system doesn't update because of network delays, you can manually mark the status as **Completed** after 24 hours.

---

## FAQ

??? quote "Can I cancel the shipment after a driver is matched?"
    If the driver is already on the way to the store, canceling the dispatch may incur a cancellation fee (depending on the delivery platform's rules). Unless necessary (for example, if items are damaged or seriously out of stock), we recommend not canceling matched orders.

??? quote "What if a customer says they didn't receive the tracking link text?"
    Have store staff copy the order's **delivery tracking link** from the **Logistics Information** section of the order details page and send it to the customer manually or through the admin's messaging tools.

??? quote "What is the Uber Direct PIN, and where can I find it?"
    The PIN is a verification step to make sure the delivery is accurate. It's usually **the last four digits of the customer's order phone number**. The driver asks the customer for it on delivery, and you can also see the phone number in the customer information on the order details page in the admin.



