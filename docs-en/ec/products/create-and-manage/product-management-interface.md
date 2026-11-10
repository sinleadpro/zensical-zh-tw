---
title: "Product Management Interface Overview"
description: "Get a quick overview of the CYBERBIZ product admin: search, filters, batch operations, and product visibility settings."
created: 2026-06-14 13:09
last_modified: 2026-07-03 11:44
lang: en-US
type: quickstart
author: Jase
reviewers: []
notes:
  - Overview 與操作流程互聯
  - Quickstart 上手指南
ga_views: 0
feedback: 0
products:
  - EC
  - POS
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
  - 商品管理介面總覽
  - 後台搜尋商品
  - 商品排除搜尋
  - 批次修改商品
features:
  - 商品管理介面
  - 商品搜尋功能
  - 商品篩選
  - 批次修改商品
  - 商品排除搜尋
  - 跨通路同步管理
  - 庫存列表
prerequisites: []
related:
  - ec/products/bulk-operations/batch-update-product-descriptions-shipping/
  - ec/products/pricing/setup-vip-member-pricing/
  - ec/products/bulk-operations/copy-products-to-pos-stores/
  - ec/products/bulk-operations/excel-import-products/
  - ec/products/create-and-manage/create-update-products/
  - ec/products/discoverability/setup-site-search/
  - ec/products/discoverability/product-search-visibility/
tags:
  - "Product Management"
  - "Product Search"
  - "Batch Edit"
  - "Product Filtering"
  - "Exclude Products from Search"
  - "Inventory Management"
acoiv: activate
apis: []
devices: []
ui_components: []
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2017
  - https://www.cyberbiz.io/helpcenter/?p=2789
  - https://www.cyberbiz.io/support/?p=7424
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/product-management-interface/"
comments: false
search:
  exclude: false
icon: lucide/panels-top-left
hide: []
---

![Product management interface overview](../../../assets/images/ec-products-management-interface-hero.en.png){ title="Product Management Interface Overview" .hero-page }

## About the Product Management Interface { #intro-product-ui }

The **product management interface** is mainly at the admin path **Products > All Products**. It brings together core features such as publishing products, quick filtering, batch editing, and cross-channel management to help you maintain your store's items efficiently.

## Interface Features { #overview-product-ui }

In the "All Products" list, you can perform the following basic actions on products:

*   [**Add Product**](#operate-product-ui-create): Click the button in the upper-right corner to publish a single product or products in batches.
*   [**Quick search**](#How-Filters-Work) and [**items per page**](#overview-product-ui-list): Find products by keyword, or adjust how many products each page shows.
*   [**Status toggle and preview**](#overview-product-ui-shortcuts): Click the "eye icon" to publish or hide a product directly, or click the link to preview the product page on the storefront.
*   [**Delete**](#overview-product-ui-shortcuts): Remove items you no longer sell.

## How Filters Work { #operate-product-ui-filter }

When you have many products, use filters to edit more efficiently:

*   **Multi-condition filtering**: Narrow down products precisely by [Type], [Vendor], [Tags], [Sell Status], [Publish Status], and [Shop].
*   **Horizontal filtering (OR)**: When you select multiple conditions in the same field, the system shows products that match "any condition"[^3].
*   **Vertical filtering (AND)**: When you set conditions across fields, the system shows only products that "match all conditions"[^4].
*   **Sell status labels**: The system labels products as "Launched", "Off Market" (expired), or "Unlisted" (not yet started). Hover over a label to see the exact date.

    ![Sell status labels](../../../assets/images/ec-products-status-labels-hover.en.png){ title="Sell Status Labels" }

=== ":lucide-search: Keyword Search"
	Enter a product name or SKU to search for products quickly.
	
	1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
	2. In the search field at the top of the page, enter the **product name** or **SKU** you want to find.
	3. Press ++enter++ or click the **search icon** :material-magnify:. The system shows the list of matching products.
	
	![Product search bar](../../../assets/images/ec-products-search-bar.zh-tw.en.png){ title="Product Search Bar" }

=== ":lucide-funnel: Advanced Filtering"
	Use filters to apply multiple specific conditions and pinpoint the products you want.
	
	1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
	2. Click **Advanced Search** next to the search field to open the dropdown menu.
	3. Click one or more **filter group fields**[^2], such as **Product Type**, **Product Vendor**, or **Product Tags**.
	4. Select the filter conditions for each field.
	5. Click **Search**. The system shows the list of products that match all conditions.
	
	![Advanced filtering](../../../assets/images/ec-products-filters.zh-tw.en.png){ title="Advanced Filtering" }
	
=== ":lucide-blend: Combined Search Conditions"
	Combine keyword search and advanced filtering to set up multiple filter conditions and find products that match complex criteria.
	
	1. Set [advanced filter conditions](#How-Filters-Work): Click **Advanced Search** next to the search field, select product attributes or categories, and click **Search** to apply the filters.
	2. [Enter keywords](#How-Filters-Work): Enter a product name or SKU in the search field, then press ++enter++ or click the **search icon** :material-magnify: to narrow the results further.
	
    > :lucide-flame: **Bulk actions on specific products**  
	After filtering the product list, [select products in batches](#operate-product-ui-select) and then [choose an action](#operate-product-ui-batch-actions) to apply batch actions to specific products.
	
	![Combined search conditions](../../../assets/images/ec-products-search-filter-combo.zh-tw.en.png){ title="Combined Search Conditions" }

## Batch Actions { #operate-product-ui-batch }

Select the checkboxes on the left of the list to perform **bulk actions**, including:

*   **Status and permissions**: Publish, hide, or delete in batches, and turn search on or [exclude products from search](#operate-product-ui-visibility).
*   **Export data**: [Export the product list](../bulk-operations/batch-update-product-descriptions-shipping.md#operate-batch-update-export) or the [member exclusive price list](../pricing/setup-vip-member-pricing.md#operate-vip-pricing-export).
*   **Channel management**: [Copy storefront products in bulk to POS stores](../bulk-operations/copy-products-to-pos-stores.md).

![Bulk actions](../../../assets/images/ec-products-batch-operations.en.png){ title="Bulk Actions" }

### Select Products in Bulk { #operate-product-ui-select }

=== "All Products on the Page"

    1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
    2. Click :lucide-square: in the **Select** menu to select all products shown on the page.

    !!! tip "Click **Show __ products** to change how many products the list shows per page."

	![Select products on the page](../../../assets/images/ec-products-select-whole-page.zh-tw.en.gif){ title="Select Products on the Page" }

=== "All Products in the Store"

	1. Clear all search and filter conditions.
	2. Click **__ products selected** and select **Select all products**.
	
	![Select all products in the store](../../../assets/images/ec-products-select-all-products.zh-tw.en.gif){ title="Select All Products in the Store" }

=== "Matching Products"

	1. [Search for products](#operate-product-ui-filter) to produce a filtered product list.
	2. Click **__ products selected** and select **Select all products**.
	
	![Select filtered results](../../../assets/images/ec-products-select-all-results.zh-tw.en.gif){ title="Select Filtered Results" }



---

### Batch Actions { #operate-product-ui-batch-actions }

1. [Select multiple products](#operate-product-ui-select).
2. Click the **Select** menu and choose a batch action[^1].  

![Bulk action flow](../../../assets/images/ec-products-batch-process.zh-tw.en.gif){ title="Bulk Action Flow" }

!!! warning "Notes"
    When "Select all products" is checked, the system limits some batch actions to prevent mistakes and keeps only actions such as exporting and copying to POS shops.

<div class="grid cards" markdown>

- :lucide-file-spreadsheet: [__Bulk Edit Product Information__](../bulk-operations/excel-import-products.md){ title="Bulk Edit Product Information" }
- :lucide-layers: [__Bulk Edit Products with Multiple Variants__](create-update-products.md#operate-product-create-variants){ title="Add and Update Products" }

</div>

## Product Search and Visibility Management { #operate-product-ui-visibility }

In the management interface, you can set each product's "product search" setting individually:

=== ":lucide-toggle-left: Single Product"

    1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
    2. Find the **Searchable** column in the product list. If it isn't shown, drag the scroll bar at the bottom.
    3. Toggle the **Searchable** switch:
        - ON: The product can be found in search.
        - OFF: The product is hidden.

    ![Search toggle](../../../assets/images/ec-product-list-search-index-toggle.en.png){ title="Search Toggle" }

=== ":lucide-square-check: Batch Action"

    1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
    2. Select the products to exclude from search.
    3. Click the **Select** dropdown menu and select **Disable Search**.  

    ![Exclude products from search in bulk](../../../assets/images/ec-商品-排除搜尋-批次操作.en.png){ title="Exclude Products from Search in Bulk" }

??? info "What Excluding from Search Does"

    When this is turned off, the system hides the product from the following:

    - **Site search**: The product can't be found through the store's search box. Learn [how to set up site search](../discoverability/setup-site-search.md){ title="Set Up Site Search" }
    - **System default list**: The product doesn't appear on the storefront "All Products (/collections/all)" page.
    - **External search engines (such as Google)**: The system automatically sends a **no-index directive** (`noindex`) telling search engines not to index the product page.

    **Note**: How long Google takes to remove search results depends on how often its crawler updates (usually days to weeks), so search results don't disappear immediately after you change the setting.

    !!! tip "Keep the Purchase Path"
        This feature only excludes products from "search discovery" and doesn't affect access through the product link. Customers with the product's direct URL (for example, shared through social media, EDM, or LINE private messages) can still open the page and order. This setting works well for "hidden deals" or "member-exclusive products".

<div class="grid cards" markdown>

- :lucide-search-check: [__Set Product Search Visibility__](../discoverability/product-search-visibility.md){ title="Set Product Search Visibility" }

</div>

## Cross-Channel Sync Management { #operate-product-ui-sync }

If you integrate other e-commerce platforms, the management interface shows the related link status:

*   **Shopee sync**: Check whether the Shopee icon in the "Connected Channel" column is lit to confirm that inventory is linked between your storefront and your Shopee shop.
*   **Tag exclusion**: To keep items from being uploaded to Google Merchant Center or the Facebook shop, enter "贈品" (gift) or "排除product feed" (exclude product feed) in the tags field on the product management page.


---

## Add Products { #operate-product-ui-create }

Create a single product, set its information, and publish it.

![Add Product button](../../../assets/images/ec-all-products-add.zh-tw.en.png){ title="Add Product Button" }

<div class="grid cards" markdown>

- :lucide-package-plus: [__Add and Update Products__](create-update-products.md){ title="Add and Update Products" }
- :lucide-upload: [__Add Products in Bulk__](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }

</div>

## Product List { #overview-product-ui-list }

Use the following features to quickly search, filter, and manage the product list.

- `Please enter Product Name, Sku`: Search for products quickly by keyword
- `Advanced Search`: Filter products
- `_ products selected`: Select products for bulk actions
- `Show _ products`: Adjust how many products each page shows

![Product list](../../../assets/images/ec-all-products-products-list.zh-tw.en.png){ title="Product List" }

## Quick Action Buttons { #overview-product-ui-shortcuts }

- :lucide-eye: Set whether the product is published: :lucide-eye-off: unpublished; :lucide-eye: published.
- :lucide-external-link: Go to the storefront product page
- :lucide-trash-2: Delete the product

![Quick action buttons](../../../assets/images/ec-product-list-shortcuts.zh-tw.en.png){ title="Quick Action Buttons" }

## Inventory List { #overview-product-ui-inventory }

View products that have [inventory management turned on](create-update-products.md#operate-product-create-inventory){ title="Add and Update Products" } and a limited inventory quantity.

![Inventory list](../../../assets/images/ec-inventory-list.zh-tw.en.png){ title="Inventory List" }

<div class="grid cards" markdown>

- :lucide-bell: [__Inventory Level Notifications__](create-update-products.md#operate-product-create-inventory){ title="Add and Update Products" }

</div>


## FAQ { #faq-product-ui }
??? quote "Why can't I find a product in search?"
	- Check that the keyword or SKU is correct
	- Check whether you've applied too many filters
	- Check whether the product has been deleted or is hidden

??? quote "Can I export search results?"
	Direct export isn't supported right now. To export products, use the [Excel export feature](../bulk-operations/batch-update-product-descriptions-shipping.md#operate-batch-update-export).

??? quote "Can I save filter conditions?"
	Saving isn't supported right now.

[^1]: The batch actions available vary by plan.
[^2]: The filter group fields available vary by plan or admin settings.
[^3]: For example, if you filter by the "Clothing" and "Shoes" types, the system shows products of either type.
[^4]: For example, if you filter by the "Clothing" type and "Launched" status, the system shows only products whose type is "Clothing" and whose status is "Launched".
