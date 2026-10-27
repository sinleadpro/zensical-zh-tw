---
title: "Guide To Stacking Multiple Coupons (Codes)"
description: "Let a single order use multiple coupons or promo codes, including setting the maximum number, discount calculation examples, and the storefront flow."
created: 2026-05-27 18:04
last_modified: 2026-07-29 14:30
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
  - 金物流
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents: 
  - 設定單筆訂單使用多張優惠券
  - 了解多張優惠券折抵邏輯
  - 提高顧客客單價
features: 
  - 多張優惠券併用
  - 優惠碼併用
  - 結帳頁優惠券設定
prerequisites: []
related: []
tags: 
  - coupon
  - "Promo Code"
  - Stacking
  - "Checkout Settings"
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: []
paths:
  - 金物流 > 結帳頁 & 物流設定 > 結帳頁優惠券設定
  - 金物流 > 結帳頁 & 物流設定 > POS 結帳頁優惠券設定
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=37637
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/multiple-coupons.en/"
comments: false
search:
  exclude: false
icon: lucide/tickets
hide: []
---

# Guide To Stacking Multiple Coupons
 Let a single order use multiple coupons or promo codes, including setting the maximum number, discount calculation examples, and the storefront flow.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品){ title="圖示慣例" } | Online Store
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Expert PLUS / Enterprise <br>
[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品){ title="圖示慣例" } | Smart POS
{ .doc-badge }

## Before You Start

- **Channels**: Stacking multiple coupons works on both the **EC online store** and the **POS system**. Set the maximum number separately for each channel.
- **Stacking rules**: Stacking multiple coupons doesn't change how they combine with bonus points or other promotions.


## Steps

=== "EC"

    1. Go to **Payment and Logistics > Checkout Page & Logistics > 結帳頁優惠券設定**.
    2. Set the **maximum number of coupons/codes per order**.

        > This number is the combined total of coupons and promo codes. You can't set separate limits for each.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定01.png){ .screenshot }

=== "POS"

    1. Go to **Payment and Logistics > Checkout Page & Logistics > POS 結帳頁優惠券設定**.
    2. Set the **maximum number of coupons/codes per order**.

        > This number is the combined total of coupons and promo codes. You can't set separate limits for each.

        ![](../../../assets/images/EC-後台-金物流-結帳頁物流設定-pos多張優惠券設定01.png){ .screenshot }

## How Multiple Coupons Are Calculated

When an order uses multiple coupons, the system calculates the discount with these rules:

| Rule | Description | Example |
| :--- | :--- | :--- |
| **Calculation order** | Fixed amounts are deducted first, then percentage discounts | A NT$100 order with "80% of list price" and "NT$20 off" is calculated as `(100-20) x 0.8 = 64` |
| **Threshold check** | Thresholds are based on the order amount before discounts | A NT$1500 order can use three coupons with thresholds of NT$1000, NT$900, and NT$800 |
| **Tag restriction** | A coupon linked to a tag only discounts products with that tag | If the cart has regular product A and tagged product B, the tag coupon only discounts product B |

!!! example "Example: Stacking Multiple coupons"
    **Scenario:**

    - Cart: Product A (NT$1000, regular product) and Product B (NT$500, linked to `特定標籤`)
    - coupons held:
        1. **Store-wide coupon**: NT$50 off
        2. **Personal tag coupon**: 90% of list price (`特定標籤` only)
        3. **Store-wide tag coupon**: 73% of list price (`特定標籤` only)

    **Calculation:**

    1. **Apply the store-wide coupon (NT$50)**: Split by product price. Product A gets NT$34 off and Product B gets NT$16 off.
    2. **Apply the personal tag coupon (90% of list price)**: Applies only to Product B's remaining amount: (500 - 16) × 10% = NT$48.
    3. **Apply the store-wide tag coupon (73% of list price)**: Applies only to Product B's remaining amount: (500 - 16 - 48) × 27% = NT$117.

    **Result:**

    - **Product A**: NT$34 off in total.
    - **Product B**: 16 + 48 + 117 = NT$181 off in total.

## Checkout On The Storefront


=== "EC"

    1. On the checkout page, the customer clicks **Select coupon or Enter Promo Code**.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定03.png){ .screenshot }

    2. The pop-up shows the member's personal coupons by default (sorted by expiry date).

        ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定04.png){ .screenshot }

    3. The customer can select multiple coupons. Once the limit is reached, the other options can't be selected.
    4. After applying, the customer sees each coupon's discount right away and can change or Remove coupons at any time.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定05.png){ .screenshot }


=== "POS"

    1. On the checkout page, the staff member clicks **Select Promo Code**.

        ![](../../../assets/images/POS-前台-結帳-多優惠券01.png){ .screenshot }

    2. The pop-up shows the **store coupon** list by default.

        ![](../../../assets/images/POS-前台-結帳-多優惠券02.png){ .screenshot }

    3. The staff member can select multiple coupons. Once the limit is reached, the other options can't be selected.

        > Switch to the **Selected coupons** tab to see the coupons currently selected.

        ![](../../../assets/images/POS-前台-結帳-多優惠券03.png){ .screenshot }

    4. Confirm and apply to see each coupon's discount right away. Coupons can be changed or canceled at any time.

        ![](../../../assets/images/POS-前台-結帳-多優惠券04.png){ .screenshot }