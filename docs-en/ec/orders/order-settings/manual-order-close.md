---
title: "How to Manually Close Orders"
description: "Manually close orders one at a time or in batches, and how closing affects bonus points, coupons, and profit sharing."
created: 2026-05-06 15:57
last_modified: 2026-06-30 09:20
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
  - 手動結案訂單
features:
  - 訂單結案
  - 購物紅利
  - 滿額贈送優惠券
  - 第三方分潤
prerequisites: []
related:
  - ec/orders/basics/search-filter-orders/
  - ec/orders/basics/order-management-interface/
  - ec/orders/order-settings/auto-close-order-settings/
tags:
  - "Order Closing"
  - "Manual Closing"
  - "Order Management"
  - "Bonus Points"
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
  - https://www.cyberbiz.io/helpcenter/?p=192
  - https://www.cyberbiz.io/support/?p=1677
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/manual-order-close/"
comments: false
search:
  exclude: false
icon: lucide/check
hide: []
---

![Close order](../../../assets/images/EC-訂單詳情頁-結案訂單-hero.en.png){ title="Close Order" .hero-page }

## About Manually Closing Orders

**Manually closing an order** formally closes the order status. Closing not only ends order processing but also triggers several marketing rewards and profit sharing calculations.

!!! info "What Closing Means and Its Effects"

    Once an order is closed, the system automatically does the following, and **even if the order is later canceled or returned, the results aren't automatically reversed or changed**:

    *   **Issues purchase bonus points**: The bonus points earned from the order are officially credited to the account, and the customer can start using them.
    *   **Activates coupons**: If a campaign includes "coupon for spending over a threshold," customers can claim and use the coupon only after the order is closed.
    *   **Calculates profit sharing**: If the order involves third-party profit sharing (such as a referrer), the system calculates the profit sharing amount when the order is closed.
    *   **Clears admin reminders**: After closing, the "Open Orders" count reminder in the admin left menu is cleared.

!!! warning "Adjust Bonus Points Manually"
    If you need to deduct or delete points after closing, the system won't reverse them automatically. Do it manually: go to Members > All Members, open the customer's details page, and deduct them there.

## Prerequisites

- [x] **Order Status**: Any order except "Canceled" can be closed.
- [x] **Delivery status recommendation**: We recommend closing an order after its return and exchange period ends and you're sure there are no returns. Orders that are "Partially Shipped" can't be closed automatically; you need to adjust them manually.
- [x] **Relation to reconciliation**: Manual closing isn't directly related to financial reconciliation. Reconciliation is based mainly on the delivery status (such as "Shipped" or "Received").

## Steps to Manually Close Orders { #close-order-manual }

You can manually close orders in two ways:

=== ":lucide-mouse-pointer-click: Single Order"

    Close from the order details page

    1.  **Open the order**: Sign in to the CYBERBIZ admin, go to **Orders > All Orders**, and click the order number of the order in the order list.
    2.  **Close it**: On the details page, click **Complete Order** in the upper-right corner.

    ![Order details page - Complete Order](../../../assets/images/EC-訂單詳情頁-結案訂單按鈕.en.png){ title="Order Details Page - Complete Order" }

=== ":lucide-check-square: Batch Action"

    Close in batches from the order list

    1.  **Admin path**: Sign in to the CYBERBIZ admin and go to **"Orders" > "All Orders"**.
    2.  **Select orders**: Select one or more orders to close.
    3.  **Choose the action**: Click **Actions...** above the list, select **Complete Order** in the drop-down menu, and confirm.

    ![Order list - Complete Order](../../../assets/images/EC-訂單-訂單列表-結案訂單.en.png){ title="Order List - Complete Order" }

## Check the Status After Closing

### Completed Orders List

After orders are closed, you can use the order list filter to create a "Completed" [order view group](../basics/search-filter-orders.md#orders-groups-tabs){ title="How to Search and Filter Orders" data-preview } to check closed orders.

![Completed orders](../../../assets/images/EC-訂單-訂單列表-已結案群組.en.png){ title="Completed Orders" }

---

### Order Closing History

The [order activity log](../basics/order-management-interface.md#order-history){ title="Order Management Interface" } at the bottom of the order details page shows an "Order closed" message and the name of the admin who closed it.

![Order closing history](../../../assets/images/EC-訂單詳情頁-操作紀錄-訂單結案.en.png){ title="Order Closing History" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-calendar-check:{ .lg }  
  [__Auto-Close Settings__](auto-close-order-settings.md){ title="Set Up Order Auto-Close" }  
  Have the system close orders automatically after the delivery status has been "Received" or "Shipped" for a set number of days (N days).

</div>

## FAQ

??? quote "If a customer returns an order after it's closed, are the bonus points taken back?"

    No. Once an order is closed, the system immediately issues bonus points, activates coupons, and calculates profit sharing, and **even if the order is later canceled or returned, the results aren't automatically reversed or changed**. To delete a customer's bonus points, go to Members > All Members, open the customer's page, and delete them there.

??? quote "Can all orders be closed manually?"

    No. Orders in any status except "Canceled" can be closed.

??? quote "Can I close multiple orders at once?"

    Yes. Use the batch action in the order list: select multiple orders, click "More Actions," and select "Complete Order."

