---
title: "Product Analysis Fields Reference"
description: "Field and metric definitions for each section of Product Analysis, including sales ranking, repurchase frequency, products with no sales, and purchases by period."
created: 2026-06-15 00:00
last_modified: 2026-07-12 19:43
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
plans: []
plan_options: []
tags:
  - "Report Analysis"
  - "Product Analysis"
  - "Sales Ranking"
  - "Repurchase Rate"
  - "Repurchase Frequency"
  - "Field Reference"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/product-analysis-metrics-reference/"
icon: lucide/table
hide:
---

# Product Analysis Field Reference

This page explains the fields and metrics in each section of "Product Analysis" so that articles such as [Product Analysis](../product-analysis.md) can link to them.

### Product Sales TOP 10 / LAST 10 { #reference-product-analysis-sales-rank }

| Item | Description |
| :-- | :-- |
| Product Name | Product name (including variant). Long names are shortened with "…" in the chart; hover to see the full name |
| Sales | Total **quantity sold** (units) of the product in the query period |

!!! note "Note"
    * Only valid orders are counted (not canceled; no return needed or return rejected).
    * Add-on products are excluded.
    * TOP 10 is sorted from highest to lowest and LAST 10 from lowest to highest, 10 items each.

### Product Repurchase Frequency { #reference-product-analysis-repurchase }

| Field | Description |
| :-- | :-- |
| Product SKU | The product's stock-keeping number |
| Product Name | Product name (including variant) |
| Repurchase Count | Total times all customers bought this product again in the query period (each purchase by the same customer from the 2nd one on counts once) |
| Average Days Between Repurchases | Average number of days between two purchases of this product by a customer |

!!! note "Note"
    * Only products repurchased **10 or more times** are listed.
    * Sorted by "Average Days Between Repurchases" from shortest to longest. A shorter interval means more frequent repurchases.

### Products Updated in the Last 90 Days with No Sales in the Last 30 Days { #reference-product-analysis-no-sales }

| Field | Description |
| :-- | :-- |
| Product SKU | The product's stock-keeping number |
| Product Name | Product name (including variant) |
| Price | The product's current selling price |
| Updated Date | The date the product data was last updated |

!!! note "Note"
    * Using "today" at the time of the query as the reference, the system automatically lists products updated in the last 90 days that have had no sales in the last 30 days.
    * This table does not support custom dates. If you have many products, page through them.

### Product Purchases by Period { #reference-product-analysis-period }

| Field | Description |
| :-- | :-- |
| Product Name | Product name (including variant) |
| Order Count | Number of orders containing this product in the query period |
| Sales Volume | Total units of this product sold in the query period |
| Total Product Sales | Total sales amount of this product in the query period |

!!! note "Note"
    * The last row of the table is the "Total" for all products.
    * Use the multi-select product filter to view only specific products. Excel export is supported.
    * Only valid orders are counted (not canceled; no return needed or return rejected).
