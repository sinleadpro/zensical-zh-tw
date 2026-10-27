---
title: Channels
description: "Set up channels to manage inventory for different sales platforms and define each channel's accepted product expiry range and shipping conditions."
created: 2026-03-12 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：通路綁定商品、報表分析
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 通路
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 新增銷售通路
  - 設定效期出貨範圍
  - 配置同效期出貨限制
features:
  - 通路管理
  - 效期規則設定
  - 出貨條件控管
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 商品需已開啟效期管理功能
related: []
tags:
  - "Platform Management"
  - "Inventory Allocation"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 通路列表頁面
  - 通路規則編輯頁面
paths:
  - 通路
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5735
  - https://www.cyberbiz.io/support/?p=9043
permalink: "https://help.cyberbiz.io/wms/channels/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Channels
Set up channels to manage inventory for different sales platforms and define each channel's accepted product expiry range and shipping conditions.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-通路-畫面總覽01.en.png){ .hero-page }

## Use Cases { #intro-channels }

- **Expiry-based routing**: Set how strict each channel is about **remaining shelf life**.
    - **Mass retail channels**: Set a longer shelf-life threshold to meet the shelving rules of large retailers.
    - **Sale or employee-benefit channels**: Set a shorter shelf life to clear stock faster and keep these orders clearly apart from orders that need normal shelf life.
- **Shipping type statistics**: Create channels by business type (such as carrier type, special packaging, or bulk purchasing). Reports can then show the share of each shipping type quickly.



## Set up Channel Rules { #operate-channels-rules }

Channel rules mainly control how **products with expiry dates** are shipped. With rules in place, the system automatically leaves out products with too little shelf life during picking.

### 1. Create a Channel { #operate-channels-create }

Go to **通路 > 列表** and click **Add Channel** to open the edit page.

- **Channel Name**: Enter a name that is easy to recognize. We recommend naming channels by **platform + logistics** or by **business type**.
    - **Name examples**: `酷澎`, `團購`, `誠品生活`, `東森-黑貓`, `東森-全家`.
- **Shipping zone**: Choose the physical or virtual warehouse for this channel, so orders deduct stock from the right zone.
- **Channel Type**: Choose `B2C` or `C2C` based on your business model.

![](../assets/images/WMS-後台-通路-新增通路01.en.png){ .screenshot }

### 2. Add Expiry Rules { #operate-channels-expiry }

Click **Add Rule** and set the product conditions this channel accepts:

#### Accepted Range { #specs-channels-scope }

- **Minimum original shelf life (required)**: The **minimum** number of days of remaining shelf life the channel accepts.
    - *Example*: Set 50 days. The system only picks products that expire more than 50 days from now.
- **Maximum original shelf life (optional)**: The **maximum** number of days of remaining shelf life the channel accepts.
    - *Example*: Set 100 days. The system leaves out products that expire more than 100 days from now. This is usually used together with the minimum to target a specific shelf-life range.

#### Shipping Rule Types { #specs-channels-shipping }

Choose whether to calculate by **ratio** or by **day**:

- **ratio**: Calculated as **total shelf life × value**.
    - *Example*: Set 50%. If a product's total shelf life is 100 days, the system ships units that expire more than 50 days (100 × 50%) from now.
- **day**: Calculated directly from the **value**.
    - *Example*: Set 50 days. No matter how long the total shelf life is, the system ships units that expire more than 50 days from now.

#### Special Conditions { #specs-channels-special }

- **Same expiry**: Select this if the channel requires **all units of the same item in one order to come from the same expiry batch**. The system then locks picking to a single batch number.

![](../assets/images/WMS-後台-通路-設定出貨效期01.en.png){ .screenshot }
