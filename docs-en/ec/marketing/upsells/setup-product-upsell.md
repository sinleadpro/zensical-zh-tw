---
title: "Set Up Product Upsells"
description: "Set prices for product upsells and multi-variant add-on items, and the storefront Show rules."
created: 2026-01-12 00:00
last_modified: 2026-06-30 10:56
lang: en-US
type: guide
author: Jase
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
  - Advanced
  - Expert
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 如何設定商品加價購
  - 商品加價購設定
features:
  - "Product Upsell"
prerequisites:
  - 設定商品標籤.en
related:
  - ec/products/categories-and-tags/manage-product-tags.en/
tags:
  - Upsell
  - 商品加價購
  - "Bundle Selling"
  - 行銷活動
  - "Product Collection"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 商品加價購
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1008
  - https://www.cyberbiz.io/helpcenter/?p=11189
  - https://www.cyberbiz.io/support/?p=7356
  - https://www.cyberbiz.io/support/?p=953
permalink: "https://help.cyberbiz.io/ec/marketing/upsells/setup-product-upsell.en/"
comments: false
search:
  exclude: false
icon: lucide/circle-plus
hide: []
---

![PWP-By Product Page](../../../assets/images/ec-marketing-pwp-by-product-hero.zh-tw.png){ title="商品加價購群組頁面" .hero-page }

## About Product Upsells

A product upsell is triggered by **specific products**. When a customer buys a qualifying product, the system will Show selected add-on products during checkout that the customer can buy at a special price.

Product upsells are often used to:

- Recommend accessories or matching products
- Raise the average sale amount of a single product
- Build product bundle strategies

!!! example "Example: After buying a camera, customers can add camera accessories or a memory card."

## Set Up PWP-By Product

### Step 1: Add A PWP-By Product Collection

1. Log in to the CYBERBIZ admin and go to  **Marketing > PWP-By Product**.
2. Below the Collection list, enter a new Collection name and click **Create a collection**.

---

### Step 2: Fill In The Upsell Collection Details

In the Collection list, click the upsell Collection to expand it and set these fields:

- **Collection name**: The Name of the product upsell, used to identify and manage it.
- **Collection start date / Collection End Date**: Set when the promotion is valid.
- **When purchased products with the following tag is at least:**: The trigger, meaning the number of products with the specified Tag (Tag) the customer must buy.
- **Then Buy This Many Items from This Collection**: The maximum number of add-on items the customer can buy once the condition is met.

    !!! example "Example"
        If "Buy This Many Items with the Tags Below (Tag)" is **3 items**
        and "Then Buy This Many Items from This Collection" is **1 item**,
        then when a customer buys **3 products with the matching Tag**, they can **add up to 1 product from this upsell Collection**.

- **Tag**: Create the product Tag for the upsell first. Learn [how to set up product Tags](../../products/categories-and-tags/manage-product-tags.md).
- **Whether product add-on items can be doubled**: Choose whether the add-on quantity can multiply with the number of items bought.

	??? example "Example: Doubling Add-On Quantity"
		 Example: Buy 1 apple, add 1 pear

		|Setting|Behavior|
		|---|---|
		|**Unchecked**|The add-on quantity stays at 1. Even if the customer buys several apples, they can't add more pears.|
		|**Checked**|The add-on quantity multiplies with the number of items bought. For example, buy 2 apples and add up to 2 pears.|

- **Adjust order in batches**: Adjust the order in which add-on products Show. If you choose **Manual Sort**, drag products with :material-arrow-all: to reorder them.
	- The default is sorting by product title (alphabetical).
	- Sorting by best-sellers is recommended to improve conversion.

![PWP-By Product Settings](../../../assets/images/ec-product-pwp-by-product-collection-setting.zh-tw.png){ title="商品加價購群組設定" }

---

### Step 3: Select Upsell Products

1. In the product list on the left, click **Add** to add products to the upsell Collection (Collection).
2. Set the **add-on price** for each product.

!!! warning "Prices for Multi-Variant Add-On Products"

	- When an add-on product has multiple variants with different prices, customers can still choose a variant on the storefront, but **the price will Show as the fixed amount set in the upsell Collection**.
	- All variants of an add-on product use the **same fixed add-on price**.
	- To **price variants differently**, **create separate add-on products** for each variant and price.

![Select Upsell Products](../../../assets/images/ec-product-pwp-by-product-add-product-to-collection.zh-tw.png){ title="選擇加價購商品" }

### Step 4: What Customers See

- On the **checkout page**, when customers buy products with the matching Tag, the system will Show add-on product options.

![Storefront Upsell Display](../../../assets/images/ec-product-pwp-by-product-frontend.zh-tw.png){ title="前台加價購呈現" }

## Multi-Language Settings

Set multi-language Names for PWP-By Product so the storefront can Show the right text for each language.

!!! warning "Notes"
	- To edit the English version, **switch to English** first.
	- Only fields that Show a **language Tag** change text when the storefront language changes (they Show per language). For example: **Collection name** Product Upsell `繁體中文`.
	- If a language field is empty, the storefront uses the **繁體中文** content by default (Show / Show).

### Steps

1. Log in to the CYBERBIZ admin and go to **Marketing > PWP-By Product**
2. In the language menu, switch to the language you want to edit (for example, Traditional Chinese or English).
3. Expand the upsell Collection, click the Collection name field to edit it, and press ++enter++ to save.

![Multi-Language Settings](../../../assets/images/ec-pwp-by-product-collection-name-multilang.gif){ title="多國語系設定" }

### How It Looks On The Storefront (Show)

- **Traditional Chinese page**

	![Multi-Language Storefront - Traditional Chinese](../../../assets/images/ec-pwp-collection-name-multilang-forntend.zh-tw.png){ title="多國語系前台-繁體中文" }

- **English page**

	![Multi-Language Storefront - English](../../../assets/images/ec-pwp-collection-name-multilang-forntend.en-us.png){ title="多國語系前台-英文" }


## FAQ

??? quote "Can add-on products have multiple variants? If variants have different prices, how will the storefront Show them?"
	Yes. Add-on products can have multiple variants, and customers can still choose a variant on the product page. Keep in mind:

	- **Fixed add-on price**: Whatever the variant price, the storefront will Show **the fixed amount set in the upsell Collection**.
	- **Different prices per variant**: To set different add-on prices for variants, **create separate add-on products** for each variant and price.

??? quote "Why can customers add unlimited upsell items?"

	- **Cause**: The add-on products also have this upsell Collection's trigger Tag, so the system can't limit the add-on quantity.
	- **Solution**: **Use different Tags** for the add-on products and for the trigger threshold (Tag). Once the Tags don't overlap, the system can limit the add-on quantity correctly.

??? quote "Can the add-on quantity multiply with the number of items bought?"
	Yes. Select **Whether product add-on items can be doubled** in the upsell Collection settings, and the add-on quantity will multiply with the number of trigger products bought. Learn [how to set up add-on quantity doubling](#步驟-2填寫加價購群組資訊).
