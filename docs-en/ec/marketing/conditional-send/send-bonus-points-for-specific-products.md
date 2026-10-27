---
title: "Bonus Points For Specific Products"
description: "Create Bonus Points for Specific Products Collections that give bonus points when spending on selected products reaches a threshold, boosting repeat purchases and average order value."
created: 2026-01-21 00:00
last_modified: 2026-07-07 12:00
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
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 設定指定商品送紅利
features:
  - 紅利點數
  - 商品群組
  - 商品標籤
prerequisites:
  - "開啟商城紅利點數功能.en"
related:
  - ec/marketing/references/coupon-and-bonus-credit-rules.en/
tags: []
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 指定商品送紅利
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1006
  - https://www.cyberbiz.io/support/?p=3489
permalink: "https://help.cyberbiz.io/ec/marketing/conditional-send/send-bonus-points-for-specific-products.en/"
comments: false
search:
  exclude: false
icon: lucide/coins
hide: []
---
# Bonus Points For Specific Products
Create Bonus Points for Specific Products Collections that give bonus points when spending on selected products reaches a threshold, boosting repeat purchases and average order value.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    On PLUS plans, Bonus Points for Specific Products is part of the Marketing A add-on module (choose 2 of 11). Make sure you've selected this module before using it. The Enterprise plan includes it by default.

![](../../../assets/images/EC-後台-行銷活動-指定商品送紅利-畫面總覽01.png){ .hero-page }

## About Bonus Points For Specific Products

!!! tip "Use Cases"
    - **High-priced items**: For a "Featured Appliances" Collections group, set "Spend NT$5,000, get 500 points." A customer who buys one NT$5,200 robot vacuum earns points. But a customer who buys two different models at NT$3,000 each (NT$6,000 total) gets nothing, because neither item reaches the threshold on its own.
    - **Bulk-buy items**: For a "Tissue Paper" Collections group, set "Spend NT$1,000, get 100 points." One pack costs NT$120. A customer who buys 9 packs at once (subtotal NT$1,080) meets the **single-item threshold** and earns bonus points.

## Before You Start

- **Prerequisite**: Turn on bonus points in **Marketing > 全館折扣-紅利&優惠券** first.
- **Calculation rules**:
    - **Bonus points are given only when a single item in the Collections reaches the threshold.** A combined total of items in the Bonus Collections doesn't count.
    - The item's **final amount after discounts** must reach the threshold. If bonus points, a coupon, or a discount promotion applies to the item, the amount after discounts is used.
- **Eligible products**: This feature doesn't support combo products.
- **Product assignment**: A product can't be in more than one Bonus Collections with overlapping promotion periods.

## Steps

### Step 1: Create Bonus Collections For Specific Products

1. Log in to the CYBERBIZ admin and go to **Marketing > Issue Bonus Points for Selected Product**.
2. At the bottom of the page, enter the **Collection name**.
3. Click **Add a new collection** to open the detailed settings.

### Step 2: Set Basic Information And The Promotion Period

1. In the **Basic Settings** section, check or edit these fields:
    - **Collection name**: The Name used in the admin.
    - **Collection URL:**: The URL path of the storefront promotion page (letters, numbers, and hyphens `-` only).
2. Set the **Start/End Time**:
    - If there's no end time, the promotion runs indefinitely.
    - Outside the promotion period, buying the products doesn't earn points.

### Step 3: Set Bonus Point Rules And Validity

1. **Set the spending threshold**: In the **Spending Threshold (NT$)** field, enter the amount to reach (for example, `1000`).
2. **Set the points to give**: In the **Bonus Points** field, enter a whole number of points (for example, `100`).
3. **Set the validity period**: In the **Valid Days** field, enter the number of days (for example, `30`).
    - Enter `0` for points that never expire.

### Step 4: Select Promotion Products

1. In the **Product List** section, click **Add to Collections**.
2. Search by Name, SKU or tag, and select the products for the promotion.
3. Click **Add** and make sure the products appear in the Collections list.


## More Actions

<div class="grid cards" markdown>

- :lucide-wallet:{ .lg }
  [__coupon / Bonus Points Crediting Rules__](../references/coupon-and-bonus-credit-rules.md)
  Explains when purchase rewards are credited to accounts (import members), and how order completion and returns affect crediting of bonus points and coupons.

</div>