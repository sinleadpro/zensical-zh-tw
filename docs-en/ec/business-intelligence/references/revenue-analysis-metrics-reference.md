---
title: "Revenue Analysis Metric Definitions Reference"
description: "What the data cards and revenue overview charts on the Revenue Analysis page mean and how they are calculated, including total revenue, gross profit, and growth rate."
created: 2026-06-15 00:00
last_modified: 2026-06-15 00:00
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
  - EC
  - "Report Analysis"
  - "Revenue Analysis"
  - "Total Revenue"
  - "Gross Profit"
  - "Growth Rate"
  - "Metrics Reference"
  - Reference
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/revenue-analysis-metrics-reference/"
icon: lucide/table
hide:
---

This page explains the meaning and calculation basis of each data card and the "Revenue Overview" chart on the "Revenue Analysis" page.

### Revenue Metric Definitions { #reference-revenue-metrics }

| Metric | What It Means | Calculation Basis |
| :-- | :-- | :-- |
| Total Revenue | Cumulative revenue from valid orders across the store | Sum of recognized order amounts |
| Revenue in the Last 30 Days | Revenue in the last 30 days | Sum of recognized order amounts |
| Revenue Growth Rate in the Last 30 Days | Percentage growth of revenue in the last 30 days compared with the preceding period of the same length | (Current period revenue − previous period revenue) ÷ previous period revenue |
| Gross Profit in the Last 30 Days | Revenue from orders placed in the last 30 days minus product costs | Revenue from placed orders − total product cost |
| Gross Margin in the Last 30 Days | Gross profit as a share of revenue in the last 30 days | Gross profit ÷ revenue |
| Undiscounted Revenue | Total amount of valid orders across the store before discounts | Sum of valid order amounts before discounts |
| Active Order Revenue | Total revenue from valid orders across the store | Sum of valid order amounts |
| Canceled Order Revenue | Total amount of canceled orders across the store | Sum of canceled order amounts |
| Returned Order Revenue | Total amount of returned orders across the store | Sum of returned order amounts |
| Unclaimed Order Revenue | Total amount of orders not picked up in time across the store | Sum of unclaimed order amounts |
| Cost | Total cost price of all products in placed orders across the store | Sum of each product's cost price × quantity |
| Gross Profit | Revenue from placed orders minus total product cost | Revenue from placed orders − total product cost |

!!! note "Note"
    * "Recognized orders" are orders that are not canceled and whose return status is no return needed or return rejected. See [Recognized Order Definition](../revenue-analysis.md#prerequisites-revenue-counted-orders){ title="Recognized Order Definition" } in the Revenue Analysis article.
    * "Gross Profit" and "Cost" can be calculated correctly only after you enter cost prices in product settings. If a product has no cost set, its cost counts as 0 for that order, which inflates gross profit.
    * A positive "growth rate" is shown starting with `+`, and a negative one with a minus sign.