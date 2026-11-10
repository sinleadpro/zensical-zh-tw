---
title: "EPSON TM-M30III Invoice Printer Installation Guide (Wi-Fi Connection)"
description: "Install the EPSON TM-M30III invoice printer over Wi-Fi so it can be used on a tablet without installing a driver."
created: 2026-05-27 12:20
last_modified: 2026-05-27 12:20
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
  - 安裝發票機
  - EPSON TM-m30III 安裝
  - Wi-Fi 連接發票機
features: 
  - 發票機安裝
  - Wi-Fi 設定
prerequisites: []
related:
  - pos/hardware/epson-tm-t82iii-invoice-printer/
tags: 
  - EPSON
  - "Invoice Printer"
  - "POS Hardware"
  - TM-m30III
  - Wi-Fi
acoiv: activate
apis: []
devices: 
  - tablet
  - mobile
ui_components: 
  - 發票機
  - 進紙按鈕
paths: 
  - POS 功能 > 所有 POS 商店 > 修改 POS 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=53134
permalink: "https://help.cyberbiz.io/pos/hardware/epson-tm-m30iii-invoice-printer/"
comments: false
search:
  exclude: false
icon: lucide/printer
hide: []
---

# EPSON TM-M30III Invoice Printer Installation Guide (Wi-Fi Connection)
Install the EPSON TM-M30III invoice printer over Wi-Fi so it can be used on a tablet without installing a driver.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


!!! tip "Use Cases"
	- **Wireless Counter Environment**: Counter space is limited, and you want fewer cables to keep the area tidy.
	- **Mobile Checkout**: Use a tablet to check out customers throughout the store and print invoices remotely.
	- **Multi-Device Sharing**: Multiple tablets share the same invoice printer.

---

## Before You Start { #prerequisites-epson-m30 }

- **Applicable Model**: EPSON TM-M30III.
- **Connection Method**: This guide uses a Wi-Fi connection, which does not require a driver.
    - For a USB connection, you must install the driver. See [EPSON TM-T82III Installation Guide](epson-tm-t82iii-invoice-printer.md).
- **Environment Requirements**: The invoice printer and the checkout tablet must connect to the same Wi-Fi network.

## Operating Procedure { #operate-epson-m30 }

### 1. Hardware Preparation and Power On { #operate-epson-m30-1-hardware }

1. Open the top cover, and load a roll of thermal paper for electronic invoice proof copies.
2. Press the **Power Button** until the indicator light blinks, which means startup is complete.

### 2. Start Wi-Fi Pairing Mode { #operate-epson-m30-2-wi-fi }

1. Open the top cover, and press and hold the **Feed Button** below the power button for about 3-5 seconds.
2. The third indicator light from the left at the bottom begins to blink.
3. Pull the invoice paper out slightly, and close the top cover. The printer automatically feeds out a short piece of paper.

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用01-scaled.jpg){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用02-scaled.jpg){ .screenshot }

    </div>

### 3. Get the Wi-Fi Setup QR Code { #operate-epson-m30-3-wi-fi }

1. Click the **Feed Button** 5 times in a row, then click it once more.
2. The printer feeds out a setup sheet that contains a **QR Code**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用03-scaled.jpg){ .screenshot }

### 4. Set up the Wi-Fi Connection { #operate-epson-m30-4-run-wi }

1. Use the checkout tablet to scan the QR Code above.
2. On the tablet, allow the printer to join the current Wi-Fi network.
3. The printer then feeds out a second QR Code. Scan this second QR Code with the tablet.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用04-scaled.jpg){ .screenshot }

4. The tablet displays the Wi-Fi setup interface. Click **Wi-Fi**.
5. Find the details sheet from step 3. Enter the alphanumeric characters that follow the SSID field `DIRECT-TM-m30III-` on that sheet into the **Current Password** field on the tablet interface.

    <div class="grid cards borderless two-columns" markdown>

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用05.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用07-scaled.jpg){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用06.png){ .screenshot }

    </div>

6. On the tablet, enter the current Wi-Fi password, and wait for Setup to complete.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用08.png){ .screenshot }

### 5. Get the IP Address and Authorize the Connection { #operate-epson-m30-5-ip-connection }

1. After setup is complete, the printer automatically feeds out a sheet that contains the **IP Address**.
2. Open a browser on the tablet, and enter the IP address in the address bar.
3. If the message "Your connection is not private" appears, click **Advanced**, then click **Proceed** to allow the connection.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用09-scaled.jpg){ .screenshot }

### 6. POS Front-End Connection Test { #operate-epson-m30-6-pos-frontend }

1. Log in to the POS front end using the same browser.
2. Click **Connect**, and enter the IP address you obtained earlier.
3. Click **Connect and Test**. If the printer feeds out a test sheet, the connection is successful.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用10.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-安裝-EPSON-TM-M30III發票機-wifi啟用11.png){ .screenshot }




