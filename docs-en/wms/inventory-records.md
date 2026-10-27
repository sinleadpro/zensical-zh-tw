---
title: "Inventory Records"
description: "Look up inventory change details and inventory age in the e-commerce warehouse system (WMS), including inventory history, the inventory change summary, and the inventory age report."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 庫存紀錄
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 查詢歷史庫存
  - 分析庫存週轉
  - 核對異動明細
features:
  - 庫存追蹤
  - 庫齡分析
  - 異動紀錄
  - 呆滯庫存管理
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 需已完成商品進倉作業
related:
  - wms/seasonal-groups/
tags:
  - WMS
  - "Inventory Age"
  - "Change Details"
  - "Report Analysis"
acoiv: integration
apis: []
devices:
  - desktop
ui_components:
  - 歷史庫存查詢頁
  - 庫齡分析列表
  - 異動明細查詢頁
paths:
  - 庫存紀錄 > 庫齡報表
  - 庫存紀錄 > 歷史紀錄
  - 庫存紀錄 > 庫存異動總表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5742
  - https://www.cyberbiz.io/support/?p=9159
permalink: "https://help.cyberbiz.io/wms/inventory-records/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Inventory Records
Look up inventory change details and inventory age in the e-commerce warehouse system (WMS), including inventory history, the inventory change details, and the inventory age report.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

## Inventory Age Report { #overview-inventory-aging }

### Analyze Turnover Health { #operate-inventory-turnover }

This report shows how long stock has been in storage. Use it to plan promotions or clear old stock.


### Filter and Search { #operate-inventory-filter }

1. Go to **庫存紀錄 > 庫齡報表**.
2. Set the filters:
    - **Specified Item**: Enter a product name or item number to filter for specific products.
    - **Inventory age / inactive days**: Enter a range of days to find products that are becoming stale.
    - **Season group**: Filter by a specific sales wave based on your [season settings](seasonal-groups.md).
    - **StockEntry Date**: Set the date range when products were first received.
3. Click **Export** to download an Excel report for analysis.

### Key Metrics { #specs-inventory-metrics }

- **Inventory Age Days**: The total number of days since the product's **first receipt date**.
- **Inactive Days**: The total number of days since the product's **last outbound date**. A high number means the product is not selling well.

![](../assets/images/WMS-後台-庫存記錄-庫齡報表-畫面總覽01.en.png){ .screenshot }


## History { #overview-inventory-history }

### Daily Snapshots { #operate-inventory-snapshot }

Shows inventory as of a past date. Use it for month-end reconciliation or to back up turnover records.

1. Go to **庫存紀錄 > 歷史紀錄**.
2. Select a **query date** (yesterday or earlier only).
3. Enter an **item number** or choose a **warehouse zone** to narrow the results.
4. Click **Search** or **Export**.

!!! info "Update Schedule"
    The system updates the previous day's inventory snapshot at **4:00 AM every day**. History for **the current day** is not available in the admin panel, so use data from **yesterday or earlier**.

![](../assets/images/WMS-後台-庫存記錄-歷史紀錄-畫面總覽01.en.png){ .screenshot }

## Inventory Change Details { #overview-inventory-changes }

### Track a Single Product { #operate-inventory-flow }

To check the receipt, shipping, and return details of a specific product, use the change details.

1. Go to **庫存紀錄 > 庫存異動總表**.
2. Enter an **item number** and set a **date range**.
3. The system lists every event that changed stock in that period, including the document number, type, and quantity change.
4. You can export the search results.

### Overall Change Summary { #overview-inventory-trends }

Use this to review total transfers, adjustments, and sales shipments.

1. Go to **庫存紀錄 > 庫存異動總表**.
2. Set a **date range** and a **warehouse zone**.
3. The results show total changes by type, such as **Inbound**, **Shipped**, and **Adjustment**.
4. You can download the full summary.

![](../assets/images/WMS-後台-庫存記錄-庫存異動總表-畫面總覽01.en.png){ .screenshot }
