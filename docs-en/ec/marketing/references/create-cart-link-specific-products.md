---
title: "Create A Cart Link With Specific Products"
description: "Create a special cart link that automatically adds preset products and quantities to the cart. Use it for social media referrals, EDM marketing, and more."
created: 2026-04-29 14:06
last_modified: 2026-08-06 11:20
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 行銷活動
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 建立商品導購連結
  - 自動加入購物車
features:
  - 指定商品購物車連結
prerequisites: []
related: []
tags:
  - "Cart Link"
  - "Product Referral"
  - "Social Media Referral"
  - "EDM Marketing"
  - "UTM Parameters"
  - "Discount Code"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=2369
permalink: "https://help.cyberbiz.io/ec/marketing/references/create-cart-link-specific-products.en/"
comments: ""
search:
  exclude: false
icon: lucide/link
hide:
---

![Product Referral Cart Link Page](../../../assets/images/ec-行銷活動-指定商品導購連結.png){ .hero-page }

## About Cart Links With Specific Products

This feature lets you generate a special URL. When customers click it, the system **automatically adds preset products and quantities to the cart** (Settings). It works well for social media referrals, EDM marketing, and promotions for specific audiences.

!!! tip "Example Use Cases"

    Use your links in these channels:

    *   **Social media links**: Add them to LINE or Instagram posts to shorten the path to the product and improve conversion.
    *   **Quick EDM orders**: Add links for popular bundles in newsletters so customers can add them in one click.
    *   **Segmented campaigns**: Create cart contents for different member audiences (Settings) to match your marketing strategy.


## Before You Start

- **Scope**: Works only with online store cart links, not one-page stores.

!!! warning "Before publishing, **always test the URL yourself** to make sure it opens the cart with the right products and quantities."

## How To Get Product IDs And Variants IDs

To build a link, first export product data from the admin to get the IDs.

1.  **Go to**: **Products**」>「**All Products**.
2.  **Select products**: In the product list, select the products you want to add to the cart.
3.  **Export data**: Click **Export Products** in the upper-right corner.

    ![Export Product Information](../../../assets/images/ec-商品列表匯出-操作選單.png)

4.  **Find the IDs**: Download and open the Excel file, then unhide the hidden columns:
    - Column A: Product ID, used with type=product (for products with a single Variants)
    - Column B: Product Variants ID, the default mode that targets an exact Variants

    ![Product List Export](../../../assets/images/ec-商品列表匯出檔案-商品id與款式id.png)

5.  **Note the values**: The numbers shown in these columns (Display) are the product IDs. Write them down to use in your link.

## Cart Link URL Format

Follow this syntax to build your link manually.

- **URL structure**: A link has a base path and a parameter string:

    ``` http
    [您的網址]/cart/replace?products=[款式ID]:[數量],[款式ID]:[數量]&[其他參數]=[數值]
    ```

    ``` http title="範例：兩款商品，數量各一"
    https://www.goodthing.com/cart/replace?products=001234:1,001235:1
    ```

- **Parameters**: All parameters go after `?`. To use more than one, join them with `&`.

    | Parameter | Required | Description | Example / Rule |
    | :--- | :---: | :--- | :--- |
    | `products` | **Yes** | Products and quantities | Format: `ID:數量`. Separate multiple products with `,` or `;`. |
    | `type` | No | ID mode | With `product`, the system treats the ID as a product ID and selects the first Variants. |
    | `coupon` | No | Auto-apply a discount code | The cart applies this code automatically when customers click the link. |
    | `utm_source` | No | Traffic source | Marks the ad channel (such as `line` or `instagram`). |
    | `utm_medium` | No | Marketing medium | Marks the traffic type (such as `social` or `email`). |
    | `utm_campaign` | No | Campaign name | Tells marketing campaigns apart (such as `summer_sale`). |
    | `utm_term` | No | Tracking keyword | Marks a specific ad keyword. |
    | `utm_content` | No | Ad content | Tells apart creatives or placements in the same campaign. |


## Advanced Use

### Use A Product ID <Small>For Products With A Single Variants</small>

Add the `type=product` parameter and use the product ID from column A:

``` http
[您的網址]/cart/replace?products=[商品ID]:[數量]&type=product
```

!!! question "Which ID Should I Use?"
    If a product has multiple Variants, use the **Variants ID** to add the correct Variants. If a product has a single Variants, the **product ID** with the `type=product` parameter is easier.

---

### Add A Discount Code

Add the coupon parameter to the link. The cart applies the discount automatically when customers click it:

``` http
[您的網址]/cart/replace?products=[款式ID]:[數量]&coupon=[折扣碼]
```

--- 

### Track With UTM Parameters

Add UTM parameters to the link to track referral performance by channel in GA or the admin:

``` http
[您的網址]/cart/replace?products=[款式ID]:[數量]&utm_source=line&utm_medium=social&utm_campaign=summer2025
```

## Examples

!!! example "Example Settings"
    - The online store is `https://www.goodthing.com`.
    - Add 1 of each of Variants IDs 001234 and 001235.

``` http title="情境一：社群導購，帶入兩款商品"
https://www.goodthing.com/cart/replace?products=001234:1,001235:1

```
``` http title="情境二：EDM 活動，搭配折扣碼與 UTM 追蹤"
https://www.goodthing.com/cart/replace?products=001234:1,001235:1&coupon=SUMMER10&utm_source=edm&utm_medium=email&utm_campaign=summer2025

```
``` http title="情境三：單一款式商品，使用商品 ID"
https://www.goodthing.com/cart/replace?products=56789:2&type=product

```

## FAQ

??? quote "How do I get product IDs and Variants IDs?"

    > Go to Products All Products, select the products to export, and click Export Products. In the downloaded Excel file, column A is the product ID and column B is the product Variants ID.

??? quote "When should I use a product ID instead of a Variants ID?"

    If a product has multiple Variants, use the **Variants ID** to add the correct Variants. If a product has a single Variants, the **product ID** with the `type=product` parameter is easier.

??? quote "Can a link apply a discount code automatically?"

    Yes. Add the `coupon=[折扣碼]` parameter to the link, and the cart will [apply the code automatically](#搭配折扣碼){ title="搭配折扣碼" } when customers click it.
