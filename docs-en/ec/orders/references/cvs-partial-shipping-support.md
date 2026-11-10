---
title: "Convenience Store Partial Shipment Support"
description: "Lists which convenience store logistics types support partial shipment: which can ship multiple times normally and which must use custom shipping instead."
created: 2026-05-26 18:41
last_modified: 2026-07-02 08:51
lang: en-US
type: guide
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
tnb: ""
plans:
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - "Convenience Store Pickup"
  - "Partial Shipment"
  - C2C
  - B2C
  - "Logistics Support"
  - "Order Management"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/cvs-partial-shipping-support/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


### Convenience Store Logistics That Support Partial Shipment { #reference-cvs-partial-supported }

| Logistics Type | Description | Partial Shipment Flow |
| :-- | :-- | :-- |
| 7-11 Store-to-Store (C2C) | The merchant drops off the package at a convenience store, and the recipient picks it up at the chosen store | First shipment through the convenience store; ship the rest with custom shipping |
| 7-11 Store Pickup (B2C) | The merchant ships through convenience store logistics to the chosen store, and the customer picks it up (including cash on delivery) | First shipment through the convenience store; ship the rest with custom logistics |
| FamilyMart Store-to-Store (C2C) | The merchant drops off the package at a convenience store, and the recipient picks it up at the chosen store | First shipment through the convenience store; ship the rest with custom shipping |
| FamilyMart Store Pickup (B2C) | The merchant ships through convenience store logistics to the chosen store, and the customer picks it up (including cash on delivery) | First shipment through the convenience store; ship the rest with custom logistics |
| Hi-Life Store-to-Store (C2C) | The merchant drops off the package at a convenience store, and the recipient picks it up at the chosen store | First shipment through the convenience store; ship the rest with custom shipping |
| Hi-Life Store Pickup (B2C) | The merchant ships through convenience store logistics to the chosen store, and the customer picks it up (including cash on delivery) | First shipment through the convenience store; ship the rest with custom logistics |
| Hi-Life Frozen Pickup | Convenience store pickup for frozen products | First shipment through the convenience store; ship the rest with custom shipping |

### Logistics with a Separate Flow { #reference-cvs-partial-other }

The following logistics are convenience store pickup, but they use the CYBERBIZ-managed shipping label flow, so they **can ship multiple times normally** (print a new shipping label each time). The "ship the second shipment with custom shipping" rule doesn't apply:

- T-CAT Rapid-to-Store Delivery (Room-temperature)
- T-CAT Rapid-to-Store Delivery (Refrigerated)
- T-CAT Rapid-to-Store Delivery (Frozen)
