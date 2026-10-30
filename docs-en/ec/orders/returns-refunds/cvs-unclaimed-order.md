---
title: "Handle Unclaimed Convenience Store Orders"
description: "How to handle unclaimed convenience store orders, including automatic refund conditions, return methods for B2C bulk shipping and store-to-store, and manual refund steps."
created: 2026-05-26 20:51
last_modified: 2026-07-09 11:51
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - 缺hero圖，沒有逾期未取訂單
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
  - 了解超商訂單逾期未取處理流程
  - 執行人工退款
  - 了解自動退款條件
features:
  - 超商逾期未取
  - 自動退款
  - 人工退款
  - 部分出貨退款
prerequisites: []
related:
  - ec/orders/references/auto-refund-timeline/
  - ec/orders/references/return-refund-status-reference/
  - ec/orders/tcat-quick-store/tcat-quick-store-overdue/
  - ec/orders/cvs-shipping/cvs-partial-shipment/
  - ec/orders/references/cvs-partial-shipping-support/
tags:
  - "Unclaimed Convenience Store Orders"
  - "Automatic Refunds"
  - "Manual Refunds"
  - "Convenience Store Returns"
  - "Order Processing"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=6996
  - https://www.cyberbiz.io/support/?p=2041
permalink: "https://help.cyberbiz.io/ec/orders/returns-refunds/cvs-unclaimed-order/"
comments: false
search:
  exclude: false
icon: lucide/package-x
hide: []
---

## About Unclaimed Convenience Store Orders

When a customer doesn't pick up an order at a convenience store before the deadline, the convenience store system marks the order "Unclaimed." This article explains what the system changes automatically, the return process for each logistics type, and the manual refund steps you need to take.

## Overview { #intro-overdue-cvs-orders }

For convenience store logistics integrated with CYBERBIZ (7-Eleven, FamilyMart, Hi-Life, EZCAT Quick Store Delivery), the convenience store reports back when a customer doesn't pick up in time, and the CYBERBIZ
system automatically moves the order to "Unclaimed" and triggers a refund and invoice allowance if conditions are met. Items are returned to the logistics warehouse or the original sending store, depending on the shipping method (B2C bulk shipping or C2C store-to-store).

**What the system does automatically**:

* Changes the delivery status from "Shipped" to "Unclaimed"
* Sets the return status to "Transit Center"
* If automatic refund conditions are met, changes the payment status to "Pending Refund" and issues the refund
* If an invoice was issued and automatic voiding isn't turned off, voids the invoice or issues an allowance

**What you need to do**:

* Collect the items at the logistics warehouse or original sending store, depending on the logistics type
* For orders the system can't refund automatically, enter the customer's refund information on the order details page and issue a manual refund
* Tell customers that if they still want to buy, they need to place a new order; unclaimed orders **can't** be shipped again

!!! info "Tip"
    Unclaimed orders can't be shipped again. If the customer still wants to buy, guide them to place a new order, and close the original order following this article.

## Prerequisites and Limitations { #prerequisites-overdue-cvs-orders }

### Scope { #prerequisites-overdue-cvs-orders-scope }

Automatic "Unclaimed" status only applies to **convenience store logistics integrated with CYBERBIZ**:

* 7-Eleven standard pickup / cash on pickup (B2C bulk shipping)
* 7-Eleven Delivery Service (C2C store-to-store)
* FamilyMart standard pickup / cash on pickup (B2C bulk shipping)
* FamilyMart store-to-store (C2C)
* FamilyMart Cold Chain
* Hi-Life standard pickup / cash on pickup (B2C bulk shipping)
* Hi-Life store-to-store (C2C)
* EZCAT Quick Store Delivery (room temperature / refrigerated / frozen)

The system doesn't automatically change orders to "Unclaimed" if they use a "Custom Shipping Method" or regular home delivery (EZCAT, Pelican Express, HCT Logistics, SF Express).

---

### Customer Pickup Deadlines { #prerequisites-overdue-cvs-orders-expired-days }

CYBERBIZ sets the number of days before an order is considered unclaimed for each logistics type based on the convenience store's rules. Merchants can't change it.

| Logistics Type | Days Before Unclaimed |
| :-- | :-- |
| 7-Eleven Delivery Service (C2C) | 7 days |
| FamilyMart store-to-store (C2C) | 6 days |
| EZCAT Quick Store Delivery (room temperature / refrigerated / frozen) | 4 days |
| Other convenience store logistics | Determined by each convenience store's system |

---

### Automatic Refund Requirements { #prerequisites-overdue-cvs-orders-auto-refund }

Not all unclaimed orders are refunded automatically. All of the following must be met:

- [x] **Payment status is "Payment Received"**: Statuses such as awaiting payment or Cash on Delivery aren't eligible for automatic refunds.
- [x] **The payment method supports automatic card refunds**: For the full list of payment methods and refund time limits, see [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" data-preview }.
- [x] **"No Automatic Refund for Unclaimed Convenience Store Orders" isn't enabled**: If you've enabled it, all unclaimed orders use manual refunds.
- [x] **The whole order was shipped**: For partial shipments (part by convenience store, part by home delivery), unclaimed convenience store items don't trigger a refund right away; they're handled after you confirm.

For detailed conditions, see [Return and Refund Statuses](../references/return-refund-status-reference.md#reference-overdue-cvs-refund-flow-auto-refund){ title="Return and Refund Statuses (Unclaimed Convenience Store Orders)" }.

!!! plan "Plans / Limitations"
    Supported plans for automatic refunds, refund support for each payment method, and whether "No Automatic Refund for Unclaimed Convenience Store Orders" is enabled all affect system behavior.

---

## Steps { #operate-overdue-cvs-orders }

### B2C Bulk Shipping: Items Return to the Logistics Warehouse { #operate-overdue-cvs-orders-b2c-return }

Unclaimed items from 7-Eleven standard pickup / cash on pickup, FamilyMart standard pickup / cash on pickup, FamilyMart Cold Chain, and Hi-Life standard pickup / cash on pickup are returned by the convenience store to the corresponding logistics warehouse.

**Return locations**:

* 7-Eleven items return to Uni-President Distribution (PCSC Logistics)
* FamilyMart items return to FamilyMart Riyi Culture
* Hi-Life items return to the HiLife Logistics Center

**How you collect them** (based on the "return cycle" and "return method" you set with CYBERBIZ **when enabling convenience store logistics**):

1. **Return cycle:** The system returns items together on the cycle you agreed on: "Weekly"[^fn-every-week], "Next Day"[^fn-next-day], or "Same Day"[^fn-same-day].
2. **Return method:** A designated carrier (such as EZCAT) picks up the items at the warehouse and delivers them to your return address, or you pick them up at the logistics center yourself.
3. **If no pickup carrier is designated:** The warehouse sends the items back to your return address by **freight-collect home delivery**, and you pay the shipping fee.

!!! note "Note"
    The return cycle, return method, and return address are set when you enable convenience store logistics with CYBERBIZ sales, and there's no place to edit them in the admin day to day. To change them, contact your CYBERBIZ sales representative.

---

### C2C Store-to-Store: Items Return to the Original Sending Store { #operate-overdue-cvs-orders-c2c-return }

Unclaimed items from 7-Eleven Delivery Service, FamilyMart store-to-store, and Hi-Life store-to-store are first returned to the **original sending store** for you to collect.

**Collection process**:

1. **Receive a notification:** When the items are returned to the original sending store, the system notifies you by **text** and **email**.
2. **Bring ID:** Bring an **original ID** matching the "Sender Name" to the original sending store to collect the items.
3. **Collect by the deadline:** Collect the items within the agreed period after they're returned to the store. Rules for uncollected items depend on each convenience store.
4. **If not collected in time:** If the store's holding period passes, the items are returned to the convenience store logistics warehouse, and the convenience store sends them to your return address by **EZCAT cash on delivery**. You pay the shipping fee.

!!! warning "Caution"
    If you **refuse** a package returned from the convenience store logistics warehouse and it goes back to the logistics center again, some convenience stores' rules call for the goods to be **discarded**, and they can't be recovered.

!!! note "Note"
    **No shipping fee** is charged for returning items to the original sending store. A shipping fee applies only if the warehouse later sends them to you by freight-collect home delivery.

---

### Automatic Refunds by the System <small>No Action Needed</small> { #operate-overdue-cvs-orders-auto-refund }

When an order meets the [automatic refund requirements](#prerequisites-overdue-cvs-orders-auto-refund){ title="Automatic Refund Requirements" }, after receiving the convenience store's unclaimed notice the system automatically:

1. Changes "Delivery Status" to "Unclaimed"
2. Changes "Return Status" to "Transit Center"
3. Changes "Payment Status" to "Pending Refund," issues the refund through the original payment channel, and then changes it to "Refunded"
4. If an invoice was issued, voids it or issues an allowance based on your settings

On the order list page, you can see the delivery status change to "Unclaimed" and the payment status to "Refunded." **No admin action is needed**.

---

### Manual Refunds: Enter Refund Information { #operate-overdue-cvs-orders-manual-refund }

If the order doesn't meet the automatic refund requirements (for example, the payment method isn't on the automatic card refund list, or you've enabled "No Automatic Refund for Unclaimed Convenience Store Orders"), the system sets the payment status to **Pending Refund**, and you issue the refund manually.

1. **Open the order details page:** Go to "Orders" > "All Orders" in the admin and click the order number of an order with delivery status "Unclaimed" and payment status "Pending Refund."
2. **Enter refund information:** Find the **Enter Refund Information** section on the order details page (titled **Manual Refund**, with the message "The automatic refund period has passed. A manual refund will be issued.").
3. **Enter the customer's bank information:** Select or enter the following:
    * **Bank:** Choose the customer's bank from the drop-down
    * **Branch:** Choose the branch from the drop-down
    * **Account name:** The customer's account name
    * **Account number:** The customer's bank account number
    * **Refund reason:** Optional, up to 250 characters
4. **Submit:** After you confirm, the system marks the order's return status as "Returned" and voids the invoice or issues an allowance based on your settings. You send the actual payment by bank transfer using the refund information.

!!! tip "Tip"
    If the customer provides their own bank information, you can also ask them to sign in to their member account, click the order, and fill in "Refund Information" (the customer-side entry). Then issue the manual refund in the admin using the information they provided.

## Important Rules and Limitations { #specs-overdue-cvs-orders }

### Unclaimed Orders Can't Be Shipped Again { #specs-overdue-cvs-orders-no-reship }

Unclaimed orders **can't** be shipped again. If the customer still wants to buy, guide them to place a new order. Close the original order after completing the return and refund following this article.

---

### Partial Shipment Special Handling { #specs-overdue-cvs-orders-partial }

When an order is "Partially Shipped," with the **first shipment by convenience store** and the **second by another carrier**:

* **First shipment (convenience store):** The delivery status changes to "Unclaimed," but **no automatic refund is triggered**. You must evaluate and issue a manual refund (even if the order would otherwise meet the automatic refund requirements).
* **Second shipment (other carrier):** The delivery status stays "Shipped" and isn't updated to "Unclaimed" along with the first.

For detailed status changes, see [Return and Refund Statuses](../references/return-refund-status-reference.md#reference-overdue-cvs-refund-flow-partial){ title="Return and Refund Statuses (Unclaimed Convenience Store Orders)" data-preview }.

---

### "No Automatic Refund for Unclaimed Convenience Store Orders" Feature { #specs-overdue-cvs-orders-no-auto-refund-plugin }

Once you enable this feature, **all**
unclaimed convenience store orders use the manual refund process. The system doesn't trigger refunds or void invoices automatically. The return status also changes from the default "Transit Center" to "Original Sender Store," and you decide how to handle the refund after checking the items.

!!! example "Use Cases"
    You want to confirm items are returned before refunding the customer, for example, when items may be damaged or you want to deduct a handling fee from the refund.

---

### Lost Package Compensation { #specs-overdue-cvs-orders-lost }

If a package isn't returned to the logistics center or original sending store within the specified time and the convenience store confirms it's lost, the system starts a compensation process and the convenience store pays compensation. Keep shipping documents and system records as evidence.

---

### Invoice Handling { #specs-overdue-cvs-orders-invoice }

* **Invoices issued by CYBERBIZ on your behalf:** The system issues an allowance automatically after the refund.
* **Invoices not issued by CYBERBIZ (issued by your own system):** Void the invoice or issue an allowance after the refund.
* **With "Don't Automatically Cancel Invoices for Unclaimed Convenience Store Orders" enabled:** Even when an order is unclaimed, the system doesn't handle the invoice automatically; you need to handle it manually.

## Next Steps { #next-steps-overdue-cvs-orders }

<div class="grid cards" markdown>

- :lucide-arrow-right-left:{ .lg }  
  [__Return and Refund Statuses__](../references/return-refund-status-reference.md){ title="Return and Refund Statuses (Unclaimed Convenience Store Orders)" }  
  How delivery, return, and payment statuses change, and the conditions for automatic refunds.

- :lucide-credit-card:{ .lg }  
  [__Automatic Card Refund Time Limits__](../references/auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" }  
  The maximum number of days each payment provider supports automatic card refunds.

- :lucide-truck:{ .lg }  
  [__EZCAT Quick Store Delivery Overdue Rules__](../tcat-quick-store/tcat-quick-store-overdue.md){ title="EZCAT Quick Store Delivery Overdue Rules" }  
  Overdue fees and start times for each temperature zone: room temperature, refrigerated, and frozen.

- :lucide-package-check:{ .lg }  
  [__Partial Shipment for Orders__](../cvs-shipping/cvs-partial-shipment.md){ title="Handle Partial Shipment of Convenience Store Orders" }  
  How partial shipment selection works and which logistics services support it.

</div>

## FAQ { #faq-overdue-cvs-orders }

??? quote "The customer still wants to buy. Can I ship the unclaimed order again?"
    [](){ #faq-overdue-cvs-orders-reship }
    No. Once an order is "Unclaimed," the system no longer allows it to ship. Guide the customer to place a new order, and close the original order through the return and refund process.

??? quote "Why wasn't my unclaimed order refunded automatically?"
    [](){ #faq-overdue-cvs-orders-no-auto-refund }
    Possible reasons:

    - The payment method isn't on the automatic card refund list (see [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" data-preview })
    - You've enabled "No Automatic Refund for Unclaimed Convenience Store Orders"
    - The order was partially shipped, and only the first (convenience store) shipment is unclaimed
    - The order's payment status hasn't reached "Payment Received"

    For detailed conditions, see [Automatic Refund Requirements](#prerequisites-overdue-cvs-orders-auto-refund){ title="Automatic Refund Requirements" }.

??? quote "How soon must I collect items returned to the original sending store?"
    [](){ #faq-overdue-cvs-orders-pickup-deadline }
    Collect items returned to the original sending store as soon as possible. Rules for uncollected items depend on each convenience store. If not collected in time, the package is returned to the convenience store logistics warehouse, and the convenience store sends it to your return address by **EZCAT cash on delivery**. You pay the shipping fee. If you're not sure of the collection deadline, we recommend **going as soon as possible** after you receive the system email / text notification.

??? quote "Where do I get the customer's refund information (bank / account number)?"
    [](){ #faq-overdue-cvs-orders-bank-info }
    There are two ways:

    - **Contact the customer:** Ask the customer for their bank / branch / account name / account number, and enter them in the "Enter Refund Information" section on the order details page
    - **Have the customer fill it in:** Guide the customer to sign in to their member account and fill in the "Refund Information" page themselves

??? quote "How many days of shipping fees are charged for unclaimed EZCAT Quick Store Delivery orders?"
    [](){ #faq-overdue-cvs-orders-tcat-fee }
    For EZCAT Quick Store Delivery, if the customer **doesn't pick up within 4 days** (the system marks it unclaimed), a **return shipping fee** is charged (based on volume and temperature zone). For the actual amount, see [EZCAT Quick Store Delivery Overdue Rules](../tcat-quick-store/tcat-quick-store-overdue.md){ title="EZCAT Quick Store Delivery Overdue Rules" } and your contract terms.

??? quote "What does discarding mean, and when are items discarded?"
    [](){ #faq-overdue-cvs-orders-discard }
    After items are returned from the original sending store to the logistics warehouse and the warehouse sends them to you by freight-collect home delivery, if you **refuse** the package, some convenience stores' rules call for the goods to be "discarded," and they can't be recovered. Be sure to collect or accept the package as agreed after receiving the return notice.

---

## References { #reference-overdue-cvs-orders }

* [Return and Refund Statuses](../references/return-refund-status-reference.md){ title="Return and Refund Statuses (Unclaimed Convenience Store Orders)" }
* [Automatic Card Refund Time Limits](../references/auto-refund-timeline.md){ title="Automatic Card Refund Time Limits" }
* [EZCAT Quick Store Delivery Overdue Rules](../tcat-quick-store/tcat-quick-store-overdue.md){ title="EZCAT Quick Store Delivery Overdue Rules" }
* [Partial Shipment Support by Logistics Type](../references/cvs-partial-shipping-support.md){ title="Convenience Store Partial Shipment Support" }

[^fn-every-week]: "Weekly": Items returned during the week are packed into one box and returned to you the following week.
[^fn-next-day]: "Next Day": Items returned on a day are packed into one box and returned to you the next day.
[^fn-same-day]: "Same Day": Items returned on a day are packed into one box and returned to you the same day.

