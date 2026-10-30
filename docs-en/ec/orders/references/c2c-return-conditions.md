---
title: "7-Eleven C2C Return Service: Conditions for Sending"
description: "Explains the order conditions for sending a 7-Eleven C2C return code, and what to do when any condition isn't met."
created: 2026-05-26 14:24
last_modified: 2026-07-08 11:13
lang: en-US
type: reference
author: Jase
tags:
  - EC
  - 7-Eleven
  - C2C
  - "Return Service"
  - "Return Codes"
  - "Order Status"
  - "Delivery Progress"
  - Reference
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
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/c2c-return-conditions/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

After you select orders in the order list, the system checks the following conditions to decide whether the batch action is available. If any condition isn't met, you can't send a return code.

## Basic Conditions { #reference-seven-eleven-c2c-return-eligibility-basic }

| Condition | Rule | If Not Met |
| :-- | :-- | :-- |
| Feature enabled | The store has applied for and turned on 7-Eleven C2C Return Service | The option doesn't appear in the batch action menu |
| Order amount | The order total must be **less than NT$20,000** | The order is excluded and can't be sent |
| Delivery type | The order uses only one delivery type | Orders with multiple delivery types (split orders) can't be sent in batches |
| Return already requested | The order isn't in "Reviewing Return" or "Returned" status | Each order can request a return only once |


## Delivery Type × Delivery Progress Matrix { #reference-seven-eleven-c2c-return-eligibility-matrix }

An order must match one of the following combinations to send a return code:

| Delivery Type | Delivery Progress That Allows Sending | Description |
| :-- | :-- | :-- |
| **CYBERBIZ logistics** | Shipped / Arrived / Received | Includes logistics integrated by CYBERBIZ, such as EZCAT, HCT, Pelican Express, and convenience store pickup |
| **Other logistics** | Received only | For packages you send yourself or logistics not integrated by CYBERBIZ, you must confirm the shopper received the order before sending a return code |

!!! info "Why the Difference?"
    The system can't track actual delivery progress for other logistics, so it confirms the shopper received the items only after you manually mark the order as "Received." This prevents sending a return code while the package is still in transit, which could lead to lost packages.

## Return Status Conditions { #reference-seven-eleven-c2c-return-eligibility-return-status }

The order's return status must be one of the following three:

| Return Status | Scenario |
| :-- | :-- |
| **No Return Needed** | Default status for regular orders; the shopper hasn't requested a return |
| **Return Requested** | The shopper requested a return in the member center and is waiting for your response |
| **Returning** | A return code was already sent (used to resend or reissue a code) |

!!! note "Notes"
    If the order is already in "Reviewing Return" or "Returned," the system treats the return process as started or completed and doesn't allow sending the code again. To resend (for example, if the code expired), contact CYBERBIZ customer service first to handle the order status.

## FAQ

??? quote "When can't an order use 7-Eleven C2C Return Service?"
    [](){ #faq-seven-eleven-c2c-return-eligibility-basic-unmet }

    If any of the following conditions isn't met, you can't send a return code:

    - [x] **The order amount exceeds NT$20,000**: This exceeds the hard limit of the 7-Eleven logistics system, so use another return method.
    - [x] **The order uses multiple delivery types**: Only orders with a single delivery type are supported. Split orders can't be sent in batches.
    - [x] **The order is already in "Reviewing Return" or "Returned"**: Each order can get a return code only once.

??? quote "Why do CYBERBIZ logistics and other logistics have different delivery progress conditions?"
    [](){ #faq-seven-eleven-c2c-return-eligibility-logistics-diff }

    It's because of differences in what the system can track:

    - **CYBERBIZ logistics** (EZCAT, HCT, Pelican Express, convenience store pickup, and so on): The system tracks delivery progress in real time, so it supports three statuses: **Shipped / Arrived / Received**.
    - **Other logistics** (packages you send yourself, not integrated): The system can't track actual delivery progress, so it confirms delivery only after you manually mark the order as "Received." This prevents sending a return code while the package is in transit, which could lead to lost packages.

??? quote "Can I resend a return code for an order that already got one?"
    [](){ #faq-seven-eleven-c2c-return-eligibility-resend }

    Yes, if the following conditions are met:

    - The order's return status is "Returning" (meaning a code was already sent).
    - If the code expired (after its 7-day validity), contact [CYBERBIZ customer service](#){ data-preview } to handle the order status and resend it.
    - Orders already in "Reviewing Return" or "Returned" can't get a code again.

