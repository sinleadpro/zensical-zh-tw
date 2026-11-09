---
title: "Southeast Asia Payment Services"
description: "CYBERBIZ offers standard credit card payments and integrates Fiuu (formerly Razer Merchant Services), a leading local payment gateway, to support bank transfers, e-wallets, and convenience store cash payments."
created: 2026-03-03 00:00
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
sites:
  - SEA
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
  - 設定東南亞信用卡支付
  - 串接_Fiuu_第三方支付
features:
  - 東南亞站
  - 馬來西亞金流
  - 新加坡金流
  - Fiuu 支付
prerequisites: []
related: []
tags:
  - Fiuu
  - Malaysia
  - Singapore
acoiv: integration
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=37692
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/southeast-asia-payment-services/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# Southeast Asia Payment Services

CYBERBIZ offers standard credit card payments. It also integrates Fiuu (formerly Razer Merchant Services), a leading local payment gateway, to support bank transfers, e-wallets, and convenience store cash payments.
{ .subtitle }


[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用方案) |Cross-Border E-Commerce (Southeast Asia)
[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }

## Payment Option Details { #intro-sea-payments }

| Payment Method | Supported Channels | Rate (per Transaction) |
| :--- | :--- | :--- |
| **CYBERBIZ PAYMENTS** | Credit Card (VISA/JCB/MasterCard) | 2.0% |
| **Fiuu (Malaysia)** | Bank Transfer | FPX 2.4% or MYR 0.6 (whichever is higher) |
| | Cash | 7-11 Cash 2.4% or MYR 0.8 (whichever is higher) |
| | E-Wallet | Boost (1.6%)<br>DuitNow (1.0%)<br>GrabPay/Shopee Pay (1.4%)<br>Touch'n Go (1.8%) |
| **Fiuu (Singapore)** | Bank Transfer | Paynow (0.7%) |
| | E-Wallet | GrabPay/Shopee Pay (2.6%) |


### Usage Notes { #prerequisites-sea-payments }

- Fiuu previously known as Razer Merchant Services.

## Task 1: Set up CYBERBIZ PAYMENTS (Credit Card) { #operate-sea-payments-card }

Go to **Payment and Logistics > Payment Settings**. Click :lucide-file-pen-line: **Settings** to the right of **CYBERBIZ PAYMENTS**.

![](../../assets/images/東南亞站-後台-金物流-金流設定-啟用金流01.en.png)

- **Enable Feature**: Turn on **Credit Card**.
- **3D Verification Threshold**: Set the order amount above which 3D verification is required.
- **Payment Threshold Settings**: Set the **minimum amount** and **maximum amount** allowed for credit card payments.

![](../../assets/images/東南亞站-後台-金物流-金流設定-開啟CYBPAYMENTS01.en.png)

## Task 2: Connect the Fiuu Third-Party Payment Platform { #operate-sea-payments-fiuu }


### 1. Get the Fiuu Back-Office Keys { #operate-sea-payments-fiuu-key }

Log in to the [Fiuu admin console](https://portal.fiuu.com/index.php?mod=authentication&opt=login), go to **Transactions > Settings**, and copy the following information:

- **Verify Key**
- **Secret Key**



### 2. Set up the Connection in CYBERBIZ { #operate-sea-payments-fiuu-bind }

1. Log in to the CYBERBIZ admin console and go to **Payment and Logistics > Payment Settings**.
2. Click **Fiuu(Malaysia)** or **Fiuu(Singapore)** to open the settings page.
    - Turn on the Fiuu (Malaysia) or Fiuu (Singapore) option that matches your contract with Fiuu. Selecting the wrong option will prevent orders from checking out.
3. Enter the keys you copied above.
    - Make sure the Merchant ID is correct and contains no spaces.

![](../../assets/images/Fiuu-後台-串接欄位填寫01.en.png)

### 3. Configure the Notification URLs { #operate-sea-payments-fiuu-notify }

To ensure Fiuu can return transaction results to your storefront, enter the following three URLs under **Settings** in the Fiuu admin console:

- **Return URL**: `https://cyberbizpay.com/razer/frontend`
- **Notification URL**: `https://cyberbizpay.com/razer/backend`
- **Callback URL**: `https://cyberbizpay.com/razer/callback`


![](../../assets/images/Fiuu-後台-串接欄位填寫02.en.png)


