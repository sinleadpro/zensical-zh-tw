---
title: "Customer Analysis"
description: "Split new and returning customers by first order date, and compare customer counts, order contribution, and repurchase performance in depth."
created: 2026-06-16 00:00
last_modified: 2026-10-07 11:30
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
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 比較新舊客銷售貢獻
  - 查看顧客回購率
  - 分析業績成長來源
features:
  - 消費顧客分析
  - 新舊客分析
  - 回購分析
prerequisites:
  - 了解有效訂單定義
  - 了解新會員與新客的定義差異
related:
  - ec/business-intelligence/references/member-analysis-definitions-reference/
  - ec/business-intelligence/member-analysis/
  - ec/business-intelligence/member-overview/
tags:
  - "Customer Analysis"
  - "New and Returning Customer Analysis"
  - "Repurchase Analysis"
  - "Customer Analysis"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分析報表 > 會員分析
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8261
permalink: "https://help.cyberbiz.io/ec/business-intelligence/customer-analysis/"
comments: false
search:
  exclude: false
icon: lucide/user-search
hide: []
---

![Purchased Member Analysis page](../../assets/images/ec-bi-customer-analysis-hero.en.png){ title="Purchased Member Analysis Page" .hero-page }

## About Purchased Member Analysis { #intro-customer-analysis }

"Purchased Member Analysis" is a tab on the Member Analysis page. It splits customers who made purchases in the specified period into "new customers" and "returning customers," and shows each group's contribution from three angles: customer count, orders, and repurchases. With this analysis, you can tell whether your current sales are driven by "acquiring new customers" or "repurchases from returning customers."

From top to bottom, the page has three sections:

- **Customer Summary**: Accumulated customers, active customers, and the number and share of new / returning customers.
- **Order Summary**: The order count and order amount from new and returning customers.
- **Repurchase Summary**: The number of repeat customers, repurchase rate, and the new / returning makeup of repurchases.

## Prerequisites and Limitations { #prerequisites-customer-analysis }

### How New and Returning Customers Are Defined { #prerequisites-customer-analysis-definition }

On this tab, new and returning customers are defined by "first order time," which differs from "new members" in "Member Analysis," which are defined by registration time:

- **New Customers**: Customers whose first order was placed in the specified period.
- **Returning Customers**: Customers who had ordered before and ordered again in the specified period.
- **Accumulated Customers**: The number of customers who placed an order from the store's opening until the end of the specified period.

For a detailed comparison, see [Two Definitions of New Members and New Customers](references/member-analysis-definitions-reference.md#reference-member-new-definitions){ data-preview }. In addition, all figures count only [valid orders](references/member-analysis-definitions-reference.md#reference-member-valid-order){ data-preview } and are [updated the next day](references/member-analysis-definitions-reference.md#reference-member-update-time){ data-preview }.

## Page Overview { #overview-customer-analysis }

| Section | Switchable Views | What It Shows |
| :-- | :-- | :-- |
| Customer Summary | — | Accumulated customers, active customers, new customers, returning customers, and the share of new and returning customers |
| Order Summary | Order count / order amount | Total order count (amount), new customer order count (amount), returning customer order count (amount), and the share of new and returning customers |
| Repurchase Summary | Repeat customers / repeat orders / repeat order value | Repeat customers and repurchase rate, repeat new customers, repeat returning customers, and their shares |

## Steps { #operate-customer-analysis }

### Set the Query Period { #operate-customer-analysis-date-range }

Unlike other tabs, **the whole tab shares one time range**, located in the upper-right corner of the page:

1. **Click the date field in the upper-right corner:** This opens the date picker.
2. **Choose a preset or custom range:** Select a preset range (the default is "This Month"), or select start and end dates yourself.
3. **Apply:** After you make your selection, all three sections on the page reload for the new period.

![Adjust the date range](../../assets/images/ec-bi-customer-analysis-date-range.zh-tw.en.png){ title="Adjust the Date Range" }

!!! note "Note"
    If the start and end dates are not selected correctly, the system shows a reminder. Select both a start and an end date again.

---

### View the Customer Summary <small>New vs. Returning</small> { #operate-customer-analysis-customer }

1. **Check customer counts:** "Customer Summary" shows **Accumulated Customers**[^2], **Active Customers**, **New Customers**, and **Returning Customers** as data cards. Hover over the hint icon on a card to see the definition of each figure.

    ![Customer summary data cards](../../assets/images/ec-bi-customer-analysis-customer-cards.zh-tw.en.png){ title="Customer Summary Data Cards" }

2. **Check the new / returning share:** The section uses the **New and Returning Customers by Period** line chart and the **Proportion of New and Returning Customer** pie chart to show how new and returning customers change and compare, so you can tell whether sales are mainly driven by new or returning customers.

    === "Line Chart"

        Hover over a data point to see the customer count for that month. Click an item name to hide or show its data.

        ![New and returning customers by period](../../assets/images/ec-bi-customer-analysis-line-chart.zh-tw.en.png){ title="New and Returning Customers by Period" }

        !!! note "Note"

            A customer who orders multiple times in the period is counted only once in active customers. So the sum of new and returning customers for each month (or day) in the line chart may not equal the cumulative values on the data cards above.

    === "Pie Chart"

        Hover over a slice to see the share for that item. Click an item name to hide or show its data.

        ![New and returning customer share](../../assets/images/ec-bi-customer-analysis-pie-chart.zh-tw.en.png){ title="New and Returning Customer Share" }

        ??? info "How Shares Are Calculated"

            - **New customer share:** New customers ÷ active customers
            - **Returning customer share:** Returning customers ÷ active customers

---

### View the Order Summary { #operate-customer-analysis-order }

1. **Switch views:** At the top of "Order Summary," you can switch between the **"Order Count"** and **"Order Amount"** views.

    === "Order Count"

        ![Order summary: order count](../../assets/images/ec-bi-customer-analysis-order-count.zh-tw.en.png){ title="Order Summary: Order Count" }

    === "Order Amount"

        ![Order summary: order amount](../../assets/images/ec-bi-customer-analysis-order-amount.zh-tw.en.png){ title="Order Summary: Order Amount" }

2. **Check new / returning contribution:** After you switch, the data cards show **total order count (amount)**[^3], **New Customer Orders**, **Returning Customer Orders**, **New Customer Order Value**, and **Returning Customer Order Value**. Together with the period analysis and share charts below, they show which group of customers brings in most orders and revenue.

    === "Order Count"

        Hover over a slice to see the share for that item. Click an item name to hide or show its data.

        ![Order summary: order count view](../../assets/images/ec-bi-customer-analysis-order-count-view.zh-tw.en.png){ title="Order Summary: Order Count View" }

        ??? info "How Shares Are Calculated"

            - **New customer order share:** New customer orders ÷ total orders
            - **Returning customer order share:** Returning customer orders ÷ total orders

    === "Order Amount"

        Hover over a slice to see the share for that item. Click an item name to hide or show its data.

        ![Order summary: order amount view](../../assets/images/ec-bi-customer-analysis-order-amount-view.zh-tw.en.png){ title="Order Summary: Order Amount View" }

        ??? info "How Shares and Averages Are Calculated"

            - **New customer order amount share:** New customer order value ÷ total order amount
            - **Returning customer order amount share:** Returning customer order value ÷ total order amount
            - **New customer average order value:** New customer order value ÷ new customer orders
            - **New customer average spend per customer:** New customer order value ÷ new customers
            - **Returning customer average order value:** Returning customer order value ÷ returning customer orders
            - **Returning customer average spend per customer:** Returning customer order value ÷ returning customers

    !!! warning "Warning"

        New customer order count / new customer order value in Order Summary include both new customers' first-purchase orders and their repeat orders.

---

### View the Repurchase Summary and Repurchase Rate { #operate-customer-analysis-repurchase }

1. **Switch views:** At the top of "Repurchase Summary," you can switch between **Repeat Customers**, **Repeat Orders**, and **Repeat Order Value**.

    === "Repeat Customers"

        ![Repurchase summary: repeat customers](../../assets/images/ec-bi-customer-analysis-repurchase-customer-count.zh-tw.en.png){ title="Repurchase Summary: Repeat Customers" }

    === "Repeat Orders"

        ![Repurchase summary: repeat orders](../../assets/images/ec-bi-customer-analysis-repurchase-order-count.zh-tw.en.png){ title="Repurchase Summary: Repeat Orders" }

    === "Repeat Order Value"

        ![Repurchase summary: repeat order value](../../assets/images/ec-bi-customer-analysis-repurchase-order-amount.zh-tw.en.png){ title="Repurchase Summary: Repeat Order Value" }

2. **Check the repurchase rate:** When you switch between repeat customers / repeat orders / repeat order value, the data cards show the corresponding repurchase metrics and details. Together with the period analysis and share charts below, they help you assess customer loyalty and repurchase contribution.

    === "Repeat Customers"
        The data cards show the **Repurchase Rate** percentage[^1], **Repeat New Customers**[^7], and **Repeat Returning Customers**[^6].

        Hover over a data point to see its value, or over a slice to see its share. Click an item name to hide or show its data.

        ![Repurchase summary: repurchase rate](../../assets/images/ec-bi-customer-analysis-repurchase-rate.zh-tw.en.png){ title="Repurchase Summary: Repurchase Rate" }

        ??? info "How the Repurchase Rate Is Calculated"

            - **Repeat Customers:** The number of customers who had purchased before and ordered again in the specified period.
            - **Repeat Customer Rate:** Among customers who ordered in the specified period, the share who are repeat customers (= repeat customers ÷ active customers)

    === "Repeat Orders"
        The data cards show **Repeat Orders**[^4], **Repeat New Customer Orders**[^5], and **Repeat Returning Customer Orders**[^8].

        Hover over a data point to see its value, or over a slice to see its share. Click an item name to hide or show its data.

        ![Repurchase summary: repeat orders view](../../assets/images/ec-bi-customer-analysis-repurchase-order-count-view.zh-tw.en.png){ title="Repurchase Summary: Repeat Orders View" }

        ??? info "Estimating First-Purchase Orders"

            New customer first-purchase orders = new customer orders – repeat new customer orders

    === "Repeat Order Value"
        The data cards show **Repeat Order Value**[^4], **Repeat New Customer Order Value**[^5], and **Repeat Returning Customer Order Value**[^9].

        Hover over a data point to see its value, or over a slice to see its share. Click an item name to hide or show its data.

        ![Repurchase summary: repeat order value view](../../assets/images/ec-bi-customer-analysis-repurchase-order-amount-view.zh-tw.en.png){ title="Repurchase Summary: Repeat Order Value View" }

        ??? info "Estimating First-Purchase Order Value"

            New customer first-purchase order value = new customer order value – repeat new customer order value

[^1]: The repurchase rate is the share of active customers in the period who are repeat customers. If the repurchase rate is low, you can use first-purchase gifts or subscription campaigns to raise it.
[^2]: The number of customers who placed an order from the store's opening until the end of the specified period. Note: placing an order means placing a valid order, that is, an order whose status is not canceled or returned.
[^3]: The number (amount) of valid orders in the specified period. Valid orders: orders whose status is not canceled or returned.
[^4]: The number (amount) of valid orders from repeat customers in the specified period, excluding first orders.
[^5]: The number (amount) of valid orders from repeat new customers in the specified period, excluding first orders.
[^6]: The number of customers who had ordered before and ordered again in the specified period (= returning customers).
[^7]: The number of customers whose first order was in the specified period and who ordered again in the specified period.
[^8]: The number of valid orders from repeat returning customers in the specified period (= returning customer orders).
[^9]: The amount of valid orders from repeat returning customers in the specified period (= returning customer order value).

---

### Download Data for the Period { #operate-customer-analysis-download }

After you set the period, click the **download icon** in the upper-right corner of the page to export and save the Purchased Member Analysis data for the period.

![Download data for the period](../../assets/images/ec-bi-customer-analysis-download.zh-tw.en.png){ title="Download Data for the Period" }

## Important Rules and Limitations { #specs-customer-analysis }

- **New vs. returning is based on first order time:** This differs from "new members" in "Member Analysis" (defined by registration time), so do not compare figures from the two pages directly.
- **The whole tab shares one time range:** Changing the date in the upper-right corner affects all three sections at once. This differs from "Member Analysis," where each chart has its own range.
- **Only valid orders are counted:** Canceled and returned orders are excluded.
- **Data is updated the next day:** Today's orders are not reflected right away.

## Application Reference { #reference-customer-analysis-appendix }

Besides helping you see how marketing campaigns perform, Purchased Member Analysis can also help you set spending thresholds for promotions. You can use the following formulas as a reference for setting thresholds:

??? example "New Customer Marketing"

    **New customer average first-purchase order value:** (new customer order value – repeat new customer order value) ÷ (new customer orders – repeat new customer orders)

    Use this to set spending thresholds for campaigns such as exclusive coupons for new customers, limited-time first-purchase gifts, and spend-threshold gifts for new customers.

??? example "Returning Customer Marketing"

    **Returning customer average order value:** Returning customer order value ÷ returning customer orders

    Use this to set spending thresholds for campaigns such as exclusive coupons for returning customers and spend-threshold gifts for returning customers.

??? example "Store-Wide Marketing"

    **Average order value:** Total order amount ÷ total orders

    Use this to set spending thresholds for campaigns such as store-wide coupons and store-wide spend-threshold gifts.

## Next Steps { #next-steps-customer-analysis }

<div class="grid cards" markdown>

- :lucide-chart-line:{ .lg }  
  [__Member Analysis__](member-analysis.md){ title="Member Analysis" }  
  Track member base size, growth trends, and overall repurchase rate.

- :lucide-users:{ .lg }  
  [__Member Overview__](member-overview.md){ title="Member Overview" }  
  See profile analysis by gender, age, registration source, and member level.

</div>

## FAQ { #faq-customer-analysis }

??? quote "The new customer count here doesn't match new members in "Member Analysis""
    [](){ #faq-customer-analysis-new-definition }
    The two use different definitions of new and returning, so this is normal.

    - "New customers" on this page are based on **first order time**.
    - "New members" in "Member Analysis" are based on **registration time**.
    - For a detailed comparison, see [Two Definitions of New Members and New Customers](references/member-analysis-definitions-reference.md#reference-member-new-definitions){ data-preview }.

??? quote "The numbers in the three sections don't seem to add up"
    [](){ #faq-customer-analysis-shared-range }
    First make sure all three sections are showing the same time range.

    - This tab shares the date range in the upper-right corner across the whole page, and all three sections update together when you change it.
    - Figures count only valid orders and are updated the next day.

## References { #reference-customer-analysis }

- [Member Analysis Shared Definitions](references/member-analysis-definitions-reference.md)
