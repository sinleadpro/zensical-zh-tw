---
title: Understand Profit Sharing
description: Learn how profit sharing works, who it is for, and when to use it to select the most suitable marketing Referral Plan.
created: 2026-02-06 00:00
last_modified: 2026-06-30 10:52
lang: zh-TW
type: guide
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
  - merchant
difficulty: beginner
tnb: branch
plans:
  - 企業
  - 進階
  - 高手
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
  - "設定推薦人分潤方案"
  - "設定註冊人分潤方案"
  - "ec/profit-sharing/export-profit-sharing-reports"
  - "ec/profit-sharing/query-profit-sharing-partners-and-codes"
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
permalink: "https://help.cyberbiz.io/ec/profit-sharing/"
comments: false
search:
  exclude: false
icon: lucide/hand-coins
hide: []
---
# Understand Profit Sharing

Learn how profit sharing works, who it is for, and when to use it to select the most suitable marketing Referral Plan.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品){ title="圖示慣例" } | Brand Official Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案){ title="圖示慣例" } | Advanced / Expert / all PLUS plans / Enterprise
{ .doc-badge }


Profit sharing is an effective tool that encourages internal and external partners to work together to increase revenue. It automatically calculates and allocates profits after an order is completed, whether the sale came from an influencer, a blogger, or an employee promotion. CYBERBIZ provides a comprehensive profit-sharing solution for online Brand Official Websites and physical stores, helping merchants attribute sales and allocate rewards across online and offline channels.

!!! tip "Use Cases"
	- **KOL/Influencer Marketing**: Sign profit-sharing agreements with external partners and track referral performance through dedicated links or Referral Code.
	- **Employee Incentive Program**: Encourage store staff to help customers register as members or recommend purchases, and attribute online sales to the employees who promoted them.
	- **Member Referral Program**: Motivate existing members to share Referral Code with friends and create word-of-mouth growth with rewards for both parties.
	- **Store Sales Attribution**: Accurately record the sales performance of checkout staff or pickup staff during POS checkout or in-store pickup.

## Important Notes

- The CYBERBIZ profit-sharing feature only provides **sales attribution and data reporting**. The system **does not disburse funds or process actual payment transactions**.
- Number of Referral Plan by Plan

    | System Specification | Number of Plans | Available Plans |
    | ------- | ------- | -------- |
    | Included | 1 set | Advanced, Advanced PLUS, Expert, and Expert PLUS<br>(Professional PLUS cannot use profit sharing unless the profit-sharing add-on is selected) |
    | Add-on | 100 sets | all PLUS plans<br>(the profit-sharing feature must be selected when purchasing the add-on) |

## Overview of Profit-Sharing Methods

The system provides the following four core profit-sharing methods based on differences in **sales attribution rules** and **sales channels**:

### Referral Program

This is the most flexible and widely used method. Referrer, such as influencers, employees, and members, provide customers with dedicated links or Referral Code.

- **Online Activity**: A customer clicks a dedicated link or enters Referral Code on the checkout page, and the system automatically tracks the order.
- **Offline Activity**: A customer provides Referral Code during in-store checkout, and the POS staff enters it to record the profit sharing.
- **Profit-Sharing Type**: Supports **profit sharing for the entire order** or **profit sharing for specified products**.

    !!! tip "How to Choose Online/Offline/Product Commission"
        - **Profit Sharing for the Entire Order**: Best for working with KOLs or external sales channels. It enables quick settlement based on the **order total** and is the easiest option to set up.
        - **Profit Sharing for Specified Products**: Best when product margins vary significantly or an order includes consignment products. Set the rate **precisely for each item** to manage profits in detail.

### Registrants Fee

This method establishes a **permanent association**. When a customer enters the Referrer code during registration, the customer is permanently associated with Referrer.

- **How It Works**: After the association is established, the system automatically calculates profit sharing for the registrant whenever the customer makes an online or in-store purchase.
- **Use Cases**: Best for store staff who recruit long-term members or distribution partners with long-term agreements.

### Checkout Staff Profit Sharing

- **How It Works**: During in-store POS checkout, the operator manually selects the **checkout staff** to attribute the order reward to that staff member.
- **Use Cases**: Allocating sales performance among staff working rotating shifts or serving customers together in a physical store.

### Store Pickup Order Profit Sharing

- **How It Works**: For **online orders picked up in stores**, the operator manually selects the **pickup staff** when the package arrives at the store and the customer picks it up. The order reward is then attributed to that staff member.
- **Use Cases**: Calculating service rewards for store staff who assist with order pickup.
- **Profit-Sharing Type**: Supports **store-arrival profit sharing** or **pickup profit sharing**.

## Profit-Sharing Recipients and Reward Methods

The following table shows the default scope of each profit-sharing method for different types of profit-sharing partners:

| Profit-Sharing Recipient | Referral Program | Registrants Fee | Checkout Staff Profit Sharing | Store Pickup Order Profit Sharing |
| ------- | --------- | ---------- | -------- | -------- |
| **Third Party (Influencer/Group-Buying Organizer)** | ✓ | ✕ | ✕ | ✕ |
| **General Customer (Member)** | ✓ | ✕ | ✕ | ✕ |
| **Store Manager/Staff (Employee)** | ✓ | ✓ | ✕ | ✕ |
| **Physical Store (POS Store)** | ✓ | ✓ | ✓ | ✓ |

The system provides different methods for obtaining profit-sharing information and accessing performance results based on the type of partner:

| Profit-Sharing Recipient | How to Obtain Referral Code | How to View Performance |
| :--- | :--- | :--- |
| **Third Party (Influencer/Group-Buying Organizer)** | Merchant provides a dedicated code | Merchant provides a dedicated Report Link |
> | **General Customer (Member)** | Storefront Member Center Personal Information  | Storefront Member Center > Personal Information |
> | **Store Manager/Staff (Employee)** | Admin Profit Sharing Profit-Sharing Query | Admin Profit Sharing > Profit-Sharing Report |
> | **Physical Store (POS Store)** | Admin Profit Sharing Profit-Sharing Query | Admin Profit Sharing > Profit-Sharing Report |

!!! warning "POS System Compatibility"
    Profit sharing for physical stores is available only with the CYBERBIZ POS system. If you currently use another system, contact a CYBERBIZ consultant to evaluate migration options.


## Core Operating Rules and Limitations

Before planning Referral Plan, review the following system rules:

### 1. Reward Settlement Timing
- The system calculates the profit-sharing amount and issues points rewards only when the order status changes to **Closed**.
- If an order is returned or canceled after it is closed, the system **does not** automatically reissue or revoke points that have already been issued.

### 2. Payment Handling Rules
- The CYBERBIZ Admin provides **profit-sharing reports** for reference only. The system **does not handle** actual cash disbursements.
- Based on the report data, merchants must issue payments independently through offline disbursement, bank transfer, or the system's bonus points.

### 3. Validity Period Restrictions
- An order qualifies for profit sharing only if it is placed during the plan's **validity period**.



## Next Steps

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }
  [__Set Up Referral Program__](referrer-profit-sharing.en.md)<br>
  Learn how to create a plan, associate influencers or members, and set up discounts.

- :lucide-users:{ .lg }
  [__Set Up Registrants Fee__](registrant-profit-sharing.en.md)<br>
  Learn how to establish a permanent registration profit-sharing association for long-term business development.

- :lucide-bar-chart-3:{ .lg }
  [__Export Profit-Sharing Reports__](export-profit-sharing-reports.en.md)<br>
  Learn how to export profit-sharing data for reward disbursement and performance evaluation.

- :lucide-file-search:{ .lg }
  [__Query Profit-Sharing Reports__](query-profit-sharing-partners-and-codes.en.md)<br>
  Learn how to query profit-sharing partner lists and related profit-sharing data to accurately verify sales records.

</div>


