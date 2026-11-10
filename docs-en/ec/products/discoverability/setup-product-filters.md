---
title: "Set up Storefront Product Filters"
description: "Set up and manage the product filters available to customers to improve the storefront shopping experience."
created: 2026-01-16 00:00
last_modified: 2026-07-22 17:39
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
difficulty: beginner
tnb: branch
plans:
  - Advanced
  - Expert
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何設定前台商品篩選器
  - 商品篩選器設定
features:
  - 商品篩選器
  - 拖拉版型
  - 商品規格篩選
prerequisites:
  - "Set up product options"
related: []
tags:
  - "Product Filters"
  - "Storefront Filters"
  - "Product Specifications"
  - "Drag-and-Drop Theme"
  - "Product Search"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=6170
  - https://www.cyberbiz.io/support/?p=31470
permalink: "https://help.cyberbiz.io/ec/products/discoverability/setup-product-filters/"
comments: false
search:
  exclude: false
icon: lucide/filter
hide: []
---

![Storefront product filter settings](../../../assets/images/ec-product-edit-product-filter-hero.zh-tw.en.png){ title="Storefront Product Filter Settings" .hero-page }

## About Storefront Product Filters { #intro-product-filters }

Storefront product filters let customers filter products by **price, inventory, bonus redemption, and product options**.

??? info-clean "Storefront Display"

    ![Storefront product filter display](../../../assets/images/ec-product-filter-frontend.zh-tw.en.png){ title="Storefront Product Filter Display" }

## Prerequisites and Limits { #prerequisites-product-filters }

- :lucide-check: Supports **customized collection pages**
- :lucide-check: Supports **conditionalized collection pages** `/collections`
- :lucide-x: Does not support **multi-level category pages** `/categories`

### Default Filters { #prerequisites-product-filters-default }

The system includes the following **default filters**. Their filter conditions are fixed by the system, and merchants cannot add, delete, or modify their sub-conditions.

**Price**

- Filters products by price range.
- The filter uses the **range from the lowest to the highest price** across the product's variants.

---

**Quantity**

- **In Stock**: The product inventory is greater than 0, or inventory is set to unlimited.
- **Pre-order**: The product inventory is 0, and "Continue selling when out of stock" is enabled.

---

**Credit(s)**

- **Products eligible for credit redemption**: The product's bonus redemption quantity is greater than 0.

!!! tip "Automatically Generated Product Option Filters"  
	The system automatically uses all **product options** in your store as filter items. To change which items appear in the filters, see [Edit Product Options](#operate-product-filters-variants).

??? info "Filter Logic"

    | Logic Type | Use Case | Filter Result | Example |
    |----------|----------|----------|------|
    | **Intersection (AND)** | Select sub-conditions from *different filters* | Products must match all conditions | `Color:Red` and `Size:S` → Shows products that are red and size S |
    | **Union (OR)** | Select multiple sub-conditions from *the same filter* | Products can match any condition | `Color:Red` or `Color:Black` → Shows products that are red or black |

## Merchant Steps { #operate-product-filters }

### Step 1: Open the Product Filter Settings { #operate-product-filters-enter }

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click **Edit Product Filter** to open the edit page.

![Open the product filter settings](../../../assets/images/ec-product-filter-setup-entry.en.png){ title="Open the Product Filter Settings" }

---

### Step 2: Enable Storefront Product Filters { #operate-product-filters-enable }

Click the **Enable Product Filter** toggle :material-toggle-switch: to show or hide filters on the storefront.

![Enable storefront product filters](../../../assets/images/ec-product-filter-enable-toggle.en.png){ title="Enable Storefront Product Filters" }

---

### Step 3: Understand Filters and Sub-Conditions { #operate-product-filters-rules }

The system automatically uses all **product options** in your store as filters, such as *Color*, *Size*, and *Material*.

- **Filter**: A dimension for filtering products, such as "Material".
- **Sub-condition**: An option under a filter, such as "Cotton", "Polyester", or "Linen".

![Filter and sub-condition settings](../../../assets/images/ec-product-filter-frontend-setting.zh-tw.en.gif){ title="Filter and Sub-Condition Settings" }

---

### Step 4: Edit Product Options { #operate-product-filters-variants }

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Select the product you want to edit to open the product edit page.
3. In the **Manage Variants** section, click **Edit product options**.

![Edit product options](../../../assets/images/ec-product-options-edit.zh-tw.en.png){ title="Edit Product Options" }

---

### Step 5: Reorder Filters and Sub-Conditions { #operate-product-filters-sort }

Drag the :material-drag-vertical: icon to the left of a filter or sub-condition to change the display order.

![Reorder filters](../../../assets/images/product-filter-reorder.zh-tw.en.gif){ title="Reorder Filters" }

---

### Step 6: Edit Filter Visibility { #operate-product-filters-status }

Click :material-eye-outline: (Published) or :material-eye-off-outline: (Unpublished) on the right to show or hide a filter on the storefront.

![Toggle filter visibility](../../../assets/images/product-filter-frontend-public-toggle.en.gif){ title="Toggle Filter Visibility" }

## Customer Experience and Storefront Display { #operate-product-filters-front }

### Storefront Display Differences { #specs-product-filters-display }
How product filters appear on the storefront depends on the device type.
	
=== ":material-monitor-dashboard: Desktop"
	- The desktop storefront shows up to 5 filters
    - If there are more than 5, customers click "All Filters" to see the rest

	![Desktop storefront filter display](https://www.cyberbiz.io/support/wp-content/uploads/商品篩選器05.png){ title="Desktop Storefront Filter Display" .screenshot }

=== ":material-cellphone: Mobile"
	On the mobile storefront, customers must click "All Filters" to see any filters.

	![Mobile storefront filter display](https://www.cyberbiz.io/support/wp-content/uploads/商品篩選器06.png){ title="Mobile Storefront Filter Display" }

---

### Sub-Condition Product Counts { #specs-product-filters-counts }

The number in parentheses after a sub-condition is the number of products that match it.

---

### Adjust Filter Conditions { #operate-product-filters-adjust }

Click **All Filters** to open a dialog and adjust the published filter groups and options.

![All filters on the storefront](../../../assets/images/ec-product-filter-all-filters-frontend.zh-tw.en.gif){ title="All Filters on the Storefront" }

---

### Clear Filter Conditions { #operate-product-filters-clear }

After applying filters, click **Reset All Filters** to remove all applied conditions at once.
	
![Reset all filters](https://www.cyberbiz.io/support/wp-content/uploads/商品篩選器08.png){ title="Reset All Filters" }


## FAQ { #faq-product-filters }

??? quote "Do product filters work on all collection pages?"
	No. They work only on **customized collection pages** and **conditionalized collection pages** (`/collections`). Multi-level category pages (`/categories`) are not supported.

??? quote "Why don't my filters appear on the storefront?"

    - Make sure the filter is set to *Published*.
    - Desktop shows up to 5 filters. On mobile, customers must click "All Filters" to see them.
