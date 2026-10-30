---
title: "Thermal Print Convenience Store Shipping Labels"
description: "Use convenience store thermal printing to print A6 shipping labels"
created:
last_modified: 2026-07-07 13:59
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/cvs-shipping/thermal-print-cvs-waybill/"
type: guide
author: Jase
reviewers: []
notes:
  - 需使用支援A6熱感應標籤機
  - 條碼不可凹折、裁切或縮放
  - 批次列印需勾選相同物流商訂單
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
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 列印託運單
  - 處理超商出貨
  - 解決列印問題
features:
  - 熱感列印
  - 超商託運單
  - A6尺寸
  - 7-11 物流
  - 全家物流
  - B2C 大宗寄倉
  - C2C店到店
  - 黑貓快速到店
prerequisites:
  - 訂單配送方式為7-11或全家
  - C2C訂單須於新版訂單列表操作
  - 瀏覽器未阻擋彈出視窗
related: []
tags:
  - "Thermal Printing"
  - "A6 Shipping Labels"
  - 7-Eleven
  - "Logistics Shipping"
  - "Shipping Label Printing"
  - FamilyMart
  - "Shipping Labels"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12114
  - https://www.cyberbiz.io/support/?p=39461
comments: false
search:
  exclude: false
icon: lucide/printer
hide:
---

![Convenience store thermal printing](../../../assets/images/ec-訂單-下載超商 B2C托運單.en.png){ title="Convenience Store Thermal Printing" .hero-page }

## About Thermal Printing Convenience Store Shipping Labels

Convenience store thermal printing outputs shipping labels in **A6 size (100 mm × 150 mm to 105 mm × 150 mm)** for **7-Eleven and FamilyMart** logistics, so you can print directly on thermal label paper and stick the labels on packages.

The system offers two formats:

- **Standard Print (A4)**
- **Thermal Print (A6)**

## Prerequisites and Limitations

**Supported logistics**

- **7-Eleven**: B2C bulk shipping / C2C store-to-store
- **FamilyMart**: B2C bulk shipping / C2C store-to-store

**Version limits**

- **B2C orders**: You can download thermal print shipping labels from the legacy or new order list.
- **C2C orders**: You can download thermal print shipping labels only from the new order list.

**Other support**

- **EZCAT Quick Store Delivery**: Supports thermal printing. We recommend waterproof labels or a clear pouch so moisture doesn't affect barcode scanning.

## Shipping Label Formats

<div class="grid" markdown>

![A4 shipping label example](../../../assets/images/ec-訂單-超商托運單範例-A4.en.png){ title="A4 Shipping Label Example" }
/// caption
Standard print - A4
///
![A6 shipping label example](../../../assets/images/ec-訂單-超商托運單範例-A6.en.png){ title="A6 Shipping Label Example" }
/// caption
Thermal print - A6
///

</div>


## Steps

!!! warning "Important Notes"
	- **Browser settings tip:** If the file doesn't download, make sure pop-up blocking isn't turned on.

### Print One Label <small>Single Order</small>

1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.
2. Select the order to ship (the delivery type must be 7-Eleven or FamilyMart).
3. Click **Select Action** in the upper-right corner.
4. Select **Thermal Print (A6)**. The system generates an A6 shipping label file.  

![Print convenience store shipping labels](../../../assets/images/ec-訂單-列印超商 B2C 托運單.en.gif){ title="Print Convenience Store Shipping Labels" }

!!! info "If the order doesn't use convenience store logistics, the thermal print option doesn't appear."

---

### Print Multiple Labels <small>Continuous Printing</small>

1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.
2. Select multiple orders. **The delivery type must be exactly the same**.
3. Click **Download XX Shipping Labels and Change to Shipped** in the upper-right corner.
4. After downloading the ZIP file, print the **A6 shipping label file** in it.


!!! warning "If you select orders from different carriers (such as 7-Eleven + FamilyMart), the download option doesn't appear."

---

## Hardware and Supplies Recommendations

### Printer Requirements

- You need a thermal label printer that supports **standalone A6 size**.

---

### Recommended Models <small>For Reference Only</small>

- TSC TTP-225
- TSC TTP-323

---

### Label Rules

- The barcode must be **flat on the wide side of the package**.
- Don't fold, cut, or scale it, or the convenience store may not be able to scan it.

## Reprint Shipping Labels

- You can reprint shipping labels from the order list. The steps are the same as the first print.

- When reprinting, you can choose:

    - Standard Print (A4)  
    - Thermal Print (A6)

## More Tasks

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Expiration by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See the reprint deadline and expiration rules for each convenience store carrier.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Shipping Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label is voided or past its reprint deadline, get a new tracking number and download a new shipping label.

</div>


## FAQ

??? quote "Why can't I find the Thermal Print (A6) option?"  
	Usually for one of the following reasons:

	- The order's delivery type isn't 7-Eleven or FamilyMart.
	- You're using **C2C orders in the legacy order list**.
	- You selected orders from different carriers for a batch action.  Make sure the order logistics type is correct and C2C orders are in the new order list.

??? quote "Why doesn't the download shipping labels option appear when I batch print?"  
	Batch printing supports only orders with **the same carrier and the same delivery type**. If you select different logistics (such as 7-Eleven + FamilyMart), the download option doesn't appear.

??? quote "Do I have to use A6 size for thermal printing?"  
	Yes. Convenience store thermal printing supports only **A6 (100 mm × 150 mm to 105 mm × 150 mm)**. If you use non-A6 label paper or scale the print, convenience store devices may not be able to read the barcode.

??? quote "Can I print thermal shipping labels with a regular printer?"  
	We don't recommend it. Thermal printing requires a **dedicated printer that supports thermal label paper**. Regular laser or inkjet printers work only for A4 shipping labels.


??? quote "Why doesn't the browser respond when I download shipping labels?"  
	The browser may have pop-up blocking turned on, or the download was blocked.

	Check that:  

	- Pop-ups are allowed for this site  
	- The browser isn't blocking downloads
