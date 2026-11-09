---
title: "Get Started"
description: "Learn about CYBERBIZ POS hardware requirements, software installation, third-party service applications, and core system concepts to help you take the first step in running your store."
created: 2026-04-17 12:00
last_modified: 2026-06-08 17:50
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - POS
sites:
  - TW
audiences:
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
  - POS 開通準備
  - 硬體設備清單
  - 軟體安裝
  - 理解帳號權限
features:
  - 智能 POS
  - 庫存連動
  - 帳號管理
prerequisites: []
related:
  - pos/hardware/
  - pos/hardware/epson-tm-t82iii-invoice-printer/
  - pos/hardware/epson-tm-m30iii-invoice-printer/
  - pos/hardware/posiflex-wired-invoice-printer/
  - pos/hardware/taishin-wired-credit-card-machine/
  - pos/hardware/mypay-wireless-credit-card-machine/
  - pos/hardware/label-printer/
  - pos/hardware/customer-display-screen/
  - pos/hardware/hprt-n130-barcode-scanner/
  - pos/software/drivers/
  - pos/third-party/monolith-e-invoice/
  - pos/check/line-pay-scan-payment/
  - ec/products/create-and-manage/create-update-products/
  - pos/get-started/bulk-update-product-skus/
  - pos/inventory/
  - pos/store/staff-permissions-and-account-management/
tags:
  - "Getting Started"
  - "Hardware List"
  - "Software Installation"
  - "POS Basics"
acoiv: activate
apis: []
devices:
  - desktop
  - tablet
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=5012
permalink: "https://help.cyberbiz.io/pos/get-started/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Get Started
Take the first step in running your store: learn about Smart POS hardware and software requirements, third-party service applications, and core system logic.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) |Smart POS
{ .doc-badge }


## Equipment and Software Checklist { #overview-get-started }

Before you activate POS features, make sure you have planned the following hardware and software environment.

![](../../assets/images/POS硬體設備展示圖.en.png){ .screenshot }

=== "Hardware Devices"

    === "Required Equipment"

        <div class="grid cards" markdown>

        - :lucide-settings:{ .lg }
          __POS Checkout Terminal__<br>
          Serves as the platform for running the POS software. Choose a **POS machine, desktop computer, laptop, or tablet** based on your checkout scenario, such as a fixed counter or mobile checkout.<br><br>
          [→ Learn about system hardware and environment requirements](../hardware/){ title="System Hardware and Environment Requirements" }

        </div>

    === "Peripherals"

        <div class="grid cards" markdown>

        - :lucide-printer:{ .lg }
          __Invoice Printer__<br>
          Used to print e-invoices. Supports EPSON [wired invoice printers](../hardware/epson-tm-t82iii-invoice-printer/), [WiFi invoice printers](../hardware/epson-tm-m30iii-invoice-printer), or [Posiflex](../hardware/posiflex-wired-invoice-printer) wired invoice printers.

        - :lucide-credit-card:{ .lg }
          __Credit Card Terminal__<br>
          Connects to payment gateway services. Supports [Taishin wired credit card terminals](../hardware/taishin-wired-credit-card-machine/) or [MYPAY wireless credit card terminals](../hardware/mypay-wireless-credit-card-machine/).

        - :lucide-tags:{ .lg }
          [__Label Printer__](../hardware/label-printer/)<br>
          Prints product barcodes or category labels.

        - :lucide-monitor:{ .lg }
          [__Customer Display__](../hardware/customer-display-screen/)<br>
          Shows transaction amounts and promotion information to customers.

        - :lucide-scan-barcode:{ .lg }
          [__Barcode Scanner__](../hardware/hprt-n130-barcode-scanner.md)<br>
          Quickly reads product SKU barcodes and member carrier codes.

        - :lucide-archive:{ .lg }
          __Cash Drawer__<br>
          Stores business cash and can be opened automatically by the POS system.
        </div>


    === "Other Equipment"

        <div class="grid cards" markdown>

        - :lucide-cpu:{ .lg }
          __Electronic Shelf Label__<br>
          Displays synchronized prices for the store and the online store.

        - :lucide-tv-2:{ .lg }
          __Digital Signage__<br>
          Plays brand promotional videos or in-store promotions.

        </div>

    !!! warning "Service Support Limitations"
        To ensure system stability, merchants must confirm system support when selecting software and hardware. If you use devices that are not CYBERBIZ-certified, we cannot provide related technical support.


=== "Software Installation"

    <div class="grid cards" markdown>

    - :lucide-layers:{ .lg }
      __CYBERBIZ Smart POS System__<br>
      The core sales system. Contact your store setup consultant to get the website link and account.

    - :lucide-download:{ .lg }
      [__POS Driver__](../software/drivers/)<br>
      Required drivers for connecting peripheral hardware (such as invoice printers and label printers).

    </div>

=== "Third-Party Services"

    <div class="grid cards" markdown>

    - :lucide-file-text:{ .lg }
      [__Mengli E-Invoice__](../third-party/monolith-e-invoice/)<br>
      Apply through the e-invoice service center to ensure invoices are issued in compliance.

    - :lucide-qr-code:{ .lg }
      [__LINE Pay Scan Payment__](../check/line-pay-scan-payment.md)<br>
      Apply for LINE Pay merchant access to support mobile payment checkout.

    </div>

## Preparation Before Setup { #intro-get-started }

Before you activate POS features, complete the basic setup on the online store and understand how the system works.

=== "Online Store Pre-Setup"

    <div class="grid cards" markdown>

    - __① Settle Fees__<br>
      Confirm that all POS system fees have been paid.

    - [__② Create Products and SKUs__](../../ec/products/create-and-manage/create-update-products.md)<br>
      Confirm that online store products are set up and that **every product has an SKU code** (an SKU is a product's unique identifier).<br><br>
      [→ Bulk Fill Product SKU Codes Tutorial](bulk-update-product-skus.md)

    - __③ Update Inventory Settings__<br>
      Check online store product inventory. If it is not set to **unlimited inventory (∞)**, inventory will default to zero after POS is activated.

    - __④ Submit an Activation Request__<br>
      Submit your request to your store setup consultant. After activation, a **POS Features** tab will appear in the back-office menu.

    </div>

=== "Understanding Core Concepts"

    <div class="grid cards" markdown>

    - :lucide-git-branch:{ .lg }
      [__Omnichannel Inventory Management__](../inventory/index.md)<br>
      The EC online store and POS stores are **separate stores with separate inventory**. After activation, use inbound, outbound, or transfer orders, or stocktaking, to adjust inventory levels.

    - :lucide-plug:{ .lg }
      [__Account Permission Management__](../store/staff-permissions-and-account-management.md)<br>
      Understand how to set up role identities and bind employee accounts to them.

    </div>