---
title: "Ship with SF Express"
description: "Ship by downloading SF Express shipping labels in batches or one at a time. The system gets tracking numbers from SF Express in real time and updates the order shipment status to Shipped. Supports delivery on Taiwan's main island and overseas."
created: 2026-05-20 20:25
last_modified: 2026-08-20 16:00
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
  - 批次下載順豐託運單
  - 順豐出貨流程
  - 順豐部分出貨
  - 順豐海外宅配出貨
features:
  - 順豐託運單
  - 順豐海外宅配
  - 順豐OpenAPI
prerequisites:
  - 需先完成順豐設定（寄件人地址）
  - 需先完成公司統一編號設定
  - 需先開通順豐託運單功能
related:
  - ec/payments-and-logistics/setup-sf-express-waybill-v2/
  - ec/website-management/setup-store-basic-info/
  - ec/payments-and-logistics/sf-express-overseas-logistics/
  - ec/payments-and-logistics/home-delivery-cash-on-delivery/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/orders/home-delivery/partial-shipment-v2/
tags:
  - "SF Express"
  - Shipping
  - "Shipping Labels"
  - "Overseas Home Delivery"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
  - 金物流 > 順豐託運單
  - 一般設定 > 公司聯絡資訊
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=384
  - https://www.cyberbiz.io/support/?p=3760
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/sf-express-shipping-v2/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![Download SF Express shipping labels](../../../assets/images/EC-訂單-所有訂單-下載順豐託運單-hero.en.png){ title="Download SF Express Shipping Labels" .hero-page }

## About SF Express Shipping { #intro-sf }

In the CYBERBIZ admin, you can download **S.F. Express shipping labels** for orders with the "SF Express" delivery method, in bulk or one at a time, and change their delivery status to "Shipped" at the same time. The system gets tracking numbers from SF Express in real time, so you don't need handwritten labels or to sign in to the SF Express system separately.

The downloaded ZIP archive contains shipping labels you can stick directly on packages. International shipments also include a **commercial invoice** for export customs declaration.

## Prerequisites and Limitations { #prerequisites-sf }

### Required Setup { #prerequisites-sf-config }

Before using SF Express shipping labels for the first time, complete the following. Missing any of them prevents shipping labels from being generated or leaves sender information incomplete:

- [x] **SF Express sender address**: Set the sender address in "Payment and Logistics" > "[SF Express Shipping Labels](../../payments-and-logistics/setup-sf-express-waybill-v2.md#configure-sf-waybill-sender){ title="Set Up SF Express Shipping Labels" }." Without it, you'll see an "Incomplete sender information" message when shipping.
- [x] **Company tax ID**: Go to "General Settings" > "[Company Contact Information](../../website-management/setup-store-basic-info.md#operate-general-preferences-company-info){ title="Set Up Basic Website Information" }" and enter your tax ID. **Required for international shipments[^1]**.
- [x] **SF Express sender information** (optional): If you want the sender phone on the shipping label to differ from your "Company Contact Information," specify a sender name and phone on the **SF Express shipping label settings page**. For details, see [Set Up SF Express Sender Information](../../payments-and-logistics/setup-sf-express-waybill-v2.md#configure-sf-waybill-sender){ title="SF Express Settings" data-preview }.

[^1]: International shipping labels can't be generated without a tax ID.

---

### Delivery Coverage { #prerequisites-sf-coverage }

* **Domestic**: Only Taiwan's main island (**On shore of Taiwan**) is supported. The system checks the recipient address automatically. **Shipping labels can't be generated for outlying islands (Penghu, Kinmen, Matsu, Green Island, Orchid Island, etc.)**; use another delivery method.
* **Oversea Country**: If you've enabled "[SF Express International Home Delivery](../../payments-and-logistics/sf-express-overseas-logistics.md){ title="SF Express International Logistics" }," you can ship to China, Hong Kong, Macao, and other countries SF Express supports. The system automatically switches to English shipping labels based on the recipient's country.

---

### Payment Status Requirements { #prerequisites-sf-payment }

* The order's payment status must be **Paid**.
* **SF Express doesn't support Cash on Delivery**. For Cash on Delivery, use [EZCAT, Pelican Express, or HCT Logistics Cash on Delivery](../../payments-and-logistics/home-delivery-cash-on-delivery.md).

## Steps { #operate-sf }

### Download SF Express Shipping Labels in Bulk { #operate-sf-bulk-shipping }

Process multiple SF Express orders at once, printing shipping labels and updating the delivery status to "Shipped."

1. **Go to the order list**: Go to "Orders" > "All Orders" in the admin.
2. **Select orders**: Select the orders to ship. **All selected orders must use SF Express as the delivery method[^2]**.
3. **Choose an action**: Open the **"Actions"** drop-down above the list and select **"Download SF Express Shipping Labels and Change Delivery Status to 'Shipped'"**.

    ![Download SF Express shipping labels](../../../assets/images/ec-orders-sf-waybill-download.en.png){ title="Download SF Express Shipping Labels"}

4. **Set download options**: The "Download SF Express Shipping Labels" window opens. Check the following in order
    * **Order list**: Shows the selected order numbers and delivery methods. Check them before continuing.
    * **Package sizes and fees**: The window shows a price table listing the CYBER Coin fee for each size for reference[^3].
    - **Estimated CYBERBIZ Coin**: Standard Plan[^4] merchants see the CYBER Coins to be deducted, the current account balance, and a "Top Up" button in the window.
    * **Sender Address**: Defaults to the sender address last used for this logistics service (the first time, it uses the address in [SF Express settings](../../payments-and-logistics/setup-sf-express-waybill-v2.md#configure-sf-waybill-sender){ title="Set Up SF Express Shipping Labels" }). To change it, click **Change** in the window[^6].

    ![Download SF Express shipping labels pop-up](../../../assets/images/ec-orders-sf-waybill-download-popup.en.png){ title="Download SF Express Shipping Labels Pop-Up"}

5. **Read the notes**: The window lists shipping reminders[^5]. Read them before continuing.
6. **Agree to the terms**: Select **"I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and SF Express contract terms"** (selected by default) to enable the confirm button.
7. **Click "Download"**: The system calls SF Express to get a tracking number for each selected order and downloads a ZIP [archive](#reference-sf-bulk-shipping-files).
8. **Check the results**: After the download, the delivery status of those orders in the order list changes to **"[Shipped (Awaiting Carrier Pickup)](shipping-status-tooltip.md#shipping-status-text-type){ title="Shipment Status Tooltip Text" data-preview }"**, and the tracking number is recorded on the order details page.

[^2]: Otherwise, the system blocks the action and shows "Order X doesn't support SF Express shipping labels."
[^3]: The system determines the size to charge automatically from the volume of the order items; you don't need to choose it.
[^4]: PLUS / Enterprise plans don't show this section. Fees go directly on the statement, so you don't need to check your balance before printing.
[^5]: Split oversized packages, shipping label expiration rules, peak-season surcharges, fees when customers refuse delivery, and rules for special locations.
[^6]: Changes also update the address on that logistics page. Addresses for different logistics services and the company logistics address don't affect each other.

---

### Archive Contents { #reference-sf-bulk-shipping-files }

After a successful download, the ZIP contains the following:

| Document | Purpose | Print? |
| :-- | :-- | :-- |
| Shipping label - sender information | Stick on the outside of the package for the SF Express driver to scan | **Required** |
| Shipping details | For internal order checking and packing | Optional |
| Order details | Can be sent with the package so the customer can check items | Optional |
| Pick list | For warehouse staff to pick items | Optional |
| Commercial invoice (international only) | For customs declaration, in English | **Required for international shipments** |

!!! info "Tip"
     We recommend printing shipping labels with a **laser printer**, so barcodes don't smear (inkjet) or fade (thermal paper) and become unreadable by SF Express, requiring a reprint.

---

### Partial Shipment { #operate-sf-partial-shipping }

When only some items in an order can ship first, open the **order details page**, select the items to ship in the "Shipping" section, choose **SF Express shipping label** in the "Select Shipping Method" drop-down, and click "Confirm Shipment."

For the full partial shipment process (shared by all logistics services), see [Partial Shipment for Orders](partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }.

---

### Schedule a Driver Pickup { #operate-sf-driver-pickup }

After downloading shipping labels, contact SF Express to arrange pickup:

* **Booking line**: **412-8830** (from a mobile phone, dial **02-412-8830**).
* **Tell the driver**: You're using **shipping labels generated through CYBERBIZ system integration**, so **no customer code is needed**. The driver can scan the labels on site.
* After the driver picks up, the order's delivery status in the admin automatically changes to **"Shipped (In Transit)"**, and then to **"Shipped (Delivered)"** when delivered to the customer.

## Important Rules and Limitations { #specs-sf }

### Shipping Label Expiration and Refunds { #specs-sf-expiration }

CYBER Coins are deducted (or billed) when you download shipping labels. If a package isn't actually shipped **within 14 days**, the system marks it "Customer canceled shipment" based on the status returned by SF Express, changes the tracking number status to **"Shipment Canceled,"** and fully refunds the deducted CYBER Coins to your account (for statement-billed plans, the charge isn't billed).

* Refund timing **depends on the status returned by the SF Express system**; it isn't refunded exactly when 14 days pass.
* When the refund is credited, the admin's "CYBER Coin History" notes **"Order XXX, SF Express tracking number XXX not shipped for over two weeks, X CYBER Coins refunded."**

---

### Package Size Recommendations { #specs-sf-size }

* We recommend **no more than 170 cm** (length + width + height) per package. Drivers at some stations **may not accept** packages over 170 cm, so split them into multiple packages.

---

### Customer Refuses Delivery { #specs-sf-reject }

If a customer refuses the package, SF Express **collects the return shipping fee from you in person when returning it**. This fee **isn't** deducted from CYBER Coins or added to your statement; pay the driver in cash on site.

---

### System-Generated Shipping Labels Required { #specs-sf-no-handwritten }

* **Don't use handwritten shipping labels**. The CYBERBIZ system can't track handwritten labels, order delivery status won't update automatically, and SF Express can't return real-time delivery status.


## Next Steps { #next-steps-sf }

<div class="grid cards" markdown>

- :lucide-printer:{ .lg }  
  [__Print Extra Shipping Labels (Multiple Packages per Order)__](../../payments-and-logistics/setup-sf-express-waybill-v2.md#operate-sf-waybill-reprint){ title="Print Extra Shipping Labels" }  
  If items exceed a single package's size limit (we recommend splitting over 170 cm) or a Cash on Delivery order ships in multiple boxes, use "Print Extra Shipping Labels."

<!-- - :lucide-refresh-ccw:{ .lg }  
  [__Reprint Shipping Labels (Lost Labels)__](../../payments-and-logistics/reprint-waybills.md){ title="Reprint and Print Extra Shipping Labels" }  
  If a shipping label file is lost or misprinted, use **"Reprint Shipping Label"** to download it again. Reprinting **doesn't** charge you again. -->

</div>

## FAQ { #faq-sf }

??? quote "Why does the system say "Order X doesn't support SF Express shipping labels" when I choose "Download SF Express Shipping Labels"?"
    [](){ #faq-sf-unsupported-order }

    Check the following in order:

    * Whether the order's **delivery method** is "SF Express." Other logistics can't use SF Express shipping labels.
    * Whether the order's **Payment Status** is "Paid" or "Cash on Delivery." Orders awaiting payment can't ship.
    * Whether the order's **delivery address** is on Taiwan's main island. Outlying islands are blocked.

??? quote "Printing is blocked when CYBER Coins are insufficient, but I'm on PLUS / Enterprise. Why am I still blocked?"
    [](){ #faq-sf-points-insufficient }

    For PLUS / Enterprise plans, SF Express fees are **included on the statement**, and CYBER Coins aren't deducted when printing, so the "insufficient balance" message shouldn't appear. If you see it, contact your account manager to check **whether your plan type is correct** or **whether feature settings are in sync**.

??? quote "Can I ship international and domestic orders together?"
    [](){ #faq-sf-mixed-shipment }

    We recommend **handling them separately**. International and domestic shipments have different sizes in the "Select a fee" drop-down. The system shows size options based on the selected orders' recipient addresses, so mixed selections may have no common size.

??? quote "Can I print the downloaded shipping labels on A4 paper, or do I need special stickers?"
    [](){ #faq-sf-paper-type }

    SF Express shipping labels are system-generated PDF / PNG files with **no required sticker format**. You can print on regular A4 paper and tape it on, or use A6 label stickers. We recommend a **laser printer** to avoid blurry barcodes.

??? quote "How do I handle return shipping fees for refused orders?"
    [](){ #faq-sf-reject-fee }

    When SF Express returns the package to you, the driver **collects the return shipping fee in person** in **cash**. This fee **isn't** deducted from CYBER Coins or added to your statement. Keep some cash on hand and discuss the return and refund process with the customer.

??? quote "Why is a tax ID required for international orders?"
    [](){ #faq-sf-vat-required }

    International shipments need customs declaration, so **the sender company must provide a tax ID** as exporter verification. Without it, the system blocks the action and shows "For SF Express international export shipments, the tax ID in Website Settings > General Settings > Company Contact Information is required."

??? quote "Can I delete a shipping label myself after downloading it?"
    [](){ #faq-sf-cancel-waybill }

    You **can't cancel** generated SF Express tracking numbers yourself in the admin. If you printed the wrong size, selected the wrong order, or no longer need to ship, just **don't hand the package to the SF Express driver**. After 14 days, the system marks it "Customer canceled shipment" and refunds the CYBER Coins / doesn't bill it.

??? quote "What if my package is over 170 cm?"
    [](){ #faq-sf-oversize }

     Drivers at some SF Express stations **may not accept** packages over 170 cm. Split it into two packages and generate a shipping label for each. To ship one order in multiple packages, use [Print Extra Shipping Labels](../../payments-and-logistics/setup-sf-express-waybill-v2.md#operate-sf-waybill-reprint){ title="Print Extra Shipping Labels" data-preview }.

??? quote "How do I download a lost shipping label again?"
    [](){ #faq-sf-redownload }

     If you lose a shipping label file, find the order in "Payment and Logistics" > "SF Express Shipping Labels" in the admin and click download again next to the record. **No CYBER Coins are deducted again**. For details on reprinting, see [Reprint Shipping Labels](../../payments-and-logistics/setup-sf-express-waybill-v2.md#operate-sf-waybill-reprint){ title="Print Extra Shipping Labels" }.

