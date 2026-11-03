---
title: "POS Product Analysis Reference"
description: "Field and metric definitions for the three POS product ranking reports, referenced from the main article."
created: 2026-06-23 15:40
last_modified: 2026-06-23 21:53
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans: []
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - POS
  - Product_Analysis
  - Reference
  - Product_Sales_Ranking
  - Product_Repurchase_Ranking
  - Product_Return_Ranking
  - Period_Product_Repurchase_Rate
  - Period_Product_Return_Rate
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/pos/business-intelligence/references/pos-product-metrics-reference/"
comments: false
search:
  exclude: false
icon: lucide/table
hide:
---

# POS Product Analysis Reference

This page brings together the field and metric reference tables for the three POS product ranking reports. It is referenced from the main article.

## Common Fields Reference { #reference-pos-product-common }

| Field | Description |
| :-- | :-- |
| Rank | The product's rank in this report. |
| SKU | The stock keeping unit (SKU) number of the product, used to uniquely identify the item. |
| Product Name | The name of the product. |
| Product Type | The category the product belongs to. |
| Vendor | The supplier of the product. |
| Product Price | The unit selling price of the product. |
| Product Sales Amount | The total sales amount of the product during the selected period. |
| Product Sales Quantity | The total quantity of the product sold during the selected period. |
| Shopper Count | The number of orders that included this product during the period. A higher number means more customers purchased it. |

!!! note "Notes"
    * The fields above are shown in all three reports (Product Sales Ranking, Product Repurchase Ranking, and Product Return Ranking).
    * All figures include only non-canceled orders. Canceled orders are deducted from revenue on the day they are canceled.

## Report-Specific Metrics Reference { #reference-pos-product-special }

| Report | Field | Description |
| :-- | :-- | :-- |
| Product Sales Ranking | Period Revenue Share | The percentage of the selected period's total revenue that comes from this product's sales. |
| Product Repurchase Ranking | Period Product Repurchase Rate | Customers who bought this product two or more times ÷ customers who bought this product. |
| Product Repurchase Ranking | Average Repurchase Count | The average number of times customers who bought this product during the period bought it again. A higher number indicates stronger customer loyalty. |
| Product Return Ranking | Period Product Return Count | The number of units of this product returned during the selected period. |
| Product Return Ranking | Period Product Return Rate | The percentage of this product's sales that were returned during the selected period. A higher rate means returns need closer attention. |

!!! note "Notes"
    * Fields that show percentages (Period Revenue Share, Period Product Repurchase Rate, and Period Product Return Rate) display a "%" sign in the reports.
    * The Product Sales Ranking sorts products by Product Sales Amount, from highest to lowest.
