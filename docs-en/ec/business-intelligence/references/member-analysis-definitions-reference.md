---
title: "Member Analysis Shared Definitions"
description: "Shared statistical basis and term definitions for the Member Analysis pages, including the definition of valid orders, data update times, and how new members and new customers are identified."
created: 2026-06-16 00:00
last_modified: 2026-07-10 15:26
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
  - "Valid Orders"
  - "Member Analysis"
  - "New Members"
  - "New Customers"
  - "Customer Analysis"
  - "Data Updates"
  - "Recognized Orders"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/member-analysis-definitions-reference/"
icon: lucide/table
hide:
---

# Member Analysis Shared Definitions

This page collects the calculation basis and term definitions shared by the three tabs of the Member Analysis page ("Member Overview," "Member Analysis," and "Purchased Member Analysis") so that tutorials can link to them.
{ .subtitle }

### Valid Order Definition { #reference-member-valid-order }

The top of the Member Analysis page shows the "Valid Order Definition." All figures on the page are based on "valid orders." A valid order must meet both of these conditions:

- [x] **Order status**: not canceled.
- [x] **Return status**: no return needed or return rejected.

In other words, canceled and returned orders are **not** counted in any member analysis figures. This is the main reason page figures may differ from the total amount in the order list.

!!! note "Note"
    Some charts (such as "Average Recognized Orders per Member" and "New Member Order Rate (Recognized Orders)") are based on "recognized orders." Recognized orders use the same criteria as valid orders above: not canceled, with a return status of no return needed or return rejected.

---

### Data Update Time { #reference-member-update-time }

Member analysis figures are not real-time. They are updated in scheduled batches:

- **Traffic and conversion rate data**: updated at 5:30 p.m. the next day.
- **All other data (including member data)**: updated at midnight the next day. Canceled and returned orders are excluded in scheduled updates.

!!! note "Note"
    Because data updates the next day, figures on this page usually run through "the previous day." Orders placed and members registered today do not appear right away. This is normal.

---

### Two Definitions of New Members and New Customers { #reference-member-new-definitions }

CYBERBIZ uses two different "new / returning" rules on different tabs, each with its own basis. Before you interpret the numbers, check which tab you are looking at:

| Tab | Name | How It Is Determined |
| :-- | :-- | :-- |
| Member Analysis | New Members | Members who "registered during that month" count as new members for the month (based on registration time) |
| Purchased Member Analysis | Accumulated Customers | Number of customers who have ever ordered from store opening until the end of the specified period |
| Purchased Member Analysis | Active Customers | Number of customers whose first order falls within the specified period |
| Purchased Member Analysis | New Customers | Customers whose first order falls within the specified period |
| Purchased Member Analysis | Returning Customers | Customers who have ordered before and ordered again within the specified period |

!!! tip "Tip"
    An easy way to remember: "Member Analysis" defines new and returning by **registration time**, while "Purchased Member Analysis" defines them by **first order time**. The same customer may fall into different categories on the two tabs. This is due to the different definitions, not a data error.
