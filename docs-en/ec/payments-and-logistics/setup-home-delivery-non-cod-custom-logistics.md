---
title: "Set up Home Delivery Non-COD / Custom Logistics"
description: "Explains how to set up home delivery options, shipping fee thresholds, and temperature zone delivery, including the country-level master switch, amount- and weight-based shipping fees, and how multi-temperature zone shopping is handled."
created: 2026-06-04 10:02
last_modified: 2026-06-30 08:52
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules:
  - 金物流
  - 商品
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents: 
  - 設定自訂物流選項
  - 設定運費門檻
  - 配置溫層配送
  - 解決多溫層拆單問題
features: 
  - 自訂物流
  - 運費門檻
  - 多溫層配送
  - 配送國家設定
prerequisites: 
  - "需先完成金流串接設定"
related:
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/orders/home-delivery/pelican-shipping-v2/
  - ec/orders/home-delivery/sf-express-shipping-v2/
  - ec/orders/home-delivery/hct-shipping-v2/
  - ec/orders/home-delivery/custom-logistic-shipping/
  - ec/payments-and-logistics/home-delivery-cash-on-delivery/
tags: 
  - Logistics_Settings
  - Shipping_Fees
  - "temperature zone"
  - Shipping_Regions
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 自訂物流列表
  - 配送國家設定
paths:
  - 金物流 > 自訂物流
  - 金物流 > 宅配物流 > 自訂物流
  - 商品 > 所有商品 > [特定商品] > 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2746
  - https://www.cyberbiz.io/support/?p=10652
  - https://www.cyberbiz.io/support/?p=5983
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics/"
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---
# Set up Home Delivery Non-COD / Custom Logistics
Let merchants set up their own home delivery options and shipping fee rules with "Custom Logistics." You can set up tiered shipping fees based on order amount or weight, and support different temperature zone delivery needs such as ambient, chilled, and frozen.
{ .subtitle }

[:lucide-tag:{ title="Applicable plans" }](../../resources/conventions#適用方案) | All versions
{ .doc-badge }


## Usage Notes

**Custom Logistics** page lets merchants set up two options: "Home Delivery Non-COD Logistics" and "Custom Logistics." Both options use the same setup process. The main difference is how orders are shipped after they are placed.

The table below compares the features and how shipping labels are created for each option. Choose the logistics type that fits your business needs.

| Logistics Type | System-Integrated Carriers | Description | How to Print Shipping Labels |
| ------- | ---- | ---- | ------------- |
| Home Delivery Non-COD Logistics | Black Cat<br>Pelican Express<br>SF Express<br>Hsinchu Logistics | This logistics option is integrated with the system and can automatically update order status after shipment. | **Requires shipping with a system waybill**<br>[Ship with Black Cat](../orders/home-delivery/tcat-home-delivery-v2.md)<br>[Ship with Pelican Express](../orders/home-delivery/pelican-shipping-v2.md)<br>[Ship with SF Express](../orders/home-delivery/sf-express-shipping-v2.md)<br>[Ship with Hsinchu Logistics](../orders/home-delivery/hct-shipping-v2.md) |
| Custom Logistics | - | This option is not integrated with the system, so order status is not updated after shipment. | [Ship with Custom Logistics](../orders/home-delivery/custom-logistic-shipping.md) |

### Hsinchu Logistics Non-COD Site Survey Process

=== "With CYBERBIZ PAYMENTS"

    Set up by following the [Hsinchu Logistics COD Activation Request](home-delivery-cash-on-delivery/#2-新竹物流) process.

=== "Without CYBERBIZ PAYMENTS"

    1. Go to **Payment and Logistics > Custom Logistics**, then click **Create Custom Logistics**.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-新增自訂物流01.png)

    2. Click **Fill Out Application Form**.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-新增自訂物流02.png)

    3. Apply to enable the logistics option.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-申請新竹物流貨到不付款01.png)

    4. Fill out the application form and submit it.

        - CYBERBIZ customer service will notify Hsinchu Logistics to schedule an on-site survey. Once the survey is complete, activation takes place right away.
        - If you need to change any information after submitting, contact CYBERBIZ customer service.
        - After activation succeeds, you can enable the logistics option and start using it. CYBERBIZ also sends a notification email (about 7–10 business days).

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-金物流-宅配物流-申請新竹物流貨到不付款02.png)

    !!! tip "Next Step"
        After you enable the logistics option, follow [Step 2: Add Custom Logistics]() to create a custom logistics option. You can name it **HCT Prepaid** and set up the related rules.

## Step 1: Shipping Country Settings (Master Switch)

Before you create specific logistics options, turn on shipping permissions for the target regions.


1. Log in to the admin panel, then go to **Payment and Logistics > Delivery Settings > Custom Logistics**.
1. At the top of the page, find **Shipping Region Settings**.
2. Based on your business needs, turn on **On shore of Taiwan**, **Off shore of Taiwan**, or **Oversea Country**.

    > **Note**: If these are not turned on (for example, if Outlying Islands is not turned on), customers still cannot select the outlying island shipping option at checkout, even if you set up outlying island shipping below.

![](https://www.cyberbiz.io/support/wp-content/uploads/物流運費設定01.png){ .screenshot }



## Step 2: Add Custom Logistics

Click **Create Custom Logistics** to open the setup page.

### 1. Basic Settings

- **Shipping Rule Name**: Custom name (for example, Black Cat-Ambient). Each name must be unique.
- **Shipping Regions**: Supports up to the City level.
- **Payment Methods**: Select the payment options this logistics option supports.

### 2. Shipping Fee Threshold Settings

The system supports two fee calculation methods: "Order Amount" and "Order Weight."

| Setting Type | Description | Recommendations |
| :--- | :--- | :--- |
| **Order Amount Shipping Fee** | Set shipping fees by order total range | Set the starting amount to NT$`0` to keep low-value orders from being unable to check out |
| **Order Weight Shipping Fee** | Set shipping fees by total order weight (including gifts) | Enter product weights in the product details first |

!!! tip "Best-Option Display Rule"
    If you set both amount-based and weight-based shipping fees, the system automatically selects the option that is most favorable to the customer (lower fee). We recommend setting up only one method to simplify management.

![](https://www.cyberbiz.io/support/wp-content/uploads/物流運費設定03.png){ .screenshot }

## Step 3: Temperature Zone Shipping Setup

Each custom logistics option can only set **one temperature zone**. If you have multiple temperature zone shipping needs, create a separate option for each.

1. **Create multiple logistics options**:
    - For example: create "Custom Home Delivery-Ambient" and "Custom Home Delivery-Frozen."
2. **Set product temperature zone**:
    - Go to **Products > All Products > [Specific Product] > 設定**.
    - In the "temperature zone and Logistics Shipping Settings" section, select the temperature zone that apply to the product.

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/物流運費設定08.png){ .screenshot }


## Handling Logic for Multi-Temperature Zone Shopping

When a customer's cart contains products from different temperature zone, the system tries to find a "common temperature zone" to avoid splitting the cart.

- **Scenario A (can be combined)**:
    - Product 1: supports "ambient, chilled."
    - Product 2: supports "chilled."
    - **Result**: The system ships as "chilled," and both products are placed in the same cart.
- **Scenario B (must be split)**:
    - Product 1: supports "ambient" only.
    - Product 2: supports "frozen" only.
    - **Result**: The system splits the cart into two carts and calculates shipping fees for each one separately.


## Frequently Asked Questions

??? quote "Why does checkout show free shipping even though I set a shipping fee?"
    Check whether "Weight-Based Shipping Fee" is turned on but product weights are not set (default is 0), or whether the shipping fee ranges are set up incorrectly.

??? quote "Why can't I select Custom Logistics after I add a payment method (such as JKOPay)?"
    After you add a payment method, you must return to **Custom Logistics > 編輯 > Payment Methods**, select the new item, and save.

??? quote "Can I set Custom Logistics to not deliver to specific regions?"
    Yes. In "Shipping Regions," select only the cities you want to deliver to. Customers who enter an address in an unselected region cannot select this logistics option.

