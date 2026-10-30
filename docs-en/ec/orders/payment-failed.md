---
title: "Handle Orders with Failed Payments"
description: "What you can do when an order payment fails, including guiding the customer to pay again, setting up automatic reminders, automatically canceling orders, and recharging subscription orders."
created: 2026-06-08 13:52
last_modified: 2026-07-09 15:31
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
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 處理付款失敗訂單
  - 引導顧客重新付款
  - 設定付款失敗自動提醒
  - 自動取消付款失敗訂單
  - 定期定額扣款失敗處理
features:
  - 重新付款連結
  - 付款失敗自動提醒
  - 訂單自動取消
  - 定期定額重新扣款
  - AFTEE 先享後付
  - 信用卡 3D 驗證
  - 美安 shop.com
prerequisites: []
related:
  - ec/orders/order-settings/provide-payment-link/
  - ec/payments-and-logistics/payments/order-settings/
  - ec/notifications/manage-email-templates/
  - ec/notifications/manage-sms-templates-v2/
  - ec/orders/basics/cancel-order/
  - ec/marketing/other-tools/subscription-campaign-page/
  - ec/payments-and-logistics/setup-aftee/
  - ec/payments-and-logistics/setup-credit-card-3d-verification/
  - ec/orders/references/payment-statuses/
tags:
  - "Payment Failed"
  - "Pay Again"
  - "Order Reminders"
  - "Automatic Cancellation"
  - Subscriptions
  - AFTEE
  - "3D Secure"
  - Shop.com
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 重新付款連結
  - 結帳頁
  - 自動提醒設定
  - 定期定額訂單列表
paths:
  - 訂單 > 所有訂單
  - 金物流 > 結帳頁 & 物流設定
  - 訊息推播 > 簡訊通知樣板
  - 訊息推播 > Email 通知樣板
  - 定期定額訂單 > 定期訂單列表
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=2402
permalink: "https://help.cyberbiz.io/ec/orders/payment-failed/"
comments: false
search:
  exclude: false
icon: lucide/banknote-x
hide: []
---

![Order payment failed status](../../assets/images/ec-訂單-所有訂單-付款失敗-hero.en.png){ title="Order Payment Failed Status" .hero-page }

## About Failed Payments { #intro-payment-failed }

When a customer's card payment doesn't go through because of incorrectly entered credit card information, an insufficient credit limit, or other reasons, the order's payment status shows "Payment Failed." These orders aren't lost for good. You can guide the customer to pay again, have the system send reminders automatically, or cancel the order once you confirm the customer won't buy, reducing lost orders.

This page explains four ways to handle orders after a failed payment, and what to do when special payment methods such as subscriptions or buy now, pay later fail.

---

## Prerequisites and Limitations { #prerequisites-payment-failed }

Each option has different requirements. Most are available on all plans; only a few require a specific plan:

- [x] **Guide the customer to pay again**: Available on all plans; no extra setup needed.
- [x] **Automatic failed payment reminders**: Available on all plans. Once enabled, notifications are sent based on the number of days you set.
- [x] **Automatic order cancellation**: Available on all plans. Takes effect once you enter the number of days on the settings page.
- [x] **Subscription recharge**: Requires a plan with the subscription feature enabled.
- [x] **Market America order commission handling**: Requires a plan with the Market America partner store feature enabled.

??? plan "Feature Availability by Plan"
    | Option | Requirement |
    | :-- | :-- |
    | Payment link | Built into all plans |
    | Automatic failed payment reminders | Built into all plans |
    | Automatic order cancellation | Built into all plans |
    | Subscription recharge | Requires the subscription feature |
    | Market America (Shop.com) referrals | Requires the Market America partner store feature |
    | AFTEE buy now, pay later | Requires the AFTEE buy now, pay later feature |

---

## Steps { #operate-payment-failed }

The following explains the steps for four common situations.

### Guide the Customer to Pay Again { #operate-payment-failed-resend-link }

When an order shows "Payment Failed," you can give the customer the order's checkout page link so they can return to the checkout page and complete payment.

1. **Open the order details page:** Go to "Orders" > "All Orders" in the admin and click the "Order Number" of the failed order.
2. **Find the checkout page link:** In the payment status section of the order details page, when the order is unpaid, the system shows the message "If you contacted the customer and they lost the online checkout page, you can send them this link"[^adjustment].
3. **Copy and share the link:** Click or copy "this link" and send it to the customer through your usual channel (phone, messaging app, etc.).
4. **The customer pays again:** When the customer opens the link, they return to the order's checkout page and can choose any payment method you've enabled to complete payment. After payment succeeds, the order's payment status updates automatically.

!!! tip "Tip"
    If the payment fails during checkout, the checkout page shows the failure message right away and the customer can retry on that page, so you don't necessarily need to send a link.

[^adjustment]: If the order has a pending additional charge or refund amount, the message changes to "If the member lost the online checkout page, you can send them this link. Note: The original order must be paid before additional charge or refund status can be recorded."

<div class="grid cards" markdown>

- :lucide-link:{ .lg }
  [__Send a Payment Link__](order-settings/provide-payment-link.md){ title="Send Customers a Payment Link" }

</div>

---

### Set Up Automatic Failed Payment Reminders { #operate-payment-failed-reminder }

To improve order conversion, you can turn on automatic reminders so the system emails or texts customers at the interval you set after a payment fails.

1. **Open the settings page:** Go to "Payment and Logistics" > "Checkout Page & Logistics" in the admin and find the "Order Payment Failure Reminder Settings" section.
2. **Set the interval:** Enter the number of days between reminders in "Set Days" and click **"Submit."** The system sends reminders at that interval, **up to three times** [^reminder-rule].
3. **Enable notification templates:** Go to "Notifications," find "Customer Payment Failure Reminder" in "SMS Notification Templates" or "Customer Payment Failure Reminder" in "Email Notification Templates," enable it, and edit the content if needed.

!!! note "Note"
    This reminder isn't sent for Cash on Delivery orders, because they don't need online payment.

[^reminder-rule]: For example, with 3 days set, an order placed on January 1 gets a reminder on January 4, 7, and 10, three times in total.

<div class="grid cards" markdown>

- :lucide-bell-ring:{ .lg }
  [__Set Up Failed Payment Reminders__](../payments-and-logistics/payments/order-settings.md#operate-order-settings-payment-reminder){ title="Order Settings" }

- :lucide-mail:{ .lg }
  [__Manage Email Notification Templates__](../notifications/manage-email-templates.md){ title="Set Up and Manage Email Notification Templates" }

- :lucide-message-square:{ .lg }
  [__Manage SMS Notification Templates__](../notifications/manage-sms-templates-v2.md){ title="Set Up and Manage SMS Notification Templates" }

</div>

---

### Cancel Orders with Failed Payments { #operate-payment-failed-cancel }

If the customer decides not to buy, or too many failed orders pile up, you can have the system cancel them automatically or handle them manually.

**Automatic cancellation (recommended):**

1. **Open the settings page:** Go to "Payment and Logistics" > "Checkout Page & Logistics" in the admin and find the "Automatic Order Cancellation" section.
2. **Set the cancellation days:** Enter the number of days and save. Orders still unpaid after that many days (**including orders with failed payments**) are canceled automatically[^auto-cancel-default].

**Manual cancellation:**

* The customer cancels the unpaid order in the storefront "Member Center."
* Or you cancel the order manually on the order details page.

[^auto-cancel-default]: The default is 7 days. If set to 0, the system doesn't cancel any orders automatically.

<div class="grid cards" markdown>

- :lucide-clock-alert:{ .lg }
  [__Set Up Automatic Order Cancellation__](../payments-and-logistics/payments/order-settings.md#operate-order-settings-auto-cancel){ title="Order Settings" }

- :lucide-circle-x:{ .lg }
  [__Cancel Orders Manually__](basics/cancel-order.md#orders-cancel-merchant){ title="How to Cancel an Order" }

</div>

---

### Recharge Subscription Sub-Orders { #operate-payment-failed-recurring-recharge }

If a charge fails for a subscription sub-order, the system emails both you and the customer. The customer can't retry on their own; you need to recharge manually in the admin.

1. **Open the subscription order list:** Go to "Subscription Orders" in the admin and open the "Subscription Order List."
2. **Find the failed sub-order:** Find the subscription order that shows a failed charge in the list.
3. **Recharge:** Click **"Recharge"** for the order, then click **"Reset Charge"** in the confirmation window to submit.

!!! plan "Plan / Requirements"
    Subscriptions are a feature that must be enabled. If your store hasn't enabled it, the "Recharge" button doesn't appear in the subscription order list. Customers can't recharge on their own and need to contact you for help.

<div class="grid cards" markdown>

- :lucide-repeat:{ .lg }
  [__Subscriptions__](../marketing/other-tools/subscription-campaign-page.md){ title="Subscription Campaign Page" }

</div>

---

## Special Payment Failure Cases { #specs-payment-failed }

Troubleshooting and handling differ slightly by payment method:

### AFTEE Buy Now, Pay Later { #specs-payment-failed-aftee }

If the customer's AFTEE buy now, pay later review isn't approved, ask the customer to try again following the system instructions, or suggest they contact AFTEE directly about the review result.

<div class="grid cards" markdown>

- :lucide-layers:{ .lg }
  [__AFTEE Buy Now, Pay Later Payments__](../payments-and-logistics/setup-aftee.md){ title="Set Up AFTEE" }

</div>

---

### Credit Card 3D Secure Failures { #specs-payment-failed-3ds }

If the customer fails credit card 3D Secure verification (didn't receive the verification text or failed verification), it's a verification issue on the card issuer's side. Ask the customer to contact their card-issuing bank to find out why.

<div class="grid cards" markdown>

- :lucide-shield-check:{ .lg }
  [__Set Up Credit Card 3D Secure Thresholds__](../payments-and-logistics/setup-credit-card-3d-verification.md){ title="Set Up Credit Card 3D Secure Thresholds" }

</div>

---

### ECPay Shipping Label Download Errors { #specs-payment-failed-ecpay-logistics }

If an error occurs when downloading ECPay shipping labels, a common cause is that the withdrawable balance in your ECPay account doesn't cover the shipping fee, so the logistics order can't be created. Top up prepaid logistics funds in the ECPay admin and download again.

---

### Market America (Shop.com) Referral Orders { #specs-payment-failed-shopcom }

!!! note "Important"
    If you use Market America (Shop.com) referrals, orders with failed payments still count toward commission. Be sure to "Cancel Order" for failed Market America orders so the system cancels them with Market America and removes them from commission.

---

## FAQ { #faq-payment-failed }

??? quote "Can customers pay again on their own for orders with failed payments?"
    [](){ #faq-payment-failed-customer-retry }
    Yes. Copy the checkout page link from the payment status section of the [order details page](#operate-payment-failed-resend-link){ title="Handle Orders with Failed Payments" } and send it to the customer. Opening it takes them back to the checkout page to pay again. If the payment failed during checkout, they can also retry on that page.

??? quote "How many automatic reminders are sent, and how often?"
    [](){ #faq-payment-failed-reminder-times }
    The system sends reminders at the interval you entered in [failed payment reminder settings](#operate-payment-failed-reminder){ title="Handle Orders with Failed Payments" }, up to three times.

    - For example, with 3 days set, an order placed on January 1 gets a reminder on January 4, 7, and 10.
    - Cash on Delivery orders aren't included in reminders.

??? quote "Are orders with failed payments canceled automatically?"
    [](){ #faq-payment-failed-auto-cancel }
    Yes. As long as you've set the [automatic order cancellation](#operate-payment-failed-cancel){ title="Handle Orders with Failed Payments" } days (default 7 days), orders still unpaid after that many days, including orders with failed payments, are canceled automatically. Set the days to 0 to turn off automatic cancellation.

??? quote "Can customers recharge a failed subscription charge on their own?"
    [](){ #faq-payment-failed-recurring }
    No. When a subscription sub-order charge fails, customers can't do anything on their side. You need to click "Recharge" in the [subscription order list](#operate-payment-failed-recurring-recharge){ title="Handle Orders with Failed Payments" }.

??? quote "Do Market America orders with failed payments need special handling?"
    [](){ #faq-payment-failed-shopcom }
    Yes. Market America orders with failed payments still count toward commission. Be sure to "Cancel Order" for those orders so the system cancels them with Market America and removes them from commission.

---

## References { #reference-payment-failed }

* [Order Payment Status Reference](references/payment-statuses.md#payment-statuses){ title="Order Payment Status Reference" data-preview }
