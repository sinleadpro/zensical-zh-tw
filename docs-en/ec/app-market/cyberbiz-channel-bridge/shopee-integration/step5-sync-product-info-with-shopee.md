---
title: "Step 5: Sync Product Information Between Your Online Store and Shopee"
description: "After linking products, use product information sync to keep product data consistent between your online store and Shopee shop. When you change content or prices in your online store, sync them to Shopee in one click without editing twice."
created: 2026-02-25 00:00
last_modified: 2026-06-27 13:40
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
  - APP MARKET
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
plan_options: []
cyb_extensions:
  - CHANNEL BRIDGE
intents:
  - 設定同步開關
  - 編輯共用欄位
  - 執行資訊更新
features:
  - 蝦皮商品搬站
  - 商品資訊同步
prerequisites:
  - "Step 1~4，確保商品已建立關聯"
  - "官網商品欄位需符合蝦皮規範"
related: 
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step3-sync-inventory-with-shopee/
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step4-create-shopee-products-from-site/
tags: []
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - APP MARKET > 我的擴充服務 > CYBERBIZ CHANNEL BRIDGE
  - 商品 > 所有商品 > 點擊商品 > 商品資訊頁籤
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12690
  - https://www.cyberbiz.io/support/?p=5362
permalink: "https://help.cyberbiz.io/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step5-sync-product-info-with-shopee/"
comments: false
search:
  exclude: false
icon: lucide/info
hide: []
---
# Step 5: Sync Product Information Between Your Online Store and Shopee

After linking products, use product information sync to keep product data consistent between your online store and Shopee shop. When you change images, text, or prices in your online store, sync them to Shopee in one click without editing twice.
{ .subtitle }

[:lucide-lock:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHANNEL BRIDGE
{ .doc-badge }

![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-畫面總覽01.en.png){ .hero-page }




!!! tip "Use Cases"
    - **Update Prices Together**: When you change prices for a promotion in your online store, update the Shopee price at the same time.
    - **Refresh Visuals**: When you replace a product's main or lifestyle images in your online store, sync them to your Shopee shop too.
    - **Correct Variants**: After you fix product variants or SKUs in your online store, make sure Shopee is updated as well.



## Before You Start { #prerequisites-shopee-s5 }

- **Sync Direction**: Sync is one-way only, **from your online store to Shopee**. Changes made on Shopee are not written back to your online store.
- **Type Restrictions**: POS products, fast delivery products, and warehouse-connected products are **not supported**.
- **Linked Products**: [Link](step3-sync-inventory-with-shopee/#operate-shopee-s3-step-1-create) your online store products with Shopee products before you continue.
- **Sync Unit**: Updates are made **per product**. If any variant of a product is linked, syncing updates **all variants** of that product.


## Setup Steps { #operate-shopee-s5 }

### Step 1: Turn on Field Sync { #operate-shopee-s5-step-1-enable }

Choose which fields to sync based on your business needs:

1. Go to **APP MARKET > My Apps > CYBERBIZ CHANNEL BRIDGE**.
2. Open the **Shopee Products** page and click **Advanced Settings**.
3. In the **Product Information** section, turn on the fields you want to sync:
    - **Product Name**
    - **Product Image**
    - **Product Price**
4. Click **Save**.

![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-開啟商品資訊同步01.en.png)


### Step 2: Edit Product Fields { #operate-shopee-s5-step-2-edit }

Before syncing, make sure both types of information below are complete:

1. **Shared Information**: Go to **Products > All Products > 點擊商品 > 商品資訊頁籤**.
    - See the [list of synced fields](step5-sync-product-info-with-shopee/#reference-sync-fields) below.
2. **Shopee Required Fields**: Switch to the **Channel Setting** tab.
    - See the [Shopee required fields](step5-sync-product-info-with-shopee/#reference-fields) below.
    ![](../../../../assets/images/EC-後台-商品-所有商品-設定商品通路頁籤01.en.png)

### Step 3: Update the Information { #operate-shopee-s5-step-3 }

1. Go to **Products > All Products**.
2. Select the products to update (they must be linked).
3. Click **更多操作 > 更新商品資訊到蝦皮**.
4. The system schedules the sync. Check the results later on the **Activity Log** tab.

![](../../../../assets/images/EC-後台-商品-所有商品-將商品資訊更新到蝦皮01.en.png)

!!! warning "Field Format Rules"
    Before syncing, make sure the content follows [Shopee's rules](step4-create-shopee-products-from-site/#reference-shopee-s4) so the sync does not fail.

## Checklist { #reference-shopee-s5 }

Make sure all of the following are set up correctly for information sync to work:

- [x] Online store products are linked with Shopee products
- [x] The product information sync switch is on
- [x] You ran the product information update from the product list
- [x] Online store product fields follow Shopee's rules

## Synced Fields { #reference-sync-fields }

| Category | Online Store Field | Shopee Field | Can Sync Separately |
| :--- | :--- | :--- | :---: |
| **Product Management** | Product Name | Product Name | ✓ |
| | Product Images | Product Images | ✓ |
| **Manage Variants** | Variants | Variations | ✕ |
| | Variant Images | Variation Images | ✕ |
| | Price | Price | ✓ |
| | Product Number (SKU) | Variation SKU | ✕ |
| | Weight | Weight | ✕ |



## Shopee Required Fields { #reference-fields }


- **Category**
- **Brand**
- **Product Introduction**
- **Shipping Settings**
- **Pre-Order**
