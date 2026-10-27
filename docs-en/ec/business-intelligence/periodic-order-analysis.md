---
title: "Subscription Order Analysis"
description: "Use data cards and charts to see the number, value, duration, and cancellations of subscription orders in your store, and spot renewal and churn trends."
created: 2026-06-16 00:00
last_modified: 2026-09-18 14:10
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
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
intents:
  - 檢視定期定額訂單數量與價值
  - 分析定期訂單持續長度與取消狀況
  - 掌握顧客訂閱續訂與流失趨勢
features:
  - 定期訂單數據卡
  - 持續長度圖表
  - 取消狀況圖表
  - 圖表日期區間調整
prerequisites:
  - 已開通定期定額功能
  - 方案支援分析報表功能
devices:
  - desktop
apis: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/business-intelligence/periodic-order-analysis/"
icon: lucide/calendar-clock
hide: []
---

![Subscription Order Analysis page](../../assets/images/ec-bi-periodic-order-analysis-hero.en.png){ title="Subscription Order Analysis Page" }

## About Subscription Order Analysis { #intro-periodic-orders }

"Subscription Order Analysis" is under "Charts" in the admin. It organizes data from all your store's subscription orders into data cards and charts, so you can see at a glance how many subscription orders you have, how much value they bring, how many cycles customers usually keep subscribing, and at which cycle they cancel.

When you open the page, its title shows as **"Periodic Order Analysis"**. This is the same page as "Subscription Order Analysis" in the left menu.

From top to bottom, the page has two parts:

- **Key data cards:** Show total subscription orders, total cycles completed, and total value as all-time cumulative figures.
- **Trend and share charts:** Show the distribution of subscription orders as pie and bar charts from two angles, "duration (number of cycles)" and "cancellations."

!!! info "Tip"
    Here a "subscription order" is one subscription created by a customer (it automatically generates each cycle's delivery and charge on schedule), and a "cycle" is each delivery that subscription actually generates. Keep these two levels in mind when reading the charts.

## Prerequisites and Limitations { #prerequisites-periodic-orders }

Subscription Order Analysis is under "Charts" in the admin. Your plan must have the **"Subscription Orders"** feature turned on for there to be subscription order data to analyze.

!!! plan "Plan / Activation Requirements"
    Subscription Order Analysis is a feature of the **Enterprise** plan. PLUS plans can add it as an option.

## Page Overview { #overview-periodic-orders }

| Section | Type | What It Shows | Affected by Date |
| :-- | :-- | :-- | :-- |
| Total Subscription Orders | Number card | Cumulative number of subscription orders created in your store | No (all-time cumulative) |
| Total Cycles Completed | Number card | Total number of cycles actually delivered for all subscription orders | No (all-time cumulative) |
| Total Subscription Order Value | Number card | Total sales amount of orders actually placed from subscription orders | No (all-time cumulative) |
| Subscription Order Duration Ratio Chart | Pie chart | Share of subscription orders at each "number of cycles completed" | Yes |
| Subscription Order Duration Chart | Bar chart | Number of subscription orders at each "number of cycles completed" | Yes |
| Cancellation at Cycle N Ratio Chart | Pie chart | For canceled subscription orders, the share canceled at each cycle | Yes |
| Cancellation at Cycle N Count Chart | Bar chart | For canceled subscription orders, the number canceled at each cycle | Yes |
| Subscription Order Cancellation Ratio Chart | Pie chart | Share of "canceled / not canceled" among all subscription orders | Yes |
| Single-Cycle Cancellation Ratio Chart | Pie chart | Share of "canceled / not canceled" by individual delivery cycle | Yes |

For detailed definitions of each metric, see [Subscription Order Analysis Metric Definitions Reference](references/periodic-order-analysis-metrics-reference.md#reference-periodic-orders-charts){ title="Subscription Order Analysis Metric Definitions Reference" data-preview }.

## Steps { #operate-periodic-orders }

### Open Subscription Order Analysis { #operate-periodic-orders-enter }

1. **Go to Charts:** In the left menu of the admin, click **"Charts"**.
2. **Open the page:** In the expanded items, click **"Subscription Order Analysis"** to open the page.
3. **Wait for the data to load:** The data cards and charts load automatically in batches. A spinner appears while loading. You don't need to do anything.

---

### View the Key Data Cards { #operate-periodic-orders-read-cards }

When you open the page, three key data cards load automatically at the top, showing all-time cumulative figures:

1. **Total Subscription Orders:** The cumulative number of subscription orders created in your store, counted in orders.
2. **Total Cycles Completed:** The total number of cycles actually delivered for all subscription orders, counted in cycles.
3. **Total Subscription Order Value:** The total sales amount of orders actually placed from subscription orders.

![Key data cards](../../assets/images/ec-bi-periodic-cards.zh-tw.en.png){ title="Key Data Cards" }

!!! note "Note"
    These three data cards are **all-time cumulative** and are not affected by the chart date ranges below. The number cards do not change when you adjust chart dates.

---

### Read the Duration Charts { #operate-periodic-orders-read-duration }

The "Subscription Order Duration Ratio Chart" (pie chart) and the "Subscription Order Duration Chart" (bar chart) show two views of the same data: how many cycles customers' subscription orders usually last.

1. **View the distribution:** The charts group subscription orders by "duration (number of cycles)," so you can see how many cycles most subscription orders last.
2. **Use the ratio chart for shares:** The pie chart shows the percentage of subscription orders at each duration.
3. **Use the bar chart for counts:** The bar chart has "duration" on the x-axis and "count" on the y-axis, showing how many subscription orders there are at each duration.
4. **View details:** Hover over a slice or bar to see the count and share for that group. Click an item name to hide or show its data.

![Duration charts](../../assets/images/ec-bi-periodic-duration-charts.zh-tw.en.png){ title="Duration Charts" }

!!! tip "Tip"
    If most subscription orders last only 1 or 2 cycles, customers are not very willing to renew. Check the "Cancellation at Cycle N" charts to find the key cycle where customers drop off.

---

### Read the Cancellation Charts { #operate-periodic-orders-read-cancel }

The four charts in the lower half of the page show subscription order cancellations from different angles:

1. **Cancellation at Cycle N Ratio Chart / Count Chart:** These count only **canceled** subscription orders and show at which cycle they tend to be canceled. The ratio chart shows the share at each cycle; the count chart has "cycle" on the x-axis and "count" on the y-axis.

    ![Cancellation at Cycle N ratio chart / count chart](../../assets/images/ec-bi-periodic-cancel-nth-stage.zh-tw.en.png){ title="Cancellation at Cycle N Ratio Chart / Count Chart" }

2. **Subscription Order Cancellation Ratio Chart:** Shows the share of "canceled" and "not canceled," counting by whole subscription order.

    ![Subscription order cancellation ratio chart](../../assets/images/ec-bi-periodic-cancel-rate.zh-tw.en.png){ title="Subscription Order Cancellation Ratio Chart" }

3. **Single-Cycle Cancellation Ratio Chart:** Shows the share of "canceled" and "not canceled," counting by individual delivery cycle[^1].

    ![Single-cycle cancellation ratio chart](../../assets/images/ec-bi-periodic-single-cancel-rate.zh-tw.en.png){ title="Single-Cycle Cancellation Ratio Chart" }

4. **View details:** Hover over a slice to see the count and share for that item. Click an item name to hide or show its data.

[^1]: "Subscription Order Cancellation Ratio" looks at whether the whole subscription was canceled, while "Single-Cycle Cancellation Ratio" looks at whether each delivery was canceled. Because they count at different levels, the numbers are usually different.

---

### Adjust the Chart Period { #operate-periodic-orders-date-range }

**Each chart has its own date range field in the upper-right corner**, so you can set the time range for each chart separately:

1. **Click the date field:** In the upper-right corner of the chart you want to adjust, click the date input box to open the date picker.
2. **Choose a preset or custom range:** Select a preset range (Today, Yesterday, Last 7 Days, Last 30 Days, This Month, Last Month), or select start and end dates on the calendar.
3. **Apply:** Click **"Apply"** to reload the chart for the new period.

![Adjust the date range](../../assets/images/ec-bi-periodic-date-range.zh-tw.en.png){ title="Adjust the Date Range" }

!!! tip "Tip"
    Each chart's date range is **independent**, so changing one does not affect the others. When the page first loads, each chart shows about the last 6 months by default. To compare them as a whole, set each chart to the same range one by one.

## Important Rules and Limitations { #specs-periodic-orders }

- **Data cards are all-time cumulative:** The three number cards at the top are not affected by the chart date ranges and show your store's cumulative figures to date.
- **Only the charts use date ranges:** Each of the six charts uses its own date range and counts by subscription order creation time.
- **Cancellation ratios have two levels:** "Subscription Order Cancellation Ratio" counts by whole subscription, while "Single-Cycle Cancellation Ratio" counts by each delivery. The numbers are usually different.

## Next Steps { #next-steps-periodic-orders }

<div class="grid cards" markdown>

<!-- - :lucide-repeat:{ .lg }  
  [__Subscription Orders__](../orders/index.md)  
  View and manage each subscription order and its delivery cycles one by one. -->

- :lucide-bar-chart-3:{ .lg }  
  [__Revenue Analysis__](../business-intelligence/revenue-analysis.md){ title="Revenue Analysis" }  
  View overall revenue, profit, and peak revenue hours across your store.

</div>

## FAQ { #faq-periodic-orders }

??? quote "I changed the chart dates, but the number cards at the top didn't change"
    [](){ #faq-periodic-orders-cards-static }
    This is normal. The three data cards at the top show all-time cumulative figures.

    - The data cards (total subscription orders, total cycles, total value) are not affected by the chart date ranges.
    - Only the six charts below update based on their own date ranges.

??? quote "What does "duration" mean?"
    [](){ #faq-periodic-orders-duration }
    "Duration" is the number of delivery cycles a subscription order has actually completed.

    - For example, a duration of 3 means this subscription order has been delivered (or charged) for 3 cycles.
    - A longer duration usually means customers are more loyal to the subscription.

??? quote "What's the difference between "Subscription Order Cancellation Ratio" and "Single-Cycle Cancellation Ratio"?"
    [](){ #faq-periodic-orders-cancel-level }
    They count at different levels.

    - **Subscription Order Cancellation Ratio:** Counts by whole subscription order (subscription) and shows what share of subscriptions were canceled.
    - **Single-Cycle Cancellation Ratio:** Counts by each delivery and shows what share of individual deliveries were canceled.
    - Because the levels differ, the two numbers are usually different.

<!-- ??? quote "I want to see details for each subscription order" -->
<!--     [](){ #faq-periodic-orders-detail } -->
<!--     This page shows summary charts only. It does not provide order-by-order details or an export feature. -->
<!---->
<!--     - To view or manage individual subscription orders and their delivery cycles, go to the subscription order list. -->

## References { #reference-periodic-orders }

- [Subscription Order Analysis Metric Definitions Reference](references/periodic-order-analysis-metrics-reference.md)
