---
title: "Product Not Found After Scanner Scan"
description: "Resolve issues where the POS system cannot recognize or find a matching product when a barcode scanner scans a product barcode, including EAN-13 and UPC-A encoding conversion settings."
created: 2026-04-07 15:30
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - CYB支援的掃碼槍是HS-8122？
  - 此文件只適用13碼(EAN-13)標籤？
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 商品
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
  - 排除掃描失敗問題
  - 設定掃描槍編碼轉換
features:
  - 掃描槍設定
  - 商品條碼
prerequisites:
  - 需先於後台建立商品並設定正確的 SKU 或條碼
related: []
tags:
  - "Barcode Scanner"
  - Barcode
  - EAN-13
  - UPC-A
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - POS 結帳界面
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=4201
permalink: "https://help.cyberbiz.io/pos/check/product-not-found-after-scanner-scan/"
comments: false
search:
  exclude: false
icon: lucide/scan-barcode
hide: []
---

# Product Not Found After Scanner Scan
Resolve issues where the POS system cannot recognize or find a matching product when a barcode scanner scans a product barcode, including EAN-13 and UPC-A encoding conversion settings.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
	- **No response after scanning**: The POS system does not load product information after a product barcode is scanned.
	- **Barcode mismatch**: The scanned digits do not match the number on the product label (for example, one digit is missing).
	- **New device setup**: You have replaced the scanner and need to align its initial encoding.


## Usage Notes { #prerequisites-scan-missing }

- **SKU check**: Make sure the product has a matching SKU or barcode set up in the CYBERBIZ admin backend.
- **Encoding differences**: UPC-A (12 digits), common in North America, and EAN-13 (13 digits), common internationally, may fail to scan correctly because the leading 0 is handled differently.
- **Device support**: This guide applies to barcode scanners provided by CYBERBIZ. If you use a device from another supplier, contact your device supplier.

## Procedure { #operate-scan-missing }

### Step 1: Check Backend Data { #operate-scan-missing-1-confirm-admin }

1. Log in to the CYBERBIZ POS admin backend and go to **Products > All Products**.
2. Check that the **SKU Code** or **Barcode** field for the product contains the correct numeric code.

### Step 2: Check the Barcode Format { #operate-scan-missing-2-barcode }

If the product barcode uses the EAN-13 format (13 digits), check whether the first digit on the label is **0**.

![](https://www.cyberbiz.co/support/wp-content/uploads/2019/10/EAN_0-1.png){ .small-image }

### Step 3: Verify the Scanner Read Result { #operate-scan-missing-3-scan-result }

1. On your computer, open a browser and click the search bar.
2. Use the scanner to scan the barcode above.
3. Check the output digits:
    - **Output is 0012345678905**: The scanner is set up correctly.
    - **Output is 012345678905**: The scanner is reading in UPC-A format and automatically omits the leading region digit 0.

### Step 4: Fix the Scanner Settings { #operate-scan-missing-4-scan-settings }

If the scanner drops the leading 0, scan the setup barcode below with your scanner. When you hear the **Bi Bi Bi~** beep, the "UPC-A to EAN-13" conversion setting is complete.

![](https://www.cyberbiz.co/support/wp-content/uploads/2019/10/image-1.png){ .small-image }



!!! info "EAN-13 and UPC-A Encoding"
    - **UPC-A**: The earliest 12-digit encoding, mainly used in the United States and Canada.
    - **EAN-13**: The international standard encoding. It adds one region digit in front of UPC-A. The region digit for the United States and Canada is **0**, but some scanners do not display this digit by default.


## Frequently Asked Questions { #faq-scan-missing }

??? quote "What should I do if garbled text appears after scanning?"
    This is usually caused by an incorrect input method setting on the scanner. Make sure the input method on the computer or POS terminal is set to **English half-width** while scanning.

??? quote "Can I set up a scanner not provided by CYBERBIZ the same way?"
    Setup barcodes differ by scanner brand. If you use your own device, look up the user manual for that model and search for settings related to **UPC-A to EAN-13** or **Transmit UPC-A Check Digit**.

