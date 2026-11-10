---
title: "POS Inventory Management Report"
description: "The Report List provides multi-dimensional data analysis tools that help managers reconcile daily accounts, monitor sales performance, and track omnichannel inventory flow."
created: "2026-03-15 23:01"
last_modified: 
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 
feedback:
products:
  - POS
modules: []
sites:
  - TW
audiences: 
  - merchant
difficulty: ""
tnb: branch
plans: 
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: [] 
intents:
  - 查看每日出金報表
  - 查詢訂單匯總報表
  - 查看商品銷售報表
  - 查詢商品庫存與銷售狀況
  - 查詢全通路庫存與商品流向
features:
  - 每日出金報表
  - 訂單匯總報表
  - 商品銷售報表
  - 商品庫存銷售報表
  - 全通路庫存流向報表
prerequisites: []
related:
  - pos/check/
  - pos/orders/manage-general-orders/
tags:
  - POS
  - "Sales Report"
  - "Account Reconciliation"
  - "Inventory Management"
  - "Revenue Calculation"
  - "Sales Recognition"
  - Omnichannel
  - "Store Management"
acoiv: operation
apis: []
devices: 
  - desktop 
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=25099
permalink: "https://help.cyberbiz.io/pos/inventory/pos-reports-list-guide/"
comments: ""
search:
  exclude: false
icon: lucide/chart-bar
hide:
---
# POS Inventory Management Report
The Report List provides multi-dimensional data analysis tools that help managers reconcile daily accounts, monitor sales performance, and track omnichannel inventory flow.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


## Access Path { #intro-pos-reports }

1. Log in to the admin, go to **POS > POS Store List**, and select the store.
2. Click **Inventory Management > Reports**.

![](../../assets/images/POS-後台-所有POS商店-庫存管理-報表01.en.png){ .screenshot }

## Report Types { #specs-pos-reports }

### Daily Cash-Out Report { #specs-pos-reports-report }

*   **Features**: View daily closing details, cash deposits, petty cash balance, income status, and information about the staff who performed each action.
*   **Use Cases**: Suitable for store managers to reconcile cash after daily business hours.

### Order Summary Report { #specs-pos-reports-order-report }

*   **Features**: View the order creation date, order confirmation date, cancellation date, order number, invoice information, POS terminal number, customer name, payment method, and order notes.
*   **Use Cases**: Revenue calculation and inventory verification.

### Product Sales Report { #reference-pos-reports-product-sales }

*   **Features**: View each product's vendor source, category, units sold, units returned, and total sales.
*   **Use Cases**: Sales recognition and bonus calculation.


![](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/POS後台－報表列表2.png){ .screenshot }

### Product Inventory and Sales Report (By Vendor) { #specs-pos-reports-product-inventory-report }

*   **Features**: Filter by vendor to view inventory balances and sales status for that vendor's products in one place.

![](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/POS後台－報表列表3.png){ .screenshot }

### Omnichannel Inventory and Product Flow Report (By Product) { #specs-pos-reports-channel-inventory-product }

*   **Features**: View the inventory quantity of a specific product at each store, as well as its flow history.

![](https://www.cyberbiz.io/support/wp-content/uploads/2022/01/POS後台－報表列表4.png){ .screenshot }

## Report Calculation Standards { #specs-report-standard }

- **Order Summary Report**: Based on **Order Creation Time**.
- **Product Sales Report**: Based on **Order Confirmation Date**.

    !!! tip "Order Confirmation Date Settings and Search"
        - **Setup Method**: POS cashiers can fill in the order confirmation date manually during [Payment Processing](../check/index.md#operate-check-payment).
        - **Search Path**: Front-desk staff can use **Advanced Filter** on the [Orders](../orders/manage-general-orders.md#operate-general-orders-query) tab to search orders by a specified date range.

- **Product Flow Report**: Based on **Order Creation Time**.

