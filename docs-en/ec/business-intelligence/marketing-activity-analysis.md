---
title: "Marketing Campaign Analysis"
description: "See the performance of discounts, coupons, and bonus points in one place, and learn which marketing activities actually drive orders and revenue."
created: 2026-06-16 00:00
last_modified: 2026-07-12 19:37
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
difficulty: intermediate
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
  - 查看行銷活動成效
  - 分析折扣活動與優惠券表現
  - 比較各折扣種類的貢獻
  - 檢視紅利使用情形
features:
  - 折扣活動分析
  - 優惠券分析
  - 紅利分析
  - 折扣活動排名
  - 優惠券種類分析
prerequisites:
  - 方案已包含行銷活動分析功能
related:
  - ec/business-intelligence/references/marketing-activity-coupon-metrics-reference/
  - ec/marketing/
  - ec/marketing/coupon/setup-coupons/
  - ec/marketing/bonus-and-gifts/setup-bonus-points/
  - ec/business-intelligence/references/marketing-activity-discount-categories-reference/
tags:
  - "Marketing Campaign Analysis"
  - "Discount Activities"
  - coupon
  - "Bonus Points"
  - "Business Analysis"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 日期選擇器
  - 下拉選單
  - 頁籤
  - 數字卡
  - 圓餅圖
  - 長條圖
  - 排名表格
  - 分頁切換
paths:
  - 經營分析 > 行銷活動分析
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5056
  - https://www.cyberbiz.io/helpcenter/?p=8101
permalink: "https://help.cyberbiz.io/ec/business-intelligence/marketing-activity-analysis/"
comments: false
search:
  exclude: false
icon: lucide/tag
hide: []
---

![Marketing Campaign Analysis page](../../assets/images/ec-bi-marketing-activity-analysis-hero.en.png){ title="Marketing Campaign Analysis Page" .hero-page }

## About Marketing Campaign Analysis { #intro-marketing-activity }

This page is under "**Marketing Campaign Analysis**" in the left menu of the admin. It brings together three analysis tabs to help you answer questions like "Did this campaign actually work?":

- **Shop Campaign Analysis**: See an overview of discounted orders across the store, the contribution of each discount type, and a performance ranking of individual discount campaigns.
- **Coupon Analysis**: See usage, revenue, and usage cycles for each coupon type and for individual coupons.
- **Bonus Analysis**: See how bonus points are used across the store, and export bonus reports.

!!! info "Tip"
    All data on this page is calculated based on "**valid orders**." For the definition of valid orders, see [Important Rules and Limitations](#specs-marketing-activity-valid-order){ title="Important Rules and Limitations" }.

## Page Overview { #overview-marketing-activity }

When you open the page, there are three tabs at the top. Each tab contains the following:

| Tab | What It Mainly Shows | Sections |
| :-- | :-- | :-- |
| **Shop Campaign Analysis** | Performance of discounted orders across the store | Discounted order overview, discount type analysis, discount campaign ranking |
| **Coupon Analysis** | Coupon usage and revenue | Coupon type analysis, specific coupon analysis |
| **Bonus Analysis** | Store-wide bonus points usage | Bonus analysis charts, export bonus report |

!!! note "Note"
    The three tabs are independent. Each has its own date range and filters, and switching tabs doesn't affect the others.

## Prerequisites and Limitations { #prerequisites-marketing-activity }

[](){ #prerequisites-marketing-activity-plan }

- [x] **Requires plan support**: "Marketing Campaign Analysis" is an advanced report and isn't available on some entry-level plans. If you can't find "Marketing Campaign Analysis" in the left menu, your current plan doesn't include this feature[^plan].
- [x] **Bonus chart export activation `Enterprise`**: The **"Export Bonus Chart"** button in the upper-right corner of the "Bonus Analysis" tab appears only if your plan includes "Bonus Report Export." If the button isn't shown, you can still view the bonus analysis charts as usual, but you can't export reports.

[^plan]: This feature isn't available on the Professional or Advanced plans. It appears only on the Pro plan and above.

## Steps { #operate-marketing-activity }

### Shop Campaign Analysis { #operate-marketing-activity-discount }

When you open the page, it shows the "**Shop Campaign Analysis**" tab by default, which is divided into three sections from top to bottom.

#### View the Discounted Order Overview { #overview-marketing-discount }

1. **Choose a date range:** Use the date picker above the "**Overview**" section to choose the period to analyze.

    ![Choose a date range](../../assets/images/ec-bi-mkt-act-date-range.en.png){ title="Choose a Date Range" }

2. **View four key figures:** The system shows four figure cards: **Discounted Orders**, **Revenue of Discounted Orders**, **Total Orders**, and **Total Order Amount**.

    ![View four key figures](../../assets/images/ec-bi-mkt-act-key-metrics.en.png){ title="View Four Key Figures" }

3. **View the share charts:** The two pie charts below show the **discounted order count share** and the **discounted order amount share**, so you can see at a glance how much discounted orders account for overall.

    ![View the share charts](../../assets/images/ec-bi-mkt-act-pie-chart.en.png){ title="View the Share Charts" }

    !!! tip "Hover over a slice to see that item's share. Click an item name to hide or show its data."

??? info "Discounted Order Overview Metric Definitions"

    | Metric | Description |
    | :--- | :--- |
    | Discounted Orders | Total number of "valid orders" that used a discount |
    | Revenue of Discounted Orders | Total amount of "valid orders" that used a discount |
    | Total Orders | Total number of "valid orders" |
    | Total Order Amount | Total order amount of "valid orders" |
    | Discounted Order Count Share | Number of valid orders with a discount applied ÷ total orders (regular orders: no discount applied ÷ total orders) |
    | Discounted Order Amount Share | Amount of valid orders with a discount applied ÷ total order amount (regular orders: no discount applied ÷ total order amount) |

---

#### Analyze the Contribution of Each Discount Type { #reference-discount-category-contribution }

1. **Set conditions:** In the "**Discount Type Analysis**" section, choose a date range, and in the **Please Select Discount Type** drop-down, select the discount types to compare (multiple selections allowed; all discount types by default).

    ![Set conditions](../../assets/images/ec-bi-mkt-act-discount-condition.en.png){ title="Set Conditions" }

2. **Switch metrics:** Use the **"Orders"** and **"Order Amount"** tabs in the section to choose whether the bar chart shows order count or order amount.

    ![Switch metrics](../../assets/images/ec-bi-mkt-act-switch-metric.en.png){ title="Switch Metrics" }

3. **Read the bar chart:** The bar chart lists how each discount type performed in the selected period, helping you find the most popular discount types.

    ![Read the bar chart](../../assets/images/ec-bi-mkt-act-bar-chart.en.png){ title="Read the Bar Chart" }

??? info "Discount Analysis Metric Definitions"

    | Metric | Description |
    | :--- | :--- |
    | Orders | Number of valid orders in the selected period that the "discount type" was applied to (the admin currently offers only 5 discount types) |
    | Order Count Share | Number of valid orders in the selected period that the "discount type" was applied to ÷ discounted orders |
    | Order Amount | Amount of valid orders in the selected period that the "discount type" was applied to |
    | Order Amount Share | Amount of valid orders in the selected period that the "discount type" was applied to ÷ revenue of discounted orders |

??? warning "Discount Type Shares May Add Up to More Than 100%"
    Because one order can have multiple discount types applied, the order count or order amount shares of all discount types may add up to more than 100%. For a full example, see the [FAQ](#faq-marketing-activity-over-100).

---

#### View and Download the Discount Campaign Ranking { #reference-discount-ranking }

1. **Set conditions:** In the "**Discount Campaign Ranking**" section, choose a date range and discount type.

    ![Set ranking conditions](../../assets/images/ec-bi-mkt-act-ranking-condition.en.png){ title="Set Ranking Conditions" }

2. **View the ranking table:** The table lists each discount campaign by rank with its **Discount Campaign**, **Discount Type**, **Total Order Amount**, **Total Orders**, and **Average Order Value**.

    ![View the ranking table](../../assets/images/ec-bi-mkt-act-ranking-table.en.png){ title="View the Ranking Table" }

3. **Change the sort order:** Click the **Total Order Amount**, **Total Orders**, or **Average Order Value** column header to sort by that column.

    ![Change the sort order](../../assets/images/ec-bi-mkt-act-adjust-sort.en.png){ title="Change the Sort Order" }

4. **Download the report:** Click the **Download** icon in the upper-right corner of the section to export the current discount campaign ranking file.

    ![Download the report](../../assets/images/ec-bi-mkt-act-download-report.en.png){ title="Download the Report" }

5. **Page through results:** When there's a lot of data, use the pagination below the table to view the remaining ranks.

    ![Page through results](../../assets/images/ec-bi-mkt-act-pagination.en.png){ title="Page Through Results" }

??? info "Discount Campaign Ranking Metric Definitions"

    | Metric | Description |
    | :--- | :--- |
    | Total Order Amount | Total amount of valid orders in the specified period that had a discount from this campaign applied (valid orders: orders whose status is neither canceled nor returned) |
    | Total Orders | Number of valid orders in the specified period that had a discount from this campaign applied |
    | Average Order Value | Average order value in the specified period for orders that had a discount from this campaign applied, that is, total order amount ÷ total orders |

!!! note "Note"
    The discount campaign ranking **doesn't include bonus discounts**. To see bonus-related performance, go to the "Bonus Analysis" tab.

---

### Coupon Analysis { #operate-marketing-activity-coupon }

Switch to the "**Coupon Analysis**" tab to analyze coupons from two angles: "type" and "individual coupon."

#### Analyze by Coupon Type { #reference-coupon-category }

1. **Choose a date range:** In the "**Coupon Type Analysis**" section, choose the period to analyze[^coupon-category-days].

    ![Choose a date range](../../assets/images/ec-bi-mkt-act-coupon-date-range.en.png){ title="Choose a Date Range" }

2. **Choose a coupon type:** In the **Please Select Coupon Type** drop-down, choose one coupon type.

    ![Choose a coupon type](../../assets/images/ec-bi-mkt-act-coupon-category.en.png){ title="Choose a Coupon Type" }

3. **Switch analysis charts:** Use the tabs above the chart to switch between **Usage Status Analysis** and **Coupon Revenue Analysis**.

    === "Usage Status Analysis"

        This tab shows trend charts of the **distributed quantity**[^coupon-distribution-count] and **used quantity**[^coupon-used-count] of coupons, and the figure cards show each metric.

        Hover over a data point to see the quantity for that day. Click an item name to hide or show its data.

        ![Usage status analysis](../../assets/images/ec-bi-mkt-act-coupon-usage.en.png){ title="Usage Status Analysis" }

    === "Coupon Revenue Analysis"

        Hover over a data point to see the revenue for that day. Click an item name to hide or show its data.

        ![Coupon revenue analysis](../../assets/images/ec-bi-mkt-act-coupon-revenue.en.png){ title="Coupon Revenue Analysis" }

4. **View the metric figure cards:** The section shows figure cards for that coupon type, such as average discount amount, discount amount, average discount ratio, usage count, and revenue. For the exact calculation of each metric, see the [Coupon Metric Definitions Reference](references/marketing-activity-coupon-metrics-reference.md#reference-marketing-activity-coupon-metrics-category){ data-preview }.

    ![View the metric figure cards](../../assets/images/ec-bi-mkt-act-coupon-metrics.en.png){ title="View the Metric Figure Cards" }

[^coupon-category-days]: The date range for coupon type analysis can't exceed 100 days.

---

#### Analyze a Specific Coupon { #reference-coupon-specific }

1. **Choose a date range:** In the "**Specific Coupon Analysis**" section, choose a period[^coupon-specific-days].

    ![Choose a date range](../../assets/images/ec-bi-mkt-act-specific-date-range.en.png){ title="Choose a Date Range" }

2. **Filter coupons:** First choose a type in **Please Select Coupon Type**, then in the **Coupon Name** field, search for and select the coupon to analyze.

    ![Filter coupons](../../assets/images/ec-bi-mkt-act-filter-coupon.en.png){ title="Filter Coupons" }

3. **Switch analysis charts:** Use the tabs to switch between **Usage Status Analysis**, **Usage Rate Analysis**, **Revenue Analysis**, and **AOV Analysis**.

    === "Usage Status Analysis"

        ![Usage status analysis](../../assets/images/ec-bi-mkt-act-specific-usage.en.png){ title="Usage Status Analysis" }

    === "Usage Rate Analysis"

        ![Usage rate analysis](../../assets/images/ec-bi-mkt-act-specific-usage-rate.en.png){ title="Usage Rate Analysis" }

    === "Revenue Analysis"

        ![Revenue analysis](../../assets/images/ec-bi-mkt-act-specific-revenue.en.png){ title="Revenue Analysis" }

    === "AOV Analysis"

        ![AOV analysis](../../assets/images/ec-bi-mkt-act-specific-aov.en.png){ title="AOV Analysis" }

    !!! tip "Hover over a data point to see the value for that day. Click an item name to hide or show its data."

4. **View the metric figure cards:** The section shows figure cards for that coupon, such as discount amount, average discount ratio, average order value, coupon order revenue, coupon usage count, usage rate, average usage cycle, target audience size, and target audience total revenue. For the exact calculation of each metric, see the [Coupon Metric Definitions Reference](references/marketing-activity-coupon-metrics-reference.md#reference-marketing-activity-coupon-metrics-specific){ data-preview }.

    ![View the metric figure cards](../../assets/images/ec-bi-mkt-act-specific-metrics.en.png){ title="View the Metric Figure Cards" }

[^coupon-specific-days]: The date range for specific coupon analysis can't exceed 180 days.

---

### Bonus Analysis { #operate-marketing-activity-bonus }

Switch to the "**Bonus Analysis**" tab to view how bonus points are used across the store, and export bonus reports when eligible.

!!! info "Tip"
    On this tab, "**bonus orders**" means **orders that redeemed bonus points** (orders that used bonus points at checkout), not "orders that earned bonus points."

#### View the Bonus Analysis Charts { #reference-bonus-chart }

1. **Switch to the tab:** Click the **Bonus Analysis** tab at the top, and the page loads analysis charts for store-wide bonus usage.
2. **View the bonus points overview at the top:** At the top of the tab are two figure cards, **Total Bonus Points Usage Rate** and **Total Bonus Points**, showing the overall status of bonus points members currently hold.

    ![View the bonus points overview at the top](../../assets/images/ec-bi-mkt-act-bonus-summary.en.png){ title="View the Bonus Points Overview at the Top" }

    !!! note "Note"
        The two figure cards (Total Bonus Points Usage Rate and Total Bonus Points) reflect **the real-time status of bonus points members currently hold**. They are a current snapshot and **aren't affected by the date range**. The other charts show order data for the selected date range.

3. **View each analysis chart:** Below the figure cards are the analysis charts in this order: **Bonus Revenue**, **Revenue Share**, **Bonus Orders**, **Order Count Share**, **AOV (Average Order Value)**, **Return Rate**, **Bonus Discount Amount**, and **Bonus Discount Ratio**. You can **choose a date range for each chart separately**.

    === "Bonus Revenue"

        ![Bonus revenue](../../assets/images/ec-bi-mkt-act-bonus-revenue.en.png){ title="Bonus Revenue" }

    === "Revenue Share"

        ![Revenue share](../../assets/images/ec-bi-mkt-act-bonus-revenue-ratio.en.png){ title="Revenue Share" }

    === "Bonus Orders"

        ![Bonus orders](../../assets/images/ec-bi-mkt-act-bonus-orders.en.png){ title="Bonus Orders" }

    === "Order Count Share"

        ![Order count share](../../assets/images/ec-bi-mkt-act-bonus-order-ratio.en.png){ title="Order Count Share" }

    === "AOV (Average Order Value)"

        ![AOV](../../assets/images/ec-bi-mkt-act-bonus-aov.en.png){ title="AOV" }

    === "Return Rate"

        ![Return rate](../../assets/images/ec-bi-mkt-act-bonus-return-rate.en.png){ title="Return Rate" }

    === "Bonus Discount Amount"

        ![Bonus discount amount](../../assets/images/ec-bi-mkt-act-bonus-discount-amount.en.png){ title="Bonus Discount Amount" }

    === "Bonus Discount Ratio"

        ![Bonus discount ratio](../../assets/images/ec-bi-mkt-act-bonus-discount-ratio.en.png){ title="Bonus Discount Ratio" }

    !!! tip "Hover over a chart to see its values. Click an item name to hide or show its data."

??? info "Bonus Analysis Metric Definitions"

    | Metric | Description |
    | :--- | :--- |
    | Total Bonus Points Usage Rate | Bonus points used by members ÷ bonus points issued × 100%. Only bonus points that haven't expired are counted |
    | Total Bonus Points | Sum of bonus points members currently hold that are **unused and unexpired** |
    | Bonus Revenue | Total revenue of valid orders split into "bonus orders / regular orders" (the trend chart is monthly; the share chart is the total for the selected period) |
    | Revenue Share | Share of total revenue from bonus orders and from regular orders |
    | Bonus Orders | Number of valid orders split into "bonus orders / regular orders" |
    | Order Count Share | Share of total orders from bonus orders and from regular orders |
    | AOV (Average Order Value) | Average amount per order, that is, total order amount ÷ number of orders, shown separately for "bonus orders / regular orders" |
    | Return Rate | Returned orders ÷ number of orders × 100%, shown separately for "bonus orders / regular orders" |
    | Bonus Discount Amount | Total bonus amount redeemed by all bonus orders in the selected period |
    | Bonus Discount Ratio | Bonus redemption amount ÷ (amount actually paid for the order + bonus redemption amount) × 100%, that is, the share of bonus redemption in the amount before redemption |

    !!! warning "Scope of the Return Rate Calculation"
        "Return Rate" is the only metric on this tab that **includes returned orders in the calculation** (otherwise the return rate would always be 0). All other metrics count only [valid orders](#specs-marketing-activity-valid-order){ title="Important Rules and Limitations" } (excluding returned and canceled orders).

---

#### Export Bonus Reports { #reference-bonus-export }

[:lucide-tag:{ title="Available Plans" }](../../../resources/conventions#適用方案) | Enterprise

1. **Click export:** Click the **Export Bonus Data** button[^bonus-export-plugin] in the upper-right corner of the tab to open the export window.

    ![Click export](../../assets/images/ec-bi-mkt-act-click-export.en.png){ title="Click Export" }

2. **Set the export period:** In **Start Date** and **End Date**, choose the period in which the bonus points were issued[^bonus-export-days].

    ![Set the export period](../../assets/images/ec-bi-mkt-act-export-range.en.png){ title="Set the Export Period" }

3. **Select report items:** Under "**Export List**," select **Total Bonus Report**.

    ![Select report items](../../assets/images/ec-bi-mkt-act-export-items.en.png){ title="Select Report Items" }

4. **Submit the export:** Click **Confirm**. The system generates the report in the background and sends it to your admin account email when it's done.

[^bonus-export-plugin]: This button appears only if your plan includes "Bonus Report Export."
[^bonus-export-days]: The export start and end times are based on when the bonus points were issued, and the period can't exceed 180 days.

## Important Rules and Limitations { #specs-marketing-activity }

[](){ #specs-marketing-activity-valid-order }

- **Valid order definition:** All data on the page is calculated from "valid orders." Valid orders are orders with "**Order Status: Non-canceled orders**" and "**a return status of No Return Needed or Return Rejected**." You can also check this definition at any time with the question mark icon next to the page title.
- **Discount type shares may exceed 100%:** In "Discount Type Analysis," a single order may have multiple discount campaigns applied at once, so the order count shares and amount shares of all discount types may add up to more than 100%. This is normal.
- **Data start time:** The system records marketing campaign data from a fixed start time. Orders before that start time aren't included in the statistics.
- **Date range limits:** Coupon type analysis allows up to 100 days, and specific coupon analysis and bonus report export allow up to 180 days. If you exceed the limit, the system prompts you to shorten the range.

## Next Steps { #next-steps-marketing-activity }

<div class="grid cards" markdown>

- :lucide-tag:{ .lg }  
  [__Marketing Campaign Settings__](../marketing/index.md){ title="Marketing Campaigns" }  
  Based on the analysis results, adjust or add marketing campaigns such as discounts and add-on purchases.

- :lucide-ticket:{ .lg }  
  [__Coupon Settings__](../marketing/coupon/setup-coupons.md){ title="Set Up Coupons" }  
  For coupon types that perform well, create new coupons to issue to customers.

- :lucide-gift:{ .lg }  
  [__Bonus Points Settings__](../marketing/bonus-and-gifts/setup-bonus-points.md){ title="Set Up Bonus Points" }  
  Adjust bonus reward and redemption rules based on how bonus points are used.

</div>

## FAQ { #faq-marketing-activity }

??? quote "Why do the shares in discount type analysis add up to more than 100%?"
    [](){ #faq-marketing-activity-over-100 }

    Because one order can have multiple discount types applied, the order count or order amount shares of all discount types may add up to more than 100%.

    For example, Store A placed 3 orders from 2023/12/01 to 2023/12/12. One order used a product add-on purchase, a coupon, and a spend-threshold gift discount; one order used a bonus discount; and one order had no offer applied.

    | Item | Value |
    | :--- | :--- |
    | Discounted Orders | 2 |
    | Total Orders | 3 |
    | Discounted Order Share | 2 ÷ 3 = 67% |
    | Product Add-On Purchase Orders | 1 (33%) |
    | Coupon Discount Orders | 1 (33%) |
    | Spend-Threshold Gift Orders | 1 (33%) |
    | Bonus Discount Orders | 1 (33%) |
    | Total of All Discount Type Shares | 33% × 4 = 132% |

    Because the same order can be counted under multiple discount types, it's normal for the shares to add up to more than 100%.

??? quote "Why can't I find bonus discounts in the discount campaign ranking?"
    [](){ #faq-marketing-activity-no-bonus-in-rank }
    The discount campaign ranking doesn't include bonus discounts. To see bonus-related performance, go to the [Bonus Analysis](#operate-marketing-activity-bonus){ title="Bonus Analysis" } tab.

??? quote "Some discount types don't appear in the drop-down. What should I do?"
    [](){ #faq-marketing-activity-missing-category }
    Some discount types appear only after you enable the corresponding marketing campaign feature.

    - For the activation requirements of each discount type, see the [Discount Type Reference](references/marketing-activity-discount-categories-reference.md){ data-preview }.

??? quote "What are "valid orders"? Why don't the figures match my actual order count?"
    [](){ #faq-marketing-activity-valid-order }
    All data on this page counts only "valid orders," defined as orders whose status isn't canceled and whose return status is No Return Needed or Return Rejected. Canceled or returned orders aren't counted, so the figures differ from the total in the order list.

[^coupon-distribution-count]: The number of coupons "available for use" on the online store that day. Each day, the system automatically counts the following sources: coupons issued today, and coupons issued before today that are still valid today.

[^coupon-used-count]: The number of coupons on the online store that day that are "within their validity period and recognized as used." When a customer successfully uses a coupon within the coupon validity period, it counts toward the used quantity (quantity 1) for each day from the day of use until the coupon expires. Once the coupon expires, it no longer counts toward the used quantity on later dates.

## References { #reference-marketing-activity }

- [Discount Type Reference](references/marketing-activity-discount-categories-reference.md)
- [Coupon Metric Definitions Reference](references/marketing-activity-coupon-metrics-reference.md)
