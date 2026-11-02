---
title: "Set up Product Color Swatches and Variant Images - Default Theme"
description: "Set up color swatches and variant images for products on the default theme so shoppers can browse and pick variants at a glance."
created: 2026-04-17 10:50
last_modified: 2026-06-30 11:26
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
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定商品色票功能
  - 款式圖片對應
  - 商品多款式設定
features:
  - 色票功能
  - 款式圖片
  - 預設版型
prerequisites:
  - ec/products/create-and-manage/create-update-products/
related:
  - ec/products/create-and-manage/product-swatches-variant-images-drag-drop/
  - ec/products/create-and-manage/create-update-products/
tags:
  - "Color Swatches"
  - "Variant Images"
  - "Default Theme"
  - "Product Images"
  - "Variant Options"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
  - 網站外觀 > 套版主題管理 > 網站設定 > 商品群組與商品頁設定 > 商品頁設定
layouts:
  - classic
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=958
  - https://www.cyberbiz.io/support/?p=2018
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/product-swatches-variant-images-default/"
comments: false
search:
  exclude: false
icon: lucide/swatch-book
hide: []
---

![Product page settings - swatches - default theme](../../../assets/images/ec-網站外觀-商品頁設定-商品色票-預設版型.en.png){ title="Product Page Settings - Swatches - Default Theme" .hero-page }

## About Color Swatches

The **color swatch feature** lets customers see all of a product's variants (such as colors or patterns) at a glance while browsing a product page or collection page. When they select a variant, the page shows the matching variant images so they can understand the product details.

!!! info "Drag-and-Drop Theme Users"
    If you use the drag-and-drop theme, see [Set Up Product Color Swatches and Variant Images - Drag-and-Drop Theme](product-swatches-variant-images-drag-drop.md){ title="Set Up Product Color Swatches and Variant Images - Drag-and-Drop Theme" }.

## Prerequisite: Turn on the Display Settings

Before you use this feature, turn on the related settings in the admin. Otherwise, swatches won't appear on product pages.

1. **Go to the settings page**: "Website Appearance" > "Theme Setting" > "Detail Settings" > "Collection and Product Page Settings" > "Product Page Settings".
2. **Turn on the feature**: Select the swatch display options (**Show product swatches** and **Expand product swatches**) and click **Save** to apply the changes.

![Product swatches - product list page display - default theme](../../../assets/images/ec-網站外觀-商品色票-前台商品列表頁-預設版型.en.png){ title="Product Swatches - Product List Page Display - Default Theme" }

## Swatch and Option Setup Flow

### Step 1: Set up Swatch Icons

The system pairs variant photos with swatch icons automatically based on the images' relative positions. Upload the images to the "Product Image" section (for upload requirements, see [Add a Product: Product Images and Videos](create-update-products.md#operate-product-create-media){ title="Add and Update Products" }) and follow the "images first, colors second" ordering logic.

1. **Open the edit page**: Go to Products > All Products and add a product or edit an existing one.
2. **Upload images**: In the "Product Image" section, upload the **product images** for all variants and the matching **swatch images**.
3. **Adjust the order**: Use the :lucide-move: icon on the images to drag and drop them into two groups:

    - **First half (images)**: Arrange the variant images of each variant in order (for example, brown shoe, blue shoe).
    - **Second half (colors)**: Arrange the swatch icons in the matching positions (for example, brown swatch, blue swatch).

!!! warning "Ordering Warning"
    The number of photos and swatches must match, and their order must correspond (the 1st image on the left matches the 1st swatch on the right). If they are interleaved or the counts don't match, the storefront swatches cannot link correctly to the variant images.

![Product images - swatch order](../../../assets/images/ec-商品-商品圖片-色票排序-預設版型.en.png){ title="Product Images - Swatch Order" }

---

### Step 2: Manage Variant Options (Key Step)

After you [upload the images](#Step-1-Set-up-Swatch-Icons), scroll down to the "Variants and Inventory" section. For the system to match swatches correctly, the order and names of the options have strict requirements.

1.  **Option order**: To use swatches, set "**Color**" as the **first option**. Otherwise, the storefront won't display them correctly.
2.  **Option names**:
    *   Name the first option "**Color**" and add color items in the same order as the images you uploaded.
    *   If needed, name the second option "**Size**" (the option name must be exactly 尺寸, the Chinese word for "size").
3.  **Other variants**: After the first two options are set, continue with any additional variant options.

![Product swatch variant settings](../../../assets/images/ec-商品-商品色票款式設定-預設版型.en.png){ title="Product Swatch Variant Settings" }

---

### Step 3: Fill in Product Variant Details

After you set the options, the system generates the variant list automatically. Complete the inventory and details for each variant combination.

1.  Fill in the details of each variant in the color and size order you set above.
2.  **Inventory management**: Choose whether to "Manage Inventory" and enter the product inventory. The storefront shows availability based on this.

![Product variant management - inventory settings](../../../assets/images/ec-商品-款式設定-庫存管理.en.gif){ title="Product Variant Management - Inventory Settings" }

---

### Step 4: Storefront Display

![Product swatches - storefront - default theme](../../../assets/images/ec-商品色票-前台-預設版型.en.png){ title="Product Swatches - Storefront - Default Theme" }

## FAQ

??? quote "Where do product swatches appear?"

    Swatches are expanded on the **Collection** page (Category/Collection Page), where each color variant of the product appears directly in the collection list.

    ![Product swatches - collection page - storefront](../../../assets/images/ec-商品色票-前台-商品群組頁-預設版型.en.png){ title="Product Swatches - Collection Page - Storefront" }

??? quote "How do I turn off swatches if I don't want to use them?"

    If you don't need this feature, turn off "Show product swatches" in "Detail Settings".

??? quote "Does this feature work with all themes?"

    This guide applies only to the **default theme**. If you use the drag-and-drop theme, see [Set Up Product Color Swatches and Variant Images - Drag-and-Drop Theme](product-swatches-variant-images-drag-drop.md){ title="Set Up Product Color Swatches and Variant Images - Drag-and-Drop Theme" }.

??? quote "What are the upload requirements for swatch images?"

    Upload the images to the "Product Image" section and follow the "images first, colors second" ordering logic. In the first half, arrange the variant images of each variant in order (for example, brown shoe, blue shoe). In the second half, arrange the swatch icons in the matching positions (for example, brown swatch, blue swatch). The number of photos and swatches must match, and their order must correspond exactly.

??? quote "Why don't the storefront swatches link correctly to the variant images?"

    Possible reasons include:

    - The number of photos and swatches doesn't match
    - The images are interleaved instead of grouped in two parts
    - "Color" is not set as the first option

??? quote "Can I customize option names?"

    The first option must be named "**Color**" to enable swatches. If needed, name the second option "**Size**" (the option name must be exactly 尺寸, the Chinese word for "size").

