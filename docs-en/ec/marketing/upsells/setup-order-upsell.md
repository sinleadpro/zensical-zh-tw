---
title: "Set Up Order Upsells"
description: "Set up order upsells triggered by order amount or other conditions, so customers can add selected products at a special price during checkout."
created: 2026-01-12 00:00
last_modified: 2026-07-22 17:39
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
  - 如何設定訂單加價購
  - 訂單加價購設定
features:
  - "Order Upsell"
prerequisites:
  - 設定商品標籤.en
related: []
tags:
  - Upsell
  - 訂單加價購
  - "Bundle Selling"
  - 行銷活動
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 訂單加價購
  - 行銷活動 > 商品加價購
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=11186
  - https://www.cyberbiz.io/support/?p=7367
permalink: "https://help.cyberbiz.io/ec/marketing/upsells/setup-order-upsell.en/"
comments: false
search:
  exclude: false
icon: lucide/shopping-cart
hide: []
---

![Order Upsell](../../../assets/images/ec-marketing-pwp-by-order-hero.en.png){ title="訂單加價購" .hero-page }

## About Order Upsells { #intro-order-upsell }

An order upsell is triggered by the **order amount or conditions**. When a customer meets the conditions at checkout, they can add selected products at a special price.

**Order Upsell Types**

There are two kinds of order upsells, based on the trigger:

- **Add-on with no minimum spend**
    Customers can choose add-on products as soon as they reach the checkout page.
- **Add-on above a minimum spend**
    Customers can add products only after the order amount reaches the threshold.

    > Example: Spend TWD 2,000 and add a knit blanket for TWD 1.

## Steps { #operate-order-upsell }

### Add A PWP-By Order Collection { #operate-order-upsell-add }

1. Log in to the CYBERBIZ admin and go to  **Marketing > PWP-By Order**.
2. Below the Collection list, enter a new Collection name and click **Create a collection**.

---

### Fill In The Upsell Collection Fields { #operate-order-upsell-fields }

In the Collection list, click the upsell Collection to expand it and set these fields:

- **Collection name**: Used to identify and manage this order upsell.
- **Collection Start/End Date**: Set when the promotion is valid.
- **Minimum spending displayed in shopping cart for this collection**: Set the order amount that triggers the upsell.
- **Collection purchase limit**: Limit how many add-on items each order can include.

	!!! info "About the Add-On Limit"
		If the Collection purchase limit is **1 item**, the system will Show "Quantity limit reached" when a customer tries to add a 2nd item.

- **Adjust order in batches**: Set how add-on products are sorted on the storefront (Show order). If you choose **manually**, drag products with :material-arrow-all: to reorder them.
	- The default is sorting by product title (alphabetical).
	- Sorting by best-sellers is recommended to improve conversion.

![Upsell Collection Settings](../../../assets/images/ec-marketing-pwp-by-order-collection-setting.zh-tw.en.png){ title="加價購群組設定" }

---

### Select Upsell Products { #operate-order-upsell-products }

1. In the product list on the left, click **Add** to **add the products to the Collection**.
2. Set the **add-on price** for each product.

![Select Upsell Products](../../../assets/images/ec-pwp-by-order-add-to-collection.en.png){ title="選擇加價購商品" }

---

### What Customers See At Checkout { #operate-order-upsell-checkout }

When the order amount reaches the **Minimum spending displayed in shopping cart for this collection**, the checkout page will Show the add-on products.

- **Below the threshold**: Add-on options don't Show.
- **Threshold reached**: Show add-on products

## Multi-Language Settings { #operate-order-upsell-language }

Set multi-language Names for PWP-By Product so the storefront can Show the right text for each language.

!!! warning "Notes"
	- To edit the English version, **switch to English** first.
	- Only fields that Show a **language Tag** change text when the storefront language changes (they Show per language). For example: **Collection name** Product Upsell `繁體中文`.
	- If a language field is empty, the storefront will Show the **繁體中文** content by default when Showing that language.

### Steps { #operate-order-upsell-language-steps }

1. Log in to the CYBERBIZ admin and go to **Marketing > PWP-By Product**
2. Open the language menu and switch to the language you want to edit (Traditional Chinese, English, and so on).
3. Expand the upsell Collection, click the Collection name field to edit it, and press ++enter++ to save.

![Multi-Language Collection name Settings](../../../assets/images/ec-pwp-by-order-collection-name-multilang.en.gif){ title="多語系群組名稱設定" }

### How It Looks On The Storefront (Show) { #overview-order-upsell-language }

- **Traditional Chinese page**

	![Storefront Show - Traditional Chinese](../../../assets/images/ec-pwp-by-order-frontend.zh-tw.en.png){ title="前台顯示-繁體中文" }

- **English page**

	![Storefront Show - English](../../../assets/images/ec-pwp-by-order-frontend.en-us.en.png){ title="前台顯示-英文" }


## FAQ { #faq-order-upsell }

??? quote "Can I limit how many add-ons each order can include?"
	Yes. Set the **Collection purchase limit** to limit the number of add-on items per order. If a customer goes over the limit, the system shows that the limit has been reached.

??? quote "Does the add-on price affect the product's regular price?"
	No. An order upsell only changes the price Shown for the add-on product at checkout. It doesn't change the product's regular price or the price on the product page.
