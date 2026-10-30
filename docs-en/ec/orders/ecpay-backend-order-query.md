---
title: "Look Up Orders in the ECPay Merchant Backend"
description: "When you need in-depth financial reconciliation, the reason a payment failed, or a check of logistics status, besides viewing them in the CYBERBIZ admin, you can sign in to the ECPay merchant backend directly to get transaction details."
created: 2026-02-13 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: reference
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
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
  - 查詢信用卡交易明細
  - 查詢全方位金流訂單
  - 查詢物流對帳明細
features:
  - 綠界金流
  - 綠界物流
  - 訂單查詢
prerequisites:
  - "已開通綠界金流或物流服務"
related: []
tags:
  - ECPay
  - ECPay
  - Reconciliation
  - "Payment Lookup"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 外部系統 > 綠界管理後台
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3966
  - https://www.cyberbiz.io/support/?p=21450
permalink: "https://help.cyberbiz.io/ec/orders/ecpay-backend-order-query/"
comments: false
search:
  exclude: false
icon: lucide/external-link
hide: []
---
# Look Up Orders in the ECPay Merchant Backend

When you need in-depth financial reconciliation, the reason a payment failed, or a check of logistics status, besides viewing them in the CYBERBIZ admin, you can sign in to the ECPay merchant backend directly to get transaction details.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../resources/conventions#適用方案) | Professional / Advanced / Expert
{ .doc-badge }

![](../../assets/images/綠界-後台-註冊綠界帳號01.en.png){ .hero-page }

!!! info "Supported Plans"
    The ECPay integration is available only to merchants on the **Professional, Advanced, and Expert plans** who **haven't turned on CYBERBIZ PAYMENTS**. If you already use CYBERBIZ PAYMENTS, it has full order features built in, so you don't need the ECPay integration.


## Before You Start

### Number Conversion Rules

Because of system limits, CYBERBIZ order numbers don't exactly match ECPay transaction numbers. If you can't find the matching number in the ECPay backend, use the following conversion rules:

- **Number structure**: `[MerchantCode][N]_[ConvertedNumber]_R[ChargeCount]`
- **Conversion formula**: ECPay order number suffix = **(CYBERBIZ order number - 1010)**
- **Charge attempts**: R1 is the first card charge. If the charge fails and is retried, it becomes R2, R3, and so on.
- **Example**:
    - Say your merchant ID is 9805.
    - The CYBERBIZ order number is `#2503`.
    - Conversion: 2503 - 1010 = 1493.
    - The number shown in the ECPay backend is `9805N1493R1`.


## Task 1: Look Up Payment Transaction Details

The ECPay backend offers two lookup methods: one for credit cards and one for all-in-one payments.

### 1. Look Up Credit Card Details

Use this to check credit card capture and refund status.

1. Sign in to the [ECPay merchant backend](https://vendor.ecpay.com.tw/).
2. Go to **Credit Card Acquiring > Transaction Details Inquiry**.
    ![](../../assets/images/綠界-後台-查詢信用卡明細01.en.png)
3. Set the date range or enter the card number.
4. Click **Search** to see details such as the authorization status and capture date.
    ![](../../assets/images/綠界-後台-查詢信用卡明細02.en.png)


### 2. Look Up All-in-One Payment Details

Use this if your orders include ATM, web ATM, convenience store payment codes, and so on.

1. Go to **General Order Inquiry > All-in-One Payment Orders**.
2. Set the search criteria (such as transaction date and payment method).
3. Click **Search**. The system lists order details for all payment methods.

![](../../assets/images/綠界-後台-查詢所有明細01.en.png)


## Task 2: Look Up Logistics Reconciliation Details

If you use ECPay convenience store pickup, you can check package status and collected amounts in the logistics management interface.

1. Sign in to the ECPay backend and go to **Logistics Management > Reconciliation Inquiry**.
2. Set the reconciliation date or enter the order number.
3. Click **Search** to check whether the package arrived at the store, whether the buyer picked up and paid, and the expected payout date.

![](../../assets/images/綠界-後台-查詢物流明細01.en.png)

## FAQ

??? quote "Why can't I find a CYBERBIZ order number in the ECPay backend?"
    Searches require the merchant order number, so convert the number first using the conversion rules at the top of this page. Also check that the search date range is correct. For orders that span midnight, adjust the start and end dates.

??? quote "The ECPay backend shows "Authorization Successful," but CYBERBIZ shows "Payment Failed"?"
    This usually happens because of network delays (disconnections), so ECPay's callback didn't reach CYBERBIZ. In this case, go by the ECPay backend data.


