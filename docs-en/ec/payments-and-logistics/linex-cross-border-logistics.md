---
title: "LINEX Cross-Border Logistics"
description: "LINEX offers flexible cross-border logistics, letting merchants choose between home pickup or self-delivery to the warehouse and generate customs waybills and related documents from the back office."
created: 2026-03-04 00:00
last_modified: 2026-08-10 11:20
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 自訂貨到付款說明
  - 需要填商品多國英文欄位嗎
  - DHL 新增自訂物流的時候有「出貨方式」、「運送溫層」欄位，LINEX有嗎
  - DHL 有商品綁定物流步驟，LINEX有嗎
  - 託運文件列點說明
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
  - 管理中心
  - 訂單
sites:
  - TW
  - US
  - JP
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
  - Pro
  - Business
plan_options: []
cyb_extensions: []
intents:
  - 設定_LINEX_運送模式
  - 建立_LINEX_託運單
  - 準備_POA_委任書
features:
  - LINEX 跨境物流
  - 到府取件預約
  - 自動報關文件
prerequisites:
  - 建議搭配多國功能以利商品資訊自動帶入
related: []
tags:
  - "cross-border logistics"
  - "international shipping"
  - "pickup appointment"
acoiv: integration
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 一般設定
  - 金物流 > LINEX 託運單
  - 金物流 > 宅配物流
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8214
  - https://www.cyberbiz.io/support/?p=38562
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/linex-cross-border-logistics/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# LINEX Cross-Border Logistics

LINEX offers flexible cross-border logistics solutions. Merchants can choose "Home Pickup" or "Self-Delivery to Warehouse" based on their needs, and the back office automatically generates the waybills and documents required for customs declaration.
{ .subtitle }

[:lucide-layers:{ title="Applicable Product" }](../../resources/conventions#適用產品) | EC Website
[:lucide-tag:{ title="Applicable Plan" }](../../resources/conventions#適用方案) | PLUS / Enterprise<br>
[:lucide-layers:{ title="Applicable Product" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (North America / Japan / Southeast Asia)
[:lucide-tag:{ title="Applicable Plan" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }

## Usage Notes { #prerequisites-linex }

- **Service Scope**: Only supports **shipments from Taiwan to overseas**.
- **Batch Restriction**: Because customs information must be verified one by one, **batch printing** of waybills is currently **not supported**.
- **Operation Tip**: We recommend using this feature together with the **Multi-Country** feature. This allows the system to automatically pull English product information into waybill details, improving efficiency. For assistance, contact CYBERBIZ customer service.
- **Printer Recommendation**: We recommend a laser printer for printing waybills to reduce delivery errors caused by information recognition issues.

## Prerequisite Setup { #operate-linex-setup }

### Step 1: Verify Company English Name { #operate-linex-verify-name }

1. Log in to the CYBERBIZ back office and go to **Website Management > General**.
2. Find the **English Company name registered at TITA** field.
3. Enter your company's official English name as registered with [Business Registration](https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do).
4. Once saved, this field is locked. The system automatically uses this name in customs documents.

![](../../assets/images/EC-後台-管理中心-一般設定-填寫國貿局進出口廠商英文名01.en.png){ .screenshot }

### Step 2: Set up Shipping Mode and Sender { #operate-linex-mode-sender }

1. Go to **Payment and Logistics > LINEX Shipping Label**.
2. **Select Mode**: Check **Pickup Appointment** or **Self Delivery**.
    - **Cannot be changed after saving**. Choose carefully.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定01.png){ .screenshot }

3. **Basic Information**: Enter the sender information you use most often.
    - Must be in **English**. It is filled in automatically when you create a waybill.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定02.png){ .screenshot }


### Step 3: Set up Logistics and Shipping Fees { #operate-linex-fee }

1. Go to **Payment and Logistics > Delivery Settings** and select the **Custom Logistics** tab.
2. Click **Create Custom Logistics**.
3. **Basic Settings**:
    - **Shipping Rule Name**: Name this logistics option. The name must not match any other custom logistics option.

        > Example: LINEX Logistics

    - **Shipping Regions**: Regions can be set down to the **County** level. Settings cannot be configured for specific **townships/districts**.
    - **Payment Method**: Select **Non-Custom Cash on Delivery**.

        > If you have another payment gateway integrated, you can select **Custom cash on delivery**.

4. **Shipping Fee Settings**: Set shipping fees based on **order amount** and **order weight**.

    - **Fee Priority**: If an order meets multiple shipping fee conditions, the system automatically applies the **most favorable condition (lowest amount)** to calculate the fee.
    - **Display Threshold**: The order amount must meet the configured starting threshold. If not, the system automatically hides this logistics option at checkout.
    - **No Amount Limit**: To allow use at any order amount, set the **starting amount** of any condition range to NT$0.

![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定03.png){ .screenshot }

## Detailed Shipping Mode Rules { #specs-linex-modes }

Merchants must comply with the following rules based on the mode selected when the service was activated:

=== "Pickup Appointment (LINEX picks up at your location)"

    - **Pickup Date**:
        - Appointments made before 13:30 on the same day are picked up that day. Others are picked up the next day.
        - Weekend pickups are not available. Appointments are limited to business days.
    - **Pickup Time**:
        - Same-day pickup: 12:00 – 16:00 time window.
        - Next-day pickup: 13:00–17:00 time window.
    - **Related Fees**:
        - **Empty Trip Fee**: If the driver arrives and there are no goods to ship, a **NT$100 per trip** fee applies.
        - **Document Processing Fee**: If the package exterior or documents do not meet requirements, a **NT$50 per carton** processing fee applies.
    - **Change Restriction**: Reply to the automated system email by **12:00 noon** on the appointment day to contact LINEX customer service to change. Late changes will be processed on the next business day.

=== "Self-Delivery (merchant ships to LINEX warehouse)"

    - **Delivery Address**: No. 49, Lane 18, Section 3, Changxing Road, Luzhu District, Taoyuan City 338.
    - **Contact Phone**: 02-77557177 #710.
    - **Cutoff Time**: Shipments must arrive by **16:00**. Late shipments will be processed on the next business day.
    - **Service Hours**: Monday to Friday 9:30–12:00 and 13:30–19:00.



## Order Shipping Operations { #operate-linex-ship }

### Step 1: Create Waybill { #operate-linex-create-waybill }

1. Go to **Orders > All Orders** and select the orders to ship.
2. Click **Actions > Create LINEX Shipping Label**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定04.png){ .screenshot }

3. **Verify Basic Information**: Confirm that all fields are filled in **English**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定05.png){ .screenshot }

### Step 2: Enter Customs Information and Taxes { #operate-linex-customs }

1. **Verify Product Details**:
    - **Required Field Check**: **Product Name**, **Quantity**, and **Weight** must be filled in, and values cannot be 0.

        > **Product Name**: Enter in **English**.

    - **Product Content Summary**: Briefly and clearly describe all products in the order, including product name, material, and use.
        - If the order contains multiple products, list the most valuable product first.
        - Correct example: pearl earrings, blouse, ceramic tray.
        - Vague example: gifts, tools.

2.  **Set Tax Collection Method**:
    - **Delivered Duty Unpaid (DDU)**: The consumer pays customs clearance taxes and handling fees.
    - **Delivered Duty Paid (DDP)**: The merchant pays customs clearance taxes and handling fees.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定06.png){ .screenshot }

3. **Select Customs Method**:
    - **Simple Declaration(Sample)**: Free on Board (FOB) value ≤ NT$50,000.
    - **Simple Declaration(Sale)**: FOB value ≤ NT$50,000, and zero-rate tax must be declared for exported goods.
    - **Formal Declaration**: FOB value > NT$50,000.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定08.png){ .screenshot }

    !!! info "Fields Required for Pickup Appointment Mode"
        If you select **Pickup Appointment** as the pickup mode, make sure to complete the following fields:

        - **Pickup Time**: Refer to the LINEX pickup policy and select a time within the delivery service window.
        - **Pickup note**: This field is **required**. Do not leave it blank.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定07.png){ .small-image }


### Step 3: Print Waybill Documents and POA { #operate-linex-print }

1. After confirming **Calculate shipping fee** is correct, click **Create shipping label**.
    - `Delivery Status`will automatically change to `Shipped`.
2. Unzip the waybill documents and print the details.
3. Attach the **LINEX_waybill** and **orders_printed_details** files to the package surface.
4. If the merchant has not signed a **long-term power of attorney** with LINEX, each shipment must include a completed [POA template](https://drive.google.com/file/d/1MwQ04jG3eDJUY33zORsszPYRXPvRTt6J/view).
    - Refer to LINEX for the latest template. For a blank form, contact LINEX customer service.

![](https://www.cyberbiz.io/support/wp-content/uploads/LINEX-物流開通設定09.png){ .screenshot }

## Frequently Asked Questions { #faq-linex }

??? quote "How do I track my package status?"
    Go to the [LINEX package tracking website](https://tracking.hub-ez.com/Tracking/Tracking) and enter the waybill number to search.


