---
title: "Use 7-Eleven C2C Return Service"
description: "Turn on 7-Eleven C2C Return Service, set up recipient details, send return drop-off codes to shoppers, and complete return review and refunds."
created: 2026-05-26 12:25
last_modified: 2026-07-06 17:13
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
cyb_extensions:
  - CYBERBIZ PAYMENTS
intents:
  - 使用 7-11 C2C 退貨便退貨
features:
  - 7-11 C2C 退貨便
prerequisites:
  - 需先向 CYBERBIZ 客服申請開通「7-ELEVEN C2C 退貨便」加值功能
related:
  - ec/orders/references/c2c-return-conditions/
  - ec/website-management/setup-store-basic-info/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/orders/order-return-process/
  - ec/orders/order-refund-process/
tags:
  - "7-Eleven C2C Return Service"
  - "Return Process"
  - "Convenience Store Returns"
  - EC
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 超商物流
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12993
  - https://www.cyberbiz.io/support/?p=5246
permalink: "https://help.cyberbiz.io/ec/orders/returns-refunds/7-11-c2c-return/"
comments: false
search:
  exclude: false
icon: lucide/undo-2
hide: []
---

![7-Eleven C2C send return service code](../../../assets/images/EC-訂單-所有訂單-發送7-11-c2c退貨便代碼-hero.en.png){ .hero-page }

## About 7-Eleven C2C Return Service

This feature lets customers send returned items back through 7-ELEVEN stores. The original order doesn't need to use convenience store pickup; you can receive return packages through this service for orders with any delivery method.


## Prerequisites and Limitations { #prerequisites-seven-eleven-c2c-return }


An order must meet all of the following conditions before you can send a return code from the order list:

- [x] **Order amount**: The order total must be less than **NT$20,000** (the system blocks orders over the limit)
- [x] **Delivery method**: Orders with a single delivery method (split orders with multiple delivery methods aren't supported)
- [x] **Return status**: The order must be "No Return Needed," "Return Requested," or "Returning"
- [x] **Delivery status**: CYBERBIZ logistics orders must be "Shipped / Arrived / Received"; other logistics orders must be "Shipped"
- [x] **Recipient information**: Merchant recipient information is set up in "Payment and Logistics > Convenience Store Logistics > 7-ELEVEN C2C Return Service"

For the full "delivery method × delivery progress × return status" matrix and details on each field, see [Conditions for Sending](../references/c2c-return-conditions.md){ title="7-Eleven C2C Return Service: Conditions for Sending" }.

## Steps { #operate-seven-eleven-c2c-return }

### 1. Enable and Set Up Recipient Information { #operate-seven-eleven-c2c-return-setup }

After enabling the feature, fill in the "Recipient Settings" so the system can generate shipping labels correctly when sending return codes.

1. **Open the settings page**: In the admin, go to **"Payment and Logistics/Convenience Store Logistics" > "7-ELEVEN C2C Return Service"** and click **Edit** :lucide-file-pen-line:.
2. **Enable the setting**: Select the checkbox to agree to enable the feature and click **Confirm**.
2. **Choose the recipient store**: Click **"Choose Store"** (shown as **"Change Store"** if already set). The official 7-ELEVEN store map window opens. After you choose a store, the system fills in the **Store Number** and **Store Name** automatically (these two fields can't be edited manually).
3. **Enter recipient information**: Enter **Name**, **Phone**, and **Email** in order[^1].
4. **Save settings**: Check the information and save.

![7-Eleven C2C return service settings](../../../assets/images/EC-金物流-7-11-c2c退貨便.en.png)

[^1]: Be sure to enter your real name **exactly as it appears on your ID**, because store staff check your ID when you pick up return packages. We recommend a mobile phone number so you can receive "package arrived at store" text notifications from the system.

---

### 2. Send the Return Code to the Customer { #operate-seven-eleven-c2c-return-send-code }

When a customer requests a return, you can generate a code for them from the order list page.

1. **Go to the order list**: In the admin, go to **"Orders" > "All Orders"**.
2. **Select the order to return**: Make sure the order meets the conditions in [Prerequisites and Limitations](#prerequisites-seven-eleven-c2c-return){ data-preview }.
3. **Choose the bulk action**: In More Actions above the orders, select **"Send 7-Eleven C2C Return Code and Change Delivery Status to 'Returning'"**.

    ![Send 7-Eleven C2C return service code](../../../assets/images/EC-訂單-所有訂單-發送7-11-c2c退貨便代碼.en.png)

4. **Choose notification methods**: The **Send 7-11 C2C Return Service code** window opens with the message "After the code is sent, the delivery status changes to 'Returning'," and offers two notification methods (select at least one to submit):
    * **Notify the customer by text**: Each text costs CYBER Coins. The system sends the code to the mobile number the customer entered when ordering.
    * **Notify the customer by email**: No extra charge. The shipping label PDF is attached to the email so the customer can print it.

    ![Send 7-Eleven C2C return service code - confirmation window](../../../assets/images/EC-訂單-所有訂單-發送7-11-c2c退貨便代碼-確認視窗.en.png)

5. **Confirm and submit**: After you confirm, the system immediately:
    * Holds CYBER Coins for the return shipping fee
    * Gets a 7-ELEVEN return code
    * Sends the code and shipping label to the customer by the selected notification methods
    * Changes the order's delivery status to **Returning**

!!! tip "Code Validity"
    The return service code is valid for **7 days** from the day it's requested and then expires automatically. If the customer still hasn't sent the package with the code within 2 weeks, the system cancels the code automatically and returns the held CYBER Coins.

---

### 3. How Customers Send Packages (For Reference) { #operate-seven-eleven-c2c-return-customer }

You can use this to explain the sending process to customers:

1. **Use the text code**: The customer goes to a 7-ELEVEN store, selects **"Delivery Service/Send/ibon Send" > "Enter Code"** on the ibon kiosk, enters the code from the notification, and prints the shipping label.
2. **Use the email shipping label**: The email notification includes a shipping label PDF the customer can print and stick on the outside of the box.
3. **Drop off at the counter**: The customer hands the labeled package to 7-ELEVEN staff to finish sending it. **No payment is needed at the counter**.

---

### 4. Merchant Pickup and Store Closures { #operate-seven-eleven-c2c-return-pickup }

1. **Package arrival notice**: When the package arrives at your recipient store, the system sends a text to the phone number you set.
2. **Pick up at the store**: Pick up the package **within 7 days** of arrival, bringing **an original ID matching the "Name" field**. If you don't pick it up in time, the package is returned automatically by **freight-collect home delivery** to the "[company logistics address](../../website-management/setup-store-basic-info.md#operate-general-preferences-return-address){ title="Set Up Basic Website Information" }" (you pay the home delivery fee).
3. **If a store closes**:
    * **Store closed before the code is sent**: Return to the "Payment and Logistics > Convenience Store Logistics > 7-ELEVEN C2C Return Service" settings page, choose a new store, and send the code again.
    * **Store closed after the package was sent**: Open the order's **order details page**. The system shows a warning and a **"Choose Store Again"** button below the logistics information section. Choose a new recipient store **within 6 days** of the closure[^2]; otherwise, the package is returned by freight-collect home delivery to the company logistics address.

        ![Order details page - 7-Eleven C2C store closure](../../../assets/images/EC-訂單-所有訂單-訂單詳情頁-7-11-c2c-門市關轉.en.png)

[^2]: The option to choose a new store appears only when all three conditions are met: "the store is closed, a new store hasn't been chosen, and the closure was within 6 days." After 6 days, the button disappears automatically.

---

### 5. Return Review and Refund { #operate-seven-eleven-c2c-return-refund }

1. **After the package is signed for**: After you pick up the package at the store and it's signed for in the system, the order's return status changes to **Reviewing Return** automatically.
2. **Check the items**: Check each item's condition. If you confirm the refund, select the order on the order list page and choose the bulk action **Returned** to mark the return complete.
3. **Issue the refund**:
    * **CYBERBIZ PAYMENTS orders**: The system starts a card refund or manual refund process based on the original payment method. Follow the instructions in the admin.
    * **Other payment orders**: Issue the card refund in the original payment provider's admin, or ask the customer for account information and send the money yourself. Then manually mark the payment status as "Refunded" on the order details page.

## Important Rules and Limitations { #specs-seven-eleven-c2c-return }

* **Only one return request per order**: Orders already marked "Returning," "Reviewing Return," or "Returned" can't be sent another return service code.
* **NT$20,000 limit**: This is a hard limit of the 7-ELEVEN logistics system. Orders over this amount need another return method (such as home delivery).
* **No other carriers**: This service only returns to 7-ELEVEN stores. You can't specify another convenience store brand.
* **No partial returns**: The whole order is handled with one return code. If only some items are returned, work out the actual refund amount with the customer.
* **7-day code validity / 7-day pickup period**: Customers must send the package at a store within 7 days of the code being generated; you must pick it up within 7 days of arrival, or it's returned by freight-collect home delivery.

## Next Steps { #next-steps-seven-eleven-c2c-return }

<div class="grid cards" markdown>

- :lucide-truck:{ .lg }  
  [__Partial Shipment__](../home-delivery/partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }  
  If you need to ship the remaining items again after a return, see the partial shipment process.

- :lucide-settings:{ .lg }  
  [__Set Up Basic Website Information__](../../website-management/setup-store-basic-info.md#operate-general-preferences-return-address){ title="Set Up Basic Website Information" }  
  Return packages not picked up in time are returned to this address by freight-collect home delivery, so make sure it's correct.

- :lucide-check-circle:{ .lg }  
  [__Return Review and Refunds__](../order-return-process.md){ title="Order Return and Refund Process" }  
  After the package is signed for, the system changes it to "Reviewing Return." Check each item's condition, then start a card refund or manual refund based on the original payment method.

- :lucide-credit-card:{ .lg }  
  [__Refunds for Other Payment Methods__](../order-refund-process.md){ title="Refund Methods and Operations" }  
  For orders not using CYBERBIZ PAYMENTS, issue the card refund in the original payment provider's admin, or ask the customer for account information and send the money yourself.

</div>

## FAQ { #faq-seven-eleven-c2c-return }

??? quote "Why can't I find "Send 7-Eleven C2C Return Code" in the order list bulk actions?"
    [](){ #faq-seven-eleven-c2c-return-action-missing }
    Check the following in order:

    - Whether your store has asked CYBERBIZ customer service to enable "7-ELEVEN C2C Return Service"
    - Whether the selected orders meet all sending conditions; see [Conditions for Sending](../references/c2c-return-conditions.md){ title="7-Eleven C2C Return Service: Conditions for Sending" }
    - Whether you selected orders with different statuses (bulk actions require all selected orders to have the same status)

??? quote "When are CYBER Coins deducted? Are they deducted if the customer doesn't send the package?"
    [](){ #faq-seven-eleven-c2c-return-cyber-charge }
    The system holds CYBER Coins for the return shipping fee as soon as you click **"Confirm"** to send the return code. If the customer doesn't send the package at a store with the code within 2 weeks, the system cancels the code automatically, returns the held CYBER Coins to your account, and records the refund details in the notes.

??? quote "What happens if I forget to pick up the return package at the store?"
    [](){ #faq-seven-eleven-c2c-return-pickup-overdue }
    If the package isn't picked up within 7 days of arrival, the system returns it by **freight-collect home delivery** to the address set in "General Settings > Company Logistics Address", **with the home delivery fee paid by you**.

??? quote "Can I use OK Mart, FamilyMart, Hi-Life, or other convenience stores for returns?"
    [](){ #faq-seven-eleven-c2c-return-other-cvs }
    The C2C return code feature in the CYBERBIZ admin currently supports only 7-ELEVEN. For other convenience store brands, the customer needs to send the package back themselves (fees follow each store's rules).

??? quote "Why can't I type in the Store Number and Store Name fields when setting up the recipient?"
    [](){ #faq-seven-eleven-c2c-return-store-readonly }
    These two fields are filled in by the system. Click **"Choose Store"** (or **"Change Store"** if already chosen) and pick a store from the official 7-ELEVEN store map window. The system fills in the correct store number and name automatically to prevent typos that would cause shipping to fail.

??? quote "What if the 7-ELEVEN store suddenly closes after the package is sent?"
    [](){ #faq-seven-eleven-c2c-return-store-closed }
    Open the order's details page. The system shows a notice and a **"Choose Store Again"** button below the logistics information section. Choose a new store **within 6 days** of the closure. After 6 days, the option disappears, and the package is returned by freight-collect home delivery to the company logistics address.

## References { #reference-seven-eleven-c2c-return }

- [Conditions for Sending](../references/c2c-return-conditions.md){ title="7-Eleven C2C Return Service: Conditions for Sending" data-preview }
- [7-ELEVEN Delivery Service Official Guide](https://www.7-11.com.tw/service/accept.aspx){ target="_blank" }


