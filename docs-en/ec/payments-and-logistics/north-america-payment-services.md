---
title: "North America Payment Services"
description: "North America payment services integrate mainstream international payment solutions, including credit card and e-wallet payments, along with the widely used PayPal service, helping merchants run their businesses smoothly in the U.S. market."
created: 2026-03-03 00:00
last_modified: 2026-06-30 08:52
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 涵蓋北美站專屬金流規格與全域購物車規則
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - US
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
  - 開通北美信用卡支付
  - 設定_PayPal_付款
  - 配置購物車結帳規則
features:
  - 北美站
  - Stripe 支付
  - PayPal
  - 電子錢包支付
prerequisites: []
related: []
tags:
  - Stripe
  - PayPal
  - "Apple Pay"
  - "Google Pay"
acoiv: integration
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=30595
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/north-america-payment-services/"
comments: false
search:
  exclude: false
icon: lucide/globe
hide: []
---

# North America Payment Services

North America payment services integrate mainstream international payment solutions, including credit card and e-wallet payments, along with the widely used PayPal service. They help merchants operate smoothly in the U.S. market.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用方案) |Cross-Border E-Commerce (North America)
[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }

## Payment Option Details

| Payment Method | Transaction Type | Cardholder Country | Fee Rate | Minimum Checkout Amount |
| :--- | :--- | :--- | :--- | :--- |
| **Credit Card /<br>Debit Card /<br>Apple Pay /<br>Google Pay** | Domestic U.S. transactions | United States | 2.6% + 0.3 USD | 0.5 USD |
| | International transactions | Non-U.S. | 3.6% + 0.3 USD | 0.5 USD |
| **PayPal** | Domestic U.S. transactions | United States | 3.49% + 0.49 USD | None |
| | International transactions | Non-U.S. | 4.99% + 0.49 USD | None |


- **Account Reconciliation**: Related payment processing fees are listed on each period's statement.
- **Minimum Checkout Amount**: The system applies a default minimum checkout amount, so merchants do not need to configure it. An order must meet this threshold before the checkout page shows the corresponding payment options.

## Usage Notes

- **Supported Credit Cards**: Visa, Mastercard, American Express, Discover, Diners Club, JCB, China UnionPay.
- **[E-Wallet Usage Guidelines](https://docs.stripe.com/stripe-js/elements/payment-request-button)**
    - **Apple Pay**:
        1. Supported on the Safari browser. Confirm that Apple Pay is enabled.
        2. Supported on Chrome for iOS 16 or later. Apple Pay and Google Pay must be enabled in advance.
    - **Google Pay**: Use the Chrome browser and confirm that Google Pay is enabled. If the payment link has not passed identity verification, complete verification as the system instructs.



## Step 1: Open Payment Options

Go to **Payment and Logistics > Payment Settings** and click :lucide-file-pen-line: **Settings** to the right of **CYBERBIZ PAYMENTS**.

- **Statement Brand Name**: The name shown on the customer's billing statement (English only, up to 12 characters).

![](../../assets/images/北美站-後台-金物流-金流設定-啟用金流01.en.png)


## Step 2: Enable Payment Methods

Select the payment methods you want to enable.

- Credit Card
- Apple Pay
- Google Pay
- PayPal

![](../../assets/images/北美站-後台-金物流-金流設定-啟用金流02.en.png)



