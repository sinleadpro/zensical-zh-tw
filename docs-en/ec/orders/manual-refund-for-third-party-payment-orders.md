---
title: "Manual Refunds for Third-Party Payment Orders"
description: "When the system can't complete an automatic refund for a LINE Pay, JKOPAY, or PayPal order because your payment account balance is insufficient, you can use manual refund."
created: 2026-03-03 00:00
last_modified: 2026-07-14 17:40
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
  - 訂單
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions:
intents:
  - 執行人工退款操作
  - 手動更新訂單狀態
features:
  - 人工退款
  - 金流狀態管理
prerequisites:
  - 需先與顧客確認線下退款方式 (如匯款)
related: []
tags:
  - "Manual Refunds"
  - "Third-Party Payments"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=39872
permalink: "https://help.cyberbiz.io/ec/orders/manual-refund-for-third-party-payment-orders/"
comments: false
search:
  exclude: false
icon: lucide/hand-coins
hide: []
---
# Manual Refunds for Third-Party Payment Orders

When the system can't complete an automatic refund for a LINE Pay, JKOPAY, PayPal, or iPASS order because your payment account balance is insufficient, you can use "Manual Refund."
{ .subtitle }

[:lucide-toggle-right:{ title="Applies To" }](../../resources/conventions#適用功能) | CYBERBIZ PAYMENTS
{ .doc-badge }

!!! tip "Use Cases"
    - **Insufficient balance**: The balance in your payment collection account doesn't cover the refund amount, so the system's automatic refund schedule keeps failing.
    - **Immediate refund needed**: The customer needs the money urgently and doesn't want to wait for the system's nightly automatic refund schedule (around 23:00).
    - **Offline closure**: You've already returned the money by over-the-counter remittance or cash and need to update the admin order status to "Refunded."


## Things to Know

- **Automatic refund time**: CYBERBIZ's default automatic refund time is around 11:00 PM daily.
- **Actual payment handling**: This feature only changes the order status in the admin. After clicking the button, you must return the money to the customer yourself through an offline channel (such as remittance or bank transfer).
- **Irreversible**: Once you click **I'll Refund Manually**, the system **stops** the automatic refund schedule for that order. Be sure to agree with the customer and confirm the refund channel first.
- **Supported payment methods**: LINE Pay, JKOPAY, PayPal, iPASS.

---

## Steps


1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.
2. Open the details page of the order to refund.
3. Click **I'll Refund Manually** at the top right of the page.
4. After completing the offline refund (such as a remittance), return to the order page.
5. Manually change the order status to **Refunded**.

![](../../assets/images/EC-後台-訂單-所有訂單-第三方支付自行人工退款01.en.png)

## FAQ

??? quote "Why can't I see the "I'll Refund Manually" button?"
    The button only appears for orders paid by **third-party payment** that are **Returned**. It doesn't appear if the order uses an unsupported payment method or the return process isn't complete.

??? quote "What if I clicked the button but forgot to send the money to the customer?"
    After you click the button, the system no longer handles the payment. Set up an internal check to make sure every order with a **Manual Refund** has a matching remittance record, to avoid customer complaints.


