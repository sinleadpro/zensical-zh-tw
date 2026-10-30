---
title: "Ship with Convenience Store B2C Bulk Shipping"
description: "Batch download shipping labels and generate tracking numbers from the order list, then send consolidated packages to the convenience store logistics center, which distributes them to the stores shoppers chose."
created: 2026-05-25 20:35
last_modified: 2026-07-01 12:30
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
difficulty: intermediate
tnb: branch
plans:
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: 
  - CYBERBIZ PAYMENTS
intents:
  - 批次下載託運單
  - B2C 大宗寄倉出貨
features:
  - B2C 大宗寄倉
  - 託運單批次下載
prerequisites:
  - ec/payments-and-logistics/setup-cvs-b2c-bulk-shipping/
related:
  - ec/payments-and-logistics/setup-cvs-b2c-bulk-shipping/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/payments-and-logistics/references/cvs-b2c-logistics-center-reference/
  - ec/orders/references/cvs-waybill-expiration-reference/
  - ec/orders/renew-waybill-after-expiration/
  - ec/payments-and-logistics/references/cvs-b2c-channel-spec-reference/
  - ec/website-management/points-deposits/
tags:
  - "Convenience Store B2C Bulk Shipping"
  - "B2C Shipping"
  - "Shipping Labels"
  - "Convenience Store Pickup"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=122
  - https://www.cyberbiz.io/support/?p=977
permalink: "https://help.cyberbiz.io/ec/orders/cvs-shipping/cvs-b2c-bulk-shipping/"
comments: false
search:
  exclude: false
icon: lucide/warehouse
hide: []
---

![Download B2C shipping labels](../../../assets/images/EC-訂單-所有訂單-下載B2C託運單-hero.en.png){ title="Download B2C Shipping Labels" .hero-page }

## About Convenience Store B2C Bulk Shipping { #intro-cvs-b2c-shipping }

1. In the order list, select orders with the same channel and payment status
2. Download shipping label PDFs in bulk from "More Actions"
3. Pack the items and stick a label on each package
4. Arrange a carrier yourself to send the large boxes to the convenience store logistics center

## Prerequisites and Limitations { #prerequisites-cvs-b2c-shipping }

- [x] **Channel set up and turned on**: Complete the application, label test, and activation in "[Set Up Convenience Store B2C Bulk Shipping](../../payments-and-logistics/setup-cvs-b2c-bulk-shipping.md){ title="Set Up Convenience Store B2C Bulk Shipping" }" first.
- [x] **Order status**: The payment status must be "**Payment Received**" or "**Cash on Delivery**," and the delivery status must be "**Unshipped**" or "**Processing**."
- [x] **Same channel per batch**: Selected orders must use the same convenience store (for example, all 7-Eleven). Process different channels in separate batches.
- [x] **Sufficient CYBER Coin balance**: Standard Plan merchants need enough balance to cover shipping fees.

## Steps { #operate-cvs-b2c-shipping }

### Download Shipping Labels { #operate-cvs-b2c-shipping-download }

1. **Open order management**: Sign in to the admin and go to "**Orders**" > "**All Orders**."
2. **Select orders**: Select the orders to ship in the order list. **Make sure all selected orders use the same delivery method** (for example, all 7-Eleven pickup).
3. **Download**: Open the "**Actions...**" drop-down in the upper right and select "**Print B2C bulk shipping labels and change to 'Shipped'**"[^1].
4. **Confirm**: When the dialog asks "Print B2C bulk shipping labels and change to Shipped?", click **Yes**.
5. **Download the files**: The system generates tracking numbers and downloads an archive with the shipping data. The delivery status in the order list changes to "**Shipped**," and the order details page shows "[Shipped (Awaiting Carrier Pickup)](../home-delivery/shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" }."

![Download B2C bulk shipping labels](../../../assets/images/EC-訂單-所有訂單-下載b2c大宗託運單.en.png){ title="Download B2C Bulk Shipping Labels" }

[^1]: The drop-down options change based on the channel of the selected orders. For FamilyMart frozen orders, the option is "Download FamilyMart cold chain shipping labels and change to 'Shipped'."

!!! warning "Stay on the Page While Downloading"
    If you close the window while the system generates tracking numbers in the background, **some orders may already be "Shipped" without their shipping labels downloaded**. Get them again with [Reprint Shipping Labels](#operate-cvs-b2c-shipping-reprint){ title="Reprint Shipping Labels" }.

---

### Handle Shipping Documents { #operate-cvs-b2c-shipping-documents }

The downloaded archive contains the following documents. Handle each according to its purpose:

| Document | Purpose |
| :-- | :-- |
| Shipping label (sender data) | **Stick it on the outside of the order's package** for scanning at the logistics center |
| Packing slip | For internal picking reference |
| Order details | Put in the package for the customer to check |
| Pick list | For internal picking checks |

!!! tip "Printing Tips"
    * Print shipping labels with a **laser printer** on **2x3 stickers** so barcodes are readable.
    * Stick the label flat on the **upper-left corner** of the package. Don't fold the barcode and QR code or cover them with tape.

---

### Drop Off at the Logistics Center { #operate-cvs-b2c-shipping-deliver }

Deliver the items to the logistics center before the deadline. Expired tracking numbers become invalid automatically, and you need to get new ones.

1. **Packing**: Put the individually labeled items **together in large boxes**, not loose. You're responsible for damage caused by missing outer boxes.
2. **Arrange a carrier**: Arrange a third-party carrier yourself (such as EZCAT, Pelican Express, or HCT Logistics) to send the large boxes to the matching logistics center.
    - For full receiving addresses, hours, and receiving units, see
[Logistics Center Receiving Information](../../payments-and-logistics/references/cvs-b2c-logistics-center-reference.md#reference-cvs-b2c-centers-list){ title="Logistics Center Receiving Information" data-preview }.
    - [Packing and delivery vehicles by channel](../../payments-and-logistics/references/cvs-b2c-logistics-center-reference.md#reference-cvs-b2c-acceptance-rules){ title="Logistics Center Receiving Information" data-preview }.
3. **Logistics center receipt**: After the logistics center receives the goods, the order status changes from "Awaiting Carrier Pickup" to "[Shipped (In Transit)](../home-delivery/shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" data-preview }" automatically.

!!! tip "Pickup SMS Notifications"
    After the items arrive at the customer's chosen store, the system sends pickup SMS notifications on **day 1** and **day 4**.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Validity by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See each convenience store's reprint deadline and expiration rules.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label has expired or is past the reprint deadline, get a new tracking number and download a new shipping label.

</div>


---

### Reprint Shipping Labels { #operate-cvs-b2c-shipping-reprint }

If a label is lost or damaged, you can reprint it in the admin before the deadline.

1. Select the orders to reprint in the order list.
2. Open the **Actions...** drop-down and select **Reprint Shipping Label**.
3. The system downloads the PDF with the same tracking number again. **Shipping fees aren't charged again**, and the order status doesn't change.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Validity by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See each convenience store's reprint deadline and expiration rules.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label has expired or is past the reprint deadline, get a new tracking number and download a new shipping label.

</div>

---

### Store Closures { #operate-cvs-b2c-shipping-store-change }

If the customer's pickup store closes (for renovation, permanent closure, and so on), the system emails you. The deadlines for contacting the customer by channel are:

| Channel | Contact Deadline |
| :-- | :-- |
| 7-Eleven | Within **2 days** of the notification email |
| FamilyMart (ambient/frozen) | Within **6 days** of the notification email |
| Hi-Life | Within **2 days** of the notification email |

1. **Contact the customer**: After receiving the email, contact the customer within the deadline above to confirm a new pickup store.
2. **Choose a new store**: Find the order in the admin, open the order details page, and **choose a new pickup store**.
3. **Confirm the update**: After you confirm, the system updates the shipping information automatically.

!!! warning "Risk of Missing the Deadline"
    If you don't choose a new store within the channel's deadline, the package may be returned. Handle it as soon as you're notified.

---

## Important Rules and Limitations { #specs-cvs-b2c-shipping }

* **Shipping can't be undone**: Once you download shipping labels, the order status changes to "Shipped," and **the delivery information can't be changed**. Check the data before downloading.
* **Insufficient CYBER Coins block downloads**: If a Standard Plan merchant doesn't have enough CYBER Coins, the system blocks the download and shows "Insufficient CYBER Coin balance."
* **Weight and size limits**: If an order's total weight or size exceeds the channel's limit, shipping labels can't be generated. See
[Weight and Size Limits](../../payments-and-logistics/references/cvs-b2c-channel-spec-reference.md#reference-cvs-b2c-channels-specs){ title="Convenience Store B2C Bulk Shipping Channel Specifications" data-preview }.
* **Receiving inspection rules**: [Receiving inspection rules by channel](../../payments-and-logistics/references/cvs-b2c-logistics-center-reference.md#reference-cvs-b2c-acceptance-rules){ title="Logistics Center Receiving Information" data-preview }.

---

## Next Steps { #next-steps-cvs-b2c-shipping }

<div class="grid cards" markdown>

- :lucide-settings:{ .lg }  
  [__Set Up Convenience Store B2C Bulk Shipping__](../../payments-and-logistics/setup-cvs-b2c-bulk-shipping.md){ title="Set Up Convenience Store B2C Bulk Shipping" }  
  Channel not set up yet? Complete the application and activation first.

- :lucide-coins:{ .lg }  
  [__Top Up CYBER Coins__](../../website-management/points-deposits.md){ title="CYBER Coins Top-Up Center Guide" }  
  Standard Plan merchants: make sure your balance covers shipping fees for large order volumes.

</div>

## FAQ { #faq-cvs-b2c-shipping }

??? quote "Why is the download shipping labels button blocked?"
    [](){ #faq-cvs-b2c-shipping-blocked }

    Possible reasons:

    - The selected orders include **different channels** (for example, both 7-Eleven and FamilyMart)
    - The order payment status doesn't match (it must be "Payment Received" or "Cash on Delivery")
    - The order delivery status is already "Shipped" or "Canceled"
    - Insufficient CYBER Coin balance

??? quote "What if nothing happens when I click download shipping labels?"
    [](){ #faq-cvs-b2c-shipping-no-response }

    Check whether the browser is **blocking pop-ups or automatic downloads**, add the CYBERBIZ admin domain to the allow list, and try again. If nothing happens, try another browser (Chrome or Edge recommended) or clear the browser cache and try again.

??? quote "What happens if I leave the page while downloading?"
    [](){ #faq-cvs-b2c-shipping-leave }

    The download is interrupted, and **some orders may already be "Shipped" before their shipping labels finish downloading**. Reprint the shipping labels to get the PDFs again.


??? quote "Does reprinting shipping labels deduct CYBER Coins again?"
    [](){ #faq-cvs-b2c-shipping-reprint-cost }

    No. Reprinting only downloads the PDF for the existing tracking number again. It doesn't create a new tracking number, charge again, or change the order status.

??? quote "Can I change the delivery information after downloading shipping labels?"
    [](){ #faq-cvs-b2c-shipping-edit }

    **No**. Downloading shipping labels means the shipping request is complete, and the address, store, and recipient can't be changed. If the store closes, follow "[Store Closures](#operate-cvs-b2c-shipping-store-change){ title="Store Closures" }."

??? quote "Can I download for different convenience stores at once?"
    [](){ #faq-cvs-b2c-shipping-mixed }

    No. Each bulk action can include orders from only one channel. Process each channel in a separate batch.

??? quote "How do I confirm the logistics center has received the goods?"
    [](){ #faq-cvs-b2c-shipping-confirm-receipt }

    After the logistics center signs for the goods, the order status changes from "Awaiting Carrier Pickup" to "**[Shipped (In Transit)](../home-delivery/shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" }**" automatically. Check the latest status in the order list or on the order details page.

??? quote "What's the difference between B2C bulk shipping and regular C2C convenience store pickup?"
    [](){ #faq-cvs-b2c-shipping-vs-c2c }

    **B2C bulk shipping** suits merchants who ship in large volumes. You download shipping labels in bulk, pack everything together, and send it to the convenience store logistics center, which distributes it to each store. **C2C store-to-store** requires shipping each order at a store kiosk, which suits occasional orders better.

??? quote "What should I watch out for when printing shipping labels?"
    [](){ #faq-cvs-b2c-shipping-label-printing }

    Use a **laser printer** with **2x3 stickers** so barcodes are readable. Stick the label flat on the **upper-left corner** of the package, and don't fold the barcode and QR code or cover them with tape.


