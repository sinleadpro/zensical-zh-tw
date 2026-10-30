---
title: "Ship with EZCAT Home Delivery"
description: "Batch download EZCAT home delivery shipping labels, deduct shipping fees, and update the order shipment status to Shipped."
created: 2026-05-12 15:53
last_modified: 2026-07-07 11:04
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - 補 金物流 > 黑貓托運單設定 sib
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
  - 批次下載黑貓託運單
  - 黑貓宅配出貨
  - 補印託運單
features:
  - 黑貓宅配
  - 部分出貨
  - 補印託運單
  - 加印託運單
  - CYBER 幣扣款
prerequisites:
  - 領取黑貓三聯空白託運單貼紙
  - 完成黑貓設定（寄件人地址）
related:
  - ec/orders/tcat-quick-store/tcat-quick-store-shipping/
  - ec/orders/home-delivery/tcat-auto-call-driver-v2/
  - ec/website-management/points-deposits/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
  - ec/orders/home-delivery/partial-shipment-v2/
tags:
  - "EZCAT Home Delivery"
  - "Shipping Labels"
  - Shipping
  - TA-Q-BIN
  - Logistics
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 更多操作
  - 下載黑貓託運單
  - 補印託運單
paths:
  - 訂單 > 所有訂單
  - 金物流 > 黑貓託運單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=84
  - https://www.cyberbiz.io/support/?p=973
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/tcat-home-delivery-v2/"
comments: false
search:
  exclude: false
icon: lucide/cat
hide: []
---

![Order list - download EZCAT shipping labels and change to Shipped](../../../assets/images/EC-訂單列表-下載黑貓托運單-hero.en.png){ title="Order List - Download EZCAT Shipping Labels and Change to Shipped" .hero-page }

## About EZCAT Home Delivery

The admin integrates with the EZCAT (Black Cat) system. From the order list, merchants can generate EZCAT home delivery shipping labels in bulk, have shipping fees (CYBER Coins) deducted automatically, and update the order delivery status to "Shipped" at the same time. This article focuses on the shipping process for **EZCAT home delivery (B2C delivery to the door)**.

!!! info "Other EZCAT Services"
    * If customers choose convenience store pickup, see [Ship with EZCAT Quick Store Delivery](../tcat-quick-store/tcat-quick-store-shipping.md){ title="Ship with EZCAT Quick Store Delivery" }.
    * To have an EZCAT driver called automatically for door pickup, see [Automatically Call an EZCAT Driver for Pickup](tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }.

## Fees and Rules { #tcat-home-pricing }

### Shipping Fee Payment <small>By Plan</small> { #tcat-home-shipping-fee }

How EZCAT shipping fees are paid depends on your plan:

- **Standard Plan**: You need to [top up CYBER Coins](../../website-management/points-deposits.md#operate-cyber-coin-deposit){ title="How to Top Up CYBER Coins" } first. When you download shipping labels, the system deducts the shipping fee from your CYBER Coin balance in real time. If your balance is insufficient, the download fails.
- **PLUS / Enterprise**: No top-up needed. Each shipping fee is recorded in the "Reconciliation Center" and settled on each period's statement.

??? tip "How to Check Deduction Details"
     Standard Plan merchants can go to **Top-Up Center > Transaction History** to [check deduction history](../../website-management/points-deposits.md#cyber-coin-transaction-history){ title="Check CYBER Coin Transaction History" data-preview }; PLUS / Enterprise merchants can check monthly statements in the **Reconciliation Center**.

---

### Shipping Label Validity { #tcat-home-label-expiry }

CYBER Coins are deducted when you download shipping labels. If **the package isn't actually shipped within 14 days of generating the shipping label**, the system treats the tracking number as expired and does the following:

- The deducted CYBER Coins are refunded to your account automatically.
- On the order list page, the order's **Delivery Status** stays "Shipped" and doesn't change.
- On the order details page, the status stays "[Shipped (Awaiting Carrier Pickup)](shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" data-preview }."
- The tracking number status changes to "Shipment Canceled."

## Prerequisites and Limitations { #prerequisites-tcat-home }

Before shipping with EZCAT home delivery, complete the following:

- [x] **Get EZCAT blank three-part shipping label stickers**: Call EZCAT (02-412-8888) to get "blank three-part shipping label stickers" (commonly called A4 three-part labels). If you choose A4
standard printing, the system's printout must be printed on these stickers or the driver won't accept the package.
- [x] **EZCAT sender address**: Set the sender address in "Payment and Logistics" > "[EZCAT Shipping Labels](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#configure-ezcat-shipping-note-sender-setup){ title="Set Up Sender Information" }." Without it, you'll see an "Incomplete sender information" message when shipping.
- [x] **Check your balance or reconciliation status**: Standard Plan merchants should [check their CYBER Coin balance in the Top-Up Center](../../website-management/points-deposits.md#cyber-coin-balance){ title="Check CYBER Coin Balance" data-preview } to make sure it covers shipping fees; PLUS /
Enterprise merchants don't have this limit.
- [x] **Recommended printer**: We recommend printing shipping labels with a **laser printer** to avoid barcode reading errors.

## Steps { #operate-tcat-home }

### Download EZCAT Home Delivery Shipping Labels in Bulk { #tcat-home-shipping-label-batch }

This is the most common bulk shipping process:

1. **Go to the order list**: Sign in to the admin and go to **Orders > All Orders**.
2. **Select orders**: Select the orders to ship in the list. Make sure all selected orders use "EZCAT Home Delivery" as the delivery method.
3. **Click "Actions..."**: Click **Actions...** above the list and select **Download EZCAT Shipping Labels and Change Delivery Status to 'Shipped'** from the drop-down[^1].

    ![Download EZCAT home delivery shipping labels](../../../assets/images/EC-訂單-所有訂單-更多操作-黑貓宅配下載托運單.en.png){ title="Download EZCAT Home Delivery Shipping Labels" }

4. **Set the pop-up fields**: In the "Download EZCAT Shipping Labels" window, set the following in order
    * **Select a temperature zone**: Choose **Room Temperature**, **Refrigerated**, or **Frozen**. Make sure **the setting matches the actual package**.
    * **Is it Fragile?**: Choose **Yes** or **No**.
    * **Sender address**: Defaults to the sender address last used for this logistics service (the first time, it uses the address in [EZCAT settings](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#configure-ezcat-shipping-note-sender-setup){ title="Set Up Sender Information" }). To change it, click **Change** in the window to edit it[^3].

    * **Agree to the terms**: Select **I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and EZCAT contract terms**. The download button can't be clicked until you do.

    ![Download EZCAT shipping labels pop-up](../../../assets/images/ec-orders-tcat-waybill-download-popup.en.png)

    !!! plan "Call an EZCAT Driver Directly from the Pop-Up"
        If your store has enabled the EZCAT driver call feature, an "Automatically Call an EZCAT Driver for Pickup" section appears at the bottom of the window, so you can book a driver for door pickup while downloading shipping labels. For details, see [How to Automatically Call an EZCAT Driver for Pickup](tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }.

5. **Confirm download and payment**: Click **Confirm**. The system automatically downloads[^2] the [shipping label ZIP archive](#reference-tcat-home-zip-contents) and [deducts the shipping fee](#tcat-home-shipping-fee).

6. **Automatic delivery status update**: After the download, the delivery status of the selected orders changes to **Shipped** automatically. (See [Check the Delivery Status Change](#tcat-home-verify-status).)

    ??? warning "Recipient Information Can't Be Changed After Shipping"
        After an order is marked "Shipped," you can't change the recipient address or contact information in the admin. If the address is wrong, see [Fix Address Errors](#tcat-home-address-error).

[^1]: If the option doesn't appear, the order status may not qualify or logistics setup may be incomplete. For details, see [FAQ: No download shipping label option](#faq-tcat-home-missing-option).
[^2]: If the download doesn't start, check whether your browser blocked pop-ups or ads, allow pop-ups for this site, and click download again. For more troubleshooting, see [FAQ: Can't download shipping labels](#faq-tcat-home-download-no-response)
[^3]: Changes also update the address on that logistics page. Addresses for different logistics services and the company logistics address don't affect each other.

---

### Call an EZCAT Driver for Pickup { #tcat-home-call-driver-pickup }

After downloading shipping labels, contact EZCAT to have a driver pick up the packages:

* **By phone**: Call the EZCAT customer service line (02-412-8888) to arrange pickup.
* **From the admin**: If you've enabled the [EZCAT driver call feature](tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }, you can book a driver pickup in the pop-up when downloading shipping labels.

---

### Check the Delivery Status Change { #tcat-home-verify-status }

After successfully downloading shipping labels, you can check the delivery status in two places:

- **Order list page**: The delivery status column shows **Shipped**
- **Order details page**: The status shows [Shipped (Awaiting Carrier Pickup)](shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" data-preview }, meaning the shipping label has been generated but EZCAT hasn't picked up the package yet

If the delivery status didn't update, check:

* Whether the download actually completed (whether your browser blocked the download dialog)
* Whether all selected orders use "EZCAT Home Delivery" (for example, you may have selected an EZCAT Quick Store Delivery order or an order from another carrier by mistake)

---

### Fix Address Errors { #tcat-home-address-error }

If you see an "Incomplete sender information" message when downloading shipping labels, the EZCAT sender address is missing or incomplete:

1. Go to **Payment and Logistics > EZCAT Shipping Label** and make sure the **sender address** in the "EZCAT Settings" section is complete (including city/county and district). After you save, the system automatically looks up the sender area code with EZCAT.
2. After saving, download again.

??? info "Address Source Priority"
    The sender address in the pop-up defaults to the address last used for this logistics service (the first time, it uses the address in "EZCAT Settings"). Changing the "company logistics address" **doesn't** affect the sender address for EZCAT shipments; change it directly on the "Payment and Logistics > EZCAT Shipping Labels" page.


## Next Steps { #tcat-home-next-steps }

<div class="grid cards" markdown>

- :lucide-package-check:{ .lg }  
  [__Partial Shipment__](partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }  
  To ship only some items in an order first, select the specific items on the order details page instead.

<!-- - :lucide-printer:{ .lg }  
  [__Reprint Shipping Labels__](../../payments-and-logistics/reprint-waybills.md){ title="Reprint and Print Extra Shipping Labels" }  
  If a downloaded shipping label file is lost (for example, a misprinted sticker or a missing file), you can reprint in bulk from the order list. -->

- :lucide-copy-plus:{ .lg }  
  [__Print Extra Shipping Labels__](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#ezcat-shipping-note-create){ title="Print Extra Shipping Labels" }  
  If a home delivery order has many items and must be split into multiple boxes, each box needs its own shipping label.

- :lucide-receipt:{ .lg }  
  [__View Reconciliation Details__](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#ezcat-shipping-note-records){ title="Records and Reconciliation" }  
  If an order's shipping fee is adjusted (such as collecting a difference or a peak-season surcharge), the system records the details in "[Reconciliation Notes](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#ezcat-shipping-note-usage-records){ title="Tracking Number History" }."

</div>


## FAQ { #faq-tcat-home }

??? quote "Nothing happens when I click download / Can't download shipping labels"
    [](){ #faq-tcat-home-download-no-response }

    This is usually caused by one of the following:

    * **Browser blocks pop-ups**: Check whether your browser blocked pop-ups or ads, allow pop-ups for this site, and click download again.
    * **Insufficient CYBER Coins (Standard Plan merchants)**: Top up in the [Top-Up Center](../../website-management/points-deposits.md#cyber-coin-balance){ title="Check CYBER Coin Balance" data-preview }.
    * **EZCAT sender address not set**: Complete setup in Payment and Logistics > [EZCAT Shipping Labels](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#configure-ezcat-shipping-note-sender-setup){ title="Set Up Sender Information" }.
    * **Terms not accepted**: Make sure "I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and EZCAT contract terms" at the bottom of the pop-up is selected.

??? quote "There's no "Download EZCAT Shipping Labels" option"
    [](){ #faq-tcat-home-missing-option }

    The drop-down filters options automatically based on the order's delivery method. Possible reasons:

    * The order's delivery method isn't EZCAT Home Delivery (it may be EZCAT Quick Store Delivery, Pelican Express, SF Express, HCT Logistics, or another carrier).
    * The order hasn't been paid yet (for example, unpaid or awaiting bank transfer).
    * The order is already "Shipped." In that case, use **Reprint Shipping Label** instead of "Download."

??? quote "Can I change the address after downloading the shipping label?"
    [](){ #faq-tcat-home-edit-address }

    No. The address on a downloaded shipping label can't be changed in the system. **Correct it by hand** on the shipping label and tell the driver when handing over the package.

??? quote "Within how many days must I ship after downloading the shipping label?"
    [](){ #faq-tcat-home-expiry }

    After generating a shipping label, you must actually ship **within 14 days**. Otherwise, the tracking number is treated as expired and the CYBER Coins are refunded automatically.

??? quote "Can one order ship with two carriers?"
    [](){ #faq-tcat-home-mixed-shipping }

     No. Each order can use only one carrier. To ship items separately, see the [Partial Shipment](partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }
     process, or contact the sales team.

??? quote "Does reprinting shipping labels cost extra?"
    [](){ #faq-tcat-home-reprint-fee }

     No. Reprints use the original tracking number, so the system doesn't deduct CYBER Coins again. If you need a **new tracking number** (for example, splitting one order into multiple boxes), use "[Print Extra Shipping Labels](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#ezcat-shipping-note-create){ title="Print Extra Shipping Labels" }." Extra labels are charged per label.

??? quote "I'm a Fengchao Logistics merchant. Can I use this process?"
    [](){ #faq-tcat-home-honeycomb }

    No. Fengchao handles shipping for Fengchao Logistics merchants. Orders go into the Fengchao warehouse automatically, and Fengchao generates the EZCAT shipping labels. Merchants don't need to download shipping labels themselves.

??? quote "How do I fix "Invalid address. Can't look up area code. Please edit it on the order page."?"
    [](){ #faq-tcat-home-address-error }

    This happens because the EZCAT system doesn't support fuzzy address search. The order address must match the address data in the EZCAT system (not the address on Google Maps); otherwise, delivery and shipping label printing aren't available.

    !!! example "Common Error Examples"

        - Typos: for example, writing Hsinchu County's "**Emei Township**" with an incorrect Chinese character
        - Incomplete address: missing road, street, or lane names, so EZCAT can't read it

    Handle it based on the shipping status:

    - **Not shipped yet**: Confirm the correct address with the customer, go to **Orders > All Orders**, click the order, change the recipient address in the "Contact Information" section, and download the shipping label again.
    - **Shipped**: You can't change the address directly in the system. Print the shipping label, **correct the address by hand**, and tell the driver when handing over the package.

??? quote "How do I view reconciliation details?"
    [](){ #faq-tcat-home-view-account-details }

    If an order's shipping fee is adjusted (such as collecting a difference or a peak-season surcharge), the system records the details in "Reconciliation Notes." Admin path: Payment and Logistics > EZCAT Shipping Labels > Tracking Number History (this path also applies to Pelican Express).

## References { #tcat-home-references }

### Shipping Label ZIP Contents { #reference-tcat-home-zip-contents }

After the download, the ZIP contains four PDFs for different processes:

| File | Purpose | Recipient |
|---|---|---|
| **Shipping Label** | Used by EZCAT for pickup and delivery; print on EZCAT blank three-part shipping label stickers and stick on the package | Driver |
| **Packing Slip** | Packing slip included in the package, with items and quantities | Customer (in the package) |
| **Picking List** | Warehouse picking list, grouped by item for easy picking | Internal warehouse staff |
| **Order Details** | Complete order information, including amounts, payment method, and customer data | Internal records / customer service |



