---
title: "Amazon FBA Cross-Border Logistics"
description: "Use Amazon FBA to have Amazon pack and ship your website orders, with automatic order, shipping status, and inventory sync."
created: 2026-03-03 00:00
last_modified: 2026-06-30 08:52
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：網站外觀、商品大量填補SKU教學
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
  - 第三方整合
  - 商品
sites:
  - US
  - JP
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - Pro
  - Business
plan_options: []
cyb_extensions: []
intents:
  - 安裝_FBA_插件
  - 授權_Amazon_帳號
  - 綁定商品_SKU
features:
  - Amazon FBA
prerequisites:
  - 需具備 Amazon Seller Central 賣家帳號
  - 商品需已入 Amazon FBA 倉庫
related:
  - ec/products/bulk-operations/set-product-shipping-method/
tags:
  - "Cross-Border Logistics"
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - APP MARKET > 擴充服務市集
  - APP MARKET > 我的擴充服務
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=20676
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/amazon-fba-cross-border-logistics/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# Amazon FBA Cross-Border Logistics

With the Amazon FBA service, you can have Amazon's logistics team pack and ship your website orders on your behalf. The system automatically sends orders to Amazon, syncs shipping status, and updates inventory, automating your cross-border operations.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (North America / Japan)
[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }



## Usage Notes { #prerequisites-amazon-fba }

- **Automatic shipping**: After a website order is placed, the system automatically sends the order data to Amazon for fulfillment.
- **Inventory sync**: Once linked, website inventory is locked and cannot be edited manually. Amazon FBA actual inventory is always the source of truth.

## Enable Logistics { #operate-amazon-fba }

### Step 1: Install the FBA Extension App { #operate-amazon-fba-install }


1. Log in to the CYBERBIZ back office and go to **APP MARKET > App Market**.
2. Find **CYBERBIZ CHANNEL BRIDGE** and click **Install App**. [Quick link :lucide-external-link:](https://appmarket.cyberbiz.io/application/eb67e6a5-d38f-4a86-a1a4-8d5727dae0db)

    ![](../../assets/images/EC-後台-APPMARKET-全通路庫存管理-安裝Amazon通路01.en.png)



### Step 2: Complete Account Authorization { #operate-amazon-fba-authorize }

1. Log in to the CYBERBIZ back office and go to **APP MARKET > My Apps**.

    ![](../../assets/images/EC-後台-APPMARKET-全通路庫存管理-安裝Amazon通路02.en.png)

2. Find **CYBERBIZ CHANNEL BRIDGE** and click **Settings**.
3. In the **Amazon** channel, click **Go to Authorization**, and the system redirects to the Amazon authorization page.

    ![](../../assets/images/EC-後台-APPMARKET-全通路庫存管理-安裝Amazon通路03.en.png)

4. Enter your Amazon Seller Central account and password to complete the link.
    - We recommend using an admin account (Admin User) to ensure full permissions.

5. After linking is complete, the system automatically redirects to the Amazon settings page. Check the connection details:

    - **Check Status**: In the **Store Settings** tab, view the current **Store Status** and **Expiration Date**.
    - **Expiration Reminders**: The system sends email notifications 15, 7, 3, and 1 days before the authorization expires.
    - **Reauthorization**: If authorization expires, click **Reauthorize** to restore functionality.

### Step 3: Link Product SKUs { #operate-amazon-fba-bind-sku }

For Amazon to correctly match website orders to products, **the CYBERBIZ product SKU must exactly match the Amazon product SKU**.

#### 1. Look up the Amazon SKU { #operate-amazon-fba-query-sku }

1. Log in to [Amazon Seller Central](https://sellercentral.amazon.com/).
    ![](../../assets/images/Amazon-後台-查看訂單資訊01.en.png)
2. Go to **Inventory > Manage FBA Inventory**.
    ![](../../assets/images/Amazon-後台-查看Amazon商品SKU01.en.png)
3. Record the **Seller SKU** for the product.
    ![](../../assets/images/Amazon-後台-查看Amazon商品SKU02.en.png)

#### 2. Map the SKU in CYBERBIZ { #operate-amazon-fba-map-sku }

1. Go to **Products > All Products**, and open the edit page for the target product.
2. Scroll down to the **Manage Variants** section.
3. In the **SKU** field, enter the exact same characters as on Amazon, including case and symbols.
4. Click Save.

![](../../assets/images/EC-後台-商品-所有商品-編輯商品SKU01.en.png)

### Step 4: Set up the Amazon Shipping Method { #operate-amazon-fba-ship-method }

For products shipped by **Amazon FBA**, specify the shipping method:

1. Follow [Set Up Product Shipping Methods](../products/bulk-operations/set-product-shipping-method.md) to configure the product's shipping method.
2. For **Shipping Method**, select **Amazon FBA**, then complete the setup and save.
3. Return to the product edit page and confirm that the **SKU** and **Shipping Method** are displayed correctly.

![](../../assets/images/EC-後台-商品-所有商品-指定出貨方式Amazon物流01.en.png)

!!! warning "Amazon SKU and Shipping Method Restrictions"
    Only stores with the corresponding Amazon feature enabled can see **Amazon FBA** in the shipping method menu. If the SKU does not match the Amazon Seller SKU, the system cannot correctly send orders or sync inventory.

## Order Monitoring and Shipping Status Tracking { #operate-amazon-fba-tracking }

### 1. View Website Orders in Amazon { #operate-amazon-fba-view-orders }

FBA orders created on the website also appear in the Amazon back office:

1. Log in to [Amazon Seller Central](https://sellercentral.amazon.com/).
    ![](../../assets/images/Amazon-後台-查看訂單資訊01.en.png)
2. Go to **Orders > Manage Orders**.
    ![](../../assets/images/Amazon-後台-查看訂單資訊02.en.png)
3. In the Sales Channel filter, select **Non-Amazon** to view orders from the website.
    ![](../../assets/images/Amazon-後台-查看訂單資訊03.en.png)

### 2. Shipping Status Sync { #specs-amazon-fba-sync }

- When the Amazon warehouse prepares to ship, the website order status updates automatically.
- When FBA completes delivery, the website delivery status automatically changes to **Shipped** and the order is officially recorded.



## CYBERBIZ and Amazon FBA Status Mapping { #specs-amazon-fba-status }

| Amazon FBA Status | CYBERBIZ Delivery Status | Notes |
| :--- | :--- | :--- |
| Receiving → Processing | Not shipped | Consumers and merchants can cancel the order |
| Processing | Preparing to ship | Order sent, waiting for Amazon to process <br>Orders cannot be canceled once in this status |
| COmplete | Shipped | Amazon has shipped the order, and the system automatically credits the payment |
| Cancelled | Canceled | Order canceled on the Amazon side |

