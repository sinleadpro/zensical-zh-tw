---
title: "Get a New Tracking Number for an Expired Convenience Store Shipping Label"
description: "When a convenience store shipping label expires and has no delivery record, get a new tracking number and download a new shipping label."
created: 2026-08-26 15:42
last_modified: 2026-10-07 16:30
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules:
  - 訂單
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents: 
  - 重新取得超商託運單
  - 處理逾期託運單
  - 處理部分出貨託運單
features: 
  - 超商託運單
  - 逾期重新取號
  - B2C_大宗寄倉
  - C2C_店到店
  - 部分出貨
prerequisites: 
  - 原託運單已完成取號並操作出貨
  - 原託運單已逾期且沒有配送記錄
related:
  - ec/orders/cvs-shipping/cvs-b2c-bulk-shipping/
  - ec/orders/cvs-shipping/cvs-c2c-shipping/
  - ec/payments-and-logistics/setup-family-mart-frozen-b2c/
  - ec/orders/cvs-shipping/family-mart-frozen-c2c/
  - ec/orders/cvs-shipping/cvs-partial-shipment/
  - ec/orders/references/cvs-waybill-expiration-reference/
tags: 
  - "Convenience Store Shipping Labels"
  - "New Tracking Number"
  - "Expired Shipping Labels"
acoiv: operation
apis: []
devices: []
ui_components: []
paths: 
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/renew-waybill-after-expiration/"
comments: false
search:
  exclude: false
icon: lucide/refresh-cw
hide: []
---

## Before You Start { #prerequisites-renew-waybill-after-expiration }

- **Use case**: The original shipping label is past its shipping (reprint) deadline and can't be used for drop-off, so you need a new shipping label.

- **Supported logistics**:
    - [Convenience Store B2C Bulk Shipping](cvs-shipping/cvs-b2c-bulk-shipping/)
    - [Convenience Store C2C Store-to-Store](cvs-shipping/cvs-c2c-shipping/)
    - [FamilyMart Frozen B2C Bulk Shipping](../payments-and-logistics/setup-family-mart-frozen-b2c/)
    - [FamilyMart Frozen C2C Store-to-Store](cvs-shipping/family-mart-frozen-c2c/)

    > EZCAT Quick Store Delivery doesn't support this feature.

- **Order delivery status**: Applies only to **Shipped** or **[Partially Shipped](cvs-shipping/cvs-partial-shipment.md)** orders.

    > For partially shipped convenience store orders, the convenience store shipping label also supports getting a new tracking number after it expires.

- **Shipping label status**: The original shipping label must be expired and have no delivery record.

    !!! tip "How the System Decides"
        - The shipping label hasn't expired: Use **Reprint Shipping Label** within the deadline to get the original shipping label.
        - The shipping label has expired and has no delivery record: Use **Get New Tracking Number and Download New Shipping Label** to get a new shipping label.
        - The shipping label has a delivery record: If **the convenience store has reported a logistics status**, you can't get a new tracking number. Guide the shopper to place a new order.

            > For example, when FamilyMart cold chain logistics shows **Reserved Slot Canceled**, the shipping label has a delivery record, and you can't get a new tracking number.



## Steps { #operate-renew-waybill-after-expiration }

1. Sign in to the CYBERBIZ admin and go to **Orders > All Orders**.
2. Select the orders, and then select **Get New Tracking Number and Download New Shipping Label**.
3. The system gets a new tracking number. Download the new shipping label and drop off the package following the original convenience store logistics process.

![](../../assets/images/EC-後台-訂單-所有訂單-託運單重新取號01.en.png)

!!! warning "Check the Delivery Record Before Getting a New Tracking Number"
    If the original shipping label has a delivery record, don't get a new tracking number. Check the actual shipping status first, and then get a new tracking number.


<div class="grid cards" markdown>

- :lucide-calendar-search:{ .lg }
  [__Check Shipping Label Expiration by Convenience Store__](references/cvs-waybill-expiration-reference.md#reference-cvs-waybill-expiration){ data-preview }
  See the reprint deadline and expiration rules for each convenience store carrier.

</div>