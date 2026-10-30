---
title: "Convenience Store Shipping Label Validity"
description: "Lists the deadlines after which each convenience store's B2C and C2C shipping labels must get a new tracking number."
created: 2026-08-27 11:06
last_modified: 2026-08-27 11:21
lang: en-US
type: reference
status: ""
author: Ann
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
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents: 
  - 查詢超商託運單失效期限
  - 確認重新取號時間
features: 
  - 超商託運單失效期限
  - 補印託運單
  - 逾期重新取號
prerequisites: []
related:
  - ec/orders/renew-waybill-after-expiration/
tags: []
acoiv: ""
apis: []
devices: []
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/cvs-waybill-expiration-reference/"
comments: false
search:
  exclude: false
icon: lucide/calendar-clock
hide: []
---

## Shipping Label Validity by Carrier { #reference-cvs-waybill-expiration }

After you create a shipping label, ship within its validity period. You can **reprint a shipping label only within its validity period**. If the label expires and has no delivery record, it's automatically voided and can't be reprinted. **You need to get a new tracking number for a new shipping label**.

The table below lists the shipping label validity for each convenience store carrier:

> **D** in the table is the day the shipping label is first printed.


| Service Type | Convenience Store | Label Validity | Store Drop-Off Deadline |
| :--- | :--- | :--- | :--- |
| B2C | 7-Eleven | D+14 days | D+15 days |
| B2C | FamilyMart (ambient / frozen) | D+6 days | D+7 days |
| B2C | Hi-Life | D+6 days | D+7 days |
| C2C | 7-Eleven | D+7 days | D+7 days |
| C2C | FamilyMart (ambient / frozen) | D+7 days | D+7 days |
| C2C | Hi-Life | D+7 days | D+7 days |

## Related Tasks


<div class="grid cards" markdown>

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Shipping Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label is voided or past its reprint deadline, get a new tracking number and download a new shipping label.

</div>