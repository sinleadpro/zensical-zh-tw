---
title: "MYPAY Wireless Credit Card Machine"
description: "Use the Sunmi wireless credit card and invoice machine with a tablet to create a mobile POS checkout point for pop-up stores, takeout counters, and large stores."
created: 2026-03-25 17:30
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 確認：MYPAY可以用星益欣發票嗎
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有 POS 商店
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
  - 如何安裝商米刷卡機
  - 商米V3H設定教學
  - 商米P2_Pro設定教學
  - MyPay金流串接步驟
features:
  - 商米刷卡機
  - MyPay金流
  - 移動式POS
  - Webhook回報
prerequisites:
  - "POS 前台登入與基礎操作"
related:
  - pos/check/line-pay-scan-payment/
tags:
  - Sunmi
  - SUNMI
  - MyPay
  - "Card Machine"
  - "Invoice Machine"
  - "Mobile POS"
acoiv: configure
apis: []
devices:
  - tablet
ui_components:
  - MyPay特店商務代號
  - 特店金鑰
  - 交易回報網址
paths:
  - POS 功能 > 所有 POS 商店 > 商店設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=51450
  - https://www.cyberbiz.io/support/?p=21480
permalink: "https://help.cyberbiz.io/pos/hardware/mypay-wireless-credit-card-machine/"
comments: false
search:
  exclude: false
icon: lucide/credit-card
hide: []
---

# MYPAY Wireless Credit Card Machine
With the Sunmi wireless credit card and invoice machine, merchants can pair it with a tablet to create a "mobile POS" checkout point. It suits pop-up stores, takeout counters, and large stores that need flexible checkout.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Mobile checkout**: At trade shows or pop-up stores, **only Wi-Fi is needed to take payments and print invoices**, with no large traditional checkout-counter cabling.
    - **Distributed checkout**: During busy periods, staff can use a handheld device to check out customers in line, easing pressure on the counter.
    - **All-in-one**: Combines **credit card payments, barcode scanning, and invoice printing** in one device, simplifying in-store hardware setup.


## Usage Notes { #prerequisites-mypay-terminal }

- **Payment restriction**: The Sunmi card machine plan requires the **MyPay payment service**. Complete the payment service application first.
- **Invoice policy**: The card machine works only as a "printer" and does not include invoice issuing services. Merchants must purchase an invoice service to issue invoices.
- **Drivers**: When you use the MyPay card machine plan, **do not install** the CYBERBIZ POS APP driver. The two use different communication mechanisms.
- **Paper roll specifications**: Use only **10m standard thermal paper rolls** (5.7 cm wide, 3.6 cm outer diameter). Oversized rolls prevent the cover from closing.


## Device Overview { #intro-mypay-terminal }

=== "Sunmi V3H"

    **Features**:

    - Professional handheld POS terminal.
    - Built-in 5.7-inch screen and high-speed thermal printer.
    - Supports 4G and dual-band Wi-Fi.

    ![](../../assets/images/POS-裝置-商米V3H無線發票機01.en.webp){ .screenshot }


=== "Sunmi P2 Pro"

    **Features**:

    - Full-screen touch design.
    - Slim and stylish, suitable for premium stores.
    - Supports magnetic stripe cards, chip cards, and contactless payments.

    ![](../../assets/images/POS-裝置-商米P2PRO無線刷卡機01.en.png){ .screenshot }

## Prerequisites: MyPay Payment Application { #prerequisites-mypay-application }

Before setting up the system, make sure you have the following information:

1. **Purchase the device**: Contact your CYBERBIZ sales representative to purchase the corresponding model.
    - If you buy the card machine from CYBERBIZ, the machine comes with one paper roll.
2. **Apply for payment service**: Go to the [MyPay application page](https://query.onecardpass.com/application/cardreader/b7b68f) and fill in the information.
    - **Review time**: Approval takes about 2 weeks, and MyPay emails the result to the contact person. (If the application fails, submit a new application.)
    - **Support phone**: MyPay customer service 04-23220267 #25.
3. **Obtain keys**: After approval, you will receive:
    - **MyPay merchant business code**
    - **MyPay admin account**
    - **MyPay card machine name**


## Setup Procedure { #operate-mypay-terminal }

### Step 1: Bind the Device { #operate-mypay-terminal-step-a-bind }

After you receive the card machine, sign in to the MyPay App on the machine and [complete the binding](https://www.mypay.com.tw/index.php/zh-tw/news/new-features-online/bind-your-device-and-activate-the-mypay-with-confidence-easy-to-get-started-and-a-smooth-experience).

- Enter the device name: `[您的統編]_01`, for example: `12345678_01`


### Step 2: Bind the CYBERBIZ Back Office { #operate-mypay-terminal-step-b-bind }

1. **Get the MyPay key**: Sign in to the [MAPAY admin console](https://biz.spay.com.tw/auth/login), go to **System Setting > Key Management**, and get the **MYPAY merchant key**.
    ![](../../assets/images/MAYPAY-後台-系統設定-金鑰管理-查詢金鑰01.en.png){ .screenshot }
2. **Go to the CYBERBIZ back office**: Sign in to the CYBERBIZ admin console and go to **POS > POS Store List**.
3. **Enter API information**: In the **POS checkout settings** section, enter the **MyPay merchant business code** and **MyPay merchant key**.
    ![](../../assets/images/POS-後台-所有POS商店-綁定MAYPAY金鑰01.en.png){ .screenshot }
4. **Set up the invoice system**: Click **Edit POS Settings**.
    ![](../../assets/images/POS-後台-所有POS商店-修改POS子機設定01.en.png){ .screenshot }
    - **POS invoice settings**: Select **Meng-Li Invoice**.
    - **Invoice machine settings**: Select **MYPAY Invoice Machine**.
    ![](../../assets/images/POS-後台-所有POS商店-修改POS子機發票設定01.en.png){ .screenshot }
5. **Configure the card machine code**: **MYPAY card machine name**: Enter `[您的統編]_01` (for example: `12345678_01`).
    ![](../../assets/images/POS-後台-所有POS商店-綁定MAYPAY金鑰01.en.png){ .screenshot }
6. **Enable the payment method**: Click the **Payment Method** tab, switch the **MYPAY** toggle to `開啟 (ON)`, and save.
    ![](../../assets/images/POS-後台-所有POS商店-付款方式-新增MYPAY付款方式01.en.png){ .screenshot }


### Step 3: MyPay Back Office Webhook Settings { #operate-mypay-terminal-step-c-mypay }

To make sure transaction results return correctly to the CYBERBIZ system, you must set up the callback URLs.

1. Sign in to the [MyPay admin console](https://biz.spay.com.tw/auth/login).
2. Go to **System Setting > Payment Service System > Connection Notification Settings**.
3. In the designated fields, enter the URL for your device model.
    - **URL format**: `https://[您的商家網址]/mypay/notify`
    - **URL example**: `https://shop123.cyberbiz.co/mypay/notify`

    === "Sunmi V3H"

        Enter the same callback URL in the following **three fields**:

        - **Real-time transaction callback URL**
        - **Non-real-time callback URL**
        - **Refund/cancellation callback URL**

        ![](../../assets/images/MAYPAY-後台-系統設定-金流服務系統-填寫回報網址V3H01.en.png){ .screenshot }

    === "Sunmi P2 Pro"

        Enter the same callback URL in the following **two fields**:

        - **Real-time transaction callback URL**
        - **Refund/cancellation callback URL**

        ![](../../assets/images/MAYPAY-後台-系統設定-金流服務系統-填寫回報網址P2 Pro01.en.png){ .screenshot }

4. Click the **Test** button. When "Connection successful" appears, setup is complete.

    > If the connection fails, first check the spelling and format of the **callback URL**. If problems persist after you rule out the URL, contact CYBERBIZ technical support.

    ![](../../assets/images/MAYPAY-後台-系統設定-金流服務系統-填寫回報網址02.en.png){ .screenshot }

5. Go to the POS front-end checkout page and check whether **Payment Method** shows the **MYPAY** option.

    > You can create a test order to confirm that the POS completes checkout after a scan or tap.


### Step 4: Card Machine Operation and Checkout { #operate-mypay-terminal-step-d-operation }

1. **Sign in to the device**: Open the **MyPay APP** on the card machine and enter your account and password.
2. **Front-end checkout**:
    - After you select items on the POS front end, select the **MyPay** payment method.
    - Click **Pay**. The system automatically prompts the card machine to show the tap screen.
    - The customer taps or inserts a card to complete payment. The machine automatically prints the receipt and invoice.
3. **Cancel and refund processing**:
    - In the POS front-end order list, click **Cancel Order**.
    - Click **Refund**. The card machine automatically prints the refund receipt.



## Frequently Asked Questions { #faq-mypay-terminal }

??? quote "Why doesn't the card machine respond after clicking Pay?"
    1. Make sure the tablet POS and the card machine are connected to the same Wi-Fi network.
    2. Check that the "card machine name" in the CYBERBIZ back office exactly matches the name you signed in with in the MyPay APP.
    3. Make sure you did not install the POS driver by mistake. If you did, remove it.

??? quote "Can the card machine process LINE Pay payments?"
    The Sunmi card machine currently supports only physical credit card payments. To use LINE Pay, see the [POS LINE Pay scan payment](../check/line-pay-scan-payment.md) tutorial and use a barcode scanner.

??? quote "Where can I buy invoice paper rolls when I run out?"
    Buy them from the [Ministry of Finance e-Invoice Thermal Paper Platform](https://invoice.ppmof.gov.tw/PSJ_Web/) or an office supply store. Specify **10m standard thermal paper rolls** (outer diameter about 3.6 cm). Standard 50m or 80m rolls for desktop invoice machines are too thick to fit.


## More Operations { #next-steps-mypay-terminal }

<div class="grid cards" markdown>

- :lucide-hand-coins:{ .lg }   
  [__Sunmi P2 Pro Operation Guide__](https://drive.google.com/file/d/1r7yUn55ci36ZcQytTHZm1aQuuOQb6Qp6/view?usp=sharing)     
  Hands-on Sunmi P2 Pro tutorial to help your store staff get up to speed quickly.

</div>

