---
title: "Store and Warehouse Sync Rules"
description: "Learn how inventory syncs between your online store (EC) and the e-commerce warehouse (WMS), how orders are passed to the warehouse, and the basic shipping rules that keep orders flowing."
created: 2026-03-20 00:00
last_modified: 2026-07-21 11:00
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：訂單切換為準備出貨
  - 編輯訂單列表欄位
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
modules:
  - 訂單
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
  - 設定同步開關
  - 管理訂單拋轉
  - 追蹤出貨狀態
features:
  - 庫存同步
  - 自動拋單
  - SKU 關聯
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 商品必須已填寫唯一的商品 SKU（不可為空）
related:
  - wms/single-items/
  - wms/setup-products-stock-limit-preorder/
tags:
  - "Sync Rules"
  - "Order Transfer"
  - WMS
acoiv: venture
apis: []
devices:
  - desktop
ui_components:
  - 官網管理後台
  - WMS 管理後台
paths:
  - 商品 > 所有商品
  - 訂單管理 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5711
  - https://www.cyberbiz.io/support/?p=9638
permalink: "https://help.cyberbiz.io/wms/site-and-warehouse-sync-rules/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Store and Warehouse Sync Rules
Learn how inventory syncs between your online store (EC) and the e-commerce warehouse (WMS), how orders are passed to the warehouse, and the basic shipping rules that keep orders flowing.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## Inventory Sync Rules { #specs-sync-rules }

The system compares inventory at several key moments, so the sellable quantity on your online store matches the physical stock in the warehouse.

### When Sync Runs { #specs-sync-rules-trigger }

1. **Customer checkout**: When a customer checks out on the online store, the system checks stock in real time.
2. **SKU update**: When you change a product SKU in the online store admin panel.
3. **Warehouse inbound and outbound**: After WMS completes a **Stock Receipt** or a **transfer order**.
4. **Scheduled sync**: The system reconciles all inventory automatically at **3:30 AM** every day.
5. **Shortest shelf life update**: When you update a product's [shortest shelf life of good products](single-items/#operate-single-items-add){ data-preview } field.

!!! tip "Key Integration Requirement"
    - **Unique SKUs**: Every product (including each variant) must have a **product SKU**. The system uses the SKU as the unique ID to compare stock on both sides.


## Order Transfer Rules { #specs-order-forwarding }

When your online store gets an order and its items have valid SKUs, the system sends (transfers) the order to WMS by these rules.

### Timing and Mechanism { #specs-order-forwarding-timing }

- **Real-time transfer**: As soon as an order is placed (whatever its payment status), the system tries to send it to WMS.
- **Automatic retry**: At **12:40 AM** every day, the system picks up orders that failed to transfer that day because of network or data errors, and transfers them again.
- **Manual trigger**: In the order list, click **Preparing** on an order to force the transfer.

### Transfer Priority { #specs-order-forwarding-priority }

If several orders are placed at the same time, the system handles them in this order:

1. **Paid orders**: Orders already paid (such as by credit card or confirmed bank transfer) are transferred first.
2. **Cash on delivery orders**: After paid orders are done, these are transferred in order of when they were placed.


## Shipping Rules { #specs-shipping-execution }

After the warehouse (WMS) receives an order, picking and shipping start only when all of these conditions are met:

1. **Order created in WMS**: The order was imported into the warehouse system.
    - In the online store admin panel, go to **Orders > All Orders** and check the warehouse message in the **Logistics Information** field.
    ![](../assets/images/EC-後台-訂單-所有訂單-串倉訂單查看物流訊息01.en.png){ .screenshot }

2. **Payment confirmed**: Orders that are not cash on delivery must be **Paid**.
3. **Enough stock**: Available stock for the SKU in WMS is greater than or equal to the order quantity.



## Notes { #prerequisites-sync-rules }

- **Preventing overselling**: The system syncs at several points, but a burst of orders in a very short time (such as a flash sale) can still oversell. For finer stock control, see [Set Up Products (In Stock, Limited, Preorder)](setup-products-stock-limit-preorder.md).
