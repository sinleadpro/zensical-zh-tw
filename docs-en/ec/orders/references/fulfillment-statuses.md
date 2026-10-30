---
title: "Delivery Status Reference"
description: "Lists the delivery statuses (Unshipped, Shipped, Received, and more) in the CYBERBIZ new order list and when they appear, for reference in search, filters, and shipping."
created: 2026-06-04 15:06
last_modified: 2026-07-02 08:53
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - "Delivery Status"
  - "Order List"
  - "Shipping Management"
  - "Arrived at Store"
  - Unclaimed
  - "Shipping Exceptions"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/fulfillment-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

This table lists the delivery statuses in the CYBERBIZ new order list, for reference in search, filters, and shipping.

## Delivery Statuses { #fulfillment-statuses-table }

| Delivery Status | Description | When It Appears |
| :-- | :-- | :-- |
| Unshipped | Shipping hasn't been arranged | Default status after the order is placed |
| Preparing | Items are being prepared; no shipping label yet | Marked manually by the merchant, or when an integrated warehouse starts processing |
| Partially Shipped | Some items in the order have shipped, and some haven't | After you select items to ship one by one on the order details page |
| Shipped | A shipping label was generated, or the order was marked as shipped | After you download a shipping label, ship with custom logistics, or import tracking numbers |
| Arrived at Store | The convenience store pickup package arrived at the chosen store | Arrival report from convenience store pickup logistics |
| Received | The customer picked up or signed for the package | Reported by the carrier, or marked manually by the merchant |
| Unclaimed | The convenience store pickup package wasn't picked up within the holding period | Overdue report from convenience store pickup |
| Shipping Exception | A problem occurred during delivery | The carrier reports an exception |
| Returned | The items were returned | After the return process is complete |
| Shipment Canceled | The original shipment was canceled | The merchant cancels the shipment |
| No Shipping Needed | The order needs no physical delivery | Digital-only products, e-tickets, and so on |

!!! note "Notes"
    * The delivery statuses you see depend on the product type and logistics used. Not every order goes through all of the statuses above.
    * "Arrived at Store" and "Unclaimed" apply only to convenience store pickup logistics, not regular home delivery.
    * Orders that need no delivery, such as digital products and e-tickets, show "No Shipping Needed."
