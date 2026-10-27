---
title: "Transfer Inventory Between POS and the Warehouse"
description: "If you use EC, POS, and WMS together, transfer stock between stores, check WMS stock allocation, and move inventory between online and offline warehouse zones."
created: 2026-03-20 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 確認版本限制
  - 圖片介面過舊
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
  - POS
modules:
  - 庫存
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
  - 申請門市補貨
  - 查詢管道庫存
  - 執行線上線下庫存互調
features:
  - 門市調貨
  - 倉別轉調
  - 庫存分配
  - POS 集成
prerequisites:
  - 需同時開通 CYBERBIZ EC、POS 與 WMS 三項服務
  - 需完成門市與總倉之關聯設定
related:
  - wms/transfer-orders/
tags:
  - "POS Stock Transfer"
  - "WMS Inventory"
  - Three-in-One
acoiv: venture
apis: []
devices:
  - desktop
  - tablet
ui_components:
  - POS 前台
  - WMS 管理後台
paths:
  - 商品 > 單一品項
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=28494
permalink: "https://help.cyberbiz.io/wms/pos-warehouse-inventory-transfer/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Transfer Inventory Between POS and the Warehouse
If you use EC, POS, and WMS together, transfer stock between stores, check WMS stock allocation, and move inventory between online and offline warehouse zones.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing / Smart POS
{ .doc-badge }

## Three-in-One Inventory { #overview-pos-transfer }

In the three-in-one (EC + POS + WMS) setup, products in the e-commerce warehouse are split by sales channel:

- **CYBERBIZ-G**: Stock for online store (EC) sales.
- **CYBERBIZ-POS**: Stock for transfers to physical stores (POS).



## Request a Transfer from the Main Warehouse to a POS Store { #operate-pos-transfer-request }

If store staff find that stock is low, they can request a transfer from the WMS main warehouse in the POS app.

1. Log in to the **POS app**, go to **Inventory**, and click **Create Transfer**.
2. In the **Source Store** field, select **POS Main Warehouse**.
3. Search for the products to restock and click to add them to the list.
4. Enter the **transfer quantity** on each item row.
5. Check the POS main warehouse's available stock and make sure each request does not exceed it.
6. Add a note if needed, and then click **Create Transfer**.

!!! tip "What Happens Next and How to Cancel"
    - **Shipping**: After you submit the request, WMS receives it and starts picking and shipping to the store.
    - **Cancel**: If you find a mistake after submitting, **you cannot delete it from POS**. Contact your WMS contact right away to confirm that work has not started, and ask the warehouse staff to stop it manually.

![](../assets/images/POS-前台-庫存-向POS總倉調貨01.en.png){ .screenshot }

## Check WMS Stock Allocation { #overview-pos-transfer-inventory }

Managers can monitor how stock is split between the EC and POS channels in the WMS admin panel.

1. Log in to the **WMS admin panel** and go to **Products > 單一品項**.
2. Find the product, and then open **Product Stock List**.
3. In the pop-up window, check the stock in each zone:
    - **CYBERBIZ-G** = stock left in the online EC main warehouse.
    - **CYBERBIZ-POS** = stock left in the offline POS main warehouse.

![](../assets/images/WMS-後台-商品-單一品項-查看POS總倉庫存01.en.png){ .screenshot }

## Transfer Stock Between Online and Offline { #operate-pos-transfer-internal }

If the POS main warehouse runs out but the EC main warehouse still has stock, managers can move online stock to the stores with an internal transfer.

1. Open the **WMS admin panel**, go to [Transfer Orders](transfer-orders.md), and click **Create Transfer**.
2. **Set the transfer route**:
    - **Source warehouse**: Select **CYBERBIZ-G**.
    - **Destination warehouse**: Select **CYBERBIZ-POS**.
3. Click **Add Item** and enter the items and quantities to transfer.
4. Check the details and submit. The system deducts the online stock and adds it to the offline available stock automatically.

![](../assets/images/WMS-後台-調倉單-調貨給POS總倉01.en.png){ .screenshot }
