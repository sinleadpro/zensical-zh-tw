---
title: "Create POS Products"
description: "Learn how to sync EC website products to POS stores, or create exclusive products for POS-only stores to enable omnichannel inventory management."
created: 2026-06-24 16:50
last_modified: 2026-06-24 16:50
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules: 
  - 商品
  - POS 功能
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents: 
  - 同步 EC 商品至 POS
  - 建立 POS 獨賣商品
  - 管理 POS 門市商品
features: 
  - POS 商品同步
  - POS 獨賣商品
  - 庫存管理
prerequisites: 
  - "所有商品-新增商品"
related:
  - ec/products/create-and-manage/create-update-products/
  - ec/products/bulk-operations/excel-import-products/
tags: 
  - POS
  - "Product Creation"
  - Sync
  - "Store Management"
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 所有商品列表
  - 複製商品至 POS 商店
paths: 
  - 商品 > 所有商品
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=5138
permalink: "https://help.cyberbiz.io/pos/get-started/create-pos-products/"
search:
  exclude: false
icon: lucide/package-plus
hide: []
---

# Create POS Products
Learn how to sync EC website products to POS stores, or create exclusive products for POS-only stores to enable omnichannel inventory management.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


## Usage Notes { #prerequisites-pos-products }

- **Image importance**: POS product images appear directly on the POS front-end screen, helping staff quickly identify products. We recommend turning on **Copy all product images** when copying.


## Workflow { #operate-pos-products }

### Create the Product in the EC Admin Panel { #operate-pos-products-ec-admin-create }

1. The first step in setting up POS store products is to create the product in the **EC admin panel** and then copy it to the POS store. This ensures a smooth process and complete information.

    !!! tip "Tip"
        Edit products mainly on the EC website. POS stores mainly use products for inventory management.

2. For how to set up products on the EC website, see [Add and Update Products](../../ec/products/create-and-manage/create-update-products/).
3. After you are familiar with creating single products, see [Bulk Import Products from Excel](../../ec/products/bulk-operations/excel-import-products/) to create products in batches.

### Copy EC Products to POS Store { #operate-pos-products-ec-product-pos }

Sync existing website products to the specified store.

1. Log in to the CYBERBIZ admin panel, go to **Products > All Products**, and select the products to sync. To select all products for batch operations, click **Select All**.
2. Click **Copy products to POS stores**.
3. In the pop-up window, complete the following settings:
    - **Select Store**: Select the POS stores to copy to (multiple selections allowed).
    - **Copy Images**: We recommend turning on **Copy all product images**.

![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品建立1.png){ .screenshot }


### Create Products for POS-Only Merchants { #operate-pos-products-pos-create-product }

For merchants who only purchase the POS system, specify the store directly **when creating a product**.

1. Go to **Products > All Products**, and click **Add Product**.
2. On the product edit page, find the **POS Store Settings** section.
3. Select the **POS stores** where this product will be sold.
4. After you complete the other product information, click **Save**.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-所有商品-POS獨賣商家建立商品時同步POS商店01.png){ .screenshot }

!!! warning "Restrictions"
    - **No retroactive application**: This sync setting applies only **when creating new products**. For existing products, use the **Copy Product to POS Store** method above to add them to a store.
    - **Plan restriction**: This feature is available only to POS-only merchants. If you use both EC and POS, use the copy feature consistently to keep data consistent.


