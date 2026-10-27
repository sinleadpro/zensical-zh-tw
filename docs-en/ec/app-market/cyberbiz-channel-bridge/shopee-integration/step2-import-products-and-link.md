---
title: "Step 2: Import Products and Create Links"
description: "After authorizing your shop, import Shopee product information to your online store in bulk and use automatic matching to categorize and publish products quickly."
created: 2026-02-25 00:00
last_modified: 2026-07-07 12:00
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：商品大量填補sku
ga_views: 0
feedback: 0
products:
  - EC
modules:
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
  - 批量匯入蝦皮商品
  - 建立官網商品
  - 分類自動同步
features:
  - 蝦皮商品搬站
  - 全通路管理助手
  - 商品自動關聯
prerequisites:
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step1-install-and-activate/
  - 建議預先整理蝦皮端的 SKU (商品選項貨號)
related: []
tags: []
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - APP MARKET > 我的擴充功能
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5923
  - https://www.cyberbiz.io/support/?p=46486
permalink: "https://help.cyberbiz.io/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step2-import-products-and-link/"
comments: false
search:
  exclude: false
icon: lucide/link
hide: []
---
# Step 2: Import Products and Create Links

After you authorize your shop, you can import Shopee product information into your online store in batches and use automatic matching to categorize and list products quickly.
{ .subtitle }

[:lucide-lock:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHANNEL BRIDGE
{ .doc-badge }

![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-畫面總覽01.en.png){ .hero-page }




!!! tip "Use Cases"
    - **List Products Fast**: Import best-selling Shopee products into your online store in one click, with all variants, images, and text brought over automatically.
    - **Automatic Categorization**: Use Shopee's existing three-level categories to create matching custom categories in your online store automatically.
    - **Initial Inventory Alignment**: Get Shopee's current inventory and prices during import as the starting point for your online store.


## Before You Start { #prerequisites-shopee-s2 }

- **SKU (Variation SKU) Rules**: **The SKU is the key identifier for migration**. It cannot contain spaces, line breaks, or Chinese characters. If a SKU is duplicated or in the wrong format, the system skips that variant or cannot create the product.
- **Content Sync Limits**:
    - The system only captures Shopee data **at the time of import**. Later changes on Shopee are **not** synced to your online store automatically.
    - Videos cannot be moved (only YouTube embed links are supported).
- **Image Limits**: Only JPG, JPEG, PNG, and GIF are supported. Total image size per product is limited to 100MB.
- **Import Scope**: Only products with the **Live**, **Under Review**, or **Unlisted** status in Shopee Seller Centre are supported. Products marked **Violation/Deleted** or **Not Yet Published** are not imported.
- **Working Environment**: Do not close the web page during import, or the process may be interrupted.
- **Product Name Format**: Uncommon symbols are converted to spaces automatically. We recommend fixing them in advance.

## System Integration (POS/Warehouse) { #intro-shopee-s2 }

When your online store (EC) is connected to a POS or warehouse system, the SKU (stock keeping unit) is required for the systems to connect correctly. To avoid data conflicts and keep later operations running smoothly, follow the guidance below:

1. **Make Sure Every SKU Is Unique and Complete**

    If your online store (EC) is also connected to a POS or warehouse system, every product SKU must be unique and cannot be empty.

    - **Avoid Duplicates**: If an imported Shopee product's SKU matches an existing product in the EC admin, the system blocks it and shows an error message.
    - **Do Not Leave It Blank**: The SKU is how the system identifies products. If a product has no SKU yet, be sure to add one.

2. **How to Fix Duplicate SKUs**

    If the system detects a duplicate SKU, fix it using either of these methods:

    - **Option A: Update Manually**: Find the duplicate product on the EC product list page and change its SKU and variant information manually.
        ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-手動修改SKU01.en.png)
    - **Option B: Import Again**: Delete the duplicate product in EC, change the **Variation SKU** in Shopee Seller Centre, and run the import again once everything is correct.

3. **Bulk Handling Tip**

    If you do not have all SKU information ready when creating products in your online store, create the products first and later use [Bulk Fill In Product SKUs]() to add them all at once.



## Setup Steps { #operate-shopee-s2 }

### Step 1: Import Shopee Products { #operate-shopee-s2-step-1-import }

1. Log in to the CYBERBIZ admin and go to **APP MARKET > 我的擴充功能**.
2. Find **CYBERBIZ CHANNEL BRIDGE** and click **Settings**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店03.en.png)
3. On the **Product Management** tab, click **Import Shopee Products**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-匯入蝦皮商品01.en.png)
4. When the progress bar finishes, the list shows all imported Shopee product information, including:
    - **Price/Inventory**: The current values on Shopee.
    - **Link Status**: `未關聯` means the product has not been created in your online store yet.

### Step 2: Create Online Store Products and Sync Categories { #operate-shopee-s2-step-2-create }

1. On the **Product Management** tab, select the products you want to create in your online store.
2. Click **Create Products**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-建立官網商品01.en.png)
3. In the pop-up window, choose whether to select **Sync Shopee product categories to online store custom categories automatically**.
    ![](../../../../assets/images/蝦皮-後台-我的商品-商品詳情-商品後台類別01.en.png)
    - **Same Name**: The product is added to the existing custom category with the same name.
    - **Different Name**: The system creates a new custom category in your online store (up to Shopee's first three category levels).
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-建立官網商品02.en.png)
4. Click **Run** to confirm. The system matches categories and creates the products automatically.
5. After the products are created, the link status changes to `已關聯`, and **Go to Store Product** :lucide-external-link: appears.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-建立官網商品03.en.png)


### Step 3: Get Ready to Publish { #operate-shopee-s2-step-3 }

New products are **listed but hidden** by default. Click **Go to Store Product** :lucide-external-link: and check the following:

- **Shipping Methods and temperature zone**: The system cannot set your store's own shipping rules automatically, so select them manually.
- **bonus redemption**: Set the product's bonus redemption cap as needed.
- **Fill In SKUs**: If SKUs were left blank during import, be sure to add them (especially if you use a POS or warehouse system).



## Shopee and Online Store Field Mapping { #reference-shopee-s2 }

| Category | Shopee Field | CYBERBIZ Online Store Field |
| :--- | :--- | :--- |
| **Product Info** | Product Name | Product Name |
| | Product Images | Product Images |
| **Variant Management** | Variations | Product Variants |
| | Promotional Price | Price |
| | Price | List Price |
| | Variation SKU | **Product Number (SKU)** |
| | Stock | Inventory |
| | Parcel Size | Volume |
| | Weight | Weight |
| | Variation Image | Variant Image |
| **Product Description** | Product Description | Product Introduction |



## FAQ { #faq-shopee-s2 }

??? quote "Are videos in Shopee product descriptions moved?"
    Only videos added as **YouTube embed links** are supported. Videos uploaded directly to Shopee cannot be moved.

??? quote "How do I sync products newly added on Shopee?"
    Click **Sync Shopee Products**. The system pulls new products from your Shopee shop that **have not been imported yet**. Linked products are not updated again.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-管理蝦皮商品01.en.png)


