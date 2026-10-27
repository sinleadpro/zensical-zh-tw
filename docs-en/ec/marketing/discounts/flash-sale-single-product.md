---
title: "Set Up Single-Product Flash Sale Collections"
description: "Create Single-Product Flash Sale Collections and set the pricing method (fixed amount, percentage, or sale price), the products, and the valid period."
created: 2026-01-13 00:00
last_modified: 2026-06-30 10:56
lang: en-US
type: guide
author: ""
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
  - 商品
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
  - 如何設定單品限時折扣群組
  - 單品折扣設定
features:
  - 單品限時折扣
  - "Product Collections"
prerequisites: []
related:
  - ec/marketing/discounts/checkout-discount-calculation-order.en/
  - ec/products/categories-and-tags/custom-collections.en/
  - ec/marketing/purchase-restrictions/exclude-products-from-promotions.en/
tags:
  - 商品群組
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
  - 行銷活動 > 單品限時折扣
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=9101
  - https://www.cyberbiz.io/support/?p=3368
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/flash-sale-single-product.en/"
comments: false
search:
  exclude: false
icon: lucide/clock
hide: []
---
# Set Up Single-Product Flash Sale Collections
Create Single-Product Flash Sale Collections and set the pricing method (fixed amount, percentage, or sale price), the products, and the valid period.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    On PLUS plans, Single-Product Flash Sale Collections is part of the Marketing A add-on module (choose 2 of 11). Make sure you've selected this module before using it. The Enterprise plan includes it by default.



![Single-Product Flash Sale Collections](../../../assets/images/ec-marketing-flash-sale-single-product-hero.zh-tw.png){ title="單品限時折扣群組" .hero-page }

## About Single-Product Flash Sales

A single-product flash sale discounts the product itself. You can apply a sale price to selected products for a set period. The discount applies only during the promotion, and prices return to normal automatically when it ends.

### Features And Benefits

- **Discount specific products**: Only the selected products are affected. Other prices stay the same.
- **Runs automatically**: Set your own start and end times. Prices return to normal when the promotion ends.
- **Boost conversion**: Limited-time offers encourage customers to order quickly or buy more.

!!! example "Use Cases"

    - **Short-term promotions**: Run a limited-time offer on specific products.
    - **Clearance**: Discount slow-moving products to turn inventory faster.
    - **New product launches**: Offer a short-term discount on new products to build early sales and attention.

## Set Up Single-Product Flash Sale Collections

### Add Single Product Discount Collections

1. Log in to the CYBERBIZ admin and go to **Marketing > Flash Sale for Single Product**.
2. Below the Collections list, enter a new Collections Name and click **Add a new collection**.

---

### Fill In The Collections Details

In the Collections list, click the Collections to expand it and set these fields:

- **Collections Name**: Used to identify and manage this discount.
- **Collections Start/End Date**: Set when the promotion is valid.
- **Pricing Rule**: Choose the pricing Type for the discount:

	- **Fixed price for any item**: Set a fixed price per item during the promotion.
    > Example: A product is NT$300. With a fixed price of NT$100 per item, buying 3 costs NT$300 at checkout.
	- **Percentage of list price for any item**: The price is calculated at the set percentage.
    > Example: A product is NT$100. At 80%, buying 1 costs NT$80 at checkout.
    - **Fixed amount off any item**: Each item is discounted by a set amount.
    > Example: A product is NT$100. With NT$20 off each item, buying 3 costs NT$240 at checkout.

- **Discount Value**: Enter the value for the pricing method you chose, such as a percentage or a fixed amount.

![Single-Product Flash Sale Collections Settings](../../../assets/images/ec-marketing-flash-sale-single-product-collection-setting.zh-tw.png){ title="單品限時折扣群組設定" }

---

### Add Products To The Collections

There are two ways to add products to the discount Collections:

**Add manually**

1. Expand the discount Collections.
2. In the product list on the left, click **Add** to add products or variants to the Collections.
3. Check the product list and order in the Collections.


**Bulk import** (for many products)

1. Download **Single_Product_Discount_Collection_Example.xlsx**.
2. Fill in the product details using the template, including product Name, variant, and discount settings.
3. Upload the completed Excel file. The system imports the products into the Collections automatically.

!!! warning "Import Notes"

	- Keep the Excel file in the same format as the template to avoid import errors.
    - The Collections Name must exactly match the Name of an existing discount Collections.

![Single-Product Discount Bulk Import](../../../assets/images/ec-marketing-flash-sale-porduct-excel-import.zh-tw.png){ title="單品折扣批次匯入" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-list-ordered:{ .lg }
  [__Checkout Discount Calculation Order__](checkout-discount-calculation-order.md)
  The order in which promotions are applied at checkout.
- :lucide-group:{ .lg }
  [__Custom Product Collections__](../../products/categories-and-tags/custom-collections.md)
  Create custom product category Collections.
- :lucide-ban:{ .lg }
  [__Exclude Products from Promotions__](../purchase-restrictions/exclude-products-from-promotions.md)
  Exclude specific products from specific promotions.


</div>
