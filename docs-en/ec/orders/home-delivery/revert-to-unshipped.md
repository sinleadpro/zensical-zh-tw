---
title: "How to Change an Order from Preparing Back to Unshipped"
description: "Change an order from Preparing back to Unshipped so the shopper can cancel the order again."
created: 2026-05-11 18:51
last_modified: 2026-06-30 15:25
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
  - 調整訂單配送狀態
  - 恢復消費者取消訂單權限
features:
  - 配送狀態變更
  - 訂單取消功能
prerequisites: []
related:
  - ec/orders/basics/search-filter-orders/
  - ec/orders/basics/cancel-order/
  - ec/orders/basics/order-fulfillment-flow/
tags:
  - "Order Management"
  - "Delivery Status"
  - Preparing
  - Unshipped
  - "Cancel Order"
  - "Return Status"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7803
  - https://www.cyberbiz.io/support/?p=23611
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/revert-to-unshipped/"
comments: false
search:
  exclude: false
icon: lucide/rotate-ccw
hide: []
---

![Change order to unshipped](../../../assets/images/EC-訂單-所有訂單-更多操作-未出貨-hero.en.png){ title="Change Order to Unshipped" .hero-page }

## About Reverting Orders to Unshipped

Once an order is marked "Preparing," you've started the shipping process, and the customer **can't cancel the order themselves** on the storefront.

If the order hasn't actually been handed to the carrier (for example, the customer suddenly asks to change the order, an item is out of stock, or there's a payment problem), you can use the "Unshipped" action to move the order back a stage so it can **be changed or canceled** again.

??? example "When to Use"

    * A customer calls to **cancel the order**, but it's already been marked "Preparing."
    * You need to swap items or change quantities, but the admin doesn't allow changing order contents while the order is "Preparing."
    * Delivery information (recipient, address, delivery date) needs major changes and can't be edited in the current status.
    * You want to hold the shipment until the customer confirms, then restart preparation.

!!! note "Related Feature Tips"

    *   **Impact on customers**: When the delivery status is "Preparing," customers usually can't cancel the order. Once it's reverted to "Unshipped," they can again.
    *   **Merchant note**: If you only need to change the recipient information or delivery date, you can also do that directly on the order details page while the order is "Unshipped."

## Before You Start

Before changing the status, check the order's "Return Status," or the change won't be possible:

*   [x] **Supported**: The return status must be **"No Return Needed"** or **"Return Refused"**.
*   [ ] **Not supported**: If the order is "Returning," "Reviewing Return," or "Returned," you can't change the delivery status back to Unshipped.

## Steps

1.  **Open the page**: Sign in to the CYBERBIZ admin and go to **"Orders" > "All Orders"**.
2.  **Select orders**: In the order list, find orders whose delivery status ([quick filter](../basics/search-filter-orders.md#orders-filter){ title="How to Search and Filter Orders" }) is **Preparing** and select them.
3.  **Choose an action**: Click the **Actions...** or **"Actions"** drop-down at the upper right of the list.
4.  **Make the change**: Select **Unshipped** in the menu.
5.  **Done**: The order's delivery status changes to "Unshipped," and the customer can see the cancel order button on the storefront (if you've turned on [customer order cancellation](../basics/cancel-order.md#orders-cancel-customer){ title="How to Cancel an Order" }).

=== "New Order List"

    ![Change order status to unshipped](../../../assets/images/EC-訂單-所有訂單-更多操作-未出貨.en.png){ title="Change Order Status to Unshipped" }

=== "Legacy Order List"


    ![Change order status to unshipped - legacy order list](../../../assets/images/EC-訂單-所有訂單-更多操作-未出貨-舊版訂單列表.en.png){ title="Change Order Status to Unshipped (Legacy Order List)" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-package:{ .lg }  
  [__Order Fulfillment Flow__](../basics/order-fulfillment-flow.md){ title="Order Fulfillment Flow" }  
  Learn the full order fulfillment flow, including Preparing, In Transit, Delivered, and other stages.

- :lucide-ban:{ .lg }  
  [__How to Cancel an Order__](../basics/cancel-order.md){ title="How to Cancel an Order" }  
  Learn the three ways orders are canceled: by you, by members on the storefront, and automatically by the system.

</div>

## FAQ

??? quote "Why can't I change an order back to "Unshipped"?"

    Check the order's return status. Only orders with a return status of **"No Return Needed"** or **"Return Refused"** can have their delivery status changed. If the order is "Returning," "Reviewing Return," or "Returned," it can't be changed.

??? quote "After I revert an order to "Unshipped," can the customer cancel it?"

    Yes. Once the delivery status is back to "Unshipped," the customer can see the cancel order button on the storefront and cancel (if you've turned on [customer order cancellation](../basics/cancel-order.md#orders-cancel-customer){ title="How to Cancel an Order" }).

??? quote "Can I edit recipient information directly while the order is "Unshipped"?"

    Yes. While the order is "Unshipped," you can edit the recipient information or delivery date directly on the order details page without moving the order back further.




---

<!--
## Overview

  Once an order is marked "Preparing," you've started the shipping process, and the
  customer **can't cancel the order themselves** on the storefront. If it hasn't actually been handed to the carrier (for example, the customer
  suddenly asks for changes, an item is out of stock, or there's a payment problem), you can use the "Unshipped" action
  to **move the order back a stage** so it can be changed or canceled again.

  !!! info "When Would You Use This Feature?"

      *   A customer calls to **cancel the order**, but it's already been marked "Preparing."
      *   You need to swap items or change quantities, but the admin doesn't allow changing order contents while the order is "Preparing"
  .
      *   
  Delivery information (recipient, address, delivery date) needs major changes and can't be edited in the current status.
      *   You want to hold the shipment until the customer confirms, then restart preparation.

  ## Read First: When You Can and Can't Revert

  The "Unshipped" action
  **isn't available in every status**. The system checks the following three conditions to decide whether to show it.
  If they aren't met, the "Unshipped" option doesn't appear in the drop-down.

  ### Required Conditions

  | Condition | Required value | Description |
  | :-- | :-- | :-- |
  | Delivery status | Preparing |
  Only Preparing can be reverted; other statuses (Shipped, In Transit, etc.) can't |
  | Return status | No Return Needed **or** Return Refused |
  The order hasn't entered the return process, or the return was refused |
  | Payment status | Paid **or** Cash on Delivery | Ensures the order has a valid payment record
  |
  | Order status | In Progress (not completed or canceled) | Completed /
  canceled orders can't be reverted |

  ### Not Supported

  *   The order has entered
  **Returning**, **Reviewing Return** (receipt inspection), **Pending Refund**, **Returned**,
  or another return process status.
  *   The order's delivery method is **express delivery** (such as Pandago, Uber Direct,
  or other on-demand delivery services). An external logistics system is already involved, so it can't be reverted from the admin.
  *   The order is completed or canceled.
  *   When you select multiple orders, if any one doesn't meet the conditions above, the "Unshipped" option doesn't
  appear. Handle them separately.

  !!! tip "Why Don't Some Orders Show the "Unshipped" Option?"

      The system checks all selected orders together. If any order doesn't meet the conditions, the menu
  hides this action. Select orders one at a time to find which one is blocking it.

  ## Steps

  === "New Order List"

      1.  **Open the page**: Sign in to the CYBERBIZ admin, click
  **"Orders"** in the left menu, then go to **"All Orders."**
      2.  **Find the orders to change**: In the order list, use
  **the delivery status quick filter** (see [Order Filters Reference][orders-filter]{
  data-preview }) to narrow the list to "Preparing" orders.
      3.  **Select orders**: Select one or more orders to revert in the order list.
      4.  **Open the action menu**: Click the **Actions...**
  drop-down above the list.
      5.  **Click "Unshipped"**: Select **Unshipped** in the menu.
      6.  **Confirm**: The system shows a confirmation window
  **"Confirm 'Unshipped'?"** Click **Yes** to finish.

      ![Change order status to unshipped](../../../assets/images/EC-訂單-所有訂單-更
  多操作-未出貨.png)

      !!! note "When the Option Appears"

          If, after selecting orders, the "More Actions" drop-down doesn't include **Unshipped**,
  at least one selected order doesn't meet the
  [Read First](#操作前必讀可調整與不可調整的情境)
  conditions. Check each order's status.

  === "Legacy Order List"

      1.  **Open the page**: Sign in to the CYBERBIZ admin and click **"Orders" >
   "All Orders"**.
      2.  **Find the orders to change**: Use the **Delivery Status**
  filter at the top to narrow the list to "Preparing" orders.
      3.  **Select orders**: Select one or more orders to revert in the order list.
      4.  **Open the action menu**: After you select orders, the **"Actions"**
  drop-down appears at the upper right of the list. Open it.
      5.  **Click "Unshipped"**: Select **Unshipped** in the menu.
      6.  **Done**: The system updates immediately, and the order's delivery status changes back to
  "Unshipped."

      !!! note "When the Option Appears"


  The legacy list's "Actions" menu builds its options based on the selected orders. If you don't see
  **Unshipped**, at least one selected order doesn't meet the conditions (delivery status isn't
  Preparing, a return process has started, or it uses express delivery).

  ## What You Can Do Next

  After an order is reverted to "Unshipped," it's back to paid but not yet being prepared, and you
  can continue with the following:

  *   **Edit the order**: On the order details page, edit
  **the recipient, address, delivery date, delivery time slot**, and other information.
  *   
  **Cancel the order**: If you decide not to ship, cancel the order on the order details page.
  *   **Let the customer cancel**: If you've turned on
  [customer order cancellation][orders-cancel-customer]{ data-preview
  }, the customer can cancel in "My Orders" on the storefront.
  *   **Mark as Preparing again**: After the items /
  information are updated, select
  **Preparing** in "More Actions" again to restart preparation.

  !!! tip "History Is Kept"

      For every delivery status change, the system records **in the order details history**
  an entry "{operator name} updated delivery status to Unshipped" so customer service and managers can
  trace it later.

  ## FAQ


      No. "Unshipped" only moves the **Delivery Status** back a stage and **doesn't**
  trigger a refund or change the payment status. To refund, run the refund process on the order details page separately.

  ??? question "Q2. Can I revert an order to Unshipped after printing the shipping label?"

      Yes, as long as the order's delivery status is still "Preparing" (not yet "Shipped") and it doesn't use
  express delivery. But **once a shipping label is printed, you need to void it yourself
  in the physical shipping process**. Cancel it with the carrier too, to avoid duplicate shipments.

  ??? question "Q3.
  After reverting to "Unshipped," will the customer always see the cancel order button?"

      Not necessarily. The storefront shows the "Cancel Order" button only if you've turned on
  [customer order cancellation][orders-cancel-customer]{ data-preview
  } in the admin. If it's off, the customer still needs to contact customer service to cancel.

  ??? question "Q4. Why can't express delivery (Pandago / Uber
  Direct) orders be reverted to Unshipped?"

      Express delivery dispatches couriers through an external on-demand platform. Once the order is Preparing,
  the external carrier has been notified to pick up, so the order **can't be reverted unilaterally from the CYBERBIZ
  admin**. To cancel, contact customer service or handle it on the logistics platform.

  ??? question "Q5. Can an order in the return process be reverted to Unshipped?"

      No. If the order's return status isn't "No Return Needed" or "Return Refused" (that is,
  it's Returning, Reviewing Return, Pending Refund, Returned, or similar), the system **doesn't**
  show the "Unshipped" option. If needed, handle the return process first.

  ## Related Links

  *   [Order Filters Reference][orders-filter]{ data-preview }
  *   [Customer Order Cancellation][orders-cancel-customer]{ data-preview }

  ---
  Design notes:

  1. Completed the legacy steps: the original legacy section was empty; based on index.html.haml:240
  and index.js.coffee:905
  process), the system **doesn't** show the "Unshipped" option. If needed, handle the return process first.

  ## Related Links

  *   [Order Filters Reference][orders-filter]{ data-preview }
  *   [Customer Order Cancellation][orders-cancel-customer]{ data-preview }

  ---
  Design notes:

  1. Completed the legacy steps: the original legacy section was empty; completed based on index.html.haml:240 and index.js.coffee:905
  , and stated that the legacy drop-down is named "Actions" (generated dynamically).
  2. Rewrote prerequisites: the original only mentioned return status, but the actual code (FulfillmentUnshippedHandler.ts + index.js.coffee:903-906)
  also restricts payment status, order status, and delivery method. Merged into one reference table, with the common "option not visible" issue called out separately.
  3. Added "What You Can Do Next": connects follow-up actions such as customer cancellation, order editing, and reshipping, so merchants know the next step.
  4. Added five FAQs: covering refunds, shipping labels, the storefront, express delivery, and orders being returned.
  5. Unified style: full-width punctuation throughout, spaces around bold, list items on single lines, per §B / §C rules.
  6. No internal terms exposed: no manual_unshipped, preparing_can_transfer_to_unshipped, pandago, or other
  code; described only from the merchant's perspective.

  Integration suggestions for existing docs:

  - Suggested file location: docs/orders/revert-to-unshipped.md (matches helpcenter/?p=7803 in wp_url).
  - The [orders-filter] and [orders-cancel-customer] anchors should point to existing reference tables under docs/orders/references/
  ; this article doesn't need a new reference table file.
  - This article and "Edit Order Recipient Information," "Cancel Orders," and "Preparing Settings" are sequential steps and can be linked in the sidebar as related.

  No reference table added: this feature is a single action, and all values are covered in the main table, so no extra references/ file is needed.
-->
