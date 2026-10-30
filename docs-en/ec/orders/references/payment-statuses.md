---
title: "Order Payment Status Reference"
description: "Explains what order payment statuses mean (Awaiting Payment, Payment Received, Cash on Delivery, Payment Failed, and more) and how automatic order cancellation works."
created: 2026-06-08 14:21
last_modified: 2026-07-02 08:52
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans:
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - "Payment Status"
  - "Order Management"
  - "Cash on Delivery"
  - "Refund Status"
  - "Payment Failed"
  - "Abandoned Orders"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/references/payment-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

## Payment Statuses { #payment-statuses }

| Payment Status | Description |
| :-- | :-- |
| Awaiting Payment | The order was placed, but the customer hasn't paid yet. Common while waiting for ATM transfers or convenience store payment codes |
| Payment Received | The customer has paid, and the payment has been received |
| Cash on Delivery | The customer chose cash on delivery; the carrier collects payment on delivery |
| Account Digits Submitted, Not Received | The customer submitted the last 5 digits of the transfer account, but the merchant hasn't confirmed receipt |
| Payment Failed | The payment process was interrupted or declined by the payment provider, such as a failed credit card authorization |
| Abandoned by Member | The customer didn't pay, and the order expired and was voided |
| All Except Abandoned by Member | Filter shortcut: selects all orders that aren't abandoned at once |
| Customer Service Processing | The order is being handled manually by customer service because of a payment or refund issue |
| Pending Refund | A refund is confirmed but hasn't been paid out yet |
| Refunding | The refund is in progress (the refund request was sent, awaiting the payment provider's response) |
| Refunded | A full refund is complete |
| Refund Failed | The refund process failed and needs manual handling |
| Pending Partial Refund | A partial refund is confirmed but hasn't been paid out yet |
| Partially Refunded | A partial refund is complete (for example, the customer returned some items in the order) |
| No Refund | The order is marked as not refunded (for example, the customer agreed to an exchange instead of a refund) |

!!! note "Notes"
    * Orders that are "Awaiting Payment" or "Payment Failed" are both covered by automatic order cancellation. If payment doesn't succeed within the set number of days, the order is canceled automatically.
    * Payment for cash on delivery orders is recognized only after the customer picks up and pays, so the online payment failure process doesn't apply.
    * "All Except Abandoned by Member" is a filter shortcut in the list, not a status an individual order can have.

<!---->
<!-- # Order Payment Status Reference -->
<!---->
<!-- ### Order Payment Status Reference { #payment-statuses } -->
<!---->
<!-- The payment status on the order details page and order list shows how payment stands for the order. The table below describes the statuses most related to handling failed payments: -->
<!---->
<!-- | Payment Status | Description from the Merchant's View | -->
<!-- | :-- | :-- | -->
<!-- | Awaiting Payment | The order was placed, but the customer hasn't paid yet. Common with payment methods that require paying later, such as ATM and convenience store payment codes. | -->
<!-- | Payment Failed | The customer tried to pay but failed, such as a declined credit card. You can guide the customer to pay again or cancel the order. | -->
<!-- | Customer Service Processing | Customer service is handling this payment. | -->
<!-- | Payment Received | Full payment from the customer is confirmed. | -->
<!-- | Partially Refunded | Part of the payment was refunded to the customer. | -->
<!-- | Pending Refund | A refund request exists but the refund isn't complete. | -->
<!---->
<!-- !!! note "Notes" -->
<!--     * Orders that are "Awaiting Payment" or "Payment Failed" are both covered by automatic order cancellation. If payment doesn't succeed within the set number of days, the order is canceled automatically. -->
<!--     * Payment for cash on delivery orders is recognized only after the customer picks up and pays, so the online payment failure process doesn't apply. -->
