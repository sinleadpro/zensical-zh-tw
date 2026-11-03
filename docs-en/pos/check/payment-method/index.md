---
title: "Payment Methods"
description: "Manage the payment methods available on the POS frontend, including cash, credit card terminal integration, and mobile payments."
created: 2026-04-10 16:30
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 其他付款方式是否需要文件
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有POS門市
sites:
  - TW
audiences:
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
  - 設定 POS 付款方式
  - 串接信用卡機
  - 設定行動支付
features:
  - POS 付款方式
  - 信用卡機串接
  - 多付款方式
prerequisites: []
related:
  - pos/hardware/taishin-wired-credit-card-machine/
  - pos/hardware/mypay-wireless-credit-card-machine/
  - pos/check/line-pay-scan-payment/
  - pos/check/payment-method/multiple-payment-methods/
tags:
  - "POS Payment Methods"
  - "Credit Card"
  - "LINE Pay"
  - "Mobile Payment"
acoiv: configure
apis: []
devices:
  - tablet
  - desktop
ui_components:
  - 付款方式
paths:
  - POS 功能 > 所有 POS 商店 > 付款方式
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=3060
permalink: "https://help.cyberbiz.io/pos/check/payment-method/"
comments: false
search:
  exclude: false
icon: lucide/banknote
hide: []
---

# Payment Methods
Manage the payment methods available on the POS frontend, including cash, credit card terminal integration, and mobile payments.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

![](../../../assets/images/POS-後台-所有POS門市-付款方式-畫面總覽01.en.png){ .hero-page }

## Usage Notes

- **Staff Permissions**: Only the **Website Owner** and **POS Store Manager** can use this feature.
- **Hardware Requirements**: Some payment methods (such as credit card terminals and EasyCard) require a specific card reader model.

## Operation Procedure

### Enable Payment Methods

=== "Backend Setup"

    1. Log in to the POS admin backend, go to **POS > POS Store List > [Click the POS store]**, and click the **Payment Method** tab.
    2. Enable the payment options that your store's checkout needs:

        <div class="grid cards" markdown>

        - :lucide-banknote-arrow-down:{ .lg }   
        __Cash__<br>
        This is a default payment method and does not need to be enabled separately.

        - :lucide-credit-card:{ .lg }   
        [__Credit Card (Card Terminal)__](../../hardware/taishin-wired-credit-card-machine.md)   
        Connects to Taishin Bank wired card terminals. Transaction amounts sync automatically to the terminal, reducing manual entry errors.

        - :lucide-smartphone:{ .lg }   
        [__MYPAY__](../../hardware/mypay-wireless-credit-card-machine.md) <br>
        Suitable for tablet use. Requires the Sunmi P2 PRO card reader service.

        - :lucide-wallet:{ .lg }   
        [__LINE Pay__](../line-pay-scan-payment.md)<br>
        Connects to LINE Pay and supports QR code payment at the front counter.

        - :lucide-layers:{ .lg }   
        [__Multiple Payment Methods__](multiple-payment-methods.md) <br>
        Splits a single order across multiple payment methods (such as cash plus gift voucher)<br>
        Use Cases: **Five-Times Vouchers, Revitalization Vouchers, Dongzi Vouchers**

        </div>

=== "Frontend Display"

    1. Log in to the POS frontend and go to **Checkout**.
    2. View the payment options successfully created on the POS device in the upper-right corner of the checkout page.

        !!! info "Payment Option Display Check"
            If a specific payment option does not appear on the frontend, the option was not created successfully. First, review the setup steps in this guide. If the issue persists, contact CYBERBIZ customer support for help.

    ![](../../../assets/images/POS-前台-結帳-付款方式01.en.png){ .screenshot }

### Frontend Display Order

=== "Backend Setup"

    - **Custom Order**: Long-press the :lucide-move: (move icon), then drag options to change their display order on the frontend.

    ![](../../../assets/images/POS-後台-所有POS門市-付款方式-調整付款排序01.en.gif){ .screenshot }

=== "Frontend Display"

    - **Golden Slot Mechanism**: The frontend displays only the **first three** payment options by default. The remaining options are collapsed under **Other Payment Methods**.
    - **Expand and Select**: Click **Other Payment Methods** to open a pop-up that shows the remaining options for quick selection.
    - **Optimization Tip**: Move frequently used payment methods higher in the backend sort order to improve checkout conversion rates.

    ![](../../../assets/images/POS-前台-結帳-付款方式01.en.png){ .screenshot }
