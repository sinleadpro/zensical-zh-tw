---
title: "Set the Print Sort Order for Shipping Documents"
description: "In Checkout Page and Shipping Settings, choose whether batch-printed shipping documents are sorted by document type or by order number."
created: 2026-09-17 16:50
last_modified: 2026-09-23 14:20
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
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 設定出貨文件列印排序
features:
  - 列印出貨文件排序設定
prerequisites: []
related:
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/orders/tcat-quick-store/tcat-quick-store-shipping/
tags:
  - "Shipping documents"
  - "Print sort order"
  - "Black Cat"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 列印出貨文件排序設定
paths:
  - 金物流 > 結帳頁 & 物流設定
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/setup-shipping-docs-sort/"
comments: false
search:
  exclude: false
icon: lucide/list-ordered
hide: []
---

![Print sort order for shipping documents](../../../assets/images/EC-後台-金物流-結帳頁物流設定-列印出貨文件排序01.en.png){ title="Print sort order for shipping documents" .hero-page }

## About Shipping Document Print Sort Order { #intro-docs-sort }

When you batch-print multiple orders, the page order in the PDF affects how the pick station splits work and whether packers can get every sheet for one order together. Choose a sort order that matches your floor process, then print shipping documents from the order list.

- **Supported carriers**: Only for **Black Cat home delivery** and **Black Cat express to store** connected directly with CYBERBIZ.


### Choose a Print Mode { #operate-docs-sort-print-mode }

=== "By document type (default)"

    - **Sort order**: Print all pick lists first, then waybills, then packing slips, then order details.

    - **Best for**: Batch or assembly-line work where the same document type can be stacked and handled together.

    - **Print example**:

        - Step 1: Pick list`訂單 A` > Pick list`訂單 B` > Pick list`訂單 C` > Pick list`訂單 D`
        - Step 2: Waybill`訂單 A` > Waybill`訂單 B` > Waybill`訂單 C` > Waybill`訂單 D`
        - Step 3: Packing slip`訂單 A` > Packing slip`訂單 B` > Packing slip`訂單 C` > Packing slip`訂單 D`
        - Step 4: Order details`訂單 A` > Order details`訂單 B` > Order details`訂單 C` > Order details`訂單 D`

=== "By order number"

    - **Sort order**: Group by order number. Print every selected document for one order in a row, then move to the next order. Within one order the default order is: pick list -> waybill -> packing slip -> order details.

    - **Best for**: Packing one order at a time without manual sorting—every sheet for that order arrives together.

    - **Print example**:

        - Step 1: Pick list`訂單 A` -> Waybill`訂單 A` -> Packing slip`訂單 A` -> Order details`訂單 A`
        - Step 2: Pick list`訂單 B` -> Waybill`訂單 B` -> Packing slip`訂單 B` -> Order details`訂單 B`
        - Step 3: Pick list`訂單 C` -> Waybill`訂單 C` -> Packing slip`訂單 C` -> Order details`訂單 C`
        - Step 4: Pick list`訂單 D` -> Waybill`訂單 D` -> Packing slip`訂單 D` -> Order details`訂單 D`






## Steps { #operate-docs-sort }

1. Sign in to the CYBERBIZ admin and go to **Payment and Logistics > Checkout Page & Logistics**.
2. Expand **Print sort order for shipping documents**.
3. Choose a sort order. The next time you run **Fulfill/Print Documents** from the order list, the PDF follows this order.




## Next Steps { #next-steps-docs-sort }

For the actual ship and print steps, see:

<div class="grid cards" markdown>

- :lucide-cat:{ .lg }  
  [__Ship with Black Cat home delivery__](../home-delivery/tcat-home-delivery-v2.md){ title="Ship with Black Cat home delivery" }  
  Ship, print, or download home-delivery shipping documents from the order list.

- :lucide-truck:{ .lg }  
  [__Ship with Black Cat express to store__](../tcat-quick-store/tcat-quick-store-shipping.md){ title="Ship with Black Cat express to store" }  
  Ship, print, or download express-to-store shipping documents from the order list.

</div>

