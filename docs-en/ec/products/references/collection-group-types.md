---
title: "Collection Types Reference"
description: "A summary of the three collection types that can be sorted in Collection Sorting in Storefront, covering how products are added, typical uses, and display conditions."
created: 2026-06-03 18:42
last_modified: 2026-07-01 20:11
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: ""
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - EC
  - "Product Management"
  - Collections
  - "Conditionalized Collections"
  - "Mix-and-Match Discounts"
  - "Reference Table"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/products/references/collection-group-types/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


This table lists the three collection types that can be sorted in "Collection Sorting in Storefront". It explains how products are added to each type, typical uses, and the conditions a collection must meet to appear in the sorting list (the "Product List" on the storefront home page).

## Sortable Collection Types { #reference-collection-order-group-types }

| Collection Type | How Products Are Added | Typical Uses | Conditions to Appear in the Sorting List |
| :-- | :-- | :-- | :-- |
| Custom collection (Customized Collections) | You hand-pick products and add them one by one | Collections whose content you want to control yourself, such as featured products, curated lists, and campaign sections | Status set to "Published" |
| Conditionalized Collections (smart collections) | You set filter conditions (such as title, product type, vendor, price, inventory quantity, and tags), and matching products are added automatically | Large catalogs that you want sorted automatically by rules. New products are added automatically as long as they match the conditions | Status set to "Published" |
| Buy X get Y discount collection | You set up a Buy X get Y discount campaign and assign participating products. Discount types include any fixed amount, any percentage, any discounted amount, and discounted amount on each item | "Buy any N items" promotions | Status set to "Published", the campaign is currently running, and a valid discount rule is set |

!!! note "Notes"
    * "Conditions to Appear in the Sorting List" are the conditions a collection must meet to show in the admin sorting list and in the "Product List" on the storefront home page. Collections that do not meet them are not sorted and do not appear on the storefront.
    * Custom collections and conditionalized collections are included as long as their status is "Published". A Buy X get Y discount collection must also be within its campaign period and have a valid discount rule to appear.
    * This page only sorts collections relative to each other. To sort products within a collection, go to that collection's edit page.
