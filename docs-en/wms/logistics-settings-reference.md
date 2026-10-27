---
title: "Home Delivery Settings by Warehouse Integration Mode"
description: "The home delivery settings for warehouse shipping and merchant self-shipping are in different places for each warehouse integration mode. This table lists where to find the settings in each case so you can set them up quickly."
created: 2026-07-13 12:00
last_modified: 2026-07-13 12:00
lang: en-US
type: reference
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
modules:
  - 電商倉儲
  - 金物流
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents: 
features:
  - 電商倉儲
  - 建立物流選項
prerequisites: []
related:
  - wms/application-process-and-activation/
  - wms/enable-partial-warehouse-integration-and-mixed-orders/
  - wms/enable-partial-warehouse-integration-and-order-splitting/
tags:
  - WMS
acoiv: activate
apis: []
devices:
  - desktop
ui_components:
  - 自訂物流頁籤
  - 串接物流頁籤
paths:
  - 金物流 > 宅配物流
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/logistics-settings-reference/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---
# Home Delivery Settings by Warehouse Integration Mode
The home delivery settings for warehouse shipping and merchant self-shipping are in different places for each warehouse integration mode. This table lists where to find the settings in each case so you can set them up quickly.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## Where to Find Each Setting { #overview-logistics }

Go to **Payment and Logistics > Delivery Settings**, and then create the shipping options on the tab that matches the shipper and payment method:

| Shipper | Payment Method | Full Integration | Partial Integration |
| :--- | :--- | :--- | :--- |
| **Warehouse shipping** | Cash on delivery | Custom Logistics tab | Custom Logistics tab |
| | No payment on delivery | Custom Logistics tab | Custom Logistics tab |
| **Merchant self-shipping** | Cash on delivery | - | **Connect Logistics tab** |
|  | No payment on delivery | - | Custom Logistics tab |

## Key Differences { #specs-logistics }

- **Full integration**: The warehouse ships all products, so you only need to set up the warehouse shipping options under **Custom Logistics**.
- **Partial integration**:
    - **Warehouse-shipped items**: Set them all up on the **Custom Logistics** tab.
    - **Self-shipped items**: If they support **cash on delivery**, set them up on the **Connect Logistics** tab. If they use **no payment on delivery**, keep them on the **Custom Logistics** tab.

## References { #reference-logistics }

- [Warehouse Integration Application and Activation](application-process-and-activation.md)
- [Enable Partial Warehouse Integration and Mixed Orders](enable-partial-warehouse-integration-and-mixed-orders.md)
- [Enable Partial Warehouse Integration and Order Splitting](enable-partial-warehouse-integration-and-order-splitting.md)