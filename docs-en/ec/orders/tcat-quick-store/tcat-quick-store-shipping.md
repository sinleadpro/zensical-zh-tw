---
title: "Ship with EZCAT Quick Store Delivery"
description: "Batch print or download EZCAT Quick Store Delivery shipping documents and update the order shipment status to Shipped."
created: 2026-05-18 15:26
last_modified: 2026-09-23 15:00
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
  - 列印黑貓出貨文件
  - 黑貓快速到店出貨
  - 補印託運單
features:
  - 黑貓快速到店
  - 進行出貨/列印文件
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
  - ec/orders/order-settings/setup-shipping-docs-sort/
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
  - 進行出貨/列印文件
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

"EZCAT Quick Store Delivery" is a service where EZCAT delivers your products to the 7-Eleven store chosen by the customer for pickup. It's divided into ambient, refrigerated, and frozen by product temperature zone. This page shows how to batch process orders in the new order list, print or download shipping labels, and change the delivery status to "Shipped." After you confirm shipping, the browser opens a new tab with the PDF, so you can print it directly without unzipping it first.

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
| [Unclaimed](#specs-tcat-cvs-overdue){ title="Unclaimed Store Packages" } | The package is returned to you, and EZCAT **charges an additional return shipping fee** |

!!! tip "Packaging Tips for Refrigerated/Frozen Shipments"
    * **Pre-chilling time**: We recommend pre-chilling refrigerated products for at least 6 hours and frozen products for at least 12 hours to keep the temperature zone until store pickup.
    * **Waterproof shipping labels**: We recommend printing shipping labels on waterproof stickers, or putting the label in a clear waterproof pouch before attaching it to the package, so condensation doesn't blur the barcode and prevent the driver from scanning it.

---

### System Limitations { #prerequisites-tcat-cvs-system-contraints }

- **Separate by temperature zone (no mixing)**: Ambient, refrigerated, and frozen use different shipping labels. When selecting orders in bulk to ship, you can't mix orders from different temperature zones.
- **Feature activation**: Your store must have the matching temperature zone feature enabled. To use refrigerated and frozen services, the system must also have the "Product-bound temperature zone" feature enabled.
- **Can't be used with Fengchao Logistics**: If your store is integrated with Fengchao Logistics, you can't use EZCAT Quick Store Delivery. You can only use one of the two.

## Steps { #operate-tcat-cvs }


### Before Shipping { #prerequisites-tcat-cvs-checklist }

Before shipping with EZCAT Quick Store Delivery, complete the following:

- [x] **EZCAT sender address**: Go to "Payment and Logistics" > "[EZCAT Quick Store Delivery Shipping Labels](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#operate-ezcat-cvs-sender-settings){ title="Set Up Sender Information" }" and set the sender address, or the sender information on the shipping label will be incomplete.
- [x] **Supplies and equipment**: You have "EZCAT three-part blank shipping label stickers" ready (call EZCAT customer service at 02-412-8888 to get them), and we recommend a laser printer so barcodes print clearly.
- [x] **Product pre-chilling (low-temperature packages)**: Refrigerated products must be pre-chilled for at least 6 hours; frozen products for at least 12 hours.
- [x] **Check your balance**: Standard Plan merchants should go to [check the CYBER Coin balance in the Top-Up Center](../../website-management/points-deposits.md#overview-cyber-coin-balance){ data-preview } and make sure the balance is sufficient; PLUS / Enterprise merchants don't have this restriction.

--- 

### Ship in Bulk and Print Shipping Documents { #operate-tcat-csv-shipping-note }

1. **Go to the order list**: Sign in to the admin and go to **Orders > All Orders**.
2. **Select orders**: Select the orders to ship in the list. Make sure all selected orders use "EZCAT Home Delivery" as the delivery method.
3. **Click "Actions..."**: Click **Actions...** above the list and select **EZCAT Home Delivery - Ship/Print Documents** from the drop-down[^1].

4. **Set the pop-up fields**: In the "Ship/Print Documents" window, set the following in order
    * **Select a temperature zone**: Choose **Room Temperature**, **Refrigerated**, or **Frozen**. Make sure **the setting matches the actual package**.
    * **Is it Fragile?**: Choose **Yes** or **No**.
    * **Sender address**: Defaults to the sender address last used for this logistics service (the first time, it uses the address in [EZCAT settings](../../payments-and-logistics/setup-print-tcat-waybill-v2.md#operate-ezcat-sender-settings){ title="Set Up Sender Information" }). To change it, click **Change** in the window to edit it[^3].

5. **Select the documents to print**: Under **Select the documents to print**, select the document types to print this time. **Shipping Label** and **Download All Documents** are selected by default.

    | Item | Default | Description | Changes the order to `Shipped` after you click Confirm |  
    | :--- | :--- | :--- | :--- |
    | Picking List | Not selected | For warehouse picking | No | 
    | Shipping Label | Selected | Attached to the outside of the package for the carrier to scan and deliver | **Yes** |
    | Shipment Details | Not selected | Available only after you select Shipping Label | No |
    | Order Details | Not selected | For internal records or to include in the package | No | 
    | Download All Documents | Selected | Also downloads the documents to your computer as a ZIP file | **Yes** |

    ![Shipping pop-up: print documents](../../../assets/images/EC-後台-訂單-所有訂單-列印黑貓出貨文件02.en.png){ title="Select Shipping Documents to Print" .screenshot }

6. **Agree to the terms**: Select **I have read and agree to the CYBERBIZ Logistics Integration Terms of Service and EZCAT contract terms**. **Confirm** can't be clicked until you do.

    !!! plan "Call an EZCAT Driver Directly from the Pop-Up"
        If your store has enabled the EZCAT driver call feature, an "Automatically Call an EZCAT Driver for Pickup" section appears at the bottom of the window, so you can book a driver for door pickup while shipping. For details, see [How to Automatically Call an EZCAT Driver for Pickup](../home-delivery/tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }.

7. **Confirm shipping**: Click **Confirm**. The browser opens a new tab that first shows "Generating documents, please wait." Don't close that tab.

    ![Generating documents](../../../assets/images/EC-後台-訂單-所有訂單-列印黑貓出貨文件03.en.png){ title="Generating Shipping Documents" .screenshot }

8. **Print the PDF**: When generation is complete, the tab shows the documents you selected. Click the print icon in the upper-right corner of the browser, or press `Ctrl + P` on Windows or `Command + P` on Mac.

    ![Shipping document PDF preview](../../../assets/images/EC-後台-訂單-所有訂單-列印黑貓出貨文件04.en.png){ title="Preview Shipping Document PDF in the Browser" .screenshot }

    If **Download All Documents** is selected, the system also downloads[^1] the [shipping label ZIP file](#reference-tcat-cvs-zip){ title="Shipping Label ZIP Contents" }. The default PDF order is Picking List → Shipping Label → Shipment Details → Order Details; for batches of multiple orders, you can change the [print order](../order-settings/setup-shipping-docs-sort.md){ title="Set the Print Order of Shipping Documents" }.

9. **Confirm the delivery status changed**: If **Shipping Label** or **Download All Documents** is selected, the delivery status of the selected orders changes to **Shipped**. (See [Confirm the Delivery Status Change](#operate-tcat-cvs-verify){ title="Confirm the Delivery Status Change" })


[^1]: If the option doesn't appear, the order status may not qualify or logistics setup may be incomplete. For details, see [FAQ: No Ship/Print Documents option](#faq-tcat-cvs-action-missing).
[^2]: If the download doesn't start, check whether your browser is blocking pop-ups or ads. Allow pop-ups for this site and click download again. For more troubleshooting, see [FAQ: Can't download shipping labels](#faq-tcat-cvs-download-no-response)
[^3]: Changes also update the address on that logistics page. Addresses for other logistics services and the company logistics address aren't affected.

---

### Call an EZCAT Driver for Pickup { #operate-tcat-cvs-call-driver }

After downloading the shipping labels, contact an EZCAT driver to pick up the packages:

* **Call by phone**: Call the EZCAT customer service line (02-412-8888) to arrange pickup.
* **Call directly from the admin**: If you've enabled the [Call EZCAT feature](../home-delivery/tcat-auto-call-driver-v2.md){ title="Automatically Call an EZCAT Driver for Pickup" }, you can schedule driver pickup in the pop-up when downloading shipping labels.

---

### Confirm the Delivery Status Change { #operate-tcat-cvs-verify }

After you confirm shipping, you can check the delivery status in two places:

- **Order list page**: The delivery status column shows **Shipped**
- **Order details page**: The status shows [Shipped (Awaiting Carrier Pickup)](../home-delivery/shipping-status-tooltip.md#reference-shipping-status){ data-preview }, meaning the shipping label was created but EZCAT hasn't picked up the package yet

If the delivery status didn't update, check:

* Whether the confirmation actually completed (whether the browser blocked the new tab or the download)
* Whether all selected orders use "EZCAT Quick Store Delivery" as the delivery method

---

### Troubleshoot Address Errors { #operate-tcat-cvs-address-error }

If an "Incomplete sender information" message appears when you download shipping labels, the EZCAT sender address isn't set or is incomplete:

1. Go to **Payment and Logistics > EZCAT Convenience Store Shipping Label** and make sure the **Sender Address** in the "EZCAT Quick Store Delivery Settings" section is complete (including city/county and district). After you save, the system automatically looks up the sender area code with EZCAT.
2. After saving, download again.

??? info "Notes on the Sender Address"
    * **Address source**: The sender address comes from the "EZCAT Quick Store Delivery Settings" address in **Payment and Logistics > EZCAT Convenience Store Shipping Label**.
    * **How to change it**: Click **Change** in the shipping label download pop-up to edit it directly. Changes also update the EZCAT Quick Store Delivery settings page.

---

### Unclaimed Store Packages { #specs-tcat-cvs-overdue }

After the package arrives at the convenience store, the customer has a pickup deadline:

* **Ambient**: Within 7 days
* **Refrigerated / frozen**: Within 4 days

EZCAT sends **2 SMS messages** to remind the customer:

| SMS | When It's Sent |
| :-- | :-- |
| 1st | The day the package arrives at the store |
| 2nd | 1 day before it's returned (day 6 for ambient, day 3 for refrigerated/frozen) |

## Next Steps { #next-steps-tcat-cvs }

<div class="grid cards" markdown>

<!-- - :lucide-printer:{ .lg }  
  [__Reprint Shipping Labels__](../../payments-and-logistics/reprint-waybills.md){ title="Reprint and Print Extra Shipping Labels" }  
  If you need to print again (for example, the label got wet or printed unclearly), go back to the order list, select the same order, and choose Reprint Shipping Label from "More Actions." -->

- :lucide-list-ordered:{ .lg }  
  [__Set the Print Sort Order for Shipping Documents__](../order-settings/setup-shipping-docs-sort.md){ title="Set the Print Sort Order for Shipping Documents" }  
  When printing documents for multiple orders in bulk, you can sort them by document type or by order number.

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


??? quote "Why can't I find the "Ship/Print Documents" option in the "More Actions" drop-down?"
    [](){ #faq-tcat-cvs-action-missing }

    This is usually caused by one of the following:

    * The selected orders didn't choose EZCAT Quick Store Delivery at checkout, or you selected orders with different temperature zones or different logistics services. Make sure this batch is all the same EZCAT Quick Store Delivery type.
    * The order's delivery status isn't "Unshipped," "Partially Shipped," or "Preparing" (for example, it's refunded or canceled), so it can't be shipped.

??? quote "If I print only the picking list or order details, does the delivery status change to Shipped?"
    [](){ #faq-tcat-cvs-print-without-waybill }

    No. The order changes to Shipped only when you select **Shipping Label** or **Download All Documents** and then click **Confirm**. If you print only the picking list or order details, the delivery status stays the same.

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

### Shipping Label ZIP Contents { #reference-tcat-cvs-zip }

After the download finishes, the ZIP contains four PDFs, each for a different process:

| File | Purpose | Recipient |
|---|---|---|
| **Shipping Label** | Used by EZCAT for pickup and delivery; print on EZCAT three-part blank shipping label stickers and attach to the package | Driver |
| **Packing Slip** | Slip included in the package, listing items and quantities | Customer (in the package) |
| **Picking List** | Warehouse picking list, grouped by item for easy picking | Internal warehouse staff |
| **Order Details** | Full order information, including amounts, payment method, and customer details | Internal records / customer service |


