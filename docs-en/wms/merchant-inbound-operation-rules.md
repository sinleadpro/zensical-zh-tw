---
title: "Merchant Inbound Rules"
description: "The standard process and rules for bringing merchant goods into the CYBERBIZ e-commerce warehouse, including inbound appointments, acceptance standards, packaging and barcode specifications, and on-site safety rules."
created: 2026-03-16 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：建立進倉單、進倉條碼
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
  - 建立進倉預約
  - 確認包裝規範
  - 處理進倉異常
features:
  - 進倉管理
  - 驗收作業
  - 條碼規格控制
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 進倉前須建立系統進倉單
related:
  - wms/inbound-orders/
tags:
  - "Acceptance Standards"
  - "Packaging Requirements"
  - "Warehouse Logistics"
acoiv: activate
apis: []
devices:
  - desktop
ui_components:
  - 進倉管理頁面
  - 進倉單明細
paths:
  - 進倉單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5730
  - https://www.cyberbiz.io/support/?p=8770
permalink: "https://help.cyberbiz.io/wms/merchant-inbound-operation-rules/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Merchant Inbound Rules
The standard process and rules for bringing merchant goods into the CYBERBIZ e-commerce warehouse, including inbound appointments, acceptance standards, packaging and barcode specifications, and on-site safety rules.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

## Inbound Appointment Process { #operate-inbound-rules-reservation }

Before any goods are received, you must [create a receipt order](inbound-orders.md) in the WMS admin panel and notify the warehouse ahead of time based on the volume.

### 1. Notice Requirements { #specs-inbound-rules-notice }

| Inbound Type | Notice Required | Description |
| :--- | :--- | :--- |
| **Standard inbound** | 3–5 business days before arrival |  |
| **Rush inbound** | 2 business days before arrival | A rush inspection fee applies |
| **Bulk inbound** (≥300 pallets) | 3 months before arrival | Scheduling must be planned in advance |

!!! info "Inbound Notice Rules"
    - **What to include**: Receipt order number, items, quantities, expiry dates, number of pallets, and number of boxes
    - **How to notify**: Book through the channel's **LINE group** or by email (`honeycomb-admin@cyberbiz.com.tw`).


### 2. Receiving Hours { #specs-inbound-rules-time }

- **Service hours**: Monday to Friday, 09:00–12:00 and 13:00–16:00 (closed on national holidays).
- **Cutoff**: Before 15:00 every day.
    - Goods that arrive between 15:00 and 16:00 are only stored temporarily, and inspection is rescheduled.



### 3. Special Cases { #specs-inbound-rules-special }

1. **Container deliveries**

    For container deliveries, the CYBERBIZ e-commerce warehouse takes these photos as standard practice, so the handover of goods is clear:

    - **Arrival check**: A full view of the unopened container doors (including the license plate) and the intact container seal (including the seal number list).
    - **Unloading**: The inside of the container right after opening, and records of the unloading process.
    - **Completion**: A photo of the empty container after unloading.


2. **No receipt order in the system on arrival day**

    If goods arrive before a receipt order exists in the system, these rules apply:

    - **First step**: Create the receipt order in the system right away. The warehouse can only inspect and receive the goods after that.
    - **Receiving time**: Inspection depends on the staff and schedule available on site. Same-day receiving is not guaranteed.
    - **Rush handling**: If you need priority inspection, a **rush inspection fee** applies.

## Packaging and Pallet Rules { #specs-inbound-rules-packaging }

### 1. Boxing { #specs-inbound-rules-box }

- **Partial boxes**: Put boxes that are not full on top of the pallet and seal them with **tape of a different color**. Never mix them in between other boxes on the pallet.
- **Load protection**: Outer boxes must be able to bear the weight of their contents. Damaged boxes are opened on site to check the products.

### 2. Product Labels { #specs-inbound-rules-label }

- **Documents with the goods**: Print the **receipt order details** and the **receipt order box details** from the WMS admin panel, and put them in one of the boxes that comes with the delivery.
- **Outer box labels**:
    - **Required labels**: Every outer box must have the **receipt order box details** and an **outer box label** firmly attached.
    - **Label position**: Labels must face outward. Do not let them face inward, overlap, or be covered, so staff can scan them without moving the boxes.
    - **Stacking**: Do not mix boxes of different sizes on the same side. Sort and stack them neatly by size.
    - **Templates and references**:
        - **Receipt order box details**: [Download the receipt order box details](inbound-orders/#operate-inbound-orders-download) from the admin panel.
        - **Outer box label**: Use the template below to make and print it.
            ![](../assets/images/WMS-外箱標籤範本01.en.png){ .screenshot }
    - **Label placement example**
        ![](../assets/images/WMS-外箱黏貼範例01.en.png){ .screenshot }
- **Barcode and label specifications**:
    - **Format**: Must use Code 128
    - **Length**: No more than 17 characters
    - **Print**: Black on white, for high scanning contrast
    - **Minimum size**: At least 4 cm × 2 cm
    - **Barcode density**: Each character must be at least 0.537 mm wide

**If barcodes do not meet these specifications, the CYBERBIZ e-commerce warehouse applies barcode labels for you at an extra charge.**



### 3. Pallet Stacking { #specs-inbound-rules-pallet }

- **Standard size**: Use standard 110 cm × 110 cm pallets.
- **Stacking limits**:
    - Height: No more than 150 cm (including the pallet).
    - Weight: No more than 800 kg per pallet.
    - Footprint: Nothing may stick out past the pallet edges.
- **Protection**:
    - Wrap the load securely with shrink film so it does not tip over in transit.
    - Use enough layers of wrap to hold the total weight, so the load does not lean when moved.
    - Keep space between pallets, so the shrink film does not stick together and tear.
- **Pallet exchange**:
    - Pallets are exchanged one for one at delivery. The warehouse may refuse to exchange damaged pallets.
    - If pallets cannot be exchanged on the spot, a pallet loan form is issued, and you must return the same number within three business days.

## Inbound Inspection and Exceptions { #operate-inbound-rules-receiving }

### 1. Acceptance Standards { #specs-inbound-rules-standard }

To keep receiving efficient and stock accurate, the warehouse inspects goods by these standards:

- **Default storage and counting**:
    - **Storage**: If you do not specify how goods should be stored, the CYBERBIZ e-commerce warehouse assigns storage based on available space.
    - **Counting**: By default, staff **spot-check** one item, one original box, and one piece.
        - If shortages or damage are found when boxes are opened during later picking, you are notified by email for follow-up.
    - **Fees**: Boxes with mixed products are charged a separate inspection fee.
- **What is checked**: Items, quantities, and expiry dates are counted against the receipt order in the system.
- **Receiving**: After inspection, the warehouse attaches a **product receiving label** and shelves the goods.
- **Special requirements**: If your products need special inspection standards, send the SOP before the delivery. Otherwise, the warehouse's standard process applies.


### 2. Exception Handling { #specs-inbound-rules-exception }

If inspection finds wrong quantities, wrong expiry dates, damaged boxes, or problems with the contents, this process starts:

1. **Report**: The warehouse photographs the problem and notifies you right away.
2. **Reply deadline**: To avoid delaying other receiving, you must reply with instructions **within 2 hours**.
3. **No reply**: If no reply arrives in time, the warehouse handles it under its **standard exception rules**.


## On-Site Operations and Safety Rules { #operate-inbound-rules-entry }

Everyone on site must follow the safety and operating rules. The warehouse may refuse deliveries from anyone who does not.

### 1. Vehicles and Unloading { #operate-inbound-rules-vehicle }

- **Vehicles**: Use vehicles with a tail lift or that can unload directly at the dock.
- **Unloading help**: If you need a forklift, notify the warehouse in advance or rent one from the warehouse area supervisor.
- **Sorting**: Goods must be **sorted and palletized before arrival**. Large-scale re-sorting on site is not allowed, because it delays other merchants' deliveries.

### 2. On-Site Safety { #specs-inbound-rules-safety }

- **Driving**: Keep speed under **20 km/h**. Turn off the engine as soon as the vehicle is parked at the dock.
- **Clothing**: No bare feet, no bare upper body, and no open-toed shoes (such as sandals or slippers).
- **Prohibited**: No smoking (except in designated areas), no betel nut chewing, no alcohol, and no littering.
- **Conduct**: Do not give warehouse staff anything of value (such as cigarettes, drinks, or betel nuts).
- **Cleanliness**: Leave the area clean when your vehicle leaves. Do not leave mud or trash behind.

### 3. Sign-Off { #operate-inbound-rules-signoff }

After you deliver goods or collect returns, be sure to complete the sign-off with warehouse staff to protect your interests.
