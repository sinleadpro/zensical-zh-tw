---
title: "Receipt Orders"
description: "Before goods arrive at the warehouse, create a receipt order in the admin panel. Enter the exact items, quantities, and expiry dates to be received, and notify the warehouse staff."
created: 2026-03-16 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 進倉單
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 建立實體進貨預約
  - 下載進倉標籤
  - 追蹤入庫進度
features:
  - 進倉單管理
  - 批次匯入
  - 箱外明細下載
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 商品主檔需先建立完成
  - 若需指定效期，商品需先設定原始效期
related:
  - wms/merchant-inbound-operation-rules/
tags:
  - "Inbound Management"
  - "Label Printing"
  - "Receipt Status"
acoiv: activate
apis: []
devices:
  - desktop
ui_components:
  - 進倉單列表頁面
  - 進倉單編輯頁面
  - 商品明細分頁
paths:
  - 進倉單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5739
  - https://www.cyberbiz.io/support/?p=4750
  - https://www.cyberbiz.io/support/?p=4781
  - https://www.cyberbiz.io/support/?p=4799
  - https://www.cyberbiz.io/support/?p=4814
  - https://www.cyberbiz.io/support/?p=9088
permalink: "https://help.cyberbiz.io/wms/inbound-orders/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Receipt Orders
Before goods arrive at the warehouse, create a receipt order in the admin panel. Enter the exact items, quantities, and expiry dates to be received, and notify the warehouse staff.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-進倉單-畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-inbound-orders }

- **Booking limits**: You can only create receipt orders for **today** or a **future date**.
- **Rush fee**: If the arrival date is **today**, the warehouse charges a **rush handling fee**. We recommend booking 3–5 days ahead.
- **Receiving cutoff**: The warehouse stops receiving at **15:00** every day. Goods that arrive between 15:00 and 16:00 are still received, but inspection and shelving are scheduled later based on the workload on site.


## Receipt Order Process { #operate-inbound-orders-process }

1. **Create the receipt order**: Add the inbound details in the admin panel. The system creates an order waiting for confirmation.
2. **Goods arrive**: The goods reach the warehouse on the booked date, and warehouse staff sign for them.
3. **Inspection and shelving**: Warehouse staff count the items and check expiry dates, and then shelve them in the system.
4. **Closed**: The system updates the receipt order status, and online store stock increases accordingly.


## Add a Receipt Order { #operate-inbound-orders-create }

Create a single receipt order manually, or import many at once with Excel.

=== "Add Manually"

    Log in to the e-commerce warehouse admin panel, go to **Receipt Orders**, and click **Add Receipt** in the upper-right corner.

    1. **Basic settings**:
        - **Arrival date (required)**: Enter the date the goods are expected at the warehouse.
        - **Warehouse zone**: **Zone G (normal)** is selected by default. If you select **Zone L (locked)**, the goods cannot be shipped after they are received.
        - **Reference number (optional)**: Enter the supplier's shipping document number to make reconciliation easier.
        - **Note (optional)**: Record special requests or receiving instructions.
    2. **Select Product**:
        - Click to add products, and select the items and quantities in this delivery.
        - If expiry management is turned on for a product, be sure to specify the expiry date here. The warehouse inspects against this date.
    3. **Save and submit**: Check the details and click Save. The system creates a receipt order with a **Receipt Status** of **Pending Confirmation**.

=== "Batch Import"

    Log in to the e-commerce warehouse admin panel, go to **Receipt Orders**, and click **Import** in the upper-right corner.

    1. Click **Download Template**.
    2. Fill in the inbound data following the Excel column rules. Make sure SKUs and quantities are correct.
    3. Select the warehouse zone, upload the file, and click Import.

![](../assets/images/WMS-後台-進倉單-建立進倉單01.en.png){ .screenshot }

## Manage the Receipt Order List { #operate-inbound-orders-list }

### Filters { #operate-inbound-orders-filter }

Use filters to quickly find shipments at a specific stage or of a specific type among many orders. This helps with financial checks and warehouse scheduling.

- **Receipt order number**: Enter the full number to see the inspection details and receiving status of a specific shipment.
- **Search Range**: Filter by **Created Date** to pull orders for weekly or monthly reports and check how often and how much you receive in each period.
- **Receipt Status**: Filter orders that are **Pending Confirmation**, **Counting**, or **Done** to track overdue or not-yet-received shipments.
- **Receipt Type**: Separate orders by type, such as **standard inbound**, **transfer inbound**, or **return inbound**, to speed up checks for each business.
- **Warehouse zone**: If your store uses several zones, switch to a specific zone to see its receiving activity.

### Track Receipt Order Status { #operate-inbound-orders-track }

Monitor receiving progress and take the matching actions.

| Status | Description | Available Actions |
| :--- | :--- | :--- |
| **Pending Confirmation** | You submitted the request and it is waiting for the warehouse to accept it | Edit, delete, download documents |
| **Cancelled** | The warehouse rejected the receipt (for example, because of wrong information) | Edit and resubmit, delete |
| **Received** | The warehouse signed for the goods and is waiting to inspect them | Download documents (cannot edit or delete) |
| **Counting** | Warehouse staff are counting, inspecting, and shelving the goods | Download documents (cannot edit or delete) |
| **Done** | All goods were inspected and received, and stock is synced | Download documents, view history |

### Export Receipt Orders { #operate-inbound-orders-export }

Click **Export** in the upper-right corner to download the report.

## Manage the Receipt Order Details Page { #operate-inbound-orders-detail }

Click a receipt order number to open its details page for more actions.

![](../assets/images/WMS-後台-進倉單-進倉單明細頁01.en.png){ .screenshot }

### Delete or Edit a Receipt Order { #operate-inbound-orders-edit }

Click **Delete Receipt** or **Edit Receipt** in the upper-right corner.

### Download and Print Receipt Documents { #operate-inbound-orders-download }

1. In the list, click the **receipt order number**.
2. Click **Download Options** and choose a file type.
    - **Download Box Detail**
    - **Download Receipt Detail**
    - **Download History Record**

> After you create a receipt order, you must send the **box detail** sheet with the goods so the warehouse can identify them and inspect them faster. For the full process, see [Merchant Inbound Rules](merchant-inbound-operation-rules/#specs-inbound-rules-label).

### View Receipt Order Information { #overview-inbound-orders-info }

1. **Receipt Product List**: Compare declared and received quantities in real time, and check product expiry dates and batch numbers.

2. **Receipt History Record**: Track partial deliveries and quickly spot missing or lost (outstanding) items.


## Exception Handling { #specs-inbound-orders-exceptions }

If the quantity received does not match the order, the system handles it as follows:

### Case A: Short Delivery or Wrong Expiry { #specs-inbound-orders-shortage }

- **Definition**: Quantity received < quantity expected
- **What the system does**: It creates a **follow-up order** automatically (with the suffix -1, for example R_54-1) and emails the account that submitted the request.
- **What to do next**: To send the rest, book again with this order. If you will not send more, delete the order manually.

### Case B: Over Delivery { #specs-inbound-orders-overage }

- **Definition**: Quantity received > quantity expected
- **What the system does**: No order is created automatically. Warehouse staff contact you to agree on how to handle it, adjust it manually, and then complete the receipt.
