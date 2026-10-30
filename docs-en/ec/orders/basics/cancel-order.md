---
title: "How to Cancel an Order"
description: "Covers three ways to cancel an order: manual cancellation by the merchant, cancellation by members on the storefront, and automatic cancellation by the system (payment timeout), including cancellation conditions, steps, and how bonus points and discounts are handled afterward"
created: 2026-05-04 12:24
last_modified: 2026-07-13 11:32
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
  - 取消訂單
  - 設定訂單自動取消
features:
  - 訂單取消
  - 訂單自動取消
prerequisites: []
related:
  - ec/orders/order-return-process/
  - ec/orders/order-refund-process/
  - ec/orders/basics/order-management-interface/
  - pos/orders/manage-general-orders/
tags:
  - "Cancel Order"
  - "Order Management"
  - "Automatic Cancellation"
  - "Payment Timeout"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=174
  - https://www.cyberbiz.io/support/?p=52159
permalink: "https://help.cyberbiz.io/ec/orders/basics/cancel-order/"
comments: false
search:
  exclude: false
icon: lucide/circle-x
hide: []
---

![Order details page: cancel order](../../../assets/images/EC-訂單詳情頁-取消訂單-hero.en.png){ title="Order Details Page: Cancel Order" .hero-page }

## About Canceling Orders { #intro-cancel }

"Cancel Order" stops an order that has been placed but hasn't entered the shipping process, ending further payment and logistics processing.

## Prerequisites and Limitations { #prerequisites-cancel }

- [x] **Delivery status limit**: Only orders with the delivery status "**Unshipped**" can be canceled.
    *   If the order is "Preparing," change it back to "Unshipped" before canceling.
    *   If the order is already "Shipped," it can't be canceled. Use the [return](../order-return-process.md){ title="Order Return and Refund Process" } and [refund](../order-refund-process.md){ title="Refund Methods and Operations" } processes instead.
- [x] **Whole order only**: The system supports **canceling the whole order** only, not partial cancellation.
- [x] **Irreversible**: After you click the cancel button, the order status changes to "Canceled," and this usually **can't be undone** (except in certain payment failure cases).

## Steps { #operate-cancel }

There are three ways an order can be canceled. Choose the one that fits your situation.

### Cancel an Order Manually { #orders-cancel-merchant }

=== ":lucide-receipt: Regular Orders"

    1.  **Open the order details page**: In the admin, go to "**Orders**" > "**All Orders**" and click the order number to open the order details page.
    2.  **Click the cancel button**: Click the red "**Cancel Order**" button in the upper-right corner.

        ![Order details page: cancel order](../../../assets/images/EC-訂單詳情頁-取消訂單.en.png){ title="Order Details Page: Cancel Order" }

    3.  **Set cancellation options**: In the dialog, set the following:
        - **Cancellation reason**: Required. Select a reason from the drop-down menu (such as out of stock, customer request, or duplicate order).
        - **Send notification email**: If selected, the system sends a cancellation email to the customer.
        - **Flag account**: If selected, the customer's account is flagged for future reference.

        ![Confirm cancellation: regular order](../../../assets/images/EC-訂單詳情頁-取消訂單-確認視窗.en.png){ title="Confirm Cancellation: Regular Order" }

     4.  **Confirm cancellation**: Click "**Cancel This Order**," and the order status changes to "Canceled."

    !!! success "Automatic Processing After Cancellation"

        After cancellation, the system automatically:

        - Returns bonus points
        - Returns coupons
        - Adds the product inventory back

=== ":simple-stryker: Shop.com Orders"

    Canceling a Shop.com order also requires notifying the Shop.com system, so the process is slightly different from regular orders.

       1.  **Open the order details page**: In the admin, go to "**Orders**" > "**All Orders**" and click the order number to open the order details page.  
       2.  **Click the cancel button**: Click the red "**Cancel Order**" button in the upper-right corner.
       3.  **Set cancellation options**: In the dialog, set the following:  
           - **Cancellation reason**: Required. Select a reason from the drop-down menu.
           - **Send notification email**: If selected, the system sends a cancellation email to the customer.  
           - **Flag account**: If selected, the customer's account is flagged.  
           - **Cancel order with Shop.com**: If selected, the system also sends a cancellation request to Shop.com (SHOP.COM).  
           - **Refund amount**: Enter the amount to refund to the customer (gift value not included).
       4.  **Confirm cancellation**: Click "**Cancel This Order**." The order status changes to "Canceled," and the Shop.com sync status changes to "Cancellation Processing."

    ??? info "Shop.com Sync Statuses"
        After the cancellation request is sent, the system syncs with the Shop.com API in the background:  

        | Status | Description |  
        |------|------|
        | Cancellation Processing | Waiting for the Shop.com API response |  
        | Cancellation Successful | Shop.com confirmed the cancellation |  
        | Cancellation Failed | The API call failed; the system retries automatically (up to 3 times, then again the next day) |  

    ??? warning "Resend a Shop.com Cancellation Manually"  
        If you didn't select "Cancel order with Shop.com" when canceling, or a network issue caused the sync status to show "Cancellation Failed," follow these steps to resend the information to Shop.com manually:

        1. **Open the order details page**: In the admin, go to "Orders" > "Shop.com Orders" and click the number of the canceled order.
        2. **Start the resend**: In the upper-right corner of the order details page, click "Cancel Order with Shop.com."
        3. **Confirm the cancellation details**: In the dialog, confirm the cancellation amount (the system fills in the amount excluding shipping).

        *Requirements: The order must be "Canceled," and the Shop.com sync status must not be "Cancellation Successful."*

        ![Shop.com order: resend cancellation manually](../../../assets/images/EC-美安訂單-補送取消訂單.en.png){ title="Shop.com Order: Resend Cancellation Manually" }

---

### Customer Cancels on the Storefront { #orders-cancel-customer }

[:lucide-layout-dashboard:{ title="Applicable Features" }](../../../resources/conventions.md#conventions-features) | Drag-and-Drop Themes

You can choose whether customers can cancel unshipped orders themselves on the storefront. If this is turned off, customers can only [ask you to cancel](#orders-cancel-merchant).

**Setup**

Turn on this feature in the admin first:

1. **Open the settings page**: In the admin, go to "Payment and Logistics" > "Checkout Page & Logistics."
2. **Turn on the feature**: Find and expand the "Customer Order Cancellation Settings" section and select "Customers Can Cancel Orders."
3. **Save the settings**: Click "Save" at the bottom of the page. The setting takes effect immediately.

![Customer order cancellation and return request settings](../../../assets/images/EC-金物流-結帳頁物流設定-顧客取消訂單申請退貨.en.png){ title="Customer Order Cancellation and Return Request Settings" }

---

**Customer Steps**

After the feature is turned on, customers can:

1. **Find the order**: Sign in to the website as a member and go to "My Account" > "Order Lookup."

    ![Order lookup path](../../../assets/images/EC-前台-訂單查詢路徑.en.png){ title="Order Lookup Path" }

2. **Click cancel**: Next to an order with the delivery status "Unshipped," click "Cancel Order."

    ![Cancel order on the storefront](../../../assets/images/EC-前台-訂單查詢-取消訂單.en.png){ title="Cancel Order on the Storefront" }

    !!! info "Limitations"
        - Only orders with the delivery status "**Unshipped**" can be canceled.
        - If the order is "Preparing" or "Shipped," customers can't cancel it themselves and need to contact customer service.

3. **Confirm cancellation**: Check the information in the dialog and click "Confirm Cancellation."

    ![Confirm order cancellation](../../../assets/images/EC-前台-訂單查詢-取消訂單-確認視窗.en.png){ title="Confirm Order Cancellation" }

4. **Done**: The order status changes to "Canceled" immediately, the system runs the follow-up processing ([points/inventory return](#post-cancel)), and the [order activity log](order-management-interface.md#order-history){ title="Order Management Interface" } records that the member canceled and why.

    ![Order canceled](../../../assets/images/EC-前台-訂單查詢-已取消訂單.en.png){ title="Order Canceled" }


---

### Automatic Cancellation by the System <small>Payment Timeout</small> { #orders-cancel-auto }

To keep unpaid orders from holding inventory for too long, you can set a "payment deadline." When an order meets [certain conditions](#orders-cancel-auto-rules) and remains unpaid [past the deadline](#orders-cancel-auto-mechanism), the system automatically changes the order status to "Canceled."

**Steps**:

1.  **Open the settings page**: In the admin, go to "**Payment and Logistics**" > "**Checkout Page & Logistics**" and find the "**Automatic Order Cancellation**" section.
2.  **Set the payment deadline**: Enter the number of days (1-29) in "**Cancel automatically after X days**."
    - If set to `0` days, the feature is turned off.
    - If not set or set to more than 29 days, virtual ATM accounts are valid for a maximum of 29 days.
3.  **Save the settings**: Click "**Save**" at the bottom of the page, and the setting takes effect.
    - Once in effect, the rule applies to all unpaid orders, whether placed before or after the setting.
4.  **Check the activity log** (optional): After cancellation, you can see the cancellation information the system recorded in the "[Activity Log](order-management-interface.md#order-history){ title="Order Management Interface" }" section of the order details page, for reconciliation and customer service.

![Automatic order cancellation settings](../../../assets/images/EC-金物流-結帳頁物流設定-訂單自動取消.en.png){ title="Automatic Order Cancellation Settings" }

---

#### Rules and Conditions { #orders-cancel-auto-rules }

The system cancels only orders that meet all of these conditions:

- **Payment status**: Awaiting Payment
- **Delivery status**: Unshipped or No Shipping Needed
- **Payment method**: Not "Cash on Delivery."
- **Scope**: After you save the setting, unpaid orders placed before it are also affected.

---

#### How the System Runs { #orders-cancel-auto-mechanism }

The system scans and cancels orders in a batch every day at 01:00 AM.

!!! example "Cancellation Example"
    If set to cancel after 3 days:

    - **1/1 12:00 PM**: The customer places the order, and the 3-day countdown starts.
    - **1/4 12:00 PM**: 72 hours (3 days) have passed, and the order can be canceled.
    - **1/5 01:00 AM**: The system runs the batch check and cancels the order.

---

#### Online Payment Expiration <small>Virtual ATM / Convenience Store Code</small> { #orders-cancel-payment-code-expiry }

For payment methods that use a code, the "payment deadline" depends on the number of days set in the admin:

| Order Time | Day 1 Starts | Deadline Example (Set to 3 Days) |
| :--- | :--- | :--- |
| **00:00 - 00:59** | The order day is day 1 | Ordered 3/18 00:15 → due **3/20 23:59** |
| **After 01:00** | The next day is day 1 | Ordered 3/18 01:15 → due **3/21 23:59** |

!!! warning "Important Notes"

    - **Maximum**: If you don't set cancellation days or set more than 29 days, virtual ATM accounts are valid for a maximum of 29 days (until 23:59).
    - **Manual cancellation exception**: If you or a member cancels an order "manually," codes/accounts already created don't expire automatically. If the customer pays within the validity period, the order changes back to "In Progress," and you can continue shipping or issue a refund.

## Bonus Points and Discounts After Cancellation { #post-cancel }

*   **Bonus points**: After an order is canceled, the system **automatically returns** the bonus points the customer redeemed in the order to their account.
    *   *Note*: If the order was closed and bonus points were already issued, the system doesn't automatically deduct the earned bonus points after cancellation. You need to remove them manually.
*   **Coupons**: Coupons used in the order are also **automatically returned** to the customer.
*   **Inventory**: After cancellation, product inventory is **automatically added back**.

## Special Cases { #special-cancel }

<div class="grid cards" markdown>

- :lucide-barcode:{ .lg } [__Virtual ATM and Convenience Store Codes__](#orders-cancel-payment-code-expiry)  

- :simple-stryker:{ .lg } [__Shop.com Orders__](#stryker-美安訂單)  

<!-- - :lucide-repeat:{ .lg }   -->
<!--   __Subscription Orders__   -->
<!--   You can cancel the whole "parent order" or a single "sub-order." Canceling the parent order stops all future deliveries. -->
<!---->
<!-- - :material-point-of-sale:{ .lg }   -->
<!--   __POS Orders__   -->
<!--   For in-store orders, find the order on the POS front end and run "[Cancel Order](../../../pos/orders/manage-general-orders.md#取消訂單)." If an invoice was issued, the system voids it or creates an allowance based on the cancellation time. -->

</div>

## Next Steps { #next-steps-cancel }

<div class="grid cards" markdown>

- :lucide-receipt:{ .lg }  
  [__Refund Methods and Operations__](../order-refund-process.md){ title="Refund Methods and Operations" }  
  If the order was paid, follow the refund process after cancellation to return the payment to the customer.

- :lucide-package-minus:{ .lg }  
  [__Order Return and Refund Process__](../order-return-process.md){ title="Order Return and Refund Process" }  
  If the order has shipped and can't be canceled, use the return process to get the items back and refund.

- :lucide-file-text:{ .lg }  
  [__Order Activity Log__](order-management-interface.md#order-history){ title="Order Management Interface" }  
  See the history of order status changes and who made them, for reconciliation and customer service.

</div>

## FAQ { #faq-cancel }

??? quote "Why can't members see the cancel order button on the storefront?"

    Possible reasons:

    - "Customer Order Cancellation Settings" isn't turned on in "Payment and Logistics" > "Checkout Page & Logistics"
    - The order's delivery status isn't "Unshipped"
    - The website doesn't use a "drag-and-drop theme"; this feature works only with drag-and-drop themes

??? quote "Is the virtual ATM account still valid after the system cancels the order automatically?"

    If you cancel an order "manually," codes/accounts already created don't expire automatically. If the customer pays within the validity period, the order changes from "Canceled" back to "In Progress," and you can continue shipping or issue a refund.

??? quote "After canceling a Shop.com order, how do I confirm Shop.com has synced?"

    After the cancellation request is sent, check the Shop.com sync status on the order details page:

    - **Cancellation Processing**: Waiting for the Shop.com API response
    - **Cancellation Successful**: Shop.com confirmed the cancellation
    - **Cancellation Failed**: The API call failed; the system retries automatically (up to 3 times, then again the next day)

