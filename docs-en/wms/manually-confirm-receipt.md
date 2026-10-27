---
title: "Manually Confirm Receipt"
description: "If a convenience store fails to send the pickup status, manually set the warehouse order to Received so that accounting can be closed and returns can proceed."
created: 2026-02-25 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: troubleshooting
author: Ann
reviewers: []
notes:
  - 內部連結：倉儲退貨、退貨進倉作業、退款作業
ga_views: 0
feedback: 0
products:
  - WMS
modules:
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
  - 手動更新收貨狀態
  - 處理物流貨態異常
features:
  - 手動確認收貨
  - 訂單狀態管理
  - 超商物流追蹤
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 僅限超商出貨訂單
related:
  - ec/orders/order-return-process/
  - wms/returns-and-vehicle-dispatch/
  - ec/orders/order-refund-process/
tags:
  - WMS
  - "Manual Receipt Confirmation"
  - "Order Status"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 訂單詳情頁面
  - 手動收貨確認彈窗
paths:
  - 訂單 > 列表
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=9105
permalink: "https://help.cyberbiz.io/wms/manually-confirm-receipt/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Manually Confirm Receipt
If a convenience store fails to send the pickup status, manually set the warehouse order to Received so that accounting can be closed and returns can proceed.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## Before You Start { #prerequisites-receipt }

### When to Use { #prerequisites-receipt-scenario }

For an order shipped to a convenience store, the store may fail to send the picked-up status. After you confirm with the customer that the item was delivered and picked up, manually change the shipping status to **Received**.


### Limits and Rules { #specs-receipt-limits }

- **Order type**: Only **convenience store pickup** orders are supported.
- **Delivery status**: The order must currently be **Shipped**.
- **Shipping status condition**: One of these exceptions applies:
    - The waybill status shows **Problem**.
    - The item reached the store more than **7 days** ago and the status has not updated.
- **Cannot be undone**: After you confirm receipt manually, the order cannot go back to its original status. If you change it by mistake, start a return to correct the accounting.

### Notes { #prerequisites-receipt-notes }

- **Responsibility**: Before you confirm receipt manually, make sure the customer actually picked up the item.
- **Fixing mistakes**: If you later find the item was not picked up (for example, the parcel was lost), start the [return process](../ec/orders/order-return-process.md) manually so that the [warehouse return inspection](returns-and-vehicle-dispatch.md#operate-return-dispatch-reverse-logistics) and the [order refund](../ec/orders/order-refund-process.md) can be done.


## Steps { #operate-receipt }

1. Go to **Orders > 列表**.
2. Click the **order number** of the order to open its details page.
3. In the delivery information section, click **Confirm Received**.

![](../assets/images/WMS-後台-訂單-列表-超商訂單手動確認收貨01.en.png){ .screenshot }
