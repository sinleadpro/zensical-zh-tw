---
title: "Order List"
description: "The order list in the e-commerce warehouse system (WMS) is the main screen for managing shipping progress and stock allocation. It shows which warehouse stage each order is in."
created: 2026-03-12 00:00
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
  - 電商倉儲
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
  - 查看訂單狀態
  - 匯入第三方訂單
  - 匯出出貨報表
features:
  - 訂單管理
  - 訂單狀態追蹤
  - 數據匯入匯出
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
related: []
tags:
  - "Order Status"
  - "Screen Guide"
  - "Report Export"
  - "Order Import"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 訂單列表頁面
paths:
  - 訂單 > 列表
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=9105
  - https://www.cyberbiz.io/helpcenter/?p=5744
permalink: "https://help.cyberbiz.io/wms/list/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Order List
The order list in the e-commerce warehouse system (WMS) is the main screen for managing shipping progress and stock allocation. It shows which warehouse stage each order is in.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-訂單-列表-畫面總覽01.en.png){ .hero-page }


## Order List Screen { #overview-order-list }

Go to **Orders > 列表** to see all orders imported into the e-commerce warehouse system. The screen offers many filters to help you find specific orders quickly.

### Filters { #operate-order-list-filter }

Use these filters to find exactly the orders you need to handle:

- **Basic search**:
    - **Search conditions**: Search directly by **order number**, **Customer Name**, **mobile number**, and other key details.
    - **Search Range**: Set a date range by **Created At** or **payment time**.
- **Order stage**:
    - **Order Status**: Filter by stage (such as Pending, Processing, or Completed).
    - **Goods / shipping status**: Separate goods preparation from delivery progress.
- **Source and routing**:
    - **Channel**: Filter orders from your brand website or other integrated (imported) channels.
    - **Shipping Status**: Track where a parcel currently is with the carrier (such as Shipped or In Delivery).
- **Priority**:
    - **Urgent Status**: Quickly filter orders marked as priority or urgent so they ship on time.



## Order Statuses { #specs-order-status }

The order status shows where the order is between the WMS system and the physical warehouse. The main stages are:

| Status | Definition | Order Editable |
| :--- | :--- | :--- |
| **Pending** | The order is in the system but has **not yet been sent** to the warehouse | ✓ |
| **Processing** | The order was sent to the warehouse for picking and packing | ✕ |
| **Shipped** | The warehouse finished the order, and the parcel was picked up by the carrier or left the warehouse | ✕ |
| **Cancelled** | Shipping for the order was stopped | ✕ |
| **no stock** | An item in the order has less stock than needed. The order moves to shipping, automatically or manually, after the warehouse's physical stock is topped up | ✕ |


When a return is requested, the order moves to one of these statuses:

| Status | Definition |
| :--- | :--- |
| **withdraw** | A return was requested, and a vehicle was dispatched for pickup or the customer is sending the items back. Waiting for the returned items to reach the warehouse |
| **Return Received** | All items in the return order reached the warehouse and passed inspection |
| **Return Partially Inspected** | Only some returned items reached the warehouse and passed inspection |


## Import and Export Data { #operate-order-list-data }

### 1. Import Orders { #operate-order-list-import }

Use the import feature when orders from channels not connected to your website need to ship from the warehouse.

- **Where**: Click the **Import** button on the right of the list.
- **Required steps**:
    1. **Download the template**: Fill in order details in the Excel format the system provides.
    2. **Upload Attachment** (optional): Upload documents to ship with the goods, such as purchase orders, sales slips, receiving notices, or shipping mark files, or documents the recipient needs at delivery.
    3. **Run the import**: After uploading, click Import. The system creates an import record.

### 2. Export Reports { #operate-order-list-export }

Export filtered order data as a report for reconciliation or analysis.

- **How**: Set your filters, and then click **Export** on the right of the page to download an Excel report.
