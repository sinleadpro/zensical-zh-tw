---
title: "Set Up and Print Order Details"
description: "Customize what order details show, apply a print template, turn on personal data masking for order detail printing, and print or download PDFs from the order list."
created: 2026-05-08 14:21
last_modified: 2026-07-13 12:24
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - next stepper doc link missing
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
  - 自訂訂單明細列印項目
  - 設定列印模板與提醒文字
  - 列印訂單明細或下載 PDF
features:
  - 訂單明細列印
  - Liquid 模板自訂
  - 個資隱碼
prerequisites: []
related:
  - ec/orders/order-settings/shipping-detail-print/
  - ec/website-management/member-security-settings/
tags:
  - "Order Details"
  - "Print Settings"
  - "Personal Data Masking"
  - "Print Templates"
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
  - 安全性設定 > 會員安全
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=6358
  - https://www.cyberbiz.io/support/?p=47677
  - https://www.cyberbiz.io/helpcenter/?p=12661
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/order-detail-print/"
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---

![Order details print settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-hero.en.png){ title="Order Details Print Settings" .hero-page }

## About Order Details

"Order details" are the printed document you include with a package for the customer when shipping. They usually include item details, orderer information, payment method, and order amount.

This article explains how to do the following in the admin:

- Customize what order details show
- Apply a print template
- Enable personal data masking for printed order details
- Print or download a PDF from the order list

To set up the "packing slip" for internal shipping staff, see [Set Up and Print Packing Slips](shipping-detail-print.md){ title="Set Up and Print Packing Slips" }.

??? info "Packing Slips vs. Order Details"

    The system has two kinds of documents for different purposes, and you can set up each one's content separately:

    *   **Order details (customer)**: Usually include full item details, unit prices, amounts, and delivery method.
    *   **Packing slip (staff)**: Mainly for warehouse or shipping staff. Usually includes only item quantities and the delivery address, **without the order amount**, to keep it simple and save costs.

## Steps

### Set Up Order Details Content { #orders-print }

#### 1. Open Order Details Print Settings { #orders-print-activate }

In the admin sidebar, follow the path for your menu version:

- New menu: **Payment and Logistics** > **Checkout Page & Logistics** > find **"Order Detail Print Settings"**
- Old menu: **Online Shopping Settings** > **Cart and Payments** > find **"Order Detail Print Settings"**

---

#### 2. Select Items to Show { #orders-print-configure }

The panel has several checkboxes you can combine as needed (all are cleared by default). [Full field reference](#orders-print-fields){ data-preview }

![Order details print settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-configure.en.png){ title="Order Details Print Settings" }

??? example "Common Combinations"

    - **B2C online shopping**
      Select: Show Logo Image, Product SKU, Product Image, Order Payment Method, Orderer Information, Invoice Information

    - **Wholesale / bulk shipping**
      Select: Product SKU, Vendor Number, Order Additional Information (skip Product Image to save paper)

    - **Brand experience focus**
      Select: Show Logo Image, Header Reminder Text, Product Image, Customer's Expected Bonus Points

---

#### 3. Set Header Reminder Text and Image <small>Optional</small>

After you select **"Header Reminder Text,"** you must enter a "Title" and "Content" on the advanced settings page in [Step 5](#orders-print-advanced-settings-alert-text), or you can't save.

!!! example "Use Cases"

    - **Shopping notes**: Return and exchange deadlines, customer service contacts
    - **Thank-you messages**: Repurchase discount codes, social media invitations

**Header reminder image**

You can upload an image below the main panel:

1. Click **"Choose Image"** to upload a file
2. The recommended image size is **90px × 90px**
3. Good for:
    - Company logo
    - Website QR code
    - LINE Official Account QR code
4. To remove it, click **"Delete Image"**

![Order details - header image - settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-開頭圖片.en.png){ title="Order Details - Header Image - Settings" }

!!! tip "Create a QR Code Quickly"

    - You can [create a QR code with the Chrome browser :lucide-external-link:](https://support.google.com/chrome/answer/10051760?hl=zh-Hant&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-pages-with-a-qr-code%2C%E9%80%8F%E9%81%8E-qr-code-%E5%88%86%E4%BA%AB%E7%B6%B2%E9%A0%81).
    - You can also use any online QR code generator. We recommend a size of **90px × 90px** to avoid blurring or distortion when printing.

---

#### 4. Save Settings

Click **Save** at the bottom of the settings section to finish basic setup.

!!! info "What Gets Saved"

    This button only saves the selected items and the reminder image. Reminder text and template style must be saved separately on the advanced settings page.

---

#### 5. Advanced Settings { #orders-print-advanced-settings }

Click **Advanced Setup** at the bottom of the settings section to open the **"Edit Order Details Print Template"** page.

![Order details settings - advanced settings](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-進階設定按鈕.en.png){ title="Order Details Settings - Advanced Settings" }

On this page, you can [edit reminder text](#orders-print-advanced-settings-alert-text), [customize the template](#orders-print-template), [preview the printout](#orders-print-preview), and [restore the default template](#orders-print-templates-revert).

---

##### Edit Header Reminder Text { #orders-print-advanced-settings-alert-text }

If you selected "Header Reminder Text" in Step 2, this page shows:

- **Header Reminder Text Title**
- **Header Reminder Text Content**

Both fields are required.

![Order details advanced settings - reminder text](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-進階設定-提醒文字.en.png){ title="Order Details Advanced Settings - Reminder Text" }

---

##### Customize the Template { #orders-print-template }

The "Template" section is Liquid code. You can adjust:

- Layout
- Font size
- Margins
- CSS styles

In most cases, we recommend the default template. For major customization, get help from someone familiar with HTML / CSS.

![Order details advanced settings - template](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-進階設定-樣板.en.png){ title="Order Details Advanced Settings - Template" }

!!! note "[Preview](#orders-print-preview) before saving (requires at least one "Shipped" order)."

---

##### Preview the Printout { #orders-print-preview }

After you click **"Order Details Preview"**:

- The system uses the most recent shipped order
- The browser print window opens automatically

You can preview the actual printout directly.

![Order details advanced settings - preview](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-進階設定-訂單明細預覽.en.png){ title="Order Details Advanced Settings - Preview" }

??? example "Order Details Preview Example"

    <div class="grid" markdown>

    ![Order details preview example 1](../../../assets/images/訂單明細預覽-1.en.png){ title="Order Details Preview Example 1" }

    ![Order details preview example 2](../../../assets/images/訂單明細預覽-2.en.png){ title="Order Details Preview Example 2" }

    </div>

---

##### Restore the Default Template { #orders-print-templates-revert }

To restore the template, click **"Restore Default Template"** to return to the system default version.

![Order details template - restore default](../../../assets/images/EC-金物流-結帳頁物流設定-列印訂單明細-進階設定-回覆預設樣板按鈕.en.png){ title="Order Details Template - Restore Default" }

!!! note "Saved checkbox selections aren't affected."

---

### Print Order Details { #orders-print-operate }

After you finish [setting up order details content](#orders-print), you can print from the order list:


1. **Go to the order list**: Sign in to the CYBERBIZ admin and go to "Orders" > "All Orders."
2. **Select orders**: Select one or more orders to print.
3. **Print**: Click the "More Actions" (or "Actions") button at the top right of the list and select "Print Order Details" from the drop-down.
4. **Confirm printing**: The system automatically generates a PDF and opens the browser print window. You can choose:
    - Print on paper: Choose a connected printer.
    - Save as PDF: Save the file to your computer.

![Order list - print order details](../../../assets/images/EC-訂單-所有訂單-更多操作-列印訂單明細.en.png){ title="Order List - Print Order Details" }

!!! note "When you run "Confirm Shipment" and download shipping labels, the system-generated [archive](#orders-print-fulfillment-zip) also includes the order details for that order automatically."

---

## Order Details in the Shipping Archive { #orders-print-fulfillment-zip }

When you run **"Confirm Shipment"** in the order list and download shipping data, the archive the system generates automatically includes:

- Shipping label
- Packing slip
- Order details
- Pick list

The order details use the following settings from this page:

- Selected items
- Print template

<!-- ## Next Steps -->
<!---->
<!-- <div class="grid cards" markdown> -->
<!---->
<!-- - :lucide-receipt:{ .lg }   -->
<!--   Japan Store Invoice and Receipt Downloads   -->
<!--   Japan store merchants can download invoices, receipts, and related refund documents in formats that comply with Japanese law from this path. -->
<!---->
<!-- </div> -->

## FAQ

??? quote "Why does the printout still show the old layout after I click save?"

    "Save" on the main panel only saves the checkbox selections. If you changed the template style, click save again on the "Advanced Settings" page.

??? quote "What should I do if the preview is blank or shows an error?"

    The preview requires at least one "Shipped" order. If you don't have any shipped orders yet, complete a test order first.

??? quote "Why is my uploaded reminder image blurry?"

    We recommend a 90px × 90px image. If the original image is too large, it may become blurry after the system resizes it.

??? quote "Are the packing slip and order details the same document?"

    No. They're set up separately. See [Set Up and Print Packing Slips](shipping-detail-print.md){ title="Set Up and Print Packing Slips" }

    - **Order details**: For customers; usually include amounts and payment information
    - **Packing slip**: For internal shipping staff; usually without amounts

## References

### Order Details Field Reference { #orders-print-fields }

| Option | Printed Result | Use Case |
| :-- | :-- | :-- |
| Show Logo Image | Prints your store logo at the top of the order details | Strengthen brand identity |
| Header Reminder Text | Prints your custom title and content at the top of the order details | Return and exchange notes, thank-you messages, repurchase discount codes |
| Product SKU | Adds the SKU number to printed items | Warehouse reconciliation, wholesale orders |
| Product Image | Adds thumbnails to printed items | B2C online shopping, better readability |
| Vendor Number | Adds the supplier-provided number to printed items | Multi-vendor drop shipping, consignment warehousing |
| Customer's Expected Bonus Points | Prints the bonus points the customer earns from this order | Encourage repurchases, marketing communication |
| Order Payment Method | Prints the payment method the customer chose (credit card / ATM / convenience store payment code, etc.) | Tell customers the payment status |
| Order Additional Information | Prints the notes the customer entered at checkout | Custom orders, gift notes |
| Delivery Date and Time Slot | Prints the delivery time the customer specified | Fresh food, scheduled delivery services |
| Invoice Information | Prints e-invoice information (tax ID, title, etc.) | B2B orders, merchant expense reporting |
| Orderer Information | Prints the orderer's name, phone, and address | Essential; most merchants select it |


!!! note "Notes"

    - Options only "add" content to the printout. Cleared fields aren't printed, but the original data is still stored.
    - After you select "Header Reminder Text," you must enter a title and content on the advanced settings page, or you can't save.

## More Actions

<div class="grid cards" markdown>

- :lucide-eye-off:{ .lg } [__Order Details Personal Data Masking Settings__](../../website-management/member-security-settings/#operate-security-pdpa)

</div>