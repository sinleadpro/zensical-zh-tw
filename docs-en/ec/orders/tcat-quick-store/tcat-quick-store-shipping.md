---
title: "Ship with EZCAT Quick Store Delivery"
description: "Batch download EZCAT Quick Store Delivery shipping labels and update the order shipment status to Shipped."
created: 2026-05-18 15:26
last_modified: 2026-07-15 14:40
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - fix link 黑貓取件設定頁 configure-ezcat-cvs-shipping-note-sender
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
  - 批次下載黑貓快速到店託運單
  - 黑貓快速到店出貨
  - 補印託運單
features:
  - 黑貓快速到店
  - 批次出貨
  - 自動呼叫黑貓司機
  - 補印託運單
prerequisites:
  - 領取黑貓三聯空白託運單貼紙
  - 設定黑貓寄件人地址
  - 確認 CYBER 幣餘額
related:
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/orders/home-delivery/tcat-auto-call-driver-v2/
  - ec/payments-and-logistics/setup-print-tcat-quick-store-waybill-v2/
  - ec/website-management/points-deposits/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
tags:
  - "EZCAT Quick Store Delivery"
  - 7-Eleven
  - "Shipping Labels"
  - "Logistics Shipping"
  - "Batch Shipping"
  - "Convenience Store Logistics"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 更多操作
  - 下載黑貓快速到店託運單
  - 補印託運單
paths:
  - 金物流 > 黑貓快速到店託運單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2678
  - https://www.cyberbiz.io/support/?p=8844
permalink: "https://help.cyberbiz.io/ec/orders/tcat-quick-store/tcat-quick-store-shipping/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![Download EZCAT Quick Store Delivery ambient shipping labels](../../../assets/images/EC-訂單-所有訂單-下載黑貓快速到店託運單-hero.en.png){ title="Download EZCAT Quick Store Delivery Ambient Shipping Labels" .hero-page }

## About EZCAT Quick Store Delivery Shipping { #intro-tcat-cvs }

"EZCAT Quick Store Delivery" is a service where EZCAT delivers your products to the 7-Eleven store chosen by the customer for pickup. It's divided into ambient, refrigerated, and frozen by product temperature zone. This page shows how to batch process orders in the new order list, download shipping labels, and change the delivery status to "Shipped."

!!! info "Other EZCAT Services"
    * If the customer chooses home delivery, see [Ship with EZCAT Home Delivery](../home-delivery/tcat-home-delivery-v2.md){ title="Ship with EZCAT Home Delivery" }.
    * To have an EZCAT driver called automatically for pickup at your location, see [Automatically Call an EZCAT Driver for Pickup](../home-delivery/tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }.

## Prerequisites and Limitations { #prerequisites-tcat-cvs }

Before shipping with EZCAT Quick Store Delivery, make sure your system settings, order statuses, and hardware meet the following requirements.

### Eligible Order Statuses { #prerequisites-tcat-cvs-order-status }

The system only allows shipping for orders that meet the following conditions:

- [x] **Delivery method**: The matching "EZCAT Quick Store Delivery" option was chosen at checkout.
- [x] **Payment status**: Shows "Payment Received" or "Cash on Delivery."
- [x] **Delivery status**: Shows "Unshipped," "Partially Shipped," or "Preparing."

---

### Delivery Rules { #prerequisites-tcat-cvs-shipping-rules }

The following are the logistics rules for EZCAT Quick Store Delivery. Check them before packing and shipping:

| Item | Details |
| :-- | :-- |
| Package weight limit | 10 kg per package |
| Package size limit | Length + width + height up to 105 cm |
| Delivery area | Taiwan main island only; outlying islands aren't supported |
| Pickup deadline | After the package arrives at the store, ambient packages are held for 7 days; refrigerated/frozen packages only 4 days. EZCAT sends the customer 1 SMS on **the day the package arrives** and 1 on **the day before it's returned**, 2 in total. |
| Shipping label validity | After the shipping label is created, you must contact EZCAT to complete pickup within 7 days, or the tracking number expires |
| [Unclaimed](#tcat-cvs-overdue-pickup){ title="Unclaimed Store Packages" } | The package is returned to you, and EZCAT **charges an additional return shipping fee** |

!!! tip "Packaging Tips for Refrigerated/Frozen Shipments"
    * **Pre-chilling time**: We recommend pre-chilling refrigerated products for at least 6 hours and frozen products for at least 12 hours to keep the temperature zone until store pickup.
    * **Waterproof shipping labels**: We recommend printing shipping labels on waterproof stickers, or putting the label in a clear waterproof pouch before attaching it to the package, so condensation doesn't blur the barcode and prevent the driver from scanning it.

---

### System Limitations { #prerequisites-tcat-cvs-system-contraints }

- **Separate by temperature zone (no mixing)**: Ambient, refrigerated, and frozen use different shipping labels. When selecting orders in bulk to ship, you can't mix orders from different temperature zones.
- **Feature activation**: Your store must have the matching temperature zone feature enabled. To use refrigerated and frozen services, the system must also have the "Product-bound temperature zone" feature enabled.
- **Can't be used with Fengchao Logistics**: If your store is integrated with Fengchao Logistics, you can't use EZCAT Quick Store Delivery. You can only use one of the two.

## Steps { #tcat-cvs-operate }


### Before Shipping { #prerequisites-tcat-cvs-checklist }

Before shipping with EZCAT Quick Store Delivery, complete the following:

- [x] **EZCAT sender address**: Go to "Payment and Logistics" > "[EZCAT Quick Store Delivery Shipping Labels](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#configure-ezcat-cvs-shipping-note-sender-setup){ title="Set Up Sender Information" }" and set the sender address, or the sender information on the shipping label will be incomplete.
- [x] **Supplies and equipment**: You have "EZCAT three-part blank shipping label stickers" ready (call EZCAT customer service at 02-412-8888 to get them), and we recommend a laser printer so barcodes print clearly.
- [x] **Product pre-chilling (low-temperature packages)**: Refrigerated products must be pre-chilled for at least 6 hours; frozen products for at least 12 hours.
- [x] **Check your balance**: Standard Plan merchants should go to [check the CYBER Coin balance in the Top-Up Center](../../website-management/points-deposits.md#cyber-coin-balance){ data-preview } and make sure the balance is sufficient; PLUS / Enterprise merchants don't have this restriction.

--- 

### Batch Download EZCAT Quick Store Delivery Shipping Labels { #operate-tcat-csv-shipping-note }

The following uses ambient shipping labels as an example. The steps for refrigerated and frozen are the same; just choose the matching option in the drop-down step.

1. **Open the order list**: In the admin, go to "Orders" > "All Orders."
2. **Select the orders to ship**: Select one or more orders using the checkboxes on the left of the list. Make sure the selected orders are all the same EZCAT Quick Store Delivery type (ambient, refrigerated, or frozen). You can't mix different temperature zones.
3. **Open "Actions..." and choose the download action**: Click the **Actions...** drop-down above the list and choose one based on the selected orders' temperature zone:
    * Download EZCAT Quick Store Delivery Ambient / Refrigerated / Frozen Shipping Labels and Change Delivery Status to "Shipped"

    ![Download EZCAT Quick Store Delivery ambient shipping labels](../../../assets/images/EC-訂單-所有訂單-下載黑貓快速到店託運單.en.png){ title="Download EZCAT Quick Store Delivery Ambient Shipping Labels" }

4. **Review the shipment information**: The system opens the "Download EZCAT Quick Store Delivery - Ambient/Frozen/Refrigerated Shipping Labels" window, which lists the orders in this shipment. Check that they're correct.
5. **(Optional) Set up automatic driver pickup**: If your store has the "[Call EZCAT](../home-delivery/tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }" feature enabled, the window shows the "Automatically call an EZCAT driver for pickup?" option. Choose **Yes** to show these three fields:

    * **Call before pickup?**: If you choose "Yes," the driver calls the contact phone number on the "[EZCAT pickup settings page](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#configure-ezcat-cvs-shipping-note-sender-setup){ data-preview }" to confirm with you before arriving.
    * **Does the EZCAT driver need to bring a cart?**: If you have many packages, you can ask the driver to bring a cart.
    * **Notes**: Enter special pickup instructions (for example, building access or floor), up to **100 characters**.

    ??? warning "Call Cutoff Time"
        The [call cutoff time](../home-delivery/tcat-auto-call-driver-v2.md#tcat-auto-call-driver-deadtime){ data-preview } is **16:30** each day. After that, this option is locked to "No," and you can't call a driver through the system that day; call EZCAT yourself to arrange pickup.

6. **Confirm the sender address**: The window shows a "Sender Address" field, which defaults to the last sender address used for this logistics service (the first time, it uses the address in the [EZCAT Quick Store Delivery settings](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#configure-ezcat-cvs-shipping-note-sender-setup){ title="Set Up Sender Information" }). To change it, click the **Change** button in the window to edit it[^2].

    ![Change sender address](../../../assets/images/EC-訂單-所有訂單-下載黑貓快速到店常溫託運單-更改地址.en.png){ title="Change Sender Address" }

7. **Agree to the terms of service**: Make sure "I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and EZCAT Contract Terms" is selected (selected by default); the "Confirm" button is enabled only then.
8. **Confirm the download**: Click **Confirm**, and the system automatically downloads[^1] the [shipping label ZIP file](#tcat-cvs-zip-contents){ title="Shipping Label ZIP Contents" }.
9. **Confirm the delivery status changed**: When you're done, the delivery status of the selected orders automatically changes to **Shipped**. (See [Confirm the Delivery Status Change](#tcat-cvs-verify-status){ title="Confirm the Delivery Status Change" })


[^1]: If the download doesn't start, check whether your browser is blocking pop-ups or ads. Allow pop-ups for this site and click download again. For more troubleshooting, see [FAQ: Can't download shipping labels](#faq-tcat-cvs-download-no-response)
[^2]: Changes also update the address on the EZCAT Quick Store Delivery settings page. Addresses for other logistics services and the company logistics address aren't affected.

---

### Call an EZCAT Driver for Pickup { #tcat-cvs-call-driver-pickup }

After downloading the shipping labels, contact an EZCAT driver to pick up the packages:

* **Call by phone**: Call the EZCAT customer service line (02-412-8888) to arrange pickup.
* **Call directly from the admin**: If you've enabled the [Call EZCAT feature](../home-delivery/tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }, you can schedule driver pickup in the pop-up when downloading shipping labels.

---

### Confirm the Delivery Status Change { #tcat-cvs-verify-status }

After you download the shipping labels, you can check the delivery status in two places:

- **Order list page**: The delivery status column shows **Shipped**
- **Order details page**: The status shows [Shipped (Awaiting Carrier Pickup)](../home-delivery/shipping-status-tooltip.md#shipping-status-text-type){ data-preview }, meaning the shipping label was created but EZCAT hasn't picked up the package yet

If the delivery status didn't update, check:

* Whether the download actually completed (whether the browser blocked the download dialog)
* Whether all selected orders use "EZCAT Quick Store Delivery" as the delivery method

---

### Troubleshoot Address Errors { #tcat-cvs-address-error }

If an "Incomplete sender information" message appears when you download shipping labels, the EZCAT sender address isn't set or is incomplete:

1. Go to **Payment and Logistics > EZCAT Convenience Store Shipping Label** and make sure the **Sender Address** in the "EZCAT Quick Store Delivery Settings" section is complete (including city/county and district). After you save, the system automatically looks up the sender area code with EZCAT.
2. After saving, download again.

??? info "Notes on the Sender Address"
    * **Address source**: The sender address comes from the "EZCAT Quick Store Delivery Settings" address in **Payment and Logistics > EZCAT Convenience Store Shipping Label**.
    * **How to change it**: Click **Change** in the shipping label download pop-up to edit it directly. Changes also update the EZCAT Quick Store Delivery settings page.

---

### Unclaimed Store Packages { #tcat-cvs-overdue-pickup }

After the package arrives at the convenience store, the customer has a pickup deadline:

* **Ambient**: Within 7 days
* **Refrigerated / frozen**: Within 4 days

EZCAT sends **2 SMS messages** to remind the customer:

| SMS | When It's Sent |
| :-- | :-- |
| 1st | The day the package arrives at the store |
| 2nd | 1 day before it's returned (day 6 for ambient, day 3 for refrigerated/frozen) |

## Next Steps { #nextstep-tcat-cvs }

<div class="grid cards" markdown>

<!-- - :lucide-printer:{ .lg }  
  [__Reprint Shipping Labels__](../../payments-and-logistics/reprint-waybills.md){ title="Reprint and Print Extra Shipping Labels" }  
  If you need to print again (for example, the label got wet or printed unclearly), go back to the order list, select the same order, and choose Reprint Shipping Label from "More Actions." -->

- :lucide-truck:{ .lg }  
  [__Call a Driver Automatically__](../home-delivery/tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }  
  If you've enabled the "Call EZCAT" feature, you can call a driver automatically when printing shipping labels.

- :lucide-package-check:{ .lg }  
  [__Partial Shipment__](../home-delivery/partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }  
  If you want to send only some items in an order first, select the specific items from the order details page instead.

- :lucide-copy-plus:{ .lg }  
  [__Print Extra Shipping Labels__](../../payments-and-logistics/setup-print-tcat-waybill-v2.md){ title="Set Up and Print Extra EZCAT Shipping Labels" }  
  If an order has many products and must be split into several boxes, each box needs its own shipping label.

</div>

## FAQ { #faq-tcat-cvs }

??? quote "Nothing happens when I download / I can't download shipping labels"
    [](){ #faq-tcat-cvs-download-no-response }

    This is usually caused by one of the following:

    * **Browser blocking pop-ups**: Check whether your browser is blocking pop-ups or ads. Allow pop-ups for this site and click download again.
    * **Not enough CYBER Coins (Standard Plan merchants)**: Go to the [Top-Up Center](../../website-management/points-deposits.md){ data-preview } to top up.
    * **EZCAT Quick Store Delivery sender address not set**: Complete the sender address in the "EZCAT Quick Store Delivery Settings" section of **Payment and Logistics > EZCAT Convenience Store Shipping Label**.
    * **Terms not accepted**: Make sure "I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and EZCAT Contract Terms" at the bottom of the pop-up is selected.


??? quote "Why can't I find the "Download EZCAT Quick Store Delivery…" option in the "More Actions" drop-down?"
    [](){ #faq-tcat-cvs-action-missing }

    This is usually caused by one of the following:

    * The selected orders didn't choose EZCAT Quick Store Delivery at checkout, or you selected orders with different temperature zones or different logistics services. Make sure this batch is all the same EZCAT Quick Store Delivery type.
    * The order's delivery status isn't "Unshipped," "Partially Shipped," or "Preparing" (for example, it's refunded or canceled), so it can't be shipped.

??? quote "Why is the "Automatically call an EZCAT driver for pickup?" option grayed out or unavailable?"
    [](){ #faq-tcat-cvs-call-disabled }

    Possible reasons:

    * It's past **16:30** today. The automatic call option turns off and stays at "No." Use it the next day, or call EZCAT yourself to arrange same-day pickup.
    * Your store hasn't enabled the "Call EZCAT" feature, so the whole automatic call section isn't shown. Contact your sales representative or call EZCAT customer service for pickup.

??? quote "Can I download shipping labels while the payment status is still "Awaiting Payment"?"
    [](){ #faq-tcat-cvs-payment-status }

    No. Shipping requires the order's payment status to be "Payment Received" or "Cash on Delivery," and the delivery status to be "Unshipped," "Partially Shipped," or "Preparing." If payment isn't confirmed yet, handle the payment first and then ship.

??? quote "Can I reprint a shipping label that printed badly or got lost?"
    [](){ #faq-tcat-cvs-redownload }

    Yes. Select the order in the order list and choose **Reprint Shipping Label** from "More Actions." The system creates the file again with the original tracking number and doesn't create a duplicate.

??? quote "Can I ship ambient and frozen orders together in the same batch?"
    [](){ #faq-tcat-cvs-mixed-temperature }

    No. Ambient, refrigerated, and frozen are three separate download actions, and the temperature zone is tied to the order at checkout. Select and ship in batches by temperature zone so a temperature zone mismatch doesn't affect product quality after shipping.

??? quote "What should I keep in mind when shipping refrigerated or frozen products?"

    When shipping refrigerated and frozen products, keep the following in mind:

    - **Pre-chilling time**: We recommend pre-chilling refrigerated products for at least 6 hours and frozen products for at least 12 hours to keep the temperature zone until store pickup
    - **Waterproof shipping labels**: We recommend printing shipping labels on waterproof stickers, or putting the label in a clear waterproof pouch before attaching it to the package, so condensation doesn't blur the barcode and prevent the driver from scanning it

??? quote "Can Standard Plan merchants download shipping labels with a low CYBER Coin balance?"

    No. When you download shipping labels, the system deducts from your CYBER Coin balance immediately, so the download fails if the balance is too low. Go to the [Top-Up Center](../../website-management/points-deposits.md){ data-preview } to top up, then try again.

### Shipping Label ZIP Contents { #tcat-cvs-zip-contents }

After the download finishes, the ZIP contains four PDFs, each for a different process:

| File | Purpose | Recipient |
|---|---|---|
| **Shipping Label** | Used by EZCAT for pickup and delivery; print on EZCAT three-part blank shipping label stickers and attach to the package | Driver |
| **Packing Slip** | Slip included in the package, listing items and quantities | Customer (in the package) |
| **Picking List** | Warehouse picking list, grouped by item for easy picking | Internal warehouse staff |
| **Order Details** | Full order information, including amounts, payment method, and customer details | Internal records / customer service |


