---
title: "Return Orders"
description: "Handle return requests in the e-commerce warehouse system, including pickup dispatch, inspection status, and the refund process that follows."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 檢查：退貨單狀態
  - 檢查：僅 EC 高手版可於倉儲建退貨單？
  - 內部連結：EC逆物流、倉庫串倉商家退貨流程
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 退貨單
  - 訂單
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 申請退貨派車
  - 手動建立退貨單
  - 查看驗收狀態
features:
  - 退貨管理
  - 逆物流派車
  - 倉儲驗收
  - 退款連動
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 訂單需已完成出貨作業
related:
  - ec/orders/order-return-process/
  - wms/returns-and-vehicle-dispatch/
tags:
  - WMS
  - Inspection
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 訂單明細頁面
  - 退貨單列表頁
  - 新增退貨單頁面
paths:
  - 訂單 > 列表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5747
  - https://www.cyberbiz.io/support/?p=9139
permalink: "https://help.cyberbiz.io/wms/return-orders/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Return Orders
Handle return requests in the e-commerce warehouse system, including pickup dispatch, inspection status, and the refund process that follows.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-退貨單-畫面總覽01.en.png){ .hero-page }


## Which Return Process to Use { #overview-return-orders }

- **Warehouse-only merchants**:
    - **Who**: Merchants who use only the CYBERBIZ warehouse system and do not connect it to a CYBERBIZ online store.
    - **Where**: Handle all return requests and restocking in the WMS warehouse system. Follow the steps below.
- **Merchants with an integrated online store**:
    - **Who**: Merchants who use a CYBERBIZ online store with warehouse integration turned on, on the **Expert** plan.
    - **Where**: You can process returns in the warehouse system, and the system syncs the status to the online store admin panel automatically. Follow the steps below.

!!! info "Returns for Merchants with an Integrated Online Store"
    - **Merchants on any plan**: Process returns, dispatch, and refunds in the **online store (EC) admin panel**. See the [EC order return process](../ec/orders/order-return-process.md).
    - **Expert plan merchants**: Besides EC, you can also request returns in the **WMS admin panel**.

## Before You Start { #prerequisites-return-orders }

- **Use only one** of the methods below, **and do not repeat it**. Otherwise, the system creates duplicate orders.


## Method 1: Request a Return from the Order Page { #operate-return-orders-apply }

1. Go to **Orders > 列表**.
2. Click the order to open its details page.
3. Choose a return mode:

![](../assets/images/WMS-後台-訂單-列表-訂單執行退貨01.en.png){ .screenshot }

=== "Return with Dispatch"

    The system sends a pickup request to the carrier and creates a return order automatically.

    - **Supported carriers**: Only **T-Cat** and **Pelican** are supported for now.
    - **Required information**: Enter the buyer's **pickup address** correctly (a convenience store address is not allowed).
    - **Note**: For **Expert** plan merchants with **CYBERBIZ PAYMENTS** turned on, WMS hides this button. Go back to the **EC admin panel** and submit a [reverse logistics request](../ec/orders/order-return-process/#operate-order-return-reverse) so the payment can be refunded automatically.

    ![](../assets/images/WMS-後台-訂單-列表-訂單執行退貨02.en.png){ .screenshot }

=== "Return Without Dispatch"

    The system creates a return order (a digital record) automatically, without dispatching a vehicle.

    ![](../assets/images/WMS-後台-訂單-列表-訂單執行退貨03.en.png){ .screenshot }



## Method 2: Create a Return Order Manually { #operate-return-orders-manual }

### When to Use { #prerequisites-return-orders-context }

- **No matching original order**: The returned items were not shipped through this warehouse system, but they need to go back to the warehouse for return receiving.
- **Return contents differ**: The original order exists, but the **items** or **Quantity** the customer actually sent back do not match the order. Create the return order manually to record what actually arrived.

    > This is for **warehouse-only merchants**. **Merchants with an integrated online store** should follow [Returns and Vehicle Dispatch](returns-and-vehicle-dispatch.md).

### Notes { #prerequisites-return-orders-notes }

- Return orders **do not dispatch vehicles**. They only serve as records for **warehouse receiving** and for returns and refunds.

### Steps { #operate-return-orders-steps }

1. Go to **Return Order** and click **Add Return Order**.
2. Fill in the details:
    - **Order number**: Enter it if the return relates to a specific order, to make reconciliation easier.
    - **Return items and quantities**: Enter exactly which products are expected back.

![](../assets/images/WMS-後台-退貨單-建立退貨單01.en.png){ .screenshot }

## Warehouse Inspection and Return Order Status { #specs-return-orders-status }


| Return Order Status | Description |
| :--- | :--- |
| **Awaiting Pickup** | The return order was created and is waiting for carrier pickup or for the items to be sent back to the warehouse |
| **Accepted** | All items in the order were returned and reached the warehouse. Staff checked the items and put them back into stock |
| **Partially Accepted** | Some items in the order were returned and reached the warehouse. Staff checked the items and put them back into stock |
