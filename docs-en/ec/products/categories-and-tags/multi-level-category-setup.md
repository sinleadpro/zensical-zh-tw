---
title: "Set up Multi-Level Product Categories"
description: "Create multi-level product categories (up to three levels) to organize collections and support marketing campaigns and navigation bar settings."
created: 2026-01-13 00:00
last_modified: 2026-09-18 14:10
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
  - 行銷活動
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
cyb_extensions: []
intents:
  - 如何設定商品多層級分類
  - 商品分類架構設定
features:
  - 商品多層級分類
  - 拖拉版型
prerequisites:
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - "Product Types"
related:
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - ec/products/create-and-manage/edit-product-description-settings/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/marketing/discounts/multi-level-category-discount/
  - pos/check/pos-frontend-menu-settings/
tags:
  - Collections
  - "Multi-Level Categories"
  - "Website Settings"
  - "Marketing Campaigns"
  - "Navigation Bar"
  - POS
  - "Customized Collections"
  - "Conditionalized Collections"
  - "Product Type"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 商品多層級分類
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=9204
  - https://www.cyberbiz.io/support/?p=43450
permalink: "https://help.cyberbiz.io/ec/products/categories-and-tags/multi-level-category-setup/"
comments: false
search:
  exclude: false
icon: lucide/network
hide: []
---
# Set up Multi-Level Product Categories
Create multi-level product categories (up to three levels) to organize collections and support marketing campaigns and navigation bar settings.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    In PLUS plans, Multi-level Product Categories is an optional module (choose 2 of 11), so you must make sure you have selected it before you can use it. The Enterprise plan includes this feature.

![Multi-level product category settings](../../../assets/images/ec-product-multi-level-product-cateogry-hero.zh-tw.en.png){ title="Multi-Level Product Category Settings" .hero-page }

## About Multi-Level Product Categories

Multi-level product categories organize **product collections** from different sources (including customized collections, conditionalized collections, and product types). Think of them as a **folder structure for collections** that helps you build a clear, adjustable product category structure.

After you set up multi-level categories, you can apply **navigation bar display settings** and **marketing campaign rules** by category level to support storefront browsing and category-based marketing.


??? info-clean "Category Levels"

    Multi-level product categories support up to a **three-level structure** (from top to bottom):

    - **Top level (main category)**: The top-level category folder, used to broadly organize the product types across the store.
    - **Middle level (subcategory)**: Created under a main category to further divide the category logic.
    - **Bottom level (sub-subcategory)**: Maps to an actual product collection, which can come from:

        - Customized collections
        - Conditionalized collections
        - Product types on the product settings page

!!! tip "Category Folders"

    Multi-level product categories are used only to **manage the category structure**. Each category level works like a folder:

    - Changing category levels or their order doesn't affect the product lists in the collections
    - Whether a product is shown still depends on the settings of its collection

## Use Cases

We recommend multi-level product categories in the following situations:

- You have many products, and a single category level can't organize them clearly
- The same product needs to appear in different categories (for example, by use or by customer group)
- You need to set up the navigation bar, category pages, or marketing campaigns by category level

## Steps

### Two-Level Structure

??? info-clean "Two-Level Structure Diagram"
    ```mermaid
    flowchart TD
        %% Layer labels
        L1[Main Category]:::layer --> L2[Sub-subcategory]:::layer

        %% Top-level categories
        A[Food] --> A1[Dry Noodles]
        A --> A2[Meal Kits]

        B[Pets] --> B1[Canned Food]
        B --> B2[Snacks]

        C[Household Goods] --> C1[Hand Soap]
        C --> C2[Cookware]

        %% Styling for layer labels
        classDef layer fill:#f2f2f2,stroke:#ccc,stroke-width:1px,font-weight:bold;

    ```
1. Log in to the CYBERBIZ admin and go to **Products > Multi-level Product Categories**.
2. Click **Add a new category** and enter the **Category title** and **Category path** on the new category page.

	![New category page](../../../assets/images/ec-product-multi-level-product-cateogories-add-category.zh-tw.en.png){ title="New Category Page" }

3. Under the main category, click **Add**.
	- New category option: Select **Collection** and enter the **Category title** and **Category path**.
	- For the collection type, choose "Customized Collections", "Conditionalized Collections", or "Product Type", then select the specific collection below.
	

	![Add sub-subcategory settings](../../../assets/images/ec-multi-level-product-cateogry-collection.zh-tw.en.png){ title="Add Sub-Subcategory Settings" }


    !!! info "A sub-subcategory is a product collection. For related settings, see [Set Up Customized Collections](custom-collections.md){ title="Set Up Customized Collections" }, [Set Up Conditionalized Collections](smart-collections.md){ title="Set Up Conditionalized Collections" }, and [Product Type](../create-and-manage/edit-product-description-settings.md#Advanced-Settings){ title="Edit Product Descriptions and Product Settings" }."

4. The completed setup

	![Completed two-level structure](../../../assets/images/ec-multi-level-product-two-layers.zh-tw.en.png){ title="Completed Two-Level Structure" }

5. Click and drag :lucide-grip-vertical: to change the category order or move a subcategory under another main category.
   
    !!! info "A sub-subcategory cannot be moved under another subcategory. Add the sub-subcategory directly under the subcategory you want."

### Three-Level Structure

??? info-clean "Three-Level Structure Diagram"
    ```mermaid
    flowchart TD
        %% Layer labels
        L1[Main Category]:::layer --> L2[Subcategory]:::layer --> L3[Sub-subcategory]:::layer

        %% Main categories
        Men["Menswear"] --> Men_Tops["Tops"] --> Men_Tops_Tshirt["Men's T-Shirts"]
        Men_Tops --> Men_Tops_Shirt["Men's Shirts"]
        Men --> Men_Pants["Pants"] --> Men_Pants_Jeans["Men's Jeans"]
        Men_Pants --> Men_Pants_Suit["Men's Suit Pants"]
        Men --> Men_Shorts["Shorts"] --> Men_Shorts_Casual["Men's Casual Shorts"]

        %% Styling for layer labels
        classDef layer fill:#f2f2f2,stroke:#ccc,stroke-width:1px,font-weight:bold;
    ```

1. Log in to the CYBERBIZ admin and go to **Products > Multi-level Product Categories**.
2. Click **Add a new category** and enter the **Category title** and **Category path** on the new category page.
	
	![New category page](../../../assets/images/ec-product-multi-level-product-cateogories-add-category.zh-tw.en.png){ title="New Category Page" }

3. Under the main category, click **Add**.
	- "New category option": Select **Category** and enter the "Category title" and "Category path".

	![Add subcategory settings](../../../assets/images/ec-multi-level-product-category-collection.zh-tw.en.png){ title="Add Subcategory Settings" }

4. Under the subcategory, click "Add".
	- New category option: Select **Collection** and enter the **Category title** and **Category path**.
	- For the collection type, choose "Customized Collections", "Conditionalized Collections", or "Product Type", then select the specific collection below.

	![Add sub-subcategory settings](../../../assets/images/ec-multi-level-product-cateogry-collection.zh-tw.en.png){ title="Add Sub-Subcategory Settings" }

	!!! info "A sub-subcategory is a product collection. For related settings, see [Set Up Customized Collections](custom-collections.md){ title="Set Up Customized Collections" }, [Set Up Conditionalized Collections](smart-collections.md){ title="Set Up Conditionalized Collections" }, and [Product Type](../create-and-manage/edit-product-description-settings.md#Advanced-Settings){ title="Edit Product Descriptions and Product Settings" }."

5. The completed setup

	![Completed three-level structure](../../../assets/images/ec-multi-level-product-cateogry-three-layers.zh-tw.en.png){ title="Completed Three-Level Structure" }
	
6. Click and drag :lucide-grip-vertical: to change the category order or move a subcategory under another main category.

    !!! info "A sub-subcategory cannot be moved under another subcategory. Add the sub-subcategory directly under the subcategory you want."

## Next Steps

<div class="grid cards" markdown>

- :lucide-menu:{ .lg }  
  [__Menu and Navigation Bar Settings__](../../../ec/website-appearance/navigation/setup-menus-navigation.md){ title="Set Up Menus and the Navigation Bar" }  
  Bind multi-level categories to the navigation bar to improve the shopping flow and experience.
- :lucide-layers:{ .lg }  
  [__Multi-Level Category Threshold Discounts__](../../../ec/marketing/discounts/multi-level-category-discount.md){ title="Set Up Multi-Level Category Threshold Discounts" }  
  Set threshold discounts by category level that apply automatically to eligible products.
- :material-point-of-sale:{ .lg }  
  [__POS Frontend Menu Settings__](../../../pos/check/pos-frontend-menu-settings.md){ title="POS Frontend Menu Settings" }  
  Manage products and create POS frontend menus for in-store display and operation.


</div>

## FAQ

??? quote "Do multi-level product categories affect product lists?"
    No. Multi-level product categories only organize collections and don't affect the product lists in them.

??? quote "When is a three-level structure not a good fit?"  
	- Your products are of a single kind or few in number, so one or two levels are enough.  
	- Your store doesn't need to bind the navigation bar or marketing campaigns at category levels.  
	- You want to avoid unnecessary management complexity and lower maintenance costs.

??? quote "What is the difference between a subcategory and a sub-subcategory?"  
	- **Subcategory**: Sits under a main category to further divide the category logic, mainly as a folder structure.  
	- **Sub-subcategory**: Maps to an actual collection, which can come from customized collections, conditionalized collections, or product types.
