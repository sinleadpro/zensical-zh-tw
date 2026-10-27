---
title: "Advertising Analysis Metrics Reference"
description: "Definitions and calculation methods for the 11 performance metrics on the Advertising Analysis page, including cost, impressions, clicks, conversions, and ROAS."
created: 2026-06-15 00:00
last_modified: 2026-07-12 19:49
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
  - "Advertising Analysis"
  - "Ad Metrics"
  - "Click-Through Rate"
  - "Conversion Rate"
  - ROAS
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/advertising-analytics-metrics-reference/"
icon: lucide/table
hide:
---

# Advertising Analysis Metrics Reference

This page lists the 11 performance metrics shared by the data overview cards and the daily trend chart on the "Advertising Analysis" page. All metric data comes from Google Shopping ads (the automated ad system) and is compiled daily.

---

### Performance Metrics { #reference-advertising-analytics-metrics }

| Metric | What It Means | Calculation |
| :-- | :-- | :-- |
| Cost | The amount spent on ads. | — |
| Impressions | The number of times the ad was shown. | — |
| Clicks | Each time a customer clicks the ad counts as one click. | — |
| Click-through Rate | How likely customers are to click the ad. | Clicks ÷ impressions |
| Average CPC | The average cost per click. | Cost ÷ clicks |
| Conversions | The number of orders customers placed after clicking the ad[^conversion]. | — |
| Conversion Rate | How likely customers are to place an order. | Conversions ÷ clicks |
| Cost per Conversion | The average cost per conversion. | Cost ÷ conversions |
| Conversions Value | The total amount of orders customers placed. | — |
| Average Conversion Value | The average order amount per conversion. | Conversions value ÷ conversions |
| ROAS | Return on ad spend. The higher the number, the more revenue each dollar of ad spend brings back. | Conversions value ÷ cost |

!!! note "Note"
    * "Click-through Rate" and "Conversion Rate" are shown as percentages (%). "Cost," "Average CPC," "Cost per Conversion," "Conversions Value," and "Average Conversion Value" are shown as amounts. The rest are counts.
    * The same 11 metrics appear on both the "Data Overview" cards at the top and the "Daily Trend Chart" below. The only difference is that the cards show totals for the period, while the chart shows day-by-day changes.
    * Hover over the name of any data card to see a tooltip that explains the metric.

[^conversion]: A conversion is counted if the customer clicked the ad within 30 days before placing the order. After ads start running, it takes some time for conversion data to appear, and a conversion may be attributed to an earlier click date.
