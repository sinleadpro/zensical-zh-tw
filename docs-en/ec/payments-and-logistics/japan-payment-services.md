---
title: "Japan Payment Services"
description: "The Japan site offers localized payment solutions, including major credit cards and Pay-Easy, a convenience service unique to Japan, to help merchants enter the Japanese e-commerce market."
created: 2026-03-03 00:00
last_modified: 2026-06-30 08:52
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：購物車相關設定、訂單相關設定、3D驗證門檻
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
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
  - 開通日本信用卡支付
  - 設定_Pay-Easy_付款
features:
  - 日本站
  - 信用卡支付
  - Pay-Easy
prerequisites: []
related: []
tags:
  - Pay-Easy
acoiv: integration
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=33442
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/japan-payment-services/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# Japan Payment Services

The Japan site offers localized payment solutions, including mainstream credit card payments and Pay-Easy, a convenience service unique to Japan. These help merchants enter the Japanese e-commerce market smoothly.
{ .subtitle }


[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用方案) | Cross-border E-commerce (Japan Site)
[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }

## Payment Option Details { #intro-jp-payments }

| Payment Method | Supported Types | Fee Rate | Minimum Checkout Amount |
| :--- | :--- | :--- | :--- |
| **Credit Card** | Credit Card<br>Debit Card (VISA, MasterCard, JCB) | 3.6% (per transaction) | 50 JPY |
| **Pay-Easy** | ATM<br>Online Bank Transfer | 1.5% (per transaction) | None |


- **Account reconciliation**: Related payment processing fees are listed on each period's statement.
- **Minimum checkout amount**: The system applies a preset minimum checkout amount, so merchants do not need to configure it. An order must meet this amount before the checkout page displays the matching payment options.


## Step 1: Credit Card Payment Setup { #operate-jp-payments-card }

Go to **Payment and Logistics > Payment Settings**. Click :lucide-file-pen-line: **Settings** to the right of **CYBERBIZ PAYMENTS**.

![](../../assets/images/日本站-後台-金物流-金流設定-啟用金流01.en.png)

- **Enable Feature**: Enable **Credit Card**.
- **3D Verification Threshold**: Set the order amount above which 3D verification is required.
- **Payment Threshold Settings**: Set the **Minimum Amount** and **Maximum Amount** for credit card payments.

![](../../assets/images/日本站-後台-金物流-金流設定-設定信用卡01.en.png)

## Step 2: Pay-Easy Payment Setup { #operate-jp-payments-payeasy }

Go to **Payment and Logistics > Payment Settings**. Click :lucide-file-pen-line: **Settings** to the right of Pay-Easy.

- **Enable Feature**: Enable **Pay-Easy Payment**.
- **Payment Threshold Settings**: Set the **Minimum Amount** and **Maximum Amount** for Pay-Easy payments.

![](../../assets/images/日本站-後台-金物流-金流設定-設定Pay-easy01.en.png)