---
title: "POS Revenue Analysis Metrics and Field Reference Table"
description: "Defines the sales metrics on the POS Revenue Analysis page and the Store Comparator table fields."
created: 2026-06-23 16:00
last_modified: 2026-06-23 18:47
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
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
related:
  - pos/business-intelligence/pos-revenue-analysis/
tags:
  - POS
  - "Revenue Analysis"
  - Reference
  - "Sales Amount"
  - "Average Order Value"
  - "Purchasing Members"
  - "Spend per Customer"
  - "Daily Average Sales"
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/pos/business-intelligence/references/pos-revenue-metrics-reference/"
comments: false
search:
  exclude: false
icon: lucide/table
hide:
---

# POS Revenue Analysis Metrics and Field Reference Table

This page describes the sales metrics shared by the comparators on the "POS Revenue Analysis" page and the field meanings in the "Store Comparator" ranking table. It is intended for reference by other documents.

### POS Revenue Analysis Metrics Reference Table { #reference-pos-revenue-metrics }

| Metric | Meaning | Calculation Basis |
| :-- | :-- | :-- |
| Sales Amount | Total sales for the selected store and date range | Total order amount of recognized orders |
| Order Count | Number of orders placed in the selected store and date range | Total count of recognized orders |
| Average Order Value | Average amount spent per order | Sales Amount ÷ Order Count |
| Purchasing Members | Number of members who made purchases in the date range (each counted once) | Unique purchasing members in the date range |
| Spend per Customer | Average amount contributed by each customer | Sales Amount ÷ Purchasing Members |

!!! note "Notes"
    * "Recognized orders" are orders with a status other than canceled and a return status of no return needed or return rejected. For details, see the [Recognized Order Definition](../pos-revenue-analysis.md#specs-pos-revenue-counted-orders){ title="Recognized Order Definition" data-preview }.
    * Purchasing Members and Spend per Customer only count orders from members with a linked account. Walk-in orders without a linked member are still included in Sales Amount and Order Count, but not in Purchasing Members.
    * All amounts are displayed as whole numbers (decimals are rounded).

### Store Comparator Field Reference Table { #reference-pos-revenue-store-columns }

| Field | Description |
| :-- | :-- |
| Rank | Rank automatically assigned in descending order of Sales |
| Store | POS store name |
| Sales | Total sales amount of the store in the selected date range |
| Order Count | Number of orders the store placed in the selected date range |
| Purchasing Members | Number of unique purchasing members of the store in the selected date range |
| Daily Average Sales | Average daily sales of the store in the selected date range (Sales ÷ number of days in the range) |
| Average Order Value | Average amount spent per order at the store (Sales ÷ Order Count) |
| Spend per Customer | Average amount contributed by each customer at the store (Sales ÷ Purchasing Members) |

!!! note "Notes"
    * The ranking table is sorted by "Sales" in descending order by default, to help you quickly identify top-performing stores and stores that need improvement.
    * The member statistics scope for each field is consistent with the [metrics reference table](#reference-pos-revenue-metrics){ title="POS Revenue Analysis Metrics Reference Table" data-preview } above.
