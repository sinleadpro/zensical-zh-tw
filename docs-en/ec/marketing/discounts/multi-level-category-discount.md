---
title: "Set Up Multi-Level Category Threshold Discounts"
description: "Set up threshold discounts for multi-level product categories. When an order qualifies, the discount applies to each item in the category separately."
created: 2024-05-23 00:00
last_modified: 2026-08-28 17:40
lang: en-US
type: guide
author: ""
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - Marketing
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 如何設定商品多層級分類滿額折扣
  - 分類優惠門檻設定
features:
  - 商品多層級分類滿額折扣
  - "Multi-Level Product Categories"
prerequisites:
  - ec/products/categories-and-tags/multi-level-category-setup.en/
related:
  - ec/products/categories-and-tags/multi-level-category-setup.en/
tags:
  - 行銷活動
  - 商品多層級分類
  - "Threshold Discount"
  - Discount
  - Promotions
  - "Ecommerce Marketing"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 商品多層級分類滿額折扣
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=9212
  - https://www.cyberbiz.io/support/?p=43281
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/multi-level-category-discount.en/"
comments: false
search:
  exclude: false
icon: lucide/layers
hide: []
---
# Set Up Multi-Level Category Threshold Discounts
Set up threshold discounts for multi-level product categories. When an order qualifies, the discount applies to each item in the category separately.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    On PLUS plans, Multi-Level Category Threshold Discounts is an add-on module (choose 2 of 11). Make sure you've selected this module before using it. The Enterprise plan includes it by default.

![Multi-Level Category Threshold Discounts](../../../assets/images/ec-marketing-product-multi-level-full-discount-hero.zh-tw.png){ title="商品多層級分類滿額折扣" .hero-page }

## About Multi-Level Category Threshold Discounts

Multi-Level Category Threshold Discounts is a **promotion applied by product category level**. You link a discount to a **top-level or mid-level category**. When the amount of products from that category in an order reaches the threshold, the system **applies the discount to each item** in the category.
!!! note "Category Levels"

	- **Large Category**: The highest level in the multi-level category structure, used to group products broadly.
	- **Medium Category**: Sits under a top-level category to break products down further.
	- **Sub-category**: The lowest level, mapped to the actual product source (custom collection, smart collection, or product type).


### Prerequisites

- [x] Finish **Multi-level Product Categories Setting** before you create a multi-level category threshold discount. Learn [how to set up multi-level product categories](../../products/categories-and-tags/multi-level-category-setup.md).

---

### Before You Start

- **Discount order**: Within one order, discounts are applied by **priority value**. Higher values are calculated first.
- **Category stacking**: If you add a **top-level category** and its **mid-level or sub-categories** to the same promotion, the discount is **counted only once**.
- **How the discount is calculated**: **Discount per item × number of qualifying items**, not a single discount for the whole order.
- **Calculation basis**: The spending threshold is based on the **original order price**.

---

### Discount Example

- Promotion: Spend **NT$1,000 on products in the category, get NT$30 off each item**
- Qualifying items in the order: 3
- Calculation: `30 × 3 = 90 元`

!!! info "The discount applies to each qualifying item."

## Steps

### Add A Category Promotion

1. Log in to the CYBERBIZ admin and go to **Marketing > Product Multi Level Filter Full Discount**.
2. Click **Add Category Campaign** and enter a promotion name.

---

### Add Categories To The Promotion

1. Select the **top-level or mid-level categories** to discount.
2. Click **Add Categories to Campaign**.
3. Added categories appear in the **Selected Categories** list. Click :lucide-x: to remove a category.

![Add Categories to the Promotion](../../../assets/images/ec-product-multi-level-full-discount-select-categories.zh-tw.gif){ title="選擇分類加入活動" }

---

### Set The Promotion Details And Period

Go to the **Campaign Settings** tab and set the following:

- **Enable Category Promotion**: Choose whether the promotion is on. **If it's off, no discount applies at checkout.**
- **Campaign Title**: Enter a name that's easy to recognize.
- **Discount Type**: Choose **Amount Discount** or **Percentage Discount**. The discount applies to **each qualifying item**.
- **Minimum Spend**: The order must reach this amount for the discount to apply.
- **Campaign Priority Weight**: Higher values are applied first.
- **Start/End Time**: Set the promotion period. The discount ends automatically when the promotion ends.

### What Customers See

Once the promotion is active, customers see the discount for qualifying products at checkout.

![Storefront Discount Display](../../../assets/images/ec-multi-level-product-full-discount-frontend.zh-tw.png){ title="前台折扣顯示" }

## FAQ

??? quote "Can the discount be applied twice?"
    No. Even if you add a top-level category and its sub-categories to the promotion, the discount is counted only once.

??? quote "Does the discount apply to the whole order or to each item?"
    The discount applies to **each qualifying item**. Total order discount = discount per item × number of items.
