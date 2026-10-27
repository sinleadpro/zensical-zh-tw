---
title: "Understanding Profit Sharing"
description: "Learn how profit sharing works, who it's for, and when to use it, so you can pick the marketing approach that fits your store best."
created: 2026-02-06 00:00
last_modified: 2026-06-30 10:52
lang: en-US
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
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
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
  - ec/profit-sharing/referrer-profit-sharing/
  - ec/profit-sharing/registrant-profit-sharing/
  - ec/profit-sharing/export-profit-sharing-reports/
  - ec/profit-sharing/query-profit-sharing-partners-and-codes/
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
# Understanding Profit Sharing

Learn how profit sharing works, who it's for, and when to use it, so you can pick the marketing approach that fits your store best.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品){ title="圖示慣例" } | Brand Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案){ title="圖示慣例" } | Advanced / Expert / All PLUS / Enterprise
{ .doc-badge }


Profit sharing helps you grow revenue together with internal and external partners. Influencers and bloggers drive traffic, or your staff promote your products, and the system calculates and allocates the profit automatically once an order is placed. CYBERBIZ offers a complete profit-sharing solution that covers both your online store and your physical stores, so you can attribute sales and distribute rewards across online and offline channels.

!!! tip "Use cases"
	- **KOL and influencer marketing**: Sign profit-sharing agreements with external partners and track the sales they drive through dedicated links or Referral Codes.
	- **Staff incentives**: Encourage store staff to get customers to sign up as members or to recommend purchases, and credit online sales to the staff member who promoted them.
	- **Customer referrals**: Encourage existing members to share their Referral Code with friends, so both sides are rewarded and word of mouth spreads.
	- **Store sales attribution**: Accurately record sales for the staff member who handles checkout or service at POS checkout or in-store pickup.

## Before You Start

- CYBERBIZ profit sharing only handles **sales attribution and statistics**. The system **does not pay out money or create actual payment transactions** for you.
- Number of plans by edition

    | Feature | Number of plans | Editions |
    | ------- | ------- | -------- |
    | Standard | 1 | Advanced, Advanced PLUS, Expert, Expert PLUS<br>(Professional PLUS can't use profit sharing unless the profit-sharing add-on is purchased) |
    | Add-on | 100 | All PLUS editions<br>(select profit sharing when purchasing add-ons) |

## How Profit Sharing Works

Based on **who gets credit for the sale** and **where the sale happens**, the system offers four core profit-sharing models:

### Referrer Profit Sharing

The most flexible and widely used model. A Referrer (such as an influencer, staff member, or member) gives customers a dedicated link or Referral Code.

- **Online**: When a customer clicks the dedicated link or enters the Referral Code on the checkout page, the system tracks the order automatically.
- **Offline**: The customer gives the Referral Code at in-store checkout, and POS staff enter it to record the profit share.
- **Profit-sharing types**: Supports **whole-order profit sharing** or **product-specific profit sharing**.

    !!! tip "Which type should I choose?"
        - **Whole-order profit sharing**: Best for working with KOLs or external channels. Settlement is based on the **order total**, which makes it the easiest to set up.
        - **Product-specific profit sharing**: Best when product margins vary a lot or you sell consignment items. You can set the rate **for each product**, for finer profit control.

### Registrant Profit Sharing

This model creates a **permanent link**. When a customer enters a registrant's code at sign-up, the customer is permanently linked to that registrant.

- **How it works**: Once linked, the system automatically calculates profit sharing for the registrant whenever the customer buys, online or offline.
- **When to use it**: Store staff recruiting long-term members, or long-term distribution partners.

### Checkout Staff Profit Sharing

- **How it works**: At POS checkout, the operator manually selects the **checkout staff member**, and the order's reward goes to that person.
- **When to use it**: Splitting sales among staff who share a counter, work in shifts, or serve customers together.

### Store Pickup Order Profit Sharing

- **How it works**: For orders **placed online and picked up in store**, when the package arrives at the store and the customer picks it up, the operator manually selects the **staff member who checked the goods**, and the order's reward goes to that person.
- **When to use it**: Rewarding store staff for handling pickups.
- **Profit-sharing types**: Supports **arrival profit sharing** or **pickup profit sharing**.

## Partners And Models At A Glance

The table below shows which profit-sharing models apply to each type of partner by default:

| Partner | Referrer | Registrant | Checkout staff | Store pickup |
| ------- | --------- | ---------- | -------- | -------- |
| **Third party (influencer / group-buy organizer)** | ✓ | ✕ | ✕ | ✕ |
| **Customer (member)** | ✓ | ✕ | ✕ | ✕ |
| **Store manager / staff (employee)** | ✓ | ✓ | ✕ | ✕ |
| **Physical store (POS store)** | ✓ | ✓ | ✓ | ✓ |

For each type of partner, you can set how they get their code and how they check their results:

| Partner | How to get the Referral Code | How to check results |
| :--- | :--- | :--- |
| **Third party (influencer / group-buy organizer)** | Provided by the merchant | Merchant provides a dedicated Report Link |
> | **Customer (member)** | Storefront: Member Center Personal Info  | Storefront: Member Center > Personal Info |
> | **Store manager / staff (employee)** | Admin: Profit Sharing Referral Search | Admin: Profit Sharing > Referral Reports |
> | **Physical store (POS store)** | Admin: Profit Sharing Referral Search | Admin: Profit Sharing > Referral Reports |

!!! warning "POS compatibility"
    Store profit sharing only works with the CYBERBIZ POS system. If you use another system, contact our consultants to evaluate switching.


## Core Rules And Limits

Before you plan your profit-sharing programs, make sure you understand how the system works:

### 1. When Rewards Are Settled
- The system calculates profit-sharing amounts and issues bonus rewards only when the order status changes to **Completed**.
- If an order is returned or canceled after it's completed, the system **does not** automatically add or take back bonuses that were already issued.

### 2. How Payments Are Handled
- The CYBERBIZ admin only provides **profit-sharing reports** for reference. The system **does not handle** actual cash payouts.
- Using the report data, you pay partners yourself by offline payment, bank transfer, or system bonus points.

### 3. Effective Period
- An order qualifies for profit sharing only if it's placed within the plan's **effective period**.



## Next Steps

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }
  [__Set up referrer profit sharing__](referrer-profit-sharing.md)<br>
  Learn how to create plans, link influencers or members, and set up discounts.

- :lucide-users:{ .lg }
  [__Set up registrant profit sharing__](registrant-profit-sharing.md)<br>
  Learn how to set up permanent registrant links for long-term business development.

- :lucide-bar-chart-3:{ .lg }
  [__Export profit-sharing reports__](export-profit-sharing-reports.md)<br>
  Learn how to export profit-sharing data to pay rewards and review performance.

- :lucide-file-search:{ .lg }
  [__Look up profit-sharing data__](query-profit-sharing-partners-and-codes.md)<br>
  Learn how to look up your profit-sharing partners and their data, so you can check sales records accurately.

</div>


