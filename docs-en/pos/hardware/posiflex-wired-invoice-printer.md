---
title: "Posiflex Wired Invoice Printer"
description: "Install the Posiflex invoice printer, including driver installation, hardware connection, invoice format testing, and common troubleshooting methods."
created: 2026-03-25 18:45
last_modified: 2026-05-28 14:48
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
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何安裝Posiflex發票機
  - 發票機連線失敗排解
  - 發票印出來是空白怎麼辦
  - 發票機隔板安裝教學
features:
  - 發票機串接
  - 自動開立發票
  - 盟立加值中心整合
  - 硬體連線診斷
prerequisites: []
related:
  - pos/software/drivers/
tags:
  - Posiflex
  - "Invoice Printer"
  - "Mengli Invoice"
  - "POS Hardware"
  - E-Invoice
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - POS 驅動程式
  - 熱感應發票機
  - 快速測試
  - 自動開立發票
paths:
  - POS 功能 > 所有 POS 商店 > 修改 POS 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=4225
  - https://www.cyberbiz.io/support/?p=5064
permalink: "https://help.cyberbiz.io/pos/hardware/posiflex-wired-invoice-printer/"
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---

# Posiflex Wired Invoice Printer
Install the Posiflex invoice printer, including driver installation, hardware connection, invoice format testing, and common troubleshooting methods.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


## Before You Begin { #prerequisites-posiflex-printer }

- **Software environment**: The CYBERBIZ POS driver must stay open. **Do not close the window** (you can minimize it).
- **Hardware time**: Invoice issue times follow the **POS computer's hardware clock**. Make sure the computer's time zone and time are correct.
- **Key requirement**: If you use the Mengli e-invoice service, provide the **Mengli channel key** to CYBERBIZ customer support before you install the invoice printer.


## Setup Procedure { #operate-posiflex-printer }

### Step 1: Install the Driver and Prepare the Hardware { #operate-posiflex-printer-step-a-install }

1. **Installer**: Download and install the [CYBERBIZ POS driver](../software/drivers.md).

    ![](../../assets/images/POS-驅動程式-桌面圖示01.en.png)

2. **Install the paper roll**: Insert the thermal paper roll into the slot (thermal side facing up).

     <div class="grid cards borderless two-columns" markdown>

    - ![Install paper roll 01](../../assets/images/POS-安裝-Posiflex有線發票機-裝紙捲01.en.jpg){ title="Install Paper Roll 01" }
    - ![Install paper roll 02](../../assets/images/POS-安裝-Posiflex有線發票機-裝紙捲02.en.jpg){ title="Install Paper Roll 02" }
    - ![Install paper roll 03](../../assets/images/POS-安裝-Posiflex有線發票機-裝紙捲03.en.jpg){ title="Install Paper Roll 03" }

    </div>

    - **Note**: If you use the **PP-8800** model, you must install the included **divider** to hold 58 mm thermal invoice paper in place.

    <div class="grid cards borderless two-columns" markdown>

    - ![Install paper roll 01](../../assets/images/POS-安裝-Posiflex有線發票機-裝隔板01.en.png){ title="Install Divider 01" }
    - ![Install paper roll 02](../../assets/images/POS-安裝-Posiflex有線發票機-裝隔板02.en.png){ title="Install Divider 02" }
    - ![Install paper roll 02](../../assets/images/POS-安裝-Posiflex有線發票機-裝隔板03.en.png){ title="Install Divider 03" }

    </div>

3. **Power on**: Connect the invoice printer to power and turn on its switch.

    ![](../../assets/images/POS-安裝-Posiflex有線發票機-開機01.en.jpg){ .small-image }

### Step 2: Connect and Link the System { #operate-posiflex-printer-step-b-connection }

1. **USB connection**: Connect the invoice printer to the computer with a USB cable.

    ![](../../assets/images/POS-安裝-Posiflex有線發票機-啟用01.en.png){ .screenshot }

2. **Start the driver**: Open the CYBERBIZ driver. The system should detect the device automatically.
3. **Select the model**: In the program interface, click **Thermal Invoice Printer**.

    <div class="grid cards borderless two-columns" markdown>

    - ![System connection 01](../../assets/images/POS-驅動程式-連線有線發票機01.en.jpg){ title="System Connection 01" }
    - ![System connection 02](../../assets/images/POS-驅動程式-連線有線發票機03.en.png){ title="System Connection 02" }

    </div>

4. **Refresh the front end**: If the message "Not yet bound to a POS store" appears, open or refresh the **POS front-end page** in your browser, and keep the driver open.

    ![](../../assets/images/POS-驅動程式-連線有線發票機02.en.png){ .screenshot }

### Step 3: Connection and Print Test { #operate-posiflex-printer-step-c-connection }

1. **Quick test**: In the driver window, **click here** to run a quick test. The invoice printer should print a short test receipt.

    <div class="grid cards borderless two-columns" markdown>

    - ![Test 01](../../assets/images/POS-驅動程式-有線發票機-列印測試01.en.png){ title="Test 01" }
    - ![Test 02](../../assets/images/POS-驅動程式-有線發票機-列印測試02.en.png){ title="Test 02" }
    - ![Test 03](../../assets/images/POS-安裝-Posiflex有線發票機-測試01.en.jpg){ title="Test 03" }

    </div>

2. **Live transaction test**:
    - Go to the POS front end and complete a small test checkout.
    - If the invoice type field shows only **"Self-issued"** and no other options such as "Paper e-invoice" or "Company tax ID", the **integration is not yet active**. Contact CYBERBIZ technical support.

    ![](../../assets/images/POS-前台-結帳-開立發票選項01.en.png){ .screenshot }

3. **Print the invoice**: Complete checkout and check whether the invoice printer prints the invoice correctly.

    ![](../../assets/images/POS-安裝-Posiflex有線發票機-測試02.en.jpg){ .small-image }

4. **Cancel the order**: After you cancel the order, the **Orders** page on the front end should show that the invoice was voided successfully.

    <div class="grid cards borderless two-columns" markdown>

    - ![Cancel order 01](../../assets/images/POS-前台-結帳-有線發票機取消測試訂單01.en.png){ title="Cancel Order 01" }
    - ![Cancel order 02](../../assets/images/POS-前台-結帳-有線發票機取消測試訂單02.en.png){ title="Cancel Order 02" }
    - ![Cancel order 03](../../assets/images/POS-前台-結帳-有線發票機取消測試訂單03.en.png){ title="Cancel Order 03" }

    </div>

### Step 4: Configure Invoice Issuing Settings { #operate-posiflex-printer-step-d-issue }

Go to **POS > POS Store List**, select the target store, click **Edit POS Settings**, and complete the issuing preferences.

![](../../assets/images/POS-後台-所有POS商店-修改POS子機設定01.en.png){ .screenshot }

- Auto-issue invoices: The system generates an e-invoice number when checkout is complete and uploads the transaction data to the Ministry of Finance.
- Auto-print invoices: The system works with the invoice printer to print paper invoices automatically.
- Auto-print details: When turned on, the system automatically prints the transaction detail report.

![](../../assets/images/POS-後台-所有POS商店-修改POS子機發票設定01.en.png){ .screenshot }

## Paper Roll and Consumable Information { #overview-posiflex-printer }

If you bought the invoice printer from CYBERBIZ, the machine includes two test rolls of paper. For future purchases, buy paper that meets the following specifications:

- **Specification**: 70 m standard thermal paper roll
- **Width**: 5.7 cm (58 mm)
- **Where to buy**: Buy from the [Ministry of Finance e-invoice thermal paper platform](https://invoice.ppmof.gov.tw/PSJ_Web/) or a general office supply store.

![](../../assets/images/POS-裝置-有線發票機紙捲01.en.png){ .screenshot }

## FAQ { #faq-posiflex-printer }

??? quote "Why does the driver show 'Registered devices: 0, 1 issue to fix'?"
    ![](../../assets/images/POS-驅動程式-疑難排解1-1.en.png){ .screenshot }

    This means the computer has not correctly recognized the invoice printer. Try the following steps:

    1. [Download and install the driver](https://drive.google.com/file/d/1_5E8MAY8fAAy5HDjuuX8cQ2hEcZBfiKQ/view?usp=sharing).

    2. Go to **Computers > Manage**.
        ![](../../assets/images/POS-驅動程式-疑難排解1-2.en.png){ .screenshot }

    3. In **Device Manager**, look for items with an exclamation mark under "Other devices".
        ![](../../assets/images/POS-驅動程式-疑難排解1-3.en.png){ .screenshot }

    4. Right-click and select **Update Driver**.
        ![](../../assets/images/POS-驅動程式-疑難排解1-4.en.png){ .screenshot }

    5. Click **Browse My Computer for Driver Software**.
        ![](../../assets/images/POS-驅動程式-疑難排解1-5.en.png){ .screenshot }

    6. In the browse dialog, select the **USBVCOM_Win_x64** folder.
        ![](../../assets/images/POS-驅動程式-疑難排解1-7.en.png){ .screenshot }
    7. Click **Install**.
        ![](../../assets/images/POS-驅動程式-疑難排解1-8.en.png){ .screenshot }
    8. After the issue is resolved, the device no longer shows an exclamation mark.
        ![](../../assets/images/POS-驅動程式-疑難排解1-9.en.png){ .screenshot }

??? quote "What should I do if the message 'An error occurred while installing the driver software' appears?"
    ![](../../assets/images/POS-驅動程式-疑難排解2-1.en.png){ .screenshot }

    1. [Download and install the program file](https://drive.google.com/file/d/1x1BPZeFaaAa8VjW3_pTiAqXP4OYCdE07/view).

    2. After installation is complete, click **Restart Now**.
        ![](../../assets/images/POS-驅動程式-疑難排解2-2.en.png){ .screenshot }

    3. Go to **Computers > Manage**.
        ![](../../assets/images/POS-驅動程式-疑難排解2-3.en.png){ .screenshot }

    4. In **Device Manager**, check whether the invoice printer is connected successfully.
        ![](../../assets/images/POS-驅動程式-疑難排解2-4.en.png){ .screenshot }

    5. A device without an exclamation mark is connected.
        ![](../../assets/images/POS-驅動程式-疑難排解2-5.en.png){ .screenshot }

??? quote "Can't find the device after I plug the USB cable into the POS host?"
    Select the setup steps that match your invoice printer model:

    === "Model 8800"
        Open the bottom of the machine, adjust the jumper settings, confirm that DIP switches 1, 2, 4, and 6 are all set to on, and restart the machine.
        ![](../../assets/images/POS-驅動程式-疑難排解3-1.en.png){ .screenshot }

    === "Model 8802"
        This model has no physical switches. Download the software and use it to check and adjust the settings.

        1. [Download the software](https://drive.google.com/file/d/11OFommtgJWqYcZFmGWaQT4373BsJC9sO/view?usp=sharing).
        2. Extract the file, click the Setup application in the folder, and complete the installation.
            ![](../../assets/images/POS-驅動程式-疑難排解3-2.en.png){ .screenshot }
        3. After installation, the following shortcut appears on the desktop.
            ![](../../assets/images/POS-驅動程式-疑難排解3-3.en.png){ .screenshot }
        4. Click the shortcut to open the software and check whether the following screen appears. If the screen does not match the image below, contact CYBERBIZ customer support.
            ![](../../assets/images/POS-驅動程式-疑難排解3-4.en.png){ .screenshot }

??? quote "What should I do if all basic checks are complete but the hardware (invoice printer / card reader) still fails to connect?"
    1. **Force restart the driver**: Fully close the **POS APP driver** in the taskbar, then run the program again.
    2. **Trigger hardware detection again**: Unplug the device's **USB cable** from the computer, wait 5 seconds, and plug it back in.
    3. **Perform a system reset (Reset)**:
        - In the **POS APP driver** interface, click the **Reset** button.
        - After the reset, repeat steps 1 and 2 above.
    4. **Key check**: Look at the driver interface and confirm that the correct device name appears or that the green connection indicator is lit.


??? quote "What should I do if the system shows the warning 'Try restarting the system and device first'?"
    ![](../../assets/images/POS-驅動程式-疑難排解5-1.en.jpg){ .screenshot }
    This issue usually stems from a **hardware connection problem** or a **driver loading failure**. Perform the following initial troubleshooting steps in order:

    1. Check the Hardware
        - Check whether the **USB cable** of the invoice printer (or card reader) is loose. We recommend unplugging and reconnecting it.
        - Confirm that the device is powered on and has enough paper (no red warning light).
    2. Restart the Core Program
        - Close and restart the **POS APP driver** on the computer.
        - Refresh the POS front-end page.
    3. Restart the Device
        - If the steps above do not work, **restart** the computer and the invoice printer. This usually resolves 90% of temporary connection conflicts.

    !!! info "Reminder"
        If the warning still appears after you restart and reconnect the devices, the device settings may have changed or the hardware may be faulty. Contact **CYBERBIZ customer service** for help with troubleshooting.


??? quote "The POS has an invoice number, but the EC order has no linked invoice record?"
    If you did not select **Self-issued** at checkout and entered a manually issued invoice number later, the invoice is **not marked** as manually issued. As a result, the EC order cannot link to or display the invoice.

??? quote "Why is the printed invoice blank?"
    This is usually because the thermal paper roll is **installed backward**. Check whether the paper feeds so that the print head contacts the thermal side (usually the smoother side facing up).
    ![](../../assets/images/POS-驅動程式-疑難排解4-1.en.png){ .screenshot }

??? quote "What should I do if the invoice printer makes unusual noises?"
    Check whether the paper roll is placed evenly and whether the cover is fully closed. Reposition the paper roll, then press the cover down firmly until you hear a click.

    [Invoice printer noise example](https://drive.google.com/file/d/12Cnb5YsTSt5HSYQBYukbcjOugdm4QGQ4/view?usp=sharing)