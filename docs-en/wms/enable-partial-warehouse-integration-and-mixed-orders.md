---
title: "Enable Partial Warehouse Integration and Mixed Orders"
description: "Customers add warehouse products and non-warehouse products to the same cart and check out together in one order with Mixed Logistics."
created: 2026-03-12 00:00
last_modified: 2026-07-13 11:45
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：拆單建立自訂物流、建立退貨單、會員前台申請退貨、編輯訂單列表欄位
  - 確認：混合物流取交集或聯集
  - 確認：混合出貨有在訂單篩選器裡嗎
  - 用詞：串接宅配
  - 訂單列表編輯欄位
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
  - 設定混合物流
  - 配置共同付款方式
  - 處理混合訂單出貨
features:
  - 部分串倉
  - 混單模式
  - 混合物流設定
  - "Combined Checkout"
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 需聯繫開店顧問或客服開通「部分串倉」功能
related:
  - wms/enable-partial-warehouse-integration-and-order-splitting/
  - ec/products/bulk-operations/set-product-shipping-method/
  - ec/orders/cvs-shipping/cvs-partial-shipment/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/orders/basics/order-management-interface/
  - ec/orders/order-return-process/
  - wms/return-orders/
  - ec/orders/member-return-request-feature/
  - wms/logistics-settings-reference/
tags:
  - 合併結帳
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 混合物流設定頁面
  - 商品編輯頁面
  - 訂單列表篩選器
  - 商品列表篩選器
paths:
  - 金物流 > 宅配物流 > 混合物流
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5726
  - https://www.cyberbiz.io/support/?p=23149
permalink: "https://help.cyberbiz.io/wms/enable-partial-warehouse-integration-and-mixed-orders/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Enable Partial Warehouse Integration and Mixed Orders
Customers add warehouse products and non-warehouse products to the same cart and check out together in one order with Mixed Logistics.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../resources/conventions.md) | Online Store / Smart Warehousing
{ .doc-badge }

![](../assets/images/EC-後台-金物流-宅配物流-混單畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-partial-mixed }

- **Order splitting vs. mixed orders**
    - **Order splitting mode**: Warehouse products and self-shipped products are **checked out separately**. This creates several orders, each with its own shipping fee. For setup, see [Enable Partial Warehouse Integration and Order Splitting](enable-partial-warehouse-integration-and-order-splitting.md).
    - **Mixed order mode (this article)**: Warehouse products and self-shipped products are **checked out together**. This creates one order, and the shipping fee can be combined.
- **Mixed order limits**
    - **Logistics**: Mixed orders **do not support convenience store pickup** (the checkout page hides the store pickup option automatically).
    - **Payments**: Mixed orders **do not support cash on delivery through integrated home delivery**.

## Setup { #operate-partial-mixed-setup }

### Step 1: Activation and System Setup { #operate-partial-mixed-init }

1. **Request the feature**: To use this feature, ask your store consultant or customer service to turn it on.
2. **Automatic changes**: When the feature is turned on, the system makes these changes:
    - All existing shipping fee settings change to **warehouse integration (warehouse shipping)**.
    - The default shipping method of all products changes to **warehouse shipping**.
3. **Prepare custom logistics**: Go to **Payment and Logistics > Delivery Settings > 自訂物流** and finish the [shipping option settings](enable-partial-warehouse-integration-and-order-splitting/#operate-partial-split-logistics).
4. [Set product shipping methods](../ec/products/bulk-operations/set-product-shipping-method.md): Link self-shipped products to a **self-shipping** logistics option, and keep warehouse products on their warehouse shipping methods.


### Step 2: Set up Mixed Logistics { #operate-partial-mixed-logistics }

Mixed logistics defines the rules for **orders that contain both warehouse and self-shipped products**.

1. Go to **Payment and Logistics > Delivery Settings > 混合物流**.
2. Click **Create Mixed Shipping Rule**.
3. **Key settings**:
    - **Shipping Rule Name**: This name appears on the customer's checkout page. Use a clear name, such as Warehouse Delivery.
    - **Choose custom logistics**: Select the logistics options to use with mixed orders.
4. **Automatic matching**:
    - The system compares the **custom logistics** and **warehouse shipping** settings and uses what they have **in common** to decide which **Shipping Regions**, **shipping methods**, **Shipping Types**, and **payment methods** the mixed logistics option supports.
    - If they have nothing in common (for example, no overlapping regions or payment methods), you cannot save.
    - **temperature zone**: The system uses the **combination** of both (for example, if one is room temperature and the other is frozen, mixed orders support products in either temperature zone).
5. **Order shipping fees**: Set fees by **Amount** or **Weight**.

!!! tip "Best Practice: Create a Catch-All Logistics Combo"
    If the cart does not match any **Mixed Logistics** you set up, checkout falls back to **order splitting mode**. To let all products in your store check out as mixed orders, we recommend creating one mixed logistics option that **covers all custom logistics options**.


![](../assets/images/EC-後台-金物流-宅配物流-新增混合物流01.en.png){ .screenshot }


## Shipping and Order Management { #operate-partial-mixed-orders }

=== "Customer Checkout"

    When the cart contains both **warehouse-shipped** and **self-shipped** products:

    - **One checkout**: The customer places the order on a single checkout page.
    - **Shipping fee**: The free shipping threshold is calculated on the order total.

=== "Merchant Order Handling"

    1. Go to **Orders > All Orders**.
    2. **Filter self-shipped orders**: Click **Add Filter** and choose **配送方式 > [混合物流名稱]**.
    3. **Self-shipped orders**: Select the orders and click **更多操作 > 列印 XXX 託運單**.

        - Self-shipped orders support partial shipping.

            > See [Partial Shipping for Convenience Stores](../ec/orders/cvs-shipping/cvs-partial-shipment.md) and [Partial Shipping for Home Delivery](../ec/orders/home-delivery/partial-shipment-v2.md).

        - Self-shipped orders do not support cash on delivery.

    4. **Warehouse-shipped orders**: The system sends the orders to WMS automatically. You only need to watch for shipping status updates.

### See Who Ships an Order { #operate-partial-mixed-source }

In the **Shipping Method** column of the order list, you can quickly see who is responsible for shipping each order:

- **Mixed order (self-shipping + [warehouse name])**: The order contains both **merchant-shipped products** and **warehouse-shipped products**, and each side ships its part.
- **Self-shipping**: You pack and ship all products yourself.
- **CYBERBIZ e-commerce warehouse**: The CYBERBIZ warehouse receives and ships all products automatically.

!!! info "Can't Find the **Shipping Method** Column?"
    If the list does not show it, [edit the order list columns](../ec/orders/basics/order-management-interface.md#operate-order-ui-edit-columns) and select **Shipping Method**. You can drag it forward to see who handles each order at a glance.

![](../assets/images/EC-後台-訂單-所有訂單-混單出貨方式01.en.png){ .screenshot }

### Delivery Status of Mixed Orders { #specs-partial-mixed-status }

Because a mixed order has two shippers, its delivery status updates based on **how far each side has progressed**:

| Delivery Status | Trigger | Description |
| ------- | -------- | --- |
| **Partially Shipped** | Either side has shipped | The order moves to this status when either you or the warehouse has shipped |
| **Shipped** | Both sides have shipped | Both shipments were handed to carriers and left the shippers |
| **Received** | Both shipments are updated to received | Both shipments were delivered to the customer |


## Returns { #operate-partial-mixed-returns }

### Return Rules { #specs-partial-mixed-return-rules }

- **How to return**: Follow the EC [order return process](../ec/orders/order-return-process.md).
- **One return address**: Return parcels for mixed orders, whether warehouse or self-shipped products, go to **your designated address** by default.
- **Sending warehouse products back**: To send warehouse products you received back to the WMS warehouse, [create a return order (reverse logistics)](return-orders.md#operate-return-orders-manual) manually in the WMS admin panel.

### When Returns Are Allowed { #prerequisites-partial-mixed-return-limits }

| Order Status | Return Allowed | Description |
| :--- | :--- | :--- |
| **Partially Shipped** | **No** | Mixed order returns all go back to the merchant. To avoid errors in refund amounts and shipping status from partial shipments, returns are blocked in this status |
| **Shipped** | **商家可<br>顧客否** | Only the merchant can start a return. Customers cannot request one on the storefront yet |
| **Received** | **Both** | Both the merchant and the customer can start a return |


## FAQ { #faq-partial-mixed }

??? quote "Can I Change the Custom Logistics in a Mixed Logistics Option After Creating It?"
    No. If you change the custom logistics, it may no longer overlap with the warehouse settings, and the mixed logistics option stops working. First **unlink the custom logistics** from the mixed logistics option, adjust the custom logistics, and then link it again.

??? quote "Why Did Checkout Suddenly Split the Cart?"
    The current product combination (warehouse shipping vs. self-shipping) does not match any **Mixed Logistics** option (for example, the payment methods do not match), so the system falls back to **order splitting mode**.


## More Tasks { #next-steps-partial-mixed }

<div class="grid cards" markdown>

- :lucide-hand-helping:{ .lg }
  [__Let Members Request Returns on the Storefront__](../ec/orders/member-return-request-feature.md)
  If customers can request returns, turn on storefront return requests as well.

- :lucide-file-spreadsheet:{ .lg }
  [__Logistics Settings by Integration Mode__](logistics-settings-reference.md)
  See where home delivery is set up in each warehouse integration mode.

</div>
