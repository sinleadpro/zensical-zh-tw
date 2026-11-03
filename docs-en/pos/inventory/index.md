---
title: "Omnichannel Inventory Management Guide"
description: "This guide explains how inventory works between CYBERBIZ POS and the EC system and provides standard procedures for Stock In, Stock Transfer, Stock Out, and Stock Count."
created: 2026-04-08 11:36
last_modified: 2026-06-30 21:55
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
  - 全通路庫存管理
  - 商品
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 管理全通路庫存
  - POS 進出倉操作
  - 執行庫存盤點
  - 申請門市調倉
features:
  - EC POS 庫存同步
  - 第三方進倉
  - 自動產生出倉單
  - 庫存校正
prerequisites: []
related:
  - pos/inventory/outbound-orders/
  - pos/inventory/inbound-orders/
  - pos/inventory/transfer-orders/
  - pos/inventory/inventory-adjustment/
  - pos/inventory/inventory-count/
tags:
  - "Omnichannel Inventory"
  - "POS Inventory Management"
  - "Stock In"
  - "Stock Out"
  - "Stock Count"
acoiv: operation
apis: []
devices:
  - desktop
  - tablet
ui_components:
  - 進倉單
  - 出倉單
  - 調倉單
  - 盤點單
paths:
  - 商品 > 所有商品
  - 商品 > 所有商品 > 點擊指定商品
  - 商品 > Excel 大量匯入商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=27443
permalink: "https://help.cyberbiz.io/pos/inventory/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Omnichannel Inventory Management
This guide walks you through how inventory works between CYBERBIZ POS and the EC system and provides standard procedures for Stock In, Stock Transfer, Stock Out, and Stock Count.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


!!! tip "Use Cases"
    - **Cross-Channel Inventory Sync**: When a merchant runs both an online store and physical stores, set up and keep EC and POS inventory separate.
    - **Inter-Store Transfers**: When Store A is out of stock, it requests stock from Store B, and the stock-out and stock-in steps complete automatically.
    - **Regular Stock Counts**: Store staff periodically count actual stock and correct book quantities in the system.


## Understand the System

Before you begin, make sure you understand the CYBERBIZ inventory structure, because it determines your daily operations.

### System Warehouse Structure

The CYBERBIZ system manages **EC website inventory** and **POS store inventory** as separate warehouses:

1. **EC warehouse**: Manages the shipping inventory for website orders.
2. **POS store warehouse**: Each physical store has its own inventory, which does not affect other stores.

!!! tip "Online and Offline Inventory Management"

    We recommend physically separating **website items awaiting shipment** from **store items for sale** in the warehouse or store back room, so staff do not mix them up during picking or counting.


### Choose an Inventory Management Mode

Based on your brand's operational needs, choose one of the following modes:

- **Store (Website) as Central Warehouse Mode**: Goods enter the **EC warehouse** or a designated **POS store warehouse**. That warehouse then distributes goods to the EC warehouse and each POS store.
- **Third-Party Central Warehouse Mode**: Goods enter the **third-party warehouse**. The website and each store order directly from the third-party warehouse and carry out their own stock-in processes.


## Inventory Management

### Manage EC Inventory

=== "Inventory Adjustment Records Can Be Searched After Changes"

    If you need a complete inventory adjustment record, use the methods below to adjust inventory.

    #### Manage Omnichannel Inventory for EC and POS

    1. Log in to the POS back office and go to **POS > Inventory Management**.
    2. Choose a method based on the type of inventory change:

        | Operation Type | Inventory Change | Responsible Role | Practical Use Case |
        | ------- | -------- | ------- | ----------- |
        | [Stock Out](outbound-orders.md) | Decrease | Shipping party | Any warehouse proactively ships to another warehouse |
        | [Stock In](inbound-orders.md) | Increase | Receiving party | **[Third-Party Central Warehouse Mode] Goods Receipt** |
        | [Stock Transfer](transfer-orders.md) | Increase | Receiving party | **[Store (Website) as Central Warehouse Mode] Goods Receipt**<br>An out-of-stock store requests inventory transfer support from other stores |
        | [Inventory Adjustment](inventory-adjustment.md) | Decrease/Increase | Any | Third-party central warehouse creates inventory<br>Manually adjust when inventory is abnormal<br>Correct inventory when products are damaged or scrapped |
        | [Stock Count](inventory-count.md) | Decrease/Increase | Any | After physically counting store product quantities, correct the system book values |


=== "Inventory Adjustment Records Cannot Be Searched After Changes"

    Update EC inventory in the following ways. The system cannot trace adjustment records, and the changes do not appear in standard reports.

    If you later need to trace the original data, contact CYBERBIZ customer service for assistance. Related services may incur a technical processing fee based on the volume of data and the time range requested.

    === "Edit a Single Item on the Product List Page"

        1. Log in to the POS back office and go to **Products > All Products**.
        2. Directly edit the **Inventory Quantity** field.

    === "Edit a Single Item on the Product Details Page"

        1. Log in to the POS back office and go to **Products > All Products > Click the target product**
        2. Directly edit the **Inventory Quantity** field.

    === "Batch Edit Using the Excel Import Feature"

        1. Log in to the POS back office and go to **Products > All Products**.
        2. Select the POS products whose inventory you want to change, then choose **Export product**.
        3. Go to **Products > Import Products from Excel**.
        4. Upload the completed Excel file.


### Manage POS Inventory

=== "Manage Omnichannel Inventory for EC and POS"

    Log in to the POS back office and go to **POS > Inventory Management**.


=== "Manage Inventory for a Specific POS Store"


    === "Manage in the Back Office"

        Log in to the POS back office and go to **POS > POS Store List > Select the target store > Inventory Management**.

    === "Manage in the POS Front End"

        Log in to the POS front end and go to **Inventory**.

         > Only store managers can perform this action. Store staff do not have this permission.

Choose a method based on the type of inventory change:

| Operation Type | Inventory Change | Responsible Role | Practical Use Case |
| ------- | -------- | ------- | ----------- |
| [Stock Out](outbound-orders/) | Decrease | Shipping party | Any warehouse proactively ships to another warehouse |
| [Stock In](inbound-orders/) | Increase | Receiving party | **[Third-Party Central Warehouse Mode] Goods Receipt** |
| [Stock Transfer](transfer-orders/) | Increase | Receiving party | **[Store (Website) as Central Warehouse Mode] Goods Receipt**<br>An out-of-stock store requests inventory transfer support from other stores |
| [Inventory Adjustment](inventory-adjustment/) | Decrease/Increase | Any | Third-party central warehouse creates inventory<br>Manually adjust when inventory is abnormal<br>Correct inventory when products are damaged or scrapped |
| [Stock Count](inventory-count/) | Decrease/Increase | Any | After physically counting store product quantities, correct the system book values |


## Initial Inventory Setup

If you already use the EC website system, be sure to complete the following **Inventory Initialization** steps after you officially activate POS. This keeps online and offline channel records separate and accurate:

1. **Correct EC Online Inventory**:
    First, make sure the existing inventory data on your website is accurate. See [Manage EC Inventory](#管理-ec-庫存) and choose the update method that suits you.
2. **Set Up Initial POS Store Inventory**:
    For the existing quantities of products at your physical store, choose [Stock In](inbound-orders/) or [Inventory Adjustment](inventory-adjustment/) to initialize them.

After the initial stock-in is complete, for day-to-day inventory management, see [Manage POS Inventory](#管理-pos-庫存) and choose the update method that suits you.



