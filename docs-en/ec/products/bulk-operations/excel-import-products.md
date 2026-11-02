---
title: "Import Products in Bulk from Excel"
description: "Use an Excel template to add or update many products at once and list multiple products in a batch."
created: 2026-01-08 00:00
last_modified: 2026-07-22 17:26
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
  - 如何使用 Excel 大量匯入商品
  - 批次上架商品
  - 批次更新商品
features:
  - Excel 匯入商品
  - 大量新增商品
  - 批次上架
prerequisites: []
related: []
tags:
  - Excel
  - Import
  - "Products"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > Excel 大量匯入商品
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=924
  - https://www.cyberbiz.io/support/?p=1960
  - https://www.cyberbiz.io/support/?p=33323
  - https://www.cyberbiz.io/support/?p=6603
permalink: "https://help.cyberbiz.io/ec/products/bulk-operations/excel-import-products/"
comments: false
search:
  exclude: false
icon: lucide/file-spreadsheet
hide: []
---

![Import products in bulk from Excel](../../../assets/images/ec-import-products-from-excel.zh-tw.en.png){ title="Import Products in Bulk from Excel: Products > Import Products from Excel" .hero-page }

## About Product Excel Import

Use the Excel template to add or update many products at once. This is useful for listing products or adjusting product information in bulk. Before importing, review the following feature limits and notes on image hosting links.

!!! plan "North America Site Limits"
	- The North America site uses English as the default editing language. Bulk import can currently upload and update only the English pages of products.
	- Product SKUs must match Amazon for orders to ship.

## Prerequisites and Limits

When you create images quickly through **image hosting** links, note the following:

- Image format: Only `jpg`, `jpeg`, `png`, `gif`, and `webp` formats are supported, and each image must not exceed 10 MB.
- Hosting permissions: Set the image hosting permissions to public, or the upload will fail.
- Chinese file names: Image hosting links with Chinese file names are not supported. Convert image names to UTF format before pasting them into Excel and uploading.
- Import failures: If the import fails during upload because of image size or format, the whole import stops. Images already uploaded stay, but the images after the failure must be uploaded separately.
- Hosting services: You can upload images with a third-party image hosting service (for example, Imgur).  

!!! info "Choose an image hosting service based on your needs. CYBERBIZ does not provide setup, operation, or technical support for third-party image hosting."

## Steps
### Download the Excel Template or Export Products

=== "Add Products in Bulk"

	1. Log in to the CYBERBIZ admin and go to **Products > Import Products from Excel**.
	2. Click **進階大量建立商品範本.xlsx** (the advanced bulk product creation template) to download it.

	![Download the bulk creation template](../../../assets/images/ec-advance-mass-import.zh-tw.en.png){ title="Download the Bulk Creation Template" }

=== "Update Products in Bulk"

	1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
	2. Select all the products you want to update.
	3. Click **Select** and choose **Export product**.

	![Export products](../../../assets/images/ec-export-product.zh-tw.en.png){ title="Export Products" }

---

### Determine Whether an Excel Upload Adds or Updates Products { #determine-add-or-update }

Columns A (`商品 id`, product ID) and B (`商品款式 id`, product variant ID) in the product Excel file are hidden by default. After you upload the Excel file, the system uses whether these two columns contain system values to decide whether to add new products or update existing ones.

=== "Add Products in Bulk"

	In the downloaded Excel template, columns A and B are empty. After upload, the rows are treated as new products.

	![Empty columns for new products](../../../assets/images/ec-product-excel-empty-inventory.zh-tw.en.png){ title="Empty Columns for New Products" }

=== "Update Products in Bulk"

	In an exported product Excel file, columns A and B contain system values. After upload, the rows are treated as updates to existing products.

	![Value columns for updated products](../../../assets/images/ec-product-excel-existing-inventory.zh-tw.en.png){ title="Value Columns for Updated Products" }

---

### Fill in the Product Excel Columns

Fill in the product information according to the columns and descriptions in the Excel template. The following fields are required:

=== "EC"
	- Product name: Set the product name. Do not use special symbols (such as `|` and `”`) or HTML.
	- Product brief type: Enter `html樣板文字` (HTML template text) or `純文字` (plain text).
	- Product variant selling price: Set the actual selling price of the product.

=== "EC + POS"
	- Product name: Set the product name. Do not use special symbols (such as `|` and `”`) or HTML.
	- Product brief type: Enter `html樣板文字` (HTML template text) or `純文字` (plain text).
	- Product variant selling price: Set the actual selling price of the product.
	- Product affiliated shops: Specify the store the product belongs to. Required if POS is enabled.
	- Product variant SKU: Required for POS products.

!!! warning "Notes"
	- Do not use bold text. It causes upload format errors.  
	- Columns support different behaviors, such as first upload only, repeated uploads, single value, comma-separated multiple values, and HTML support.

---

### Import the Excel File

1. In the CYBERBIZ admin, go to **Products > Import Products from Excel**.
2. Click **Choose file** and select the edited product Excel file.
3. Click **Confirm Upload**.
4. The system emails you the update status. Follow the instructions for next steps.

|Status|Description|Recommended Action|
|---|---|---|
|:lucide-circle-x: Failed|Shows an error message or the reason for the failure|Fix the issue and upload again|
|:lucide-circle-check: Succeeded|Wait for the system to finish the import. You will receive an email notification when it is done.|Do not upload again|
|:lucide-check: Completed|The import is confirmed as complete|Check the results or update other content|

## FAQ

??? quote "Why weren't my products added or updated after I uploaded the Excel file?"
    - Check whether the Excel file uses bold text or whether product names contain special symbols.
    - Make sure image links meet the format and size limits and that the image hosting permissions are public.
    - Check columns A and B to make sure you [determine whether an Excel upload adds or updates products](#determine-add-or-update) correctly.
    - The import takes time. Wait for the completion email and avoid uploading again.
