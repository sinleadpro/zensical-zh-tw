---
title: "Send Customers a Payment Link"
description: "When an order isn't paid yet, you can send a payment link so the customer can check out online again, without canceling and recreating the order."
created:
last_modified: 2026-07-22 15:49
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/provide-payment-link/"
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
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans:
  - Professional
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 提供付款連結
  - 引導顧客付款
  - 處理付款失敗
  - 重新產生條碼
features:
  - 付款連結取得
  - 付款連結複製
  - 付款方式支援
  - 連結時效性
  - 信用卡付款
  - 電子錢包
  - 超商條碼
prerequisites: []
related:
  - ec/orders/order-settings/unpaid-reminder-settings/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
tags:
  - "Payment Links"
  - "Order Payment"
  - "Payment Failed"
  - "Convenience Store Barcode"
  - "Credit Card Payment"
  - E-Wallets
  - "Order Management"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單 > 訂單明細 > 貨款
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12784
  - https://www.cyberbiz.io/support/?p=23826
comments: false
search:
  exclude: false
icon: lucide/link
hide:
---

![Payment link location](../../../assets/images/ec-訂單明細-付款連結.en.png){ title="Payment Link Location" .hero-page }

## About Payment Links

When a customer doesn't pay right away when ordering, or payment fails because of a credit card authorization failure or similar, you can send a payment link so the customer can pay again without canceling and placing a new order.

!!! example "Use Cases"

    - **Failed payments**: When the order status shows "Payment Failed," send this link so the customer can try paying again.
    - **Expired convenience store barcodes**: If the order was automatically canceled for "Payment Timeout," or the barcode expired because of the automatic update every 3 hours, send the link again so the customer can get a new barcode.

## Prerequisites and Limitations

- [x] **Order editing limits**:

	- For orders that aren't cash on delivery, if you **edit the order items or amount** before the customer pays, the storefront payment link still charges **the original amount before editing**.

	- If editing creates a difference, arrange the extra payment or refund with the customer yourself. The system doesn't handle the difference through the link.

- [x] **Link validity**: If you set a number of days for automatic order cancellation (such as canceling orders unpaid after 3 days), the payment link stops working after the system cancels the order.


## Get the Payment Link

1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders** from the left menu.
2. Click the order number to open the **order details page**.
3. In the **Payment** section of the page, find the **Payment Link** field.
4. Copy the link and send it to the shopper by email, text message, or a messaging app.

![Payment link process](../../../assets/images/ec-訂單-付款連結頁面.en.gif){ title="Payment Link Process" }

## Payment Methods Supported by Payment Links

The link opens a checkout page for that order, where customers can pay with:

- **Credit card** (one-time payment).

- **E-wallets**: Such as LINE Pay and JKOPAY.

- **Convenience store barcode payment**: If you turned on this feature, customers can get a barcode on the link page and pay at 7-Eleven or FamilyMart.


## Related Tasks

<div class="grid cards" markdown>

- :lucide-bell:{ .lg }  
  [__Unpaid Reminder Notifications__](unpaid-reminder-settings.md){ title="Set Up Unpaid Reminders" }  
  Set up automated notifications that send unpaid reminders on a schedule, guiding customers to complete checkout through the link in the message.

- :lucide-ban:{ .lg }  
  [__Logistics Restrictions and Exclusions__](../../products/shipping/cvs-shipping-restrictions-exclusions.md){ title="Set Up Convenience Store Delivery Restrictions and Logistics Exclusions" }  
  Set product delivery conditions to limit which delivery types appear and can be used at checkout.

</div>

## FAQ

??? quote "Can a payment link be reused?"

	Yes. Until the order is paid and as long as the system hasn't automatically canceled it, you can send the payment link to the customer any number of times.

??? quote "Does a payment link expire?"

	The payment link itself has no fixed expiration, but it stops working when:

	- The system automatically cancels the order (for example, if set to cancel after 3 days unpaid).

	- You cancel the order manually.


	Once the order status changes to "Canceled," the payment link can't be used.

??? quote "Can the payment link be used again after the customer pays?"

	No. After the order is paid, the payment link expires and can't charge again.

??? quote "Can customers change the payment method through the payment link?"

	Yes, but only to payment methods the order originally supports. On the payment link page, customers can choose a different payment method within what the system allows (for example, from credit card to an e-wallet).

??? quote "Do payment links support installments or other special payment methods?"

	Payment links support only the online payment methods turned on for your site. Whether credit card installments, specific e-wallets, or other payment methods are supported depends on your payment settings in the admin.

??? quote "If I change the order amount, does the payment link update automatically?"

	No. For orders that aren't cash on delivery:

	- If you edit the order amount or items before the customer pays,

	- the payment link still charges "the original amount before editing."

	The system doesn't sync amount changes automatically, so you need to settle the difference with the customer yourself.

??? quote "Why is the convenience store barcode different after it's generated again through the payment link?"

	Convenience store barcodes are time-limited, so the system updates them regularly (such as every 3 hours). When the customer opens the checkout page again through the payment link, the system generates a new valid barcode for payment.

??? quote "Do payment links work for all order statuses?"

	No. Payment links work only for orders that are:

	- Not yet paid

	- Not canceled


	If the order is paid, canceled, or closed, the payment link can't be used.
