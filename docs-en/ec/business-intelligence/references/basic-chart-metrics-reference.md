---
title: "Basic Report Calculation Rules Reference"
description: "Learn the calculation rules for the four core sections of the basic report: order count, total sales, product sales ranking, and page views over the last 7 days."
created: 2026-06-21 00:00
last_modified: 2026-07-09 15:55
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
products:
  - EC
plan_options: []
modules: []
sites:
  - TW
audiences:
  - merchant
tags:
  - "Report Analysis"
  - "Basic Reports"
  - "Order Count"
  - "Total Sales"
  - "Product Sales Ranking"
  - "Page Views"
  - "Calculation Rules"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/basic-chart-metrics-reference/"
icon: lucide/table
hide:
---

## Calculation Rules for Each Basic Report Section { #reference-basic-chart-metrics }

| Report | What It Counts | Inclusion / Recognition | Update Frequency |
| :-- | :-- | :-- | :-- |
| Order Count | Number of valid orders in each month of the selected period | Excludes canceled and returned orders | Real time |
| Total Sales | Total amount of valid orders in each month of the selected period | Excludes canceled and returned orders | Real time |
| Product Sales Ranking | Top 10 products by sales in the specified date range | Counts only valid orders that were not returned; amount = quantity sold × transaction unit price | Real time (calculated at export) |
| Page Views in the Last 7 Days | Daily visits to the store home page over the past 7 days | Each visit to the home page counts once; duplicates are not removed | Previous day's data compiled daily |

!!! note "Note"
    * "Real time" means the data is calculated from the latest orders when you view or export it. "Compiled daily" means you see the previous day's data the next day.
    * The date range for "Product Sales Ranking" is set by that section's start and end dates. It is independent of the period menu in the upper-right corner of the page (6 months / 1 year / 3 years / 5 years).
