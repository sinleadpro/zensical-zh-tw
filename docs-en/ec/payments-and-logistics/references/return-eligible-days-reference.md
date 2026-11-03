---
title: "Storefront Return-Eligible Days Reference"
description: "Summarizes the default return-eligible days and calculation start point for each shipping method, used by checkout and payment and logistics settings."
created: 2026-06-16 00:00
last_modified: 2026-07-06 17:33
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
  - Return_Days
  - Shipping_Method
  - Return_Eligible_Days
  - Reference
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/references/return-eligible-days-reference/"
icon: lucide/table
hide:
---

# Storefront Return-Eligible Days Reference

This table summarizes the default return-eligible days and calculation start point for each shipping method in “Return Time Adjustment Settings.” It is referenced by checkout and payment and logistics settings.

## Return-Eligible Days by Shipping Method { #return-eligible-days }

| Shipping Method | Setting Field | Default Days | Calculation Start Point |
| :-- | :-- | :-- | :-- |
| CYBERBIZ Home Delivery, CVS Pickup | Return-eligible days for CYBERBIZ home delivery and CVS pickup | 10 days | After the logistics status is “Delivered” |
| Other shipping methods (including custom logistics) | Return-eligible days for other shipping methods | 14 days | After the logistics status is “Shipped” |

!!! note "Notes"
    * Leaving the field **blank** uses the default days shown above.
    * Entering **0** in the field disables customer-initiated return requests on the storefront.
    * “Partial Return Requests” is a separate feature that must be enabled. Once enabled, customers can select the items they want to return on the return request page. The merchant still determines the refund amount for partial returns.
