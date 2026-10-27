---
title: "Warehouse Integration Application and Activation"
description: "Before the warehouse integration goes live, the merchant must sign the contract, set up the system environment, and sync product data so that orders are passed to the warehouse correctly."
created: 2026-03-18 00:00
last_modified: 2026-07-13 11:45
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：大量填補SKU教學、建立單一品項、建立加工商品
  - 確認：宅配物流，結帳頁是串接物流與自訂物流並存？串接物流與自訂物流皆須設置？
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
modules:
  - 電商倉儲
  - 商品
  - 金物流
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 填寫入倉表單
  - 同步商品 SKU
  - 開啟庫存管理
  - 設定物流運費
features:
  - 電商倉儲
  - WMS 串接
  - 庫存同步
  - B2C 大宗寄倉
prerequisites:
  - 需完成商品 SKU 編碼規劃（不可為空值）
related:
  - wms/single-items/
  - wms/merchant-inbound-operation-rules/
  - wms/logistics-settings-reference/
tags:
  - WMS
acoiv: activate
apis: []
devices:
  - desktop
ui_components:
  - 電商倉儲申請頁面
  - 商品編輯頁面
  - 金物流設定頁面
paths:
  - 商品 > 所有商品
  - 商品 > 單一品項
  - 金物流 > CYBERBIZ 電商倉儲設定
  - 金物流 > 超商物流
  - 金物流 > 宅配物流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5708
  - https://www.cyberbiz.io/support/?p=28967
permalink: "https://help.cyberbiz.io/wms/application-process-and-activation/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---
# Warehouse Integration Application and Activation
Before the warehouse integration goes live, the merchant must sign the contract, set up the system environment, and sync product data so that orders are passed to the warehouse correctly.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## Key Integration Rules { #prerequisites-wms-activation }

- **Unique SKUs**: After integration, every product (including each variant) must have a SKU.
- **Who does the work**: Once the integration is live, the CYBERBIZ e-commerce warehouse handles all shipping and returns.
- **Logistics center returns**: If a logistics center needs to return goods, the carrier returns them to the CYBERBIZ warehouse. You do not need to arrange a vehicle.
- **Check the data**: In the first week after activation, we recommend closely checking order transfer status to make sure SKUs sync correctly.

## Step 1: Apply and Sign the Contract { #operate-wms-activation-apply }

Before any system setup, finish the admin process and warehouse needs assessment.

1. **Fill in the warehouse form**: Go to the [CYBERBIZ e-commerce warehouse application page](https://www.cyberbiz.io/wms/#list) and describe your needs. A warehouse manager will contact you.
2. **Assessment and contract**: Confirm product types, inbound volume, and logistics rates with the warehouse manager, and sign the contract.
3. **Check your logistics mode**:
    - If you use the convenience store C2C mode, contact your consultant or customer service to switch to **B2C bulk warehouse shipping**.
    - Logistics center returns are sent back to the CYBERBIZ warehouse by **Ji Chuan Freight**.

## Step 2: Set up Your System { #operate-wms-activation-setup }

After signing the contract, complete these settings in the online store admin panel (EC) so the systems can connect.

### 1. Sync Product SKUs { #operate-wms-activation-sku }

- [Create items](single-items/#operate-single-items-add) in the e-commerce warehouse admin panel for the products going into the warehouse.
- Make sure product SKUs in the online store (EC) and the e-commerce warehouse (WMS) admin panels are **all filled in and exactly the same**.
- Every variant (such as color or size) must have its **own unique** SKU. Do not leave it blank.

=== "View EC Product SKUs"

    Log in to the online store admin panel, go to **Products > All Products**, click a product, and check the **SKU** field.

    ![](../assets/images/EC-後台-商品-所有商品-串倉商品檢查SKU與庫存開關01.en.png){ .screenshot }

=== "View WMS Item Numbers"

    Log in to the e-commerce warehouse admin panel, go to **Products > 單一品項**, click a product, and check the **Product Uid** field.

    ![](../assets/images/WMS-後台-商品-單一品項-查看品號01.en.png){ .screenshot }

### 2. Turn on Inventory Management { #operate-wms-activation-inventory }

- Go to **Products > All Products** and open each product's edit page.
- Turn on the **Inventory** option.

    > You do not need to enter stock quantities. After activation, the system pulls the physical stock from the warehouse automatically.

![](../assets/images/EC-後台-商品-所有商品-串倉商品檢查SKU與庫存開關01.en.png){ .screenshot }

### 3. Clear Pending Orders { #operate-wms-activation-orders }

- Before the integration goes live, **all existing orders** in the EC admin panel must be shipped.
- Update each order's **delivery status** to **Shipped** or **Received**.


## Step 3: Activation and Logistics Setup { #operate-wms-activation-open }

After you finish the setup, reply to CYBERBIZ customer service. A specialist activates the integration and **emails you when it is done**.

!!! info "What CYBERBIZ Sets Up"
    - Convenience store pickup label testing
    - Activating and configuring the integration fields in **Payment and Logistics > CYBREBIZ 電商倉儲設定**
    - Activating the e-commerce warehouse logistics types

After you receive the activation email, finish these settings:

### Fill in Basic Information { #operate-wms-activation-basic }

1. Go to **Payment and Logistics > CYBERBIZ 電商倉儲設定**.
2. In the **Return Settings** section, fill in the blank fields.
    - Company name
    - Product type

![](../assets/images/EC-後台-金物流-CYBERBIZ電商倉儲設定-填寫串倉基本資訊01.en.png){ .screenshot }


### Set Shipping Fees { #operate-wms-activation-freight }


#### Convenience Store Settings { #operate-wms-activation-cvs }

1. Go to **Payment and Logistics > Convenience Store Logistics**.
2. For each logistics option you turned on, set the **Shipping Fee** and the **free shipping threshold**.
3. Choose whether to offer **COD**.

![](../assets/images/EC-後台-金物流-超商物流-串倉商家建立超商物流01.en.png){ .screenshot }

#### Home Delivery Settings { #operate-wms-activation-home }

1. Go to **Payment and Logistics > Delivery Settings**.
2. On the **Custom Logistics** tab, create a custom logistics option.
    - **Shipping Rule Name**: The delivery option customers see at checkout (such as chilled home delivery).
    - **Delivery range**: Set the **Shipping Regions** and the matching **Temperature zone**.
    - **Logistics type**: Link the shipping logistics option.
    - **Payment and fees**: Choose the supported **Payment Methods** and set the matching **Shipping Fee** rules.

![](../assets/images/EC-後台-金物流-宅配物流-串倉商家建立宅配物流01.en.png){ .screenshot }

!!! tip "Flexible Shipping Fee Policies"
    To match different shipping fee thresholds or delivery limits, create several **custom logistics** options by **logistics type**, **Shipping Regions**, **Temperature zone**, and other conditions.

    - **Example**: Create both "Room-temperature home delivery (main island)" and "Room-temperature home delivery (outlying islands)" with different surcharge rules.



## More Tasks { #next-steps-wms-activation }

<div class="grid cards" markdown>

- :lucide-square-arrow-right:{ .lg }
  [__Inbound Rules__](merchant-inbound-operation-rules.md)
  After the integration is set up, start inbound operations to send products to the CYBERBIZ warehouse.

- :lucide-file-spreadsheet:{ .lg }
  [__Logistics Settings by Integration Mode__](logistics-settings-reference.md)
  See where home delivery is set up in each warehouse integration mode.

</div>

