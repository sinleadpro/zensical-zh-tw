---
title: "Can't Download Shipping Labels or Update Shipment Status"
description: "Common causes and fixes when shipping labels fail to download or shipment status doesn't update, including topping up ECPay prepaid logistics fees, browser blocking, address errors, and store closures or transfers."
created: 2026-06-08 20:12
last_modified: 2026-06-30 10:08
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
  - 下載託運單
  - 更新貨態
  - 補印託運單
  - 門市關轉處理
features:
  - 綠界金物流
  - 黑貓宅配
  - 順豐速運
  - 超商取貨
  - DHL 跨境物流
prerequisites: []
related:
  - ec/payments-and-logistics/apply-for-ecpay-payment-and-cvs-cod/
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
  - ec/orders/references/fulfillment-statuses/
  - ec/orders/cvs-shipping/cvs-c2c-shipping/
  - ec/orders/cvs-shipping/cvs-b2c-bulk-shipping/
  - ec/orders/returns-refunds/7-11-c2c-return/
  - ec/payments-and-logistics/dhl-cross-border-logistics/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/orders/payment-failed/
tags:
  - "Shipping Labels"
  - "Shipment Status Errors"
  - "Shipping Issues"
  - ECPay
  - "EZCAT Home Delivery"
  - "Convenience Store Pickup"
  - "Store Closure or Transfer"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4407
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/shipping-label-or-shipment-status-error/"
comments: false
search:
  exclude: false
icon: lucide/triangle-alert
hide: []
---
![Shipping label download errors](../../../assets/images/ec-訂單-所有訂單-下載託運單異常-hero.en.png){ title="Shipping Label Download Errors" .hero-page }

## About Shipping Label Errors { #intro-shipping-issue }

When you ship, download shipping labels, or track delivery status in the admin, you may occasionally find that "the shipping label won't download" or "the delivery status didn't update as expected." This page lists the most common causes and fixes to help you resolve issues quickly and finish shipping.

Most cases aren't system failures but issues you can fix yourself, such as your logistics account balance, browser settings, recipient information, or shipping label validity. Start by finding your situation in the quick reference table below, then go to the matching section.

## Quick Reference { #overview-shipping-issue }

| Your Situation | Most Likely Cause | Go To |
| :-- | :-- | :-- |
| No file after clicking download, but the delivery status changed to "Shipped" | The browser blocked automatic downloads | [No File After Clicking Download](#operate-shipping-issue-popup-blocked) |
| ECPay shipping labels keep failing to download | Insufficient prepaid logistics funds in your ECPay account | [ECPay Shipping Label Download Fails](#operate-shipping-issue-ecpay-balance) |
| EZCAT home delivery can't generate a tracking number | The recipient address has a typo or is incomplete | [Can't Generate a Tracking Number](#operate-shipping-issue-wrong-address) |
| Tracking number expired and delivery status can't be tracked | The package wasn't dropped off before the shipping label expired | [Expired Shipping Labels](#operate-shipping-issue-label-expired) |
| Convenience store pickup notice of a "store closure" | The pickup store closed or is under renovation | [Handle Store Closures](#operate-shipping-issue-store-closed) |
| The shipping label file is missing | You need to download it again | [Reprint Shipping Labels](#operate-shipping-issue-reprint) |


## Troubleshooting { #operate-shipping-issue }

### ECPay Shipping Label Download Fails { #operate-shipping-issue-ecpay-balance }

If you use ECPay payment and logistics integration and shipping label downloads keep failing, the most common cause is **an insufficient "prepaid logistics funds" balance in your ECPay account** to cover the logistics prepayment.

1. **Sign in to the ECPay admin:** Go to your ECPay merchant admin.
2. **Go to account management:** In the menu, click "Account Management" > "Prepayments."
3. **Top up:** Choose "Prepaid Logistics Funds" and enter the amount to deposit. The system generates an ATM payment account; complete the transfer.
4. **Download again:** After the funds arrive, return to the CYBERBIZ admin and download the shipping label again. The order's delivery status then updates to "Shipped."

For full top-up instructions, see the ECPay website: [Prepaid Logistics Funds Top-Up Guide :lucide-external-link:](https://support.ecpay.com.tw/9772/).

!!! note "Note"
    Prepaid logistics funds are a setting in your ECPay account and are separate from billing in the CYBERBIZ admin. If you still can't download after topping up, contact ECPay customer service to check your account status.

<div class="grid cards" markdown>

- :lucide-credit-card:{ .ig .middle } [__Apply for ECPay Payments and Convenience Store Cash on Pickup__](../../payments-and-logistics/apply-for-ecpay-payment-and-cvs-cod.md){ title="Apply for ECPay Payments and Convenience Store Cash on Pickup" }

</div>

---

### No File After Clicking Download { #operate-shipping-issue-popup-blocked }

If the system changed the delivery status to "Shipped" after you clicked download, but no file was downloaded, **the browser usually blocked automatic downloads** (especially when downloading multiple shipping labels at once).

1. **Check the delivery status first:** If the order changed to "Shipped," the system generated the shipping label successfully and only the file didn't download. You don't need to create a new label.
2. **Check browser blocking:** Look for a blocked download notice on the right side of the address bar, set this site to "Allow multiple downloads," and temporarily turn off ad-blocking extensions such as AdBlock.
3. **Get the file again:** Use **"Reprint Shipping Label"** to download the existing file again. You won't be charged again and no new tracking number is generated (see [Reprint Shipping Labels](#operate-shipping-issue-reprint)).

!!! tip "Tip"
    If you close or leave the page while downloading multiple orders, some orders may have changed to "Shipped" without their files downloaded. Use "Reprint Shipping Label" to get the files for all of those orders.

---

### EZCAT Home Delivery Can't Generate a Tracking Number { #operate-shipping-issue-wrong-address }

With **EZCAT home delivery**, the system doesn't support fuzzy address matching. If the recipient address has a typo (for example, a wrong Chinese character in a township name) or is incomplete, no tracking number can be generated.

=== "Not Shipped Yet"
    1. **Confirm the correct address:** Confirm the complete, correct recipient address with the customer.
    2. **Change the recipient information:** Change the address in the recipient information section of the order details page.
    3. **Download again:** After updating the address, download the shipping label again to generate a tracking number.

=== "Tracking Number Generated / Shipped"
    1. **Print the shipping label:** The address can no longer be changed in the system, so print the shipping label first.
    2. **Correct it by hand:** Write the correct address on the shipping label by hand.
    3. **Tell the driver:** Tell the driver the correct address when handing over the package.

<div class="grid cards" markdown>

- :lucide-truck:{ .ig .middle } [__Ship with EZCAT Home Delivery__](../home-delivery/tcat-home-delivery-v2.md)
- :lucide-settings:{ .ig .middle } [__Set Up and Print Extra EZCAT Shipping Labels__](../../payments-and-logistics/setup-print-tcat-waybill-v2.md)

</div>

---

### Expired Shipping Labels { #operate-shipping-issue-label-expired }

If a package isn't dropped off within the validity period after the shipping label is generated, the tracking number expires and the delivery status can no longer be tracked. The status may change to [Shipping Exception](../references/fulfillment-statuses.md#fulfillment-statuses-table){ title="Delivery Status Reference" data-preview } or "Shipment Canceled."

* **Home delivery:** CYBER Coins are deducted when you download the shipping label. If the package isn't actually shipped within **14 days**, the tracking number expires, and the deducted CYBER Coins are refunded to your account after it expires.
* **Convenience store B2C bulk shipping:** Deliver the goods to the convenience store logistics center within the deadline after the shipping label is generated. If overdue, the status changes to "Shipping Exception," the tracking number expires, and you need to get a new one.
* **Convenience store C2C store-to-store:** Drop off the goods at a convenience store within the deadline after the shipping label is generated. If overdue, the status changes to "Shipping Exception," the tracking number expires, and you need to get a new one.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Expiration Deadlines by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See each convenience store logistics service's reprint deadline and expiration rules.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for Expired Shipping Labels__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label has expired or the reprint deadline has passed, get a new tracking number and download a new shipping label.

</div>



---

### Handle Store Closures { #operate-shipping-issue-store-closed }

If the convenience store a customer chose for pickup closes or is under renovation (a store closure), the system sends a notification email. You need to contact the customer to choose a new store before the deadline.

1. **Contact the customer:** After receiving the store closure notice, confirm a new pickup store with the customer.
2. **Choose a new store:** On the order details page, in the store information section, click **"Choose Store Again"** to set the new pickup store.
3. **Finish before the deadline:** Choose a new store and report it to the carrier within each channel's deadline:
    * 7-Eleven (C2C store-to-store): **within 6 days**
    * 7-Eleven (B2C bulk shipping): **within 2 days**
    * FamilyMart: **within 6 days**
    * Hi-Life: Contact the customer **as soon as possible** to choose a new store

!!! info "Tip"
    If a new store isn't chosen by the channel's deadline, the package may be returned. Handle it as soon as you receive the notice.

<div class="grid cards" markdown>

- :lucide-store:{ .ig .middle } [__Convenience Store C2C Store Closures__](../cvs-shipping/cvs-c2c-shipping.md#operate-cvs-c2c-exception-store-closed)
- :lucide-package:{ .ig .middle } [__Handle Convenience Store B2C Store Closures__](../cvs-shipping/cvs-b2c-bulk-shipping.md#operate-cvs-b2c-shipping-store-change)
- :lucide-rotate-ccw:{ .ig .middle } [__7-Eleven C2C Return Store Closures__](../returns-refunds/7-11-c2c-return.md#operate-seven-eleven-c2c-return-pickup)

</div>

---

### Reprint Shipping Labels { #operate-shipping-issue-reprint }

If a shipping label file is lost, damaged, or didn't download, you can download the **already generated** shipping label again. You won't be charged again and no new tracking number is generated.

1. **Find the reprint option:** On the order list or order details page, click **"Reprint Shipping Label"** for a shipped order (for convenience store pickup orders, it's **"Reprint Store Barcode"**).
2. **Download again:** The system downloads the originally generated shipping label file again.

!!! note "Note"
    Reprints give you the original tracking number and shipping label, with no duplicate charge.

---

### DHL Shipping Exceptions { #operate-shipping-issue-dhl-problem }

If a DHL shipment runs into an exception in transit, CYBERBIZ contacts you to help resolve it and keeps tracking it after it's resolved until the delivery status updates to "Received." You don't need to do anything; just watch for customer service notifications.

<div class="grid cards" markdown>

- :lucide-globe:{ .ig .middle } [__DHL Cross-Border Logistics__](../../payments-and-logistics/dhl-cross-border-logistics.md){ title="DHL Cross-Border Logistics" }

</div>

---

## FAQ { #faq-shipping-issue }

??? quote "Nothing happens when I click download / Can't download shipping labels"
    [](){ #faq-shipping-issue-download-no-response }
    If the delivery status changed to "Shipped," the shipping label was generated successfully and only the file didn't download. Check the following in order:

    * Whether the browser blocked automatic downloads. Allow multiple downloads for this site.
    * Whether an extension such as AdBlock is blocking it. Turn it off temporarily and try again.
    * If you still can't get the file, use [Reprint Shipping Labels](#operate-shipping-issue-reprint) to download it again. You won't be charged again.

??? quote "What happens if I leave the page during a download?"
    [](){ #faq-shipping-issue-leave-page }
    If you leave the page while downloading multiple shipping labels, the download stops, and some orders may have changed to "Shipped" without their files. Use [Reprint Shipping Labels](#operate-shipping-issue-reprint) to download them again for all of those orders, with no duplicate charge.

??? quote "Do reprinted shipping labels cost extra?"
    [](){ #faq-shipping-issue-reprint-fee }
    No. Reprints give you the originally generated tracking number and shipping label file. It's a re-download, so there's no duplicate charge and no new tracking number.

??? quote "I found the recipient address was wrong after shipping"
    [](){ #faq-shipping-issue-address-after-ship }
    Once a shipping label is generated (especially for EZCAT home delivery), the address can no longer be changed in the system. Print the shipping label, correct the address by hand, and tell the driver when handing over the package.

## Next Steps { #next-steps-shipping-issue }

<div class="grid cards" markdown>

- :lucide-package-check:{ .lg }  
  [__Partial Shipment for Orders__](../home-delivery/partial-shipment-v2.md)  
  How to ship only some items in an order first.

- :lucide-banknote-x:{ .lg }  
  [__Troubleshoot Failed Payments__](../payment-failed.md)  
  What to do when a customer's payment fails or an order is stuck awaiting payment.

</div>

## References { #reference-shipping-issue }

* [Delivery Status Reference](../references/fulfillment-statuses.md)

