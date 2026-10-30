---
title: "Handle Orders Past the Return Deadline"
description: "When an order is past its return deadline, you can start a return manually in the admin."
created: 2026-05-26 20:52
last_modified: 2026-08-20 17:00
lang: en-US
type: guide
author: Jase
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
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 後台手動退貨
  - 設定退貨天數
  - 執行退款
features:
  - 後台手動退貨
  - 退貨時間調整設定
  - 部分退款
  - 系統逆物流
  - 自動退刷
  - 人工退款
  - 峰潮串倉退貨
prerequisites: []
related:
  - ec/orders/references/auto-refund-timeline/
  - ec/orders/returns-refunds/cvs-c2b-return/
  - ec/orders/order-refund-process/
tags:
  - Returns
  - "Return Deadline"
  - "Admin Returns"
  - "Fengchao Warehouse Integration"
  - "Automatic Card Refunds"
  - "Manual Refunds"
  - "Partial Refunds"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 更多操作
  - 選擇操作
  - 退貨狀態
paths:
  - 金物流/結帳頁 & 物流設定 > 退貨時間調整設定
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=2034
permalink: "https://help.cyberbiz.io/ec/orders/returns-refunds/overdue-return-handling/"
comments: false
search:
  exclude: false
icon: lucide/clock-alert
hide: []
---

![Order list - returning](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨中-hero.en.png){ title="Order List - Returning" .hero-page }

## About Orders Past the Return Deadline { #intro-overdue-returns }

When a customer's order is past the return deadline set in the system, the storefront "Request Return" button no longer appears, and you need to start the return process manually in the admin. This page explains how to set the return deadline and the complete steps for handling a return in the admin after the deadline has
passed.

## Prerequisites and Limitations { #prerequisites-overdue-returns }

- [x] **Manual return process in the admin**: Available on all plans.
- [x] **Return period settings**: Only PLUS and higher plans can change the number of return days; the Standard Plan keeps the default values.
- [x] **Partial refunds**: Available only on PLUS and higher plans.
- [x] **System reverse logistics (EZCAT C2B, Pelican Express return service, 7-Eleven C2B Return Service)**: Must be requested and enabled separately; not included in plans by default.

!!! note "Refund Method Limitations"
    After a certain number of days, some payment methods can't be refunded to the card automatically and must use a manual refund instead. For each payment method's automatic card refund limit, see [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ data-preview }.

---

## Steps { #operate-overdue-returns }

??? info "Fengchao Warehouse Integration Merchants"
      If the order is fulfilled by a Fengchao warehouse, "Start a return" and "Move to return review" in the steps below are handled automatically through the Fengchao warehouse integration:

      - When you click **Returning**, the system automatically notifies the Fengchao warehouse and the carrier, so you don't need to contact them.
      - When the package arrives at the Fengchao warehouse, the order status automatically updates to **Reviewing Return**, with no manual action needed.
      - You still need to manually choose **Returned** in the last step to complete the refund.

      Exceptions still follow the regular process: **POS orders**, and orders **not fulfilled by Fengchao** for merchants with partial warehouse integration.

### 1. Set the Storefront Return Period { #operate-overdue-returns-set-days }

Set "the number of days customers can request returns themselves in the storefront." After that, only you can start a return.

1. **Open the settings page**: Admin path: **"Payment and Logistics/Checkout Page & Logistics"** > **"Return Period Settings"**.
2. **Set the return days**: Set them separately by shipping method.
    * **Return days for CYBERBIZ home delivery and convenience store pickup**: Applies to integrated logistics such as EZCAT and convenience store pickup. Defaults to **10 days** if left blank[^1].
    * **Return days for other shipping methods**: Applies to custom logistics. Defaults to **14 days** if left blank[^2].
3. **Save**: Click **Save** to apply the settings.

![Return period settings](../../../assets/images/EC-金物流-結帳頁物流設定-前台退貨設定-退貨時間調整.en.png){ title="Return Period Settings" }

!!! tip "Turn Off Customer Self-Service Returns Completely"
    Entering **0** days means customers can't request returns themselves at all, and all returns must be started by you in the admin.

[^1]: Counted from the day the delivery status changes to "Received."
[^2]: Counted from the day the delivery status changes to "Shipped."

---

### 2. Start a Return Manually in the Admin { #operate-overdue-returns-initiate }

When an order is past the return deadline and the customer can't request a return, you start the return process manually from the order list page.

=== "New Order List"
    1. **Find the order**: Go to **"Orders"** > **"All Orders"**, then search for and select the order.
    2. **Change to Returning**: Open the **Actions...** drop-down at the top and select **Returning**.
    3. **Confirm the update**: The order's "Return Status" updates to **Returning**, and the customer's storefront order page shows it too.

    ![Order list - returning](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨中.en.png){ title="Order List - Returning" }

=== "Old Order List"

    1. **Find the order**: Go to **"Orders"** > **"All Orders"**, then search for and select the order.
    2. **Change to Returning**: After you select the order, an **"Actions"** drop-down appears at the top right of the page. Select **Returning**.
    3. **Confirm the update**: The order's "Return Status" updates to **Returning**, and the customer's storefront order page shows it too.

    ![Order list - returning - old version](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨中-舊版訂單列表.en.png){ title="Order List - Returning - Old Version" }

!!! note "Automatic Process for Fengchao Warehouse Orders"
      If the order meets the Fengchao automatic return conditions[^3], clicking "Returning" makes the system call the Fengchao warehouse to create a reverse logistics order instead. The order status doesn't change right away; it updates after the warehouse finishes processing.

  [^3]: The conditions are: the store has enabled Fengchao warehouse integration and the default return warehouse feature; for stores with partial warehouse integration, the order must be fulfilled by Fengchao; and the order isn't a combined shipment or a POS order.

---

### 3. Get the Returned Items Back { #operate-overdue-returns-receive-goods }

Choose any of the following ways to get the items back based on your situation. This step doesn't involve system actions; it's coordinated between you and the customer.

| Collection Method | When to Use | Notes |
| :-- | :-- | :-- |
| System reverse logistics | You've enabled services such as EZCAT C2B, Pelican Express return service, or 7-Eleven C2B Return Service | Create a reverse logistics order in the admin to send it back |
| Your own pickup | You contact a carrier to pick up the items | No system records; keep your own records |
| Customer sends it back | The customer sends it to the address you specify | No system records; keep your own records |

!!! info "Fengchao Warehouse Orders"
      For orders that meet the Fengchao automatic return conditions, the system creates the reverse logistics order and notifies the carrier automatically in this step, so you don't need to arrange collection. The carrier sends the items back to the Fengchao warehouse.

---

### 4. Move to Return Review { #operate-overdue-returns-review }

After you receive and check the items, move the order to **Reviewing Return**, the stage for confirming the refund amount and items.

1. **Get the items**: Get the items back using a method from Step 3 and check them.
2. **Update the status**: Select the order in the order list, open the **Actions...** drop-down, and choose **Reviewing Return**.

![Order list - reviewing return](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨審查.en.png){ title="Order List - Reviewing Return" }

!!! note "When the System Moves It Automatically"
    * **Fengchao warehouse orders**: When the package arrives at the Fengchao warehouse, the system automatically updates the status to **Reviewing Return** and records it in the order history, with no manual action needed.
    * **Other integrated reverse logistics**: If you collect items through reverse logistics integrated in the admin, the system may update the status automatically based on events sent by the carrier. The extent of automation varies by reverse logistics provider; if the status doesn't update, change it manually.

---

### 5. Issue the Refund { #operate-overdue-returns-refund }

Choose a **full refund** or a **partial refund** based on the refund scope. This step is the same for Fengchao merchants and other merchants; it must be done manually.

=== "Full Refund"
    1. **Start the refund**: Select the order in the order list, open the **Actions...** drop-down, and choose **Returned**.
    2. **Determine the refund method**: The system automatically determines whether an automatic card refund is possible based on the order's payment method and payment date. See [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ data-preview }.
        * **Automatic card refund available**: The system sends the card refund to the payment provider directly, and the customer receives the refund after the provider's processing time.
        * **Manual refund required**: A pop-up opens where you enter the bank account information the customer provided.
    3. **Enter bank information (manual refunds only)**: In the pop-up, enter the **Account Name**, **Bank**, **Branch**, and **Bank Account Number**, then submit.

=== "Partial Refund"
    1. **Open order details**: Click the order number to open the details page.
    2. **Find the partial refund section**: Find the "Partial Refund" section on the order details page.
    3. **Enter refund details**: Select the items to refund and enter the refund amount.
    4. **Confirm the refund**: Click **"Confirm Refund"** to finish.


## Important Rules and Limitations { #specs-overdue-returns }

### Automatic Card Refund Day Limits { #specs-overdue-returns-refund-window }

If an order is past the payment provider's automatic card refund limit after payment, the system can't refund the card directly, and you must use the manual refund process. For the full reference, see [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" data-preview }.

---

### After a Manual Refund { #specs-overdue-returns-manual-refund }

For manual refunds, you provide the customer's bank account information and CYBERBIZ sends the money on your behalf. The actual arrival time, whether an accounting fee is charged, and the fee per transaction depend on the contract terms in effect. Contact CYBERBIZ customer service for the latest rules.

---

### Handling Marketing Rewards { #specs-overdue-returns-rewards }

How returns affect bonus points, coupons, and commissions depends on your store settings and the order status. Before issuing a refund, we recommend checking the following, and contacting CYBERBIZ customer service if needed:

- Whether the bonus points or coupons already issued for the order need adjusting.
- If the order involves commission calculation, whether the return needs to be handled there too.

## Next Steps

<div class="grid cards" markdown>

- :lucide-package-check:{ .lg }  
  [__Use Convenience Store C2B Return Service__](cvs-c2b-return.md){ title="Use 7-Eleven C2B Return Service" }  
  Set up the 7-Eleven C2B Return Service reverse logistics so customers can send returns back from convenience stores.

- :lucide-credit-card:{ .lg }  
  [__Refund Methods and Operations__](../order-refund-process.md){ title="Refund Methods and Operations" }  
  Learn the complete order refund process, including how automatic card refunds and manual refunds are determined and the steps for each.

</div>

## FAQ { #faq-overdue-returns }

??? quote "Why does the customer still see the "Request Return" button after the return deadline?"
    [](){ #faq-overdue-returns-button-still-visible }
     Check that the number of days in **"Return Period Settings"** is what you expect, and that the order's delivery status has reached the starting point (system logistics count from "Received," custom logistics from "Shipped"). If the problem persists, contact CYBERBIZ customer service.

??? quote "If I want to cancel an order that's still "Preparing," do I need to use the return process?"
    [](){ #faq-overdue-returns-cancel-before-shipped }
    No. If the order hasn't shipped, change the shipping status to **Unshipped** and then cancel it. You don't need the return process.

??? quote "What if the system says an automatic card refund isn't possible after I choose "Returned"?"
    [](){ #faq-overdue-returns-cannot-auto-refund }
    This means the order is past the payment provider's automatic card refund limit and needs a manual refund. Enter the customer's bank account information in the pop-up, and CYBERBIZ will send the money on your behalf.

??? quote "Can I issue several partial refunds for the same order?"
    [](){ #faq-overdue-returns-multiple-partial-refunds }
    Yes. In the "Partial Refund" section of the order details page, select the items and amount to refund each time and confirm.

??? quote "I'm a Fengchao warehouse integration merchant. Why didn't the status change after I clicked "Returning"?"
    [](){ #faq-overdue-returns-honeycomb-status-delay }
     If the order meets the Fengchao automatic return conditions, clicking "Returning" makes the system call the Fengchao warehouse to create a reverse logistics order first. The order status doesn't change right away; it updates after the warehouse finishes processing. Wait a moment and refresh the page. If it doesn't update for a long time, contact CYBERBIZ customer service.

??? quote "For merchants with partial warehouse integration, do self-fulfilled orders also use the automatic process?"
    [](){ #faq-overdue-returns-honeycomb-partial }
    No. The system checks each order. Only orders fulfilled by Fengchao use the automatic process; other self-fulfilled orders still follow the regular manual steps.

??? quote "What happens if I set the return days to 0?"
    [](){ #faq-overdue-returns-set-to-zero }

    Entering **0** days means customers can't request returns themselves at all, and all returns must be started manually by you in the admin.

??? quote "How do the return period start dates differ between system logistics and custom logistics?"
    [](){ #faq-overdue-returns-calculation-diff }

    - **CYBERBIZ home delivery and convenience store pickup**: Counted from the day the delivery status changes to "Received."
    - **Other shipping methods (custom logistics)**: Counted from the day the delivery status changes to "Shipped."

---

## References { #reference-overdue-returns }

- [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" }


