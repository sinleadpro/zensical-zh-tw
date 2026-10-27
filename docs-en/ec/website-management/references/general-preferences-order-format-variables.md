---
title: "Order Number Format Variable Reference"
description: "Lists the variables available for the order number format, with descriptions and usage limits for variables such as the order sequence number, random numbers, and date and time."
created: 2026-06-26 10:00
last_modified: 2026-06-26 10:00
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
difficulty: ""
tnb: ""
plans: []
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - "Order Number"
  - "Format Variables"
  - "Order Settings"
  - "General Settings"
  - Reference
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/references/general-preferences-order-format-variables/"
comments: false
search:
  exclude: false
icon: lucide/table
hide: []
---

# Order Number Format Variables

Use these variables in the **Standards and Formats** section of **General** to set how order numbers look. When an order is made, the system puts the real value in place of each variable.

| Variable | Represents | Description |
| :-- | :-- | :-- |
| `{{number}}` | Order sequence number | A number the system increments automatically, for example `1234`. This variable is required |
| `{{random}}` | 6-digit random number | A randomly generated 6-digit number |
| `{{random:N}}` | N-digit random number | A random number with the number of digits you set, up to 9 digits (for example, `{{random:4}}` gives 4 digits) |
| `{{date}}` | Order date | The full date the order was created |
| `{{year}}` | Year | The year the order was created |
| `{{month}}` | Month | The month the order was created |
| `{{today}}` | Day | The day of the month the order was created |
| `{{hour}}` | Hour | The hour the order was created |
| `{{minute}}` | Minute | The minute the order was created |
| `{{second}}` | Second | The second the order was created |
| `{{timestamp}}` | Timestamp | The timestamp when the order was created |

!!! note "Notes"
    * The format **must include** `{{number}}` and can't be longer than 64 characters. If not, you can't save it.
    * The default format is `#{{number}}`, which displays as, for example, `#1234`.
    * A new format only applies to new orders. Old order numbers stay the same.
