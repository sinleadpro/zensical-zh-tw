---
title: "Gift Coupon Specs"
description: "Learn about CYBERBIZ gift coupon specs, product restrictions, how to create them, and how they work at checkout."
created: 2026-06-17 10:39
last_modified: 2026-07-06 17:00
lang: en-US
type: reference
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - WMS
modules:
  - 行銷活動
  - 會員
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
    - 瞭解贈品券規格
    - 設定贈品券
    - 處理贈品券庫存問題
features: 
    - "Gift Coupon"
    - coupon
    - 庫存管理
prerequisites:
  - ec/marketing/coupon/setup-coupons.en/
  - ec/marketing/coupon/setup-promo-codes.en/
related:
  - ec/members/manage-member-profiles.en/
  - ec/marketing/other-tools/interactive-games.en/
  - ec/marketing/coupon/setup-promo-codes.en/
  - ec/members/vip/setup-exclusive-vip-discounts.en/
tags:
    - 贈品券
    - 優惠券
    - Marketing
    - "Gift per"
acoiv: configure
apis: []
devices: 
    - desktop
    - mobile
ui_components:
    - 結帳頁面
    - 優惠券輸入框
paths: 
    - 行銷活動 > 優惠券設定
    - 會員 > 所有會員
layouts: []
wp_url: 
    - https://www.cyberbiz.io/support/?p=41796
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/gift-coupon-spec.en/"
comments: false
search:
  exclude: false
icon: lucide/gift
hide: []
---
# Gift Coupon Specs
Learn about CYBERBIZ gift coupon specs, product restrictions, how to create them, and how they work at checkout.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    - On PLUS plans, gift coupons are an add-on module (choose 2 of 11). Confirm that you've selected this module before using it. The Enterprise plan includes it by default.

## Before You Start

- **Product restriction**: Gift coupons don't support combo products.
- **Listing restriction**: Gift coupons can only be linked to regular products that are listed.
- **Unlisting**: If the linked product is unlisted, the gift coupon becomes invalid and is unlisted too. Customers can't find, view, or redeem it in the storefront cart.
- **Channel restriction**: Gift coupons don't support POS, subscriptions, or CYBERBIZ NOW! fast delivery.
- **Warehouse integration**: For merchants with an integrated warehouse, the gift product must have a SKU (per gift coupon), or the coupon can't be applied.
- **API integration**:
    - Gift coupons appear in the order items from the API and webhooks.
    - You can add gift coupons through the API.

        > Gift coupons sent for VIP birthday gifts, Upgrade gifts, or member days can't be added through the API.

- **Empty cart**: A cart that contains only gift coupon items isn't supported. If the cart has no regular paid products, the system treats it as empty and checkout can't continue.


## Create A Gift Coupon

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__Send coupons from the Member List__](../../members/manage-member-profiles.md#2-優惠券派發與管理)
    Use member filters to send coupons in bulk.

- :lucide-hash:{ .lg }
    [__Send coupons with Interactive Games__](../other-tools/interactive-games.md)
    Create an interactive game and give out gift coupons through a spin wheel or prize draw.

- :lucide-hash:{ .lg }
    [__Create a Gift Promo Code__](setup-promo-codes.md)
    Create a store-wide promo code that isn't tied to a member account. Members get a gift when they enter the code at checkout.

- :lucide-hash:{ .lg }
    [__Create VIP Offers__](../../members/vip/setup-exclusive-vip-discounts/)
    Send gift coupons for VIP birthdays, Upgrades, or member days.


</div>


## Gift Coupon Rules

### Inventory Check Order

When an order is placed, the system checks inventory in this order. If the gift coupon product is out of stock, the customer is asked to remove the coupon before checking out:

1. Combo products
2. Regular products
3. first-purchase gift products
4. Threshold or quantity gift products
5. **Gift coupon products**

### Analytics

Gift coupons are a type of coupon. You can see their performance in **圖表分析 > Marketing Campaign Analysis > 優惠券分析** in the admin. Gift coupons sent from the member list are counted as "member-exclusive coupons."

### Special Cases

1. **Coupon no longer applies**: If the customer refreshes the cart, updates cart items, or the gift runs out of stock after the coupon is applied, the coupon may fail or show an error. The customer needs to remove the coupon and check out again.
2. **Minimum spend**: Even if the gift coupon threshold is NT$0, the cart must contain at least one regular (non-gift) product. If the cart is empty, the customer is sent back to the home page or member page.
3. **Threshold vs. inventory**: If the order both misses the spending threshold and the gift is out of stock, the system checks the threshold first.

## Checkout Flow

1. On the checkout page, the customer clicks "Select coupon or Enter Promo Code."

    ![](https://www.cyberbiz.io/support/wp-content/uploads/優惠券-多張優惠券設定03.png){ .screenshot }

2. If a store-wide promo code and a personal coupon have the same code, the system applies the **personal coupon** first.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼08.png){ .screenshot }

3. If the gift is in stock, the customer can choose to apply the gift coupon.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠碼09.png){ .screenshot }


## FAQ

??? quote "Why can't I apply my gift coupon?"
    Check the following:
    1. Is the gift product in stock?
    2. Does the gift product have a SKU (for merchants with an integrated warehouse)?
    3. Are there other products in the cart? (The cart can't contain only gifts.)