---
title: "Product Status Reference"
description: "Explains the three independent status groups (sell status, publish status, and product search) that decide whether a product can be seen, searched, and bought on the storefront."
created: 2026-06-05 13:40
last_modified: 2026-07-06 19:08
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
  - "Product Status"
  - "Listing Status"
  - "Publishing Status"
  - "Site Search"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/product-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---

Whether a product can be seen, searched, and bought on the storefront is decided by three independent status groups. The table below explains what each status means and where it applies.

### Product Listing and Publishing Status Reference { #reference-product-statuses }

| Status Group | Displayed Text | Description |
| :-- | :-- | :-- |
| Sell Status | Launched | The product is within its sales period (the listing time has passed and the delisting time has not), and it is sold normally on the storefront. |
| Sell Status | Unlisted | A **Sell From** time is set but has not arrived yet. The product is hidden on the storefront for now and is listed automatically when the time comes. |
| Sell Status | Off Market | The set **Sell To** time has passed, and the product is automatically delisted from the storefront. |
| Publish Status | Published | The product is displayed and sold normally on the storefront. |
| Publish Status | Unpublished | The product is hidden on the storefront and cannot be bought even through its link. This is often used for products that are temporarily off sale or still being prepared. |
| Product Search | Enable Search | Customers can find this product with site search. |
| Product Search | Exclude from Search Results | The product does not appear in site search results, but you can still share the product link so specific customers can buy it. Google search is not affected. |

!!! note "Notes"
    * **Sell Status** is calculated automatically from the Sell From and Sell To times. Leaving both empty means "list now and never delist."
    * **Sell Status** and **Publish Status** are independent. Even within the sales period, a product set to "Unpublished" does not appear on the storefront.
    * POS store products cannot be set to "Published". They are for in-store use only.
