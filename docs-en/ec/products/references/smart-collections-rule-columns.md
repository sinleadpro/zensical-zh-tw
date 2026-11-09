---
title: "Conditionalized Collection Filter Fields Reference"
description: "A list of the filter fields available in Conditionalized Collections and the match conditions each one supports, for reference when you set up conditionalized collections."
created: 2026-06-03 21:50
last_modified: 2026-07-02 10:06
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
related:
  - ec/products/references/smart-collections-rule-relations/
tags:
  - "Product Management"
  - "Conditionalized Collections"
  - "Filter Fields"
  - "Product Tags"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/smart-collections-rule-columns/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


This table lists the filter fields available in Conditionalized Collections and the match conditions each field supports, for reference when you set up conditionalized collections.

## Filter Fields Reference { #reference-smart-collections-columns }

| Filter Field | Product Data Matched | Field Type | Supported Conditions |
| :-- | :-- | :-- | :-- |
| Product Name | The product's name | Text | Equals, Begins With, Ends With, Contains, Does Not Contain |
| Product Type | The product's "Product Type" field | Text | Equals, Begins With, Ends With, Contains, Does Not Contain |
| Product Vendor | The product's "Vendor" field | Text | Equals, Begins With, Ends With, Contains, Does Not Contain |
| Variant Name | The name of the product variant (option) | Text | Equals, Begins With, Ends With, Contains, Does Not Contain |
| Product Tag | The tags set on the product | Text | Equals, Begins With, Ends With, Contains, Does Not Contain |
| Product Price | The product's selling price | Numeric | Equals, Greater Than, Less Than |
| List Price | The product's original price (strikethrough price) | Numeric | Equals, Greater Than, Less Than |
| Inventory Quantity | The product's current inventory quantity | Numeric | Equals, Greater Than, Less Than |

!!! note "Notes"
    * **Text fields** (product name, product type, product vendor, variant name, and product tag) can use text conditions (Equals, Begins With, Ends With, Contains, Does Not Contain).
    * **Numeric fields** (product price, list price, and inventory quantity) can only use numeric conditions (Equals, Greater Than, Less Than). Enter a number as the value to match.
    * For the detailed meaning of each condition, see the [Filter Conditions Reference](smart-collections-rule-relations.md){ title="Conditionalized Collection Filter Conditions Reference" }.
