---
title: "Order Analysis"
description: "Use the Order Analysis page to view sales trends, payment and shipping preferences, and sales reports."
created: 2026-06-15 00:00
last_modified: 2026-07-10 13:12
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
cyb_extensions: []
intents:
  - 查看訂單銷售趨勢
  - 分析付款與出貨偏好
  - 下載業績明細報表
features:
  - 訂單總體分析
  - 訂單金物流分析
  - 訂單報表
prerequisites:
  - 已開通 CYBERBIZ 商店後台
related:
  - ec/business-intelligence/references/order-analysis-overview-metrics-reference/
  - ec/business-intelligence/references/order-analysis-finance-logistics-reference/
  - ec/business-intelligence/references/order-analysis-report-fields-reference/
tags:
  - "Order Analysis"
  - "Order Overview Analysis"
  - "Order Payment and Shipping Analysis"
  - "Order Reports"
  - "Cancellation Rate"
  - "Return Rate"
  - "Change Value"
  - "Analysis Reports"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分析報表 > 訂單分析
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5043
  - https://www.cyberbiz.io/support/?p=8473
  - https://www.cyberbiz.io/support/?p=8714
  - https://www.cyberbiz.io/support/?p=9602
permalink: "https://help.cyberbiz.io/ec/business-intelligence/order-analysis/"
comments: false
search:
  exclude: false
icon: lucide/shopping-cart
hide:
---

![Order Analysis page](../../assets/images/ec-bi-order-hero.en.png){ title="Order Analysis Page" .hero-page }

## About Order Analysis { #intro-order-analysis }

"Order Analysis" is a report page for understanding your store's performance. From high-level sales trends to details such as cancellation rate, return rate, and referral sources, it helps you quickly understand the overall health of your orders.

The page has three tabs: **Order Overview Analysis** (overall sales trends and health metrics), **Order Payment and Shipping Analysis** (payment and shipping preferences), and **Order Reports** (downloadable sales detail tables).

## Page Overview { #overview-order-analysis }

| Tab | What You Can See |
| :-- | :-- |
| Order Overview Analysis | Store-wide order volume, average order value, distribution of order amount and item count per order, and health metrics such as cancellation rate and return rate. |
| Order Payment and Shipping Analysis | Order count trends, shares, average order value, and return rate broken down by payment method, shipping method, and third-party referral. |
| Order Reports | Three tables you can download as Excel: date range comparison, sales by time slot, and daily sales. |


### Order Overview Analysis Charts { #overview-order-analysis-overall }

| Chart | What It Shows | Details |
| :-- | :-- | :-- |
| Total Orders | Cumulative number of recognized orders for the whole store. | [Go](#total-orders) |
| Orders in the Last 30 Days | Orders in the last 30 days, with change value. | [Go](#orders-in-the-last-30-days) |
| Monthly Order Trend | Number of orders per month (by order creation time). | [Go](#monthly-order-trend) |
| Average Daily Orders (Monthly Trend) | Average daily orders per month, with the last 30 days and change value. | [Go](#average-daily-orders-monthly-trend) |
| Monthly Order Amount Trend | Number of orders per month grouped by amount range. | [Go](#monthly-order-amount-trend) |
| Monthly Order Amount Trend (Ratio) | Share of each amount range in the selected month. | [Go](#monthly-order-amount-trend-ratio) |
| Order Amount (Share) | Share of each amount range within the period. | [Go](#order-amount-share) |
| Items per Order (Share) | Share of each item-count range (including add-on purchases and spend-threshold gifts). | [Go](#items-per-order-share) |
| Average Daily Order Amount (Monthly Trend) | Average daily order amount per month, with the last 30 days and change value. | [Go](#average-daily-order-amount-monthly-trend) |
| Monthly Order Cancellation Rate Trend | Cancellation rate per month, with the last 30 days and change value. | [Go](#monthly-order-cancellation-rate-trend) |
| Monthly Order Return Rate Trend | Return rate per month, with the last 30 days and change value. | [Go](#monthly-order-return-rate-trend) |

For detailed definitions of each metric, see the [Order Overview Analysis Metrics Reference](references/order-analysis-overview-metrics-reference.md#reference-order-analysis-overview-metrics){ data-preview }.

---

### Order Payment and Shipping Analysis Charts { #overview-order-analysis-finance-logistics }

=== "Payment Method"
    | Chart | What It Shows | Details |
    | :-- | :-- | :-- |
    | Orders (Monthly Trend) | Orders per payment method per month. | [Go](#overview-order-analysis-payment) |
    | Share (Monthly Trend) | Order share of each payment method per month. | [Go](#overview-order-analysis-payment) |
    | Share (Period) | Order share of each payment method within the period. | [Go](#overview-order-analysis-payment) |
    | Average Order Value (Monthly Trend) | Average order value of each payment method per month. | [Go](#overview-order-analysis-payment) |
    | Average Order Value (Period) | Average order value of each payment method within the period. | [Go](#overview-order-analysis-payment) |
    | Return Rate (Monthly Trend) | Return rate of each payment method per month. | [Go](#overview-order-analysis-payment) |
    | Return Rate (Period) | Return rate of each payment method within the period. | [Go](#overview-order-analysis-payment) |

=== "Shipping Method"
    | Chart | What It Shows | Details |
    | :-- | :-- | :-- |
    | Orders (Monthly Trend) | Orders per shipping method per month. | [Go](#overview-order-analysis-shipping) |
    | Share (Monthly Trend) | Recognized order share of each shipping method per month. | [Go](#overview-order-analysis-shipping) |
    | Share (Period) | Recognized order share of each shipping method within the period. | [Go](#overview-order-analysis-shipping) |
    | Average Order Value (Monthly Trend) | Average order value of each shipping method per month. | [Go](#overview-order-analysis-shipping) |
    | Average Order Value (Period) | Average order value of each shipping method within the period. | [Go](#overview-order-analysis-shipping) |
    | Return Rate (Monthly Trend) | Return rate of each shipping method per month. | [Go](#overview-order-analysis-shipping) |
    | Return Rate (Period) | Return rate of each shipping method within the period. | [Go](#overview-order-analysis-shipping) |

=== "Third-Party Referral"
    | Chart | What It Shows | Details |
    | :-- | :-- | :-- |
    | Orders (Monthly Trend) | Orders per source per month. | [Go](#overview-order-analysis-third-party) |
    | Share (Period) | Recognized order share of each source within the period. | [Go](#overview-order-analysis-third-party) |
    | Average Order Value (Monthly Trend) | Average order value of each source per month. | [Go](#overview-order-analysis-third-party) |
    | Average Order Value (Period) | Average order value of each source within the period. | [Go](#overview-order-analysis-third-party) |
    | Return Rate (Monthly Trend) | Return rate of each source per month. | [Go](#overview-order-analysis-third-party) |
    | Return Rate (Period) | Return rate of each source within the period. | [Go](#overview-order-analysis-third-party) |

For detailed definitions of each chart, see the [Order Payment and Shipping Analysis Chart Reference](references/order-analysis-finance-logistics-reference.md#reference-order-analysis-finance-logistics){ title="Order Payment and Shipping Analysis Chart Reference" data-preview }.

!!! note "Different Bases"
    Payment method shares use **total orders** as the base. Shipping method and third-party referral shares and average order value use [recognized orders](#prerequisites-order-analysis-recognized-order){ title="Recognized Order Definition" } as the base. For return rate in every dimension, the denominator is always "non-canceled orders."

<!---->
<!-- ### Order Overview Analysis Charts -->
<!---->
<!-- | Section | Chart Type | What It Shows | -->
<!-- | :-- | :-- | :-- | -->
<!-- | Total Orders | Figure card | Cumulative number of recognized orders for the whole store. | -->
<!-- | Orders in the Last 30 Days | Figure card (with change value) | Orders in the last 30 days, compared with the past 30 days and the long-term average. | -->
<!-- | Order Amount Distribution | Chart | Distribution of recognized orders by order amount range. | -->
<!-- | Item Count Distribution | Chart | Distribution of recognized orders by item count range. | -->
<!-- | Cancellation Rate Trend | Trend chart | How the cancellation rate changes over time. | -->
<!-- | Return Rate Trend | Trend chart | How the return rate changes over time (based on recognized orders after excluding cancellations). | -->
<!---->
<!---->
<!-- For detailed definitions of each metric, see the [Order Overview Analysis Metrics Reference][reference-order-analysis-overview-metrics]{ data-preview }. -->
<!---->
<!-- --- -->
<!---->
<!-- ### Order Payment and Shipping Analysis Charts -->
<!---->
<!-- | Dimension | Chart Type | What It Shows | -->
<!-- | :-- | :-- | :-- | -->
<!-- | Payment Method | Share / Details | Orders, share, average order value, and return rate of each payment method. | -->
<!-- | Shipping Method | Share / Details | Orders, share, average order value, and return rate of each shipping method. | -->
<!-- | Third-Party Referral | Share / Details | Orders, share, average order value, and return rate of each referral source (shown only when a referral platform is connected). | -->
<!---->
<!---->
<!-- For detailed definitions of each chart, see the [Order Payment and Shipping Analysis Chart Reference][reference-order-analysis-finance-logistics]{ data-preview }. -->

---

### Order Reports Tables { #overview-order-analysis-report }

| Table | What It Shows |
| :-- | :-- |
| Date Range Comparison | Sales comparison between two date ranges. |
| Sales by Time Slot | Sales performance by time slot. |
| Daily Sales | Sales performance by day. |

For what each table's fields mean, see the [Order Report Field Reference](references/order-analysis-report-fields-reference.md){ title="Order Report Field Reference" }.

## Prerequisites and Limitations { #prerequisites-order-analysis }

### Recognized Order Definition { #prerequisites-order-analysis-recognized-order }

Order Analysis data doesn't include every order. It counts only "recognized orders." A recognized order must meet both of these conditions:

- [x] **Order Status**: "Non-canceled order."
- [x] **Return Status**: "No Return Needed or Return Rejected."

In other words, canceled orders and orders with a completed return aren't counted in sales data.

---

### Plan Differences { #prerequisites-order-analysis-plan }

The "Order Payment and Shipping Analysis" and "Order Reports" tabs are available only on the **Enterprise** plan. If you can see only the "Order Overview Analysis" tab, your current plan doesn't include the other two tabs.

??? plan "Which plans show only "Order Overview Analysis"?"
    The following four plans **show only "Order Overview Analysis"** and don't have the "Order Payment and Shipping Analysis" and "Order Reports" tabs:

    * Pro
    * Pro PLUS
    * Professional PLUS
    * Advanced PLUS

---

### Display Conditions for Third-Party Referral Charts { #prerequisites-order-analysis-third-party }

The **Third-Party Referral** charts in "Order Payment and Shipping Analysis" appear only if your store is connected to a referral platform. They appear if any of the following conditions is met:

* "Market America Partner Store" is set up
* "LINE Shopping" is connected

If none of these are enabled, the whole set of third-party referral charts isn't shown.

---

## Steps { #operate-order-analysis }

### Open Order Analysis { #operate-order-analysis-enter }

1. In the left menu of the admin, click **"Charts."**
2. Click **"Order Analysis"** to open the Order Analysis page. It shows the "Order Overview Analysis" tab by default.

---

### Switch Analysis Tabs { #operate-order-analysis-switch-tab }

There are tabs at the top of the page. Click one to switch to a different analysis view:

1. Click **"Order Overview Analysis"** to view overall sales trends and health metrics.
2. Click **"Order Payment and Shipping Analysis"** to view performance by payment method, shipping method, and third-party referral.
3. Click **"Order Reports"** to view and download sales detail tables.

![Switch analysis tabs](../../assets/images/ec-bi-order-switch-tab.zh-tw.en.png){ title="Switch Analysis Tabs" }

!!! info "Tip"
    If you can see only the "Order Overview Analysis" tab, this is due to plan differences. See [Plan Differences](#prerequisites-order-analysis-plan){ title="Plan Differences" }.

---

### Adjust the Date Range of Charts and Reports { #operate-order-analysis-date-range }

Each chart and report has its own date picker, so you can adjust the period for each one separately:

1. Click the **date field** on the chart (or report).
2. Choose a preset range (Last 7 days, Last 30 days, This month, Last month), or choose "Custom" to select your own start and end dates.
3. Click **Apply**, and the chart refreshes with the new range.

![Adjust the date range](../../assets/images/ec-bi-order-date-range.zh-tw.en.png){ title="Adjust the Date Range" }

!!! note "Note"
    The date format is MM/DD/YYYY. Each chart is adjusted independently, so changing one doesn't affect the others.

---

### Download Order Reports as Excel { #operate-order-analysis-download }

All three tables on the "Order Reports" tab can be downloaded as Excel for further analysis:

1. Switch to the **"Order Reports"** tab.
2. Find the table to download (Date Range Comparison, Sales by Time Slot, or Daily Sales).
3. Click the **"Download as Excel"** button in the upper-right corner of the table to download the file.

=== "Date Range Comparison"

    ![Date range comparison](../../assets/images/ec-bi-order-report-compare.zh-tw.en.png){ title="Date Range Comparison" }

    For field descriptions, see the [Order Report Field Reference](references/order-analysis-report-fields-reference.md#reference-order-analysis-report-compare){ data-preview }.

=== "Sales by Time Slot"

    ![Sales by time slot](../../assets/images/ec-bi-order-report-by-time.zh-tw.en.png){ title="Sales by Time Slot" }

    For field descriptions, see the [Order Report Field Reference](references/order-analysis-report-fields-reference.md#reference-order-analysis-report-by-time){ data-preview }.

=== "Daily Sales"

    ![Daily sales](../../assets/images/ec-bi-order-report-daily.zh-tw.en.png){ title="Daily Sales" }

    For field descriptions, see the [Order Report Field Reference](references/order-analysis-report-fields-reference.md#reference-order-analysis-report-daily){ data-preview }.

!!! tip "Tip"
    Chart sections (Order Overview Analysis, Order Payment and Shipping Analysis) can't be downloaded. To export data, use the three tables on the "Order Reports" tab.

---

## Understanding Order Overview Analysis { #overview-order-analysis-overall }

"Order Overview Analysis" uses data cards and several trend and share charts to show the overall health of the store's orders. For the full definitions and formulas of each chart, see the [Order Overview Analysis Metrics Reference](references/order-analysis-overview-metrics-reference.md#reference-order-analysis-overview-metrics){ data-preview }.

### Order Volume { #overview-order-analysis-volume }

=== "Total Orders"

    Total number of recognized orders since the store opened.

    ![Total orders](../../assets/images/ec-bi-order-total-orders.zh-tw.en.png){ title="Total Orders" }

=== "Orders in the Last 30 Days"

    Orders in the 30 days before the current date. The **change value**[^1] on the card compares the past 30 days with the long-term average since the store opened. A positive value means growth.

    ![Orders in the last 30 days](../../assets/images/ec-bi-order-30d-orders.zh-tw.en.png){ title="Orders in the Last 30 Days" }

=== "Monthly Order Trend"

    Number of orders per month in the time range (by order creation time). By default, it shows the 6 months before today.

    ![Monthly order trend](../../assets/images/ec-bi-order-monthly-orders.zh-tw.en.png){ title="Monthly Order Trend" }

=== "Average Daily Orders (Monthly Trend)"

    Average daily orders per month (total orders in the month ÷ days in the month), plus **average daily orders in the last 30 days**[^6] and **change value**[^2].

    ![Average daily orders (monthly trend)](../../assets/images/ec-bi-order-daily-avg-orders.zh-tw.en.png){ title="Average Daily Orders (Monthly Trend)" }

---

### Order Amount and Item Count { #overview-order-analysis-amount }

=== "Monthly Order Amount Trend"

    Number of orders per month grouped by order amount range. For example, in February 2020, there were 3 orders with amounts of 0–NT$1000.

    Hover over a data point to see the number of orders in that amount range. Click an item name to hide or show its data.

    ![Monthly order amount trend](../../assets/images/ec-bi-order-amount-monthly.zh-tw.en.png){ title="Monthly Order Amount Trend" }

=== "Monthly Order Amount Trend (Ratio)"

    Order share of each amount range in the selected month. For example, in May 2020, orders of 3001–NT$5000 accounted for 32.1% of the month.

    Hover over a bar to see the share of that amount range. Click an item name to hide or show its data.

    ![Monthly order amount trend (ratio)](../../assets/images/ec-bi-order-amount-monthly-ratio.zh-tw.en.png){ title="Monthly Order Amount Trend (Ratio)" }

=== "Order Amount (Share)"

    Share of total orders for each amount range in the time range (not split by month).

    Hover over a slice to see the share of that amount range. Click an item name to hide or show its data.

    ![Order amount (share)](../../assets/images/ec-bi-order-amount-ratio.zh-tw.en.png){ title="Order Amount (Share)" }

=== "Items per Order (Share)"

    Order share of each item-count range. Item count **includes add-on purchases and spend-threshold gifts**.

    Hover over a slice to see the share of that item-count range. Click an item name to hide or show its data.

    ![Items per order (share)](../../assets/images/ec-bi-order-item-count-ratio.zh-tw.en.png){ title="Items per Order (Share)" }

=== "Average Daily Order Amount (Monthly Trend)"

    Average daily order amount per month, plus **average order amount in the last 30 days**[^7] and **change value**[^3].

    Hover over a data point to see the average order amount for that month.

    ![Average daily order amount (monthly trend)](../../assets/images/ec-bi-order-daily-avg-amount.zh-tw.en.png){ title="Average Daily Order Amount (Monthly Trend)" }

---

### Order Health { #overview-order-analysis-health }

=== "Monthly Order Cancellation Rate Trend"

    Order cancellation rate per month (canceled orders in the month ÷ all orders in the month), plus **cancellation rate in the last 30 days**[^8] and **change value**[^4].

    Hover over a data point to see the cancellation rate for that month.

    ![Monthly order cancellation rate trend](../../assets/images/ec-bi-order-cancel-rate.zh-tw.en.png){ title="Monthly Order Cancellation Rate Trend" }

=== "Monthly Order Return Rate Trend"

    Order return rate per month (returned orders in the month ÷ orders that aren't "canceled"; canceled orders can't be shipped, so they're excluded), plus **return rate in the last 30 days**[^9] and **change value**[^5].

    Hover over a data point to see the return rate for that month.

    ![Monthly order return rate trend](../../assets/images/ec-bi-order-return-rate.zh-tw.en.png){ title="Monthly Order Return Rate Trend" }

[^1]: Value for the last 30 days − long-term average since the store opened
[^2]: Average orders over the past 30 days − average orders since the store opened
[^3]: Average order amount over the past 30 days − average order amount since the store opened
[^4]: (Canceled in the last 30 days ÷ total orders in the last 30 days) × 100 − (canceled since the store opened ÷ total orders since the store opened) × 100
[^5]: (Returned in the last 30 days ÷ non-canceled orders) × 100 − (returned since the store opened ÷ non-canceled since the store opened) × 100
[^6]: Orders in the last 30 days ÷ 30
[^7]: Order amount in the last 30 days ÷ 30
[^8]: (Canceled in the last 30 days ÷ total orders in the last 30 days) × 100
[^9]: (Returned in the last 30 days ÷ non-canceled orders) × 100

---

## Understanding Order Payment and Shipping Analysis { #overview-order-analysis-finance-logistics }

[:lucide-tag:{ title="Available Plans" }](../../../resources/conventions#適用方案) | Enterprise

"Order Payment and Shipping Analysis" breaks down orders by three dimensions, **payment method, shipping method, and third-party referral**, and looks at them in terms of order count, share, average order value, and return rate. For the full formulas of each chart, see the [Order Payment and Shipping Analysis Chart Reference](references/order-analysis-finance-logistics-reference.md#reference-order-analysis-finance-logistics){ title="Order Payment and Shipping Analysis Chart Reference" }.

### Payment Method { #overview-order-analysis-payment }

=== "Orders (Monthly Trend)"

    Orders per payment method per month.

    Hover over a data point to see the order count for that month. Click an item name to hide or show its data.

    ![Monthly order trend by payment method](../../assets/images/ec-bi-order-payment-count-trend.zh-tw.en.png){ title="Monthly Order Trend by Payment Method" }

=== "Share (Monthly Trend)"

    Order share of each payment method per month. For example, in April 2020, credit card had 468 orders, 47.3% of the month.

    Hover over a data point to see the share for that month. Click an item name to hide or show its data.

    ![Monthly share trend by payment method](../../assets/images/ec-bi-order-payment-ratio-trend.zh-tw.en.png){ title="Monthly Share Trend by Payment Method" }

=== "Share (Period)"

    Order share of each payment method in the time range. For example, credit card had 3427 orders, 47%.

    Hover over a slice to see the share of that payment method. Click an item name to hide or show its data.

    ![Share by payment method](../../assets/images/ec-bi-order-payment-ratio.zh-tw.en.png){ title="Share by Payment Method" }

=== "Average Order Value (Monthly Trend)"

    Average order value of each payment method per month (total order amount for the payment method ÷ orders for the payment method).

    Hover over a data point to see the average order value for that month. Click an item name to hide or show its data.

    ![Monthly average order value trend by payment method](../../assets/images/ec-bi-order-payment-aov-trend.zh-tw.en.png){ title="Monthly Average Order Value Trend by Payment Method" }

=== "Average Order Value (Period)"

    Average order value of each payment method in the time range.

    Hover over a bar to see the average order value of that payment method.

    ![Average order value by payment method](../../assets/images/ec-bi-order-payment-aov.zh-tw.en.png){ title="Average Order Value by Payment Method" }

=== "Return Rate (Monthly Trend)"

    Return rate of each payment method per month (returned orders for the payment method ÷ non-canceled orders for the payment method).

    ![Monthly return rate trend by payment method](../../assets/images/ec-bi-order-payment-return-trend.zh-tw.en.png){ title="Monthly Return Rate Trend by Payment Method" }

=== "Return Rate (Period)"

    Return rate of each payment method in the time range.

    ![Return rate by payment method](../../assets/images/ec-bi-order-payment-return.zh-tw.en.png){ title="Return Rate by Payment Method" }

### Shipping Method { #overview-order-analysis-shipping }

=== "Orders (Monthly Trend)"

    Orders per shipping method per month. For example, in May 2020, Black Cat had 751 orders.

    Hover over a data point to see the order count for that month. Click an item name to hide or show its data.

    ![Monthly order trend by shipping method](../../assets/images/ec-bi-order-shipping-count-trend.zh-tw.en.png){ title="Monthly Order Trend by Shipping Method" }

=== "Share (Monthly Trend)"

    The ratio of each shipping method's recognized orders to all recognized orders in the month. For example, in May 2020, Black Cat accounted for 62.6%.

    Hover over a data point to see the share for that month. Click an item name to hide or show its data.

    ![Monthly share trend by shipping method](../../assets/images/ec-bi-order-shipping-ratio-trend.zh-tw.en.png){ title="Monthly Share Trend by Shipping Method" }

=== "Share (Period)"

    Recognized order ratio of each shipping method in the time range. For example, Black Cat had 4845 orders, 62%.

    Hover over a slice to see the share of that shipping method. Click an item name to hide or show its data.

    ![Share by shipping method](../../assets/images/ec-bi-order-shipping-ratio.zh-tw.en.png){ title="Share by Shipping Method" }

=== "Average Order Value (Monthly Trend)"

    Average order value of each shipping method per month (based on the shipping method's recognized orders). For example, Black Cat: NT$3575.96.

    Hover over a data point to see the average order value for that month. Click an item name to hide or show its data.

    ![Monthly average order value trend by shipping method](../../assets/images/ec-bi-order-shipping-aov-trend.zh-tw.en.png){ title="Monthly Average Order Value Trend by Shipping Method" }

=== "Average Order Value (Period)"

    Average order value of each shipping method in the time range. For example, Black Cat: NT$3799.98.

    Hover over a bar to see the average order value of that shipping method.

    ![Average order value by shipping method](../../assets/images/ec-bi-order-shipping-aov.zh-tw.en.png){ title="Average Order Value by Shipping Method" }

=== "Return Rate (Monthly Trend)"

    Return rate of each shipping method per month (returned orders for the shipping method ÷ non-canceled orders for the shipping method).

    Hover over a data point to see the return rate for that month. Click an item name to hide or show its data.

    ![Monthly return rate trend by shipping method](../../assets/images/ec-bi-order-shipping-return-trend.zh-tw.en.png){ title="Monthly Return Rate Trend by Shipping Method" }

=== "Return Rate (Period)"

    Return rate of each shipping method in the time range.

    Hover over a bar to see the return rate of that shipping method.

    ![Return rate by shipping method](../../assets/images/ec-bi-order-shipping-return.zh-tw.en.png){ title="Return Rate by Shipping Method" }

---

### Third-Party Referral { #overview-order-analysis-third-party }

!!! plan "Display Conditions"
    These charts appear only if a referral platform is connected, and they show each source based on the platforms actually connected. See [Display Conditions for Third-Party Referral Charts](#prerequisites-order-analysis-third-party){ title="Display Conditions for Third-Party Referral Charts" data-preview }.

=== "Orders (Monthly Trend)"

    Orders per order source per month. For example, in April 2020, LINE Shopping had 90 orders.

    Hover over a data point to see the order count for that month. Click an item name to hide or show its data.

    ![Monthly order trend by third-party referral](../../assets/images/ec-bi-order-referral-count-trend.zh-tw.en.png){ title="Monthly Order Trend by Third-Party Referral" }

=== "Share (Period)"

    The ratio of each source's recognized orders to all recognized orders in the time range.

    Hover over a slice to see the share of that source. Click an item name to hide or show its data.

    ![Share by third-party referral](../../assets/images/ec-bi-order-referral-ratio.zh-tw.en.png){ title="Share by Third-Party Referral" }

=== "Average Order Value (Monthly Trend)"

    Average order value of each source per month (total recognized order amount for the source ÷ recognized orders for the source). For example, in May 2020, LINE Shopping: NT$3312.93.

    Hover over a data point to see the average order value for that month. Click an item name to hide or show its data.

    ![Monthly average order value trend by third-party referral](../../assets/images/ec-bi-order-referral-aov-trend.zh-tw.en.png){ title="Monthly Average Order Value Trend by Third-Party Referral" }

=== "Average Order Value (Period)"

    Average order value of each source in the time range. For example, LINE Shopping: NT$3222.52.

    Hover over a bar to see the average order value of that source.

    ![Average order value by third-party referral](../../assets/images/ec-bi-order-referral-aov.zh-tw.en.png){ title="Average Order Value by Third-Party Referral" }

=== "Return Rate (Monthly Trend)"

    Return rate of each source per month (returned orders for the source ÷ non-canceled orders for the source).

    Hover over a data point to see the return rate for that month. Click an item name to hide or show its data.

    ![Monthly return rate trend by third-party referral](../../assets/images/ec-bi-order-referral-return-trend.zh-tw.en.png){ title="Monthly Return Rate Trend by Third-Party Referral" }

=== "Return Rate (Period)"

    Return rate of each source in the time range.

    Hover over a bar to see the return rate of that source.

    ![Return rate by third-party referral](../../assets/images/ec-bi-order-referral-return.zh-tw.en.png){ title="Return Rate by Third-Party Referral" }

---

## Important Rules and Limitations { #specs-order-analysis }

* **Only recognized orders are counted**: All data is based on [recognized orders](#prerequisites-order-analysis-recognized-order){ title="Recognized Order Definition" data-preview }. Canceled orders and orders with a completed return are excluded.
* **Data is updated on a schedule, not in real time**: Report data is calculated in scheduled batches, not in real time. The system periodically excludes canceled and returned orders and recalculates, so figures may differ slightly from the real-time "All Orders" list.
* **Return rate is calculated after excluding cancellations**: When calculating the return rate, canceled orders are excluded first, and recognized orders are then used as the base.
* **Charts are independent**: Each chart's date range is set separately. When reviewing data, check whether the periods currently applied to the charts are the same.

---

## FAQ { #faq-order-analysis }

??? quote "Why don't the Order Analysis figures match the "All Orders" list?"
    [](){ #faq-order-analysis-data-mismatch }
    There are two main reasons:

    * Order Analysis counts only [recognized orders](#prerequisites-order-analysis-recognized-order){ title="Recognized Order Definition" data-preview }. Canceled orders and orders with a completed return aren't counted.
    * Report data is updated in scheduled batches, not in real time, so it lags slightly behind the "All Orders" list.

<!-- ??? quote "Why can't I see the "Order Payment and Shipping Analysis" or "Order Reports" tab?" -->
<!--     [](){ #faq-order-analysis-missing-tabs } -->
<!--     This is due to plan differences. The Pro, Pro PLUS, Professional PLUS, and Advanced PLUS plans show only "Order Overview Analysis." -->

??? quote "What does the "change value" on the cards mean?"
    [](){ #faq-order-analysis-variation }
    The "change value" compares two values: the **past 30 days** and the **long-term average**. A positive value means recent performance is above the long-term average (growth), and a negative value means it's below (decline). Use it to quickly judge recent growth.

??? quote "Why can't I see the "Third-Party Referral" charts?"
    [](){ #faq-order-analysis-no-third-party }
    Third-party referral charts appear only if your store is connected to a referral platform. Check whether "Market America Partner Store" or "LINE Shopping" is set up. See [Display Conditions for Third-Party Referral Charts](#prerequisites-order-analysis-third-party){ title="Display Conditions for Third-Party Referral Charts" }.

??? quote "Can I export Order Analysis data?"
    [](){ #faq-order-analysis-export }
    Yes, but only for the three tables on the "Order Reports" tab. Click "Download as Excel" in the upper-right corner of a table. Chart sections (Order Overview Analysis, Order Payment and Shipping Analysis) can't be downloaded.

---

## References { #reference-order-analysis }

* [Order Overview Analysis Metrics Reference](references/order-analysis-overview-metrics-reference.md)
* [Order Payment and Shipping Analysis Chart Reference](references/order-analysis-finance-logistics-reference.md)
* [Order Report Field Reference](references/order-analysis-report-fields-reference.md)
