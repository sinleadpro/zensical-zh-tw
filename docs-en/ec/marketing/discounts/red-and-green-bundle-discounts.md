---
title: "Bundle Discounts"
description: "Combine products from different Collections (for example, A Collections + B Collections) and set fixed-price, percentage, or amount-off rules to raise average order value and cross-category sales."
created: 2026-01-21 00:00
last_modified: 2026-06-30 10:56
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 是否適用POS：EXCEL表格有門市欄位
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 行銷活動
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
  - 建立紅配綠活動
  - 設定計價規則
  - 管理商品群組
  - 批次匯入群組商品
features:
  - 紅配綠多組合優惠
  - 組合優惠
prerequisites:
  - "需先準備好欲參與活動的商品.en"
related: []
tags:
  - Multi-Country
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 行銷活動 > 紅配綠多組合優惠
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8226
  - https://www.cyberbiz.io/support/?p=23847
  - https://www.cyberbiz.io/support/?p=7378
permalink: "https://help.cyberbiz.io/ec/marketing/discounts/red-and-green-bundle-discounts.en/"
comments: false
search:
  exclude: false
icon: lucide/layers
hide: []
---
# Bundle Discounts

Bundle products from different Collections (such as Collections A + Collections B) and set fixed price, percentage, or amount-off rules to raise order value and cross-category sales.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Version Differences"
    On PLUS plans, Bundle Discounts is part of the "Marketing A" add-on module (choose 2 of 11). Make sure you have selected this module before using it. Enterprise includes it by default.

![](../../../assets/images/EC-後台-行銷活動-紅配綠多組合優惠-畫面總覽01.png){ .hero-page }

## About Bundle Discounts

Bundle discounts are a classic promotion. You group products by margin or type (such as main dish + drink, or console + accessory), and customers get the bundle deal after picking a set number of items from each of the Collections. This helps sell long-tail products and improves your overall margin mix.

The system supports bundles across any number of Collections. Beyond the classic two Collections, you can combine as many Collections as you like to build flexible bundles.

!!! tip "Use Cases"
    - **Meal deals**: Pick 1 main dish (Collections A) + 1 drink (Collections B) for NT$199.
    - **Outfit bundles**: Pick 1 top + 1 bottom + 1 accessory and get NT$300 off.
    - **Add-on deals**: Buy 1 main product (Collections A) and add 1 selected accessory (Collections B) for NT$99.

## Before You Start

- **Hidden by default**: New promotions are "Hidden" by default. If the storefront shows a 404 error, check the status toggle.
- **One group per product**: In a bundle promotion, a product (or variant) can belong to only one of the Collections.
- **Shopping experience**: Keep the number of products in each of the Collections small (8 or fewer recommended) so customers can choose easily.
- **Discount order:**: If an order qualifies for several promotions, the one with the higher "Priority" value applies first.

## Steps

### Step 1: Create The Promotion

1. Log in to the CYBERBIZ admin and go to **Marketing > Bundle Discounts**.
2. Enter the promotion **Promotion name** and click **Create a promotion**.
3. **Start/End Date**: Set when the promotion is active.
4. **Promotion Link**: Customize the URL path of the promotion page.
5. **Discount order:**: Enter a value (1–999). Higher values take priority.

### Step 2: Set The Pricing Rule

In the "Pricing Rule" section of the promotion page, choose a discount method:

| Rule Type | Description | Example |
| :--- | :--- | :--- |
| **Fixed price** | The bundle has a fixed total price | A(1)+B(1) = NT$999 |
| **Fixed discount** | The bundle gets a set percentage off | A(1)+B(1) at 85% of list price |
| **Discount fixed amount** | A fixed amount is taken off the bundle total | A(1)+B(1) NT$100 off |
| **Discount fixed amount per item** | A fixed amount is taken off each item in the bundle | A(1)+B(1) NT$10 off each item |

### Step 3: Manage Product Collections

1. Enter the **Collection name** (such as Main Dishes or Add-Ons) and click **Create a collection**.
2. Set the **Collections Purchase Quantity**: how many items customers must pick from the Collections to trigger the deal.
3. Set the **Block Color**: the color of each of the Collections on the storefront, so customers can tell them apart.

![](../../../assets/images/EC-後台-行銷活動-紅配綠多組合優惠-設定群組01.png)

### Step 4: Select And Add Products

1. In the product list on the left, Search Product by Name, SKU or tag.
2. Select products and click **Add**.
    *   **Added to these Collections**: Can be removed at any time.
    *   **Added to other Collections**: Can't be added again.

### Step 5: Bulk Import Products (Optional)

For many products, use Excel to import them in bulk:

1. On the promotion page, download the **Bundle Discounts Template**.
2. Fill in the Excel sheet. Key fields:

    - **Action**: Create a promotion or remove a promotion.
    - **Promotion Name**: Must exactly match the promotion Name in the admin.
    - **Collection name**: Must exactly match the Collections Name in the admin.
    - **SKU**: Enter the correct variant SKU.
    - **All Stores**: Enter "是" or "true" to apply to all stores. Blank or any other value counts as "No."
    - **Store Name**: If not all stores apply, enter the exact "Website Name" or "POS store name."
    - **Run in Online Store**: Set to "Yes" to show and apply the promotion in the online store.

3. Back in the admin, click **No file selected** and import the file.
4. You'll get the import results by email.

## Multi-Language Settings

Set multi-language Names for bundle discounts so the storefront shows the right text for each language.

!!! warning "Notes"
	- To edit the English version, **switch to English** first.
	- Only fields with a **language tag** change text when the storefront language changes. For example: **Collection name** Bundle Discounts `繁體中文`.
	- If a language field is empty, the storefront shows the **繁體中文** content by default.

### Steps

1. Log in to the CYBERBIZ admin and go to **Marketing > Bundle Discounts**
2. In the language menu, switch to the language you want to edit (for example, Traditional Chinese or English).
3. Expand the Collections, click the Collections Name field to edit it, and press ++enter++ to save.

![](../../../assets/images/EC-後台-行銷活動-紅配綠多組合優惠-設定多國01.png)



## FAQ

??? quote "Why can't I see the promotion page on the storefront?"
    Check that: 1. The promotion is set to "Public." 2. Today is within the promotion period. 3. There are at least two Collections, and each has products.

??? quote "Can I set up "buy 2, get 1 free"?"
    Yes. Create Collections A (buy 2) and Collections B (get 1), choose "Fixed amount off" as the pricing rule, and set the amount to the price of the product in Collections B. If product prices vary, the "Quantity Discount" feature is more accurate.

??? quote "If a customer picks 2 items from Collections A and 2 from Collections B, does the deal apply twice?"
    Yes. The system multiplies the deal based on the required quantity for each of the Collections. For example, with an A(1)+B(1) deal, buying A(2)+B(2) applies the bundle deal twice.


