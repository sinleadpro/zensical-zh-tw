---
title: "Chart Overview"
description: "Use the chart overview to see key business data for your online store and physical stores on a single page, compare it with industry benchmarks, and quickly find areas to improve."
created: 2026-06-15 10:01
last_modified: 2026-07-22 17:05
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
  - POS
modules:
  - 分析報表
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: branch
plans:
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents: []
features:
  - 圖表總覽
  - EC 總覽
  - POS 總覽
  - 指標趨勢圖
  - 指標卡
  - 每日數據表
  - 基準參考範圍
  - 門市排行表
prerequisites: []
related:
  - ec/business-intelligence/references/bi-overview-metrics-reference/
  - ec/business-intelligence/references/benchmark-reference-range-status-reference/
  - ec/business-intelligence/benchmarking/
tags:
  - "Analysis Reports"
  - "Chart Overview"
  - Benchmarking
  - "Benchmark Reference Range"
  - "EC Analysis"
  - "POS Analysis"
  - "Trend Charts"
  - "Metric Cards"
  - "Sales Revenue"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2974
  - https://www.cyberbiz.io/support/?p=8275
permalink: "https://help.cyberbiz.io/ec/business-intelligence/business-intelligence-overview/"
comments: ""
search:
  exclude: false
icon: lucide/gauge
hide:
---

![Chart Overview page](../../assets/images/ec-bi-overview-hero.en.png){ title="Chart Overview Page" .hero-page }

## About Chart Overview { #intro-chart-overview }

Chart Overview (admin path: "Charts" > "Summary Chart") organizes your store's core metrics, such as traffic, conversion rate, average order value, repurchase rate, and revenue, into trend charts and metric cards. Enterprise merchants also see a **"Benchmark Reference Range"** that compares your metrics with statistics from similar merchants with comparable performance in similar categories, so you can tell which metrics still have room to grow.

!!! tip "One Formula to Find Your Optimization Priorities"
    A common e-commerce formula for breaking down revenue is: **Revenue = traffic × conversion rate × average order value × repurchase rate**. When a metric is below its benchmark reference range, improving it usually pays off the most, so make it a priority.

## Page Overview { #overview-chart-overview }

| Section | Description |
| :-- | :-- |
| EC Overview | Overall operating data for your online store, such as traffic, conversion rate, orders, and revenue |
| [POS Overview](#operate-chart-overview-pos) | Data for physical stores (POS), such as revenue, orders, and number of customers |
| [Metric Trend Chart](#operate-chart-overview-switch-chart) | A line chart showing how a single metric changes over the selected period |
| [Metric Cards](#operate-chart-overview-read-benchmark) | Summary figures for each key metric; Enterprise plans also show the benchmark reference range |
| [Daily Data Table](#daily-data-table) | Metric details listed by day, with pagination |

For the definition and calculation of each metric on the page, see [Chart Overview Metrics](references/bi-overview-metrics-reference.md#reference-bi-overview-metrics){ data-preview }.

=== "EC Overview"
    Overall operating data for your online store, such as traffic, conversion rate, orders, and revenue

    ![EC Overview](../../assets/images/ec-bi-overview-ec.en.png){ title="EC Overview" }

=== "Metric Trend Chart"
    A line chart showing how a single metric changes over the selected period

    ![Metric trend chart](../../assets/images/ec-bi-overview-trend-chart.en.png){ title="Metric Trend Chart" }

=== "Metric Cards"
    Summary figures for each key metric; Enterprise plans also show the benchmark reference range

    ![Metric cards](../../assets/images/ec-bi-overview-metric-cards.en.png){ title="Metric Cards" }

=== "Daily Data Table"
    Metric details listed by day, with pagination

    ![Daily data table](../../assets/images/ec-bi-overview-daily-table.en.png){ title="Daily Data Table" }

    ??? note "Differences from the Admin Overview Page"
        "Daily orders and revenue" are calculated differently from "orders and revenue on the admin home page → Overview," so the figures differ.

        - **Admin home page → Overview:** Orders that were not canceled (including returned / return-rejected orders), updated in real time.
        - **Charts → Chart Overview:** Valid orders, updated at fixed times.

=== "POS Overview"
    Data for physical stores (POS), such as revenue, orders, and number of customers

    ![POS Overview](../../assets/images/ec-bi-overview-pos.en.png){ title="POS Overview" }

## Prerequisites and Limitations { #prerequisites-chart-overview }

Chart Overview is part of the "Charts" feature. Some advanced content appears only if the corresponding conditions are met:

- [x] **Benchmark reference range**: Shown only to **Enterprise** merchants, and the merchant's industry must be a supported category.
- [x] **POS Overview tab**: Appears only if you have connected the CYBERBIZ POS system.
- [x] **Industry category assignment**: The benchmark reference range automatically determines your industry from your product attributes. You can't set it manually.

!!! plan "Plan Differences"
    The benchmark reference range is an Enterprise-only feature. If your plan doesn't include it, the metric cards don't show the benchmark reference range or status labels.

## Steps { #operate-chart-overview }

### Open Chart Overview { #operate-chart-overview-enter }

1. **Open the page:** In the left menu of the admin, click "Charts" > "Summary Chart."
2. **Switch tabs:** At the top of the page there are two tabs, **"EC Overview"** and **"POS Overview"**[^pos]. EC Overview is shown by default.

[^pos]: The POS Overview tab appears only if the merchant has connected the CYBERBIZ POS system.

---

### Choose a Query Period { #operate-chart-overview-date-range }

1. **Open the date picker:** Click the date range picker in the upper-right corner of the page.
2. **Select start and end dates:** Select the start and end dates to query. After you select them, the system automatically loads data for that range, and the title changes from **"Last 30 Days Overview"** to **"Selected Period Overview."**
3. **Mind the range limit:** The query range can be up to 365 days. If it is longer, you'll see the reminder "The time range cannot exceed 365 days." If you select only a start date without an end date, you'll see the reminder "Please specify an end date."

![Choose a query period](../../assets/images/ec-bi-overview-date-range.en.png){ title="Choose a Query Period" }

---

### Switch Metric Trend Charts { #operate-chart-overview-switch-chart }

1. **Choose a metric:** In the metric bar above the trend chart, click the metric you want to view: Traffic, Conversion Rate (%), Orders, Average Order Value, Revenue, or Registered Members.
2. **View the trend:** The chart shows how the metric changes over the selected period. Hover over the line to see the detailed value at each data point. Click an item name to hide or show its data.
3. **View daily details:** The data table below the chart lists details by day, with pagination (100 rows per page).

![Switch metric trend charts](../../assets/images/ec-bi-overview-switch-trend-chart.en.gif){ title="Switch Metric Trend Charts" }

??? info "Line Color Key"
    The line colors in the trend chart represent different comparison bases:

    - **Dark blue line:** Shows data for the current period (the time range you set).
    - **Light blue line:** Shows data for the same period last year (the same time range a year earlier).
    - **Pink line:** Shows data for the previous period in the same year (the time range of the same length just before the current period).

    ??? example "Example"
        Suppose you set the time range to 2025-06-01 ~ 2025-07-31, a total of 2 months.

        - **Dark blue line:** Covers 2025-06-01 ~ 2025-07-31, 2 months.
        - **Light blue line:** Covers 2024-06-01 ~ 2024-07-31, 2 months.
        - **Pink line:** Covers 2025-04-01 ~ 2025-05-31, 2 months.

??? example "Use Case"
    You can choose a specific marketing season as the time range, such as Lunar New Year, Mother's Day, or summer vacation.

    - **Dark blue line:** Helps you understand sales for this season this year.
    - **Light blue line:** Helps you understand sales for this season last year.
    - **Pink line:** Helps you understand sales for the same length of time just before this year's season started.

---

### Read the Benchmark Reference Range { #operate-chart-overview-read-benchmark }

For Enterprise merchants in a supported industry, the following four metric cards also show the benchmark reference range:

1. **Find the metric cards:** In the metric card area below the trend chart, the **Total Traffic**, **Average Conversion Rate**, **Average Order Value**, and **Repurchase Rate** cards show a **"Benchmark Reference Range"** and a status label at the bottom.
2. **Read the status label:** There are three statuses: **Better than the benchmark**, **In line with the benchmark**, and **Below the benchmark**[^bm-status]. "Below the benchmark" is shown in red, meaning improving that metric pays off more.
3. **Check the data source:** Hover over the hint icon on the card to see "This value comes from statistics of merchants with comparable performance in similar categories," along with a link to related "Learning Resources."

![Benchmark reference range on metric cards](../../assets/images/ec-bi-overview-metric-cards-small.en.png){ title="Benchmark Reference Range on Metric Cards" }

[^bm-status]: For what each status means and the recommended actions, see [Benchmark Reference Range Status Reference](references/benchmark-reference-range-status-reference.md#reference-chart-overview-benchmark-status){ data-preview }.

<div class="grid cards" markdown>

- :lucide-bar-chart-3:{ .lg }
  [__Benchmarking__](benchmarking.md){ title="Benchmarking" }

</div>

---

### View the POS Overview { #operate-chart-overview-pos }

!!! plan "Plan / Feature Requirements"
    The POS Overview tab appears only if the merchant has connected the CYBERBIZ POS system.

1. **Switch tabs:** Click the "POS Overview" tab at the top of the page.
2. **View the store summary metric cards:** "This Month's POS Overview" at the top shows physical store summary figures such as revenue, orders, number of customers, and average spend per customer as metric cards.

    ![This month's POS overview metric cards](../../assets/images/ec-bi-overview-pos-metric-cards.en.png){ title="This Month's POS Overview Metric Cards" }

3. **Switch metric trend charts:** The trend chart below the metric cards can switch between five metrics: **revenue, orders, number of customers, average order value, and average spend per customer**, so you can see how they change over the selected period. Hover over the line to see the value at a single point.

    === "Revenue"
        ![Revenue trend chart](../../assets/images/ec-bi-overview-pos-trend-revenue.en.png){ title="Revenue Trend Chart" }

    === "Orders"
        ![Orders trend chart](../../assets/images/ec-bi-overview-pos-trend-orders.en.png){ title="Orders Trend Chart" }

    === "Number of Customers"
        ![Number of customers trend chart](../../assets/images/ec-bi-overview-pos-trend-customers.en.png){ title="Number of Customers Trend Chart" }

    === "Average Order Value"
        ![Average order value trend chart](../../assets/images/ec-bi-overview-pos-trend-aov.en.png){ title="Average Order Value Trend Chart" }

    === "Average Spend per Customer"
        ![Average spend per customer trend chart](../../assets/images/ec-bi-overview-pos-trend-per-customer.en.png){ title="Average Spend per Customer Trend Chart" }

4. **View store rankings:** The store detail table at the bottom of the page lists one store per row, with these columns:

    ![Store ranking table](../../assets/images/ec-bi-overview-pos-ranking-table.en.png){ title="Store Ranking Table" }

??? info "Field Descriptions"

    | Field | Description |
    | :-- | :-- |
    | Rank | Sorted by this month's revenue from highest to lowest |
    | Store | Store name |
    | This Month's Revenue | The store's cumulative revenue this month |
    | This Month's Orders | The store's number of orders this month |
    | This Month's Customers | The store's number of customers this month |
    | This Month's Average Daily Revenue | This month's revenue ÷ number of days |
    | This Month's Average Order Value | This month's revenue ÷ orders |
    | This Month's Average Spend per Customer | This month's revenue ÷ number of customers |

## Important Rules and Limitations { #specs-chart-overview }

### Recognized Order Definition { #specs-chart-overview-order-definition }

Chart Overview calculations include only "recognized orders," which must meet both of these conditions:

- Order status: not canceled
- Return status: no return needed or return rejected

So the numbers on the charts differ slightly from the count in "All Orders." This is normal. EC Overview counts only online store orders. For physical stores, see POS Overview.

---

### Supported Industry Categories { #specs-chart-overview-categories }

The benchmark reference range currently supports the following industry categories. The system automatically determines your industry from your product attributes:

- [x] Food, Beverages & Tobacco
- [x] Health & Beauty
- [x] Apparel & Accessories
- [x] Home & Garden

If your industry is not in these categories, the metric cards do not show the benchmark reference range.

---

### Data Update Time { #specs-chart-overview-update-time }

- Traffic and conversion rate data are updated at 5:30 PM the next day.
- Other data is updated at midnight the next day (canceled and returned orders are excluded in scheduled updates).

## Next Steps { #next-steps-chart-overview }

After you find metrics to improve with the benchmark reference range, use the following resources to build the related skills:

<div class="grid cards" markdown>

- :lucide-mouse-pointer-click:{ .lg }  
  [__Increase Traffic__](https://tutorcyb.cyberbiz.co/search?tab=programs&tag=流量篇)  
  Learn SEO, advertising, and social media traffic generation to bring more customers to your store.

- :lucide-percent:{ .lg }  
  [__Increase Conversion Rate__](https://tutorcyb.cyberbiz.co/search?tab=programs&tag=轉換率)  
  Optimize product pages and checkout so more traffic turns into orders.

- :lucide-receipt:{ .lg }  
  [__Increase Average Order Value__](https://tutorcyb.cyberbiz.co/search?tab=programs&tag=AOV)  
  Use add-on purchases, bundles, and similar methods to raise the amount of each order.

- :lucide-repeat:{ .lg }  
  [__Increase Repurchase Rate__](https://tutorcyb.cyberbiz.co/search?tab=programs&tag=回購率)  
  Use member engagement and remarketing to bring customers back to order again.

</div>

## FAQ { #faq-chart-overview }

??? quote "Why can't I see the benchmark reference range?"
    [](){ #faq-chart-overview-no-benchmark }
    The benchmark reference range appears only if all of these conditions are met:

    - Your plan is Enterprise.
    - Your industry is a supported category (food and beverages, health and beauty, apparel and accessories, home and garden).
    - The system has determined your industry from your product attributes.

    If it still doesn't appear, contact your store consultant or customer service.

??? quote "Where do the benchmark reference range numbers come from?"
    [](){ #faq-chart-overview-benchmark-source }
    The benchmark reference range comes from "statistics of merchants with comparable performance in similar categories." It is a reference range compiled from the operating data of merchants in the same industry and of similar size as you, not the numbers of a single store.

??? quote "Why hasn't today's data been updated yet?"
    [](){ #faq-chart-overview-update-time }
    Each metric is updated at a different time:

    - Traffic and conversion rate are updated at 5:30 PM the next day.
    - Other data (orders, revenue, and so on) is updated at midnight the next day.

    So the latest day's data is usually complete only the next day.

??? quote "Why don't chart figures match the order list?"
    [](){ #faq-chart-overview-recognized-order }
    Chart Overview counts only "recognized orders" (orders that are not canceled and do not require a return or had a return rejected), while the order list includes orders in all statuses. So the counts differ, which is normal.

??? quote "Can't find the POS Overview tab?"
    [](){ #faq-chart-overview-no-pos }
    The POS Overview tab appears only if the merchant has connected the CYBERBIZ POS system. If you don't use POS yet, the page shows only EC Overview.

## References { #reference-chart-overview }

- [Chart Overview Metrics Reference](references/bi-overview-metrics-reference.md)
- [Benchmark Reference Range Status Reference](references/benchmark-reference-range-status-reference.md)
- Online courses for improving each metric: [CYBERBIZ Business School](https://tutorcyb.cyberbiz.co/)

