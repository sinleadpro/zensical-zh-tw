---
title: "Order Filters and Statuses Reference"
description: "Complete reference of CYBERBIZ admin order filters, including payment status, delivery status, return status, order status, and keyword matching logic."
created: 2026-05-08 09:38
last_modified: 2026-07-13 09:58
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 查詢訂單狀態
  - 了解篩選條件
features:
  - 付款狀態查詢
  - 配送狀態查詢
  - 退貨狀態查詢
  - 訂單狀態查詢
  - 關鍵字匹配
prerequisites: []
related:
  - ec/orders/references/payment-statuses/
  - ec/orders/references/fulfillment-statuses/
  - ec/orders/references/shipping-methods/
tags:
  - "Order Filters"
  - "Order Status"
  - "Payment Status"
  - "Delivery Status"
  - "Return Status"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/order-filter-status-reference/"
comments: false
search:
  exclude: false
icon: lucide/file-search
hide: []
---

## Filter Overview { #orders-v2-filters }  

!!! info "The available filter fields and options change based on your **plan** or **admin feature settings**."


| Filter | Description |
|---|---|
| **[Order Status](#orders-status){ title="Order Status Reference" data-preview }** | Filter by overall order status (In Progress / Completed / Canceled) |
| **[Payment Status](payment-statuses.md#payment-statuses){ title="Order Payment Status Reference" data-preview }** | Filter by payment collection / refund status (Payment Received, Awaiting Payment, Refunded, and so on) |
| **[Delivery Status](fulfillment-statuses.md#fulfillment-statuses-table){ title="Delivery Status Reference" data-preview }** | Filter by shipping status (Unshipped, Shipped, Arrived at Store, and so on) |
| **[Return Status](#orders-return-status){ title="Return Status Reference" data-preview }** | Filter by return status (Return Requested, Returning, Returned, and so on) |
| **[Order Source](#orders-store){ title="Order Source Reference" data-preview }** | Distinguish online EC orders from orders at each POS store |
| **[Merchant Source/<br>Remittee](#orders-merchant-from){ title="Remittee Reference" data-preview }** | Filter by who actually collects the payment (Shunli collection / Merchant / POS / Warehouse) |
| **[Delivery Type](shipping-methods.md#shipping-methods){ title="Shipping Methods Reference" data-preview }** | Filter by logistics channel (convenience store pickup, home delivery, self-pickup, and so on) |
| **Product Distribution Channel** | Filter by the product channel tags in the order, for multichannel selling |
| **Delivery Temperature** | Filter by the ambient / refrigerated / frozen temperature zone assigned to products |
| **Tags** | Filter by your custom order tags (can be added manually in order details) |
| **Order Products** | Select specific products to show only orders that include them |
| **[Order Type](#orders-line-group-buy){ title="Order Type Reference" data-preview }** | Filter LINE group buying orders |
| **Order Date** | Filter by order creation time, with "Between" and "Past N days" modes |
| **Order Delivery Date** | Filter by scheduled or actual delivery date, with "Between" and "Past N days" |

<!--

## Order Filter Reference { #orders-filter }


All filters available in the system:

=== "Statuses"

	Used to track key points in the order lifecycle.

	- **Order Status:** Overall order progress (such as In Progress, Completed, Canceled).

	- **Payment Status:** Payment reconciliation (such as Unpaid, Payment Received, Refunding).

	- **Delivery Status:** Logistics progress (such as Unshipped, Shipped, Arrived).

	- **Return Status:** After-sales progress (such as Return Requested, Reviewing Return, Returned).


=== "Channels and Tags"

	Used to distinguish order sources and custom categories.

	- **Product Distribution Channel:** Distinguishes order sources (such as website, stores, third-party platforms).

	- **LINE:** Filters orders from LINE features (such as LINE Shopping and LINE OA).

	- **Remittee:** If you have multiple payment accounts, use this to tell which account received the payment.

	- **Tags:** Categorizes by tags you added (such as VIP customer, urgent).


=== "Date Ranges"

	- **Order Date:** The time the shopper placed the order.

	- **Order Delivery Date:** The scheduled/actual shipping time recorded by the system or entered by the merchant.

-->

## Return Status Reference { #orders-return-status }


| Return Status | Description |
| :-- | :-- |
| No Return Needed | The order has no return |
| Return Requested | The customer requested a return, pending merchant review |
| Reviewing Return | The merchant is reviewing the return request |
| Returning | The return is in progress, and the package is on its way back from the customer |
| Partially Returned | Some items in the order have been returned, and the rest are kept |
| Return Rejected | The merchant reviewed and declined the return |
| Transit Center | The return package has arrived at the logistics transit center |
| Original Sender Store | The return package is back at the original sender convenience store |
| Returned   | The customer completed the return, and the package is back with the merchant |


## Order Status Reference { #orders-status }


| Order Status | Description |  
| :-- | :-- |  
| In Progress | The order is placed but not yet closed or canceled; shipping, payment, returns, and other actions are still possible |  
| Completed | The whole order process is complete (paid, shipped, received, and so on), with no further changes |
| Canceled | The order was stopped because the customer or merchant canceled it; related payment / logistics won't continue |  


## Remittee Reference { #orders-merchant-from }


| Remittee | Description |  
| :-- | :-- |  
| Shunli collection | CYBERBIZ (Shunli) collects payments and issues invoices, then pays out to the merchant on the settlement cycle |  
| Merchant | The merchant collects payment directly with its own payment account (requires the "Own Payment Provider" feature) |  
| POS merchant | Payment collected in store through POS (credit card, cash, and so on) and recorded directly by POS |
| Warehouse | The warehouse collects payment, common in certain 3PL warehousing partnerships |


!!! note "Note"
    This filter appears only for Enterprise, PLUS plans (Expert PLUS / Advanced PLUS / Professional PLUS), or stores without the "Own Payment Provider" feature.

## Order Source Reference { #orders-store }  

| Order Source | Description |  
| :-- | :-- |  
| CYBERBIZ | Orders placed through the online EC store (web / app / mobile site) |  
| Each POS store | Orders checked out at physical stores through POS; the drop-down lists all your active POS stores |  

!!! note "This filter appears only when the **POS system** is turned on."

## Order Type Reference { #orders-line-group-buy }


| Order Type | Description |
| :-- | :-- |
| LINE group buying | Orders placed through **LINE group buying** (customers order in LINE groups) |

!!! note "Note"
    This filter appears only when **LINE group buying** is turned on. Leaving it unselected means "all order types" (including regular EC orders and LINE group buying orders).  

## Warehouse Type Reference { #orders-warehouse-type }  

| Warehouse Type | Description |
| :-- | :-- |  
| Self-shipped | Orders the merchant picks, packs, and hands to the carrier |  
| CYBERBIZ e-commerce warehousing | Orders picked and shipped by CYBERBIZ's own warehouse (Fengchao) |
| Mixed orders (self-shipped + CYBERBIZ e-commerce warehousing) | Within one order, some items are shipped by the merchant and some by CYBERBIZ warehousing |
| Amazon logistics | Orders shipped by Amazon FBA |
| Mixed orders (self-shipped + Amazon logistics) | Within one order, some items are shipped by the merchant and some by Amazon FBA |
| EZCAT cold-chain warehouse | Orders shipped by the EZCAT cold-chain warehouse (for frozen / refrigerated products) |  

!!! note "Note"
    - This filter appears only for stores with **partial warehouse integration** activated. The default option is **"All Shipping Types."**  
    - The "Mixed orders" options identify **single orders shipped from multiple warehouses**, helping pickers handle them by warehouse.
    - Options appear in the drop-down based on the warehouse integrations you actually use; inactive warehouses aren't listed.

## Keyword Matching Rules { #orders-match-mode }

To improve search speed and accuracy, the system uses two search modes for different fields. If you don't get the results you expect, check that your input matches the field's matching rule.

=== "Exact Match"

	These fields must **match your search exactly** to return results:

	- **Customer information**: Shopper email, member email.

	- **Logistics information**: Tracking number.

	- **Product information**: Product SKU.

	- **Recipient information**: Recipient phone, recipient full address.

	- **Payment information**: Payment provider order number.

=== "Partial Match"

	These fields support searching with **partial information**:

	- **Order information**: Order number, coupon code, order source (such as POS user ID).

	- **Product information**: Product name.

	- **Delivery information**: Recipient name, delivery type, warehouse status (only for Fengchao Logistics integrations).

## What's in the Shipping Label Download { #reference-logistics-zip-contents }

When you run "Download Shipping Labels and Change to Shipped" in the admin, the system creates a ZIP file. It contains 4 PDF files covering the full process of picking, packing, reconciliation, and delivery:

| File | Purpose | Recipient |
|---|---|---|
| **Shipping Label** | Used by the carrier for pickup and delivery; print on the carrier's blank shipping label stickers and stick on the package | Driver |
| **Packing Slip** | Packing slip included in the package, with items and quantities | Shopper (in the package) |
| **Picking List** | Warehouse picking list, grouped by item for easy picking | Internal warehouse staff |
| **Order Details** | Full order information, including amounts, payment method, and shopper details | Internal records / customer service |
