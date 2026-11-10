---
title: "Bulk Fill Product SKUs"
description: "Learn how to quickly fill in missing SKU codes for existing products using Excel bulk export and import, so you can enable POS features and manage inventory accurately."
created: 2026-06-24 17:25
last_modified: 2026-06-24 17:25
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules: 
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
  - 批次更新商品 SKU
  - 補齊 POS 商品 SKU
  - 大量編輯商品資訊
features: 
  - Excel 大量匯入
  - SKU 管理
  - POS 串接
prerequisites: 
  - "所有商品-新增商品"
related:
  - ec/products/bulk-operations/excel-import-products/
tags: 
  - SKU
  - "Bulk Update"
  - "Excel import"
  - POS
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 所有商品列表
  - Excel 大量匯入商品
paths: 
  - 商品 > 所有商品
  - 商品 > Excel 大量匯入商品
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=3296
permalink: "https://help.cyberbiz.io/pos/get-started/bulk-update-product-skus/"
search:
  exclude: false
icon: lucide/file-spreadsheet
hide: []
---

# Bulk Fill Product SKUs
Learn how to quickly fill in missing SKU codes for existing products using Excel batch export and import, so you can enable POS features and manage inventory accurately.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

## Before You Start { #prerequisites-sku-bulk }

- **POS Activation Requirement**: Products must have a SKU code before they can be activated and use POS system features.
- **SKU Uniqueness**: Each product variant must have a unique SKU code to avoid inventory calculation errors.
- **Overwrite Logic**: Files exported from the product list contain "Product ID" and "Variant ID." When you edit and import such a file, the system **overwrites** the existing product information instead of creating new products.
- **Backup Recommendation**: Before a large import, keep the original exported Excel file so you can restore it if an error occurs.



## Steps { #operate-sku-bulk }

### Step 1: Export Existing Product Data { #operate-sku-bulk-step-a-export }

Get the complete list including product IDs.

1. Log in to the CYBERBIZ admin dashboard and go to **Products > All Products**.
2. Select the products you want to update, or click **Select All** above the list to select all products.
3. Click the **Select** dropdown menu and choose **Export product**.
4. The system automatically generates a product list Excel file and sends it to the email address of your admin login.

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學1.png){ .screenshot }

### Step 2: Fill in SKUs in Excel { #operate-sku-bulk-step-b-excel }

Use Excel's filter feature to quickly locate missing data.

1. Download and open the product Excel file from your email.
2. Find the **Variant SKU Code** column.
3. Use Excel's **Filter** feature and select only **(Blanks)** to list all products without an SKU.
4. After entering the correct SKU codes, clear the filter and save the file.

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學4.png){ .screenshot }

### Step 3: Import the Updated File { #operate-sku-bulk-step-c-import }

Upload the revised data back to the system.

1. Return to the admin dashboard and go to **Products > Import Products from Excel**.
2. Click **Upload File** and select the Excel file you just saved.
3. Click **Confirm Upload**. The system will schedule the update processing.

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學5.png){ .screenshot }

### Step 4: Verify the Update Results { #operate-sku-bulk-step-d-confirm }

The system notifies you of processing progress by email.

- **Failed**: The system displays the reason for failure. Correct the errors and upload the file again.
- **Success**: Wait for the completion email. Uploading again before processing finishes will cause data confusion, so please wait patiently.
- **Completed**: The import is confirmed complete. You can review the update results or update other content.

After the SKUs are filled in, **contact online customer service or your LINE@ specialist** to apply for POS activation.

![](https://www.cyberbiz.io/support/wp-content/uploads/商品大量補填SKU教學6.png){ .screenshot }

## More Actions { #next-steps-sku-bulk }

<div class="grid cards" markdown>

- :lucide-arrow-right:{ .lg }   
  [__Check Whether an Excel Upload Adds or Updates Products__](../../ec/products/bulk-operations/excel-import-products/#operate-excel-import-add-update)
  Learn the difference between "Add New Product" and "Overwrite Existing Product."

</div>