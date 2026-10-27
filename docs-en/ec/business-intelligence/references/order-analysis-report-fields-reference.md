---
title: "Order Report Fields Reference"
description: "Field definitions and descriptions for the three Excel tables on the order report tab."
created: 2026-06-15 00:00
last_modified: 2026-07-10 11:39
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
  - "Order Analysis"
  - "Order Reports"
  - "Average Order Value"
  - "Growth Rate"
  - "Sales by Hour"
  - "Daily Sales"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/order-analysis-report-fields-reference/"
icon: lucide/table
hide:
---

The "Order Report" tab provides three tables you can download as Excel. The fields in each table are described below.

### Date Range Comparison { #reference-order-analysis-report-compare }

Set two periods, a "query date range" and a "comparison date range," and the system automatically calculates the growth rate (%) between them.

| Field | Description |
| :-- | :-- |
| Order Count | Number of recognized orders in the period. |
| Purchasing Members | Number of members who actually placed orders in the period. |
| Sales Amount | Total amount of recognized orders in the period. |
| Average Order Value | Sales amount ÷ order count; the average amount per order. |
| Average Spend per Member | Sales amount ÷ purchasing members; the average spending per member. |
| Growth Rate (%) | The growth of the "query date range" relative to the "comparison date range." A positive value means growth; a negative value means decline. |

---

### Performance by Time of Day { #reference-order-analysis-report-by-time }

Shows orders by "time slot" so you can see how orders come in at different times of day. Use it to find the best times for ads or promotions.

| Field | Description |
| :-- | :-- |
| Time Slot | The time period. |
| Order Count (Awaiting Payment / Paid / Cash on Delivery / Total) | Number of orders in each time slot, in separate columns by payment status. |
| Sales Amount (Awaiting Payment / Paid / Cash on Delivery / Total) | Order amount in each time slot, in separate columns by payment status. |

---

### Daily Performance { #reference-order-analysis-report-daily }

Lists performance details for each day in the query period, by "date."

| Field | Description |
| :-- | :-- |
| Date | The date of the figures. |
| Order Count (Awaiting Payment / Paid / Cash on Delivery / Total) | Number of orders that day, in separate columns by payment status. |
| Sales Amount (Awaiting Payment / Paid / Cash on Delivery / Total) | Order amount that day, in separate columns by payment status. |
| Average Order Value (Awaiting Payment / Paid / Cash on Delivery / Total) | Average amount per order that day, in separate columns by payment status. |

!!! note "Note"
    * All three tables can be exported with the **"Download as Excel"** button in the upper-right corner of the table.
    * "Awaiting Payment," "Paid," and "Cash on Delivery" are payment status categories. "Total" is the sum of all three.
