---
title: "View Sales Performance"
description: "Store managers and staff can use the sales report to quickly see the number of linked members and online and offline sales attribution data for a specific time range."
created: 2026-05-04 14:14
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - APP MARKET
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions:
  - STORE PAL
intents:
  - 查看業績報表
  - 分析綁定會員數
  - 核對業績歸因
features:
  - 門市助理 業績報表
  - "Sales Attribution"
prerequisites: []
related: []
tags:
  - 業績歸因
acoiv: operation
apis: []
devices:
  - mobile
  - desktop
ui_components:
  - 業績報表
  - 時間區間
paths:
  - 設定 > 功能設定 > 前台功能設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/view-sales-performance/"
comments: false
search:
  exclude: false
icon: lucide/bar-chart-3
hide: []
---

# View Sales Performance
Store managers and staff can use the sales report to quickly see the number of linked members and online and offline sales attribution data for a specific time range.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

![](../../../assets/images/門市助理-前台-業績報表-畫面總覽01.en.png){ .hero-page }

!!! tip "Use Cases"
	- **Performance Tracking**: Store staff can check their own referral sales for today or this month in real time.
	- **Store Management**: Store managers analyze each staff member's linked members and sales contribution.
	- **Better Decisions**: Adjust store promotion strategies based on the share of online and offline sales.


## Before You Start { #prerequisites-sales-view }

- **Data Source**: Report data includes total online and offline sales attribution. Choose the time range you need.
- **Permission Differences**:
    - **Store Manager**: Can view **Store Sales** and **Personal Sales**.
    - **Staff**: Can view only **Personal Sales** by default. Staff need admin authorization to view store sales.


## How to Use { #operate-sales-view }

=== "Store Assistant Frontend"

	### View the Sales Report { #operate-sales-view-view-report }

	1. On the Store Assistant frontend home page, click **Sales Report** at the bottom.
	2. Switch tabs to view information:

		| Tab | Content | Available To |
		|----------|----------|----------|
		| **Store Sales** | Total store links, staff sales ranking, online/offline sales attribution | Store managers<br>Authorized staff |
		| **Personal Sales** | Personal total links, personal online/offline sales attribution | All store staff |

	3. Click **Time Range** in the upper-right corner to filter data by date.
	4. Click the **question mark (?)** icon next to a field to see the detailed definition of that sales item.


=== "Store Assistant Admin"

	### Let Staff View Store Sales { #operate-sales-view-view-store }

	1. Log in to the Store Assistant admin and go to **設定 > 功能設定 > 前台功能設定**.
	2. In the **Sales Report** section, switch **Store Sales Report** to `Open`.
	3. Click **Save** to update the permissions.

	![](../../../assets/images/門市助理-後台-設定-功能設定-門市業績報表01.en.png){ .screenshot }