---
title: "Pay with a Convenience Store Barcode"
description: "Turn on convenience store barcode payment, and see how customers get a barcode and pay at 7-Eleven or FamilyMart."
created: 2026-05-04 10:27
last_modified: 2026-06-30 09:30
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - modularize 啟用超商條碼 step 1 into a section in cyberbiz payments doc
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
  - "CYBERBIZ PAYMENTS"
intents:
  - 使用超商條碼繳費
  - 開啟超商條碼付款功能
features:
  - 超商條碼繳費
  - CYBERBIZ PAYMENTS
prerequisites: []
related:
  - ec/payments-and-logistics/payments/order-settings/
  - ec/notifications/manage-email-templates/
  - ec/orders/order-settings/provide-payment-link/
  - ec/orders/order-settings/unpaid-reminder-settings/
tags:
  - "Convenience Store Barcode"
  - "Convenience Store Payment"
  - CYBERBIZ PAYMENTS
  - 7-Eleven
  - FamilyMart
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
  - https://www.cyberbiz.io/helpcenter/?p=12765
  - https://www.cyberbiz.io/support/?p=52159
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/cvs-barcode-payment/"
search:
  exclude: false
icon: lucide/barcode
hide: []
comments: false
---

![Convenience store barcode payment settings](../../../assets/images/EC-後台-金物流-金流設定-超商條碼繳費設定.en.png){ title="Convenience Store Barcode Payment Settings" .hero-page }

## About Convenience Store Barcode Payment

**Convenience store barcode payment** gives customers a unique barcode after they place an order on your website, so they can pay at a designated convenience store.

!!! info "Supported Stores"
    Barcode payment is currently supported only at **7-Eleven** and **FamilyMart**.

## Turn On Convenience Store Barcode Payment

You can turn on this feature through CYBERBIZ PAYMENTS so shoppers can generate a convenience store barcode at checkout and pay in store.

### Step 1: Edit the CYBERBIZ PAYMENTS Payment Settings

1.  Sign in to the CYBERBIZ admin and go to **Payment and Logistics > Payment Settings**.
2.  In the payment settings list, find **CYBERBIZ PAYMENTS**.
3.  Click the **Edit** :lucide-file-pen: button on the right to open the settings page.

![Edit CYBERBIZ PAYMENTS](../../../assets/images/EC-後台-金物流-金流設定-CYBERBIZ-PAYMENTS-編輯.en.png){ title="Edit CYBERBIZ PAYMENTS" .screenshot }

---

### Step 2: Turn On Convenience Store Barcode Payment

1.  On the CYBERBIZ PAYMENTS settings page, find **7-Eleven / FamilyMart Convenience Store Barcode Payment**.
2.  Switch the toggle to **Enable**.

![Turn on convenience store barcode payment](../../../assets/images/EC-後台-金物流-金流設定-開啟超商條碼繳費.en.png){ title="Turn On Convenience Store Barcode Payment" .screenshot }

---

### Step 3: Save the Settings

1.  After turning it on, click **Save** at the bottom of the page.
2.  After the system shows a success message, you can confirm in the payment settings list that the feature is on.

![Convenience store barcode payment turned on](../../../assets/images/EC-後台-金物流-金流設定-已開啟超商條碼繳費.en.png){ title="Convenience Store Barcode Payment Turned On" .screenshot }

!!! warning "Important"
    - After turning on convenience store barcode payment, make sure you also offer a supported delivery type (such as convenience store pickup) so shoppers can select this payment method at checkout.
    - If you set a day limit for "[Automatic Order Cancellation](../../payments-and-logistics/payments/order-settings.md#operate-order-settings-auto-cancel){ title="Order Settings" }," the barcode expires once the limit passes and can't be used to pay.
    - If you [cancel an order manually](../basics/cancel-order/#orders-cancel-merchant), the barcode doesn't expire automatically, and the customer can still pay within its validity period. After payment, the order is placed again, and you can continue shipping or issue a refund.

## How Customers Get the Barcode <small>Customer</small>

During and after ordering, customers can get the payment barcode in these ways:

1.  **Checkout page**: At checkout on your website, select "**Convenience Store Barcode**" as the payment method and submit the order.

    ![Payment method: convenience store barcode](../../../assets/images/EC-前台-購物車-付款方式-超商條碼.en.png){ title="Payment Method: Convenience Store Barcode" }

2.  **Order confirmation page**: After the order is placed, the page shows the barcode directly. You can keep this page open and show it to the store clerk to scan.

    ![Get the convenience store barcode](../../../assets/images/EC-前台-購物車-付款方式-取得超商條碼.en.png){ title="Get the Convenience Store Barcode" }

3.  **Order lookup page**: If you didn't pay right after ordering, sign in to the website as a member, go to "Order Lookup," and click "**Go to Payment**" for the order. The system takes you back to the order confirmation page and shows the barcode.

    ![Go to payment](../../../assets/images/EC-前台-訂單查詢-前往付款.en.png){ title="Go to Payment" }

4.  **Email notification**: If the merchant [turned on new order notifications](../../notifications/manage-email-templates.md){ title="Set Up and Manage Email Notification Templates" }, customers can click the "**Go to Payment**" button in the order confirmation email to get the barcode.

    ![Order confirmation email: go to payment](../../../assets/images/EC-Email通知-訂單成立-前往付款.en.png){ title="Order Confirmation Email: Go to Payment" }

## How to Pay at the Convenience Store <small>Customer</small>

After getting the barcode, go to a supported convenience store (**7-Eleven or FamilyMart**) to pay:

*   **No printing needed**: You don't need to print the barcode. Just show the barcode on your phone screen to the clerk to scan.
*   **Full screen and brightness**: We recommend tapping the barcode to open **full-screen mode** and setting your phone to **maximum screen brightness** so the store scanner can read it.
*   **Complete payment**: After the clerk scans the barcode and collects payment, the payment is complete.

!!! warning "Important Notes"
    - **Barcode validity**: The barcode **refreshes automatically every 3 hours**, and old barcodes expire. When you arrive at the store, reopen the live barcode from the website or email link. **Don't pay with an old barcode screenshot taken in advance.**
    - **Payment link**: If customers have trouble getting the barcode, they can also ask the merchant for a dedicated "[customer payment link](provide-payment-link.md){ title="Send Customers a Payment Link" }" to open the payment page again.

??? example "Convenience Store Barcode Example"
    ![Convenience store barcode example](../../../assets/images/EC-前台-訂單查詢-前往付款-超商條碼範例.en.png){ title="Convenience Store Barcode Example" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-clock:{ .lg }  
  [__Set Automatic Order Cancellation Rules__](../../payments-and-logistics/payments/order-settings.md#operate-order-settings-auto-cancel){ title="Order Settings" }  
  Set the number of days before unpaid orders are canceled automatically in "Payment and Logistics > Checkout Page & Logistics" to avoid problems with expired barcodes.

- :lucide-bell:{ .lg }  
  [__Set Up Unpaid Reminders__](unpaid-reminder-settings.md){ title="Set Up Unpaid Reminders" }  
  Turn on automatic email reminders for unpaid orders to help more customers complete payment.

- :lucide-link:{ .lg }  
  [__Send Customers a Payment Link__](provide-payment-link.md){ title="Send Customers a Payment Link" }  
  Get a dedicated payment link in the admin and send it to customers so they can pay right away.

</div>

## FAQ

??? quote "How long is a convenience store barcode valid?"

    The barcode **refreshes automatically every 3 hours**, and old barcodes expire. When you arrive at the store, reopen the live barcode from the website or email link.

??? quote "Can I take a screenshot of the barcode in advance and use it at the store later?"

    **Not recommended.** Because the barcode refreshes every 3 hours, an old screenshot may have expired, and the payment may fail. Open the live barcode after you arrive at the store.

??? quote "Can I still pay with the barcode after the automatic cancellation period passes?"

    No. If the merchant set a day limit for automatic order cancellation, the system cancels the order once the limit passes, and the barcode expires at the same time, so it can't be used to pay.

