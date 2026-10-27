---
title: "Account Status And Purchase Access Reference"
description: "Explains how customer account status (not logged in, active, warning, disabled) affects purchase access to limited products, and the messages shown at checkout."
created: 2026-06-08 17:46
last_modified: 2026-06-08 20:11
lang: en-US
type: reference
author: Jase
tags:
  - EC
  - "Member Tier"
  - "Purchase Access"
  - "Account Status"
  - "Limited Products"
  - "Login Restriction"
  - Reference
  - "Reference Table"
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
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/marketing/references/purchase-limit-account-status.en/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


### Account Status And Purchase Access Reference { #reference-purchase-limit-account }

Whether a customer can buy products in a purchase limit group depends on whether they're logged in and on their member account status. Regular (non-limited) products aren't affected.

| Customer Status | Can Buy Limited Products | Checkout Message |
| :-- | :-: | :-- |
| Not logged in (guest) | ❌ | Your cart contains limited products. Please log in to purchase. |
| Account active | ✅ | — (normal checkout) |
| Flagged as warning account | ✅ | — (normal checkout) |
| Account disabled | ❌ | Your account has been disabled. Please contact customer service if you have any questions. |
| Account not activated | ❌ | Your account isn't activated, so you can't buy limited products. |
| Account not verified | ❌ | Your account isn't activated, so you can't buy limited products. |
| Activation invite sent | ❌ | Your account isn't activated, so you can't buy limited products. |
| Activation invite declined | ❌ | Your account isn't activated, so you can't buy limited products. |

!!! note "Note"
    * Only "Account active" and "Flagged as warning account" can buy limited products. Warning accounts are flagged but can still buy as usual.
    * All other statuses, including guests who aren't logged in, can't buy limited products and see the matching message above at checkout.
    * This restriction applies only to products in a purchase limit group. Regular products aren't affected.
