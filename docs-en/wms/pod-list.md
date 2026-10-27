---
title: "POD List"
description: "Use the POD list in the e-commerce warehouse system (WMS) to track the dispatch status of dedicated-vehicle orders."
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
  - POD列表
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 查詢回單狀態
  - 追蹤出貨派車憑證
  - 核對訂單交付進度
features:
  - POD 列表
  - 回單管理
  - "Proof of Delivery"
  - 訂單追蹤
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 僅適用於開通專車派車配送模式
related: []
tags:
  - WMS
  - 收貨證明
  - "Signed Receipt"
  - "Shipping Management"
acoiv: venture
apis: []
devices:
  - desktop
ui_components:
  - POD 列表頁面
  - 訂單篩選區塊
paths:
  - POD 列表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8113
  - https://www.cyberbiz.io/support/?p=39973
permalink: "https://help.cyberbiz.io/wms/pod-list/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# POD List
Use the POD list in the e-commerce warehouse system (WMS) to track the dispatch status of dedicated-vehicle orders.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-POD列表-畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-pod }

- **Dedicated vehicle shipping**: Dedicated vehicle dispatch is a **value-added service** with an extra fee. If you need it, contact your warehouse manager for a quote. After the service is turned on, you can track dedicated vehicle dispatch status here.


## POD List Overview { #overview-pod }
The screen has a filter area and a results list, so you can track orders precisely.

1. Open the CYBERBIZ e-commerce warehouse (WMS) admin panel and click **POD List**.
2. **Set the filters**:
    - **Date range**: Choose a period of no more than **30 days**, or leave it open to search all records.
    - **Attached Status**:
        - **Done**: The carrier returned the proof of delivery, and the system recorded it.
        - **Not Done**: The shipment may still be in delivery, or the returned proof has not been filed yet.
3. Click **Search**.


## Using the Results { #operate-pod-results }

After the list appears, you can:

- **Track signed receipts**: Use the **Attached Status** column to see each order's delivery status at a glance.
- **View order details**: Click an **order number** in the list to open that order's details page and check the items and recipient.
- **Spot problems**: If the shipping status shows delivered but the POD status stays **Not Done** for a long time, contact warehouse customer service or the carrier.
