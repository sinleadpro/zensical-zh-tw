---
title: "Product Information Settings for Japan-to-Taiwan Cross-Border Sales"
description: "To use Japan-to-Taiwan logistics, complete the customs information for your products. This guide explains how to edit fields such as JANCODE, ingredients, and country of origin one by one or in bulk."
created: 2026-07-24 15:03
last_modified: 2026-07-24 15:03
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
products:
  - EC
modules:
  - APP MARKET
  - 商品
sites:
  - JP
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - global_advanced
plan_options: []
cyb_extensions:
  - EXPRESS
intents: 
  - 設定跨境商品報關資訊
  - 補齊日到台商品資訊
features: 
  - 跨境物流
  - EXPRESS
prerequisites: []
related:
  - ec/products/bulk-operations/excel-import-products/
tags: 
  - "Japan to Taiwan"
  - "Cross-Border E-Commerce"
  - "Product Settings"
  - "Customs Information"
acoiv: configure
apis: []
devices: []
ui_components: 
  - 單筆編輯
  - 批次編輯
paths: 
  - 商品 > 所有商品
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/express/product-info-setting/"
comments: false
search:
  exclude: false
icon: lucide/file-edit
hide: []
---
# Product Information Settings for Japan-to-Taiwan Cross-Border Sales
To use Japan-to-Taiwan logistics, you need to complete customs information for your products. This guide explains how to edit JANCODE, ingredients, country of origin, and other fields one by one or in bulk.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (Japan to Taiwan)<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ EXPRESS
{ .doc-badge }



To use **Japan-to-Taiwan** logistics, every product sold cross-border must include the following customs information:

| Field Name | Field Info | Language | Rule |
| ------- | -------- | ------- | ------- |
| **GTIN(Barcode)** | JANCODE | Japanese | Required |
| **Item Name(Local)** | Product name | Japanese | Required |
| **Ingredients** | Ingredients | Japanese | Required |
| **Category** | Item description | Japanese | Required |
| **Country of Origin** | Country of origin | Japanese | Required |
| **Item Name(English ONLY)** | Product name | English (use half-width punctuation) | EXPRESS home delivery: Not required<br>EMS: Required |


## How to Edit { #operate-product-info }

=== "Edit One Product"

    Go to **Products > All Products** and fill in the fields on the product details page.

    ![](../../../assets/images/EC-後台-商品-所有商品-日到台站台報關用商品欄位01.en.png){ .screenshot }

=== "Edit in Bulk"

    1. [Export the product Excel file](../../products/bulk-operations/excel-import-products/#operate-excel-import-download).
    2. Fill in the customs fields and save the file.
    3. [Import the product Excel file](../../products/bulk-operations/excel-import-products/#operate-excel-import-upload) to finish bulk editing.

    ![](../../../assets/images/EC-後台-商品-所有商品-日到台站台報關用商品欄位02.en.png){ .screenshot }
