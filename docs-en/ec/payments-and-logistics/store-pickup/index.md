---
title: "Store Pickup: Omnichannel Operations Navigation"
description: "Integrate online shopping with offline pickup to give customers a flexible shopping experience, and optimize OMO operational efficiency through close collaboration between the back office and the POS system."
created: 2026-04-27 16:55
last_modified: 2026-06-22 11:15
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 金物流
  - 訂單
  - 分潤
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
  - 設定門市取貨
  - 處理門市取貨訂單
  - 門市包裹入庫
  - 顧客到店取貨
features:
  - 門市取貨
  - POS 門市取貨
  - 店員分潤
prerequisites: []
related:
  - ec/payments-and-logistics/create-stores/
  - ec/payments-and-logistics/store-pickup/enable-store-pickup-service/
  - ec/orders/store-pickup-orders/
  - pos/orders/store-pickup-orders-inbound-and-pickup/
  - pos/store/pos-store-pickup-staff-commission/
tags:
  - "Store Pickup"
  - OMO
  - Omnichannel
  - "In-Store Pickup"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
  - tablet
ui_components:
  - 門市取貨設定
  - 門市訂單
  - 到店條碼
paths:
  - 金物流 > 所有門市
  - 訂單 > 門市訂單
  - 分潤 > 門市取貨店員分潤
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/store-pickup/"
comments: false
search:
  exclude: false
icon: lucide/store
hide:
  - feedback
---

# Store Pickup: Omnichannel Operations Navigation

**Store Pickup** is the core feature that enables OMO (Online Merge Offline). With this service, customers can place orders on the online store and choose to pick up at a physical store. This saves customers shipping fees and gives them flexible pickup options, while also effectively directing online traffic to physical stores and creating opportunities for repeat sales.

!!! tip "Use Cases"
    - **Boost store visits**: Attract customers to pick up orders in store and give store staff more chances to recommend add-on products.
    - **Reduce logistics costs**: Deliver parcels to stores in bulk to cut individual home-delivery shipping expenses.
    - **Speed up pickup**: Receive stock at stores and verify pickups by scanning codes to shorten customer wait times.

## Operating Structure

The store pickup feature spans **Payment and logistics settings**, **Order fulfillment**, **Commission rewards**, and **POS front-end operations**. This navigation page groups the features spread across different paths by "operation journey" to help you quickly complete setup and daily operations.

## Quick Navigation

<div class="grid cards" markdown>

- :lucide-settings-2:{ .lg } __1. Foundation and Activation__

    ---

    Before you start offering this service, first create your stores and configure pickup rules.

    [__Create and Manage Stores__](../create-stores.md)<br>
    [__Enable Store Pickup Service__](enable-store-pickup-service)

- :lucide-truck:{ .lg } __2. Fulfillment Operations (Back Office)__

    ---

    Manage store pickup orders received on the online store and deliver parcels to the designated store.

    [__Store Pickup Order Fulfillment Workflow__](../../orders/store-pickup-orders.md)

- :lucide-package-check:{ .lg } __3. In-Store Operations (POS)__

    ---

    Store staff handle in-store receiving of parcels, customer pickup verification, and overdue order handling.

    [__Store Parcel Receiving and Customer Pickup__](../../../pos/orders/store-pickup-orders-inbound-and-pickup.md)

- :lucide-hand-coins:{ .lg } __4. Management and Incentives (POS)__

    ---

    Use the commission mechanism to motivate store staff and track operational performance.

    [__Set Up POS Store Pickup Staff Commissions__](../../../pos/store/pos-store-pickup-staff-commission.md)

</div>

## Usage Notes

Before enabling the service, check the following restrictions based on your store type:

- **Payment restriction**: Only "pay first, pick up later" is supported. The system automatically filters the payment options on the checkout page.
- **Store type**:
    - **General Store**: For online-only merchants. You must manually update the order status in the admin dashboard.
    - **POS store**: For merchants integrated with a POS system. Supports barcode-scan receiving and automatic shipment status updates.
- **Order restriction**: Store pickup orders support only "ship all items," and returns must follow the full-order return policy.

---

## Frequently Asked Questions

??? quote "Why doesn't the checkout page show the "Store Pickup" option?"
    Check the following: 1. Confirm that the "Store Pickup Settings" for the store is turned on. 2. Confirm that the product edit page has the corresponding logistics delivery permission turned on. 3. Confirm that at least one available payment method is selected.

??? quote "Does the order status change automatically after the customer picks up the order?"
    - **POS store**: After store staff perform "Customer pickup in store," the system automatically updates the delivery status to "Received."
    - **General Store**: Merchants must manually mark the order as closed in **Order Management**.