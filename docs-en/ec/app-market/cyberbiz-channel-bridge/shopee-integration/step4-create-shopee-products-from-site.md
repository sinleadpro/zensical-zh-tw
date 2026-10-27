---
title: "Step 4: Create Shopee Products from Online Store Products"
description: "Publish existing online store products to your Shopee shop quickly. After publishing, the system links the products on both sides automatically so inventory and information can sync later."
created: 2026-02-26 00:00
last_modified: 2026-08-28 17:30
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - WMS
modules:
  - 商品
  - APP MARKET
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
plan_options: []
cyb_extensions:
  - CHANNEL BRIDGE
intents:
  - 官網商品發佈至蝦皮
  - 編輯蝦皮特定欄位
  - 核對發佈紀錄
features:
  - 蝦皮商品搬站
  - 關聯自動建立
prerequisites:
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step1-install-and-activate/
  - 商品需為官網手動建立且未關聯過蝦皮
related:
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step3-sync-inventory-with-shopee/
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step5-sync-product-info-with-shopee/
tags: []
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 商品 > 所有商品
  - App MARKET > 我的擴充服務 > CYBERBIZ CHANNEL BRIDGE
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12688
  - https://www.cyberbiz.io/support/?p=51554
permalink: "https://help.cyberbiz.io/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step4-create-shopee-products-from-site/"
comments: false
search:
  exclude: false
icon: lucide/package-plus
hide: []
---
# Step 4: Create Shopee Products from Online Store Products

You can also publish existing online store products to your Shopee shop quickly. After publishing, the system links the products on both sides automatically, so you can sync inventory and product information later.
{ .subtitle }

[:lucide-lock:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHANNEL BRIDGE
{ .doc-badge }

![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-畫面總覽01.en.png){ .hero-page }



!!! tip "Use Cases"
    - **Expand to New Channels**: You have run your online store for a while and want to list selected products on Shopee quickly.
    - **Launch New Products on Both Sides**: After you create a new product in your online store, sync it to Shopee in one click instead of pasting images and text again.
    - **Keep Links Consistent**: Products on both sides are linked correctly from the moment they are published, avoiding errors from matching SKUs by hand.


## Before You Start { #prerequisites-shopee-s4 }

Before publishing, make sure the products meet the following conditions:

| Item | Details and Limits |
| :--- | :--- |
| **Product Source** | Must be created manually in your online store and **not yet linked to Shopee** |
| **Type Restrictions** | POS products and fast delivery products are **not supported**<br>Warehouse-connected products can be created as Shopee products, but their information cannot be synced |
| **Authorization Status** | Your Shopee shop authorization must be valid |


## Setup Steps { #operate-shopee-s4 }

### Step 1: Select Products and Start Publishing { #operate-shopee-s4-step-1-product }

1. Go to **Products > All Products**.
2. Use filters to find products faster:
    - **Shop Type**: Select `EC`.
    - **Created From**: Select `EC Website`.
    - **Not Connected Channel**: Select `Shopee store`.
3. Select the products to publish and click **更多操作 > 建立商品到蝦皮**.

![](../../../../assets/images/EC-後台-商品-所有商品-建立蝦皮商品01.en.png)

### Step 2: Edit Shopee-Specific Fields { #operate-shopee-s4-step-2-edit }

The system opens the Shopee information editing page, where you can fine-tune the content published to Shopee (**changes here do not affect your online store's original data**).

!!! warning "Shopee Product Listing Rules"
    To make sure products convert successfully, check that every field follows the [field rules](#reference-shopee-s4) so the import does not fail.

![](../../../../assets/images/EC-後台-商品-所有商品-建立蝦皮商品前編輯欄位01.en.png)

### Step 3: Check the Publishing Results { #operate-shopee-s4-step-3 }

1. Go to **APP MARKET > My Apps > CYBERBIZ CHANNEL BRIDGE**.
2. Switch to the **Activity Log** tab.
3. Check the publishing status. If it failed, click **Failure Reason** to see and fix the issue (common causes: duplicate SKUs or text that exceeds the length limit).
4. After publishing succeeds, the product changes to `已關聯` automatically. You can then turn on [inventory sync](step3-sync-inventory-with-shopee.md) or [product information sync](step5-sync-product-info-with-shopee.md).



## Field Rules { #reference-shopee-s4 }

To avoid publishing failures, follow Shopee's rules strictly:

| Field Name | Key Rules |
| :--- | :--- |
| **Product Name** | **More than 10 characters**<br>No spaces at the beginning or end |
| **Product Description** | Image height > 32px<br>Image width > 700px<br>Aspect ratio between 0.5 and 3.2<br>Image size up to 2MB<br>Up to 12 images |
| **Product Image** | Shopee Mall: Upload 3 to 9 images<br>Regular sellers: Upload 1 to 9 images<br>If you exceed this limit, the system uses the first 9 images by default |
| **Product Specification** | **Up to 2 variation combinations**（如尺寸 x 顏色）<br>原商品須有完整的商品款式組合，**No missing variants (see Example 1 below)**<br>Variation names up to 14 characters<br>Option names up to 20 characters<br>No spaces at the beginning or end |
| **Variant Images** | Make sure every variant has an image; if not, leave all variants without images<br>**Images for only some variants are not supported**<br>上限 1 張，超過會自動以第 1 張為預設<br>**With two variation levels, images can only be set by the first level (see Example 2 below)**<br> | Uses the image of the matching first-level option automatically |
| **Category** | Uses Shopee's category levels |
| **Shipping Settings** | Uses your Shopee shop's shipping options |
| **Pre-Order (Optional)** | Set a custom number of days to ship |

!!! example "Example 1: Complete Variant Combinations"
    If the variations are: Size (S/M/L) ✕ Color (Black/White)

    - **Correct Options**: (S/Black) (S/White) (M/Black) (M/White) (L/Black) (L/White)
    - **Incorrect Options**: (S/Black) (S/White) (M/Black) (L/Black)

!!! example "Example 2: How Variant Images Apply to Two-Level Variations"
    For products with two variation levels, the system only supports images by the **first level**. Each variant uses the image of the first option at that level as a shared image. You cannot set images for the second level separately.

    - If the variations are: Size (S/M/L) ✕ Color (Black/White).
    - The first level is Size (S/M/L), with 3 options (S/M/L).

    | Option | Online Store Variant Image | How It Applies | Shopee Variant Image |
    | ------- | --------- | ------- | --------- |
    | Size (S)| (S/Black/**Image A**）<br>（S/白/圖B）| **Image A** is the shared image for Size (S) | (S/Black/**Image A**）<br>（S/白/**Image A**)|
    | Size (M)| (M/Black/**Image C**）<br>（M/白/圖D）| **Image C** is the shared image for Size (M) | (M/Black/**Image C**）<br>（M/白/**Image C**)|
    | Size (L)| (L/Black/**Image E**）<br>（L/白/圖F）| **Image E** is the shared image for Size (L) | (L/Black/**Image E**）<br>（L/白/**Image E**)|


The table below shows how the system maps online store data to each field and which fields you can edit after import:

| Field Name | How It Is Filled In | Editable |
| :--- | :--- | :--- |
| **Product Name** | Filled in from the online store field | ✓ |
| **Product Description** | Filled in from the **Product Introduction** 欄位內容，並僅保留純文字與圖片<br>路徑：**Products > All Products > click a product > Product Description tab** | ✓ |
| **Product Image** | Filled in from the online store field | ✓ |
| **Product Specification** | Filled in with **variation names, option names, SKUs, and prices** | **✕** |
| **Variant Images** | Filled in from the online store field | ✓ |
| **Category** | Determined automatically by the product name | ✓ |
| **Shipping Settings** | **Left blank** | ✓ |
| **Pre-Order (Optional)** | **Left blank** | ✓ |



