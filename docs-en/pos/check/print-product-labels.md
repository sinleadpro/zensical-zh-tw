---
title: "Print Product Labels"
description: "In addition to batch printing in the back office, CYBERBIZ POS lets staff print product labels directly at the front-desk checkout."
created: 2026-03-25 16:30
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有 POS 商店
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何從POS前台列印標籤
  - POS結帳頁列印商品標籤
  - 開啟POS前台標籤列印功能
  - POS標籤列印設定
features:
  - POS 前台列印
  - 商品標籤
  - 條碼列印
  - 結帳流程優化
prerequisites:
  - "標籤機安裝與後台列印教學"
related:
  - pos/hardware/label-printer/
tags:
  - "POS Front Desk"
  - "Label Printing"
  - "Store Efficiency"
  - "Product Labels"
  - TSC
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - POS 列印標籤設定
  - 啟用 POS 前台列印功能
  - 列印商品標籤
paths:
  - POS 功能 > 所有 POS 商店 > 修改 POS 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=13988
permalink: "https://help.cyberbiz.io/pos/check/print-product-labels/"
comments: false
search:
  exclude: false
icon: lucide/tag
hide: []
---

# Print Product Labels
In addition to batch printing in the admin, CYBERBIZ POS lets you print product labels directly at the checkout counter. Staff can generate labels directly when they check out or re-label products.
{ .subtitle }

![](../../assets/images/POS-後台-所有POS商店-列印商品標籤-單筆建立04.en.png){ .small-image }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Label Before Checkout**: When a customer selects a product without a label, staff can search for the product at the front desk and print the label immediately.
    - **Labeling Split Items**: When products need to be sold separately or repackaged, quickly reprint barcodes at the front desk.
    - **Real-Time Price Check**: After confirming product information at the front desk, if a label is damaged, reprint it immediately.


## Before You Start { #prerequisites-product-labels }

- **Hardware Requirement**: You must first install the label printer driver and complete a connection test. For details, see [Label Printer Installation Guide](../hardware/label-printer.md).
- **Feature Activation**: You must contact CYBERBIZ customer support to enable the **POS Front-Desk Label Printing** permission.


## Print Labels in the Admin { #operate-product-labels }

=== "Create a Single Label"

    ### Step 1: Set up Label Style { #operate-product-labels-style }

    1. Log in to the CYBERBIZ admin, go to **POS > POS Store List**, select the store you want to configure, and then click the **Print product label** tab.
        ![](../../assets/images/POS-後台-所有POS商店-列印商品標籤01.en.png){ .screenshot }
    2. Go to **Basic Label Settings**.
    3. **Barcode Source**: Select **Product Number (SKU)** or **Manufacturer Barcode** as the barcode to print.
    4. **Label Layout**: Select a layout, and adjust the content items shown on the label.
        ![](../../assets/images/POS-後台-所有POS商店-列印商品標籤-單筆建立01.en.png){ .screenshot }

    ### Step 2: Create Labels { #operate-product-labels-create }

    1. In the product list below, select the products you want to print labels for.
    2. **Search Products**:
        - **Scan to Search**: Click **Switch Mode: barcode**, then scan the product barcode with a barcode scanner.
        - **Manual Search**: Click **Switch Mode: Product Search**, then enter **Product Name** or the **SKU**.
        ![](../../assets/images/POS-後台-所有POS商店-列印商品標籤-單筆建立02.en.png){ .screenshot }
    3. Click **Add Label to Print**.
        ![](../../assets/images/POS-後台-所有POS商店-列印商品標籤-單筆建立03.en.png){ .screenshot }
    4. Enter the **Print Quantity** and, if needed, the **Shelf Life**.
    5. Click **Confirm**. The system sends the command to the label printer to generate the labels.



=== "Batch Import"

    1. Click **Excel import Products**.
    2. Download the Excel example.
    3. Fill in the label information according to the template fields.
    4. Upload the file in the dialog.

    ![](../../assets/images/POS-後台-所有POS商店-列印商品標籤-批次匯入01.en.png){ .screenshot }

## Print Labels at the POS Front Desk { #operate-frontend-print }


### Step 1: Enable Front-Desk Printing { #operate-frontend-print-step-a-enable }

Before you use the POS front desk, you must first enable permissions for the specific device in the admin.

1. Log in to the CYBERBIZ admin and go to **POS > POS Store List**.
2. Click the **POS Store Name** you want to configure to open the store detail page.
3. Find the device you want to enable, then click **Edit POS Settings** next to it.
4. In the **POS Label Printing Settings** section, switch **Enable POS Front-Desk Printing** to **On (ON)**.

![](../../assets/images/POS-後台-所有POS商店-開啟前台列印標籤設定01.en.png){ .screenshot }

### Step 2: Select and Print at the POS Front Desk { #operate-frontend-print-step-b-pos }

After you complete the back-office setup, refresh or log in to the POS front-desk app.

1. On the POS front-desk checkout page (cart screen), click a product in the product list.
2. Select the products you want to print labels for.
    ![](../../assets/images/POS-前台-結帳-列印商品標籤01.en.png){ .screenshot }
3. After you select products, the bottom-left corner of the screen shows the **Products to Print Quantity** and the **Total Label Count**.
    ![](../../assets/images/POS-前台-結帳-列印商品標籤02.en.png){ .screenshot }
4. After you confirm, click the **Print product label** button.
    ![](../../assets/images/POS-前台-結帳-列印商品標籤03.en.png){ .screenshot }
5. The label printer prints the corresponding product labels in sequence, based on the selected products and quantities.
    - **Label Content**: Printed labels include **Product Name**, **Variant** (if applicable), **Selling Price**, **Product Barcode**, and **SKU**.

!!! warning "Precautions"
    - If a printed barcode cannot be scanned, check that the label paper is aligned and whether the label printer sensor needs calibration.
    - Print one label first to confirm the style and avoid wasting materials during large print runs.


## FAQ { #faq-product-labels }

??? quote "Can I select multiple products to print at once?"
    Yes. You can select multiple different products at once, and the system prints all labels in sequence.


