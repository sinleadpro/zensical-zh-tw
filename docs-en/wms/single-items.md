---
title: "Single Products"
description: "Create and manage single products in the e-commerce warehouse, including adding product details, batch import, setting vendors, and exporting inventory reports."
created: 2026-03-18 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 商品
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 新增單一商品
  - 批次匯入商品
  - 設定來源廠商
  - 匯出庫存報表
features:
  - 單一品項管理
  - 庫存水位警示
  - 效期控管
  - 供應商綁定
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
related:
  - wms/suppliers/
  - wms/seasonal-groups/
tags:
  - WMS
  - "Product Management"
  - "Expiry Settings"
acoiv: activate
apis: []
devices:
  - desktop
ui_components:
  - 單一品項列表頁
  - 新增商品彈窗
  - 商品編輯頁面
paths:
  - 商品 > 單一品項
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5733
  - https://www.cyberbiz.io/support/?p=8920
permalink: "https://help.cyberbiz.io/wms/single-items/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Single Products
Create and manage single products in the e-commerce warehouse, including adding product details, batch import, setting vendors, and exporting inventory reports.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-商品-單一品項-畫面總覽01.en.png){ .hero-page }


## Before You Start { #prerequisites-single-items }

- **Barcodes are required**: The outer packaging of every physical product must have an international barcode. If a product has no barcode, create one yourself and stick it on the packaging.


## Add a Single Product { #operate-single-items-add }

Before a new product enters the warehouse, create its record in the WMS admin panel.

1. Go to **Products > 單一品項**.

2. Click **Add Product** in the upper-right corner.

3. **Basic settings**:
    - **Product name (required)**: We recommend using the same name as on your online store.
    - **Barcode (Required)**: Enter the barcode on the product packaging (letters and numbers only, no symbols).
    - **Product Uid (Required)**: Enter the product's unique ID code.

        !!! info "Online Store Integration Tip"
            If your warehouse system is connected to a CYBERBIZ online store, this field must match the **product SKU** in the online store admin panel.
            To find the SKU, log in to the online store admin panel, go to **Products > All Products**, and open the product details page. The SKU is shown in the variant information.

    - **Storage temperature zone**: Choose the temperature at which the product is stored.
    - **Record serial numbers**: Turn this on if each unit's serial number must be recorded at **inbound sign-off** and **outbound scanning** for later tracking.

        > For high-value products (such as large appliances, computers, or phones), this helps you track where each unit goes.

    - **Product Image**: Upload a photo of the product to reduce picking errors on site.

4. **Export Info**: Required if the product may be shipped overseas.

5. **Advanced settings**:
      - **Valid Period**: Enter the number of valid days (for example, 1095 days for three years).
      - **Expiration Action**: Choose what the system does after the product expires (keep or destroy).
      - **Low Stock Threshold**: Set a threshold. When stock falls below it, the system sends a reminder email every day.
      - **Shortest shelf life of good products**: Set the shortest remaining shelf life allowed for shipping, to help you plan for near-expiry stock.
      - **Air transport restricted goods**: Select this if the product contains batteries, sprays, or similar items, to meet carrier rules.
      - **Vendor**: Choose the product's vendor. To add a vendor, go to **Vendors** and [create the vendor record](suppliers.md).
      - **Season Group**: Choose a season group. To add one, go to **Season Groups** and [create a group](seasonal-groups.md).

6. **Size Setting**:
      - **Product size**: Set single unit, box, or carton, to help warehouse staff identify the product.

7. Click **Add Product** to finish.

!!! warning "Food and Cosmetics Rules"
    By law, food and cosmetics must have strict expiry control. The outer packaging must carry complete Chinese labeling and an expiry date, and the **Valid Period** in the system must be greater than the **Shortest shelf life of good products**.

![](../assets/images/WMS-後台-商品-單一品項-單筆新增品項01.en.png){ .screenshot }


## Check Product Stock { #operate-single-items-query }

After you create a product, check its real-time stock in the **Product Stock List**.


- **Batch management**: To track manufacturing batches closely, view the receiving details of each batch here.
- **Key numbers**:
    - **Pcs**: Total physical stock minus **defective units** and units **reserved for shipping (allocated to orders)**.
    - **Locked Pcs**: Units locked by orders that have not physically left the warehouse yet.
    - **Shipped**: The total number of units shipped since the product entered the warehouse.

## Import Products in Batches { #operate-single-items-import }

If you have many products, use an Excel batch import.

1. Go to **Products > 單一品項** and click **Import** in the upper-right corner.
    ![](../assets/images/WMS-後台-商品-單一品項-批次匯入單品01.en.png){ .screenshot }
2. Click **Download Template** to get the standard Excel format.
    ![](../assets/images/WMS-後台-商品-單一品項-匯入範本01.en.png){ .screenshot }
3. Fill in the data.
4. Click **Import** and upload the file.

!!! warning "Import Notes"
    **Do not refresh or leave the page** during the import. Wait for the progress bar to finish. Otherwise, the data may be incomplete or the import result may be reported as failed.


## Export Product Reports { #operate-single-items-export }

Export the summaries regularly for stocktaking and data updates.

1. Go to **Products > 單一品項** and click **Export** in the upper-right corner.
2. Choose an export type:
    - **Product Information List**: Contains the basic product master data. Edit it and import it again to update existing products in batches.
    - **Product Inventory List**: Contains the real-time total stock and reserved quantities in the warehouse, so you can reconcile your records.

## FAQ { #faq-single-items }

??? quote "Can I Edit Product Information in Batches?"
    Yes. Click **Export** to download the **Product Information List**, edit it in Excel, and then upload it with **Import**. The system updates the products in batches automatically.
