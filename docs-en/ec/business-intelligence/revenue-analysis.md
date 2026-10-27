---
title: "Revenue Analysis"
description: "Use data cards and a variety of charts to quickly see store-wide revenue performance, profitability, and peak revenue hours."
created: 2026-06-15 00:00
last_modified: 2026-07-20 18:40
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
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
intents:
  - 查看全店營收表現
  - 分析營收趨勢與獲利狀況
  - 找出營收高峰時段
features:
  - 營收數據卡
  - 營收總覽折線圖
  - 營收占比圖表
  - 時段分析圖表
prerequisites:
  - 已開通 CYBERBIZ 商店後台
  - 方案已包含營收分析功能
devices:
  - desktop
apis: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5041
  - https://www.cyberbiz.io/support/?p=8368
permalink: "https://help.cyberbiz.io/ec/business-intelligence/revenue-analysis/"
icon: lucide/trending-up
hide:
---

![Revenue Analysis page](../../assets/images/ec-bi-revenue-hero.zh-tw.en.png){ title="Revenue Analysis Page" .hero-page }

## About Revenue Analysis { #intro-revenue }

"Revenue Analysis" is under "Charts" in the admin. It organizes store-wide order data into data cards and charts, so you can see at a glance your overall revenue, recent growth, profitability, and how revenue breaks down by payment method, shipping method, member type, and time period.

From top to bottom, the page has three parts:

- **Key data cards**: Show total revenue, revenue and growth rate in the last 30 days, and gross profit and gross margin in the last 30 days.
- **Revenue overview chart**: Shows how each type of revenue and cost changes over time as a line chart.
- **Multi-dimension share and time period charts**: Show the makeup and peaks of revenue by order status, payment method, member type, shipping method, and hour / day of week / day of month.

## Prerequisites and Limitations { #prerequisites-revenue }

### Recognized Order Definition { #prerequisites-revenue-counted-orders }

All figures in Revenue Analysis are calculated from "recognized orders." A recognized order meets these conditions:

- [x] **Order Status**: The order status is not canceled.
- [x] **Return Status**: The return status is "No Return Needed" or "Return Rejected."

In other words, amounts from canceled and returned orders are **not** counted as revenue. This is the main reason figures on the page may differ from the total amount in the order list.

!!! note "Note"
    In the "Revenue Overview" chart, canceled order revenue, returned order revenue, and unclaimed order revenue appear as **separate lines**, so you can view these uncounted amounts on their own. They are not added to total revenue.

### Data Update Time { #specs-revenue-data-update }

The system updates data daily at these times:

- **00:00**, **08:00**, **12:00**, **16:00**, **20:00**

> Because data processing takes some time, the data shown may lag slightly behind the current situation.

## Page Overview { #overview-revenue }

| Section | Chart Type | What It Shows |
| :-- | :-- | :-- |
| [Key Data Cards ×3](#operate-revenue-read-cards) | Number card | Total revenue, revenue / growth rate in the last 30 days, gross profit / gross margin in the last 30 days |
| [Revenue Overview](#operate-revenue-read-overview) | Line chart | Changes over time in undiscounted revenue, active order revenue, canceled / returned / unclaimed order revenue, cost, and gross profit |
| [Order Active Status](#operate-revenue-read-order-status) (revenue share) | Pie chart | How much revenue each order status accounts for |
| [Payment Method](#operate-revenue-read-payment) (revenue share) | Pie chart | Share of revenue from each payment method |
| [Existing Members vs. New Members](#operate-revenue-read-member) (revenue share) | Bar chart | Compare revenue contribution of new and existing members |
| [Shipping Method](#operate-revenue-read-shipping) (revenue share) | Pie chart | Share of revenue from each shipping method |
| [Average Revenue by Hour](#operate-revenue-read-hourly) | Line chart | Average revenue and today's revenue for each hour of the day, to find peak revenue hours |
| [Average Revenue by Day of Week](#operate-revenue-read-weekday) | Bar chart | Average revenue from Monday to Sunday in the period, plus this week's revenue |
| [Average Revenue by Day of Month](#operate-revenue-read-daily) | Bar chart | Average revenue for each day in the period, plus each day's revenue this month |

For detailed definitions of each metric, see [Revenue Metric Definitions Reference](references/revenue-analysis-metrics-reference.md#reference-revenue-metrics){ title="Revenue Analysis Metric Definitions Reference" data-preview }.

## Steps { #operate-revenue }

### View Key Revenue Figures { #operate-revenue-read-cards }

When you open the page, three key data cards load automatically at the top. You don't need to do anything:

1. **Total Revenue:** Shows the cumulative total of recognized order revenue across the store.
2. **Revenue in the Last 30 Days / Revenue Growth Rate:** Shows revenue for the last 30 days and the growth percentage compared with the previous period of the same length.
3. **Gross Profit in the Last 30 Days / Gross Margin:** Shows the gross profit amount and gross margin for the last 30 days[^1].

[^1]: Gross profit and gross margin are calculated correctly only after you enter cost prices in product settings. If products have no cost set, gross profit will be too high.
[^2]: Average revenue calculation: within the specified date range, the total order amount for the same hour each day ÷ total number of days.
[^3]: Average revenue calculation: within the specified date range, the total of all orders on each day of the week ÷ total number of weeks.
[^4]: Average revenue calculation: within the specified date range, the total of all orders on each day across all months ÷ total number of months.

![Key data cards](../../assets/images/ec-bi-revenue-cards.zh-tw.en.png){ title="Key Data Cards" }

---

### Read the Revenue Overview Line Chart { #operate-revenue-read-overview }

"Revenue Overview" uses multiple lines to show different types of revenue and cost:

1. **View each line:** Each line in the chart represents one type of revenue or cost (for example, active order revenue, returned order revenue, cost, and gross profit).
2. **See item descriptions:** Hover over the legend (the item names above the chart) to see the definition of that item.
3. **Show or hide items:** Click an item name above the chart to hide or show its data line, so you can focus on specific items.
4. **Compare trends:** Compare the relative height of the lines in the same chart to see how revenue, cost, and gross profit change in relation to each other over time.

![Revenue overview line chart](../../assets/images/ec-bi-revenue-overview-chart.zh-tw.en.png){ title="Revenue Overview Line Chart" }

For full definitions of each line, see [Revenue Metric Definitions Reference](references/revenue-analysis-metrics-reference.md#reference-revenue-metrics){ title="Revenue Analysis Metric Definitions Reference" data-preview }.

---

### Adjust the Chart Period { #operate-revenue-date-range }

**Each chart has its own date range field in the upper-right corner**, so you can set the time range for each chart separately:

1. **Click the date field:** In the upper-right corner of the chart you want to adjust, click the date input box to open the date picker.
2. **Choose a preset or custom range:** Select a preset range (Today, Yesterday, Last 7 Days, Last 30 Days, This Month, Last Month), or select start and end dates on the calendar.
3. **Apply:** Click **"Apply"** to reload the chart for the new period.

![Adjust the date range](../../assets/images/ec-bi-revenue-date-range.zh-tw.en.png){ title="Adjust the Date Range" }

!!! tip "Tip"
    Each chart's date range is **independent**, so changing one does not affect the others. When the page first loads, each chart shows about the last six months by default. To compare them as a whole, set each chart to the same range one by one.

---

### Order Active Status <small>Revenue Share</small> { #operate-revenue-read-order-status }

A pie chart showing how much revenue each order status accounts for. The items are:

- **Active Order Revenue:** Revenue from validly placed orders.
- **Canceled Order Revenue:** Amounts from canceled orders.
- **Returned Order Revenue:** Amounts from returned orders.

Hover over a slice to see the revenue amount and share percentage for that item. Click an item name to hide or show its data.

![Order active status revenue share](../../assets/images/ec-bi-revenue-order-status.zh-tw.en.png){ title="Order Active Status Revenue Share" }

---

### Payment Method <small>Revenue Share</small> { #operate-revenue-read-payment }

A pie chart showing the share of revenue from each payment method. Items appear dynamically based on the payment methods your store actually uses (for example, credit card, convenience store payment, and cash on delivery). Methods that aren't used do not appear.

Hover over a slice to see the revenue amount and share percentage for that payment method. Click an item name to hide or show its data.

![Payment method revenue share](../../assets/images/ec-bi-revenue-payment-method.zh-tw.en.png){ title="Payment Method Revenue Share" }

---

### Shipping Method <small>Revenue Share</small> { #operate-revenue-read-shipping }

A pie chart showing the share of revenue from each shipping method. Items appear dynamically based on the shipping methods your store actually uses (for example, home delivery and custom shipping methods). Methods that aren't used do not appear.

Hover over a slice to see the revenue amount and share percentage for that shipping method. Click an item name to hide or show its data.

![Shipping method revenue share](../../assets/images/ec-bi-revenue-shipping-method.zh-tw.en.png){ title="Shipping Method Revenue Share" }

---

### Existing Members vs. New Members <small>Revenue Share</small> { #operate-revenue-read-member }

A bar chart comparing the revenue contribution share of new and existing members, so you can see whether revenue mainly comes from new or returning customers.

Hover over a bar to see the revenue amount for each member type. Click an item name to hide or show its data.

![New and existing member revenue share](../../assets/images/ec-bi-revenue-member-type.zh-tw.en.png){ title="New and Existing Member Revenue Share" }

---

### Average Revenue by Hour { #operate-revenue-read-hourly }

A line chart showing how revenue is distributed across the 24 hours of the day, to help you find peak revenue hours. It shows two sets of data:

- **Average revenue by hour for the period:** The average revenue for each hour in the selected period[^2].
- **Today's revenue by hour:** Revenue for each hour so far today.

Hover over a data point to see the revenue amount for that hour. Click an item name to hide or show its data.

![Average revenue by hour](../../assets/images/ec-bi-revenue-hourly.zh-tw.en.png){ title="Average Revenue by Hour" }

---

### Average Revenue by Day of Week { #operate-revenue-read-weekday }

A bar chart showing how revenue is distributed from Monday to Sunday. It shows two sets of data:

- **Average revenue by day of week:** The average revenue for each day from Monday to Sunday in the selected period[^3].
- **This week's revenue by day:** Revenue for each day so far this week.

Hover over a bar to see the revenue amount for that day. Click an item name to hide or show its data.

![Average revenue by day of week](../../assets/images/ec-bi-revenue-weekly.zh-tw.en.png){ title="Average Revenue by Day of Week" }

---

### Average Revenue by Day of Month { #operate-revenue-read-daily }

A bar chart showing how revenue is distributed across the days of a month. It shows two sets of data:

- **Average revenue by day for the period:** The average revenue for each day in the selected period[^4].
- **This month's revenue by day:** Revenue for each day so far this month.

Hover over a bar to see the revenue amount for that day. Click an item name to hide or show its data.

![Average revenue by day of month](../../assets/images/ec-bi-revenue-daily.zh-tw.en.png){ title="Average Revenue by Day of Month" }

## Important Rules and Limitations { #specs-revenue }

- **Data is based on recognized orders:** Canceled and returned orders are not counted as revenue, so figures may differ from the total amount in the order list.
- **Share chart items appear dynamically:** Items in share charts such as payment method and shipping method appear based on the methods your store actually uses. Methods that aren't used do not appear.
- **Gross profit depends on product cost:** Gross profit and cost figures are accurate only after you enter cost prices in product settings.
- **Number format:** Revenue and amounts are shown as whole numbers with thousands separators. Positive growth rates are shown with a leading `+`.

## FAQ { #faq-revenue }

<!-- ??? quote "The page shows "Your current plan does not support this feature"" -->
<!--     [](){ #faq-revenue-plan } -->
<!--     This means your current plan does not include Revenue Analysis yet. -->
<!---->
<!--     - Contact customer service or your store consultant to check whether you can upgrade your plan or add the data analysis feature. -->

??? quote "Chart figures don't match the amounts in the order list"
    [](){ #faq-revenue-counted-orders }
    Revenue Analysis counts only "recognized orders," which are orders that are not canceled and not returned (no return needed or return rejected).

    - Amounts from canceled and returned orders are not counted as revenue.
    - For details, see [Recognized Order Definition](#prerequisites-revenue-counted-orders){ title="Recognized Order Definition" data-preview }.

??? quote "Gross profit shows 0 or seems too low"
    [](){ #faq-revenue-gross-profit }
    Gross profit is calculated as "revenue from placed orders minus total product cost," so products need a cost price set.

    - If a product has no cost price in product settings, the system calculates its cost as 0, which makes gross profit too high or inaccurate.
    - Add cost prices to your products first, then return to this page to check gross profit.

??? quote "I changed the date on one chart, but the other charts didn't change"
    [](){ #faq-revenue-date-range }
    This is normal. Each chart's date range is independent.

    - To show the same time range on multiple charts, set each chart's date field to the same range one by one.

## References { #reference-revenue }

- [Revenue Analysis Metric Definitions Reference](references/revenue-analysis-metrics-reference.md)
