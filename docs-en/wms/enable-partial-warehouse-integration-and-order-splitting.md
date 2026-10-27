---
title: "Enable Partial Warehouse Integration and Order Splitting"
description: "Partial warehouse integration is for merchants who store some products at a CYBERBIZ partner warehouse (such as Honeycomb or Changjie) and ship the rest themselves. In order splitting mode, if a customer buys both kinds of products, the system splits the cart into separate orders that are checked out independently."
created: 2026-03-12 00:00
last_modified: 2026-07-13 11:45
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：建立自訂物流、部分出貨
  - 相關操作：批次匯入編輯商品、訂單篩選器、商品篩選器、編輯訂單列表欄位
  - 確認：自訂出貨訂單不適用貨到付款
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
modules:
  - 訂單
  - 商品
  - 金物流
sites:
  - TW
audiences: []
difficulty: ""
tnb: branch
plans:
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定出貨方式運費
  - 更改商品出貨來源
  - 處理拆單後訂單
features:
  - 部分串倉
  - 拆單模式
  - 庫存同步
  - 多出貨來源管理
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 需聯繫開店顧問或客服開通「部分串倉」功能
related:
  - wms/enable-partial-warehouse-integration-and-mixed-orders/
  - ec/products/bulk-operations/set-product-shipping-method/
  - ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics/
  - ec/orders/cvs-shipping/cvs-partial-shipment/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/orders/basics/order-management-interface/
  - wms/returns-and-vehicle-dispatch/
  - ec/orders/order-return-process/
  - wms/logistics-settings-reference/
tags: []
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 宅配物流列表頁
  - 商品編輯頁面
  - 訂單列表篩選器
  - 商品列表篩選器
paths:
  - 金物流 > 宅配物流
  - 商品 > 所有商品
  - 商品 > Excel 大量匯入商品
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5723
  - https://www.cyberbiz.io/support/?p=22981
permalink: "https://help.cyberbiz.io/wms/enable-partial-warehouse-integration-and-order-splitting/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Enable Partial Warehouse Integration and Order Splitting
Use this when some products are stored at the CYBERBIZ warehouse and you ship the rest yourself. If a customer buys both kinds of products, the system splits the cart into separate orders that are checked out independently.
{ .subtitle }


[:lucide-layers:{ title="Applicable Products" }](../resources/conventions.md) | Online Store / Smart Warehousing
{ .doc-badge }

![](../assets/images/EC-後台-金物流-宅配物流-拆單畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-partial-split }

- **Order splitting vs. mixed orders**
    - **Order splitting mode (this article)**: Warehouse products and self-shipped products are **checked out separately**. This creates several orders, each with its own shipping fee.
    - **Mixed order mode**: Warehouse products and self-shipped products are **checked out together**. This creates one order, and the shipping fee can be combined. For setup, see [Enable Partial Warehouse Integration and Mixed Orders](enable-partial-warehouse-integration-and-mixed-orders.md).
- **Order splitting limits**
    - **Logistics**: Self-shipped orders **do not support convenience store pickup** (the checkout page hides the store pickup option automatically).

## Setup { #operate-partial-split-setup }

### Step 1: Activation and System Setup { #operate-partial-split-init }

1. **Request the feature**: To use this feature, ask your store consultant or customer service to turn it on.
2. **Automatic changes**: When the feature is turned on, the system makes these changes:
    - All existing shipping fee settings change to **warehouse integration (warehouse shipping)**.
    - The default shipping method of all products changes to **warehouse shipping**.
3. **Follow-up**: You must manually change products that are **not stored in the warehouse** to **self-shipping** to separate them.


### Step 2: Set up Logistics Options { #operate-partial-split-logistics }

Set up the available logistics options separately for **warehouse shipping** and **self-shipping**.

Go to **Payment and Logistics > Delivery Settings** and open the **Custom Logistics** tab.

#### 1. Create Warehouse Shipping Logistics { #operate-partial-split-warehouse }

1. **Add a logistics option**: Click **Create Custom Logistics**.
2. **Set the display name**: Enter a name in the **Shipping Rule Name** field.

    > This name appears on the customer's checkout page. Use a clear name, such as Warehouse Delivery.

3. **Choose the shipping type**: In the **Shipping Method** drop-down list, select **Honeycomb Logistics**.
4. **Finish the details**: Fill in the shipping fee rules and delivery regions. For details, see [Create Custom Logistics](../ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md).

#### 2. Create Self-Shipping Logistics { #operate-partial-split-self }

=== "Cash on Delivery"

    1. Go to the **Connect Logistics** tab and click a logistics option.
    2. Enter the shipping fee and free shipping threshold.

    ![](../assets/images/EC-後台-金物流-宅配物流-部分串倉商家建立自行出貨貨到付款01.en.png){ .screenshot }

=== "No Payment on Delivery"

    1. **Add a logistics option**: Click **Create Custom Logistics**.
    2. **Set the display name**: Enter a name in the **Shipping Rule Name** field.

        > This name appears on the customer's checkout page. Use a clear name, such as Merchant Delivery.

    3. **Choose the shipping type**: In the **Shipping Method** drop-down list, select **Self-Shipment**.
    4. **Finish the details**: Fill in the shipping fee rules and delivery regions. For details, see [Create Custom Logistics](../ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md).

    ![](../assets/images/EC-後台-金物流-宅配物流-新增自訂物流01.en.png){ .screenshot }


### Step 3: Assign Product Shipping Sources { #operate-partial-split-products }

After partial integration is turned on, all products default to **warehouse shipping**. Change products that are not stored in the warehouse to **self-shipping**.

1. Sort your product list into warehouse products and non-warehouse products.
2. Update each product's shipping method as described in [Set Product Shipping Methods](../ec/products/bulk-operations/set-product-shipping-method.md).
3. Choose the matching warehouse shipping method for warehouse products, and **self-shipping** for the others.



## Shipping and Order Management { #operate-partial-split-orders }

=== "Customer Checkout"

    When the cart contains both **warehouse-shipped** and **self-shipped** products:

    - **Forced split**: At checkout, the customer chooses a delivery method for each of the two orders.
    - **Shipping fee**: The free shipping threshold is calculated separately for each order.

=== "Merchant Order Handling"

    1. Go to **Orders > All Orders**.
    2. **Filter self-shipped orders**: Click **Add Filter** and choose **配送方式 > [自行出貨物流名稱]**.
    3. **Self-shipped orders**: Select the orders and click **更多操作 > 列印 XXX 託運單**.
        - Self-shipped orders support partial shipping.

             > See [Partial Shipping for Convenience Stores](../ec/orders/cvs-shipping/cvs-partial-shipment.md) and [Partial Shipping for Home Delivery](../ec/orders/home-delivery/partial-shipment-v2.md).

        - Self-shipped orders do not support cash on delivery.
    4. **Warehouse-shipped orders**: The system sends the orders to WMS automatically. You only need to watch for shipping status updates.


### See Who Ships an Order { #operate-partial-split-source }

In the **Shipping Method** column of the order list, you can quickly see who is responsible for shipping each order:

- **Self-shipping**: You pack and ship all products yourself.
- **CYBERBIZ e-commerce warehouse**: The CYBERBIZ warehouse receives and ships all products automatically.

!!! info "Can't Find the **Shipping Method** Column?"
    If the list does not show it, [edit the order list columns](../ec/orders/basics/order-management-interface.md#operate-order-ui-edit-columns) and select **Shipping Method**. You can drag it forward to see who handles each order at a glance.

![](../assets/images/EC-後台-訂單-所有訂單-混單出貨方式01.en.png){ .screenshot }


## Returns { #operate-partial-split-returns }

| Order Type | Return Logic | Handling | Return Process |
| :--- | :--- | :--- | :--- |
| **Warehouse-shipped orders** | Follow the WMS return process | Parcels go back to the **e-commerce warehouse address** by default | [Warehouse Returns and Vehicle Dispatch](returns-and-vehicle-dispatch.md) |
| **Self-shipped orders** | Follow the standard EC return process | You [arrange reverse logistics](../ec/orders/order-return-process/#operate-order-return-reverse) yourself, or the customer sends items back to **your designated address** | [Order Return Process](../ec/orders/order-return-process.md) |


## FAQ { #faq-partial-split }

??? quote "Does Stock for Self-Shipped Products Sync with the Warehouse?"
    No. Stock syncs automatically only for products whose shipping method is **warehouse shipping** and whose SKU matches the warehouse.

??? quote "How Do I Quickly Find Products I Ship Myself?"
    Go to **商品管理 > All Products**, click **Advanced Search**, and under the **Shipping Method** filter select the **[self-shipping logistics name]** you set up. The matching products are listed.

    ![](../assets/images/EC-後台-商品-所有商品-篩選倉庫出貨與自行出貨商品01.en.png){ .screenshot }

## More Tasks { #next-steps-partial-split }

<div class="grid cards" markdown>

- :lucide-file-spreadsheet:{ .lg }
  [__Logistics Settings by Integration Mode__](logistics-settings-reference.md)
  See where home delivery is set up in each warehouse integration mode.

</div>