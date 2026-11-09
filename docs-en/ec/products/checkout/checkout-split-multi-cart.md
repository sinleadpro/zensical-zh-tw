---
title: "Set up Automatic Checkout Splitting into Multiple Carts"
description: "Set split-order rules based on a product's channel, temperature zone, logistics, and pre-order attributes so the system automatically assigns products to multiple carts at checkout."
created: 2026-03-05 15:00
last_modified: 2026-07-15 13:58
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
  - 商品
sites:
  - TW
tnb: branch
plans:
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: intermediate
intents:
  - 結帳自動拆分購物車
  - 區分預購與現貨訂單
  - 依溫層或物流分開結帳
features:
  - 多購物車
  - 商品通路設定
  - 配送溫層拆單
  - 物流綁定拆單
  - 預購商品拆單
prerequisites: []
related: []
tags:
  - "Shopping Cart"
  - "Automatic Order Splitting"
  - "Shipping Conditions"
  - "Temperature Zone Order Splitting"
  - "Logistics Binding"
  - "Pre-Order Products"
  - "Multiple Carts"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 商品編輯頁
  - 設定分頁
  - 溫層與物流配送設定
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8632
  - https://www.cyberbiz.io/support/?p=2142
permalink: "https://help.cyberbiz.io/ec/products/checkout/checkout-split-multi-cart/"
search:
  exclude: false
icon: lucide/shopping-cart
hide: []
comments: false
---

![Split checkout into multiple carts](../../../assets/images/ec-split-checkout-multi-cart-frontend.zh-tw.en.png){ .hero-page title="Split Checkout into Multiple Carts" }

## About Checkout Splitting into Multiple Carts { #intro-split-cart }

When the products in a customer's cart have different "delivery conditions" (such as fulfillment channel, delivery temperature zone, or logistics method), **the system automatically splits the products into multiple separate carts during checkout**. Each cart:
    
- Calculates applicable discounts separately
- Calculates shipping fees separately
- Creates its own order after checkout. The customer must complete checkout for each cart one by one.  

The same product may appear in different carts, but **once one cart is checked out, that product is automatically removed from the other carts that haven't been checked out**, to avoid duplicate purchases.

??? example "Use Cases"

    - Fulfillment channel binding: When products belong to *different fulfillment channels*[^channels], set product channels so the system automatically splits them into different carts at checkout.
    - Delivery temperature zone binding: When products must be delivered in *different delivery temperature zones* (room temperature/refrigerated/frozen), you can set multiple delivery temperature zones, and the system automatically splits carts based on each product's temperature zone requirement.
    - Logistics binding: When products must be bound to *different logistics providers*[^logistics], set the logistics methods available for each product.

    ??? example-clean "Example"
    
          - Product A: Supports T-Cat home delivery only
          - Product B: Supports Pelican Express only
          - Product C: Supports both T-Cat home delivery and Pelican Express

          When a customer buys products A, B, and C together, *the system automatically splits them into 2 carts based on the logistics restrictions, and each is checked out separately*.

!!! warning "Assess Checkout Complexity"
    Multiple delivery attributes make checkout more complex and may affect the customer experience. Carefully assess your actual use cases before setting them up.

    ??? info-clean "How Product Delivery Conditions Affect Checkout"

        ```mermaid
        flowchart LR
          A(Products have different temperature zones,<br>delivery methods, or channels) --> B(The system assigns carts automatically)
          B --> C(Each cart calculates<br>discounts and shipping separately)
          C --> D(Separate checkouts<br>create separate orders)
        ```

## Steps { #operate-split-cart }

### Set Product Channels { #operate-split-cart-channel }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions.md#conventions-plans) | Expert / PLUS / Enterprise

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to open its edit page, then switch to the **Settings** tab.
3. In the "Product distribution channel" section, add or manage product channels. The default is empty, which means the product applies to all channels.

![Product channel settings](../../../assets/images/ec-product-distribution-channel-setting.zh-tw.en.png){ title="Product Channel Settings" }

!!! tip "Adding and Naming Channels"
    Enter a channel name directly to add it. **Channels cannot be deleted once added.** Duplicate channel names are not allowed; if you need the same name, distinguish them with numbers. Each product can be bound to only **one channel**.

??? info "How Product Channels Work"
    Think of a product channel as a kind of tag: create a name and apply it to products. The system automatically splits carts by channel and calculates discounts and shipping fees separately.

---

### Set Product Temperature Zone { #operate-split-cart-temp }

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to open its edit page, then switch to the **Settings** tab.
3. In the "Temperature Zone Settings" section, you can set the product's temperature zone: room temperature, refrigerated, or frozen. You can select more than one.

![Product temperature zone settings](../../../assets/images/ec-product-temp-setting.zh-tw.en.png){ title="Product Temperature Zone Settings" }

---

### Set Product Logistics { #operate-split-cart-logistics }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions.md#conventions-plans) | Expert / PLUS / Enterprise

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to open its edit page, then switch to the **Settings** tab.
3. In the "Temperature Zone and Logistics Settings" section, you can set the product's logistics methods and choose delivery methods as needed.

![Product logistics settings](../../../assets/images/ec-product-shipping-temperature-and-logistics-setting.zh-tw.en.png){ title="Product Logistics Settings" }

---

### Set a Pre-Order Product Channel { #operate-split-cart-preorder }

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to open its edit page, then switch to the **Settings** tab.
3. Under "Product distribution channel", add a dedicated "Pre-order" channel.
4. Click the "Product Information" tab, and under "Manage Variants", set "Insufficient Stock" to `Continue selling`.
5. After you complete these settings, the system automatically puts products bought through the "Pre-order" channel into the same cart, so you can ship "in-stock" and "pre-order" products separately.

!!! warning "If 'Insufficient Stock' is not set to `Continue selling`, the pre-order product cannot be added to the cart."

![Pre-order product settings](../../../assets/images/ec-product-preorder-product.zh-tw.en.gif){ title="Pre-Order Product Settings" }

## Example Scenarios { #specs-split-cart-examples }

### Same Logistics / Same Temperature Zone / Different Product Channels { #specs-split-cart-same-ship }

**Settings**

*   Vendor A Room Temp: Shipped by Vendor A, temperature zone is room temperature.
*   Vendor B Room Temp: Shipped by Vendor B, temperature zone is room temperature.
*   AS: Can be shipped by either Vendor A or Vendor B.
*   *All products have the same delivery temperature zone and logistics method.*

**Result**

*   Vendor A's cart can check out `Vendor A Room Temp` and `AS`.
*   Vendor B's cart can check out `Vendor B Room Temp` and `AS`.
*   *Whichever cart is checked out first, AS is automatically removed from the other cart.*

![Different product channels](https://www.cyberbiz.io/support/wp-content/uploads/商品-商品通路設定03-1.png){ title="Different Product Channels" .screenshot }

---

### Same Logistics / Different Product Channels / Different Temperature Zone { #specs-split-cart-diff-temp }

**Settings**

*   Vendor A Room Temp: Shipped by Vendor A, with temperature zone limited to "Room temperature".
*   Vendor A Refrigerated: Shipped by Vendor A, with temperature zone limited to "Refrigerated".
*   Vendor B Room Temp: Shipped by Vendor B, with temperature zone limited to "Room temperature".
*   Vendor B Refrigerated: Shipped by Vendor B, with temperature zone limited to "Refrigerated".

**Result**

*   At checkout, the cart is automatically split into four orders by "Product distribution channel" and "temperature zone".
*   *If a product appears in more than one cart, it is automatically removed from the other cart once any of those carts is checked out.*

![Multiple channels and temperature zones](../../../assets/images/ec-multi-distribution-channel-multi-temp-scenario.zh-tw.en.png){ title="Multiple Channels and Temperature Zones" }

---

### Different Logistics / Same Temperature Zone / Same Product Channel { #specs-split-cart-diff-ship }

**Settings**

*   Vendor A Room Temp: Shipped by Vendor A, with temperature zone limited to "Room temperature" and logistics set to "SF Express Overseas, Pelican Express".  
*   AS: Shipped by Vendor A, with temperature zone limited to "Refrigerated" and logistics set to "SF Express Overseas, Pelican Express".
*   In-store pickup order: No "Product distribution channel" limit, temperature zone limited to "Room temperature", and logistics set to "In-store pickup".

**Result**

*   This example shows that, with all other conditions the same, different logistics methods still split checkout into multiple carts.

![Logistics](https://www.cyberbiz.io/support/wp-content/uploads/商品-商品通路設定05-1.png){ title="Logistics" .screenshot }


## FAQ { #faq-split-cart }

??? quote "Do multiple carts increase shipping costs?"
    Yes. Each cart calculates shipping fees separately. If products are split into multiple carts, customers may need to pay multiple shipping fees.

??? quote "How are carts split if a product has a channel, temperature zone, and logistics set?"
    The system combines all the different attributes and splits products into the matching carts. For example, products with different channels and temperature zones produce multiple carts.


[^channels]: Such as different warehouses, stores, or suppliers.
[^logistics]: Such as Chunghwa Post, Hsinchu Logistics, or T-Cat.
[^preorder-channel]: Pre-order products are handled by creating a "Pre-order" channel, which is a channel attribute.
