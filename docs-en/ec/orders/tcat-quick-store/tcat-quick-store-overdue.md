---
title: "EZCAT Quick Store Delivery Overdue Rules"
description: "Explains when EZCAT Quick Store Delivery (ambient, refrigerated, frozen) orders count as overdue and how return fees are charged."
created: 2026-05-27 10:50
last_modified: 2026-07-22 16:16
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans:
plan_options: []
cyb_extensions: []
intents:
  - 了解黑貓快速到店逾期判定
  - 了解黑貓快速到店退貨運費計算
  - 查詢黑貓快速到店 CYBER 幣扣抵規則
features:
  - 黑貓快速到店
  - 逾期未取判定
  - 退貨運費
  - CYBER 幣扣抵
prerequisites: []
related:
  - ec/orders/references/return-refund-status-reference/
  - ec/orders/returns-refunds/cvs-unclaimed-order/
tags:
  - EC
  - "EZCAT TA-Q-BIN"
  - "Quick Store Delivery"
  - Unclaimed
  - "Return Shipping Fees"
  - "CYBER Coins"
  - "Logistics Rules"
  - Reference
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/tcat-quick-store/tcat-quick-store-overdue/"
comments: ""
search:
  exclude: false
icon: lucide/clock-alert
hide:
---

T-CAT Rapid-to-Store Delivery (room-temperature / refrigerated / frozen) is a special logistics service run with convenience stores. Its overdue rules and return fee rules differ from regular 7-11, FamilyMart, and Hi-Life convenience store logistics. This article explains when orders count as overdue and how fees are calculated.

## Overview { #intro-tcat-quick-store-overdue }

With T-CAT Rapid-to-Store Delivery, T-CAT TA-Q-BIN delivers products to the convenience store the customer chose. If the customer doesn't pick up in time, T-CAT returns the products. T-CAT charges the merchant the return shipping fee based on its official rates.

## Overdue Rules { #specs-tcat-quick-store-overdue-days }

| Temperature Zone | Logistics Code | Overdue Rule |
| :-- | :-- | :-- |
| Room-temperature | T-CAT Rapid-to-Store Delivery - Room-temperature | If the customer hasn't picked up 4 days after shipping (D+3), the system marks the order as overdue |
| Refrigerated | T-CAT Rapid-to-Store Delivery - Refrigerated | Same as above |
| Frozen | T-CAT Rapid-to-Store Delivery - Frozen | Same as above |

!!! note "Notes"
    CYBERBIZ sets the overdue period based on T-CAT's official rules. Merchants can't change it.

## Fee Calculation { #reference-tcat-quick-store-overdue }

### How Fees Are Charged { #reference-tcat-quick-store-overdue-billing }

If a customer doesn't pick up a T-CAT Rapid-to-Store Delivery order in time, a **return shipping fee** applies. The total shipping fee charged to the merchant is:

> **Outbound shipping fee + Return shipping fee**

* **Outbound shipping fee:** Deducted in CYBER Coins by package size when the customer places the order.
* **Return shipping fee:** Deducted again by T-CAT after the customer fails to pick up in time.

---

### Rate Basis { #reference-tcat-quick-store-overdue-rate }

| Temperature Zone | Billing Basis |
| :-- | :-- |
| T-CAT Rapid-to-Store Delivery - Room-temperature | T-CAT's official room-temperature size-based rates (by package size / weight) |
| T-CAT Rapid-to-Store Delivery - Refrigerated | T-CAT's official refrigerated size-based rates |
| T-CAT Rapid-to-Store Delivery - Frozen | T-CAT's official frozen size-based rates |

!!! warning "Note"
    The actual return shipping fee follows T-CAT's latest published rates and varies by package size (such as 60 cm, 90 cm, and 120 cm). Refer to the latest T-CAT Rapid-to-Store Delivery contract terms you signed with CYBERBIZ / T-CAT.

---

### CYBER Coin Deductions { #reference-tcat-quick-store-overdue-coin }

* Both outbound and return shipping fees are deducted from the merchant account in **CYBER Coins**.
* Every deduction is recorded in the CYBER Coin usage history in the admin for later reconciliation.

## Important Notes { #specs-tcat-quick-store-overdue-notes }

* **"Quick Store Delivery - Ambient" orders can only use ambient shipping rates**, and the same applies to refrigerated and frozen. If you mix them, the system blocks it and shows the related error.
* Refund conditions for unclaimed T-CAT Rapid-to-Store Delivery orders are the same as for regular convenience store logistics. See [Automatic Refund Support](../references/return-refund-status-reference.md#reference-overdue-cvs-refund-flow-auto-refund){ title="Return and Refund Statuses (Unclaimed Convenience Store Orders)" }.

## See Also { #reference-tcat-quick-store-overdue-ref }

* [Handle Unclaimed Convenience Store Orders](../returns-refunds/cvs-unclaimed-order.md){ title="Handle Unclaimed Convenience Store Orders" }
* [Return and Refund Statuses](../references/return-refund-status-reference.md){ title="Return and Refund Statuses (Unclaimed Convenience Store Orders)" }
