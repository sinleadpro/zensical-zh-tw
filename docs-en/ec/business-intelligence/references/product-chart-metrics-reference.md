---
title: "Product Chart Metrics Reference"
description: "Learn the three core product chart metrics (views, purchases, and conversion rate), how they are calculated, and their limitations."
created: 2026-06-21 00:00
last_modified: 2026-07-12 20:49
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
  - "Product Charts"
  - Views
  - Purchases
  - "Conversion Rate"
  - "Metrics Reference"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/product-chart-metrics-reference/"
icon: lucide/table
hide:
---

# Product Chart Reference

This page collects the metric reference tables for "Product Charts" for quick lookup.

## Product Chart Metrics { #reference-product-chart-metrics }

| Metric | Description | Calculation |
| :-- | :-- | :-- |
| Views | Total number of times the product page was opened during the period. This is raw data: repeat visits or page refreshes by the same customer are each counted. | Accumulated daily |
| Purchases | Number of orders placed during the period that include the product. Orders are recorded on the day they are placed and are not adjusted for later cancellations, returns, or payment status changes. | Accumulated daily |
| Conversion Rate | The rate at which the product page turns "views" into "orders." Use it to assess how well the product page copy, images, or pricing drive orders. | (Purchases ÷ Views) × 100% |

!!! note "Note"
    * When views are 0, the conversion rate shows as 0%.
    * All data for the previous day is updated daily at 2:00 a.m. Same-day real-time data does not appear in the report.
    * The system keeps only about the last 2 months of daily data. Older data cannot be queried.
