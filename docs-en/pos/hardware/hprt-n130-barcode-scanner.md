---
title: "Set up POS Barcode Scanner (HPRT N130)"
description: "Learn how to connect the HPRT N130 barcode scanner to the POS system, and test the connection, scan products, and troubleshoot common issues."
created: 2026-06-12 18:55
last_modified: 2026-06-12 18:55
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
  - 硬體設定
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
  - 設定 POS 掃碼槍
  - 排除掃碼槍連線問題
  - 測試條碼掃描器
features: 
  - POS 結帳
  - 條碼掃描
prerequisites: 
  - "需具備 HPRT N130 條碼掃描器"
related: []
tags: 
  - "Barcode Scanner"
  - "Barcode Scanning"
  - "Hardware Setup"
  - HPRT
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - POS 結帳畫面
  - 商品搜尋
paths: 
  - POS 功能 > 所有 POS 商店
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/pos/hardware/hprt-n130-barcode-scanner/"
search:
  exclude: false
icon: lucide/barcode
hide: []
---

# Set up POS Barcode Scanner (HPRT N130)
Learn how to connect the HPRT N130 barcode scanner to the POS system, and test the connection, scan products, and troubleshoot common issues.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
	- **Quick Checkout**: On the POS checkout screen, scan a product barcode to automatically add the product details and amount.
	- **Product Search**: Scan a barcode in the admin or POS search field to quickly locate a specific product.
	- **Inventory Count**: Scan products during a stocktake to improve inventory verification efficiency.


## Before You Start { #prerequisites-hprt-scanner }

- **Applicable Devices**: The HPRT N130 uses a USB interface. Once connected, the system automatically recognizes it as an input device, so no driver installation is required.

  	![](../../assets/images/POS-裝置-HPRT N130掃碼槍01.en.jpg){ .small-image }

- **Input Method Requirement**: When scanning, make sure the input method is set to **English mode** to prevent scanned barcode numbers from being misread due to input method interference.
- **Prepare Products in Advance**: The scanner only reads barcodes and does not create product records. If the POS cannot find a product, first check the barcode settings in the product admin.
- **Maintenance Tip**: Keep the scan window clean and free of scratches or smudges, which can affect scanning performance.


## Connect and Test the Connection { #operate-hprt-scanner }

Run a basic connection test when you use the scanner for the first time or after you replace a device.

1. Plug the scanner's USB connector into a USB port on the computer or POS host.
2. The scanner turns on automatically and emits a beep.
3. Open **Notepad** or **Excel** on the computer.
4. Place the cursor in a blank area, and scan any product barcode.
5. **Expected Result**: The screen should correctly display the number sequence of the barcode.

## Scan Products { #operate-scan-products }

Scan products during checkout or search in the POS system.

1. Sign in to the POS system, and go to the **Checkout** or **Product Search** screen.
2. Click the search field, **make sure the cursor is in the field**, and aim the scanner's light at the center of the product barcode.
3. After you hear the beep, the system automatically enters the barcode into the field and displays the matching product.

!!! info "The barcode appears in Notepad, but the POS does not show the product?"
    The scanner only reads the barcode number. If the POS cannot find a product after scanning, first check whether the barcode is correctly entered in the product data in the admin.


## FAQ { #faq-hprt-scanner }

??? quote "The scanner does not respond, and the indicator light is off?"
    1. Check that the USB cable is securely connected.
    2. Try a different USB port.
    3. If the scanner still does not respond, contact your hardware supplier to check the device status.

??? quote "The scanner beeps, but no barcode number appears on the screen?"
    Check the following:

    - You have clicked the field where you want to enter the barcode.
    - Open Notepad to test whether the barcode can be scanned.
    - If Notepad also shows nothing, unplug and reconnect the scanner, or test it with a different USB port.

    If only specific products cannot be scanned, test with other products:

    - If other products scan correctly, check whether the barcode on the product is clear and complete.
    - If the barcode scans but the POS cannot find the product, check whether the barcode has been added to the product in the admin.

??? quote "After scanning, the POS shows 'Product not found'?"
    - **Confirm the Product Record**: Check whether the barcode has been set up for the product in the admin.
    - **Verify the Barcode**: Go to the admin and confirm that the Barcode field for the product exactly matches the scanned number.
    - **Barcode Integrity**: Check whether the barcode on the product packaging is damaged, dirty, or unclearly printed.

??? quote "How do I restore the scanner's default settings if its configuration is abnormal?"
    Scan the **Restore Factory Defaults** setting barcode in the manufacturer's manual to restore factory default values. **Any scanner settings you previously changed will be cleared**.

