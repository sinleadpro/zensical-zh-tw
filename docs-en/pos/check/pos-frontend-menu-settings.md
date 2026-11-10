---
title: "POS Front-End Menu Settings"
description: "Learn how to set up the POS front-end graphical product menu with multi-level categories to speed up checkout for items without barcodes, such as food and bulk goods."
created: 2026-06-01 16:22
last_modified: 2026-06-01 16:22
lang: en-US
type: guide
author: Ann
reviewers: []
notes: 
  - 內部連結
ga_views: 0
feedback: 0
products: 
  - POS
modules:
  - POS 前台
  - 商品
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
  - 設定 POS 前台選單
  - 建立商品多層級分類
  - 提升 POS 結帳效率
features: 
  - POS 選單
  - 商品多層級分類
  - 圖形化介面
prerequisites: 
  - "建議先完成「自訂群組」或「商品類型」設定"
related:
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/create-and-manage/edit-product-description-settings/
tags: 
  - POS
  - product_menu
  - multi_level_categories
  - checkout_optimization
acoiv: configure
apis: []
devices: 
  - tablet
  - desktop
ui_components: 
  - POS 選單設定
  - 商品多層級分類
paths:
  - 商品 > 商品多層級分類
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=11224
permalink: "https://help.cyberbiz.io/pos/check/pos-frontend-menu-settings/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# POS Front-End Menu Settings
Use the graphical menu on the POS front end so staff can quickly tap products to add them to the cart without scanning barcodes one by one. This feature is especially useful for food and bulk products, or for mobile checkout with a tablet.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Items Without Barcodes**: Products that cannot be labeled, such as bread, cakes, and bulk produce.
    - **Fast Checkout**: Create shortcut menus for popular products to reduce the time staff spend searching.
    - **Tablet Use**: When checking out on a tablet at a mobile stall or exhibition, the graphical interface is more intuitive.


## Before You Start { #prerequisites-menu-settings }

- **Prerequisites**: We recommend setting up **[Custom Groups](../../ec/products/categories-and-tags/custom-collections.md)** or **[Product Types](../../ec/products/create-and-manage/edit-product-description-settings.md#operate-product-desc-settings)** first so you can link them directly when you create menus.
- **Image Requirements**:
    - Recommended size: `80 x 80 px`.
    - File size: Do not exceed `2 MB`.
- **Menu Structure**: The system supports a three-level structure (main category > subcategory > product item).


## Step 1: Create Multi-Level Product Categories { #operate-menu-settings }

Before you set up the POS menu, define the category logic for your products.


1. Log in to the CYBERBIZ admin dashboard and go to **Products > Multi-level Product Categories**.
2. Click the **POS Setting** tab.
3. Click **Add Category**: This is the first level of the menu (main category, such as cakes or beverages).
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單2.png){ .screenshot }
4. **Add a Second-Level Category**:
    - Click the **+** icon next to the first-level category.
    - Select a link type: Link to an existing **Custom Group** or **Product Type**.
    - Edit the category name and upload a representative image.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單3.png){ .screenshot }



## Step 2: Enable and Configure the POS Menu { #operate-step-b-enable-pos }

After you define the categories, add them to the POS front-end menu and sort them.


1. Log in to the CYBERBIZ admin dashboard and go to **POS > POS Store List**.
1. Go to the target store and click the **Product Menu Settings** tab.
2. Turn on the **Enable Feature** toggle.
3. Click **Add a new category**, then select the multi-level categories you created in Step 1.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單4.png){ .screenshot }
4. **Adjust Order and Remove Items**:
    - Drag the handle icon to change the order in which menu items appear on the front end.
    - To remove an item you no longer need to display, click the trash can icon.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單5.png){ .screenshot }


## Front-End Preview { #overview-menu-settings }

After setup, staff can see the menu structure shown below on the POS front end:

1. **Level 1**: Main category (such as cakes).
2. **Level 2**: Subcategory (such as loaf cakes).
3. **Level 3**: Individual product items (tap to add to the cart).

![](https://www.cyberbiz.io/support/wp-content/uploads/POS商品選單1.png){ .screenshot }

