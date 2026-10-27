---
title: "Understand Coupon And Promo Codes"
description: "Helps merchants tell coupon and promo codes apart, including how each is defined, sent, and used, so you can choose the right marketing tool."
created: 2026-06-11 12:20
last_modified: 2026-06-22 11:15
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules:
  - 行銷活動
  - 金物流
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 了解優惠券與優惠碼的差異
  - 選擇合適的行銷工具
features: 
  - coupon
  - "Promo Code"
prerequisites: []
related:
  - ec/marketing/bonus-and-gifts/setup-registration-gift.en/
  - ec/marketing/bonus-and-gifts/setup-birthday-gift.en/
  - ec/marketing/bonus-and-gifts/limited-time-first-purchase-gift.en/
  - ec/marketing/other-tools/interactive-games.en/
  - ec/marketing/conditional-send/send-coupons-for-specific-products.en/
  - ec/marketing/coupon/setup-coupons.en/
  - ec/marketing/coupon/setup-promo-codes.en/
  - ec/marketing/coupon/free-shipping-coupon-spec.en/
  - ec/marketing/coupon/gift-coupon-spec.en/
  - ec/marketing/purchase-restrictions/coupon-and-bonus-points-expiry-notification.en/
  - ec/marketing/coupon/multiple-coupons.en/
tags: 
  - 優惠券
  - 優惠碼
  - "Marketing Tools"
acoiv: configure
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 結帳頁面
  - 會員中心
paths:
  - 金物流 > 結帳頁 & 物流設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/marketing/coupon.en/"
search:
  exclude: false
icon: lucide/split
hide: []
---

# Understand Coupons And Promo Codes
Helps merchants choose between account-linked coupons and general promo codes based on their business needs.
{ .subtitle }

## Overview

coupons and promo codes are the core discount tools for online store promotions. **Promo codes are a type of coupon.** Both have the same priority at checkout and can be used to reduce the order amount.

- coupons let you add discounts directly to specific member accounts.
- Promo codes let you share one general code widely.


## Key Differences

The table below shows the main differences between coupons and promo codes in how they work and how they're used:

| Item | coupon | Promo Code |
| :--- | :--- | :--- |
| **Type** | **Account-linked** (tied to a member account) | **General** (not tied to an account) |
| **Visibility** | Members can see them in **會員中心 > 專屬優惠券** | Not shown in the member center. You share it with customers |
| **How it's sent** | automatically sent by the system or sent manually to accounts by you | You provide a code and customers enter it |
| **How it's used** | Select it from the **Available Offers** list at checkout | Enter the correct **promo code** manually at checkout |


## Use Cases

### Coupon

- **Automated rewards**: Use supported promotions to send coupons at key moments, such as sign-up, birthdays, or first purchases.

    <div class="grid cards" markdown>

    - :lucide-user-plus:{ .lg }
      [__registration gift__](../bonus-and-gifts/setup-registration-gift.md)
      automatically sent when a customer signs up as a member.

    - :lucide-cake:{ .lg }
      [__birthday gift__](../bonus-and-gifts/setup-birthday-gift.md)
      Automatically send an exclusive discount in the member's birthday month.

    - :lucide-shopping-cart:{ .lg }
      [__first-purchase gift__](../bonus-and-gifts/limited-time-first-purchase-gift.md)
      Reward customers who complete their first order.

    - :lucide-gamepad-2:{ .lg }
      [__Interactive Games__](../other-tools/interactive-games.md)
      Give out prizes through games such as spin wheels and red envelopes.

    - :lucide-package-plus:{ .lg }
      [__Send coupons for Specific Products__](../conditional-send/send-coupons-for-specific-products.md)
      Automatically send a coupon after a customer buys specific products.

    </div>

- **Targeted rewards**: Send exclusive reward coupons to a specific list of members.

    <div class="grid cards" markdown>

    - :lucide-ticket:{ .lg }
      [__Set Up coupons__](setup-coupons.md)
      Learn how to create account-linked coupons and set sending conditions.

    </div>

### Promo Codes

- **General promo codes**: Valid store-wide for anyone. Customers simply enter the code on the checkout page to get the discount.

    <div class="grid cards" markdown>

    - :lucide-hash:{ .lg }
      [__Set Up Promo Codes__](setup-promo-codes.md)
      Learn how to generate promo codes and set usage limits.

    </div>


## Coupon Specs By Type

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__Free Shipping Coupon Specs__](free-shipping-coupon-spec.md)
    Learn the limits of free shipping coupons and how checkout works.

- :lucide-hash:{ .lg }
    [__Gift Coupon Specs__](gift-coupon-spec.md)
    Learn the limits of gift coupons and their inventory rules.

</div>

## Checkout Order

coupons and promo codes are applied in the same order: after discount promotions, upsells, and threshold gifts. If a coupon (code) has a minimum spend, the order must still meet it after those discounts.

![](https://www.cyberbiz.io/support/wp-content/uploads/2020/03/結帳順序-優惠券.png){ .screenshot }

## Turn On Coupons (Codes) At Checkout

To let customers use coupons (codes) at checkout, turn on the storefront display switch first.

1. Log in to the CYBERBIZ admin and go to **Payment and Logistics > Checkout Page & Logistics**.
2. Find the **Coupon setting for checkout page** section and switch the feature to `開啟`.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼13.png){ .screenshot }


## Shared Coupon (Code) Settings

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }
  [__coupon (Code) and bonus points Expiry Notifications__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.md)
  Set up email, SMS, or LINE notifications automatically sent by the system to remind customers to use expiring coupons and bonus points.

- :lucide-hash:{ .lg }
  [__Multiple coupons (Codes)__](multiple-coupons.md)
  Set the maximum number of coupons (codes) per order and learn how multiple discounts are calculated.

</div>



## FAQ

??? quote "Why do members say they can't see the promo code I published?"
    Promo codes aren't linked to accounts, so the system doesn't show them in the member center. Share the code with customers by email, SMS, store banners, or social media.
