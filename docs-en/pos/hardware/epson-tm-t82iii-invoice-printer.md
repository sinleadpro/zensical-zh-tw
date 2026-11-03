---
title: "EPSON TM-T82III Wired Invoice Printer"
description: "Learn how to install the EPSON TM-T82III invoice printer, including hardware setup, Virtual Port Driver installation, COM Port assignment, and paper width adjustment."
created: 2026-03-25 20:45
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：POS驅動程式
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - POS 功能
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何安裝EPSON發票機
  - TM-T82III驅動程式下載
  - 解決EPSON發票機COM Port衝突
  - 調整發票列印寬度
features:
  - 發票機串接
  - TM Virtual Port Driver
  - 58mm發票列印
  - 自動裁刀
prerequisites: []
related:
  - pos/software/drivers/
tags:
  - EPSON
  - Invoice_Printer
  - TM-T82III
  - POS_Hardware
  - Driver
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - POS 驅動程式
  - Port Assignment Tool
  - TM-T82III Utility
paths:
  - POS 功能 > 所有 POS 商店 > 修改 POS 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=52249
permalink: "https://help.cyberbiz.io/pos/hardware/epson-tm-t82iii-invoice-printer/"
comments: false
search:
  exclude: false
icon: lucide/printer
hide: []
---

# EPSON TM-T82III Wired Invoice Printer
By correctly installing the EPSON TM-T82III professional invoice printer and configuring a virtual COM Port, merchants can print e-invoices quickly and reliably. This guide walks you through the full process, from hardware setup to driver configuration.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **Efficient In-Store Checkout**: Use the high-speed printing of the EPSON printer to reduce the time customers wait at the counter for their invoices.
    - **Space-Saving Setup**: The compact design of the TM-T82III suits checkout counters with limited space.
    - **Automated Tax Compliance**: Print e-invoice receipts that comply with Ministry of Finance regulations as soon as checkout is complete.


## Usage Notes

- **Applicable Model**: This guide is written specifically for the **EPSON TM-T82III** model.
- **Consumable Specification**: The printer uses **58mm** e-invoice thermal paper by default. When installing the paper, make sure the spacer is positioned correctly.


## Operating Procedure

### Step 1: Download and Install the POS Driver

Before setting up the hardware, make sure the computer is ready for communication.

1. Download the [CYBERBIZ POS Driver](../software/drivers.md).
2. After installation, open the program and wait for it to update automatically to the latest version.



### Step 2: Prepare the Hardware and Install the Paper Roll

Refer to the manual included with the printer, or to the [Product Manual List](https://support.epson.net/setupnavi/?PINF=bsmanual&OSC=IOS&LG2=ZH&MKN=TM-T82III) and the [User’s Guide](https://download4.epson.biz/sec_pubs/bs/pdf/TM-T82III_ug_asia_04.pdf), and complete the following steps:

1. **Install the spacer**: Open the printer's top cover and make sure the spacer included in the box is installed to secure the 58mm paper roll.
2. **Load the thermal paper**: Insert the thermal paper designated for e-invoice receipts, and make sure the heat-sensitive side faces up.
3. **Connect the power**: Plug in the printer and turn on the power switch.


### Step 3: Install the Virtual Port Driver and Assign a COM Port

This step is critical for a successful connection. Be sure to follow the steps in order.

1. **Download the driver**: Download the [TM Virtual Port Driver](https://download-center.epson.com/download/?module_id=070d7dfb-72df-4f28-9304-3336b198c5f3%3A8.70f&device_id=TM-T82III&os=WIN1164&region=TW&language=zh-TW).
2. **Run the installer**: After installation is complete, **we strongly recommend restarting your computer**.
3. **Connect the hardware**: Use a USB cable to connect the printer to your Windows computer.
4. **Assign a COM Port**:
    - Open the **EPSON TM Virtual Port Driver Port Assignment Tool** software.
    - Refer to `C:\Program Files (x86)\EPSON\TMCOMUSB\TMVirtualPortDriver_User'sManual.pdf`'s `手動設備設定 - USB` setup guide, and assign the detected printer to a currently **unused** COM Port (such as COM3 or COM4).


<div style="position: relative; padding-bottom: 56.25%; height: 0;">
  <iframe src="https://www.cyberbiz.io/support/wp-content/uploads/POS-EPSON發票機軟體安裝設定.mp4" 
          frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen 
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
  </iframe>
</div>

### Step 4: Verify the Paper Width Setting

If invoice text is misaligned or cut off, check this setting. This setting is usually preconfigured before shipment, so merchants only need to verify it when problems occur.

1. Install the [TM-T82III Utility](https://download3.ebz.epson.net/dsc/f/03/00/15/59/89/e13530028b241ec0d281f763e894ce21988975cb/TM-T82IIIUtility111_e2.exe). [EPSON Official Download Site](https://support.epson.net/setupnavi/?PINF=swlist&OSC=IOS&LG2=ZH&MKN=TM-T82III)
2. Go to **Basic Settings > Printing Control**.
3. Make sure **Paper width - Number of columns** is set to `58mm - 35 columns`.



### Step 5: Connect and Print a Test Page

1. Return to **CYBERBIZ POS Driver**.
2. In the device list, select the **EPSON invoice printer** that has an assigned COM Port.
3. Click **Test Print**. If a test receipt prints successfully, the installation is complete.

