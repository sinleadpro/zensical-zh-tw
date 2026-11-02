---
title: "Conditionalized Collection Filter Conditions Reference"
description: "Explains what each filter condition (operator) in Conditionalized Collections means, for reference when you set up rules."
created: 2026-06-03 21:55
last_modified: 2026-07-02 10:07
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
  - ec/products/references/smart-collections-rule-columns/
tags:
  - "Product Management"
  - "Conditionalized Collections"
  - "Filter Conditions"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/smart-collections-rule-relations/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


This table explains what each filter condition (operator) in Conditionalized Collections means, for reference when you set up rules.
  
## Filter Conditions Reference { #smart-collections-rule-relations }

| Filter Condition | Meaning | Applicable Field Type | Example |
| :-- | :-- | :-- | :-- |
| Equals | The field value is exactly the same as what you enter | Text or numeric | Product vendor "Equals" CYBERBIZ |
| Contains | The field text contains the words you enter | Text | Product name "Contains" Summer |
| Does Not Contain | The field text does not contain the words you enter | Text | Product name "Does Not Contain" Lucky Bag |
| Begins With | The field text begins with the words you enter | Text | Product name "Begins With" 2024 |
| Ends With | The field text ends with the words you enter | Text | Variant name "Ends With" L |
| Greater Than | The value is greater than the number you enter | Numeric | Product price "Greater Than" 1000 |
| Less Than | The value is less than the number you enter | Numeric | Inventory quantity "Less Than" 10 |

!!! note "Notes"
    * "Greater Than" and "Less Than" appear only when you select a numeric field (product price, list price, or inventory quantity). Enter a number as the value to match.
    * Text field matching ignores formatting differences other than letter case. Enter words that match your product data.
    * To see which fields are text and which are numeric, see the [Filter Fields Reference](smart-collections-rule-columns.md){ title="Conditionalized Collection Filter Fields Reference" }.
