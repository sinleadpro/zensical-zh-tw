---
title: "Basic Reports"
description: "See your store's sales and traffic at a glance on one admin page, including product sales rankings, order count, total sales, and page views over the last 7 days."
created: 2026-06-21 00:00
last_modified: 2026-07-13 09:00
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 分析報表
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - Professional
  - Advanced
plan_options: []
cyb_extensions: []
intents:
  - 查看商店銷售與流量概況
  - 匯出商品銷售排行報表
  - 了解各報表計算規則
features:
  - 基本報表
  - 商品銷售排行
  - 訂單數量趨勢
  - 總銷售額趨勢
  - 近七日瀏覽人次
prerequisites: []
related:
  - ec/business-intelligence/references/basic-chart-metrics-reference/
  - ec/business-intelligence/product-chart/
  - ec/orders/reports/export-order-report/
  - ec/business-intelligence/business-intelligence-overview/
tags:
  - "Basic Reports"
  - "Report Analysis"
  - "Product Sales Ranking"
  - "Order Count"
  - "Total Sales"
  - "Page Views"
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分析報表 > 基本報表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3023
permalink: "https://help.cyberbiz.io/ec/business-intelligence/basic-chart/"
comments: false
search:
  exclude: false
icon: lucide/chart-bar
hide:
---

![Basic Reports page](../../assets/images/ec-business-intelligence-basic-chart-hero.en.png){ title="Basic Reports Page" .hero-page }

## About Basic Reports { #intro-basic-chart }

!!! path "Path: In the left menu of the admin, go to "Charts" > "Base Chart""

## Page Overview { #overview-basic-chart }

"Basic Reports" has the following four sections. Here is what each is for and how to use it:

| Section | What It Shows | How to Use |
| :-- | :-- | :-- |
| Product Sales Ranking Report | Top 10 products by sales in the specified period | Select a date range and export to Excel |
| Order Count | Monthly trend of valid order count | Switch the period in the upper-right corner of the page |
| Total Sales | Monthly trend of valid order amounts | Switch the period in the upper-right corner of the page |
| Page Views in the Last 7 Days | Daily visits to the store home page over the past 7 days | Hover over a data point to see the value |

!!! note "Note"
    "Order Count" and "Total Sales" share the same period menu in the upper-right corner of the page, and both charts update together when you switch. "Page Views in the Last 7 Days" always shows the last 7 days and is not affected by that menu.

## Steps { #operate-basic-chart }

### View Order Count and Total Sales Trends { #operate-basic-chart-trend }

1. **Open the report page:** In the admin, go to "Charts" > "Base Chart."
2. **Select a period:** In the drop-down menu in the upper-right corner of the page, select "6 months," "1 year," "3 years," or "5 years" (the default is 6 months).

    ![Select a period](../../assets/images/ec-business-intelligence-basic-chart-date-range.en.png){ title="Select a Period" }

3. **View the trends:** The "Order Count" and "Total Sales" charts are redrawn by month for the selected period.

    === "Order Count"

        ![Order count trend chart](../../assets/images/ec-business-intelligence-basic-chart-order-count.en.png){ title="Order Count Trend Chart" }

    === "Total Sales"

        ![Total sales trend chart](../../assets/images/ec-business-intelligence-basic-chart-total-sales.en.png){ title="Total Sales Trend Chart" }

4. **View a single month:** Hover over any data point on the line chart to see the detailed figures for that month.

!!! note "Note"
    These two charts count only valid orders. Canceled and returned orders are not included. For details on how orders are counted, see [Calculation Rules for Each Report](references/basic-chart-metrics-reference.md#reference-basic-chart-metrics){ title="Calculation Rules for Each Basic Report Section" data-preview }.

---

### Export the Product Sales Ranking Report { #operate-basic-chart-export-rank }



1. **Set the start date:** In the "Product Sales Ranking Report" section, click the "Start Date" field and pick the start date from the calendar.
2. **Set the end date:** Click the "End Date" field and pick the end date (it cannot be earlier than the start date).
3. **Export to Excel:** The **"Export"** button becomes available only after you select both dates. Click it to download the Excel file[^export-sheets].
4. **View the ranking:** The Excel file lists the top 10 products by sales in the period, from highest to lowest.

[^export-sheets]: If your store has the POS (in-store sales) feature, the exported Excel file is split into separate sheets for "All," "Online," "Physical Stores," and each store. Otherwise, it has only one "All" sheet.

![Product sales ranking report section](../../assets/images/ec-business-intelligence-basic-chart-export-section.en.png){ title="Product Sales Ranking Report Section" }

---

## Important Rules and Limitations { #specs-basic-chart }

- **Valid order definition:** "Order Count" and "Total Sales" count only valid orders and automatically exclude "Canceled" and "Returned" orders.
- **Amount basis for the product sales ranking:** The ranking is sorted by "actual transaction amount" (quantity sold × transaction unit price) from highest to lowest. It also counts only valid orders that were not returned, consistent with the charts.
- **How page views in the last 7 days are counted:** This chart counts only visits to the "store home page." Each time a visitor opens the home page counts once, and duplicates are not removed (for example, refreshing the page counts again).
- **Data update time:** "Order Count," "Total Sales," and "Product Sales Ranking" are real-time. "Page Views in the Last 7 Days" compiles the previous day's data daily, so today's home page visits appear on the chart tomorrow.

How each report is calculated is summarized in [Calculation Rules for Each Report](references/basic-chart-metrics-reference.md#reference-basic-chart-metrics){ title="Calculation Rules for Each Basic Report Section" data-preview }.

---

## Next Steps { #next-steps-basic-chart }

<div class="grid cards" markdown>

- :lucide-line-chart:{ .lg }  
  [__Product Charts__](product-chart.md){ title="Product Charts" }  
  Analyze views, purchases, and conversion rate for individual products in depth.

- :lucide-file-spreadsheet:{ .lg }  
  [__Export Order Reports__](../orders/reports/export-order-report.md){ title="Export Order Reports" }  
  Export more complete order details for further reconciliation and analysis.

- :lucide-bar-chart-3:{ .lg }  
  [__Operations Chart Analysis__](business-intelligence-overview.md){ title="Chart Overview" }  
  See advanced operations analysis with metrics such as conversion rate and average order value.

</div>

---

## FAQ { #faq-basic-chart }

??? quote "Why don't today's orders or page views show up?"
    [](){ #faq-basic-chart-today-missing }
    It depends on the report:

    - "Order Count" and "Total Sales" are real-time, so new orders appear right away (you may need to refresh the page).
    - "Page Views in the Last 7 Days" compiles the previous day's data daily, so today's home page visits appear tomorrow.

??? quote "Why don't the numbers in "Product Sales Ranking" and "Product Charts" match?"
    [](){ #faq-basic-chart-mismatch }
    They use different bases, so they are not expected to match:

    - The "Product Sales Ranking Report" counts the "actual transaction amount" and includes only valid orders that were not returned.
    - "[Product Charts](product-chart.md){ title="Product Charts" }" counts daily compiled "views" and "purchases." Purchases record only the quantity at the time the order is created and do not reflect later payment, cancellation, or return status.

??? quote "I selected the dates, but the "Export" button is still grayed out?"
    [](){ #faq-basic-chart-export-disabled }
    Make sure both the "Start Date" and "End Date" fields are selected and the end date is not earlier than the start date. Then the button becomes available.

??? quote "Which orders does the report count? Are canceled and returned orders included?"
    [](){ #faq-basic-chart-which-orders }
    "Order Count," "Total Sales," and "Product Sales Ranking" count only valid orders and automatically exclude canceled and returned orders.

---

## References { #reference-basic-chart }

- [Calculation Rules for Each Report](references/basic-chart-metrics-reference.md#reference-basic-chart-metrics)


