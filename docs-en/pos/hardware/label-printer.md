---
title: "Label Printer"
description: "Print your own product labels with barcodes, prices, and expiration dates to speed up in-store checkout and improve inventory accuracy."
created: 2026-03-25 16:20
last_modified: 2026-05-28 14:48
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
  - 如何安裝標籤機
  - TSC_標籤機列印教學
  - 商品條碼標籤列印步驟
  - 標籤機碳帶安裝教學
features:
  - 商品標籤列印
  - TSC TTP-323
  - POS APP 整合
  - 條碼標籤
prerequisites:
  - 設定 POS 商店與機台
related:
  - pos/software/drivers/
  - pos/check/print-product-labels/
tags:
  - label_printer
  - TSC
  - product_barcode
  - store_operations
  - label_printing
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 標籤基本設定
  - 選擇商品
  - 列印數量
  - POS_APP_驅動程式
paths:
  - POS 功能 > 商品標籤列印
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=9723
permalink: "https://help.cyberbiz.io/pos/hardware/label-printer/"
comments: false
search:
  exclude: false
icon: lucide/printer
hide: []
---

# Label Printer
Merchants can print their own product labels with barcodes, prices, expiration dates, and other information to speed up in-store checkout and improve inventory accuracy.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
    - **New Arrivals**: Print custom labels for newly received products that have no original barcode, so the front counter can scan them quickly at checkout.
    - **Price Changes**: Reprint and apply labels when a product's price changes or a promotion starts.
    - **Expiration Management**: For fresh or date-sensitive products, print the expiration date on the label so staff and customers can identify it easily.
    - **Private-Label Brands**: Use the label printer to produce internationally compliant barcode labels for self-made and self-sold products, enhancing their professional appearance.


## Important Notes { #prerequisites-label-printer }

- **Supported Models**: The system currently supports only **TSC TTP-225** and **TSC TTP-323** label printers.
- **Operating System Requirement**: The computer must run Windows Pro. Windows Home will not run the feature properly.

    > Path: Settings > System > System Information > Windows Specifications (Windows 11 shown as an example).
        ![](../../assets/images/Windows-系統-系統資訊-POS標籤機適用系統版本01.en.png){ .screenshot }

- **Feature Activation**: Contact CYBERBIZ Customer Support to enable the **Label Printing** feature in the back office.
- **Software Environment**: Connect the label printer to a computer with the **POS APP Driver** installed first.
- **Encoding Restrictions**:
    - Product SKU codes should be **15 characters** or fewer (letters or digits).
    - SKUs that contain special characters (such as @, #, *, &) cannot be converted to barcodes at this time.
- **Hardware Compatibility Warning**: If you use existing devices other than the supported models, the system does not guarantee a successful connection.

    > Recommended setup: First download the [POS Device Connection Driver](../software/drivers.md) and run a label printing test. Confirm compatibility before use.


## Operating Procedure { #operate-label-printer }

### Step 1: Select the Label Printer and Supply Specifications { #operate-label-printer-step-a-supplies }

| **Model** | **TSC TTP-225** | **TSC TTP-323** |
| -------- | --------------- | --------------- |
| **Resolution** | 203 dpi (8 dots/mm) | 300 dpi (12 dots/mm) |
| **Print Method** | Direct thermal / Thermal transfer | Direct thermal / Thermal transfer |
| **SDRAM** | 4 MB SDRAM | 4 MB SDRAM |
| **Flash** | 8 MB | 8 MB |
| **Maximum Ribbon Length** | 90 m | 90 m |
| **Print Speed** | 5 ips (127 mm/s) | 3 ips (76 mm/s) |
| **Supply Specifications** | 1. Ribbon VSI 5cmX74M<br>2. Label stickers Label_40X30X1500 | 1. Ribbon VSI 5cmX74M<br>2. Label stickers Label_40X30X1500 |

![](../../assets/images/POS-裝置-標籤列印機01.en.png){ .screenshot }

### Step 2: Hardware Installation and Connection Test { #operate-label-printer-step-b-hardware }

Before you start printing, make sure the label printer's hardware is fully set up.

1. **Install Supplies**: See the TSC official tutorial videos on [installing the ribbon](https://www.youtube.com/watch?v=tEFeqpA--hs) and [installing label rolls](https://www.youtube.com/watch?v=thvZkQJV-Rs).
2. **Connect to Computer**: Connect the label printer to the computer via USB.
3. **Start the Driver**: Open the [POS APP Driver](../software/drivers.md) on the computer.
4. **Auto-Detection**: POS APP automatically detects the new device. In the pop-up window, select **TSC Label Printer** and click Start Using.




## More Actions { #next-steps-label-printer }

<div class="grid cards" markdown>

- :lucide-printer-check:{ .lg }   
  [__Print Product Labels__](../check/print-product-labels.md)     
  Run a print test in the back office.

</div>
