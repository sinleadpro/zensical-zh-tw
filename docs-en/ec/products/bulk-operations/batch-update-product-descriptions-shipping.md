---
title: "Batch Edit Product Descriptions and Shipping Settings"
description: "Use Excel batch export, editing, and upload to update the descriptions, temperature zones, shipping methods, and sales channels of multiple products at once and save manual maintenance time."
created: 2026-03-05 10:50
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
  - 金物流
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
  - 批次更新商品資訊
  - 節省大量商品編輯時間
  - 修改配送與通路設定
features:
  - 批次匯出商品
  - Excel 大量匯入
  - 配送設定批次修改
prerequisites: []
related:
  - ec/products/create-and-manage/product-management-interface/
  - ec/products/create-and-manage/edit-product-description-settings/
  - ec/products/bulk-operations/excel-import-products/
  - ec/products/shipping/setup-product-shipping-conditions/
tags:
  - "Batch Edit"
  - "Excel Import"
  - "Product Description"
  - "Temperature Zone Settings"
  - "Logistics Channels"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 進階搜尋
  - 商品列表
  - 操作選單
paths:
  - 商品 > 所有商品
  - 商品 > 所有商品 > 點擊特定商品 >「商品描述」頁籤
  - 商品 > Excel 大量匯入商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=9397
  - https://www.cyberbiz.io/support/?p=44199
permalink: "https://help.cyberbiz.io/ec/products/bulk-operations/batch-update-product-descriptions-shipping/"
comments: false
search:
  exclude: false
icon: lucide/file-pen
hide: []
---

![Bulk update product descriptions and shipping settings](../../../assets/images/ec-export-product-hero.zh-tw.en.png){ title="Bulk Update Product Descriptions and Shipping Settings" .hero-page }

## About Bulk Updating Product Descriptions and Shipping { #intro-batch-update }

Export, edit, and upload an Excel file to update the descriptions, temperature zones, shipping methods, and sales channels of many products at once, without opening each product page. This saves a lot of manual maintenance time. Suitable scenarios include:

- Product information needs a full update
- Shipping methods or channels change
- Adding temperature zone settings to many products, and so on.

The process has three stages: **Export the product Excel** > **Edit the Excel** > **Upload the Excel file**. After upload, the system processes the file on a schedule and emails you the result.

!!! info "Before You Update"
    - Once added, a product channel **cannot be deleted**. Make sure the channel name is correct before entering it.
    - For the product shipping name, enter a logistics name already set up in the admin. Entering a logistics name that doesn't exist makes the import fail.
    - When uploading, the `商品 id` (product ID) and `商品款式 id` (product variant ID) columns must keep their system values to update existing products. If they are empty, the rows are treated as new products.

## Steps { #operate-batch-update }
### Export the Product Excel File { #operate-batch-update-export }

=== "Export Some Products"

	1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
	2. In the product list, select the products you want to edit.
	3. Click the actions menu and choose **Export product**. The system automatically downloads the Excel file to your computer.

	!!! tip "Select Many Products Quickly"
	    To select many products at once, first use *Advanced Search* to filter the products that match your criteria,
	    then click the *"Selected products"* checkbox above the product list to select all products in the current filter results. For more search and filter options, see [Search Products](../create-and-manage/product-management-interface.md#operate-product-ui-filter){ title="Product Management Interface Overview" }.


=== "Export All Products"

	1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
	2. Click the **__ products selected** field and choose **Select all products**.
	3. Click the actions menu and choose **Export product**. The system automatically downloads the Excel file to your computer.
	
	![Export all products](https://www.cyberbiz.io/helpcenter/wp-content/uploads/批次修改商品資料2.png){ title="Export All Products" .screenshot }

---

### Edit the Excel File { #operate-batch-update-edit }

Open the downloaded product export Excel file and enter or change the product descriptions and shipping settings in the corresponding columns. For the actual admin settings and steps, see [Edit Product Descriptions and Product Settings](../create-and-manage/edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }.

---

#### Product Description { #operate-batch-update-description }

- The product description page has three sections: "Product Introduction", "Product Specifications", and "Delivery Type". Enter the content in the matching "Product Introduction", "Product Specifications", and "Delivery Type" columns of the Excel file.
- To check how the column content appears in the admin, go to **Products > All Products**, click a product, and open the **Product Description** tab.

---

#### Product Channel { #operate-batch-update-channel }

- Enter the product's fulfillment channel name. If you enter a channel the store doesn't have yet, the system treats it as a **new channel**.
- Leave it empty to **apply to all channels**.

!!! warning "Note"
    Once added, a channel **cannot be deleted**.

---

#### Product Temperature Zone { #operate-batch-update-temp }
- Enter `常溫` (room temperature), `冷藏` (refrigerated), or `冷凍` (frozen).
- Leave it empty to **default to room temperature**.
- You can select multiple temperature zone values. Separate them with **half-width commas (,)**, for example: `常溫,冷藏,冷凍`.

---

#### Product Shipping Name { #operate-batch-update-ship-name }
- Enter the shipping logistics name. Do not enter logistics names that are not set up in the admin.
- You can select multiple logistics options. Separate them with **half-width commas (,)**, for example: `黑貓,宅配通`.
- Leave it empty to **apply to all shipping methods**.

## Upload the Excel File { #operate-batch-update-upload }
	
1. Log in to the CYBERBIZ admin and go to **Products > Import Products from Excel**.
2. Upload the edited Excel file.

![Upload the Excel file](../../../assets/images/ec-upload-product-excel.zh-tw.en.png){ title="Upload the Excel File" }

!!! info "Rules for Updating and Adding Products"
    In the uploaded Excel file, the `商品 id` and `商品款式 id` columns must contain existing system values to *update existing products*. If the columns are empty, the system automatically *adds new products*. For details and examples, see [Differences Between Adding and Updating Products](excel-import-products.md#operate-excel-import-add-update){ title="Import Products in Bulk from Excel" }.

## Wait for the Import Notification { #operate-batch-update-notify }

=== ":material-progress-check: Data Import in Progress"
    If the format is correct, you receive a "Data import in progress" email notification.

    ![Data import in progress](https://www.cyberbiz.io/helpcenter/wp-content/uploads/批次修改商品資料5.png){ title="Data Import in Progress" .screenshot }

=== ":material-check-circle-outline: Product Data Imported Successfully"

    When the import is complete, you receive a "Product data imported successfully" email notification, which means the bulk update is done.

    ![Product data imported successfully](https://www.cyberbiz.io/helpcenter/wp-content/uploads/批次修改商品資料6.png){ title="Product Data Imported Successfully" .screenshot }

## Next Steps { #next-steps-batch-update }

After the bulk update, we recommend reading the following documents to understand product description and shipping settings more fully:

<div class="grid cards" markdown>

- :lucide-file-spreadsheet:{ .lg }  
  [__Import Products in Bulk from Excel__](excel-import-products.md){ title="Import Products in Bulk from Excel" }  
  Learn the full Excel import process, including adding products, image hosting links, and the rules for deciding between adding and updating.

- :lucide-file-pen:{ .lg }  
  [__Edit Product Descriptions and Product Settings__](../create-and-manage/edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }  
  Learn how to edit product descriptions, channels, and logistics attributes one product at a time in the admin, and how they appear.

- :lucide-truck:{ .lg }  
  [__Set Up Product Shipping Conditions__](../shipping/setup-product-shipping-conditions.md){ title="Set Up Product Shipping Conditions (Logistics, Temperature Zone, and Fulfillment Channel)" }  
  Understand the admin setup logic for logistics, temperature zones, and fulfillment channels, and how checkout splits orders.

</div>

