---
title: "Set up Product Color Swatches and Variant Images - Drag-and-Drop Theme"
description: "Set up the color swatch feature for products on a drag-and-drop theme so shoppers see the matching image as soon as they pick a variant."
created: 2026-04-14 14:55
last_modified: 2026-07-06 10:22
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
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定色票功能
  - 款式圖片對應
features:
  - 拖拉版型
  - 色票功能
  - 款式圖片
prerequisites:
  - ec/products/create-and-manage/create-update-products/
related:
  - ec/products/create-and-manage/product-swatches-variant-images-default/
  - ec/products/create-and-manage/create-update-products/
  - ec/integrations/fb/mbe/setup-fb-instagram-shop/
tags:
  - "Color Swatches"
  - "Variant Images"
  - "Drag-and-Drop Theme"
  - "Swatches"
  - "Variant Image Mapping"
acoiv: 
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 款式選單
  - 圖片視窗
paths:
  - 商品 > 所有商品
  - 網站外觀 > 套版主題管理 > 網站設定 > 全站設定
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4833
  - https://www.cyberbiz.io/support/?p=31319
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/product-swatches-variant-images-drag-drop/"
comments: false
search:
  exclude: false
icon: lucide/swatch-book
hide: []
---

![Color variant settings](../../../assets/images/ec-商品-顏色款式設定.en.png){ title="Color Variant Settings" .hero-page }

## About Product Color Swatches

The **color swatch feature** lets customers click a specific variant (such as a color, outfit, or option) while browsing a product on the storefront and instantly see the images for that variant. This helps customers understand product details and increases purchase intent.

!!! warning "Notes"
    *   **Bonus Mall** does not currently support color swatches.
    *   To make product images in your Facebook shop change correctly with the color as well, we strongly recommend turning on this feature and placing images in color order.

## Prerequisites and Limits

- [x] This feature is **available only to users of the drag-and-drop theme**.
- [x] It applies to plans that support the drag-and-drop theme, such as Enterprise and PLUS.

!!! info "Default Theme Users"
    If you use the default theme, see [Set Up Product Color Swatches and Variant Images - Default Theme](product-swatches-variant-images-default.md){ title="Set Up Product Color Swatches and Variant Images - Default Theme" }.

## Steps

### Admin Settings

1. **Open the product edit page**: Go to **Products > All Products** and click **Add Product** or search for and select an existing product to open the edit page.
1.  **Create a multiple variant product**:

    *   After you finish the [basic product settings](create-update-products.md#operate-product-create-basic){ title="Add and Update Products" }, click "Create a multiple variant product" or "Edit Options".
    - Click **Create an option**, name it "Color" (or a custom variant name), and add items under it (such as Red and Blue). When you are done, click **Save** in the pop-up window and then **Save** at the bottom of the product edit page to apply the options.

    ![Add a color option](../../../assets/images/ec-商品-新增顏色款式.en.gif){ title="Add a Color Option" }

3.  **Upload variant images**:

    *   After you save the options, an **image window icon** appears in front of each option name.

    !!! warning "If you don't see the image window icon, the options haven't been fully applied. Click **Save** at the bottom of the page, then refresh to see the feature."

    *   Click the icon to upload variant images by dragging files from a folder or by choosing images to upload.
    *   After uploading, choose the image for each specific variant.

    ![Set color variant images](../../../assets/images/ec-商品-設定顏色規格圖片.en.gif){ title="Set Color Variant Images" }

4.  **Check image sync**: Images uploaded in the variant menu also appear in the product's main image list.

    ![Color variant images](../../../assets/images/ec-商品-商品圖片-顏色款式.en.png){ title="Color Variant Images" }

5.  **Save and preview**: When you are done, click "Save Settings" at the top, then click "Go to Product Page" to see the [storefront display](#Storefront-Display).

    ![Go to Product Page](../../../assets/images/ec-商品-商品編輯頁-前往該商品.en.png){ title="Go to Product Page" }

---

### Show Swatches on Storefront Product List Pages <small>Global Setting</small> { #enable-swatch-on-product-list }

!!! plan "Prerequisites and Limits"
    - [x] You have completed the [admin settings](#Admin-Settings)
    - [x] You have the **Enterprise** plan

To show swatch thumbnails on product list pages (such as collection pages and multi-level product category pages), complete the following global settings:

1.  Go to the Global Settings page: Website Appearance > Theme Setting > Detail Settings > Global Settings.
2.  Find the "Product Settings" section.
3.  Select "**Show product swatch thumbnails**" and click **Save** to apply the changes.
4.  **Where they appear**: Swatch thumbnails then appear on list pages such as collection pages and multi-level product category pages.

![Swatch cards on a collection page](../../../assets/images/ec-網站外觀-全站設定-商品色票小卡-商品群組頁.en.png){ title="Swatch Cards on a Collection Page" }

## Storefront Display

On the product page, swatch thumbnails for each color variant appear below the product, so customers can click to preview how each variant looks.

=== ":lucide-gallery-thumbnails: Before a Variant Is Selected"
    Customers can see all of the product's images.

    ![No color variant selected](../../../assets/images/ec-商品-顏色款式未選擇-前台.en.png){ title="No Color Variant Selected" }

=== ":lucide-mouse-pointer-click: After a Variant Is Selected"
    The system automatically filters the images and shows only those linked to that variant (such as a specific color).

    ![Color variant selected](../../../assets/images/ec-商品-顏色款式已選擇-前台.en.png){ title="Color Variant Selected" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-store:{ .lg }  
  [__Facebook Shop Settings__](../../integrations/fb/mbe/setup-fb-instagram-shop.md){ title="Set Up Facebook and Instagram Shops" }  
  After you set up swatches, you can set up Facebook and Instagram shops so product images show multiple variants on social platforms.

</div>


## FAQ

??? quote "Does Bonus Mall support color swatches?"

    **Bonus Mall** does not currently support color swatches. To make product images in your Facebook shop change correctly with the color as well, we strongly recommend turning on this feature and placing images in color order.

??? quote "Why can't I see the image window icon?"

    If you don't see the image window icon, the options haven't been fully applied. Click **Save** at the bottom of the page, then refresh to see the feature.

??? quote "Which plan do swatch thumbnails on product list pages require?"

    Swatch thumbnails on product list pages are exclusive to the **Enterprise** plan. After setup, they appear on list pages such as collection pages and multi-level product category pages.

