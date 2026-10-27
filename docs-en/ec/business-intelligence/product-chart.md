---
title: "Product Charts"
description: "See how a single product performs in views and purchases over a set period, and quickly judge how well its product page attracts shoppers and converts."
created: 2026-06-21 00:00
last_modified: 2026-07-12 20:51
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
  - 觀察商品瀏覽與購買趨勢
  - 分析商品成交率
features:
  - 商品圖表
prerequisites:
  - 方案需包含「商品圖表」功能
related:
  - ec/business-intelligence/references/product-chart-metrics-reference/
  - ec/business-intelligence/product-analysis/
  - ec/business-intelligence/basic-chart/
tags:
  - "Product Charts"
  - Views
  - Purchases
  - "Conversion Rate"
  - "Data Analysis"
  - "Analysis Reports"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 分析報表 > 商品圖表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3052
permalink: "https://help.cyberbiz.io/ec/business-intelligence/product-chart/"
comments: false
search:
  exclude: false
icon: lucide/pie-chart
hide: []
---

![Product Charts page](../../assets/images/ec-business-intelligence-product-chart-hero.en.png){ title="Product Charts Page" .hero-page }

## About Product Charts { #intro-product-chart }

This page is under "**Charts**" in the admin. Using three daily metrics, "Views," "Purchases," and "Conversion Rate," you can find which products get many views but few orders (good candidates for better copy, images, or pricing) and which convert smoothly, to guide future marketing and product selection.

!!! info "Tip"
    Data on this page is updated daily at 2:00 a.m. with the previous day's results, so today's data appears tomorrow. For detailed definitions of the three metrics, see [Product Chart Metrics](references/product-chart-metrics-reference.md#reference-product-chart-metrics){ data-preview }.

## Prerequisites and Limitations { #prerequisites-product-chart }

- [x] **Your plan includes the "Product Charts" feature**: "Product Charts" is a basic operations report. If you cannot find this page in the admin, your plan usually offers the more complete "Product Analysis" instead, and we recommend using that page.

??? plan "Plan Differences: Product Charts vs. Product Analysis"
    * "Product Charts" shows daily view and purchase trends for individual products and suits everyday monitoring.
    * Some advanced plans (such as Enterprise) offer the more complete "Product Analysis" instead, with deeper metrics such as conversion funnels, repurchase behavior, average days between repurchases, and slow-mover monitoring. If your admin has "Product Analysis," we recommend using it.

## Steps { #operate-product-chart }

### Query and View Product Performance { #operate-product-chart-query }

1. **Open the page:** In the admin, go to "Charts" > "Product Chart."
2. **Set the query period:** In the two date fields at the top of the page, select the start date on the left and the end date on the right[^range].

    ![Set the query period](../../assets/images/ec-business-intelligence-product-chart-date-range.en.png){ title="Set the Query Period" }

3. **Run the query:** Click **"Search"**.
4. **View the trend line chart:** The chart shows the daily trend of "Views" and "Purchases" over the period as lines. Hover over a data point on a line to see the values for that date. Click an item name to hide or show its data.

    ![Trend line chart](../../assets/images/ec-business-intelligence-product-chart-trend.en.png){ title="Trend Line Chart" }

5. **View the product details table:** The table below the chart lists "Views," "Purchases," and "Conversion Rate" for each product. Click the "Views" or "Purchases" column header to change the sort order, and choose to show 10, 25, or 50 rows per page.

    ![Product details table](../../assets/images/ec-business-intelligence-product-chart-table.en.png){ title="Product Details Table" }

!!! tip "Tip"
    To find products that "get looked at but not bought," sort by "Views" from highest to lowest and check for a low "Conversion Rate" on the right. These product pages are the best ones to improve first.

[^range]: The page loads the last 7 days by default. Because the system keeps only about the last 2 months of daily data, the earliest date you can query is about 2 months ago.

## Important Rules and Limitations { #specs-product-chart }

### Definitions of the Three Metrics { #specs-product-chart-metrics }

"Views," "Purchases," and "Conversion Rate" in the report are all raw statistics. For full definitions and calculations, see [Product Chart Metrics](references/product-chart-metrics-reference.md#reference-product-chart-metrics){ data-preview }. Two points to note:

- **Views are raw data:** Duplicate events are not removed, so the same person refreshing the page is counted again.
- **Purchases count only orders placed that day:** Only the number of orders created that day is recorded. It is not adjusted later for cancellations, returns, or payment status changes.

---

### Data Updates and Retention { #specs-product-chart-data }

- **Update time:** The previous day's data is updated automatically at 2:00 a.m. every day, so today's views and purchases appear tomorrow.
- **Retention period:** The system keeps only about the last 2 months of daily data. Older records are deleted automatically and can no longer be queried.

## Next Steps { #next-steps-product-chart }

<div class="grid cards" markdown>

- :lucide-bar-chart-3:{ .lg }  
  [__Product Analysis__](product-analysis.md){ title="Product Analysis" }  
  Available on advanced plans, with deeper metrics such as conversion funnels, repurchase behavior, and slow-mover monitoring.

- :lucide-trophy:{ .lg }  
  [__Export the Product Sales Ranking Report__](basic-chart.md#operate-basic-chart-export-rank){ title="Basic Reports" }  
  Set a date range in "Basic Reports" and export an Excel file listing the products with the highest total sales in that period.

</div>

## FAQ { #faq-product-chart }

??? quote "Why don't today's views and purchases show up yet?"
    [](){ #faq-product-chart-update-time }
    Product Charts data is updated with the "previous day's" results at 2:00 a.m. every day. It is not real-time.

    Views and orders that happen today appear in the report after tomorrow's update. This is normal.

??? quote "Why do some products have many views but 0 purchases?"
    [](){ #faq-product-chart-low-conversion }
    This means the product page attracts clicks, but few people actually order. In other words, the "Conversion Rate" is low.

    Review the product page from these angles:

    - Does the product copy clearly explain the selling points?
    - Are the product images appealing enough?
    - Are the price or shipping fees putting customers off?

??? quote "Can't find older data, or can't select earlier dates?"
    [](){ #faq-product-chart-data-retention }
    The system keeps only about the last 2 months of daily data. Records older than that are deleted automatically.

    If you need long-term historical analysis, check the report regularly and save the data you need yourself.

??? quote "Do purchases go down when a customer returns or cancels an order?"
    [](){ #faq-product-chart-purchase-count }
    No. Purchases record "the number of orders placed that day." This is raw data and is not adjusted later for cancellations, returns, or payment status changes.

## References { #reference-product-chart }

- [Product Chart Metrics](references/product-chart-metrics-reference.md#reference-product-chart-metrics)

