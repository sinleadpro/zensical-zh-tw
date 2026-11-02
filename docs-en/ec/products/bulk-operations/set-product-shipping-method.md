---
title: "Set the Product Fulfillment Method"
description: "Based on where a product actually ships from, point it to self-shipment, third-party warehousing, or cross-border logistics through single-product editing, batch settings, or Excel import."
created: 2026-09-16 12:11
last_modified: 2026-09-16 12:11
lang: en-US
type: guide
status: ""
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
sites:
  - TW
  - US
  - JP
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定商品出貨方式
  - 批次修改商品出貨方式
  - 匯入商品出貨方式
features:
  - 商品出貨方式
  - 單筆修改
  - 批次修改
  - Excel大量匯入
prerequisites:
  - "Enable the fulfillment warehouses or logistics options you want to use"
related:
  - ec/products/references/product-warehouse/
  - ec/products/bulk-operations/excel-import-products/
  - wms/enable-partial-warehouse-integration-and-order-splitting/
  - wms/enable-partial-warehouse-integration-and-mixed-orders/
  - ec/payments-and-logistics/amazon-fba-cross-border-logistics/
tags:
  - "Product Fulfillment Method"
  - Self-Shipment
  - "Warehouse Fulfillment"
  - "Cross-Border Logistics"
  - "Excel Import"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 商品編輯頁
  - 設定分頁
  - 出貨方式
  - 商品列表操作選單
  - Excel大量匯入商品
paths:
  - 商品 > 所有商品
  - 商品 > Excel 大量匯入商品
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/bulk-operations/set-product-shipping-method/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

# Set the Product Fulfillment Method

Based on where a product actually ships from, point it to self-shipment, third-party warehousing, or cross-border logistics.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../../resources/conventions.md) | Smart Warehousing / Cross-Border E-commerce
{ .doc-badge }

## Before You Start

- **Option source**: The options available in **Warehouse** depend on the logistics features activated for your store.

## Steps

### Set a Single Product

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Click the product to open its edit page.
3. Switch to the **Settings** tab, and in **Warehouse**, select the fulfillment source that applies.
4. Click **Save** to finish setting the product's fulfillment method.

![](../../../assets/images/EC-後台-商品-所有商品-單筆設定出貨方式01.en.png){ .screenshot }

### Batch Settings

1. Go to **Products > All Products** and select the products you want to change.
2. Click **Actions... > Select Warehouse**.
3. Select the fulfillment source that applies to finish the batch change.

!!! warning "Batch Setting Limits"
    If your store has turned on **Express Delivery** or **POS**, exclude those products before you run the batch setting.

![](../../../assets/images/EC-後台-商品-所有商品-批次設定出貨方式01.en.png){ .screenshot }

### Bulk Settings with Excel

1. Go to **Products > All Products** and select the products you want to change.
2. Click **Actions... > Export Product** to download the product Excel file.
3. In the `出貨方式` column of the Excel file, enter the name of a fulfillment source that already exists in the admin.
4. Keep the existing values in the `商品 id` and `商品款式 id` columns.
5. Go to **Products > Import Products from Excel** and upload the edited file.

!!! info "Import Results"
    The system processes the file on a schedule and emails you the import results. When it is done, go back to the product list and check each product's fulfillment method.

To learn how Excel import decides between adding and updating products, and for the full flow, see [Import Products in Bulk from Excel](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }.

## Verify the Settings

- **Method 1**: Go back to **Products > All Products**, use **Advanced Search** to filter products by **Warehouse**, and check that the products in the filtered list are correct.

    ![](../../../assets/images/EC-後台-商品-所有商品-篩選器指定出貨方式01.en.png){ .screenshot }

- **Method 2**: Open the product's **Settings** tab and check that **Warehouse** shows the expected fulfillment source.


## Return to Your Scenario

Smart warehousing (order splitting and mixed orders) and Amazon FBA create the matching orders based on the fulfillment method. After you finish the settings on this page, go back to the original scenario guide to continue.

<div class="grid cards" markdown>

- :lucide-git-branch:{ .lg }
  [__Enable Partial Warehouse Integration and Order Splitting__](../../../wms/enable-partial-warehouse-integration-and-order-splitting.md){ title="Enable Partial Warehouse Integration and Order Splitting" }
  Check out separately based on each product's fulfillment source, and handle warehouse orders and merchant orders separately.

- :lucide-layers:{ .lg }
  [__Enable Partial Warehouse Integration and Mixed Orders__](../../../wms/enable-partial-warehouse-integration-and-mixed-orders.md){ title="Enable Partial Warehouse Integration and Mixed Orders" }
  Check out warehouse products and self-shipped products together, and then ship them separately.

- :lucide-globe:{ .lg }
  [__Amazon FBA Cross-Border Logistics__](../../payments-and-logistics/amazon-fba-cross-border-logistics.md){ title="Amazon FBA Cross-Border Logistics" }
  Bind Amazon SKUs to the fulfillment method to push cross-border orders and sync shipment status.

</div>

