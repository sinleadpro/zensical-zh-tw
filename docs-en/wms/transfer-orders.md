---
title: "Transfer Orders"
description: "In the e-commerce warehouse, stock is spread across several warehouse zones. Use a transfer order to move product stock from one zone to another."
created: 2026-03-19 00:00
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
  - 調倉單
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 建立調倉單
  - 批次匯入調倉
  - 追蹤調倉狀態
features:
  - 調倉單
  - 庫內移庫
  - 多倉管理
  - 庫存調度
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 系統中需存在多個可用倉別（如 G 倉與特定的通路專屬倉）
related: []
tags:
  - WMS
  - "Stock Transfer"
  - "Inventory Management"
  - "Multi-Zone Control"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 調倉單列表頁
  - 新增調倉單頁面
  - 調倉單匯入頁面
paths:
  - 調倉單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5737
  - https://www.cyberbiz.io/support/?p=3006
  - https://www.cyberbiz.io/support/?p=4825
  - https://www.cyberbiz.io/support/?p=9068
permalink: "https://help.cyberbiz.io/wms/transfer-orders/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Transfer Orders
In the e-commerce warehouse, stock is spread across several warehouse zones. Use a transfer order to move product stock from one zone to another.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-調倉單-畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-transfer-orders }

### Why Transfer Stock? { #intro-transfer-orders-purpose }

The system can bind each **warehouse zone** to a specific **Channel** (shipping rule). For example:

- **Zone A**: Ships only for a specific platform.
- **Zone B**: Open to all channels.

When zone A runs out of stock, use a transfer order to move products from zone B to zone A, so the specific platform channel can keep shipping.

### Notes { #prerequisites-transfer-orders-notes }

- **Stock locking**: While a transfer order is **Pending Confirmation** or **Processing**, the system may lock that stock so it cannot be used for other shipments.
- **Check details**: Click the **Name** in the transfer order list at any time to see the items and history of that transfer.


## Transfer Order Statuses { #specs-transfer-orders-status }

Track transfer progress by status in the list:

| Status | Description |
| :--- | :--- |
| **Pending Confirmation** | The order was created and is waiting for warehouse customer service to review and confirm it |
| **Processing** | Warehouse staff are checking the products and moving them on site |
| **Done** | The transfer is done, and available stock in the destination zone has increased |


## Create a Transfer Order Manually { #operate-transfer-orders-create }

For small stock moves, add a transfer order directly in the admin panel.

1. Go to **Transfer**.
2. **Choose zones**:
    - **Source Zone**: Select the zone where the products are now.
    - **Destination Zone**: Select the zone to move them to.
3. **Select Product**:
    - Click **Add Item**.
    - Search for and select products, and enter the **Quantity** to move.
4. Click **Confirm** to submit.
5. **Key step**: After you create the transfer order, be sure to **contact warehouse customer service** so they can confirm the physical move.

![](../assets/images/WMS-後台-調倉單-單筆新增調倉單01.en.png){ .screenshot }


## Import Transfer Orders in Batches { #operate-transfer-orders-import }

To move many products at once, use the import feature.

1. Go to **Transfer**.
2. Click **Import** in the upper-right corner.
3. Download the template, fill it in, and upload the file.
4. Select the file and click **Import**.

![](../assets/images/WMS-後台-調倉單-批次匯入調倉單01.en.png){ .screenshot }

## Export Transfer Orders { #operate-transfer-orders-export }

To reconcile stock changes or keep transfer records, export the details.

1. Go to **Transfer**.
2. Click **Export** in the upper-right corner.
3. The system creates and downloads the **transfer order details** file.

![](../assets/images/WMS-後台-調倉單-匯出調倉單01.en.png){ .screenshot }
