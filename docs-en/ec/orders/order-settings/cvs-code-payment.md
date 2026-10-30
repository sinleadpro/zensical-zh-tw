---
title: "Pay with a Convenience Store Payment Code"
description: "Turn on convenience store payment codes, and see how customers get a payment code and print a payment slip at a 7-Eleven, FamilyMart, or Hi-Life kiosk to pay."
created: 2026-09-01 11:30
last_modified: 2026-09-01 12:29
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
  - 使用超商代碼繳費
  - 開啟超商代碼付款功能
features:
  - 超商代碼繳費
  - CYBERBIZ PAYMENTS
prerequisites:
  - ec/payments-and-logistics/apply-cyberbiz-payments/
related:
  - ec/payments-and-logistics/payments/order-settings/
  - ec/orders/basics/cancel-order/
  - ec/notifications/manage-email-templates/
  - ec/orders/order-settings/unpaid-reminder-settings/
tags: []
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/cvs-code-payment/"
search:
  exclude: false
icon: lucide/hash
hide: []
comments: false
---

![Convenience store payment code settings](../../../assets/images/EC-後台-金物流-金流設定-啟用超商條碼01.en.png){ title="Convenience Store Payment Code Settings" .hero-page }

## About Convenience Store Payment Codes

**Convenience store payment code** gives customers a payment code after they order on your website. They print a payment slip at the kiosk in a supported convenience store and then pay at the counter.

## Before You Start

- **Maximum per transaction**: NT$20,000
- **Payment deadline**: 7 days. After it expires, customers can get a new code.
- **Supported convenience stores**: 7-Eleven, FamilyMart, Hi-Life


## Turn On Convenience Store Payment Codes

You can turn on this feature in CYBERBIZ PAYMENTS so shoppers can choose a convenience store payment code at checkout and pay in store.

### Step 1: Edit the CYBERBIZ PAYMENTS Payment Settings

1.  Sign in to the CYBERBIZ admin and go to **Payment and Logistics > Payment Settings**.
2.  In the payment settings list, find **CYBERBIZ PAYMENTS**.
3.  Click the **Edit** :lucide-file-pen: button on the right to open the settings page.

![Edit CYBERBIZ PAYMENTS](../../../assets/images/EC-後台-金物流-金流設定-CYBERBIZ-PAYMENTS-編輯.en.png){ title="Edit CYBERBIZ PAYMENTS" .screenshot }

---

### Step 2: Turn On Convenience Store Payment Codes

1.  On the CYBERBIZ PAYMENTS settings page, find **Convenience Store Payment Code**.
2.  Turn the switch to **Enable**.

![Edit CYBERBIZ PAYMENTS](../../../assets/images/EC-後台-金物流-金流設定-啟用超商條碼02.en.png){ title="Edit CYBERBIZ PAYMENTS" .screenshot }

---

### Step 3: Save the Settings

1.  After you turn it on, click **Save** at the bottom of the page.
2.  After the system shows a success message, you can confirm the feature is on in the payment settings list.

!!! warning "Important"
    - After you turn on convenience store payment codes, make sure you also offer a supported delivery type (such as convenience store pickup) so shoppers can choose this payment method at checkout.
    - If you set a day limit for [automatic order cancellation](../../payments-and-logistics/payments/order-settings.md#operate-order-settings-auto-cancel){ title="Order Settings" }, the code expires once the limit passes and can no longer be used to pay.
    - If you [cancel an order manually](../basics/cancel-order/#orders-cancel-merchant), the convenience store payment code doesn't expire automatically, and the customer can still pay within its validity period. After payment, the order is placed again, and you can ship it or refund it.

## Get a Convenience Store Payment Code <small>Customer</small>

During and after ordering, customers can get the payment code in the following ways:

1.  **Select at checkout**: When checking out on your website, select **Paycode** as the payment method and submit the order.

    ![Payment method - convenience store payment code](../../../assets/images/EC-前台-結帳頁-使用超商條碼01.en.png){ title="Payment Method - Convenience Store Payment Code" }

2.  **Order confirmation page**: After ordering, the page shows the payment code. Write down the code, or keep this page open to use at the store.

    ![Get the convenience store code](../../../assets/images/EC-前台-結帳頁-使用超商條碼02.en.png){ title="Get the Convenience Store Code" }

3.  **Order lookup page**: If they didn't pay right after ordering, customers can sign in as members on your website, go to **Order Lookup**, and click **Go to Payment** for the order. The system takes them back to the order confirmation page and shows the code.

    ![Go to payment](../../../assets/images/EC-前台-訂單查詢-前往付款.en.png){ title="Go to Payment" }

4.  **Email notification**: If you [turned on new order notifications](../../notifications/manage-email-templates.md){ title="Set Up and Manage Email Notification Templates" }, customers can click **Go to Payment** in the order confirmation email they receive to get the code.

    ![Order confirmation email - go to payment](../../../assets/images/EC-Email通知-訂單成立-前往付款.en.png){ title="Order Confirmation Email - Go to Payment" }

## Pay at the Convenience Store <small>Customer</small>

After getting the code, go to a supported convenience store, enter the code at the kiosk, print the payment slip, and pay at the counter. For each store's kiosk, see the following:

<div class="grid cards" markdown>

- :lucide-monitor:{ .lg }  
  [__7-Eleven ibon__ :lucide-external-link:](https://www.ibon.com.tw/operate.aspx?fromPage=paymentcode.aspx&routeIDListInfo=4;100002;0,179#gsc.tab=0){ target="_blank" }  
  Enter the payment code at ibon, print the payment slip, and pay at the counter.

- :lucide-monitor:{ .lg }  
  [__FamilyMart FamiPort__ :lucide-external-link:](https://www.famiport.com.tw/Web_Famiport/page/fp_operating.aspx?MN=4&CN=1122){ target="_blank" }  
  Select code payment at FamiPort, print the payment slip, and pay at the counter.

- :lucide-monitor:{ .lg }  
  [__Hi-Life Life-ET__ :lucide-external-link:](../../../assets/docs/ec-cvs-life-et-code-payment-flow.pdf){ target="_blank" }  
  Select code entry payment at Life-ET, print the payment slip, and pay at the counter.

</div>


## Next Steps

<div class="grid cards" markdown>

- :lucide-clock:{ .lg }  
  [__Set Up Automatic Order Cancellation Rules__](../../payments-and-logistics/payments/order-settings.md#operate-order-settings-auto-cancel){ title="Order Settings" }  
  In Payment and Logistics > Checkout Page & Logistics, set the number of days before unpaid orders are canceled automatically, matching the convenience store payment code deadline.

- :lucide-bell:{ .lg }  
  [__Set Up Unpaid Reminders__](unpaid-reminder-settings.md){ title="Set Up Unpaid Reminders" }  
  Turn on automatic email reminders for unpaid orders to raise the rate of customers who complete payment.

</div>
