---
title: "Ship with FamilyMart Frozen C2C Store-to-Store"
description: "Ship with FamilyMart Frozen C2C Store-to-Store, including setup, order shipping, packaging rules, drop-off deadlines, and exception handling."
created:
last_modified: 2026-07-26 19:55
lang: en-US
permalink: "https://help.cyberbiz.io/ec/orders/cvs-shipping/family-mart-frozen-c2c/"
type: guide
author: Jase
reviewers: []
notes:
  - 企業版超商取貨付款方式表格有誤，目前以 [https://docs.google.com/spreadsheets/d/1EnwSkTWX2o5wkjBkfUcvxmfdv9dDj2d5/edit?gid=385488738#gid=385488738](https://docs.google.com/spreadsheets/d/1EnwSkTWX2o5wkjBkfUcvxmfdv9dDj2d5/edit?gid=385488738#gid=385488738) 更全面 BY MOMO
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 啟用冷凍店到店服務
  - 處理冷凍訂單出貨
  - 管理包裹與配送
  - 解決異常取貨狀況
features:
  - 全家冷凍店到店 C2C 出貨服務
  - 訂單出貨
  - 包裝規範
  - 寄件時效
  - 異常處理
prerequisites:
  - 於CYBERBIZ後台啟用全家冷凍店到店服務
  - 同意相關服務條款
  - 填寫寄件人資訊
related:
  - ec/orders/cvs-shipping/cvs-c2c-shipping/
  - ec/orders/references/cvs-waybill-expiration-reference/
  - ec/orders/renew-waybill-after-expiration/
tags:
  - "FamilyMart Frozen Store-to-Store"
  - "Frozen Logistics"
  - "Convenience Store Shipping"
  - "Frozen Store-to-Store"
  - "Logistics Settings"
  - C2C
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 金物流 > 超商物流
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8221
  - https://www.cyberbiz.io/support/?p=40721
comments: false
search:
  exclude: false
icon: lucide/snowflake
hide:
---

![Frozen store-to-store shipping](../../../assets/images/ec-金物流-超商物流-全家冷凍店到店 C2C.en.png){ title="Frozen Store-to-Store Shipping" .hero-page }

## About FamilyMart Frozen C2C Store-to-Store Shipping

FamilyMart frozen store-to-store (C2C) lets you easily manage frozen product sales and inventory, receive and ship orders from the admin, and deliver quickly to the store the shopper chose, boosting sales and customer satisfaction.

With FamilyMart frozen store-to-store (C2C), you can:

- Manage frozen product inventory and orders
- Complete store-to-store delivery quickly
- Give shoppers more pickup options
- Grow frozen product sales and revenue

## Prerequisites and Limitations

### Packaging and Temperature Rules

Frozen packages have strict size and temperature limits. If they don't meet the rules, store staff or drivers can refuse them:

- **Temperature**: Supports only **frozen food** below **-18℃**. Packages must be **pre-chilled for 12+ hours** and fully frozen before shipping.
- **Box rules**:
    - **Since 2025/06/09**, FamilyMart has removed the requirement to use dedicated boxes, and you can use your own boxes.
    - We recommend boxes **0.5 cm** thick. Don't use straps, styrofoam, tamper-evident bags, or combined boxes, and seal the package fully with nothing exposed.
- **Labels**: Print the shipping label, put it in a **clear waterproof pouch**, and stick it flat on the wide side of the box. Don't fold or scale the barcode.

---

### Shipping and Time Limits

- **How to ship**: Print and stick the shipping label yourself, or [write down the tracking number and print the service slip (payment slip) at a FamilyMart **FamiPort** kiosk](cvs-c2c-shipping.md#famiport){ title="Ship with Convenience Store C2C Store-to-Store" }.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Expiration by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See the reprint deadline and expiration rules for each convenience store carrier.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Shipping Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label is voided or past its reprint deadline, get a new tracking number and download a new shipping label.

</div>

## Steps

### Set Up in the Admin

Before shipping, turn on the service in the system.

1. **Open the settings page**: Sign in to the CYBERBIZ admin, go to **Payment and Logistics > Convenience Store Logistics**, and click **FamilyMart Frozen Store-to-Store**.
2. **Accept the terms**: Read and agree to the "CYBERBIZ Logistics Integration Terms of Service" and "FamilyMart Contract Terms."
3. **Enter sender information**: Enter the **sender's real name and mobile number** correctly, because if a package is returned, store staff check ID before releasing it.
4. **Set fees and payment**: Enter the shipping fee and free shipping threshold, and turn on "Cash on Delivery" (only for merchants with CYBERBIZ PAYMENTS) or "Pickup Without Payment" as needed.

![Frozen store-to-store settings](../../../assets/images/ec-金物流-超商物流-全家冷凍店到店設定.en.gif){ title="Frozen Store-to-Store Settings" }

---

### Ship Orders

1. **Select orders**: Go to **Orders > All Orders** and select the frozen orders to process.
2. **Get tracking numbers and download shipping labels**: Click **Select Action** in the upper-right corner and, based on package size, select **Download FamilyMart Frozen S60 / S105 Shipping Labels**.
    - **s60**: Each side ≤ 45 cm, total weight ≤ 5 kg.
    - **s105**: Each side ≤ 45 cm, total weight ≤ 10 kg.
3. **Update the status**: When you download the shipping labels, the order delivery status changes to **Shipped**, and the customer is notified.


## Exceptions and Special Cases

- **Store closure**: If the pickup store closes, contact the shopper within **6 days** of the notice and choose a new store in the admin.
- **Unclaimed packages**: If the shopper doesn't pick up within 4 days, the package goes back to the original sender store. Pick it up within **4 days** at no extra shipping cost. If you don't pick it up after 4 days, it goes back to the logistics center and is sent to your address by **home delivery, freight collect**.
- **Prohibited items**: Cash, securities, fragile items, electronics (computers, phones, and so on), live animals and plants, or products worth more than NT$5,000.
- **Shipping exceptions**: For shipping exceptions, first [check the package status on the convenience store site :lucide-external-link:](https://fmec.famiport.com.tw/FP_Entrance/QueryBox). If you still have questions, ask through the customer service system in the CYBERBIZ admin.  

!!! info "**Important:** The **maximum compensation for a lost or damaged frozen store-to-store package is NT$5,000**."

### Reprint Shipping Labels { #operate-cvs-b2c-shipping-reprint }

If a label is lost or damaged, you can reprint it in the admin within the deadline.

1. In the order list, select the orders to reprint.
2. Open the **More Actions** drop-down and select **Reprint Shipping Label**.
3. The system downloads the PDF with the same tracking number again. **Shipping isn't charged again**, and the order status doesn't change.

<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Expiration by Convenience Store__](../references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See the reprint deadline and expiration rules for each convenience store carrier.

- :lucide-refresh-cw:{ .lg }
  [__Get a New Tracking Number for an Expired Shipping Label__](../renew-waybill-after-expiration.md#operate-renew-waybill-after-expiration){ data-preview }
  When the original shipping label is voided or past its reprint deadline, get a new tracking number and download a new shipping label.

</div>

## FAQ

??? quote "What happens if the shopper doesn't pick up the package in time?"  
	- The package goes back to the original sender store. Pick it up within **4 days** at no extra shipping cost.  
	- If you don't pick it up after 4 days, the package goes back to the logistics center and is sent to your address by **home delivery, freight collect**.  
	- The shopper receives a system notification reminding them to pick up or about the return.

??? quote "Are there size or weight limits for frozen products?"  
	- **S60 size**: Each side ≤ 45 cm, total weight ≤ 5 kg.  
	- **S105 size**: Each side ≤ 45 cm, total weight ≤ 10 kg.  
	- Before shipping, make sure products are fully frozen and use a suitable box.

??? quote "What can I ship? Are there prohibited items?"  
	Only **frozen food**. Prohibited items include cash, securities, fragile items, electronics (computers, phones, and so on), live animals and plants, and products worth more than **NT$5,000** each.

??? quote "How do I choose a new pickup store?"  
	If the store closes or pickup isn't possible, sign in to the admin within **6 days** of the notice and choose a new store for pickup.

??? quote "What if there's a shipping exception with a tracking number?"  
	Use [FamilyMart FamiPort to check the package status](https://fmec.famiport.com.tw/FP_Entrance/QueryBox). If you still have problems, contact CYBERBIZ admin customer service.
