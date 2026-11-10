---
title: "Fulfillment Method Reference"
description: "Compares product fulfillment methods: the differences and requirements of self-shipment, third-party warehousing, and cross-border logistics."
created: 2026-06-05 13:47
last_modified: 2026-07-15 11:12
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans:
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - "Product Management"
  - "Fulfillment Method"
  - "Warehouse Management"
  - "Logistics Warehouse"
  - SKU
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/product-warehouse/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

The fulfillment method decides who stores and ships a product. By default, every product uses **Self-Shipment**. Matching logistics warehouse options appear only if you have enabled third-party warehousing or cross-border logistics.

### Fulfillment Method Reference { #reference-product-warehouse }

| Fulfillment Method | Description | Requirements |
| :-- | :-- | :-- |
| Self-Shipment | You pack and ship the product yourself. Inventory and shipping are managed manually in the admin. |  |
| Warehouse / Cross-Border Logistics Warehouse | A third-party warehouse or cross-border logistics provider stores and ships the product. After an order is placed, it is pushed to the warehouse automatically based on your settings. | The matching logistics warehouse feature must be enabled |

!!! note "Notes"
    * The warehouses available in the **Warehouse** dropdown **change based on the logistics features you have activated**, so different stores see different options.
    * For products shipped from a third-party warehouse, the product **SKU must match the SKU in that warehouse** for the order to be pushed successfully.
    * If you have no warehousing feature, every product uses Self-Shipment.
