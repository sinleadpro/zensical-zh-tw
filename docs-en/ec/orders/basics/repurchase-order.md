---
title: "Use the Buy Again Feature"
description: "The storefront Buy Again feature lets members easily reorder products they bought before. Covers prerequisites, steps, and special cases."
created: 2026-05-06 21:15
last_modified: 2026-07-13 11:40
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
  - 訂單
  - 會員
sites:
  - TW
audiences:
  - merchant
  - customer
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 使用再次購買功能
  - 重新下單商品
  - 提升回購率
features:
  - 再次購買
  - 拖拉版型
  - 購物車結帳
prerequisites: []
related:
  - ec/orders/basics/order-management-interface/
  - ec/marketing/upsells/setup-order-upsell/
tags:
  - "Buy Again"
  - Repurchase
  - "Drag-and-Drop Theme"
  - "Member Features"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/support/?p=42098
permalink: "https://help.cyberbiz.io/ec/orders/basics/repurchase-order/"
comments: false
search:
  exclude: false
icon: lucide/repeat-1
hide: []
---
![Buy Again for orders](../../../assets/images/EC-訂單-訂單查詢-前台-再次購買-hero.en.png){ title="Buy Again for Orders" .hero-page }

## About Buy Again

**Buy Again** lets members easily reorder products they bought before, without browsing the whole website or searching for products again. It shortens shopping time and helps improve members' shopping experience and loyalty.

## Prerequisites and Limitations

Before you start, make sure your store meets the following conditions:

- [x] **Theme limit**: This feature works only with **drag-and-drop themes**.
- [x] **Order type**: Supports only **regular orders**, not subscription orders or Quick Delivery orders.
- [x] **Checkout basis**: When buying again, product prices, contents, and discounts are all based on **the final information on the new cart checkout page**.

## Storefront Steps for Members

1.  **Open the order list**: After signing in to the website, members go to the "Regular Orders" tab in **Order Lookup**.

    ![Order lookup - regular orders](../../../assets/images/EC-前台-訂單查詢-一般訂單.en.png){ title="Order Lookup - Regular Orders" }

2.  **Choose an order**: Choose a past order to buy again, whether or not it's paid or shipped.
3.  **Click Buy Again**: Click **Buy Again** in the lower-right corner of the order, or click it directly from "Recent Orders."

    ![Order lookup - buy again](../../../assets/images/EC-前台-訂單查詢-再次購買.en.png){ title="Order Lookup - Buy Again" }

    !!! note "Non-Sale Items Filtered Automatically"
        The system adds only regular products to the cart. Gifts, add-on items, first-purchase gift, and gift vouchers in the original order are excluded automatically and aren't added again. [Learn more][order-repurchase-block]{ data-preview }

    ??? warning "If There Are Unavailable or Out-of-Stock Products"

        When the original order includes products that are unpublished or low in stock, the system shows a pop-up message.

        * **What happens**: After clicking "Confirm," the system still adds the other eligible products to the cart.
        * **Details**: [System Messages and Warnings][order-repurchase-error]{ data-preview }.

4.  **Add to cart**: The system automatically adds eligible products and quantities to a new cart, and the member can then go to the cart to check out.

## When Items Can't Be Added to the Cart { #order-repurchase-block }

When a member clicks **Buy Again**, items in the original order are **not** added to the new cart in the following cases:

*   **Unavailable product**: The original product no longer exists or is set to **Hidden**.
*   **Out of stock**: The product's stock is zero, and the admin is set to **Stop selling when out of stock**.
*   **Marketing gifts**: The original product is a **gift, add-on item, first-purchase gift, or gift voucher**.
*   **Bundle limits**: If the original order included a bundle and any item in it meets the rules above, the whole bundle can't be added to the new cart.

## System Messages and Warnings { #order-repurchase-error}

After the member clicks the button, if some products run into certain issues, the system shows a pop-up to the member:

* **Message content**: Lists which products can't be added because they're "Unpublished," "Hidden," or "Low in Stock."
* **What's next**: After clicking "Confirm" in the pop-up, the system still adds **the other eligible** products to the cart, and checkout can continue.

## Next Steps

<div class="grid cards" markdown>

- :lucide-file-search:{ .lg }  
  [__Check Order Status__](order-management-interface.md){ title="Order Management Interface" }  
  After checking out, members can see order status, shipping progress, and payment information in Order Lookup.

- :lucide-tag:{ .lg }  
  [__Set Up Order Upsells__](../../marketing/upsells/setup-order-upsell.md){ title="Set Up Order Upsells" }  
  When members buy again, they can add other products on the checkout page, raising average order value and repeat purchase rates.

</div>

## FAQ

??? quote "Why weren't some products added to the cart after clicking Buy Again?"

    Items in the original order aren't added to the new cart in the following cases:

    - **Unavailable product**: The original product no longer exists or is set to "Hidden"
    - **Out of stock**: The product's stock is zero, and the admin is set to "Stop selling when out of stock"
    - **Marketing gifts**: The original product is a gift, add-on item, first-purchase gift, or gift voucher
    - **Bundle limits**: If the original order included a bundle and any item in it meets the rules above, the whole bundle can't be added

??? quote "Which order types support Buy Again?"

    This feature supports only **regular orders**, not subscription orders or Quick Delivery orders. Members can buy again whether or not the order is paid or shipped.

??? quote "How are product prices calculated when buying again?"

    When buying again, product prices, contents, and discounts are all based on **the final information on the new cart checkout page**, not the original order's prices or discounts.

