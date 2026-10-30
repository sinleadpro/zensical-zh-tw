---
title: "Order Fulfillment Flow"
description: "Explains the order fulfillment flow: steps and rules for integrated logistics, custom logistics, bulk tracking number import, and item-by-item partial shipment."
last_modified: 2026-07-13 12:02
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify 宅配跟超取出貨流程
  - 篩選群組可以做出快結案訂單群組嗎
  - verify 批次出貨的確認條件步驟。
products:
  - EC
modules:
  - 訂單
sites: []
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
intents:
  - 執行單筆或批次訂單出貨
  - 下載並列印物流託運單與揀貨單
  - 了解宅配與超商取貨的交寄流程
  - 設定自訂物流與回填貨運單號
features:
  - 單筆出貨
  - 批次出貨
  - 託運單產出
  - 揀貨單與出貨明細
  - 自動呼叫司機 黑貓
  - 儲值中心
prerequisites:
  - 完成物流設定
  - 填寫公司物流地址
  - 確認儲值中心餘額充足_一般版
apis: []
devices:
  - desktop
  - mobile
paths: []
wp_url:
  - https://www.cyberbiz.io/support/?p=24829
  - https://www.cyberbiz.io/support/?p=952
permalink: "https://help.cyberbiz.io/ec/orders/basics/order-fulfillment-flow/"
comments: ""
search:
  exclude: false
icon: lucide/workflow
---

## About Order Fulfillment { #intro-fulfillment }

Shipping is the core step after an order is placed and payment is confirmed. In the order list, you can select orders and "generate shipping labels" and "update the delivery status" in one go, saving the time of handling orders one by one.

Depending on the delivery method, shipping falls into three main types:

- **Integrated logistics:** EZCAT, convenience store pickup, Pelican Express, HCT Logistics, SF Express, and more. The system gets tracking numbers from the carrier and generates shipping labels automatically.
- **Custom logistics:** You deliver yourself or ship with a partner carrier, mark orders as shipped manually, and enter the tracking number.
- **Warehouse shipping:** For orders connected to [Smart Warehouse (Fengchao)](../../../wms/){ title="hide:" }, the warehouse picks and ships.

Whether you select one order or many, the shipping entry in the new order list is the same. The only difference is how many orders you handle at once.

---

## Features Overview { #overview-fulfillment }

| Shipping Entry | Location | Purpose |
| :-- | :-- | :-- |
| Single / bulk shipping | "More Actions" in the order list | Select orders and a carrier, generate shipping labels, and change the delivery status to "Shipped" |
| Bulk import custom logistics tracking numbers | Tools above the order list | Import custom logistics tracking numbers in bulk with Excel |
| Item-by-item / partial shipping | "Shipping" section on the order details page | Ship in-stock items from an order first |

---

## Prerequisites and Limitations { #prerequisites-fulfillment }

Before you ship, check the following:

- [x] **CYBER Coin balance:** The system collects shipping fees for integrated logistics, so make sure your balance is sufficient before shipping[^billing].
- [x] **Sender address:** In the admin, under "Payment and Logistics" in the left menu, fill in the sender information on each carrier's shipping label settings page (such as EZCAT Shipping Label Settings or HCT Logistics Shipping Label Settings). Otherwise, the sender information on shipping labels will be incomplete.
- [x] **Printer and supplies:** We recommend a laser printer, with A4 paper and shipping label / convenience store label stickers ready, so barcodes are clear and readable.

[^billing]: On the Standard Plan, CYBER Coins are deducted when you download shipping labels. On plans with the Reconciliation Center (PLUS plans and Enterprise), fees are added to the statement and settled at the end of the billing period.

---

## Billing Rules { #pricing-fulfillment }

The system collects shipping fees for integrated logistics (EZCAT, convenience store pickup, Pelican Express, HCT Logistics, SF Express, and more). For custom logistics, you settle with the carrier yourself, outside the system.

In the shipping dialog, check the **"Shipping Rate Table"** for the rate for each package size. The actual amount depends on the package size you hand to the carrier, not a fixed amount.

- **Standard Plan:** CYBER Coins are deducted when you download shipping labels.
- **Plans with the Reconciliation Center:** Shipping fees are added to the statement and settled at the end of the billing period, not charged at shipping.


---

## Steps { #operate-fulfillment }

In the new order list, you ship by selecting orders in the list. **Select one order for single shipping or multiple orders for bulk shipping**; the process is the same.

!!! tip "Tip"
    For bulk shipping, select only orders with the **same delivery method** at a time (for example, all EZCAT or all 7-Eleven) so the system can ship the whole batch with one action.

### Ship with Integrated Logistics { #operate-fulfillment-carrier }

Integrated logistics gets tracking numbers from the carrier and generates shipping labels automatically. The following uses EZCAT as an example; other carriers (convenience stores, Pelican Express, HCT Logistics, SF Express, and more) work much the same way:

1. **Open the order list:** In the admin, go to "Orders" > "All Orders."
2. **Select orders:** Select the orders to ship in the list.
3. **Choose a shipping action:** Click **"More Actions"** at the top and select **"Download EZCAT shipping labels and change status to 'Shipped'"**.
4. **Confirm the shipping rate:** In the dialog, select the shipping fee standard (you can check the **"Shipping Rate Table"**), then click confirm to download.
5. **Download and print shipping labels:** The system generates a **shipping label archive (ZIP)** in the background and downloads it automatically, and the batch's delivery status changes to "Shipped." Unzip it to print the shipping labels and details (see [Shipping Label Archive Contents](#operate-fulfillment-zip)).

<div class="grid cards" markdown>

- :lucide-cat: [**EZCAT Home Delivery**](../home-delivery/tcat-home-delivery-v2.md){ title="Ship with EZCAT Home Delivery" }
- :lucide-bird: [**Pelican Express**](../home-delivery/pelican-shipping-v2.md){ title="Ship with Pelican Express" }
- :lucide-truck: [**HCT Logistics**](../home-delivery/hct-shipping-v2.md){ title="Ship with HCT Logistics" }
- :lucide-box: [**SF Express**](../home-delivery/sf-express-shipping-v2.md){ title="Ship with SF Express" }

</div>

---

### Ship with Convenience Stores { #operate-fulfillment-cvs }

Convenience store pickup is integrated logistics, and the process is the same as [shipping with integrated logistics](#operate-fulfillment-carrier): select orders > "More Actions" > choose the matching convenience store shipping action > the system generates a shipping label archive and changes the delivery status to "Shipped."

<div class="grid cards" markdown>

- :lucide-store: [**Convenience Store C2C Shipping Guide**](../cvs-shipping/cvs-c2c-shipping.md){ title="Ship with Convenience Store C2C Store-to-Store" }
- :lucide-factory: [**B2C Bulk Shipping**](../cvs-shipping/cvs-b2c-bulk-shipping.md){ title="Ship with Convenience Store B2C Bulk Shipping" }
- :lucide-snowflake: [**FamilyMart Frozen Store-to-Store**](../cvs-shipping/family-mart-frozen-c2c.md){ title="Ship with FamilyMart Frozen C2C Store-to-Store" }

</div>

!!! warning "Select One Convenience Store Type for Bulk Shipping"
    Convenience store B2C, C2C, and cold chain are different shipping actions. For bulk shipping, select only orders from **the same convenience store and the same type** at a time (for example, all "7-Eleven Pickup with Payment") so the system can ship the whole batch with one action.

---

### Ship with Custom Logistics { #operate-fulfillment-custom }

If you use logistics not integrated with the system (self-delivery or a partner carrier), mark orders as shipped with custom logistics:

1. **Select orders:** Select the orders to ship in the order list.
2. **Open the shipping dialog:** Click **"More Actions"** and select the custom logistics shipping option.
3. **Choose a carrier:** Select the carrier from the **"Select a carrier"** menu.
4. **Confirm shipping:** Optionally select **"Send email notification to customer."** After you confirm, the order's delivery status changes to "Shipped."

<div class="grid cards" markdown>

- :lucide-truck: [**Custom Logistics Shipping Guide**](../home-delivery/custom-logistic-shipping.md){ title="How to Ship with Custom Logistics" }

</div>

For large order volumes, use "Bulk Import Custom Logistics Tracking Numbers" below to import tracking numbers at once.

---

### Bulk Import Custom Logistics Tracking Numbers { #operate-fulfillment-import }

When you have many custom logistics orders, import tracking numbers at once with Excel:

1. **Open the import tool:** Above the order list, open **"Bulk Import Custom Logistics Tracking Numbers."**
2. **Download and fill in the template:** Download the Excel template and enter order numbers, tracking numbers, and carriers.
3. **Upload the file:** After upload, successfully imported orders change to "Shipped," and customers are notified by email[^import-partial].

<div class="grid cards" markdown>

- :lucide-file-spreadsheet: [**Bulk Import Custom Logistics Tracking Numbers Guide**](../home-delivery/custom-logistic-shipping.md#excel-bulk-import){ title="How to Ship with Custom Logistics" }

</div>

[^import-partial]: Bulk import supports shipping whole orders only, not partial shipment.

---

### Item-by-Item and Partial Shipping { #operate-fulfillment-partial }

To ship only the in-stock items from an order first, select items one by one in the "Shipping" section of the order details page instead of shipping in bulk from the list. For details, see [Partial Shipment](../home-delivery/partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }.

---

## Shipping Label Archive { #operate-fulfillment-zip }

Shipping labels for integrated logistics aren't a single PDF. The system generates them in the background and **packs them into an archive (ZIP) that downloads automatically**. The archive is named after the carrier (for example, `ezcat` for EZCAT, `seven` for 7-Eleven, and `family` for FamilyMart), so you get all the documents for a batch at once.

After unzipping, the archive usually contains:

| Document | Purpose |
| :-- | :-- |
| Shipping label | Logistics label / barcode stuck on the package |
| Packing slip | List of shipped items included with the package |
| Pick list | For picking and preparing items in the warehouse |
| Order details | Printable order details for the batch |


??? example "Archive Contents Example"
    ![Shipping label archive contents](../../../assets/images/ec-訂單-所有訂單-託運單壓縮檔內容.en.png){ title="Shipping Label Archive Contents" }

!!! info "Why an Archive?"
    Bulk shipping can cover many orders and documents at once, so the system packs them into a ZIP instead of downloading each one separately. Unzip it first, then print the shipping labels and details you need.

---

## Important Rules and Limitations { #specs-fulfillment }

- **Downloading marks orders as shipped:** As soon as you download integrated logistics shipping labels, the batch's delivery status changes to "Shipped." Make sure the items are ready first.
- **Stay on the page while downloading:** Closing or leaving the order page during the download interrupts it, and some orders may already be "Shipped" and need reprinting.
- **Reprint shipping labels:** For shipped orders, select **"Reprint Shipping Label"** in "More Actions" to download the shipping label PDF again.
- **Outlying island convenience stores and dangerous goods:** When delivering to convenience stores on outlying islands, follow the regulations on air transport of dangerous goods.

---

## Next Steps { #next-steps-fulfillment }

<div class="grid cards" markdown>

- :lucide-package-open:{ .lg }  
  [__Partial Shipment__](../home-delivery/partial-shipment-v2.md){ title="Set Up Partial Shipment for Orders" }  
  Ship in-stock items from an order first and the rest later.

</div>

---

## FAQ { #faq-fulfillment }

??? quote "Nothing happens / can't download shipping labels"
    [](){ #faq-fulfillment-download-failed }
    If the dialog shows "An error occurred and the PDF can't be generated" or nothing happens, check the following in order:

    - Make sure the browser isn't blocking pop-ups and downloads
    - Don't close or leave the order page during the download
    - Wait a moment and try again

??? quote "The download is an archive. What documents are in it?"
    [](){ #faq-fulfillment-zip-contents }
    Shipping labels for integrated logistics are packed into a ZIP archive with shipping labels, packing slips, pick lists, and order details. Unzip it first, then print the documents you need. See [Shipping Label Archive Contents](#operate-fulfillment-zip).

??? quote "How are shipping fees calculated? Where can I check them?"
    [](){ #faq-fulfillment-shipping-fee }
    The "Shipping Rate Table" in the shipping dialog lists the rate for each package size. The actual amount depends on the package size. On the Standard Plan, CYBER Coins are deducted immediately; on plans with the Reconciliation Center, fees are added to the statement.

??? quote "Can I print shipping labels again after downloading them?"
    [](){ #faq-fulfillment-redownload }
    Yes. Select "Reprint Shipping Label" in "More Actions" to download the order's shipping label PDF again.

??? quote "Can I reship an order if something goes wrong after shipping?"
    [](){ #faq-fulfillment-reship }
    No. If something goes wrong during delivery, except for **convenience store closures**, where you can change the pickup store (see the next question), the only option is to have the customer place a new order.

??? quote "What if the convenience store closes after shipping?"
    [](){ #faq-fulfillment-store-closed }
    It depends on the convenience store (see [Convenience Store C2C Store Closures](../cvs-shipping/cvs-c2c-shipping.md#operate-cvs-c2c-exception-store-closed){ title="Ship with Convenience Store C2C Store-to-Store" }).

??? quote "Can I combine multiple orders from the same customer into one shipment?"
    [](){ #faq-fulfillment-merge }
    It depends on whether you use Smart Warehouse (Fengchao):

    - **Connected to Smart Warehouse (Fengchao):** Combined shipping isn't supported.
    - **Not connected:** You can combine orders manually, **for paid home delivery orders only**.

    For example, with home delivery orders A and B from the same customer:

    1. **Order A** follows the normal home delivery shipping process. When picking, **put order B's items in the same package**.
    2. **Order B** is marked as shipped with **"Custom Logistics"** (nothing is actually sent; this just updates the order status to Shipped).

??? quote "How do I ship when the customer picks up the items themselves (no carrier)?"
    [](){ #faq-fulfillment-self-pickup }
    Use the **"Custom Logistics"** shipping process. You can enter anything in the tracking number field (the system doesn't track custom logistics). The **"Shipped"** delivery status is the final status, and the order is included in reconciliation. See [How to Ship with Custom Logistics](../home-delivery/custom-logistic-shipping.md){ title="How to Ship with Custom Logistics" }.

## References { #reference-fulfillment }

- [Delivery Status Reference](../references/fulfillment-statuses.md){ title="Delivery Status Reference" }
- [Convenience Store Partial Shipment Support](../references/cvs-partial-shipping-support.md){ title="Convenience Store Partial Shipment Support" }
