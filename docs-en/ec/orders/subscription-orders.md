---
title: "Manage Subscription Orders"
description: "When a shopper orders on a subscription campaign page, the system creates a parent order and automatically creates sub-orders on the set cycle (such as monthly or weekly). You can manage these subscriptions and each cycle's delivery progress in the admin."
created: 2026-06-01 14:54
last_modified: 2026-09-18 14:10
lang: en-US
type: guide
author: Ann
reviewers: []
notes: 
  - 詞彙表：母訂單、子訂單
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 訂單
  - 行銷活動
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
cyb_extensions: []
intents: 
  - 管理定期定額訂單
  - 修改定期訂單配送時間
  - 查詢母子訂單關係
features: 
  - 定期定額
  - 訂閱制
  - 母子訂單
prerequisites: 
  - "定期定額活動頁"
related:
  - ec/orders/basics/order-management-interface/
  - ec/marketing/other-tools/subscription-campaign-page/
tags: 
  - Subscriptions
  - "Subscription Model"
  - "Order Management"
  - "Order Conversion"
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 定期定額訂單列表
  - 定期訂單明細
paths:
  - 訂單 > 定期定額訂單
  - 訂單 > 所有訂單
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=4570
  - https://www.cyberbiz.io/support/?p=6824
  - https://www.cyberbiz.io/support/?p=6816
permalink: "https://help.cyberbiz.io/ec/orders/subscription-orders/"
comments: false
search:
  exclude: false
icon: lucide/calendar-days
hide: []
---

# Manage Subscription Orders
When a shopper orders from a subscription page, the system creates a parent order and then automatically creates sub-orders based on the set cycle (such as monthly or weekly). You can manage these subscriptions and the delivery progress of each cycle in the admin.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    - Subscriptions are an optional module in PLUS plans (choose 2 of 11), so make sure you've selected this module before using it. Enterprise includes this feature.


## Before You Start

- **Terms**
    - **Parent order (subscription number)**: Records the overall subscription rules, such as the product combination, delivery frequency, and remaining cycles.
    - **Sub-order (regular order number)**: The delivery order actually created for each cycle, used for shipping, payment collection, and reconciliation.



## Subscription Order List Tabs

Sign in to the CYBERBIZ admin and go to **Orders > Subscription Orders**.

The system groups subscription orders into the following tabs by status so you can check them quickly:

| Tab | Description | Search By |
| :--- | :--- | :--- |
| **All Customer Orders** | Shows all placed parent orders | Subscription number<br>Recipient information (customer, recipient address, recipient phone)<br>Notes |
| **Latest Orders** | Shows each customer's latest sub-order | Order number<br>Recipient information (customer, recipient address, recipient phone) |
| **To Ship** | Shows sub-orders that are placed and ready to ship | Order number<br>Recipient information (customer, recipient address, recipient phone) |
| **Shipped** | Shows sub-orders that have been delivered | Order number<br>Recipient information (customer, recipient address, recipient phone) |
| **Order Exceptions** | Shows orders that failed to be created (such as insufficient stock or a failed credit card charge) or have delivery exceptions | Order number<br>Recipient information (customer, recipient address, recipient phone) |
| **Canceled** | Split into "Fully Canceled (parent order)" and "Partially Canceled (sub-order)" | Subscription number<br>Order number |

![](https://www.cyberbiz.co/support/wp-content/uploads/2019/11/定期定額new-14.png){ .screenshot }

## Find Parent and Sub-Order Relationships

To see which subscription order and cycle a regular order belongs to:

1. Go to **Orders > All Orders**.
2. Click **[Edit Columns](../orders/basics/order-management-interface/#編輯欄位與排序)** in the upper-right corner.
3. Select **Parent Order Number**, **Delivery Cycle**, or **Actual Deliveries** to see the order's subscription delivery information.


## Change Delivery Information

You can change delivery information for a single cycle or for the whole subscription.

### 1. Change a Single Cycle (Sub-Order)

In the subscription order list, click the text directly to change it:

- **Recipient information**: Changes only that cycle's order. Later cycles stay the same.
- **Ship date**: Changes only that cycle's ship date.

### 2. Change the Whole Subscription (Parent Order)

Click the **subscription number** to open the details page for advanced editing. Changes here affect all later sub-orders that haven't been created yet:

- **Change the delivery plan (timing)**:
  Click the edit icon next to "Purchase Plan" and adjust based on the original unit:

    - **Monthly**: You can change only "Every few weeks" and "Day of the week."
    - **Weekly**: You can change only "Day of the week."
    - **Specific date each month**: You can change only "Specific date."
    > **When it takes effect**: Changes apply starting from the cycle after the "3 upcoming orders." To change upcoming orders, edit them individually in the "Upcoming Orders" section.
        ![](https://www.cyberbiz.co/support/wp-content/uploads/2019/11/定期定額new-32.png){ .screenshot }

    !!! warning "Can I Change the Delivery Frequency?"
        **No.** The system doesn't support changing "monthly delivery" to "weekly delivery" directly. To change the frequency, cancel the original parent order and have the customer order again.


    ![](https://www.cyberbiz.co/support/wp-content/uploads/2019/11/定期定額new-26.png){ .screenshot }

- **Change products**:
  In the order details section, you can do the following with products:

    - **Edit products**: Change the quantity or unit price.
    - **Delete products**: Remove a specific product variant.
    - **Add products**: Click "Add Product," then search for and add other product variants to this subscription order (they take effect from the next order).
    > **Risk**: If changing the amount means a sub-order no longer meets the free shipping threshold, the system **automatically adds a shipping fee** when creating the order.

    ![](https://www.cyberbiz.co/support/wp-content/uploads/2019/11/定期定額new-28.png){ .screenshot }

## What Sub-Orders Include

- **Products and prices**: Sub-orders inherit the parent order's items and unit prices.

    > You can't edit items or prices directly in sub-orders. To change them, edit the related parent order.

- **Marketing discounts and gifts**: When a sub-order is created, the system applies and issues discounts based on the current [discount settings on the subscription page](../marketing/other-tools/subscription-campaign-page/#4-進階優惠設定).

    > If you change the "gift and discount rules" in the subscription campaign after the parent order is created, the changes take effect after you save them and apply to sub-orders **created afterward**.


## FAQ

??? quote "How is shipping calculated?"
    Subscription orders use **the shipping fee from when the parent order was placed** by default. The shipping fee doesn't change unless you manually change a sub-order's products or amount and the system checks the free shipping threshold again.