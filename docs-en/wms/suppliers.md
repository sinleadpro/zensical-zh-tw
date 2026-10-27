---
title: Vendors
description: "Create vendor records in the e-commerce warehouse to keep track of where your goods come from. When products are linked to vendors, the system fills in vendor details automatically when you create receipt orders or count inventory."
created: 2026-03-16 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：權限設定
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 供應商
  - 商品
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 建立供應商帳號
  - 編輯廠商基本資訊
  - 綁定商品來源廠商
features:
  - 供應商管理
  - 商品來源追蹤
  - 進倉資料對接
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
related: []
tags:
  - "Source Vendors"
  - "Product Management"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 供應商列表頁面
  - 供應商編輯頁面
  - 商品編輯頁面
paths:
  - 商品 > 單一品項
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7975
  - https://www.cyberbiz.io/support/?p=39949
permalink: "https://help.cyberbiz.io/wms/suppliers/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Vendors
Create vendor records in the e-commerce warehouse to keep track of where your goods come from. When products are linked to vendors, the system fills in vendor details automatically when you create receipt orders or count inventory.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-供應商-畫面總覽01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Track inbound sources**: Tell apart deliveries from different brands or contract manufacturers for inbound inspection.
    - **Inventory accountability**: With products linked to vendors, you can quickly trace where goods came from when a stock count finds a problem.
    - **Inventory report analysis**: Later, analyze purchase cost and sales speed by vendor.


## Before You Start { #prerequisites-suppliers }

- **Unique records**: We recommend giving each vendor a unique code or name, so receipt orders are not matched to the wrong vendor.


## Steps { #operate-suppliers }

### Task 1: Create a Vendor Record { #operate-suppliers-create }

Create basic records for the factories, brands, or traders you work with, to identify them in later business.

1. Log in to the e-commerce warehouse admin panel and go to **Vendors**.
2. Click **Add Vendor** in the upper-right corner (or go straight to the add page).
3. Enter the **Vendor Name**, **Contact Person**, **Phone**, **Email**, and **Address**.
4. Check the details, and then click **Save**.
5. The new vendor appears in the list.

![](../assets/images/WMS-後台-供應商-新增供應商01.en.png){ .screenshot }

### Task 2: Link Products to a Vendor { #operate-suppliers-bind }

After you create a vendor, link its products to it manually so the system can match them automatically at receiving.


1. Go to **Products > 單一品項** and click the **product name** to open the edit page.
2. Find the **Vendor** field on the page.
3. Select the vendor name from the drop-down list.
4. Click **Save** to link them.

![](../assets/images/WMS-後台-商品-單一品項-商品綁定供應商01.en.png){ .screenshot }

### Task 3: Edit Vendor Information { #operate-suppliers-maintain }

When a vendor's contact details change, update them promptly to avoid miscommunication at receiving.

1. Go to **Vendors** and select the **vendor name** to change in the list.
2. Click :lucide-pencil:.
3. Correct the details (such as phone or address), and then click **Save**.
