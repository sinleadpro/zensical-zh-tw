---
title: "Order Auto-Close Types"
description: "Lists the closing types, trigger conditions, and required order statuses for order auto-close settings, for reference by checkout and payment and logistics settings."
created: 2026-06-16 00:00
last_modified: 2026-06-27 23:07
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
plans: []
plan_options: []
tags:
  - Auto-Close
  - "Closing Types"
  - "Order Status"
  - Reference
permalink: "https://help.cyberbiz.io/ec/orders/references/order-auto-close-types-reference/"
icon: lucide/check-circle-2
hide:
---

# Order Auto-Close Types

This table lists the closing types, trigger conditions, and required order statuses in Order Auto-Close Settings, for reference by checkout and payment and logistics settings.

## Auto-Close Types { #order-auto-close-types }

| Closing Type | Trigger Condition | Required Order Status | Use Case |
| :-- | :-- | :-- | :-- |
| N days after the customer picks up the order | The integrated logistics (convenience store, EZCAT, and so on) delivery status has been "Received" for N days | Paid / Cash on Delivery, Picked Up, No Return Needed | You use integrated logistics, so the system knows when the customer picks up |
| N days after the order ships | The custom logistics delivery status has been "Shipped" for N days | Paid / Cash on Delivery, Shipped, No Return Needed | You use custom logistics, so the system can't tell whether the order was picked up |
| Ticket orders (N days after the customer pays) | N days have passed since the customer paid | Paid | Ticket products; profit sharing is calculated after closing |

!!! note "Notes"
    * "After the customer picks up the order" and "After the order ships" are mutually exclusive. Choose the one that matches the logistics type you mainly use.
    * Example: If you set 7 days, an order picked up (or shipped) on January 1 is automatically closed on January 8.
    * Ticket order auto-close appears only when the ticket feature is turned on.
    * After an order is closed, the system settles and issues purchase bonus points and profit sharing. To set whether bonus points are returned when an order is returned, use Bonus Settings for Order Cancellations and Returns.
