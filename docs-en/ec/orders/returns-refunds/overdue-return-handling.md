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
  - ec/orders/order-refund-process/
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

---

## Steps { #operate-overdue-returns }

??? info "Fengchao Warehouse Integration Merchants"
      If the order is fulfilled by a HONEYCOMB warehouse, "Start a return" and "Move to return review" in the steps below are handled automatically through the HONEYCOMB warehouse integration:

      - When you click **Returning**, the system automatically notifies the HONEYCOMB warehouse and the carrier, so you don't need to contact them.
      - When the package arrives at the HONEYCOMB warehouse, the order status automatically updates to **Reviewing Return**, with no manual action needed.
      - You still need to manually choose **Returned** in the last step to complete the refund.

      Exceptions still follow the regular process: **POS orders**, and orders **not fulfilled by Fengchao** for merchants with partial warehouse integration.

### 1. Set the Storefront Return Period { #operate-overdue-returns-set-days }

Set "the number of days customers can request returns themselves in the storefront." After that, only you can start a return.

1. **Open the setup page**: Admin path: **"Payment and Logistics/Checkout Page & Logistics"** > **"Return Period Settings"**.
2. **Set the return days**: Set them separately by shipping method.
    * **Return days for CYBERBIZ home delivery and convenience store pickup**: Applies to integrated logistics such as T-CAT and convenience store pickup. Defaults to **10 days** if left blank[^1].
    * **Return days for other shipping methods**: Applies to custom logistics. Defaults to **14 days** if left blank[^2].
3. **Save**: Click **Save** to apply the settings.

![Return period settings](../../../assets/images/EC-金物流-結帳頁物流設定-前台退貨設定-退貨時間調整.en.png){ title="Return Period Settings" }

!!! tip "Turn Off Customer Self-Service Returns Completely"
    Filling in **0** days means customers can't request returns themselves at all, and all returns must be started by you in the admin.

[^1]: Counted from the day the delivery status changes to "Received."
[^2]: Counted from the day the delivery status changes to "Shipped."

---

### 2. Start a Return Manually in the Admin { #operate-overdue-returns-initiate }

When an order is past the return deadline and the customer can't request a return, you start the return process manually from the order list page.

=== "New Order List"
    1. **Find the order**: Go to **"Orders"** > **"All Orders"**, then search for and select the order.
    2. **Change to Returning**: Open the **Actions...** dropdown at the top and select **Returning**.
    3. **Confirm the update**: The order's "Return Status" updates to **Returning**, and the customer's storefront order page shows it too.

    ![Order list - returning](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨中.en.png){ title="Order List - Returning" }

=== "Old Order List"

    1. **Find the order**: Go to **"Orders"** > **"All Orders"**, then search for and select the order.
    2. **Change to Returning**: After you select the order, an **"Actions"** dropdown appears at the top right of the page. Select **Returning**.
    3. **Confirm the update**: The order's "Return Status" updates to **Returning**, and the customer's storefront order page shows it too.

    ![Order list - returning - old version](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨中-舊版訂單列表.en.png){ title="Order List - Returning - Old Version" }

!!! note "Automatic Process for Fengchao Warehouse Orders"
      If the order meets the HONEYCOMB automatic return conditions[^3], clicking "Returning" makes the system call the HONEYCOMB warehouse to create a reverse logistics order instead. The order status doesn't change right away; it updates after the warehouse finishes processing.

  [^3]: The conditions are: the store has enabled HONEYCOMB warehouse integration and the default return warehouse feature; for stores with partial warehouse integration, the order must be fulfilled by HONEYCOMB; and the order isn't a combined shipment or a POS order.

---

### 3. Get the Returned Items Back { #operate-overdue-returns-receive-goods }

Choose any of the following ways to get the items back based on your situation. This step doesn't involve system actions; it's coordinated between you and the customer.

| Collection Method | Use Cases | Notes |
| :-- | :-- | :-- |
| System reverse logistics | You've enabled services such as T-CAT C2B, Pelican return service, or 7-11 C2B Return Service | Create a reverse logistics order in the admin to send it back |
| Your own pickup | You contact a carrier to pick up the items | No system records; keep your own records |
| Customer sends it back | The customer sends it to the address you specify | No system records; keep your own records |

!!! info "Fengchao Warehouse Orders"
      For orders that meet the HONEYCOMB automatic return conditions, the system creates the reverse logistics order and notifies the carrier automatically in this step, so you don't need to arrange collection. The carrier sends the items back to the HONEYCOMB warehouse.

---

### 4. Move to Return Review { #operate-overdue-returns-review }

After you receive and check the items, move the order to **Reviewing Return**, the stage for confirming the refund amount and items.

1. **Get the items**: Get the items back using a method from Step 3 and check them.
2. **Update the status**: Select the order in the order list, open the **Actions...** dropdown, and choose **Reviewing Return**.

![Order list - reviewing return](../../../assets/images/EC-訂單-所有訂單-更多操作-退貨審查.en.png){ title="Order List - Reviewing Return" }

!!! note "When the System Moves It Automatically"
    * **HONEYCOMB warehouse orders**: When the package arrives at the HONEYCOMB warehouse, the system automatically updates the status to **Reviewing Return** and records it in the order history, with no manual action needed.
    * **Other integrated reverse logistics**: If you collect items through reverse logistics integrated in the admin, the system may update the status automatically based on events sent by the carrier. The extent of automation varies by reverse logistics provider; if the status doesn't update, change it manually.

---

### 5. Issue the Refund { #operate-overdue-returns-refund }

Choose a **full refund** or a **partial refund** based on the refund scope. This step is the same for HONEYCOMB merchants and other merchants; it must be done manually.

=== "Full Refund"
    1. **Start the refund**: Select the order in the order list, open the **Actions...** dropdown, and choose **Returned**.
    2. **Determine the refund method**: The system automatically determines whether an automatic card refund is possible based on the order's payment method and payment date. See [Refund Methods and Operations](../order-refund-process/#specs-order-refund){ data-preview }.
        * **Automatic card refund available**: The system sends the card refund to the payment provider directly, and the customer receives the refund after the provider's processing time.
        * **Manual refund required**: A dialog opens where you fill in the bank account information the customer provided.
    3. **Fill in bank information (manual refunds only)**: In the dialog, fill in the **Account Name**, **Bank**, **Branch**, and **Bank Account Number**, then submit.

=== "Partial Refund"
    1. **Open order details**: Click the order number to open the detail page.
    2. **Find the partial refund section**: Find the "Partial Refund" section on the order detail page.
    3. **Enter refund details**: Select the items to refund and enter the refund amount.
    4. **Confirm the refund**: Click **"Confirm Refund"** to finish.


## Next Steps { #next-steps-overdue-return }

<div class="grid cards" markdown>

- :lucide-package-check:{ .lg }  
  [__Use Convenience Store C2B Return Service__](cvs-c2b-return.md){ title="Use 7-Eleven C2B Return Service" }  
  Set up the 7-11 C2B Return Service reverse logistics so customers can send returns back from convenience stores.

- :lucide-credit-card:{ .lg }  
  [__Refund Methods and Operations__](../order-refund-process.md){ title="Refund Methods and Operations" }  
  Learn the complete order refund process, including how automatic card refunds and manual refunds are determined and the steps for each.

</div>

## FAQ { #faq-overdue-returns }

??? quote "Why does the customer still see the "Request Return" button after the return deadline?"
    [](){ #faq-overdue-returns-button-still-visible }
     Check that the number of days in **"Return Period Settings"** is what you expect, and that the order's delivery status has reached the starting point (system logistics count from "Received," custom logistics from "Shipped"). If the problem persists, contact CYBERBIZ customer support.

??? quote "If I want to cancel an order that's still "Preparing," do I need to use the return process?"
    [](){ #faq-overdue-returns-cancel-before-shipped }
    No. If the order hasn't shipped, change the shipping status to **Unshipped** and then cancel it. You don't need the return process.

??? quote "What if the system says an automatic card refund isn't possible after I choose "Returned"?"
    [](){ #faq-overdue-returns-cannot-auto-refund }
    This means the order is past the payment provider's automatic card refund limit and needs a manual refund. Fill in the customer's bank account information in the dialog, and CYBERBIZ will send the money on your behalf.

??? quote "I'm a Fengchao warehouse integration merchant. Why didn't the status change after I clicked "Returning"?"
    [](){ #faq-overdue-returns-honeycomb-status-delay }
     If the order meets the HONEYCOMB automatic return conditions, clicking "Returning" makes the system call the HONEYCOMB warehouse to create a reverse logistics order first. The order status doesn't change right away; it updates after the warehouse finishes processing. Wait a moment and refresh the page. If it doesn't update for a long time, contact CYBERBIZ customer support.

??? quote "For merchants with partial warehouse integration, do self-fulfilled orders also use the automatic process?"
    [](){ #faq-overdue-returns-honeycomb-partial }
    No. The system checks each order. Only orders fulfilled by HONEYCOMB use the automatic process; other self-fulfilled orders still follow the regular manual steps.

??? quote "What happens if I set the return days to 0?"
    [](){ #faq-overdue-returns-set-to-zero }

    Filling in **0** days means customers can't request returns themselves at all, and all returns must be started manually by you in the admin.

??? quote "How do the return period start dates differ between system logistics and custom logistics?"
    [](){ #faq-overdue-returns-calculation-diff }

    - **CYBERBIZ home delivery and convenience store pickup**: Counted from the day the delivery status changes to "Received."
    - **Other shipping methods (custom logistics)**: Counted from the day the delivery status changes to "Shipped."



