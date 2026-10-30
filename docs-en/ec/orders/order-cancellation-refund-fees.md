---
title: "Order Cancellation and Refund Fees"
description: "When an order is canceled or returned and refunded, the system determines whether each fee is refunded based on the refund method and refund scope."
created: 2026-08-27 16:27
last_modified: 2026-10-02 15:20
lang: en-US
type: reference
status: ""
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
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 確認退款手續費返還規則
  - 查詢金流自動退款期限
  - 判斷人工退款手續費
features: 
  - 訂單取消
  - 全額退款
  - 部分退款
  - 自動退款
  - 人工退款
  - 金流手續費
prerequisites: []
related: 
  - ec/orders/order-refund-process/
tags: 
  - "Order Cancellation"
  - "Order Refunds"
acoiv: operation
apis: []
devices: []
ui_components: 
  - 退款方式
  - 付款狀態
  - 退貨狀態
paths: 
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/order-cancellation-refund-fees/"
comments: false
search:
  exclude: false
icon: lucide/receipt-text
hide: []
---

## Refund Scope and Fee Refunds

The tables below apply to order cancellations and return refunds (full refunds / partial refunds):


### Standard Plan Without CYBERBIZ PAYMENTS

> **Applicable payment providers**: LINE Pay / PayPal / JKOPAY / iPASS / **ECPay** / **NewebPay**

| Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
| ------- | -------- | -------- | ---------- | ------------- |
| Cancel order | **Merchant bank transfer** | Not applicable | Handled by the third-party payment provider | **Not charged** |
| Full refund | **Merchant bank transfer** | Not applicable | Handled by the third-party payment provider | **Not charged** |


### Standard Plan with CYBERBIZ PAYMENTS

=== "CYBERBIZ PAYMENTS"

    > **Applicable payment options**: Credit card / Apple Pay / Google Pay / UnionPay / Virtual ATM / Convenience store code / Cash on Delivery

    | Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
    | ------- | -------- | -------- | ---------- | ------------ |
    | Cancel order | Automatic system refund | Not applicable | Fully refunded | Not charged |
    | | **Merchant bank transfer** | Not applicable | Not refunded | **Not charged** |
    | Full refund | Automatic system refund | Not applicable | Fully refunded | Not charged |
    | | **Merchant bank transfer** | Not applicable | Not refunded | **Not charged** |
    | Partial refund | Automatic system refund | Not applicable | Refunded in proportion to the refund amount | Not charged |
    | | **Merchant bank transfer** | Not applicable | Not refunded | **Not charged** |

=== "Other Payment Providers"

    > **Applicable payment providers**: LINE Pay / PayPal / JKOPAY / iPASS

    | Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
    | ------- | -------- | -------- | ---------- | ------------ |
    | Cancel order | Automatic system refund | Not applicable | Handled by the third-party payment provider | Not charged |
    | | **Merchant bank transfer** | Not applicable | Handled by the third-party payment provider | **Not charged** |
    | Full refund | Automatic system refund | Not applicable | Handled by the third-party payment provider | Not charged |
    | | **Merchant bank transfer** | Not applicable | Handled by the third-party payment provider | **Not charged** |
    | Partial refund | Automatic system refund | Not applicable | Handled by the third-party payment provider | Not charged |
    | | **Merchant bank transfer** | Not applicable | Handled by the third-party payment provider | **Not charged** |


### PLUS and Enterprise

=== "CYBERBIZ PAYMENTS"

    > **Applicable payment options**: Credit card / Apple Pay / Google Pay / UnionPay / Virtual ATM / Convenience store code / Cash on Delivery

    | Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
    | ------- | -------- | -------- | ---------- | ------------- |
    | Cancel order | Automatic system refund | Fully refunded | Fully refunded | Not charged |
    | | **System manual refund** | Fully refunded | Not refunded | **Charged** |
    | Full refund | Automatic system refund | Fully refunded | Fully refunded | Not charged |
    | | **System manual refund** | Fully refunded | Not refunded | **Charged** |
    | Partial refund | Automatic system refund | Refunded in proportion to the refund amount | Refunded in proportion to the refund amount | Not charged |
    | | **System manual refund** | Refunded in proportion to the refund amount | Not refunded | **Charged** |


=== "Other Payment Providers"

    > **Applicable payment providers**: LINE Pay / PayPal / JKOPAY / iPASS

    | Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
    | ------- | -------- | -------- | ---------- | ------------- |
    | Cancel order | Automatic system refund | Fully refunded | Handled by the third-party payment provider | Not charged |
    | | **Merchant bank transfer** | Fully refunded | Handled by the third-party payment provider | **Not charged** |
    | Full refund | Automatic system refund | Fully refunded | Handled by the third-party payment provider | Not charged |
    | | **Merchant bank transfer** | Fully refunded | Handled by the third-party payment provider | **Not charged** |
    | Partial refund | Automatic system refund | Refunded in proportion to the refund amount | Handled by the third-party payment provider | Not charged |
    | | **Merchant bank transfer** | Refunded in proportion to the refund amount | Handled by the third-party payment provider | **Not charged** |



### Cross-Border

=== "CYBERBIZ PAYMENTS"

    > **Applicable sites**: North America / Japan (Taiwan to Japan) / Southeast Asia

    | Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
    | ------- | -------- | -------- | ---------- | ------------- |
    | Cancel order | Automatic system refund | Fully refunded | Southeast Asia site: Refunded<br>Other sites: **Not refunded** | Not charged |
    | | **Merchant bank transfer** | Fully refunded | Southeast Asia site: Refunded<br>Other sites: **Not refunded** | **Not charged** |
    | Full refund | Automatic system refund | Fully refunded | Southeast Asia site: Refunded<br>Other sites: **Not refunded** | Not charged |
    | | **Merchant bank transfer** | Fully refunded | Southeast Asia site: Refunded<br>Other sites: **Not refunded** | **Not charged** |
    | Partial refund | Automatic system refund | Refunded in proportion to the refund amount | Southeast Asia site: Refunded<br>Other sites: **Not refunded** | Not charged |
    | | **Merchant bank transfer** | Refunded in proportion to the refund amount | Southeast Asia site: Refunded<br>Other sites: **Not refunded** | **Not charged** |


=== "Other Payment Providers"

    > **Applicable sites (payment providers)**: Japan to Taiwan (SoftBank), Southeast Asia (Fiuu), Malaysia Local Edition (Fiuu), Australia Local Edition (Airwallex)

    | Refund Scenario | Refund Method | System Maintenance Fee | Payment Processing Fee | Manual Refund Fee |
    | ------- | -------- | -------- | ---------- | ------------- |
    | Cancel order | Automatic system refund | Fully refunded | Not refunded / Handled by the third-party payment provider :lucide-info: | Not charged |
    |  | **Merchant bank transfer** | Fully refunded | Not refunded / Handled by the third-party payment provider :lucide-info: | **Not charged** |
    | Full refund | Automatic system refund | Fully refunded | Not refunded / Handled by the third-party payment provider :lucide-info: | Not charged |
    |  | **Merchant bank transfer** | Fully refunded | Not refunded / Handled by the third-party payment provider :lucide-info: | **Not charged** |
    | Partial refund | Automatic system refund | Refunded in proportion to the refund amount | Not refunded / Handled by the third-party payment provider :lucide-info: | Not charged |
    |  | **Merchant bank transfer** | Refunded in proportion to the refund amount | Not refunded / Handled by the third-party payment provider :lucide-info: | **Not charged** |

    !!! info "How Payment Processing Fees Are Handled"
        Refunds of payment processing fees depend on how your site is connected to payment providers:

        - **CYBERBIZ collects payments**: CYBERBIZ payment processing fees aren't refunded.
        - **Third-party provider pays out directly**: Payment processing fees follow that provider's refund policy.


!!! note "How Proportional Refunds Are Calculated"
    For partial refunds, the proportional refund is calculated as **refund amount ÷ order amount × original fee**.

## Manual Refund Fee Exceptions

The manual refund fee isn't charged in these cases:


| Exception | Description |
| :--- | :--- |
| E-ticket orders | Refunds on ticket-type orders |
| Disputed payment refunds | Refunds issued because of a payment dispute |
| Cash on Delivery not received | Cash on Delivery orders not yet received |
| Merchant-changed order amount | Refunds issued after the merchant adjusts the order amount |


## Next Steps

<div class="grid cards" markdown>

- :lucide-rotate-ccw:{ .lg }
  [__Refund an Order__](order-refund-process.md){ title="Refund Methods and Operations" }
  Complete an automatic refund, manual refund, or merchant bank transfer based on the payment method.

- :lucide-hand-coins:{ .lg }
  [__Manually Refund Third-Party Payments__](manual-refund-for-third-party-payment-orders.md){ title="Manual Refunds for Third-Party Payment Orders" }
  Handle offline refunds and payment status updates for third-party payment orders.

</div>

## FAQ

??? quote "How do I check whether an order is past the automatic refund deadline?"
    Check the payment method and payment date, then compare them with the [automatic refund deadlines by plan and payment provider](order-refund-process/#步驟-1判定退款方式). For CYBERBIZ PAYMENTS payment methods, the actual deadline follows your admin settings.
