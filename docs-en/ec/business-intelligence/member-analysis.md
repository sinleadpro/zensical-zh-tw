---
title: "Member Analysis"
description: "Track member base size, growth trends, and retention and repurchase after the first purchase to assess the health of your membership program."
created: 2026-06-16 00:00
last_modified: 2026-07-10 15:39
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
  - 了解會員經營健康度
  - 查看會員規模
  - 查看會員成長趨勢
  - 評估會員留存與回購表現
features:
  - 會員分析
  - 會員規模
  - 會員留存
  - 會員回購
prerequisites:
  - 了解有效訂單定義
  - 了解數據更新時間與新舊會員判定方式
related:
  - ec/business-intelligence/references/member-analysis-definitions-reference/
  - ec/business-intelligence/member-overview/
  - ec/business-intelligence/customer-analysis/
tags:
  - "Member Analysis"
  - "Member Base Size"
  - "Member Growth"
  - "Member Retention"
  - "Member Repurchase"
  - "Membership Health"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分析報表 > 會員分析
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5050
permalink: "https://help.cyberbiz.io/ec/business-intelligence/member-analysis/"
comments: false
search:
  exclude: false
icon: lucide/user-cog
hide: []
---

![Member Analysis page](../../assets/images/ec-bi-member-analysis-hero.en.png){ title="Member Analysis Page" .hero-page }

## About Member Analysis { #intro-member-analysis }

"Member Analysis" is on the member analysis page under "Charts" in the admin. It organizes store-wide member and order data into data cards and charts, so you can see at a glance your total members, recent growth, retention after the first purchase, repurchase cycles, and per-member contribution.

From top to bottom, the page covers three areas:

- **Size and growth**: Total members, new members registered in the last 30 days, and member count trend.
- **First purchase and retention**: Share of registered members by number of purchases, and new member order rate.
- **Repurchase and contribution**: Average member repurchase cycle, average spend per member, average recognized orders per member, and member repurchase rate.

## Prerequisites and Limitations { #prerequisites-member-analysis }

### Data Basis { #prerequisites-member-analysis-basis }

Before you interpret the numbers, understand the shared calculation basis:

- **Valid orders**: All figures count only valid orders. Canceled and returned orders are excluded. See [Valid Order Definition](references/member-analysis-definitions-reference.md#reference-member-valid-order){ data-preview }.
- **Update time**: Data is updated the next day, so today's orders and registrations do not appear right away. See [Data Update Time](references/member-analysis-definitions-reference.md#reference-member-update-time){ data-preview }.
- **New vs. returning**: "New members" on this page are based on registration time, which differs from the new and returning customer definitions in "Purchased Member Analysis." See [Two Definitions of New Members and New Customers](references/member-analysis-definitions-reference.md#reference-member-new-definitions){ data-preview }.

## Page Overview { #overview-member-analysis }

| Section | Type | What It Shows |
| :-- | :-- | :-- |
| [Total Members](#operate-member-analysis-scale) | Number | Cumulative total members since the store opened |
| [New Members in the Last 30 Days](#operate-member-analysis-scale) | Number | Number of members who joined in the last 30 days |
| [Member Count Trend](#operate-member-analysis-growth) | Line chart | How the number of new members changes month by month |
| [Purchase Count of Members Registered in the Period (Share of Total Members)](#operate-member-analysis-frequency) | Chart | Among members registered in the period, the share who purchased once, twice, 3 or more times, or never |
| [Average Recognized Orders per Member (Monthly Trend)](#operate-member-analysis-avg-orders) | Line chart | Total recognized orders ÷ total members, by month |
| [Average Member Repurchase Cycle (Days)](#operate-member-analysis-repurchase-cycle) | Number | Average number of days between a member's orders |
| [Average Spend per Member (Monthly Trend)](#operate-member-analysis-avg-spend) | Line chart | Average amount contributed per purchasing member each month |
| [New Member Order Rate](#operate-member-analysis-order-rate) | Chart | Among members who registered that month, the share who ordered and did not order (for both "All Non-Canceled Orders" and "Recognized Orders") |
| [Member Repurchase Rate](#operate-member-analysis-repurchase-rate) | Number | Customers with 2 or more orders ÷ customers who have ever ordered |

## Steps { #operate-member-analysis }

Each section loads automatically when you open the page. The following explains how to read each group of sections by purpose and how to adjust the period.

### View Member Base Size { #operate-member-analysis-scale }

**"Total Members"** at the top of the page shows the cumulative number of members since the store opened. **"New Members in the Last 30 Days"** shows how many joined in the last 30 days, so you can judge recent recruitment results.

![Member base size](../../assets/images/ec-bi-member-scale.zh-tw.en.png){ title="Member Base Size" }

---

### View the Member Growth Trend { #operate-member-analysis-growth }

"Member Count Trend" shows the monthly change in new members as a line chart. Hover over a data point to see that month's figure and check whether member growth is speeding up or slowing down.

![Member growth trend](../../assets/images/ec-bi-member-growth-trend.zh-tw.en.png){ title="Member Growth Trend" }

---

### View the Purchase Count Distribution { #operate-member-analysis-frequency }

"Purchase Count of Members Registered in the Period (Share of Total Members)" shows, among members registered in the specified period, the share who purchased **once**, **twice**, **3 or more times**, and **never**. The more the share shifts toward "3 or more times," the better you are at retaining members after their first purchase.

Hover over a slice to see the share for that item. Click an item name to hide or show its data.

![Purchase count distribution](../../assets/images/ec-bi-member-consumption-frequency.zh-tw.en.png){ title="Purchase Count Distribution" }

---

### View the New Member Order Rate { #operate-member-analysis-order-rate }

"New Member Order Rate" shows the share of members who registered that month who **ordered** and **did not order**, calculated two ways: "All Non-Canceled Orders" and "Recognized Orders"[^1]. It helps you judge whether newly recruited members actually go on to buy.

[^1]: "All Non-Canceled Orders" has a broader scope, while "Recognized Orders" also excludes returns and is stricter. Both define new members as "members who registered during that month."

Hover over a bar to see the share for that item. Click an item name to hide or show its data.

![New member order rate](../../assets/images/ec-bi-member-order-rate.zh-tw.en.png){ title="New Member Order Rate" }

??? info "How the New Member Order Rate Is Calculated"
    - **New member definition**: Within the specified period, members are first grouped by month. Members who registered during a month are new members for that month.
    - **All non-canceled orders**: (New members who ordered (non-canceled orders) or new members who did not order ÷ total new members) × 100%, rounded to the nearest whole number.
    - **Recognized orders**: (New members who ordered (recognized orders) or new members who did not order ÷ total new members) × 100%, rounded to the nearest whole number.

---

### View the Repurchase Cycle { #operate-member-analysis-repurchase-cycle }

"Average Member Repurchase Cycle (Days)" estimates the average interval between a member's orders. Use it to time repurchase notifications (for example, remind members to buy again shortly before the average cycle).

![Repurchase cycle](../../assets/images/ec-bi-member-repurchase-cycle.zh-tw.en.png){ title="Repurchase Cycle" }

??? info "How the Average Member Repurchase Cycle Is Calculated"
    The average repurchase cycle for all members since the store opened is calculated in two steps:

    1. **Average repurchase days for one member** = (time of last order − time of first order) ÷ the member's total orders
    2. **Store-wide average repurchase cycle** = sum of all members' repurchase days ÷ total members

---

### View Average Spend per Member { #operate-member-analysis-avg-spend }

"Average Spend per Member (Monthly Trend)" shows the average amount contributed per purchasing member each month, so you can see whether per-customer contribution is rising or falling. Hover over the chart to see each month's data.

![Average spend per member](../../assets/images/ec-bi-member-avg-spend.zh-tw.en.png){ title="Average Spend per Member" }

??? info "How the Average Spend per Member Monthly Trend Is Calculated"
    Within the specified period, the average recognized order value per member is calculated for each month:

    **Average spend per member** = total order amount in the period ÷ total members who purchased in the period

---

### View Average Orders { #operate-member-analysis-avg-orders }

"Average Recognized Orders per Member (Monthly Trend)" is total recognized orders divided by total members, reflecting the average number of orders each member brings in.

![Average orders](../../assets/images/ec-bi-member-avg-orders.zh-tw.en.png){ title="Average Orders" }

??? info "How Average Recognized Orders per Member Is Calculated"
    **Average recognized orders per member** = total recognized orders since the store opened ÷ total members since the store opened

    > Total members are taken from "Customers > Customer List."

---

### View the Repurchase Rate { #operate-member-analysis-repurchase-rate }

"Member Repurchase Rate" is the number of customers with 2 or more orders divided by the number of customers who have ever ordered. It is a core measure of customer loyalty.

![Repurchase rate](../../assets/images/ec-bi-member-repurchase-rate.zh-tw.en.png){ title="Repurchase Rate" }

---

### Adjust the Chart Period { #operate-member-analysis-date-range }

Some sections (trend charts, purchase count share, and so on) **have their own date range field in the upper-right corner**, so you can set the time range for each section separately:

1. **Click the date field:** In the upper-right corner of the chart you want to adjust, click the date input box to open the date picker.
2. **Choose a preset or custom range:** Select a preset range (Last 7 Days, Last 30 Days, This Month, and so on), or select start and end dates on the calendar.
3. **Apply:** Click **Apply** to reload the section for the new period.

![Adjust the period](../../assets/images/ec-bi-member-date-range.zh-tw.en.png){ title="Adjust the Period" }

!!! tip "Tip"
    Each section's date range is **independent**, so changing one does not affect the other charts. To compare them as a whole, set each section to the same range one by one.

## Important Rules and Limitations { #specs-member-analysis }

- **Only valid orders are counted:** Canceled and returned orders are excluded, so figures may differ from the total amount in the order list.
- **Data is updated the next day:** Today's orders and registrations are not reflected right away. This is normal.
- **New vs. returning is based on registration time:** "New members" on this page are members who registered during that month. This differs from "Purchased Member Analysis," which defines new and returning customers by "first order time," so do not add or compare figures from the two pages directly.
- **Number format:** Amounts are shown as whole numbers with thousands separators.

## Next Steps { #next-steps-member-analysis }

<div class="grid cards" markdown>

- :lucide-users:{ .lg }  
  [__Member Overview__](member-overview.md){ title="Member Overview" }  
  See profile analysis by gender, age, registration source, and member level.

- :lucide-repeat:{ .lg }  
  [__Purchased Member Analysis__](customer-analysis.md){ title="Purchased Member Analysis" }  
  Split new and returning customers by "first order time" to see order contribution and repurchase performance in depth.

</div>

## FAQ { #faq-member-analysis }

??? quote "Chart figures don't match the member or order list"
    [](){ #faq-member-analysis-counted-orders }
    Member Analysis counts only "valid orders," and data is updated the next day.

    - Amounts from canceled and returned orders are not counted.
    - Orders placed and members registered today appear after the next day's update.
    - For details, see [Valid Order Definition](references/member-analysis-definitions-reference.md#reference-member-valid-order){ data-preview }.

??? quote ""New members" don't match the new customer figures in "Purchased Member Analysis""
    [](){ #faq-member-analysis-new-definition }
    This is because the two tabs define new and returning differently. It is not a data error.

    - "New members" in Member Analysis are based on **registration time**.
    - "New customers" in Purchased Member Analysis are based on **first order time**.
    - For a detailed comparison, see [Two Definitions of New Members and New Customers](references/member-analysis-definitions-reference.md#reference-member-new-definitions){ data-preview }.

## References { #reference-member-analysis }

- [Member Analysis Shared Definitions](references/member-analysis-definitions-reference.md)
