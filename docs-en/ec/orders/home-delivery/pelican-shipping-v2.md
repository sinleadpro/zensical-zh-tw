---
title: "Ship with Pelican Express"
description: "Ship with Pelican Express, including batch downloading shipping labels, single and partial shipments, and reprinting shipping labels, plus shipping fee rules and FAQs."
created: 2026-05-19 21:30
last_modified: 2026-10-01 14:25
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
cyb_extensions: []
intents:
  - 宅配通出貨操作
  - 批次下載託運單
  - 補印託運單
  - 宅配通逆物流退貨
features:
  - 宅配通託運單
  - 批次出貨
  - 單筆出貨
  - 補印託運單
  - 加印託運單
  - 逆物流退貨
prerequisites:
  - ec/payments-and-logistics/setup-pelican-waybill-v2/
tags:
  - "Pelican Express"
  - Shipping
  - "Shipping Labels"
  - "Logistics and Delivery"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
  - 金物流 > 宅配通託運單
  - 宅配託運單管理 > 宅配通託運單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=63
  - https://www.cyberbiz.io/support/?p=975
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/pelican-shipping-v2/"
comments: false
search:
  exclude: false
icon: lucide/bird
hide: []
---

![Download Pelican Express shipping labels](../../../assets/images/EC-訂單-所有訂單-下載宅配通託運單-hero.en.png){ title="Download Pelican Express Shipping Labels" .hero-page }

## About Pelican Express Shipping { #intro-pelican }

After you activate logistics integrated with Pelican Express, you can generate official Pelican Express shipping label PDFs directly in the admin, and the system automatically updates the order's delivery status to "Shipped (Awaiting Carrier Pickup)." No handwritten labels or separate tracking entry needed.

This article focuses on **day-to-day shipping**, including downloading shipping labels in bulk, single-order and partial shipments, and reprinting shipping labels. For advanced management such as sender settings, extra shipping labels (multiple boxes per order), and reverse logistics returns, see the [Pelican Express shipping label management page](../../payments-and-logistics/setup-pelican-waybill-v2.md){ title="Set Up Pelican Express Shipping Labels" }.

!!! info "Important Rules"
    * **Handwritten labels are prohibited**: Integrated logistics must use system-generated shipping labels. Handwritten labels can't report delivery status, which affects reconciliation and customer service.
    * **Special areas and sizes**: Some [outlying islands and remote areas](#reference-pelican-exclusion), special sizes, and special goods may not be deliverable or may incur surcharges per Pelican Express announcements. Actual delivery and fees follow Pelican Express announcements.
    * **Cold chain products**: Pelican Express low-temperature delivery isn't available yet. Use another logistics option.

## Prerequisites and Limitations { #prerequisites-pelican }

### Billing { #prerequisites-pelican-billing-mode }

| Merchant type | Billing | Printing requirement |
| :-- | :-- | :-- |
| Standard Plan | **CYBER Coins** deducted in advance from your account balance | Can't print with an insufficient balance; top up in the Top-Up Center first |
| PLUS / Enterprise | Billed on each **statement** | No top-up needed |

!!! info "Tip"
    If you're not sure which billing applies to you, open the "Pelican Express Shipping Labels" page. If the top shows "Current CYBER Coin balance," you're on the Standard Plan; if it shows statement information, you're on PLUS / Enterprise.

---

### Shipping Setup { #prerequisites-pelican-preconfig }

Before shipping with Pelican Express for the first time, complete the following:

- [x] **Pelican Express sender address** (for batch shipping): Set the sender address in "Payment and Logistics" > "[Pelican Express Shipping Labels](../../payments-and-logistics/setup-pelican-waybill-v2.md#configure-pelican-shipping-note-sender){ title="Set Up Sender Information" }." Without it, you'll see an "Incomplete sender information" message when shipping.
- [x] **Pelican Express sender information** (for extra shipping labels and reverse logistics): Fill it in under "Pelican Express Settings" on the "Payment and Logistics" > "Pelican Express Shipping Labels" page. For details, see the [Pelican Express shipping label management page](../../payments-and-logistics/setup-pelican-waybill-v2.md#configure-pelican-shipping-note-sender){ title="Set Up Sender Information" }.

---

### Shipping Label Stickers and Equipment { #prerequisites-pelican-preparations }

* Shipping labels must be printed on the official **"Pelican Express three-part blank shipping label stickers"** so the generated content lines up with the fields.
* Getting stickers: Contact CYBERBIZ customer service for your "customer code" first, then call Pelican Express to request stickers.
* We recommend a **laser printer**, so barcodes don't fade or blur and cause scanning failures.
* Never ship with handwritten documents. The system can't track delivery status, and later reconciliation and complaints can't be handled.

---

### Order Requirements { #prerequisites-pelican-order-status }

Orders shipped with Pelican Express must meet the following:

* The order's **delivery method is Pelican Express** (in batch shipping, selected orders with other logistics types can't be downloaded together).
* The payment status is "Paid" or "Cash on Delivery."
* The delivery status is "Unshipped," "Partially Shipped," "Preparing," or "Shipping Exception."

## Steps { #operate-pelican }

### Download Shipping Labels in Bulk and Update Delivery Status { #operate-pelican-bulk-download }

When you have many Pelican Express orders to ship at once, batch processing from the order list is most efficient.

1. **Go to the order list**: Go to "Orders" > "All Orders" in the admin.
2. **Filter Pelican Express orders**: We recommend filtering "Delivery Method" by "Pelican Express" first, so all selected orders use the same logistics[^1].
3. **Select orders to ship**: Select the orders on the left of the order list (you can select across pages or the whole page).
4. **Run the batch action**: Open the "Actions" drop-down above the list and select **"Download Pelican Express Shipping Labels and Change Delivery Status to 'Shipped'"**.

    ![Download Pelican Express shipping labels](../../../assets/images/EC-訂單-所有訂單-下載宅配通託運單.en.png){ title="Download Pelican Express Shipping Labels" }

5. **Review the shipping fees**: The middle of the pop-up lists the CYBER Coins or statement amount for this batch. Make sure it's what you expect.
6. **Confirm the sender address**: Defaults to the sender address last used for this logistics service (the first time, it uses the address in [Pelican Express settings](../../payments-and-logistics/setup-pelican-waybill-v2.md#configure-pelican-shipping-note-sender){ title="Set Up Sender Information" }). To change it, click **Change**[^4].

    ![Confirm the sender address](../../../assets/images/ec-orders-pelican-waybill-popup-address.en.png){ title="Confirm the Pelican Express Shipping Label Address" }

7. **Agree to the terms**: Select **"I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and Pelican Express contract terms"** at the bottom.
8. **Confirm the download**: Click **"Confirm."** The system creates shipping labels, deducts shipping fees, and updates the order delivery status to "[Shipped (Awaiting Carrier Pickup)](shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" data-preview }."

    !!! warning "Recipient Information Can't Be Changed After Printing"
        Once you download a shipping label, the recipient information is tied to it and can't be changed in the admin. To change it, the shipping label must be canceled (contact CYBERBIZ customer service) and created again.

9. **Get the shipping label files**: The system automatically downloads an [archive](../references/order-filter-status-reference.md#reference-logistics-zip-contents){ title="Shipping Label Download Contents" data-preview } with shipping label PDFs and related shipping documents. Print the labels on "Pelican Express three-part blank shipping label stickers" and stick them on the boxes.
10. **Schedule pickup**: After printing, contact Pelican Express customer service to schedule pickup, or prepare for your regular pickup time agreed with Pelican Express. After pickup, the status on the order details page shows "[Shipped (In Transit)](shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" data-preview }."

[^1]: If the selected orders include non-Pelican Express orders (such as EZCAT or convenience store pickup), the pop-up won't open or shows an error on submit. Use the "Delivery Method" filter first to keep the logistics type consistent in the batch.
[^4]: Changes also update the address on that logistics page. Addresses for different logistics services and the company logistics address don't affect each other.

---

### Single-Order and Partial Shipment { #operate-pelican-single-shipment }

To ship **a single order**, or only some items in an order first, use the order details page instead.

1. Go to "Orders" > "All Orders" and click the order number to open the order details page.
2. In the "Shipping" section on the right, select the items to ship now.
3. In the "Select Shipping Method" drop-down, choose "Pelican Express Shipping Label."
4. In the "Select a fee" drop-down, choose the matching delivery size.
5. Select or deselect "Send email notification to customer" as needed.
6. Click **"Confirm Shipment."** The system creates the shipping label and deducts the shipping fee.

For the detailed partial shipment process, differences between logistics services, and FAQ, see [Partial Shipment for Orders](partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }.

---

### Reprint Shipping Labels <small>Damaged or Lost</small> { #operate-pelican-reprint }

If a shipping label was already downloaded but the sticker was misprinted or lost, or you want to print the same label again, use reprint. **Reprinting doesn't generate a new tracking number or charge you again.**

1. Go to "Orders" > "All Orders."
2. Filter or select Pelican Express orders with status "Shipped."
3. Select **"Reprint Shipping Label"** from the "Actions" drop-down.
4. The system regenerates the original shipping label PDF. Print it on Pelican Express three-part blank shipping label stickers.

!!! info "Tip"
     Reprinting only prints the PDF again for **existing tracking numbers**. To generate **new tracking numbers** for the same order (for example, to ship in multiple boxes), use [Print Extra Shipping Labels](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-note-add-print){ title="Print Extra Shipping Labels" } instead.

## Next Steps { #followup-pelican }

<div class="grid cards" markdown>

- :lucide-truck:{ .lg }  
  [__Track Delivery Status__](shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" }  
  After shipping, the delivery status changes to "Shipped (Awaiting Carrier Pickup)." After Pelican Express picks up and scans the package, the status updates step by step, such as In Transit and Delivered, based on carrier updates.

- :lucide-receipt:{ .lg }  
  [__View Reconciliation Records__](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-records){ title="Records and Reconciliation" }  
  The tracking number history at the bottom of the "Pelican Express Shipping Labels" page lists each shipping label's order number, tracking number, amount deducted, and status for reconciliation.

- :lucide-printer:{ .lg }  
  [__Print Extra Labels or Handle Returns__](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-note-add-print){ title="Print Extra Shipping Labels" }  
  To ship one order in multiple boxes or handle customer returns, print extra shipping labels or create reverse logistics on the Pelican Express shipping label management page.

</div>

---

## FAQ { #faq-pelican }

??? quote "The "Download Pelican Express Shipping Labels and Change Delivery Status to 'Shipped'" option is missing?"
    [](){ #faq-pelican-action-missing }

    Check the following in order:

    * Whether the selected orders include **non-Pelican Express** logistics types (mixed selections can't be batch processed)
    * Whether the order payment status is "Paid" or "Cash on Delivery"

??? quote "What if I don't have enough CYBER Coins?"
    [](){ #faq-pelican-insufficient-points }

    Standard Plan merchants must top up CYBER Coins in the "Top-Up Center" before printing shipping labels. PLUS / Enterprise merchants don't have this limit; shipping fees are included on each statement.

??? quote "If I download a shipping label but don't ship, are the CYBER Coins refunded automatically?"
    [](){ #faq-pelican-unused-refund }

    Yes. If the package **isn't actually shipped within two weeks (14 days)** of downloading, the system automatically refunds that label's shipping fee and marks the tracking number "Shipment Canceled."

??? quote "To ship one order in multiple boxes, should I use "Partial Shipment" or "Print Extra Shipping Labels"?"
    [](){ #faq-pelican-multibox }

    How to decide:

    * Items **ship all at once but don't fit in one box** > Use [Print Extra Shipping Labels](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-note-add-print){ title="Print Extra Shipping Labels" } to create multiple tracking numbers for the same order, one per box.
    * Items **ship in batches** (for example, ship some now and the rest when restocked) > Use "Partial Shipment" and select the items to ship on the order details page.
    * Cash on Delivery orders shipped in multiple boxes **must** use extra shipping labels (the collected amount must be tied to a tracking number).

??? quote "What's the difference between "Reprint Shipping Label" and "Print Extra Shipping Labels"?"
    [](){ #faq-pelican-reprint-vs-addprint }

    * **Reprint Shipping Label**: Prints the PDF again for **an existing tracking number**. No new tracking number is generated, and **you aren't charged again**. Use it when a sticker is misprinted or the file is lost.
    * **Print Extra Shipping Labels**: Creates **new tracking numbers** for the same order. **Each label is charged separately**, and the system fills in the original order information. Use it to ship one order in multiple boxes.

??? quote "Can I use handwritten Pelican Express shipping labels?"
    [](){ #faq-pelican-handwritten }

    No. Integrated logistics must use system-generated shipping labels so the system can receive delivery status updates from Pelican Express. Handwritten labels prevent package tracking, and reconciliation and complaints can't be handled.

??? quote "Can I use Pelican Express for outlying islands or remote areas?"
    [](){ #faq-pelican-remote-area }

    Some outlying islands (such as Penghu, Kinmen, and Matsu), remote areas, and special addresses (such as P.O. boxes) may not be deliverable or may incur surcharges per Pelican Express announcements. Actual delivery coverage and fees follow official Pelican Express announcements; we recommend checking with the customer before shipping.

## References { #reference-pelican }



### Areas Pelican Express Doesn't Serve { #reference-pelican-exclusion }

Pelican Express doesn't deliver to the following areas:

- **Penghu**: Wang'an Township, Qimei Township, Hujing Island, Tongpan Island, Dacang Islet, Yuanbei Islet, Niao Islet, Hua Islet, Jibei Islet.
- **Kinmen**: Wuqiu, Lieyu, Dadan, Erdan.
- **Matsu (Lienchiang County)**: Nangan Township, Beigan Township, Juguang Township, Dongyin Township.
- **Other**: Outlying islands such as Orchid Island, Green Island, and Xiaoliuqiu, and P.O. boxes.

!!! info "Friendly Reminder"
    Service coverage for outlying islands and remote areas may change. For the latest detailed service areas, check the [Pelican Express official website - Service Locations :lucide-external-link:](https://www.e-can.com.tw/m/search_Location.aspx).
