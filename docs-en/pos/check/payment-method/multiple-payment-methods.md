---
title: "Set up Multiple Payment Methods on POS"
description: "Learn how to set up multiple payment methods in CYBERBIZ POS so that one order can be split across tools such as cash, gift vouchers, and stimulus vouchers, and how to configure bonus accumulation rules."
created: 2026-04-10 17:00
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 報表 > 訂單彙總報表還有嗎
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - POS 功能
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定 POS 多付款方式
  - 拆分訂單支付金額
  - 設定不累計紅利的付款方式
features:
  - POS 多付款方式
  - 紅利累計規則
  - 補差額功能
prerequisites:
  - pos/check/payment-method/
related: []
tags:
  - POS_Multiple_Payment_Methods
  - Gift_Voucher
  - Stimulus_Voucher
  - Bonus_Calculation
  - Split_Payment
acoiv: configure
apis: []
devices:
  - tablet
  - desktop
ui_components:
  - 多付款方式
  - 補差額
paths:
  - 後台 > POS 功能 > 所有 POS 商店 > 付款方式
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=3268
  - https://www.cyberbiz.io/support/?p=7844
permalink: "https://help.cyberbiz.io/pos/check/payment-method/multiple-payment-methods/"
comments: false
search:
  exclude: false
icon: lucide/layers
hide: []
---

# Set up Multiple Payment Methods on POS
When a transaction requires multiple payment methods, such as cash plus a gift voucher, you can use the multiple payment methods feature to split the payment and record each part.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
	- **Split payment**: The customer wants to pay part of the amount in cash and the remaining balance by credit card.
	- **Voucher redemption**: The customer holds store gift vouchers, 5x vouchers, or Dongzi vouchers. The voucher face value is deducted first, and then the customer pays the difference.
	- **Bonus control**: For specific payment methods, such as gift vouchers, set them so they do not earn bonus points.

## Usage Notes

- **Manual recording only**: Multiple payment methods only provide **payment records**, and they **cannot connect automatically** to physical card readers or mobile payment devices. For card payments, staff must enter the amount manually on the card reader.
- **Bonus calculation logic**: The system automatically calculates the final bonus points the order can earn, based on the **Accumulate Bonus** setting of each payment item.


## Back-Office Setup

### Step 1: Turn on Multiple Payment Methods

1. Log in to the CYBERBIZ POS admin dashboard and go to **POS > POS Store List > [Click the POS store] > Payment Methods**.
2. In the **Payment Method** list on the left, turn on the **Multiple Payment Methods** option.

![](../../../assets/images/POS-後台-所有POS門市-付款方式-新增多付款方式01.en.png){ .screenshot }


### Step 2: Select an Invoice Issuance Method

Select whether to issue an invoice for the amount paid with each payment method:

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-後台-所有POS商店-新增付款方式01.png){ .screenshot }

- **Issue invoice**: Add payment methods in the **Multiple Payment Methods (Issue Invoice)** section.
- **Do not issue invoice**: Add payment methods in the **Multiple Payment Methods (Do Not Issue Invoice)** section.
    - When the system issues an invoice at checkout, the amount paid with payment methods in this section is not invoiced.
    - In the order details, the `[付款方式名稱] 扣抵` field marks the order amount that is not invoiced.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS發票-多付款方式不開立發票01.png){ .small-image }

!!! example "Example"
    For an order amount of NT$1,000, `現金（開立發票）` pays NT$500 and `禮券（不開立發票）` pays NT$500.
    When the system issues an invoice, it issues an invoice only for NT$500.


### Step 3: Set up Payment Items

1. In the **Multiple Payment Methods** list on the right, click **Add Item** and enter a custom name, such as gift voucher or stimulus voucher.

    > You can create multiple payment categories, such as gift vouchers and complimentary vouchers, to handle diverse payment scenarios.

2. Set the **Accumulate Bonus** toggle:
    - `On`: The amount paid with this method counts toward bonus points.
    - `Close`: This portion of the amount is not included in the bonus base.

    !!! example "Bonus Calculation Example"
        The order total is NT$5,000, split into the following payment methods:

        - **Cash**: NT$2,000 (Accumulate Bonus: On)
        - **Gift voucher**: NT$3,000 (Accumulate Bonus: Off)

        In this case, only **NT$2,000** is used as the basis for issuing bonus points.

3. Switch the **On / Off** toggle to `ON(啟用)`.
4. Click **Save Payment Method Settings** to complete the setup.

![](../../../assets/images/POS-後台-所有POS門市-付款方式-新增多付款方式02.en.png){ .screenshot }

## Front-End Operations

### Checkout

1. On the POS front-end checkout page, click **Other Payment Methods**.
2. Select **Multiple Payment Methods**.
3. Click **Add Payment Item**, then select a configured payment tool from the drop-down list.
4. Enter the deduction amount for each payment tool.
    - **Tip**: Click the **Fill Balance** button, and the system automatically fills in the remaining amount to be paid.
5. After confirming the total is correct, click **Confirm**.
6. After selecting an invoice issuance method, click **Collect Payment** to complete checkout.

![](../../../assets/images/POS-前台-結帳-多付款方式-建立多付款選項01.en.gif){ .screenshot }


### Order Details Lookup

1. In **POS > Orders**, click the :lucide-info: info box in the upper-right corner to view the order details.
2. The first line of the details shows the split payment information and amounts.

![](../../../assets/images/POS-前台-訂單-顯示多付款方式細項01.en.gif){ .screenshot }

### Shift Close Reconciliation

1. Log in to the POS front-end and go to **Others > Interim Closing**.
2. In the **Sales** section, you can view the amounts received during the current shift.

![](../../../assets/images/POS-前台-其他功能-小結關帳-營業額顯示多付款方式細項01.en.png){ .screenshot }

### Record Lookup

1. Log in to the POS front-end and go to **Others > Reconciliation**.
2. Set a time range.
2. In the **Sales** section, you can view the amounts received during that time range.

![](../../../assets/images/POS-前台-其他功能-對帳-多付款方式細項01.en.png){ .screenshot }

