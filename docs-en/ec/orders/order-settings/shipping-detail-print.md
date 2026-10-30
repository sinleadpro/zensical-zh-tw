---
title: "Set Up and Print Packing Slips"
description: "Customize what packing slips show, apply a print template, and batch download packing slips from the order list."
created: 2026-05-08 16:00
last_modified: 2026-07-13 12:36
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - add links to 出貨流程 for 如何列印出貨明細 section
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
plans:
  - Professional
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 自訂出貨明細列印項目
  - 設定列印模板
  - 批次下載出貨明細
features:
  - 出貨明細列印
  - Liquid 模板自訂
  - 批次出貨打包
prerequisites: []
related:
  - ec/orders/order-settings/order-detail-print/
  - ec/orders/basics/order-fulfillment-flow/
tags:
  - "Packing Slips"
  - "Print Settings"
  - "Pick Lists"
  - "Batch Shipping"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 進階設定
  - 樣板編輯器
paths:
  - 金物流 > 結帳頁 & 物流設定
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=6364
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/shipping-detail-print/"
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---

![Packing slip settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-hero.en.png){ title="Packing Slip Settings" .hero-page }

## About Packing Slips

A "packing slip" is a printed document for internal warehouse, picking, and shipping staff during fulfillment. It's usually kept with the package during shipping to help check shipments and hand off work internally.

This page explains how to do the following in the admin

- Customize what the packing slip shows
- Get packing slips during actual fulfillment.

To set up the "order details" sent to customers with the package, see [Set Up and Print Order Details](order-detail-print.md){ title="Set Up and Print Order Details" }.

??? info "Packing Slips vs. Order Details"

    The system has two kinds of documents for different purposes, and you can set up each one's content separately:

    *   **Order details (customer)**: Usually include full item details, unit prices, amounts, and delivery method.
    *   **Packing slip (staff)**: Mainly for warehouse or shipping staff. Usually includes only item quantities and the delivery address, **without the order amount**, to keep it simple and save costs.

## Steps

### Set Up Packing Slip Content { #fulfillment-print }

#### 1. Open Packing Slip Print Settings { #fulfillment-print-activate }

In the admin sidebar, find the following path (it varies slightly by admin menu version):

- New menu: **Payment and Logistics** > **Checkout Page & Logistics** > find **"Packing Slip Print Settings"** section
- Old menu: **Online Shopping Settings** > **Cart and Payments** > find **"Packing Slip Print Settings"** section

---

#### 2. Select Items to Show { #fulfillment-print-configure }

The panel has 9 checkboxes you can combine to fit your internal fulfillment process (all are cleared by default). [Full field reference](#fulfillment-print-fields){ title="Packing Slip Field Reference" data-preview }

![Packing slip content settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-設定.en.png){ title="Packing Slip Content Settings" }

??? example "Common Combinations"
    - **Warehouse picking first**: Select Product SKU, Product Image, Product Vendor Number, Delivery Date and Time Slot
    - **Shipment checking first**: Select Product SKU, Order Additional Information, Delivery Date and Time Slot, Shipping Staff Information
    - **Multi-warehouse / drop shipping**: Select Product Vendor Number, Order Additional Information, Shipping Staff Information


!!! tip "Keep It Simple"

    The packing slip is an internal process document. We recommend selecting only the minimum information needed for picking and checking shipments, which saves paper and helps staff read faster. Sensitive customer information such as amounts, bonus points, and personal data usually doesn't need to appear on it.

---

#### 3. Save Settings

Click **Save** at the bottom of the settings section to finish basic setup.

![Packing slip settings - save](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-儲存按鈕.en.png){ title="Packing Slip Settings - Save" }

---

#### 4. Advanced Settings { #fulfillment-print-advanced-settings }

Click **Advanced Setup** at the bottom of the settings section to open the **"Edit Packing Slip Print Template"** page.

![Packing slip settings - advanced settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-進階設定.en.png){ title="Packing Slip Settings - Advanced Settings" }

On this page, you can [customize the template](#fulfillment-print-template){ title="Customize the Template" }, [preview the printout](#fulfillment-print-preview){ title="Preview the Printout" }, and [restore the default template](#fulfillment-print-revert){ title="Restore the Default Template" }.

---

##### Customize the Template { #fulfillment-print-template }

The "Template" section is Liquid code. You can adjust layout, font size, margins, and more. In most cases, the default template is fine.

![Packing slip - template settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-進階設定-樣板.en.png){ title="Packing Slip - Template Settings" }

!!! warning "Reminder"

    - Always preview to make sure it displays correctly before saving.
    - The preview needs a "Shipped" order; otherwise, the template may not render correctly.

---

##### Preview the Printout { #fulfillment-print-preview }

Click **"Packing Slip Preview."** The system applies your current template to the most recent shipped order and opens the browser print dialog right away.

![Packing slip preview](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-進階設定-出貨明細預覽.en.png){ title="Packing Slip Preview" }

---

##### Restore the Default Template { #fulfillment-print-revert }

To undo your changes, click **"Restore Default Template"** to reset to the system default version (saved checkbox selections aren't affected).

![Packing slip settings - restore default template](../../../assets/images/EC-金物流-結帳頁物流設定-列印出貨明細-進階設定-回復預設樣板.en.png){ title="Packing Slip Settings - Restore Default Template" }

!!! info "Packing Slips Have No Header Reminder Text"

    Unlike order details, the packing slip's advanced settings page has no "Header Reminder Text Title / Content" fields. That's because the packing slip is an internal document and doesn't need customer-facing copy.

### Print Packing Slips { #fulfillment-print-operate }

After you finish [setting up the content](#fulfillment-print), packing slips can't be printed on their own like order details. Instead, they're generated with other shipping documents during **bulk shipping and packing**:

1. In the admin menu, go to **Orders** > **All Orders**.
2. Select one or more orders to ship in the order list.
3. Click the actions drop-down above the list (shown as **Actions...** or **"Actions"** depending on the admin version).
4. Select **Download** and specify the carrier to download for.
5. The system generates a ZIP archive containing:

    - The carrier's **Shipping Label** (PDF)
    - **Packing slip** (using the template set on this page)
    - **Pick list**
    - **Order details** (using the order details template)

6. After extracting it, distribute the files for picking, shipping, and customer packages.

??? example "Packing Slip Example"

    ![Packing slip example image](../../../assets/images/出貨明細範例.en.png){ title="Packing Slip Example Image" }

??? quote "Why is there no separate "Print Packing Slip" option?"

    Packing slips are designed to be generated together with "shipping labels." Merchants usually need the shipping label, packing slip, and pick list at the same step when preparing shipments, so the system generates them together in one ZIP instead of printing each one separately. If you only need the customer-facing document, see the [Print Order Details](order-detail-print.md){ title="Set Up and Print Order Details" } process.

## Next Steps

<div class="grid cards" markdown>

- :lucide-receipt:{ .lg }  
  [__Set Up and Print Order Details__](order-detail-print.md){ title="Set Up and Print Order Details" }  
  Learn how to set up the order details sent to customers with the package, including full item details, unit prices, amounts, and delivery method.

- :lucide-truck:{ .lg }  
  [__Order Fulfillment Flow__](../basics/order-fulfillment-flow.md){ title="Order Fulfillment Flow" }  
  Learn the full fulfillment process, from single shipments to bulk packing, covering home delivery, convenience store pickup, and custom logistics.

</div>


## FAQ

??? quote "The packing slip looks a lot like the order details. How should I use each one?"

    - **Order details**: For customers, put in the package. We recommend selecting information customers care about, such as Orderer Information, Invoice Information, and Customer's Expected Bonus Points.
    - **Packing slip**: For internal shipping staff, to help with picking and checking. We recommend selecting information the fulfillment process needs, such as SKU, vendor number, and delivery date.

    Although the two share some fields, in practice you can clearly separate them by "selecting different items."

??? quote "Does the packing slip show the customer's name / address?"

    Yes (recipient information taken from the shipping label). If customers might see the packing slip (for example, if it's stuck on the outside of the package), we recommend adding custom masking in the template, or simply not putting the packing slip outside the package.

??? quote "Why didn't the ZIP contents change the next time I shipped after clicking "Save"?"

    - "Save" on the main panel only saves the checkbox selections. Template style changes take effect only after you go to the **Advanced Setup** page and click **Save**.
    - ZIP files already generated aren't updated. Only new ZIPs generated the **next** time you click "Download" use the new settings.

??? quote "What should I do if the preview is blank or shows an error?"

    The preview needs at least one **Shipped** order as a sample. If you don't have any shipped orders yet, complete the shipping process for a test order first, then come back to preview.

??? quote "Can I download only the packing slip without the other documents?"

    The admin doesn't currently support downloading the packing slip alone. If you need it, download from the order list and then use only the packing slip PDF from the ZIP.

??? quote "What's the difference between a packing slip and a pick list?"

    - **Packing slip**: Similar in format to order details; good for a final check before packing.
    - **Pick list**: A simplified version designed for warehouse staff to "pick from a list." It usually lists only item name, SKU, quantity, and storage location.

    Both are included in the shipping ZIP.



## References  

### Packing Slip Field Reference { #fulfillment-print-fields }


| Option | Printed Result | Use Case |
| :-- | :-- | :-- |
| Show Logo Image | Prints the store logo at the top of the packing slip | Identify the source when multiple brands share a warehouse |
| Product SKU | Adds the SKU number to printed items | Main basis for warehouse picking |
| Product Image | Adds thumbnails to printed items | Helps pickers check items visually |
| Product Vendor Number | Adds the supplier number to printed items | Checking multi-vendor drop shipping and consignment warehousing |
| Order Payment Method | Prints the payment method the customer chose | Usually not selected (customer information) |
| Order Additional Information | Prints the notes the customer entered at checkout | Custom requests, gift notes, special instructions |
| Delivery Date and Time Slot | Prints the delivery time the customer specified | Scheduled shipping, fresh food time control |
| Invoice Information | Prints e-invoice information | Usually not selected (customer information) |
| Shipping Staff Information | Prints the admin user who handled this shipment | Accountability when multiple people handle fulfillment |

!!! note "Notes"

    - Options only "add" content to the printout. Cleared fields aren't printed, but stored data isn't affected.
    - Packing slips have no "Header Reminder Text / Image" settings.  

---

