---
title: "Free Shipping Coupon Specs"
description: "Learn about CYBERBIZ free shipping coupon specs, how to create them, and how they work at checkout."
created: 2026-06-17 10:39
last_modified: 2026-06-17 10:39
lang: en-US
type: reference
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
    - EC
modules: 
    - Marketing
sites: 
    - TW
audiences: 
    - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents: 
    - 瞭解免運券規格
    - 設定免運券
    - 處理免運券結帳問題
features: 
    - "Free Shipping Coupon"
    - coupon
    - 紅利商城
prerequisites:
  - ec/marketing/coupon/setup-coupons.en/
  - ec/marketing/coupon/setup-promo-codes.en/
related:
  - ec/members/manage-member-profiles.en/
  - ec/marketing/coupon/setup-promo-codes.en/
tags: 
    - 免運券
    - 優惠券
    - 行銷活動
    - "Shipping Fee Discount"
acoiv: configure
apis: []
devices: 
    - desktop
    - mobile
ui_components: 
    - 結帳頁面
    - 優惠券輸入框
paths: 
    - 行銷活動 > 優惠券
layouts: []
wp_url: 
    - https://www.cyberbiz.io/helpcenter/?p=7960
    - https://www.cyberbiz.io/support/?p=28947
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/free-shipping-coupon-spec.en/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---
# Free Shipping Coupon Specs
Learn about CYBERBIZ free shipping coupon specs, how to create them, and how they work at checkout.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

## Before You Start

- **Editing restriction**: You can't edit a free shipping coupon after you save it. To change it, delete it and create a new one.
- **Bonus Mall eligibility**: Free shipping coupons used in the Bonus Mall ignore the coupon's minimum spend and always cover the shipping fee.

## Create A Free Shipping Coupon

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__Send coupon from the Member List__](../../members/manage-member-profiles.md#2-優惠券派發與管理)
    Use member filters to send coupons in bulk.

- :lucide-hash:{ .lg }
    [__Create a Gift Promo Code__](setup-promo-codes.md)
    Create a store-wide promo code that isn't tied to a member account. Members get free shipping when they enter the code at checkout.


</div>


## Checkout Flow

1. On the checkout page, the customer clicks "Select coupon or Enter Promo Code."

    ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定03.png){ .screenshot }

2. If a store-wide promo code and a personal coupon have the same code, the system applies the **personal coupon** first.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼08.png){ .screenshot }

3. Before a free shipping coupon is applied, the original shipping fee is shown.

    - Select or enter the free shipping coupon code.
    - After it's applied, the shipping fee field changes to **(Free shipping by coupon)**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/免運券05.png){ .screenshot }

