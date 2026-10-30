---
title: "Set Up Order Auto-Close"
description: "Based on logistics status and a set number of days, the system's batch process automatically updates eligible orders to Completed and triggers follow-up processes such as issuing bonus points, calculating commissions, and activating coupons."
created:
last_modified: 2026-07-13 14:43
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/auto-close-order-settings/"
type: guide
author: Jase
reviewers: []
notes:
  - add doclink 訂單自動結案
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 自動結案訂單
  - 觸發紅利發送
  - 計算分潤
  - 使優惠券生效
  - 管理訂單狀態
features:
  - 訂單自動結案
  - 取貨後自動結案
  - 出貨後自動結案
  - 批次執行時間
  - 結案狀態確認
  - 紅利點數發送
  - 優惠券生效
  - 分潤計算
prerequisites: []
related:
  - ec/orders/basics/order-management-interface/
  - pos/orders/pos-order-auto-close/
  - ec/e-ticket/e-ticket-setup-guide/
  - ec/orders/basics/cancel-order/
tags:
  - "Order Auto-Close"
  - "Auto-Close Settings"
  - "Order Management"
  - "Logistics Status"
  - "Bonus Points"
  - Coupons
  - "Profit Sharing Calculation"
  - "Order Closing"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 結帳頁 & 物流設定 > 訂單相關設定 > 訂單自動結案設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=49
  - https://www.cyberbiz.io/support/?p=4606
comments: false
search:
  exclude: false
icon: lucide/calendar-check
hide:
---

![Automatic order closing settings](../../../assets/images/ec-金物流-結帳頁-訂單自動結案.en.png){ title="Automatic Order Closing Settings" .hero-page }

## About Automatic Order Closing { #intro-auto-close-order-settings }

When you set a number of days, the system automatically changes qualifying orders to "Completed," which then triggers bonus point issuing, commission calculation, coupon activation, and other follow-up actions.

!!! info "How Closing Affects the System"

    After an order is closed, the system automatically performs these marketing and financial actions:

    - **Issue bonus points:** Purchase reward bonus points are credited to the customer's account after the order is closed.
    - **Activate coupons:** Coupons members earn from "spend-threshold coupon giveaway" campaigns can be used only after the order is closed.
    - **Calculate commissions:** Referrer commissions, sign-up commissions, and others are calculated when the order is closed.
    - **Clear reminder counts:** The red count for "Open Orders" in the left admin menu is cleared automatically.

## Prerequisites and Limitations { #prerequisites }

- [x] **Partial shipment limit:** If an order is "Partially Shipped," the system **can't close it automatically**. The order can be closed manually or automatically only after all its items are updated to "Shipped" or "Received."
- [x] **Returns and closing:** By default, the system closes orders automatically only when the "return status" is "No Return Needed."
- [x] **Returns after closing:** Once an order is closed, even if it's later returned or canceled, the system **doesn't automatically deduct** bonus points or coupons already issued and doesn't affect commissions already calculated. You need to handle these manually on the member page.
- [x] **Reconciliation basis:** The "Completed" status isn't directly related to financial reconciliation. Reconciliation is based on the delivery status "Received" or "Shipped," not the closing date.

## Steps { #steps }

This setting applies to orders placed **on the storefront**. Based on the order's delivery type (**system-integrated logistics / custom logistics**), the system automatically updates the order status to "Completed" when the conditions are met.


**Automatic order closing** offers two closing modes. Choose the one that matches the delivery type you use:

- [**Close automatically after pickup**](#auto-close-delivery): For system-integrated logistics only. Orders close a set number of days after they're received.
- [**Close automatically after shipping**](#auto-close-ship): For custom logistics only. Orders close a set number of days after they're shipped.

---

#### Close Automatically After Pickup <small>Close When Received</small> { #auto-close-delivery }

For orders using system-**integrated logistics** (such as 7-Eleven, FamilyMart, EZCAT, and Pelican Express). When the system receives a "Received" status from the carrier and the set number of days passes, the system closes the order automatically.

1. Admin path: **Payment and Logistics > Checkout Page & Logistics > Order Settings > Automatic Order Completion Settings**.
2. Turn on (ON) **Automatic Order Closing**.
3. Select **Close Automatically After Pickup**.
4. Set "Days after the customer receives the order before it closes automatically."

![Close automatically after pickup settings](../../../assets/images/ec-金物流-結帳頁-訂單自動結案-已收貨訂單自動結案.en.png){ title="Close Automatically After Pickup Settings" }

---

#### Close Automatically After Shipping <small>Close When Shipped</small> { #auto-close-ship }

For orders using **custom logistics** (such as merchant self-delivery or custom Cash on Delivery). Because the system can't get the actual received status, it closes the order automatically once the order status is "Shipped" and the set number of days passes.

1. Admin path: **Payment and Logistics > Checkout Page & Logistics > Order Settings > Automatic Order Completion Settings**.
2. Turn on (ON) **Automatic Order Closing**.
3. Select **Close Automatically After Shipping**.
4. Set "Days after the order ships before it closes automatically."

![Close automatically after shipping settings](../../../assets/images/ec-金物流-結帳頁-訂單自動結案-已出貨訂單自動結案.en.png){ title="Close Automatically After Shipping Settings" }

---

## Important Rules and Limitations { #important-notes }

### Batch Run Time { #batch-schedule }

The system closes orders in a batch **every day at 06:15 AM**.

**Calculation:** An order closes at the **next 06:15 AM** after "N full days" have passed.

!!! example "Example (Set to 21 Days)"

    - **12/03 19:25** The customer picks up the order.  
    - **12/24 19:25** 21 full days have passed.
    - **12/25 06:15** The system closes the order.

!!! tip "If set to **0 days**, the order closes at "06:15 AM the next morning" after pickup."

---

### Check the Closing Status { #close-status-confirmation }

After automatic closing runs, you can check the closing status in two ways:

- **Order activity log:** The system automatically adds a record in the order details showing "Order closed." Go to **Orders > All Orders**, click the order number, and check the details in the [order activity log section](../basics/order-management-interface.md#order-history){ title="Order Activity Log" } at the bottom of the page.

- Order list status label: On the order list page, a **Completed** label appears next to the order number of closed orders.

	=== "New Order List"

		![New order list: completed](../../../assets/images/ec-訂單-所有訂單-訂單列表-已結案.en.png){ title="New Order List: Completed" }

	=== "Legacy Order List"

		![Legacy order list: completed](../../../assets/images/ec-訂單-所有訂單-舊版訂單列表-已結案.en.png){ title="Legacy Order List: Completed" }

## Next Steps { #related-operations }

<div class="grid cards" markdown>

- :lucide-file-clock:{ .lg }  
  [__Close POS Orders Automatically__](../../../pos/orders/pos-order-auto-close.md)  
  Set up automatic closing for POS orders.

- :lucide-ticket-check:{ .lg }  
  [__Close Ticket Orders Automatically__](../../e-ticket/e-ticket-setup-guide.md#票券分潤與自動結案設定)  
  Set up automatic closing for e-ticket orders.

- :lucide-circle-x:{ .lg }  
  [__Automatic Order Cancellation (Payment Timeout)__](../basics/cancel-order.md#orders-cancel-auto)  
  Have the system cancel unpaid orders automatically after a set number of days.

</div>

## FAQ { #faq }


??? quote "Why didn't my order close automatically?"

	Check that all of these conditions are met:

	1. **Automatic Order Closing** is turned on.

	2. The order's delivery type matches the selected closing mode:

	    - Integrated logistics → Close automatically after pickup

	    - Custom logistics → Close automatically after shipping

	3. The order status has reached "Received" or "Shipped."

	4. The order isn't "Partially Shipped."

	5. The return status is "No Return Needed."

	6. The set number of days has passed, and the next system batch time (06:15) has passed.

??? quote "Can I close only certain order types automatically?"

	No. Automatic order closing is currently a **store-wide setting** and can't be set by product type, payment method, or membership tier.

??? quote "Is there a difference between closing manually and automatically?"

	In system logic, **there's no difference**. Both manual and automatic closing trigger:

	- Bonus point issuing
	- Coupon activation
	- Commission calculation

	The only difference is how it runs (manually or by system batch).

??? quote "If an order is returned after it's closed, does the system take back bonus points or commissions?"

	No. Once an order is closed, even if it's later returned or canceled:

	- The system doesn't automatically deduct bonus points
	- Activated coupons aren't canceled
	- Calculated commissions aren't rolled back


	You need to adjust these manually in member management or the commission admin.

??? quote "Why doesn't an order close right away when set to 0 days?"

	Because automatic order closing runs as a **daily batch job (06:15)**.

	Setting 0 days means:

    > The order closes at the next batch time (06:15) after it reaches "Received / Shipped," not immediately.

??? quote "Does the closing time affect financial reconciliation?"

	No. Financial reconciliation is based on the delivery status "Shipped / Received" and isn't directly related to whether or when the order is closed.

??? quote "Can I see which orders are about to close automatically?"

	The system doesn't currently provide an "upcoming closing list" or forecast. We recommend:

	- Filtering the order list by delivery status
	- Exporting an order report and calculating the days yourself

    to estimate and manage this internally.
