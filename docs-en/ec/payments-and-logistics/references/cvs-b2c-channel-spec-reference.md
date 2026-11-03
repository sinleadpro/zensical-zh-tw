---
title: "Convenience Store Bulk Consignment B2C Channel Specifications"
description: "Summarizes the weight and volume limits for each B2C convenience store bulk consignment channel, for reference when setting up shipping methods and creating products."
created: 2026-05-25 21:42
last_modified: 2026-07-01 11:28
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
tnb: ""
plans:
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - EC
  - Convenience_Store_Pickup
  - B2C
  - Bulk_Consignment
  - Weight_Limit
  - Volume_Limit
  - Application_Fields
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
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/references/cvs-b2c-channel-spec-reference/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

## Weight and Volume Limits { #reference-cvs-b2c-channels-specs }

| Channel | Weight Limit | Sum of Three Sides | Longest Side |
| :-- | :-- | :-- | :-- |
| 7-ELEVEN Convenience Store Pickup | < 10 kg | ≤ 105 cm | ≤ 45 cm |
| FamilyMart Convenience Store Pickup | ≤  10 kg | ≤  120 cm | Per official announcement |
| FamilyMart Frozen Convenience Store Pickup | ≤  5 kg | ≤ 105 cm | Per official announcement |
| Hi-Life Convenience Store Pickup | ≤  10 kg | ≤ 105 cm | ≤ 45 cm |

!!! note "Notes"
    * If the weight or volume entered when creating a product exceeds the limit, the storefront automatically blocks customers from selecting this delivery method.
    * The actual limits follow the official announcements from each convenience store at the time of application.

---

## Required Fields When Applying { #reference-cvs-b2c-channels-fields }

Field differences by channel on the "Merchant Information Application" page:

| Field | 7-ELEVEN | FamilyMart | FamilyMart Frozen | Hi-Life |
| :-- | :--: | :--: | :--: | :--: |
| Company Name | ✅ | ✅ | ✅ | ✅ |
| Contact Name | ✅ | ✅ | ✅ | ✅ |
| Contact Email | ✅ | ✅ | ✅ | ✅ |
| Return Address | ✅ | ✅ | ✅ | ✅ |
| Company Phone | ✅ | ✅ | ✅ | ✅ |
| Return Method | ✅ | ✅ | — | ✅ |
| Return Frequency | ✅ | ✅ | — | ✅ |
| Merchant Alias | ✅ | — | — | — |
| Unified Business Number | ✅ | — | — | — |
| Company Website | ✅ | — | — | — |
| Product Type | ✅ | — | — | — |
| Designated Collection Date | — | — | ✅ | — |
| Warehouse Store Name | — | — | ✅ | — |
| Business Hours | — | — | ✅ | — |
| Closed Days | — | — | ✅ | — |

!!! note "Notes"
    * 7-ELEVEN requires additional company information and product type verification, so it has the most required fields.
    * FamilyMart Frozen involves cold-chain storage and requires additional warehouse information.
    * Fields are synced to each convenience store system after submission, so they must be entered accurately.
