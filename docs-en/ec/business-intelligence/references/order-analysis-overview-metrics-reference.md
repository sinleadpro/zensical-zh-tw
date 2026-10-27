---
title: "Order Overview Analysis Metrics Reference"
description: "Definitions of the key metrics and trend charts on the order overview analysis tab."
created: 2026-06-15 00:00
last_modified: 2026-07-10 11:35
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
  - Orders
  - "Average Order Value"
  - "Cancellation Rate"
  - "Return Rate"
  - "Change Value"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/order-analysis-overview-metrics-reference/"
icon: lucide/table
hide:
---

### Key Figures and Trend Charts { #reference-order-analysis-overview-metrics }

| Metric | What It Means | Calculation |
| :-- | :-- | :-- |
| Total Orders | Total orders since the store opened | Sum of recognized orders since the store opened |
| Orders in the Last 30 Days | Orders in the 30 days before today | Sum of recognized orders in the last 30 days |
| Monthly Order Trend | Orders per month in the period (by order creation time) | Sum of orders per month; last 6 months by default |
| Monthly Order Amount Trend | Number of orders per month grouped by amount range | Orders per amount range per month |
| Monthly Order Amount Trend (Ratio) | Share of each amount range in the selected month | (Orders in one amount range in the month ÷ total orders in the month) × 100% |
| Order Amount (Share) | Share of total orders in each amount range during the period | (Orders in one amount range ÷ total orders in the period) × 100% |
| Items per Order (Share) | Share of each item-count range (including add-on purchases and spend-threshold gifts) | (Orders in one item-count range ÷ all orders in the period) × 100% |
| Average Daily Orders (Monthly Trend) | Average daily orders in each month | Total orders in the month ÷ days in the month |
| Average Daily Orders in the Last 30 Days | Average orders over the past 30 days | Orders in the last 30 days ÷ 30 |
| Change (Average Daily Orders) | Growth of the last 30 days compared with the long-term average | Average orders over the past 30 days − average orders since the store opened |
| Average Daily Order Amount (Monthly Trend) | Average daily order amount in each month | Sum of daily average order amounts in the month ÷ days in the month |
| Average Order Amount in the Last 30 Days | Average order amount over the past 30 days | Order amount in the last 30 days ÷ 30 |
| Change (Average Order Amount) | Growth of the last 30 days compared with the long-term average | Average order amount over the past 30 days − average order amount since the store opened |
| Monthly Order Cancellation Rate Trend | Order cancellation rate in each month | (Canceled orders in the month ÷ all orders in the month) × 100% |
| Order Cancellation Rate in the Last 30 Days | Cancellation rate over the past 30 days (by order creation time) | (Canceled orders in the last 30 days ÷ all orders in the last 30 days) × 100% |
| Change (Order Cancellation Rate) | Growth rate of the last 30 days compared with the long-term average | (Canceled in the past 30 days ÷ all in the past 30 days) × 100 − (canceled since opening ÷ all since opening) × 100 |
| Monthly Order Return Rate Trend | Order return rate in each month (excluding canceled orders) | (Returned orders in the month ÷ orders not "Canceled") × 100% |
| Order Return Rate in the Last 30 Days | Return rate over the past 30 days (excluding canceled orders, by order creation time) | (Returned in the last 30 days ÷ orders not "Canceled") × 100% |
| Change (Order Return Rate) | Growth rate of the last 30 days compared with the long-term average (excluding canceled orders) | (Returned in the past 30 days ÷ not "Canceled") × 100 − (returned since opening ÷ not "Canceled" since opening) × 100 |

!!! note "Note"
    * "Recognized orders" are orders that are not canceled and whose return status is no return needed or return rejected. See [Recognized Order Definition](../order-analysis.md#prerequisites-order-analysis-recognized-order){ title="Recognized Order Definition" } in the main article.
    * The return rate's denominator is orders that are not "Canceled." Canceled orders cannot be shipped, so they are always excluded.
    * Data is updated in scheduled batches (daily at 8:00, 12:00, 16:00, 20:00, and 24:00), not in real time.
    * ⚠️ The `÷ 30` in "Average Daily Orders / Average Order Amount in the Last 30 Days" is a reasonable calculation inferred from the definition. Please verify it against actual data.

<!---->
<!---->
<!-- | Metric / Chart | What It Means for Merchants | -->
<!-- | :-- | :-- | -->
<!-- | Total Orders | Cumulative recognized orders since the store opened. | -->
<!-- | Orders in the Last 30 Days | Recognized orders in the last 30 days, for a quick view of the past month's sales volume. | -->
<!-- | Monthly Order Trend | Line chart of orders per month in the specified period. | -->
<!-- | Monthly Order Amount Trend | Groups each month's orders by amount range (such as 0–NT$1000 and 3001–NT$5000) to show changes in each range. | -->
<!-- | Monthly Order Amount Trend (Ratio) | Same as above, shown as stacked percentages for each amount range. | -->
<!-- | Order Amount (Share of Total Orders) | Pie chart of each amount range's share of all orders over the period, to help set average order value targets. | -->
<!-- | Items per Order (Share of Total Orders) | Pie chart of how many items customers usually buy per order (including add-on purchases and spend-threshold gifts). | -->
<!-- | Average Daily Orders (Monthly Trend) | Trend chart of "average daily orders" per month. | -->
<!-- | Average Daily Orders in the Last 30 Days | Average orders placed per day over the last 30 days. | -->
<!-- | Change (Average Daily Orders) | Growth of the last 30 days' average daily orders compared with the long-term average. | -->
<!-- | Average Daily Order Amount (Monthly Trend) | Trend chart of "average daily order amount" per month. | -->
<!-- | Average Order Amount in the Last 30 Days | Average daily order amount over the last 30 days. | -->
<!-- | Change (Average Order Amount) | Growth of the last 30 days' average order amount compared with the long-term average. | -->
<!-- | Monthly Order Cancellation Rate Trend | Trend chart of monthly order cancellation rates, for spotting operational issues. | -->
<!-- | Order Cancellation Rate in the Last 30 Days | Order cancellation rate over the last 30 days. | -->
<!-- | Change (Order Cancellation Rate) | Growth rate of the last 30 days' cancellation rate compared with the long-term average. | -->
<!-- | Monthly Order Return Rate Trend | Trend chart of monthly order return rates. | -->
<!-- | Order Return Rate in the Last 30 Days | Order return rate over the last 30 days. | -->
<!-- | Change (Order Return Rate) | Growth rate of the last 30 days' return rate compared with the long-term average. | -->
<!---->
<!-- !!! note "Note" -->
<!--     * Cards labeled "Change" compare two values, the **past 30 days** and the **long-term average**. A positive value means recent growth; a negative value means a recent decline. -->
<!--     * The return rate first excludes canceled orders and then uses recognized orders as the base. See "Important Rules and Limitations" in the main article for the definition. -->

