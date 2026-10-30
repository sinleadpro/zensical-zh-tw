---
title: "Return and Refund Statuses (Unclaimed Convenience Store Orders)"
description: "Reference of how delivery status, return status, and payment status change when a convenience store order goes unclaimed"
created: 2026-05-27 10:45
last_modified: 2026-07-09 12:04
lang: en-US
type: reference
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
  - 查看超商逾期未取退款流程
  - 了解退貨退款狀態流轉
features:
  - 超商逾期未取
  - 自動退款
  - 人工退款
  - 部分出貨退款
prerequisites: []
related:
  - ec/orders/references/auto-refund-timeline/
  - ec/orders/returns-refunds/cvs-unclaimed-order/
  - ec/orders/tcat-quick-store/tcat-quick-store-overdue/
tags:
  - "Unclaimed Convenience Store Orders"
  - "Return Status"
  - "Refund Status"
  - EC
  - "Convenience Store Logistics"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/return-refund-status-reference/"
comments: false
search:
  exclude: false
icon: lucide/table
hide: []
---

This reference summarizes how the **Delivery Status**, **Return Status**, and **Payment Status** change when a convenience store order is unclaimed, and the combined conditions that trigger automatic refunds.

## Overview { #intro-overdue-cvs-refund-flow }

After the convenience store system marks an order as unclaimed, the CYBERBIZ admin updates three fields:

* **Delivery Status** (shipping progress)
* **Return Status** (where the returned items are)
* **Payment Status** (refund progress)

How these three statuses update depends on whether the whole order shipped together, whether the payment method supports automatic refunds, and whether you turned on related features.

## Status Changes { #reference-overdue-cvs-refund-flow-status-transition }

### Whole Order Shipped with One Convenience Store Carrier { #reference-overdue-cvs-refund-flow-status-transition-whole }

| Stage | Delivery Status | Return Status | Payment Status |
| :-- | :-- | :-- | :-- |
| Shipped | Shipped | No Return Needed | Payment Received |
| Customer didn't pick up in time (system determined) | Unclaimed | Transit Center[^1] | Payment Received → Pending Refund |
| Automatic refund completed | Unclaimed | Transit Center → Returned | Refunded |
| Items returned | Unclaimed | Returned | Refunded |

[^1]: If you turned on "No Automatic Refund for Unclaimed Convenience Store Orders," the return status becomes "Original Sender Store" instead of "Transit Center," and waits for you to check the items.

---

### Partial Shipment <small>First Shipment by Convenience Store + Second by Other Logistics</small> { #reference-overdue-cvs-refund-flow-partial }

| Stage | First Shipment Delivery Status | Second Shipment Delivery Status | Return Status | Payment Status |
| :-- | :-- | :-- | :-- | :-- |
| Both shipments shipped | Shipped | Shipped | No Return Needed | Payment Received |
| First convenience store shipment unclaimed | Unclaimed | Shipped (unchanged) | Original Sender Store | Payment Received (**doesn't automatically change to Pending Refund**) |
| Manual refund after you check | Unclaimed | Shipped | Returned | Refunded |

!!! warning "Note"
    For partial shipments, even if your store would otherwise qualify for automatic refunds, an unclaimed convenience store shipment **doesn't** trigger an automatic refund. Check the items and then refund manually.

---

## Automatic Refund Support { #reference-overdue-cvs-refund-flow-auto-refund }

### Payment Methods That Support Automatic Refunds { #reference-overdue-cvs-refund-flow-auto-refund-payment }

For each payment provider's automatic refund coverage and deadlines, see the [Automatic Card Refund Time Limits](auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" data-preview }.

For unclaimed convenience store orders (not picked up within 4–7 days), every payment method that supports automatic refunds is well within its refund deadline, so **the payment deadline usually isn't an issue**. Whether an automatic refund is triggered depends on the combined conditions below.

---

### Combined Conditions for Automatic Refunds { #reference-overdue-cvs-refund-flow-auto-refund-conditions }

An order must meet **all** of the following conditions for the system to refund automatically after it's marked unclaimed:

- [x] **Delivery status:** Changes from "Shipped" to "Unclaimed"
- [x] **Payment status:** Is "Payment Received"
- [x] **Payment method:** Is listed in the [Automatic Card Refund Time Limits](auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" data-preview } (and still within the refund deadline)
- [x] **Whole order shipped with the same convenience store carrier:** Not a partial shipment
- [x] **"No Automatic Refund for Unclaimed Convenience Store Orders" isn't turned on**
- [x] **Your plan supports automatic refund payment methods**

If any condition isn't met, the order goes through the manual refund process, and you enter the customer's refund information on the order details page.

## Return Status Meanings { #reference-overdue-cvs-refund-flow-return-status }

| Return Status | Description |
| :-- | :-- |
| No Return Needed | Default value; the order hasn't entered the return process |
| Transit Center | The items have been sent from the original sender store to the convenience store logistics warehouse. Default value for automatic refunds of unclaimed orders |
| Original Sender Store | The items are still at the original sender store, waiting for you to pick them up. Default value when "No Automatic Refund for Unclaimed Convenience Store Orders" is turned on |
| Returning | The items are on their way back |
| Returned | The items are back with you and the return process is complete |
| Shipping Exception | An exception occurred while the return was in transit |

---

## References { #reference-overdue-cvs-refund-flow }

* [Handle Unclaimed Convenience Store Orders](../returns-refunds/cvs-unclaimed-order.md){ title="Handle Unclaimed Convenience Store Orders" }
* [Automatic Card Refund Time Limits](auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" }
* [EZCAT Quick Store Delivery Overdue Rules](../tcat-quick-store/tcat-quick-store-overdue.md){ title="EZCAT Quick Store Delivery Overdue Rules" }



