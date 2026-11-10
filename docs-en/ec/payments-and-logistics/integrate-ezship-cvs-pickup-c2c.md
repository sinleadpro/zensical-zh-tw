---
title: "Integrate ezShip CVS Pickup (C2C)"
description: "Connect ezShip to turn on pickup at FamilyMart, Hi-Life, and OK Mart in one step, giving customers more delivery options."
created: 2026-02-03 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
  - 管理中心
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - Professional
  - Advanced
  - Expert
plan_options: []
cyb_extensions: []
intents:
  - 申請 ezShip 會員
  - 綁定 ezShip 帳號
  - 設定超商取貨運費
  - 申請超商貨到付款功能
features:
  - ezShip 台灣便利配
  - 超商取貨
  - C2C 寄件
prerequisites:
  - "申請 ezShip 帳號"
  - "確保會員註冊欄位已將「電子郵件」設為必填"
related: []
tags: []
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 顧客註冊設定 > 顧客註冊欄位設定
  - 金物流 > 超商物流 > ezShip 台灣便利配
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2524
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/integrate-ezship-cvs-pickup-c2c/"
comments: false
search:
  exclude: false
icon: lucide/store
hide: []
---
# Integrate ezShip CVS Pickup (C2C)

Through ezShip, merchants can turn on pickup at FamilyMart, Hi-Life, and OK Mart in one step, giving customers more delivery choices.
{ .subtitle }

[:lucide-tag:{ title="Applicable plans" }](../../resources/conventions#適用方案) | Professional / Advanced / Expert
{ .doc-badge }

![](../../assets/images/EC-後台-金物流-超商物流-EZSHIP超取01.en.png){ .hero-page }

!!! info "Plan Applicability"
    ECPay integration is available only to **Professional, Advanced, and Expert** merchants, and only to users who have **not enabled CYBERBIZ PAYMENTS**. If you already use CYBERBIZ PAYMENTS, its system includes full convenience store logistics, so you do not need to integrate ezShip separately.



!!! tip "Use Cases"
    - **Multi-channel convenience store coverage**: In addition to 7-11, add pickup at FamilyMart, Hi-Life, and OK Mart in one go.
    - **Small-scale start**: Suited to merchants with low shipment volume and no immediate bulk shipping (B2C) needs who use the store-to-store (C2C) model.
    - **Flexible payment options**: With an ezShip business membership, offer convenience store cash on delivery to encourage customers to place orders.


## Usage Notes { #prerequisites-ezship-c2c }

Before you enable the ezShip service, make sure you understand the following system logic and operating limits:

- **Shipping label printing**: For orders created with ezShip, you **must go to the ezShip backend** to generate shipping labels and ship. The CYBERBIZ backend does not provide printing.
- **Shipping fee limit**: The **Cash on Delivery** and **Non-custom cash on delivery** shipping fees in ezShip **cannot be set separately**.
- **Cash-on-delivery limits**:
    - You must apply for an ezShip **business membership** and sign a contract. An annual fee also applies.
    - The COD handling fee is **0.8%** of the collected amount, with amounts below NT$3 calculated as NT$3. (The fee may vary depending on the application plan.) It is deducted when collected funds are remitted.
    - The per-order COD cap is **NT$10,000**.
- **Feature support**: Only the store-to-store (C2C) model is supported for now. ezShip B2C bulk shipping is not yet supported.


## Setup Steps { #operate-ezship-c2c }

### Step 1: Adjust Member Sign-up Fields { #operate-ezship-c2c-register-fields }

The ezShip integration uses email as the link, so be sure to complete this step first.

1. Log in to the CYBERBIZ backend and go to **Website Management > Member Registration Setting > Member registration field setting**.
2. Make sure the **Email** field is selected as **Required**.

![](../../assets/images/EC-後台-管理中心-顧客註冊設定-電子郵件勾選必填01.en.png)

### Step 2: Apply for an ezShip Member Account { #operate-ezship-c2c-account }

1. Go to the [ezShip backend](https://www.ezship.com.tw/sender/sender_register_account.jsp) to register.

    > **Tip**: We recommend filling in **Company Name** as the sender name. This name appears on the shipping label.

2. Complete email and mobile SMS verification.
3. Go to the ezShip backend **我的便利配 > 購物網站串接 > 網站串接申請**.
    ![](../../assets/images/EZSHIP-後台-申請超取-網站串接申請01.en.png)
4. Enter your **store website URL** in the URL field and submit for review.
    ![](../../assets/images/EZSHIP-後台-申請超取-網站串接申請02.en.png)

### Step 3: Apply for Convenience Store Cash on Delivery (Optional) { #operate-ezship-c2c-cod }

If you only need pickup without payment on delivery, you can skip this step.

1. In the ezShip backend, click **我的便利配 > 商務會員 > 申請/續約**.
    ![](../../assets/images/EZSHIP-後台-申請超取-申請續約01.en.png)
2. Select **Individual** or **Corporate** as your identity.
    ![](../../assets/images/EZSHIP-後台-申請超取-申請續約02.en.png)
3. Fill in the details and submit for review.
    > Review usually takes 1–2 business days. You will receive a notification when the feature is enabled.
    ![](../../assets/images/EZSHIP-後台-申請超取-申請續約03.en.png)

    !!! example "Corporate Application Process Example"

        1. Enter the required details in order, and provide photos of your ID card and bank passbook.
        2. Once complete information is provided, ezShip completes the review within 1–2 business days and sends `申請審核完成《功能開啟》通知` by SMS and email.

### Step 4: Connect and Configure in the CYBERBIZ Backend { #operate-ezship-c2c-bind }

1. Log in to the CYBERBIZ backend and go to **Payment and Logistics > Convenience Store Logistics > ezShip 台灣便利配**.
2. **Basic settings**: Enter your ezShip registered email in the **ezShip Membership Account** field.
3. **Enable settings**:
    - **Shipping Fee**: Set a fixed shipping fee per order.
    - **Free shipping threshold**: Set the order amount required for free shipping.
    - **Cash on Delivery**: If you have a business membership, you can switch this toggle to `ON`.
4. Click **Save** to finish setup.

![](../../assets/images/EC-後台-金物流-超商物流-EZSHIP超取01.en.png)

## FAQ { #faq-ezship-c2c }

??? quote "Why can't I find where to print the shipping label in the backend after an order is placed?"
    Because ezShip is a third-party integration platform, its shipping label is generated by the ezShip system. You must log in to the ezShip admin backend to find the order and print the label.

??? quote "Does ezShip support 7-11 pickup?"
    The current integration mainly supports **FamilyMart, Hi-Life, and OK Mart**. For 7-11 pickup, we recommend applying separately for the 7-11 C2C or B2C service offered by **CYBERBIZ PAYMENTS**.

??? quote "Where can I check package status if a customer does not receive an SMS notification?"
    You can check in the ezShip backend. Status sync between ezShip and CYBERBIZ may have a slight delay, so the ezShip backend shows the most accurate status.

