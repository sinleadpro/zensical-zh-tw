---
title: "OMO Analysis Report"
description: "Combine business data from your online store (EC) and physical stores (POS), and compare revenue, orders, members, products, and marketing performance across both channels on one page."
created: 2026-06-23 10:00
last_modified: 2026-07-12 20:16
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 分析報表
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 查看 OMO 全通路經營數據
  - 比較 EC 與 POS 的營收與銷售表現
  - 分析線上官網與實體門市的會員與商品數據
features:
  - OMO 分析報表
  - 全通路數據總覽
  - 營收分析
  - 訂單分析
  - 會員分析
  - 商品分析
  - 行銷活動分析
prerequisites:
  - 已開通 CYBERBIZ POS
related:
  - ec/business-intelligence/references/omo-definitions-reference/
  - ec/business-intelligence/revenue-analysis/
  - ec/business-intelligence/member-analysis/
  - ec/business-intelligence/customer-analysis/
tags:
  - OMO
  - Omnichannel
  - "Cross-Channel Analysis"
  - POS
  - "Online Store"
  - "Physical Stores"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分析報表 > OMO分析報表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7800
  - https://www.cyberbiz.io/support/?p=33261
permalink: "https://help.cyberbiz.io/ec/business-intelligence/omo-analysis-report/"
comments: false
search:
  exclude: false
icon: lucide/line-chart
hide:
---

![OMO Analysis Report page](../../assets/images/ec-bi-omo-analysis-report-hero.en.png){ title="OMO Analysis Report Page" .hero-page }

## About the OMO Analysis Report { #intro-omo }

The "OMO Analysis Report" brings data from your online store (EC) and physical stores (POS) together on one page. You no longer need to check two separate systems; you can directly compare revenue, orders, members, products, and marketing performance across both channels and understand your overall omnichannel operations.

The report has six tabs by topic: "Overview," "Revenue," "Orders," "Members," "Products," and "Marketing Campaigns." On each tab, you can filter by time range, comparison period, and POS store, and compare against the same period in the past to judge growth trends and marketing results.

## Prerequisites and Limitations { #prerequisites-omo }

### Activation Requirements { #prerequisites-omo-plan }

!!! plan "Plan / Activation Requirements"
    The "OMO Analysis Report" requires your store to have activated and be using **CYBERBIZ POS**. Only then does the report appear in the admin menu, open, and show physical store data. Stores without POS enabled won't see this report.

---

### Data Basis { #prerequisites-omo-basis }

- **Valid orders**: All figures in the report count only valid orders. Canceled and returned orders are excluded. See [Valid Order Definition](references/omo-definitions-reference.md#reference-omo-valid-order){ title="OMO Analysis Report Shared Definitions" data-preview }.
- **Update time**: Data is updated in a batch the next day, so orders placed and members registered today don't appear right away. See [Data Update Time](references/omo-definitions-reference.md#reference-omo-update-time){ title="OMO Analysis Report Shared Definitions" data-preview }.

## Page Overview { #overview-omo }

The report has six tabs. Use the table below to quickly see what each tab covers, then read the details of each tab as needed. For how each metric is calculated and what terms mean, see the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" data-preview }.


| Tab | What It Shows |
| :-- | :-- |
| [Overview](#overview-omo-summary) | EC/POS comparison and change in revenue, order count, and registered members; average order value; and EC/POS product sales TOP10 |
| [Revenue](#overview-omo-revenue) | EC/POS revenue and trend chart, and EC/POS revenue heatmap |
| [Orders](#overview-omo-order) | EC/POS order count and average order value trends, and order count and amount for store pickup / POS store pickup |
| [Members](#overview-omo-member) | EC/POS registered members, POS quick sign-in member registration completion rate, comparison of average member spend, and purchasing and repurchasing status |
| [Products](#overview-omo-product) | EC/POS product sales volume and sales amount TOP10, and a sales list of products with the same SKU |
| [Marketing Campaigns](#overview-omo-marketing) | EC/POS bonus usage and trend chart |


### Overview { #overview-omo-summary }

A quick look at core omnichannel metrics, ideal for checking the overall situation first thing each day:

- **Core metric cards**: Revenue, order count, and registered members, each showing EC and POS values and the change compared with the comparison period.

    === "Revenue"
        ![Revenue metric card](../../assets/images/ec-bi-omo-revenue-card.en.png){ title="Revenue Metric Card" }

    === "Order Count"
        ![Order count metric card](../../assets/images/ec-bi-omo-order-count-card.en.png){ title="Order Count Metric Card" }

    === "Registered Members"
        ![Registered members metric card](../../assets/images/ec-bi-omo-member-count-card.en.png){ title="Registered Members Metric Card" }

    !!! tip "Hover over a slice to see the data details for that section. Click an item name to hide or show its data."

- **Average order value**: Shows EC and POS average order value as "total revenue ÷ total orders." See the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" data-preview }.

    ![Average order value](../../assets/images/ec-bi-omo-aov-card.en.png){ title="Average Order Value" }

    !!! tip "Hover over a bar to see its value details. Click an item name to hide or show its data."

- **Product sales TOP10**: Lists the top 10 products by sales volume for EC and POS separately.

    ![Product sales TOP10](../../assets/images/ec-bi-omo-top10-products.en.png){ title="Product Sales TOP10" }

---

### Revenue { #overview-omo-revenue }

Focuses on online and offline revenue performance and its distribution over time:

- **EC/POS revenue and trend chart**: See how revenue in both channels changes over time.

    === "Revenue Metrics"

        Hover over a slice to see the data details for that section. Click an item name to hide or show its data.

        ![Revenue metrics](../../assets/images/ec-bi-omo-ec-revenue-trend.en.png){ title="Revenue Metrics" }

    === "Revenue Trend Chart"

        Hover over any point on the line to see the value for that date. Click an item name to hide or show its data.

        ![Revenue trend chart](../../assets/images/ec-bi-omo-pos-revenue-trend.en.png){ title="Revenue Trend Chart" }

- **EC/POS revenue heatmap**: Uses color intensity to show revenue by time slot. The darker the color, the higher the revenue in that time slot. Use it as a reference when scheduling marketing campaigns or livestreams. See the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" data-preview }.

    Hover over a time block to see the revenue for that time slot.

    ![Revenue heatmap](../../assets/images/ec-bi-omo-revenue-heatmap.en.png){ title="Revenue Heatmap" }

---

### Orders { #overview-omo-order }

Analyzes order volume, average order value, and how well store pickup drives sales:

- **EC/POS order count and average order value trends**: See how order volume and average order value change in both channels.

    === "Order Count"

        Hover over a slice or any point on the line to see detailed values. Click an item name to hide or show its data.

        ![Order count metric card](../../assets/images/ec-bi-omo-order-detail-card.en.png){ title="Order Count Metric Card" }
        ![Order count trend chart](../../assets/images/ec-bi-omo-order-count-trend.en.png){ title="Order Count Trend Chart" }

    === "Average Order Value"

        Hover over a bar or any point on the line to see detailed values. Click an item name to hide or show its data.

        ![Average order value metric card](../../assets/images/ec-bi-omo-aov-detail-card.en.png){ title="Average Order Value Metric Card" }

        ![Average order value trend chart](../../assets/images/ec-bi-omo-aov-trend.en.png){ title="Average Order Value Trend Chart" }

- **Store pickup / POS store pickup analysis**: Counts the orders and order amounts for store pickup and POS store pickup, so you can see how well online and offline channels drive conversions to each other. See the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" data-preview }.

    ![Store pickup / POS store pickup](../../assets/images/ec-bi-omo-store-pickup.en.png){ title="Store Pickup / POS Store Pickup" }

    !!! tip "Hover over a bar to see its value details. Click an item name to hide or show its data."

---

### Members { #overview-omo-member }

Understand which channel members come from, how complete their registrations are, and how they spend across channels:

- **Registered members and registration completion rate**: EC and POS registered members, and the POS quick sign-in member registration completion rate. See the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" data-preview }.

    === "Member Count"

        Hover over a slice or any point on the line to see detailed values. Click an item name to hide or show its data.

        ![Member count metric card](../../assets/images/ec-bi-omo-member-detail-card.en.png){ title="Member Count Metric Card" }

        ![Member count trend chart](../../assets/images/ec-bi-omo-member-registration-trend.en.png){ title="Member Count Trend Chart" }

    === "Registration Completion Rate"
        ![Registration completion rate](../../assets/images/ec-bi-omo-completion-rate.en.png){ title="Registration Completion Rate" }

- **Average member spend comparison**: Compares the average spend in each channel of members who registered via EC and via POS, so you can tell which source brings higher-value customers.

    === "All Members"

        Hover over a bar to see its value details. Click an item name to hide or show its data.

        ![Average spend bar chart](../../assets/images/ec-bi-omo-aov-bar-chart-all.en.png){ title="Average Member Spend by Registration Source" }

        ![Average spend of all members](../../assets/images/ec-bi-omo-aov-card-all.en.png){ title="Average Spend of All Members" }

    === "EC Average Spend"

        Hover over a bar to see its value details. Click an item name to hide or show its data.

        ![EC average spend bar chart](../../assets/images/ec-bi-omo-aov-bar-chart-ec.en.png){ title="EC Average Member Spend by Registration Source" }

        ![EC average spend](../../assets/images/ec-bi-omo-aov-card-ec.en.png){ title="EC Average Spend" }

    === "POS Average Spend"

        Hover over a bar to see its value details. Click an item name to hide or show its data.

        ![POS average spend bar chart](../../assets/images/ec-bi-omo-aov-bar-chart-pos.en.png){ title="POS Average Member Spend by Registration Source" }

        ![POS average spend](../../assets/images/ec-bi-omo-aov-card-pos.en.png){ title="POS Average Spend" }

- **Member purchasing and repurchasing status**: Grouped by members' first registration source, shows their purchasing and repurchasing performance in EC and POS, along with the overall repurchase rate. See the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" data-preview }.

    === "Purchasing Status"

        Hover over a slice to see the data details for that section. Click an item name to hide or show its data.

        ![Purchasing status](../../assets/images/ec-bi-omo-purchase-status.en.png){ title="Purchasing Status" }

    === "Repurchasing Status"

        Hover over a slice to see the data details for that section. Click an item name to hide or show its data.

        ![Repurchasing status](../../assets/images/ec-bi-omo-repurchase-status.en.png){ title="Repurchasing Status" }

---

### Products { #overview-omo-product }

See best-selling products across all channels and cross-channel sales of the same item:

- **Product sales TOP10**: The top 10 products by quantity sold for EC and POS separately.

    ![Product sales TOP10](../../assets/images/ec-bi-omo-top10-sales-detail.en.png){ title="Product Sales TOP10" }

- **Product sales amount TOP10**: The top 10 products by sales amount for EC and POS separately.

    ![Product sales amount TOP10](../../assets/images/ec-bi-omo-top10-revenue.en.png){ title="Product Sales Amount TOP10" }

- **Product sales list**: Matches the same product in EC and POS by SKU to show order count and sales amount, sorted by total sales amount.

    ![Product sales list](../../assets/images/ec-bi-omo-product-list.en.png){ title="Product Sales List" }

!!! warning "SKU Consistency"
    Products are combined in the statistics only if they have the same SKU. The product sales list on the "Products" tab matches EC and POS sales by SKU. If the same product has different SKUs in the two channels, it can't be combined into one row.

---

### Marketing Campaigns { #overview-omo-marketing }

Monitor how bonus points are used online and offline:

- **Bonus usage and trend chart**: Bonus points redemption and usage in EC and POS during the specified period.

=== "Usage Metrics"

    Hover over a slice to see the data details for that section. Click an item name to hide or show its data.

    ![Bonus usage metrics](../../assets/images/ec-bi-omo-bonus-usage-card.en.png){ title="Bonus Usage Metrics" }

=== "Trend Chart"

    Hover over any point on the line to see the value for that date. Click an item name to hide or show its data.

    ![Bonus usage trend chart](../../assets/images/ec-bi-omo-bonus-usage-trend.en.png){ title="Bonus Usage Trend Chart" }

## Steps { #operate-omo }

After you open the report, first set the period and stores to analyze at the top of the page, then switch tabs to view data on different topics.

### Set the Analysis Period { #operate-omo-period }

1. **Open the report:** In the admin, go to "Charts" > "OMO Analysis Report."
2. **Choose a time range:** In "Time Range" at the top of the page, select the start and end dates to analyze.

    ![Choose a time range](../../assets/images/ec-bi-omo-step-time-range.en.png){ title="Choose a Time Range" }

3. **Choose a comparison period:** In "Comparison Time Range," choose the basis for comparison: "Previous year," "Previous period," "Previous month," or "Customize period"[^1]. For what each option means, see the [Comparison Period Options Reference](references/omo-definitions-reference.md#reference-omo-compare){ title="OMO Analysis Report Shared Definitions" data-preview }.

    ![Choose a comparison period](../../assets/images/ec-bi-omo-step-compare-range.en.png){ title="Choose a Comparison Period" }

4. **Filter POS stores:** In the "Select or search POS stores" field, choose the stores to include. You can select several at once. If you don't select any, "All POS stores" is included by default.

    ![Filter POS stores](../../assets/images/ec-bi-omo-step-filter-store.en.png){ title="Filter POS Stores" }
5. **Apply the filters:** Click **Confirm** to apply the selected time range, comparison period, and store conditions to all charts on the page at once.

[^1]: By default, the report's time range is "the past month through today," and the comparison period is the same period in the "Previous year."

---

### Switch Report Tabs { #operate-omo-tabs }

1. **Switch tabs:** Click "Overview," "Revenue," "Orders," "Members," "Products," or "Marketing Campaigns" at the top of the page to switch to that analysis.
2. **Filters carry over:** When you switch tabs, the time range, comparison period, and POS store filters you set still apply, so you don't need to set them again.

![Switch report tabs](../../assets/images/ec-bi-omo-step-switch-tab.en.png){ title="Switch Report Tabs" }

!!! tip "Tip"
    The report has an **"Export Chart"** feature that exports chart data so you can save it or analyze it further.

## Important Rules and Limitations { #specs-omo }

- **Only valid orders are counted:** No figures in the report include canceled or returned orders, so they may not match the total amount in the order list.
- **Data is updated the next day:** Traffic and conversion rate data are updated at 5:30 PM the next day, and other data at midnight the next day. Canceled and returned orders are excluded in scheduled updates.
- **Requires CYBERBIZ POS:** Stores without POS enabled can't see this report, and physical store data can't be shown.
- **Products must have the same SKU to be combined:** The product sales list on the "Products" tab matches EC and POS sales by SKU. If the same product has different SKUs in the two channels, it can't be combined into one row.

## Next Steps { #next-steps-omo }

<div class="grid cards" markdown>

- :lucide-dollar-sign:{ .lg }  
  [__Revenue__](revenue-analysis.md){ title="Revenue Analysis" }  
  Look more closely at your online store's revenue makeup and growth trends.

- :lucide-users:{ .lg }  
  [__Member Analysis__](member-analysis.md){ title="Member Analysis" }  
  Track member base size, growth, and repurchase trends.

- :lucide-repeat:{ .lg }  
  [__Purchased Member Analysis__](customer-analysis.md){ title="Purchased Member Analysis" }  
  Split new and returning customers to see order contribution and repurchase performance in depth.

- :lucide-file-text:{ .lg }  
  [__Make the OMO Analysis Report Your Planning Assistant__](https://drive.google.com/file/d/1rZ8ZXbhTkOYl4mX250o-2cdfMoeQSmnJ/view)  
  A PDF guide to learn how to use OMO data to plan your operating strategy.

</div>

## FAQ { #faq-omo }

??? quote "Data doesn't match / today's orders haven't appeared yet"
    [](){ #faq-omo-data-delay }
    The report is updated in a batch the next day, not in real time.

    - Traffic and conversion rate data are updated at 5:30 PM the next day, and other data at midnight the next day.
    - Canceled and returned orders are excluded in scheduled updates, so figures may differ from the total amount in the order list. See [Valid Order Definition](references/omo-definitions-reference.md#reference-omo-valid-order){ title="OMO Analysis Report Shared Definitions" data-preview }.

??? quote "The same product isn't combined across EC and POS"
    [](){ #faq-omo-sku-merge }
    The "Products" tab matches sales in the two channels by SKU, and they are combined only if the SKUs match.

    - If the same product has different SKUs in EC and POS, it is treated as two different products and listed separately.
    - Set the same SKU for the same product in both channels so the data can be combined.

??? quote "How is the "repurchase rate" calculated?"
    [](){ #faq-omo-repurchase }
    The repurchase rate is the percentage of purchasing customers in the specified period who are returning customers.

    - It is calculated as "returning customers in the period ÷ total purchasing customers in the period."
    - For detailed term descriptions, see the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" }.

??? quote "What does "POS quick sign-in member registration completion rate" mean?"
    [](){ #faq-omo-fast-registration }
    It is the share of members who quick-registered at POS and then completed their profile and the registration process.

    - If your store allows customers to register and check out without account verification, they are treated as having completed registration.
    - See the [Glossary of Terms](references/omo-definitions-reference.md#reference-omo-glossary){ title="OMO Analysis Report Shared Definitions" }.

## References { #reference-omo }

- [OMO Analysis Report Shared Definitions](references/omo-definitions-reference.md)
