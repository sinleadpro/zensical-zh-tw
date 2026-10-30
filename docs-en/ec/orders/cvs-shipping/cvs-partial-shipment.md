---
title: "Handle Partial Shipment of Convenience Store Orders"
description: "Handle partial shipment of convenience store orders (7-Eleven, FamilyMart, Hi-Life), including full steps for the first shipment through the convenience store system and shipping the remaining items with custom logistics."
created: 2026-05-26 16:14
last_modified: 2026-07-02 07:15
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
  - 超商訂單部分出貨
  - 分批出貨超商取貨訂單
features:
  - 超商部分出貨
  - 自訂出貨方式
prerequisites: []
related:
  - ec/orders/references/cvs-partial-shipping-support/
  - ec/orders/references/cvs-waybill-expiration-reference/
  - ec/orders/renew-waybill-after-expiration/
  - ec/orders/home-delivery/custom-logistic-shipping/
  - ec/orders/references/order-filter-status-reference/
tags:
  - "Convenience Store Partial Shipment"
  - "Convenience Store Pickup"
  - 7-Eleven
  - FamilyMart
  - Hi-Life
  - "Custom Logistics"
  - "Split Shipments"
  - "Cash on Delivery"
  - "Order Management"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 選擇出貨方式
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=9359
  - https://www.cyberbiz.io/support/?p=44069
permalink: "https://help.cyberbiz.io/ec/orders/cvs-shipping/cvs-partial-shipment/"
comments: false
search:
  exclude: false
icon: lucide/package-check
hide: []
---

![Convenience store partial shipment](../../../assets/images/EC-訂單-所有訂單-訂單詳情頁-超商物流部分出貨-hero.en.png){ title="Convenience Store Partial Shipment" .hero-page }

## About Convenience Store Partial Shipment

When a customer chooses convenience store pickup at **7-Eleven**, **FamilyMart**, or **Hi-Life**
but some items in the order need to ship separately (for example, some items are awaiting restock, exceed convenience store size limits, or need to switch to home delivery), you can use "Convenience Store Partial Shipment" to ship items in batches.

## Overview { #intro-cvs-partial-shipment }

Convenience store partial shipment applies to orders whose **delivery method is convenience store pickup (7-Eleven, FamilyMart, Hi-Life)**. The process has two stages:

- **First shipment**: Get a shipping label through the original convenience store delivery system and ship through the convenience store logistics network.
- **Remaining shipments**: Because convenience stores support only one tracking number per order, you must switch to **Custom Shipping Method** and ship with a carrier you've arranged yourself (such as EZCAT or HCT Logistics).

!!! info "Tip"
    Partial shipment isn't a separate module. You do it in the **shipping section of the order details page** by selecting some items and confirming the shipment. It's built into all plans, so no activation is needed.

## Prerequisites and Limitations { #prerequisites-cvs-partial-shipment }

### Supported Convenience Store Logistics { #prerequisites-cvs-partial-shipment-supported }

The following convenience store logistics services support partial shipment. For details, see [Convenience Store Partial Shipment Support](../references/cvs-partial-shipping-support.md).

- [x] **7-Eleven**: Delivery Service, convenience store pickup (including Cash on Delivery)
- [x] **FamilyMart**: Store-to-store, convenience store pickup (including Cash on Delivery)
- [x] **Hi-Life**: Store-to-store, convenience store pickup, frozen pickup (including Cash on Delivery)

??? info "EZCAT Quick Store Delivery Uses a Different Process"
      **EZCAT Quick Store Delivery (room temperature/refrigerated/frozen)** also supports partial shipment, but **the second shipment doesn't need to switch to Custom Shipping Method**.
      On the order details page, select some items > choose "EZCAT Quick Store Delivery Shipping Label" > confirm the shipment. The system automatically requests a new shipping label from EZCAT (up to 8 per order). Come back later to ship the remaining items; the process is the same as partial shipment for regular home delivery.

!!! warning "Logistics That Don't Support Partial Shipment"
    The following logistics types **don't support** partial shipment, and all items must ship at once:

    - **FamilyMart Cold Chain**: The system shows "FamilyMart Cold Chain doesn't support partial shipment. Select all items!"
    - **FamilyMart Frozen Store-to-Store**: Same message as above.

---

### Order Status Requirements { #prerequisites-cvs-partial-shipment-status }

The item checkboxes and "Confirm Shipment" button appear only when the order has one of these statuses:

- [x] **Unshipped**: No shipping action has been taken on the order yet.
- [x] **Preparing**: The order has been paid/confirmed and is waiting to ship.
- [x] **Partially Shipped**: Some items in the order have shipped, and the rest are waiting to ship.

## Steps { #operate-cvs-partial-shipment }

### Open the Order Details Page { #operate-cvs-partial-shipment-enter }

1. Go to the **"Orders" > "All Orders"** list in the admin.
2. Find the convenience store pickup order and click the **Order Number** to open the order details page.
3. The **"Select the items you're shipping now"** section at the lower right lists all items waiting to ship in this order.

![Order details page - convenience store partial shipment](../../../assets/images/EC-訂單-所有訂單-訂單詳情頁-超商物流出貨商品.en.png){ title="Order Details Page: Convenience Store Partial Shipment" }

---

### First Shipment: Ship Through the Convenience Store System { #operate-cvs-partial-shipment-first }

1. In the item list, **select the items to ship first**[^select-all].
2. After you select items, the **"Select Shipping Method"** section expands below, and its drop-down shows the matching convenience store shipping label option, such as "Store-to-Store Shipping Label."
3. Make sure the drop-down is set to **that convenience store's shipping label**.
4. Click **"Confirm Shipment."** The system asks "Ship the N selected items?" After you click **Yes**:
    * The system requests a tracking number from the convenience store and generates a shipping label PDF
    * The order status automatically changes to **"Shipped"** or **"Partially Shipped"**, depending on how many items shipped[^status-rule]
    * Shipped items show **"Shipped on {date and time}"**
5. After you get the shipping label, hand the items to the matching convenience store logistics service to ship.

[^select-all]: Click **"Select All"** at the upper right of the section to select all items at once, or **"Deselect All"** to clear the selection.
[^status-rule]: If the shipped quantity equals all items, the status is "Shipped." If any items remain unshipped, the status is "Partially Shipped."

![Order details page - convenience store partial shipment](../../../assets/images/EC-訂單-所有訂單-訂單詳情頁-超商物流部分出貨.en.png){ title="Order Details Page: Convenience Store Partial Shipment" }

---

### Remaining Shipments: Custom Shipping Method { #operate-cvs-partial-shipment-rest }

After the first shipment, open the order details page again to ship the remaining items. **Convenience store options are now hidden automatically**, and only **"Custom Shipping Method"** is available[^why-custom].

1. Open the order details page again and **select the remaining items to ship** in the item list.
2. The **"Select Shipping Method"** drop-down automatically switches to **"Custom Shipping Method."**
3. Fill in the expanded fields:
    * **Tracking Number**: The tracking number from the carrier you used.
    * **Carrier**: Choose the carrier from the drop-down (such as EZCAT or HCT Logistics).
4. Select **Send email notification to customer** if needed.
5. Click **"Confirm Shipment"** to ship the remaining items. These items also show **"Shipped on {date and time}"**, and the whole order changes to **"Shipped."**

![Order details page - convenience store partial shipment - remaining items](../../../assets/images/EC-訂單-所有訂單-訂單詳情頁-超商物流部分出貨-剩餘商品.en.png){ title="Order Details Page: Convenience Store Partial Shipment, Remaining Items" }

[^why-custom]: The convenience store delivery API supports only one tracking number per order. After the first shipment uses it, the system hides convenience store options and keeps only "Custom Shipping Method" so you can enter the second shipment's logistics information manually.

## Important Rules and Limitations { #specs-cvs-partial-shipment }

### Payment Rules for Cash on Delivery (COD) { #specs-cvs-partial-shipment-cod }

If the order uses **convenience store Cash on Delivery**, note the following:

- When the customer **picks up the first convenience store package, they pay the full order amount at once**, not just the amount for that batch.
- When the second batch ships through a custom carrier, the convenience store can't collect payment for it.
- **We strongly recommend contacting the customer before shipping** to explain the batch shipment and one-time payment, to avoid refused deliveries or return disputes.

---

### Delivery Tracking { #specs-cvs-partial-shipment-tracking }

Customers can see **two tracking numbers** under **"Order Lookup/Order Details" > "Delivery Information"** in the storefront member area, to track the convenience store and custom carrier deliveries separately.

---

### Returns { #specs-cvs-partial-shipment-return }

If a customer wants to return items after a partial shipment:

- **Partial returns aren't possible through the convenience store system**: Its return process covers the whole order and doesn't accept split returns.
- The customer needs to contact you, and you arrange the refund amount and return method with them (for example, the customer ships it back, or you send a carrier to pick it up).

---

## Reprint Shipping Labels

If a shipping label is lost or damaged, you can reprint it before the deadline.

1. Select the orders to reprint in the order list.
2. Open the **Actions...** drop-down and select **Reprint Shipping Label**.
3. The system downloads the PDF with the same tracking number again. Shipping fees aren't charged again, and the order status doesn't change.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Validity by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See each convenience store's reprint deadline and expiration rules.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label is past the reprint deadline, get a new tracking number and download a new shipping label.

</div>


## Next Steps { #next-steps-cvs-partial-shipment }

<div class="grid cards" markdown>

- :lucide-package:{ .lg }  
  [__Custom Logistics Shipping Settings__](../home-delivery/custom-logistic-shipping.md){ title="How to Ship with Custom Logistics" }  
  Set up the custom carrier list and tracking number field so you can quickly choose them for the second shipment.

<!-- - :lucide-truck:{ .lg }  
  [__Print and Reprint Shipping Labels__](../../payments-and-logistics/reprint-waybills.md){ title="Reprint and Print Extra Shipping Labels" }  
  To reprint the first convenience store shipping label, see this page. -->

<!-- - :lucide-receipt:{ .lg }  
  [__Cash on Delivery Payment Recognition Rules__](../references/cod-settlement.md)  
  Learn when COD order payments are recognized and how they're reconciled. -->

</div>

## FAQ { #faq-cvs-partial-shipment }

??? quote "Why can't I find the convenience store delivery option for the second shipment?"
    [](){ #faq-cvs-partial-shipment-no-cvs-option }
    The convenience store delivery API supports only one tracking number per order. After the first shipment requests it, the system hides convenience store options automatically. This is **a convenience store logistics limitation**, not a system error. Ship the remaining items with "Custom Shipping Method" and a carrier such as home delivery.

??? quote "For Cash on Delivery, does the customer pay in full or in part when the first batch arrives?"
    [](){ #faq-cvs-partial-shipment-cod-amount }
    The customer **pays the full order amount when picking up the first convenience store package**, not just the first batch's amount. We recommend agreeing with the customer before shipping, so they don't refuse the package thinking they'd pay per batch.

??? quote "Where can customers find the tracking numbers for both shipments?"
    [](){ #faq-cvs-partial-shipment-tracking-where }
    Customers can sign in to the storefront member center and see two tracking numbers on the **"Order Lookup" > "Order Details" > "Delivery Information"** page. Click each one to check the carrier's delivery progress.

??? quote "What if the customer picks up the first batch but doesn't want the second?"
    [](){ #faq-cvs-partial-shipment-partial-refund }
    Follow the regular return process:

    - Confirm the items and amount to return with the customer.
    - Refund the order in the admin.
    - If the second batch has already shipped, ask the customer to refuse it or ship it back.

    Single items can't be returned through the convenience store system; you need to arrange it yourself.

??? quote "How is EZCAT Quick Store Delivery partial shipment different from regular convenience store partial shipment?"
    [](){ #faq-cvs-partial-shipment-blackcat-diff }

    The main difference is **how the second shipment ships**:

    - **Regular convenience stores (7-Eleven/FamilyMart/Hi-Life)**: After the first shipment through the convenience store system, the remaining items must use **Custom Shipping Method**, and you enter the carrier and tracking number yourself.
    - **EZCAT Quick Store Delivery**: No need to switch to custom shipping. Each time, select the remaining items and choose "EZCAT Quick Store Delivery Shipping Label" to request a new shipping label from EZCAT, up to 8 per order.

??? quote "What conditions must an order meet for partial shipment?"
    [](){ #faq-cvs-partial-shipment-status-required }

    The order must meet all of the following:

    - The delivery method is **convenience store pickup (7-Eleven, FamilyMart, Hi-Life)** or **EZCAT Quick Store Delivery**
    - The order status is **Unshipped**, **Preparing**, or **Partially Shipped**
    - It isn't **FamilyMart Cold Chain** or **FamilyMart Frozen Store-to-Store** (these don't support partial shipment)

??? quote "After partial shipment, how are the delivery status and COD payment recognition timing determined?"
    [](){ #faq-cvs-partial-shipment-status-cod-timing }

    It depends on whether **the second shipment via custom logistics** or **the customer's pickup of the first convenience store package** happens first:

    - **Scenario 1 (pickup first, then shipment)**: The customer picks up the first package at the store → you ship the second batch later → the delivery status is **Shipped**, and CYBERBIZ recognizes the payment after the second shipment.
    - **Scenario 2 (shipment first, then pickup)**: You ship the second batch right after the first → the customer picks up the first package later → the delivery status is **Received**, and CYBERBIZ recognizes the payment after the customer picks up the first package.

## References { #reference-cvs-partial-shipment }

- [Convenience Store Partial Shipment Support](../references/cvs-partial-shipping-support.md){ title="Convenience Store Partial Shipment Support" }
- [Order Filters and Statuses Reference](../references/order-filter-status-reference.md){ title="Order Filters and Statuses Reference" }
<!-- - [Custom Carrier List](../../payments-and-logistics/references/custom-shipping-companies.md) -->

