---
title: "Product Analysis"
description: "Understand how your products sell, find best sellers, slow movers, and repurchase behavior, and use the data to inform purchasing, marketing, and pricing decisions."
created: 2026-06-15 00:00
last_modified: 2026-07-12 19:45
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - 商品報表分頁限企業版但商品報表下載適用plus跟企業版？看不到要怎麼下載？
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
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 查看商品銷售排行
  - 分析商品回購頻率
  - 找出滯銷商品
  - 匯出商品期間報表
features:
  - 商品銷售概況
  - 商品銷量 TOP 10 / LAST 10
  - 商品回購頻率
  - 無銷量商品清單
  - 商品期間別購買狀況
  - Excel 匯出
prerequisites:
  - 方案需包含「圖表分析」功能
  - 需有實際訂單資料
related:
  - ec/business-intelligence/references/product-analysis-metrics-reference/
  - ec/business-intelligence/revenue-analysis/
  - ec/business-intelligence/order-analysis/
  - ec/products/create-and-manage/create-update-products/
tags:
  - "Product Analysis"
  - "Product Sales Ranking"
  - "Repurchase Analysis"
  - "Data Analysis"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 圖表分析 > 商品分析
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10991
  - https://www.cyberbiz.io/helpcenter/?p=5054
  - https://www.cyberbiz.io/support/?p=9791
permalink: "https://help.cyberbiz.io/ec/business-intelligence/product-analysis/"
comments: false
search:
  exclude: false
icon: lucide/box
hide: []
---

![Product Analysis hero](../../assets/images/ec-bi-product-hero.en.png){ title="Product Analysis Hero" .hero-page }

## About Product Analysis { #intro-product-analysis }

"Product Analysis" helps you quickly understand how your store's products are selling: find your best-selling star products and slow movers that need promotion, and see how customers repurchase specific products.

This page is under "Charts" > "Product Analysis" in the admin. It organizes product performance into charts and tables for the period you choose, giving you data for purchasing, marketing, and pricing decisions. The page has two tabs: "Product Sales Overview" and "Product Report."

!!! info "Tip"
    This page counts only **valid orders** (orders that are not canceled and do not require a return or had a return rejected), so figures may differ from the number of orders in the "All Orders" list. For what is counted, see [Important Rules and Limitations](#specs-product-analysis).

## Page Overview { #overview-product-analysis }

| Tab | Section | Format | Purpose |
| :-- | :-- | :-- | :-- |
| Product Sales Overview | [Product Sales TOP 10](#operate-product-analysis-sales-rank) | Bar chart | Find the 10 best-selling products in the specified period |
| Product Sales Overview | [Product Sales LAST 10](#operate-product-analysis-sales-rank) | Bar chart | Find the 10 worst-selling products in the specified period |
| Product Sales Overview | [Product Repurchase Frequency](#operate-product-analysis-repurchase) | Table | See which products are bought repeatedly and their average repurchase interval |
| Product Sales Overview | [Products Updated in the Last 90 Days with No Sales in the Last 30 Days](#operate-product-analysis-no-sales) | Table | Spot products that were recently updated but aren't selling |
| Product Report | [Product Purchases by Period](#operate-product-analysis-period-report) | Table (exportable to Excel) | View order count, quantity sold, and sales amount for each product |

!!! note "Note"
    Each section has **its own query period** and does not affect the others. The only exception is "Products Updated in the Last 90 Days with No Sales in the Last 30 Days," which the system calculates automatically based on today and does not support custom dates.

## Prerequisites and Limitations { #prerequisites-product-analysis }

<!-- - [x] **Your plan must include the "Chart Analysis" feature**: This page is part of the operations data analysis features. If your plan does not include it, the page shows "Your current plan does not support this feature. Please contact customer service or your store consultant." In that case, contact customer service or your store consultant. -->
- [x] **Actual order data is required**: Each chart and table is calculated from valid orders. For a new store, or when there are no orders in the query period, the corresponding section is blank.

!!! plan "Plan Differences"
    The Pro / PLUS plans do not show the "**Product Report**" tab (that is, "Product Purchases by Period"). If you only see "Product Sales Overview" and no "Product Report" tab on the page, your current plan does not include this section.

## Steps { #operate-product-analysis }

### Switch Tabs and Choose a Query Period { #operate-product-analysis-switch-and-date }

1. **Open the page:** In the admin, go to "Charts" > "Product Analysis." The page opens on the "**Product Sales Overview**" tab by default.
2. **Switch tabs:** Click "**Product Sales Overview**" or "**Product Report**" at the top of the page to switch. The "Product Report" tab loads its data the first time you click it, so please wait a moment.
3. **Choose a query period:** Each chart or table has its own date field in the upper-right corner. Click it to choose a preset range or custom start and end dates. By default, the system shows data for **the last month**.

![Switch tabs and choose a query period](../../assets/images/ec-bi-product-analysis-switch-date.en.png){ title="Switch Tabs and Choose a Query Period" }

??? info "Available Preset Ranges"
    | Preset | Range |
    | :-- | :-- |
    | Today | The current day |
    | Yesterday | The previous day |
    | Last 7 Days | The 7 days up to and including today |
    | Last 30 Days | The 30 days up to and including today |
    | This Month | From the 1st to the end of the current month |
    | Last Month | The whole previous month |
    | Custom | Start and end dates you specify |

!!! tip "Tip"
    The date format is `MM/DD/YYYY` (month/day/year). Changing the date of any section updates only that section. Other sections keep their query periods.

---

### Find Best-Selling and Slow-Moving Products <small>TOP 10 / LAST 10</small> { #operate-product-analysis-sales-rank }

1. **View best-selling products:** In the "**Product Sales TOP 10**" bar chart on the "Product Sales Overview" tab, the 10 products with the highest quantity sold in the period are listed from top to bottom.
2. **View slow-moving products:** "**Product Sales LAST 10**" on the right shows the 10 products with the lowest quantity sold in the same period.
3. **Compare periods:** Click the date field of each chart to see how the rankings change across periods.
4. **See individual figures:** Hover over any bar to see the product's full name and quantity sold.

![Product Sales TOP 10 and LAST 10](../../assets/images/ec-bi-product-analysis-sales-rank.en.png){ title="Product Sales TOP 10 and LAST 10" }

For field definitions, see [Product Sales Fields](./references/product-analysis-metrics-reference.md#reference-product-analysis-sales-rank){ data-preview }.

---

### Understand Product Repurchase Frequency and Intervals { #operate-product-analysis-repurchase }

1. **Find the section:** Scroll down on the "Product Sales Overview" tab to find the "**Product Repurchase Frequency**" table.
2. **Set the period:** Click the date field next to the table title to choose a query period.
3. **Interpret the data:** The table lists each product's "**Repurchase Count**" and "**Average Repurchase Interval (Days)**," helping you identify highly loyal products that suit subscription plans or restock reminders.

![Product repurchase frequency](../../assets/images/ec-bi-product-analysis-repurchase.en.png){ title="Product Repurchase Frequency" }

!!! note "Note"
    A product appears in this table only if it was **repurchased 10 or more times** in the query period. Products below 10 are not listed. For field definitions, see [Product Repurchase Frequency Fields](./references/product-analysis-metrics-reference.md#reference-product-analysis-repurchase){ data-preview }.

---

### Spot Slow-Moving New Products to Review <small>No-Sales List</small> { #operate-product-analysis-no-sales }

1. **Find the section:** Go to the "**Products Updated in the Last 90 Days with No Sales in the Last 30 Days**" table on the "Product Sales Overview" tab.
2. **Review the list:** This table automatically lists products that **were updated in the last 90 days but had no sales in the last 30 days**, so you can check whether the issue is copy, pricing, or exposure.
3. **Page through:** If there are many products, use the page buttons below the table to view them page by page.

![Products updated in the last 90 days with no sales in the last 30 days](../../assets/images/ec-bi-product-analysis-no-sales.en.png){ title="Products Updated in the Last 90 Days with No Sales in the Last 30 Days" }

!!! info "Tip"
    This section is calculated automatically based on "today" and **has no date field**, so you don't need to (and can't) set a custom query period. For field definitions, see [No-Sales Product Fields](./references/product-analysis-metrics-reference.md#reference-product-analysis-no-sales){ data-preview }.

---

### Use "Product Report" to View Purchases by Period and Export { #operate-product-analysis-period-report }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | Enterprise

1. **Switch tabs:** Click the "**Product Report**" tab at the top and wait for the "**Product Purchases by Period**" table to load.

2. **Choose a period:** Click the date field next to the table title and choose the query period to report on.

    ![Choose a query period](../../assets/images/ec-bi-product-analysis-select-period.en.png){ title="Choose a Query Period" }

3. **Filter specific products (optional):** Use the "Unselected Products / Selected Products" lists to pick the items you want to view, then click "**Apply Filter**" to show only those products[^period-filter].

    ![Filter specific products](../../assets/images/ec-bi-product-analysis-filter-products.en.png){ title="Filter Specific Products" }

4. **Interpret the data:** The table shows each product's "Order Count," "Quantity Sold," and "Total Product Sales" row by row. The last row is the "**Total**" for all products.

    ![Product purchases by period data](../../assets/images/ec-bi-product-analysis-period-data.en.png){ title="Product Purchases by Period Data" }

5. **Export to Excel:** Click "**Download as Excel**" in the upper-right corner of the table. The system generates and downloads an Excel file for the current query period.

    ![Export to Excel](../../assets/images/ec-bi-product-analysis-export-excel.en.png){ title="Export to Excel" }

For field definitions, see [Product Purchases by Period Fields](./references/product-analysis-metrics-reference.md#reference-product-analysis-period){ data-preview }.

[^period-filter]: The filter lists support keyword search. If no products are selected, the table shows all products.

## Important Rules and Limitations { #specs-product-analysis }

- **Recognized order scope:** All figures count only **valid orders**, which are "non-canceled orders" that "do not require a return or had a return rejected." Canceled and returned orders are not counted.
- **Add-on items are excluded:** Quantities in "Product Sales TOP 10 / LAST 10" exclude add-on items, so the sales ranking isn't skewed by add-ons.
- **Repurchase frequency threshold:** "Product Repurchase Frequency" lists only products repurchased 10 or more times in the query period. A repurchase is when the same customer buys the same product again; each purchase from the 2nd onward counts as one repurchase.
- **The no-sales list is calculated dynamically:** "Products Updated in the Last 90 Days with No Sales in the Last 30 Days" is always based on "today" at the time you view it and cannot go back to a specific date.
- **Data update time:** Data is updated daily at 8:00, 12:00, 16:00, 20:00, and 24:00.
- **Data is based on operations data:** Figures on this page may lag slightly behind the real-time order list. Use them to read trends, and rely on order and financial reports for exact reconciliation.

## Next Steps { #next-steps-product-analysis }

<div class="grid cards" markdown>

- :lucide-trending-up:{ .lg }  
  [__Revenue Analysis__](./revenue-analysis.md){ title="Revenue Analysis" }  
  Combine revenue and gross profit data to understand overall operating performance.

- :lucide-shopping-cart:{ .lg }  
  [__Order Analysis__](./order-analysis.md){ title="Order Analysis" }  
  Understand your sales mix from order volume, average order value, and cancellation rate.

- :lucide-package:{ .lg }  
  [__Add and Edit Products__](../products/create-and-manage/create-update-products.md){ title="Add and Update Products" }  
  Adjust listings, pricing, and copy for slow-moving or best-selling products.

</div>

## FAQ { #faq-product-analysis }

??? quote "The product repurchase frequency table is empty and shows no products"
    [](){ #faq-product-analysis-repurchase-empty }
    This is normal. A product is listed only if it was **repurchased 10 or more times** in the query period. If your store's repurchases are still building up, or the query period is short, the table may be empty for now. You can try:

    - Extending the query period (for example, choose "Last 30 Days" or a longer custom range)
    - Checking again after repurchase data has built up for a while

??? quote "Are product sales ranked by "amount" or "quantity"?"
    [](){ #faq-product-analysis-rank-basis }
    "Product Sales TOP 10 / LAST 10" is ranked by **sales volume** (number of units), not sales amount. To see per-product data based on amount, use "Product Purchases by Period" on the "Product Report" tab, which includes a "Total Product Sales" field.

??? quote "Are add-on items or gifts counted in sales?"
    [](){ #faq-product-analysis-addon-excluded }
    No. "Product Sales TOP 10 / LAST 10" excludes add-on items, so the ranking reflects sales of your main products.

??? quote "Report figures don't match the order list"
    [](){ #faq-product-analysis-number-mismatch }
    This page counts only **valid orders** (not canceled, and not requiring a return or with a return rejected), while the order list includes canceled and returned orders, so counts and amounts may differ. This is expected and reflects a difference in how data is counted.

## References { #reference-product-analysis }

- [Product Analysis Field Reference](./references/product-analysis-metrics-reference.md)
