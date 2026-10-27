---
title: "Bundle Products"
description: "A bundle product is what online stores usually call a combo product. You bind several single products into one new sales unit. When an order is placed, the system deducts stock from each component product automatically."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 加工商品可以匯出批次編輯嗎
  - 加工品會對應到EC的一般商品還是組合品
  - 內部連結：批次修改商品 sku
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
  - 建立組合商品
  - 設定加工項目
  - 批次匯入加工品
  - 同步 EC 庫存
features:
  - 加工商品
  - 組合品管理
  - 庫存自動扣減
  - SKU 映射
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 子品項需已在 WMS 單一品項完成建檔
related:
  - ec/products/create-and-manage/create-update-products/
  - wms/single-items/
tags:
  - WMS
  - "Combo Product"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 加工商品列表頁
  - 新增加工商品頁面
  - 加工商品匯入頁面
paths:
  - 商品 > 加工商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5717
  - https://www.cyberbiz.io/support/?p=8920
  - https://www.cyberbiz.io/support/?p=9749
permalink: "https://help.cyberbiz.io/wms/processed-products/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Bundle Products
A bundle product is what online stores usually call a combo product. You bind several single products into one new sales unit. When an order is placed, the system deducts stock from each component product automatically.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-商品-加工商品-畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-processed-products }

- **CYBERBIZ online store inventory link**: If your warehouse system is connected to your CYBERBIZ online store (EC), follow these rules:
    - **Order of setup**: After you create the **bundle product** in WMS, [create a matching product](../ec/products/create-and-manage/create-update-products.md) in the online store admin panel.
    - **Key match**: The online store product's **SKU** must exactly match the **Product Uid** in WMS.
    - **Automatic sync**: Once the details match, the system keeps stock in sync between both sides in real time.
- **Bundle stock logic**
    - **Formula**: Available stock of a bundle product = **the lowest sellable quantity among all its component products**.
    - **Example**: Bundle A+B. Component A has 100 units in stock, and component B has 80 units.
    - **Result**: The bundle can sell at most 80 sets.
    - **Linked stock**: If 30 units of component B sell (on their own or in another bundle), this bundle's stock drops to 50 sets automatically.


## Apply and Prepare { #prerequisites-processed-products-setup }

Bundle products need manual assembly at the warehouse, so finish these admin steps before you set anything up in the system:

1. **Consult and get a quote**: Contact your account manager or warehouse admin staff and describe the processing you need (such as shrink-wrapping, labeling, or boxing). The warehouse calculates the processing fee and sends a quote.
2. **Processing items**: Based on the quote, the warehouse creates the matching **processing items** in the system. **You can only select these items in the admin panel after the warehouse finishes this step.**
3. **Single product records**: Make sure every **component product** for the bundle already exists in **Products > 單一品項**. See [Create Products](single-items/#operate-single-items-add).



## Create a Bundle Product Manually { #operate-processed-products-create }

After preparation, bind single products into a bundle product in the WMS admin panel.

1. Go to **Products > 加工商品**.
2. Click **Add Bundle Product** in the upper-right corner.
3. Fill in the basic information:
    - **Name**: Enter the bundle product's name.
    - **International barcode**: Enter the new outer-carton barcode if the bundle has one (optional).
    - **Product Uid (Required)**: If the warehouse system is connected to your CYBERBIZ online store, enter the **product SKU** used in the online store (EC) admin panel.
4. **Add items**:
    - Click **Add Item**.
    - Search by keyword or SKU and select the component products.
    - Enter the **Quantity** of each in the bundle.
5. **Add processing items**: Select the processing service the warehouse set up from the drop-down list.
6. Click **Add** to finish.

![](../assets/images/WMS-後台-商品-加工商品-單筆新增加工品01.en.png){ .screenshot }


## Import Bundle Products in Batches { #operate-processed-products-import }

If you need many bundles, use an Excel batch import.

1. Go to **Products > 加工商品** and click **Import** in the upper-right corner.
2. Click **Download Template**.
    ![](../assets/images/WMS-後台-商品-加工商品-批次匯入加工品01.en.png){ .screenshot }
3. Fill in the **bundle item number**, **processing item**, **component SKU**, and **Quantity** in the template format.
    ![](../assets/images/WMS-後台-商品-加工商品-匯入範本01.en.png){ .screenshot }
4. Upload the file and click **Start Import**.

!!! warning "Import Notes"
    **Do not refresh or leave the page** during the import. Wait until the progress bar reaches 100%. Otherwise, data may be damaged or the import may be incomplete.

## Next Steps { #next-steps-processed-products }

<div class="grid cards" markdown>

- :lucide-chart-bar-increasing:{ .lg }
  [__Check Data in the Inventory Summary__](single-items/#operate-single-items-export)
  Download the product inventory summary to make sure records match physical stock.

- :lucide-square-chart-gantt:{ .lg }
  [__Manage Single Products__](single-items.md)
  Add individual products to WMS and set their basic attributes.

</div>
