---
title: "Member Overview"
description: "Build member profiles from gender, age, registration source, and member level to help you adjust product copy, ad audiences, and your membership program."
created: 2026-06-16 00:00
last_modified: 2026-07-10 15:20
lang: en-US
type: guide
author: Jase
reviewers: []
notes: 
  - verify 適用方案是否包括專業跟進階
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
  - 查看會員性別年齡分群
  - 了解會員註冊來源分布
  - 比較 VIP 與普通會員銷售貢獻
  - 下載會員輪廓報表
features:
  - 會員總覽
  - 會員性別分群
  - 會員年齡分群
  - 會員現況
  - 會員等級銷售狀況
prerequisites:
  - 了解有效訂單定義
  - 了解數據更新時間
related:
  - ec/business-intelligence/references/member-analysis-definitions-reference/
  - ec/business-intelligence/references/member-status-registration-sources-reference/
  - ec/business-intelligence/references/member-age-groups-reference/
  - ec/business-intelligence/references/member-level-sales-status-reference/
  - ec/business-intelligence/member-analysis/
  - ec/business-intelligence/customer-analysis/
tags:
  - "Member Overview"
  - "Member Analysis"
  - "Member Profiles"
  - "Gender Groups"
  - "Age Groups"
  - "Registration Source"
  - "Member Level"
  - "Sales Status"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 分析報表 > 會員分析
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=11624
permalink: "https://help.cyberbiz.io/ec/business-intelligence/member-overview/"
comments: false
search:
  exclude: false
icon: lucide/users
hide: []
---

![Member Overview page](../../assets/images/ec-bi-customer-summary-hero.en.png){ title="Member Overview Page" .hero-page }

## About Member Overview { #intro-member-overview }

"Member Overview" is a tab on the Member Analysis page that provides more detailed member attribute data than "Member Analysis." It shows member counts and sales by gender, age, registration source, and member level in tables, and you can download each table as Excel for targeted marketing and audience planning.

The page has the following sections:

- **Member Gender Groups**: Member counts by gender.
- **Member Age Groups**: Member counts by age range.
- **Member Status**: Member counts by registration status and sign-in source (FB, LINE, and so on).
- **Member Level Sales Status by Period**: Compares the sales contribution of VIP members and regular members.
- **Sales from LINE Shopping**: Sales from the LINE Shopping channel (appears only if the LINE Shopping feature is turned on).

## Prerequisites and Limitations { #prerequisites-member-overview }

### Plan Requirements { #prerequisites-member-overview-plan }

"Member Overview" is an advanced member profile analysis available only on the **Enterprise** plan.

---

### Data Basis { #prerequisites-member-overview-basis }

- **Valid orders**: Sales figures count only valid orders. Canceled and returned orders are excluded. See [Valid Order Definition](references/member-analysis-definitions-reference.md#reference-member-valid-order){ data-preview }.
- **Update time**: Data is updated the next day, so today's orders and registrations do not appear right away. See [Data Update Time](references/member-analysis-definitions-reference.md#reference-member-update-time){ data-preview }.

## Page Overview { #overview-member-overview }

| Section | Type | What It Shows |
| :-- | :-- | :-- |
| [Member Gender Groups](#operate-member-overview-gender) | Table | Number of male, female, and unspecified members |
| [Member Age Groups](#operate-member-overview-age) | Table | Number of members in each age range |
| [Member Status](#operate-member-overview-status) | Table | Member counts by registration status and sign-in source |
| [Member Level Sales Status by Period](#operate-member-overview-levels) | Table | Sales contribution of VIP members compared with regular members |
| [Sales from LINE Shopping](#operate-member-overview-line) | Table | Sales from the LINE Shopping channel |

For the detailed meaning of each category, see [Member Status and Registration Sources Reference](references/member-status-registration-sources-reference.md#reference-member-registration-sources){ title="Member Status and Registration Sources Reference" data-preview }, [Member Age Groups Reference](references/member-age-groups-reference.md#reference-member-age-groups){ title="Member Age Groups Reference" data-preview }, and [Member Level Sales Status Reference](references/member-level-sales-status-reference.md#reference-member-levels){ title="Member Level Sales Status Reference" data-preview }.

## Steps { #operate-member-overview }

Each table loads automatically when you open the tab. Here is how to read them, adjust the period, and download them.

### View Member Gender Groups { #operate-member-overview-gender }

"Member Gender Groups" lists the number of **male**, **female**, and **unspecified** members in a table to help you fine-tune product copy and ad audiences.

![Member gender groups table](../../assets/images/ec-bi-customer-gender.zh-tw.en.png){ title="Member Gender Groups" }

---

### View Member Age Groups { #operate-member-overview-age }

"Member Age Groups" lists member counts by age range (from 19 and under to 70 and over, plus unspecified). For the definition of each range, see [Member Age Groups Reference](references/member-age-groups-reference.md#reference-member-age-groups){ data-preview }.

![Member age groups table](../../assets/images/ec-bi-customer-age.zh-tw.en.png){ title="Member Age Groups" }

---

### View Member Status and Registration Sources { #operate-member-overview-status }

1. **Check registration status:** "Member Status" splits members into **New Members**, **Existing Members**, **Registered Members**, and **Unregistered Members** so you can see the makeup of your list.
2. **Check sign-in sources:** The same section also lists sources such as **FB Sign-In Members**, **LINE Sign-In Members**, and **Linked LINE@ Members**, so you can compare the size of each source. For the meaning of each category, see [Member Status and Registration Sources Reference](references/member-status-registration-sources-reference.md#reference-member-registration-sources){ data-preview }.

![Member status and registration sources table](../../assets/images/ec-bi-customer-status-source.zh-tw.en.png){ title="Member Status and Registration Sources" }

??? info "How Average Order Value Is Calculated"
    - **Average order value per order**: For each member group in the period (new members, existing members, registered members, unregistered members, FB sign-in members, LINE sign-in members, linked LINE@ members, and so on), total sales ÷ total orders (rounded to 2 decimal places)
    - **Average spend per member**: For each member group in the period (new members, existing members, registered members, unregistered members, FB sign-in members, LINE sign-in members, linked LINE@ members, and so on), total sales ÷ number of purchasing members (rounded to 2 decimal places)

---

### Compare Sales of VIP and Regular Members { #operate-member-overview-levels }

1. **Check level contribution:** "Member Level Sales Status by Period" splits members into **VIP Members** and **Regular Members** and compares their sales in the specified period to assess how well your member level system works. The line between VIP and regular members depends on the thresholds you set. See [Member Level Sales Status Reference](references/member-level-sales-status-reference.md#reference-member-levels){ data-preview }.

![Member level sales status table](../../assets/images/ec-bi-customer-vip-sales.zh-tw.en.png){ title="Member Level Sales Status" }

??? note "VIP Rules"
    VIP and regular members are classified by their **current member status** (not their status when they ordered). As long as a customer is currently a VIP member, their orders count toward the VIP group, whether or not the order used a VIP discount.

??? info "How Average Order Value Is Calculated"
    - **Average order value per order**: For each group in the period (regular members or VIP members), total sales ÷ total orders (rounded to 2 decimal places)
    - **Average spend per member**: For each group in the period (regular members or VIP members), total sales ÷ number of purchasing members (rounded to 2 decimal places)

---

### View LINE Shopping { #operate-member-overview-line }

The "Sales from LINE Shopping" section lists sales data from the LINE Shopping channel. This section appears only if the LINE Shopping feature is turned on.

![LINE Shopping sales status table](../../assets/images/ec-bi-customer-line-shopping.zh-tw.en.png){ title="LINE Shopping Sales Status" }

---

### Adjust the Period and Download Excel { #operate-member-overview-export }

1. **Adjust the period:** Each table has its own date range field in the upper-right corner. Click it to choose a preset range or custom start and end dates, then click **Apply** to reload.
2. **Download the report:** Click the table's **"Download as Excel"** to export its data to an Excel file for further analysis or for importing into ad platforms to plan audiences.

![Adjust the period and download Excel](../../assets/images/ec-bi-customer-export-excel.zh-tw.en.png){ title="Adjust the Period and Download" }

## Important Rules and Limitations { #specs-member-overview }

- **Only valid orders are counted:** Sales figures exclude canceled and returned orders.
- **Data is updated the next day:** Today's orders and registrations are not reflected right away.
- **The LINE Shopping section appears dynamically:** "Sales from LINE Shopping" appears only if the LINE Shopping feature is turned on.
- **Age is calculated from the birthday in real time:** Members without a birthday are grouped under "Not provided."

## Next Steps { #next-steps-member-overview }

<div class="grid cards" markdown>

- :lucide-chart-line:{ .lg }  
  [__Member Analysis__](member-analysis.md){ title="Member Analysis" }  
  Return to the default tab to track member base size, growth, and repurchase trends.

- :lucide-repeat:{ .lg }  
  [__Purchased Member Analysis__](customer-analysis.md){ title="Purchased Member Analysis" }  
  Split new and returning customers to see order contribution and repurchase performance in depth.

</div>

## FAQ { #faq-member-overview }

??? quote "Many members are "Not provided""
    [](){ #faq-member-overview-unfilled }
    This means many members have not filled in their gender or birthday.

    - Gender and age groups are based on the information members provide. Members who have not filled it in are grouped under "Not provided."
    - Encourage members to complete their profiles through member engagement or campaigns to make segmentation more accurate.

## References { #reference-member-overview }

- [Member Status and Registration Sources Reference](references/member-status-registration-sources-reference.md)
- [Member Age Groups Reference](references/member-age-groups-reference.md)
- [Member Level Sales Status Reference](references/member-level-sales-status-reference.md)
- [Member Analysis Shared Definitions](references/member-analysis-definitions-reference.md)
