---
title: "Set Up Product Not Applicable To Selected Promotion"
description: "Exclude specific products from promotions such as store-wide promotions, coupon, multi-level category threshold discounts, and VIP discounts."
created: 2026-01-13 00:00
last_modified: 2026-06-30 10:56
lang: en-US
permalink: "https://help.cyberbiz.io/ec/marketing/purchase-restrictions/exclude-products-from-promotions.en/"
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
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
  - Professional
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 如何設定商品排除指定優惠
  - 商品排除優惠設定
features:
  - 商品排除指定優惠
prerequisites: []
related: []
tags:
  - "Product Collections"
  - "Single-Product Discount"
  - "Flash Sale"
  - 行銷活動
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 商品排除指定優惠
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8058
  - https://www.cyberbiz.io/support/?p=3623
comments: false
search:
  exclude: false
icon: lucide/ban
hide: []
---

![Product Not Applicable to Selected Promotion](../../../assets/images/ec-marketing-product-not-applicable-to-select-promotion.zh-tw.png){ title="商品排除指定優惠" .hero-page }

## About Product Not Applicable To Selected Promotion

Exclude products from specific promotions to avoid double discounts and protect your margins. You can exclude products from store-wide discount, coupons, multi-level category threshold discounts, and VIP discounts.

!!! example "Use Cases"

    - **Avoid double discounts**: Exclude products that already have their own promotion from other store-wide offers to protect margins.
    - **Manage special products**: Keep high-priced, limited, or special products out of general promotions to protect brand value and exclusivity.
    - **Targeted marketing**: Adjust exclusions by product attributes or sales goals to make better use of your marketing budget.
    - **POS-exclusive products**: Make sure in-store-only products aren't affected by online offers.

---

### Promotion Types You Can Exclude

Add products to the matching "Not Applicable to Discount" Collections to keep them out of these promotions:

- **store-wide discount promotions**: Excludes all store-wide price discounts and stacked bonus points or coupons.
- **coupons and promo codes**: Excludes all coupons, promo codes, and coupons sent by other promotions.
>  The system also excludes coupons sent through promotions such as first-purchase gift, Interactive Games, and Send coupons for Specific Products.

- **Multi-level category threshold discounts**: Excludes threshold discounts calculated by product category or level.
- **VIP member discounts**: Excludes exclusive discounts based on member tier.

!!! info "For POS-Exclusive Products"
    This feature also supports merchants with POS-exclusive products, so in-store-only products aren't affected by online promotions.

<!--
## Related Settings

<div class="grid cards" markdown>

- :lucide-tag:{ .lg }
  [__store-wide discount Promotions__](../discounts/storewide-discounts.md)
  Exclude products from the store-wide discount and stacked offers set in "store-wide discount - Bonus & coupon."

- :lucide-percent:{ .lg }
  [__Promo Codes / coupon__](../coupon/setup-promo-codes.md){ title="設定優惠碼" }
  Exclude products from promo code and coupon promotions, including first-purchase gift, Interactive Games, and Send coupons for Specific Products.

- :lucide-clock:{ .lg }
  [__limited-time first-purchase gift__](../bonus-and-gifts/limited-time-first-purchase-gift.md)
  Exclude products from the limited-time first-purchase gift promotion.

- :lucide-gamepad:{ .lg }
  [__Interactive Games__](../other-tools/interactive-games.md)
  Exclude products from coupons sent by interactive games.

- :lucide-list-check:{ .lg }
  [__Multi-Level Category Threshold Discounts__](../discounts/multi-level-category-discount.md){ title="設定商品多層級分類滿額折扣" }
  Exclude products from multi-level category threshold discounts.

- :lucide-crown:{ .lg }
  [__VIP Offers__](../../members/vip/setup-exclusive-vip-discounts.md.md)
  Exclude products from member-exclusive discounts.

</div>

-->

---

### How Exclusion Works

After you exclude a product from selected promotions, the checkout page shows a notice based on your settings, and the product isn't included in the excluded promotions.

![Storefront Exclusion Notice](../../../assets/images/ec-product-not-applicable-to-select-promotion-frontend.zh-tw.png){ title="前台排除優惠顯示" }

## Steps

Follow these steps to exclude products from specific promotions:

1. Log in to the CYBERBIZ admin and go to **Marketing > Product Not Applicable to Selected Promotion**.
2. In the Collections list, find the "Not Applicable to Discount" Collections you want and click to expand the Collections details.
3. In the product list on the left, select the products to exclude and click **Add** or **Remove**:

    - A product can be in more than one "Not Applicable to Discount" Collections.
    - Products already added are skipped and won't be added twice.

4. After adding products, you can set a schedule (start/end date) for each product in the Collections.

![Product Exclusion Settings](../../../assets/images/ec-marketing-product-not-applicable-to-select-promotion-setting.zh-tw.png){ title="商品排除優惠設定" }

## FAQ

??? quote "Can a product be in more than one Not Applicable to Discount Collections?"
    Yes. A product can be in several Not Applicable to Discount Collections at once, for example to exclude it from both store-wide promotions and coupons.

??? quote "Can customers still buy a product after it's excluded from promotions?"
    Yes. This feature only keeps the product out of specific promotions. It doesn't affect how the product is shown or sold in your Shop.
