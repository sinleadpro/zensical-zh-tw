---
title: "Understanding The Profit-sharing Function"
description: "Understanding the working mechanism, applicable targets, and scenarios of profit-sharing functions will help you choose the most suitable marketing profit-sharing plan."
created: 2026-02-06 00:00
last_modified: 2026-06-30 10:52
lang: en-US
type: guide
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 行銷活動
sites:
  - TW
audiences:
  - admin
difficulty: beginner
tnb: branch
plans:
  - Enterprise
  - Advanced
  - Expert
cyb_extensions: []
intents:
  - 了解分潤機制
  - 選擇分潤方案
features:
  - 分潤設定
  - 推薦人分潤
  - 註冊人分潤
prerequisites: []
related:
  - [[設定推薦人分潤方案]]
  - [[設定註冊人分潤方案]]
  - [[匯出分潤報表]]
  - [[查詢分潤夥伴與代碼資訊]]
tags: []
acoiv: activate
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 推薦人分潤
  - 行銷活動 > 註冊人分潤
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=28632
permalink: "https://help.cyberbiz.io/ec/profit-sharing.en"
comments: false
search:
  exclude: false
icon: lucide/hand-coins
hide: []
---
#  Understand The Profit Sharing Function

Understand the operation mechanism, applicable targets and scenarios of the profit sharing function to help you choose the most suitable marketing profit sharing plan.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品){ title="圖示慣例" } | Brand Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案){ title="圖示慣例" } | Advanced / Expert / All PLUS / Enterprise
{ .doc-badge }


Profit sharing is an effective tool to promote revenue growth for internal and external partners. Through influencer marketing, blogger promotion, or internal employee promotion, profits are automatically calculated and distributed after an order is completed. CYBERBIZ offers a comprehensive revenue-sharing solution covering both its online website and offline stores, helping merchants resolve issues related to sales performance attribution and reward distribution during the integration of online and offline channels. **Application Scenarios:** **KOL/Influencer Marketing:** Sign revenue-sharing agreements with external partners and track sales performance through exclusive links or referral codes. **Employee Incentive System:** Encourage store staff to guide customers to register as members or make purchases, attributing online sales to the promoting staff. **Refurbished Customer Referral Program:** Incentivize existing members to share referral codes with friends, achieving a "two-way feedback" word-of-mouth marketing effect. **Store Sales Attribution:** Accurately record the sales performance of employees who assist with checkout or provide services at POS checkout or in-store pickup.## Instructions For Use
The profit-sharing function of
- CYBERBIZ is only responsible for **performance attribution and data statistics**. The system **will not make payments or generate actual cash flow transactions**. A list of revenue-sharing plans for each version of
- 
        
    | System Specifications | Number of Plans | Applicable Versions |
    | ------- | ------- | -------- |
    | Standard Configuration | 1 Set | Advanced Version, Advanced PLUS Version, Expert Version, Expert PLUS Version <br> (Professional PLUS version cannot use revenue sharing function if not selected) |,
,     , | (optional), | (100 units), |, all PLUS versions of <br> (profit sharing function must be selected when purchasing), |,

## Overview Of Profit Sharing Mechanism
Based on the different **performance attribution logic** and **occurrence scenarios**,
provides the following four core profit-sharing models:

### Referrer Profit Sharing

is the most flexible and widely used model. Referrers (such as influencers, employees, and members) provide exclusive links or referral codes to consumers.

-  **Online Behavior**: Consumers click the exclusive link or enter the referral code on the checkout page; the system automatically tracks the order.
-  **Offline Behavior**: Consumers provide the referral code at checkout in-store, which is entered by POS staff to record profit sharing.
-  **Profit Sharing Types**: Supports **profit sharing on the entire order** or **profit sharing on specific products**.

    !!! tip " How to choose a profit sharing method? "
        -  **Profit sharing on the entire order**: Suitable for collaborations with KOLs or external channels, providing quick settlement based on **total order amount**, offering the most convenient setup.
        -  **Designated Product Profit Sharing**: Suitable for situations with large profit margins on products or involving agency parts. It allows for **precise** setting of percentages for each product, enabling refined profit management.

### Profit Sharing By Registrant

emphasizes a **permanent binding** relationship. When a consumer enters a referrer's code during registration, the consumer is permanently bound to the referrer.

-  **Operating Logic**: After successful binding, the system will automatically calculate and distribute commissions to the registrant for all future online and offline purchases by the consumer.
-  **Suitable Scenarios**: Suitable for store staff recruiting long-term members or for long-term cooperative distribution partners.

### Profit Sharing For Billing Staff

-  **Operating Logic**: During POS checkout at the store, the operator manually selects the **checkout person**, and the reward for that order is awarded to that person.
-  **Applicable Scenarios**: Performance distribution in store counter shifts and shared service scenarios.

### Profit Sharing For In-store Pickup Orders

-  **Operating Logic**: For orders placed online and picked up offline, when the package arrives at the store and the customer picks it up, the operator manually selects the **person in charge of checking the goods**, and the reward for that order is awarded to that person.
-  **Applicable Scenarios**: Calculating labor rewards for store staff assisting with pickup services.
-  **Revenue Sharing Types**: Supports **In-Store Revenue Sharing** or **Pickup Revenue Sharing**.

## Comparison Of Profit Sharing Recipients And Feedback

's preset profit-sharing mechanisms apply to different types of partners as shown in the table below:

| Profit-Sharing Partners | Referrer Profit Sharing | Registrant Profit Sharing | Checkout Profit Sharing | In-Store Pickup Order Profit Sharing |
| ------- | --------- | ---------- | -------- | -------- |
| **Third-Party (Influencers/Group Buyers)** | ✓ | ✕ | ✕ | ✕ |
| **General Customer (Member)** | ✓ | ✕ | ✕ | ✕ |
| **Store Manager/Staff (Employee)** | ✓ | ✓ | ✕ | ✕ |
| **Physical Store (POS Store)** | ✓ | ✓ | ✓ | ✓ The |

system allows for setting corresponding acquisition methods and performance query permissions for different partners:

| Profit Sharing Targets | Referral Code Acquisition Methods | Performance Query Methods |
| :--- | :--- | :--- |
| **Third-Party (Influencers/Group Buyers)** | Merchant-Provided Exclusive Codes | Merchant-Provided Exclusive Report Links |
> | **General Customers (Members)** | Front-end Member Center Personal Information | Front-end Member Center > Personal Information |
> | **Store Manager/Employee (Staff)** | Backend Revenue Sharing Revenue Sharing Inquiry | Backend Revenue Sharing > Revenue Sharing Report |
> | **Physical Store (POS Store)** | Backend Revenue Sharing Revenue Sharing Inquiry | Backend Revenue Sharing > Revenue Sharing Report |

!!! warning "POS System Compatibility Notes "
     The revenue sharing function for physical stores is only available when used with the CYBERBIZ POS system. If you are currently using another system, we recommend contacting our consultants to evaluate a conversion plan.


## Core Operating Rules And Restrictions
Before planning a profit-sharing scheme, please be sure to understand the following system operation logic:
### 1.  Bonus Settlement Timing
The -  system only calculates profit sharing and distributes bonuses when the order status changes to **Closed**. If an order is returned or cancelled after being closed, the system **will not** automatically reissue or reclaim any bonuses already distributed.### 2.  Payment Processing Principles
The - CYBERBIZ backend only provides **profit sharing reports** for statistical reference; the system **does not handle** actual cash payments. Merchants can make payments themselves via offline funds, bank transfers, or system bonus points based on the report data.

### 3.  Has An Expiration Date Limit.
-  orders must be placed within the **effective period** of the plan to be eligible for profit sharing.



## Next Steps

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }
  [__Set Referrer Revenue Sharing__](referrer-profit-sharing.en.md)<br>
   Learn how to create plans, bind influencers or members, and set discounts.

- :lucide-users:{ .lg }
  [__Set Registerer Revenue Sharing__](registrant-profit-sharing.en.md)<br>
   Understand how to establish a permanently bound registration revenue sharing relationship, suitable for long-term business development.

- :lucide-bar-chart-3:{ .lg }
   [__Export Profit Sharing Report__](export-profit-sharing-reports.en.md)<br>
   Learn how to export profit sharing data as the basis for bonus distribution and performance evaluation.

- :lucide-file-search:{ .lg }
   [__Query Profit Sharing Report__](query-profit-sharing-partners-and-codes.en.md)<br>
   Learn how to query the list of profit sharing partners and corresponding profit sharing data to help you accurately verify performance records.

</div>


