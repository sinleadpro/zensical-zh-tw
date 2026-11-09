---
title: "Set up Apple Pay"
description: "Enable and set up Apple Pay as a payment option through CYBERBIZ PAYMENTS for fast and secure transactions."
created: 2026-01-26 00:00
last_modified: 2026-06-30 08:52
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents:
  - 如何設定 Apple Pay
  - Apple Pay 付款設定
features:
  - Apple Pay
  - CYBERBIZ PAYMENTS
  - 金流串接
prerequisites:
  - 已開通 CYBERBIZ PAYMENTS
related:
  - ec/payments-and-logistics/apply-cyberbiz-payments/
  - ec/payments-and-logistics/setup-credit-card-3d-verification/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
tags:
  - "Apple Pay"
  - PAYMENTS
  - "CYBERBIZ PAYMENTS"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8162
  - https://www.cyberbiz.io/support/?p=40622
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/setup-apple-pay/"
comments: false
search:
  exclude: false
icon: simple/applepay
hide: []
---

![Apple Pay Settings](../../assets/images/ec-payments-apple-pay.zh-tw.en.png){ title="Apple Pay Settings" .hero-page }

## Why Use Apple Pay { #intro-apple-pay }

- **Faster checkout**: Customers do not need to enter credit card details manually and can pay directly with their phone.
- **Better experience**: Reduces checkout friction and improves conversion rates.
- **Stronger security**: Verifies transactions with Touch ID or Face ID.
- **Automatically enabled**: Apple Pay is enabled automatically after you activate CYBERBIZ PAYMENTS.
- **Transparent fees**: Rates are the same as for one-time credit card payments, with no additional fees.


## Prerequisites { #prerequisites-apple-pay-req }

- [x] Already [activated **CYBERBIZ PAYMENTS**](apply-cyberbiz-payments.md){ title="Apply for CYBERBIZ PAYMENTS" }

## Usage Notes { #prerequisites-apple-pay }

### Device and Browser Restrictions { #prerequisites-apple-pay-devices }

- **Requirements**: Apple device + Safari browser

- Devices that do not meet these requirements do not display the Apple Pay option.
- Supported devices: [Apple official documentation :lucide-external-link:](https://support.apple.com/zh-tw/102896)

---

### Payment Restrictions { #prerequisites-apple-pay-limits }

- **Supported**: One-time payment
- **Not supported**: Installment payments (use credit card installments instead)

---

### Fees { #specs-apple-pay-fees }

- Same as one-time credit card payments
- No additional transaction fees or annual fees

---

### Refunds { #specs-apple-pay-refund }

- The process is the same as for credit cards

## Steps { #operate-apple-pay }

Apple Pay is usually enabled automatically with CYBERBIZ PAYMENTS. You can adjust its availability and transaction thresholds in the back office.

1. Log in to the CYBERBIZ back office and go to **Payment and Logistics > Payment Settings**.
2. In the CYBERBIZ PAYMENTS section, click **:material-file-document-edit-outline: Edit** to open the edit page.
3. In the Apple Pay settings section:

    - **Toggle on/off** Apple Pay
    - **Set payment thresholds**: Define the maximum and minimum order amounts   

4. Save settings

![Apple Pay settings screen](../../assets/images/ec-金物流-設定 Apple Pay.en.gif){ title="Apple Pay settings screen" }

## Next Steps { #next-steps-apple-pay }

<div class="grid cards" markdown>

- :lucide-shield-check:{ .lg }   
  [__Set Up 3D Verification Threshold__](setup-credit-card-3d-verification.md){ title="Set up 3D verification threshold" }     
  Set the transaction amount threshold. Credit card transactions at or above this amount require additional identity verification to improve transaction security.

- :lucide-ban:{ .lg }     
  [__Set Up Convenience Store Delivery Restrictions and Logistics Exclusions__](../products/shipping/cvs-shipping-restrictions-exclusions.md){ title="Set up convenience store delivery restrictions" }  
  Set delivery logistics conditions for products. Restrict specific logistics methods from appearing or being used during checkout.

</div>


## Frequently Asked Questions { #faq-apple-pay }

??? quote "Does Apple Pay support installment payments?"
	No. Apple Pay supports only one-time payments. For installments, customers must select the "Credit Card Installments" payment method.

??? quote "Do I need to separately apply for Apple Pay after activating CYBERBIZ PAYMENTS?"
	No. Apple Pay is enabled automatically. Merchants can turn it on or off in the back office.

??? quote "Why can't customers see the Apple Pay option?"
	Possible causes:

	- Non-Apple device
	- Non-Safari browser
	- Apple Pay is turned off in the back office
	- The order amount is outside the configured threshold range

??? quote "What is the Apple Pay rate?"
	Rates are the same as for one-time credit card payments and depend on the merchant's contract with CYBERBIZ. There are no additional fees.

??? quote "Can I set order amount limits?"
	Yes. Set the minimum and maximum order amounts in the back office.

??? quote "How long do Apple Pay refunds take?"
	Refunds follow the same process and timeline as credit cards, usually 7 to 14 business days.
