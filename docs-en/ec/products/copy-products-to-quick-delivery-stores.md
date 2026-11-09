---
title: "Copy Products to Express Delivery Stores"
description: "Learn how to copy products suited for fast delivery to the store section, including product selection tips, the batch copy flow, and how store inventory is managed separately."
created: 2026-02-03 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
  - 金物流
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
plan_options: 
  - optional
cyb_extensions:
  - NOW!
intents:
  - 挑選快速到貨商品
  - 批次複製商品至門市
  - 管理門市獨立庫存
features:
  - CYBERBIZ NOW
  - 快速到貨
  - 門市商品管理
prerequisites:
  - "Express Delivery is enabled for the store"
  - "Products are launched and have enough online store inventory"
related:
  - ec/website-appearance/setup-quick-delivery-frontend-entry/
tags:
  - "Express Delivery"
  - "Multiple Carts"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 商品列表 > 更多操作
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=12814
permalink: "https://help.cyberbiz.io/ec/products/copy-products-to-quick-delivery-stores/"
comments: false
search:
  exclude: false
icon: lucide/copy
hide: []
---
# Copy Products to Stores

Copy products suited to fast delivery to Express Delivery stores so customers can shop them in the Express Delivery section and get on-demand delivery.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

![](../../../assets/images/EC-後台-商品-所有商品-複製商品到門市01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Increase on-demand purchases**: Copy daily necessities and best-selling snacks to stores to meet customers' **need it now** demand.
    - **Region-specific sales**: Copy regional products that fit the customer profile of specific store areas.
    - **Improve delivery efficiency**: Choose products of moderate size and weight to make delivery easier for couriers and reduce the risk of damage.


## Before You Start { #prerequisites-copy-qd }

### Separate Inventory and Pricing { #prerequisites-copy-qd-stock }

Store products are **copies** of website products.

- **Sales deduction**: When store A sells a product, only store A's inventory is deducted. The inventory of the website and of store B does not change.
- **Differential pricing**: You can raise store prices for stores in high-rent urban areas without affecting the website price.

### Multi-Cart Checkout Flow { #prerequisites-copy-qd-cart }

When a customer adds both a **Normal Product** and an **Express Delivery product** to the cart:

1. At checkout, the system directs the customer to the **multi-cart** page.
2. The customer must choose one cart to check out first (the two kinds of products cannot be placed in the same order).


## Steps { #operate-copy-qd }

### Step 1: Choose Suitable Products { #operate-copy-qd-select }

Not every product is suited to Express Delivery. We recommend filtering products by the following criteria:

| Criterion | Recommended Spec | Examples |
| :--- | :--- | :--- |
| **Size and weight** | Each side ≤ 45 cm, weight ≤ 2 kg | Electronics accessories, apparel, daily necessities |
| **Storage temperature zone** | Room-temperature products are preferred | Cookies, beverages, books |
| **Turnover rate** | Best sellers or frequently purchased products | Masks, charging cables, toilet paper |

!!! warning "Products to Avoid"
    Do not copy large furniture, fragile glassware, or fresh products that need special cold-chain protection (unless the store has the equipment) to the Express Delivery section.

### Step 2: Copy Products in Bulk { #operate-copy-qd-batch }

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Select the products you want to copy (you can filter by search or tags).
3. At the top of the page, click **Actions... > Copy Products to Branch Stores**.
4. In the pop-up window, set the following:
    - **Target stores**: Choose the Express Delivery stores to add the products to (you can select several or all).
    - **Copy images too**: We recommend selecting this so the store section shows complete information.
5. Click **Confirm** to run the task.

### Step 3: Check the Copy Results and Enable the Products { #operate-copy-qd-enable }

1. The system processes the copy task in the background and sends an email notification when it is done.
2. After you receive the notification, go back to **Products > All Products** and click **Advanced Search**.
3. In the **Store type** drop-down list, select the store and check that the products appear in the list.
4. Switch the status to :lucide-eye: `Published` and set the correct store inventory.

## Express Delivery Product Specifications { #specs-copy-qd }

- **Default status**: Newly copied Express Delivery products are :lucide-eye-off: `Unpublished` by default.
- **Inventory management**: The **Inventory** toggle is `ON` by default.
  > **Insufficient Stock** defaults to **Stop selling**, and **Shipping Address** defaults to **Address required**. These cannot be changed.
- **Feature limits**: Express Delivery products **do not support pre-orders**, and you cannot set SEO, product categories, or temperature zones for them individually.
  > If a courier's delivery box has an insulated bag and dividers, products of different temperature zones can be delivered together, so you don't need to set a product temperature zone in the admin.
- **Product category binding**: Only **customized collections** are copied. Other categories are not copied.
- **No marketing campaigns**: Express Delivery products cannot be added to Mix and Match multi-group offers, Buy X Get Y discount collections, or Bonus Mall.
- **Logistics binding**: The system automatically binds the store's Express Delivery logistics, and other logistics are not supported.
- **Sync**: When you edit product information on the website, store products are **not synced automatically**. Run **Copy Products to Branch Stores** again to overwrite them.

## FAQ { #faq-copy-qd }

??? quote "How long does it take to copy products to stores?"
    Processing time depends on the number of products and whether images are copied. Ten products usually take about 5–10 minutes.<br>
    We recommend working in batches so that selecting too many products at once doesn't make processing take too long.

??? quote "Can I copy only specific variants (options) to a store?"
    The system currently does not support **partial variant copying**. All variants of the product are copied.<br>
    If a store doesn't sell a specific option, edit the store product after copying and set that variant's inventory to `0`.

??? quote "If a website product is deleted, do the store products disappear too?"
    Yes. When you delete the original website product in product management, the system also removes its copies from all stores.

---

## Next Steps { #next-steps-copy-qd }

<div class="grid cards" markdown>

- :lucide-layout-dashboard:{ .lg }  
  [__Set Up the Express Delivery Storefront Entry and Section__](../website-appearance/setup-quick-delivery-frontend-entry.md)  
  Plan the layout of the storefront section to encourage customers to use on-demand delivery.

</div>

