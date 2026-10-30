---
title: "Order Report Fields"
description: "Complete list of fields available in the order report, covering product discount breakdowns, referral source platforms, and UTM parameters, to help you export and read order reports."
created: "2026-03-15 16:58"
last_modified: 2026-06-02 13:47
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: ""
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 查看訂單報表欄位
  - 了解折扣種類說明
  - 認識導購來源
  - 查看UTM參數說明
features:
  - 折扣拆分
  - 導購來源
  - UTM 參數
prerequisites: []
related: []
tags:
  - "Order Reports"
  - "Discount Fields"
  - "Referral Sources"
  - "UTM Parameters"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 訂單報表匯出
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/order-report-fields/"
comments: false
search:
  exclude: false
icon: lucide/table
hide: []
---
## Order Discount Breakdown


| Product Discount Field | Description | Notes |
| :--- | :--- | :--- |
| Total product mix-and-match discount | Total discount from "Any X items for Y% off" or "Mix-and-match spend threshold" promotions | |
| Product store-wide discount amount | Discount allocated from store-wide promotions (such as store-wide 10% off) | |
| Total product VIP discount | Discount from offers set by membership tier (VIP/VVIP) | |
| Total product coupon discount | Amount allocated after the customer uses a coupon at checkout | |
| Total product bonus points discount | Amount the customer redeemed with bonus points | |
| Total product manager price change discount | Difference from prices changed manually by store staff at checkout | **POS only** |
| Total product single-item discount | Difference between the sale price set directly for a product and its original price | |
| Total product bundle discount | Discount from "bundle (A+B)" promotions | |
| Total product category discount | Spend or quantity threshold discounts set for specific categories (including multi-tier) | |
| Total product third-party discount | Exclusive discounts from integrated external platforms (such as LINE Shopping) | |
| Total product game discount | Discounts won through interactive marketing games (such as spin wheels and scratch cards) | |
| Total product member-exclusive price discount | Difference between a "fixed exclusive price" set for specific member groups and the original price | |


## Referral Source


| Third-Party Platform / Partner | Type | Description |
| :--- | :--- | :--- |
| **OmniSegment** | Marketing automation (MA) | Omnichannel member data integration and automated targeted marketing platform |
| **SOOCKER** | Conversational commerce | Traffic tool combining social referrals and conversational marketing |
| **Affiliates.One** | Affiliate marketing | Commission-based referral partnerships with bloggers, influencers, and other partners |
| **iChannels affiliate marketing platform** | Affiliate marketing | Large affiliate marketing platform in Taiwan with pay-for-performance promotion |
| **AviviD.ai** | AI marketing / push notifications | AI-predicted push notifications and automated traffic return solutions |
| **ShopBack** | Cashback platform | Traffic channel that attracts members with cashback rewards |
| **Ruten** | E-commerce platform sync | Integrates with Ruten for product sync and order management |
| **LINE Shopping** | Referral platform | Integrates with the LINE ecosystem, using points rewards to drive conversions |
| **Shop.com** | Partner store | Referral partnership with the Shop.com cashback program |


## UTM Parameters


| UTM Parameter | System Field | Description |
| :--- | :--- | :--- |
| **"UTM Source"** | `utm_source` | Traffic source platform, for example: google, facebook, newsletter |
| **"UTM Campaign Name"** | `utm_campaign` | Name of a specific promotion or product campaign, for example: spring_sale |
| **"UTM Medium"** | `utm_medium` | Type of marketing medium, for example: cpc, email, social |
| **"UTM Campaign Term"** | `utm_term` | Usually used for keyword ads to mark the search keyword |
| **"UTM Click Time"** | `utm_click_time` | Exact time the customer clicked the tracking link and entered the site |
| **"UTM Campaign Content"** | `utm_content` | Distinguishes different versions of the same link (A/B testing), for example: logolink, textlink |


## Bundle Price Difference

### Calculation Steps

1.  **Calculate the total price difference**: "Total original price of products" - "Bundle price"
2.  **Calculate the "bundle price difference"**: Calculate the discount per sub-product type.  

    1.  Allocate by original price ratio: "Total bundle price difference" × "Each sub-product's original price ratio."
    2.  Round down to a whole number. If any discount is left unallocated after rounding down, the system allocates it NT$1 at a time in sub-product order.

3.  **Calculate the "bundle price difference details"**: If a sub-product has a quantity greater than one, the item's total discount is further allocated to each unit.  

    1.  Allocate by quantity: "Bundle price difference" ÷ "Sub-product quantity."
    2.  Round down to a whole number. If any discount is left unallocated after rounding down, the system allocates it NT$1 at a time in sub-product order.


### Example 1: One Unit of Each Sub-Product

Suppose you create a bundle priced at NT$850 that includes these 3 sub-products:

- Sub-product A: original price NT$100
- Sub-product B: original price NT$300
- Sub-product C: original price NT$500

#### Calculation Steps

1. **Calculate the total price difference**

    The original total price of the sub-products is 100 + 300 + 500 = NT$900

    NT$900 (original total) − NT$850 (bundle price) = NT$50 (total price difference)

2. **Calculate the "bundle price difference"**

    1. **Allocate by ratio**

        - Sub-product A: 50 × [ 100 / 900 ] = NT$5.56 ➔ rounded down to NT$5
        - Sub-product B: 50 × [ 300 / 900 ] = NT$16.67 ➔ rounded down to NT$16
        - Sub-product C: 50 × [ 500 / 900 ] = NT$27.78 ➔ rounded down to NT$27

    2. **Allocate the remainder**

        Discount allocated so far: 5 + 16 + 27 = NT$48.

        The remaining unallocated discount is 50 − 48 = NT$2. Following the order A, B, C, add NT$1 to each:

        - Sub-product A: gets NT$1 ➔ final price difference is NT$6
        - Sub-product B: gets NT$1 ➔ final price difference is NT$17
        - Sub-product C: allocation complete ➔ final price difference stays NT$27

3. **Calculate the "bundle price difference details"**

    Each sub-product in the bundle has a quantity of 1, so the "price difference for the item type" equals the "discount per unit," and the system doesn't need to break it down further.

#### How It Appears in the Report

| Product Name | Bundle Price Difference | Bundle Price Difference Details |
| ------- | ---------- | ------------ |
| Sub-product A | 6 | [6] |
| Sub-product B | 17 | [17] |
| Sub-product C | 27 | [27] |

> This table shows only the fields relevant to the example; other report fields are omitted.

### Example 2: One Sub-Product with Multiple Units

Suppose you create a bundle priced at NT$777 that includes these 4 sub-product units:

- Sub-product A: original price NT$166 × 1 unit
- Sub-product B: original price NT$250 × 3 units (this sub-product has multiple units)

When a shopper buys 2 bundles, the calculation is as follows:

#### Calculation Steps

1. **Calculate the total price difference**

    Total bundle price = 777 × 2 = NT$1,554

    Original total per bundle = 166 + 250 × 3 = NT$916; original total for 2 bundles = 916 × 2 = NT$1,832

    NT$1,832 (original total for 2 bundles) − NT$1,554 (price for 2 bundles) = NT$278 (total price difference)

2. **Calculate the "bundle price difference"**

    1. **Allocate by ratio**

        - Sub-product A: 278 × [ (166 × 2) / 1,832 ] = NT$50.36 ➔ rounded down to NT$50
        - Sub-product B: 278 × [ (750 × 2) / 1,832 ] = NT$227.63 ➔ rounded down to NT$227

    2. **Allocate the remainder**

        Discount allocated so far: 50 + 227 = NT$277

        The remaining unallocated discount is 278 − 277 = NT$1. Allocate it in product order:

        - Sub-product A: gets NT$1 ➔ final total price difference is 50 + 1 = NT$51
        - Sub-product B: final total price difference stays NT$227 ➔ **the sub-product has multiple units, so the discount is further split per unit**

3. **Calculate the "bundle price difference details"**

    1. **Allocate by ratio**

        - Sub-product B-1: 227 ÷ 3 = NT$75.6 ➔ rounded down to NT$75
        - Sub-product B-2: 227 ÷ 3 = NT$75.6 ➔ rounded down to NT$75
        - Sub-product B-3: 227 ÷ 3 = NT$75.6 ➔ rounded down to NT$75

    2. **Allocate the remainder**

        Discount allocated so far: 75 + 75 + 75 = NT$225

        The remaining unallocated discount is 227 − 225 = NT$2. Allocate it in product order:

        - Sub-product B-1: gets NT$1 ➔ final price difference is 75 + 1 = NT$76
        - Sub-product B-2: gets NT$1 ➔ final price difference is 75 + 1 = NT$76
        - Sub-product B-3: allocation complete ➔ final price difference stays NT$75

#### How It Appears in the Report

| Product Name | Bundle Price Difference | Bundle Price Difference Details |
| ------- | ---------- | ------------ |
| Sub-product A | 51 | [51] |
| Sub-product B | 227 | [76,76,75] |

> This table shows only the fields relevant to the example; other report fields are omitted.