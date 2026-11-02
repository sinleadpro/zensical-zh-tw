---
title: "Set up Site Search"
description: "Set up site search, including the search scope, word segmentation logic, admin management, and GA4 tracking settings."
created: 2026-04-15 10:20
last_modified: 2026-06-30 11:26
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify 商品群組名稱url/slug的問題
ga_views:
feedback:
products:
  - EC
modules:
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定站內搜尋
  - 排除商品搜尋
features:
  - 分詞搜尋
  - GA4 加強型評估
  - 站內搜尋追蹤
prerequisites: []
related:
  - ec/products/create-and-manage/create-update-products/
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - ec/products/create-and-manage/edit-product-description-settings/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/products/create-and-manage/product-management-interface/
  - ec/products/discoverability/exclude-keyword-products-search/
  - ec/integrations/google/ga/setup-ga4-site-search-tracking/
tags:
  - "Site Search"
  - "Product Search"
  - "Segmented Search"
  - "GA4 Tracking"
  - "Exclude from Search"
  - "Site Search Tracking"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 套版主題管理
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8765
  - https://www.cyberbiz.io/support/?p=23999
permalink: "https://help.cyberbiz.io/ec/products/discoverability/setup-site-search/"
comments: ""
search:
  exclude: false
icon: lucide/search
hide:
---

![Site search - storefront](../../../assets/images/ec-商品-站內搜尋-前台.en.png){ title="Site Search - Storefront" .hero-page }

## About Site Search

On the CYBERBIZ storefront, the **search (magnifier) feature** is a key tool that helps shoppers find products quickly.

## Search Basics

*   **Location**: To search for products, shoppers click the **magnifier icon** :lucide-search: on the storefront and enter a keyword.

    ![Search products on the site](../../../assets/images/ec-商品-站內搜尋-前台輸入關鍵字.en.png){ title="Search Products on the Site" }

*   **Search scope**: By default, search results cover the following fields:

    | Search Field | Description | Where to Set It |
    |---|---|---|
    | Product name | The main name that identifies the product | [Product basic settings](../create-and-manage/create-update-products.md#operate-product-create-basic){ title="Add and Update Products" } |
    | Collection name | The names of collections, including customized collections and conditionalized collections.<br> (for example, in the URL `https://xxx/collections/mygroup`, the `mygroup` part) | [Customized collection settings](../categories-and-tags/custom-collections.md#operate-custom-collections-add-products){ title="Set Up Customized Collections" }, [Conditionalized collection settings](../categories-and-tags/smart-collections.md#operate-smart-collections-create){ title="Set Up Conditionalized Collections" }. |
    | Product vendor | The product's vendor name, shown on the storefront | [Product edit page > Settings](../create-and-manage/edit-product-description-settings.md#Advanced-Settings){ title="Edit Product Descriptions and Product Settings" } |
    | Product type | The product's type label | [Product edit page > Settings](../create-and-manage/edit-product-description-settings.md#Advanced-Settings){ title="Edit Product Descriptions and Product Settings" } |
    | Product channel | The product's channel labels (pre-order, in stock, room temperature, and so on)| [Product edit page > Settings](../create-and-manage/edit-product-description-settings.md#Advanced-Settings){ title="Edit Product Descriptions and Product Settings" } |
    | Product variant | Variant names (such as color M or size XL)| [Product variant settings](../create-and-manage/create-update-products.md#operate-product-create-variants){ title="Add and Update Products" } |
    | SKU | The product's stock keeping unit | [Product variant settings](../create-and-manage/create-update-products.md#operate-product-create-variants){ title="Add and Update Products" } |
    | Product introduction | The product's detailed description, including content in the text editor's source code. | [Product edit page > Product Description](../create-and-manage/edit-product-description-settings.md#Product-Description){ title="Edit Product Descriptions and Product Settings" } |

*   **Search logic and word segmentation**:

    *   Product names use **segmented search**. If a title contains a space or a hyphen (-) (such as "ER-1410"), the system splits it into separate words (such as "ER" and "1410"), and a search must exactly match a segment.
    *   If you enter the full model number in the **SKU field** (such as "ER1410"), searching for "1410" still finds the product even if its name is segmented (such as "ER-14010").

## Admin Settings and Management

Depending on your brand's needs, you can choose whether to show the search feature or exclude specific products:

<div class="grid cards" markdown>

- :lucide-toggle-left:{ .lg .middle } [__Site-Wide Search Bar Toggle__](../../website-appearance/navigation/setup-menus-navigation.md#operate-menus-nav-search){ title="Set Up Menus and the Navigation Bar" }  

- :lucide-package-x:{ .lg .middle } [__Exclude Individual Products from Search__](../create-and-manage/product-management-interface.md#Product-Search-and-Visibility-Management){ title="Product Management Interface Overview" }  

- :lucide-code:{ .lg .middle } [__Exclude by Keyword (Advanced)__](exclude-keyword-products-search.md){ title="Exclude Products with Specific Keywords from Search Results" }  

</div>

## Site Search Data Tracking <small>GA4</small>

You can monitor shopper search behavior with **Google Analytics 4 (GA4)** to improve product selection or SEO:

<div class="grid cards" markdown>

- :lucide-toggle-left:{ .lg .middle } [__Turn On Site Search Tracking__](../../integrations/google/ga/setup-ga4-site-search-tracking.md){ title="Set Up GA4 Site Search Tracking" }  

- :lucide-bar-chart-2:{ .lg .middle } [__View Tracking Results__](../../integrations/google/ga/setup-ga4-site-search-tracking.md#如何查看追蹤成果){ title="Set Up GA4 Site Search Tracking" }  

</div>

## FAQ

??? quote "Why can't I find a product with search?"

    Possible reasons include:

    - The keyword contains **special symbols** (such as `@`, `#`, or `$`) that the system cannot recognize. Remove them and search again.
    - The product title uses **word segmentation** (for example, "ER-1410" is split into "ER" and "1410"), so a search must exactly match a segment.
    - To search by a partial keyword, enter the full model number in the SKU field instead.

??? quote "Does the CYBERBIZ APP have a search feature too?"

    Yes. If you use the CYBERBIZ APP mobile app (iOS/Android), its home page also has a search bar so shoppers can find products anytime, anywhere.

??? quote "How do I keep specific products out of search?"

    There are two ways:

    - **Single product**: Turn the "Searchable" toggle on or off directly in the product list.
    - **Batch operation**: Select multiple products in the product list and choose "Disable Search".
    
    Excluded products cannot be found through the site search box, the all-products list, or Google search. They can only be opened through a direct link.

??? quote "Can search find a product introduction edited in source code mode?"

    Yes. The "product introduction" (the product's detailed description) is part of the site search scope, and content edited in the text editor's "source code" mode can also be found by search.

