---
title: "OMO Analysis Report Shared Definitions"
description: "Shared statistical basis and term definitions used across the tabs of the OMO Analysis Report, for linking from tutorial docs."
created: 2026-06-23 10:00
last_modified: 2026-06-23 10:00
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules: []
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
  - OMO
  - Omnichannel
  - "Valid Orders"
  - "Repurchase Rate"
  - "Average Order Value"
  - AOV
  - "Revenue Heat Map"
  - "Comparison Period"
  - POS
  - Reference
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/omo-definitions-reference/"
comments: false
search:
  exclude: false
icon: lucide/table
hide:
---

# OMO Analysis Report Shared Definitions

This page collects the calculation basis and term definitions shared by all tabs of the OMO analysis report so that tutorials can link to them.
{ .subtitle }

### Valid Order Definition { #reference-omo-valid-order }

The top of the report shows the "Valid Order Definition." All figures in the OMO analysis report are based on valid orders. A valid order must meet both of these conditions:

- [x] **Order status**: not canceled.
- [x] **Return status**: no return needed or return rejected.

In other words, canceled and returned orders are **not** counted in any report figures. This is the main reason report figures may differ from the total amount in the order list.

---

### Data Update Time { #reference-omo-update-time }

Report figures are not real-time. They are updated in scheduled batches:

- **Traffic and conversion rate data**: updated at 5:30 p.m. the next day.
- **All other data (including revenue, orders, and members)**: updated at midnight the next day. Canceled and returned orders are excluded in scheduled updates.

!!! note "Note"
    Because data updates the next day, report figures usually run through "the previous day." Orders placed and members registered today do not appear right away. This is normal.

---

### Comparison Period Options { #reference-omo-compare }

When you set the analysis period, you can choose a comparison basis. The report shows the figures for the selected period side by side with the comparison period:

| Option | Description |
| :-- | :-- |
| Previous year | Compares with "the same period last year" |
| Previous period | Compares with a period of "the same length" immediately before the selected period |
| Previous month | Compares with "the previous month" of the selected period |
| Customize period | Lets you specify another date range as the comparison basis |

!!! note "Note"
    The comparison period defaults to "Previous year." If you choose "Customize period," you also need to set the start and end dates for the comparison.

---

### Term Definitions { #reference-omo-glossary }

| Term | Description |
| :-- | :-- |
| Revenue | EC and POS revenue for the specified period, compared with the comparison period |
| Number of Orders | EC and POS order count for the specified period, compared with the comparison period |
| Registered Members | New members registered through each channel (EC and POS) in the specified period, compared with the comparison period |
| Average Order Value (AOV) | "Total revenue ÷ total orders" for the specified period, compared with the comparison period |
| Repurchase Rate | The percentage of returning customers in the specified period, calculated as "returning customers in the period ÷ total customers who purchased in the period" |
| POS Quick Sign-In Member Registration Completion Rate | The share of members quick-registered at POS who complete their profile and registration. If your store lets customers register and check out without account verification, they count as registered right away |
| Revenue Heatmap | Shows revenue by time slot using color intensity. The darker the color, the higher the order revenue in that time slot. Use it to plan when to run marketing |
| Store Pickup / POS Store Pickup | Orders where customers chose to pick up in store. Use it to measure how well online traffic converts to orders across online and offline channels |
| Member Purchasing / Repurchasing Status | Splits EC and POS members by their "first registration source" and compares their purchase and repurchase performance in each channel |
| Number of Bonus Usage | Bonus points used (redeemed) at EC and POS in the specified period |

!!! note "Note"
    "Member purchasing status" and "Member repurchasing status" both group members by their first registration source (EC or POS), not by the channel where they ordered.
