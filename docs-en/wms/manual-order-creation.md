---
title: "Create Orders Manually"
description: "Send shipping instructions straight to the warehouse when you need to ship orders from a non-integrated channel or move products from the warehouse back to your company."
created: 2026-03-12 00:00
last_modified: 2026-08-13 17:10
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：建立通路
  - 確認：出貨日與配達日
  - 確認：效期/批號管理是否有材料對應文件
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
  - 建立非串接通路訂單
  - 設定預約出貨日期
  - 配置物流配送資訊
features:
  - "Manual Order Creation"
  - 通路管理
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 商品已入庫並有可用庫存
related:
  - wms/channels/
tags:
  - 手動建單
  - "Warehouse Shipping"
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 手動建單頁面
paths:
  - 訂單 > 手動建單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5744
  - https://www.cyberbiz.io/support/?p=9105
permalink: "https://help.cyberbiz.io/wms/manual-order-creation/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Create Orders Manually
Send shipping instructions straight to the warehouse when you need to ship orders from a non-integrated channel or move products from the warehouse back to your company.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-訂單-手動建單-畫面總覽01.en.png){ .hero-page }


## Use Cases { #intro-manual-order }

- **Multi-channel shipping**: Ship orders from channels not integrated with CYBERBIZ (such as Shopee or momo).
- **Warehouse returns to you**: Move stock from the warehouse back to your business for business changes or trade shows.
- **Urgent shipping**: In special cases, skip the system's automatic order pickup and create a shipping task manually.


## Steps { #operate-manual-order }

### Step 1: Enter Basic Order Information { #operate-manual-order-basic }

Go to **Orders > 手動建單** and enter the order's source and schedule.

1. **Basic data**: Enter the **order number** and **recipient information**.
2. **Choose a channel**: Select the order's sales channel. If you have not added it yet, [create the channel](channels.md) first.
3. **Scheduled Shipping Date**:
    - This is the **date the warehouse plans to ship**, not the delivery date. Allow time for delivery.
    - To schedule shipping for a future date, choose **the day before** the **expected delivery date**.
4. **Notes**:
    - **Note**: This text is printed on the waybill and **is visible to the customer and the courier**. Use it for special delivery requests.


### Step 2: Set Delivery Information { #operate-manual-order-delivery }

Fill in the recipient details for the shipping method the customer chose.

#### 1. Home Delivery { #operate-manual-order-home }

- **Supported carriers**: T-Cat, Pelican, SF Express (overseas), and Hsinchu Transport, or choose **Any**.
- **Required fields**: Country/region, **City**, **District**, full address, and order total.
- **Optional fields**:
    - **Delivery time slot**: Choose "Before noon" or "12:00–17:00".
    - **Round-trip delivery**: Select this if items need to be collected (for example, for an exchange).
    - **COD**: After you select it, enter the amount to collect.

#### 2. Convenience Store Pickup { #operate-manual-order-cvs }

- **Supported stores**: 7-ELEVEN, FamilyMart, and Hi-Life.
- **Required fields**: **Convenient Store Id** and order total.
- **COD**: Choose whether the store collects payment.

#### 3. Warehouse Pickup { #operate-manual-order-pickup }

- **Address**: Enter the **warehouse address** in the address field.
- **Note**: In the **Shipping Note** field, be sure to enter **Self Pickup**.
- **Optional fields**: Enter the order total if needed.

!!! tip "How Can I Keep an Order Editable?"
    If you expect changes after you create the order, select **Pending** when you create it. The order then stays **Pending** until you confirm the details and start shipping manually.

### Step 3: Choose Products to Ship { #operate-manual-order-products }

1. Click **Add Item** to open the product selection window.
2. Search for products: Enter the **Product Uid** or **product name** as a keyword.
3. **Check the details**:
    - Select the **goods status** (such as normal or defective).
    - Select the **Product Exp.** or **Batch Code** (if expiry or batch management is turned on for the product).

        > When you select an **expiry date**, you can **choose an allocation method**. See [Expiry-Based Allocation Methods](#specs-manual-order-expiry).

    - Enter the quantity to ship.
4. Click **Add** to add the product to the shipping list.

### Step 4: Finish the Order { #operate-manual-order-complete }

1. **Shipping Note**: Only WMS staff can see this. **Customers cannot see it.**
2. **Upload Attachment**: Upload any shipping slips, purchase orders, or custom documents that need to go with the order.
3. **Submit**: Check the delivery information and product details, and then click **Submit** at the bottom.

## Expiry-Based Allocation Methods { #specs-manual-order-expiry }

When you create an order for a product with expiry management, choose an allocation method under **product expiry** to decide which batch the system ships from.

=== "Shortest Expiry"

    - **How the system allocates**: Starting from the date you set, it ships from the nearest expiry date to the latest. It can combine several batches to fill the quantity.
    - **What your date means**: The earliest expiry date you accept (inclusive). Any batch expiring on or after this date can be used.
    - **When stock is short**: Other qualifying batches fill the gap automatically, so the same product in one order may have different expiry dates.

=== "Shortest Single Expiry"

    - **How the system allocates**: Starting from the date you set, it finds one expiry batch with enough stock and ships it all from that batch.
    - **What your date means**: The earliest expiry date you accept (inclusive).
    - **When stock is short**: It moves to the next expiry batch with enough stock. Once allocated, it does not switch back even if the original batch is restocked later.


=== "Specific Expiry"

    - **How the system allocates**: It ships only from the expiry date you specify and never uses another date.
    - **What your date means**: A locked expiry date (must match exactly).
    - **When stock is short**: The order stays out of stock and keeps the quantity already allocated. The rest is filled automatically after that expiry batch is restocked.



## FAQ { #faq-manual-order }

??? quote "What Is the Difference Between **Note** and **Shipping Note**?"
    The main difference is **who can see the information**:

    - **Note**: Public. Customers can see it on the order page, and it is printed on the shipping label for the **courier**.
    - **Shipping Note**: Internal. Only the admin panel and **WMS staff** can see it. Customers and couriers cannot. Use it for internal instructions.


??? quote "Can I Change an Order After It Is Created?"
    It depends on the current **Order Status**:

    - **Pending**: You can change the products or recipient information, or cancel the order.
    - **Processing**: The warehouse has started picking or packing. To avoid shipping errors, the system **blocks direct changes**.
