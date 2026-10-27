---
title: "Bonus Points For Specific Shipping Methods"
description: "Use the Bonus Points for Specific Shipping Methods tool to reward bonus points for selected shipping methods and steer customers toward low-cost or partner carriers."
created: 2026-02-05 00:00
last_modified: 2026-06-30 10:56
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
  - Marketing
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - Enterprise
cyb_extensions: []
intents:
  - 建立物流紅利活動
  - 設定物流贈點規則
  - 管理物流紅利群組
features:
  - 紅利點數
  - 物流紅利群組
prerequisites:
  - "商店已開啟紅利點數功能.en"
  - "已完成基本物流方式設定.en"
related:
  - ec/marketing/references/coupon-and-bonus-credit-rules.en/
tags:
  - 行銷活動
  - "Bonus Rewards"
  - "Shipping Optimization"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 指定物流送紅利
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=3480
permalink: "https://help.cyberbiz.io/ec/marketing/conditional-send/send-bonus-points-for-specific-logistics.en/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---
# Bonus Points For Specific Shipping Methods

Use the Bonus Points for Specific Shipping Methods tool to reward bonus points for selected shipping methods and steer customers toward low-cost or partner carriers.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

![](../../../assets/images/EC-後台-行銷活動-指定物流送紅利-畫面總覽01.png){ .hero-page }

!!! tip "Use Cases"
    - **Lower shipping costs**: Give more bonus points for lower-cost options such as store pickup or convenience store pickup to reduce home delivery volume.
    - **Match carrier promotions**: When a carrier (such as 7-Eleven or FamilyMart) runs a limited-time shipping offer, add extra bonus points at the same time.
    - **Ease peak-season load**: During big sales, use bonus points to steer customers away from home delivery and reduce shipping backlogs.


## Before You Start

Before you set up shipping bonus points, make sure you understand these key rules:

- **When points are given**: bonus points are automatically credited to the member's account after the order status changes to **Completed**.
- **Stacking**: If an order qualifies for bonus points by shipping method, product, and payment method, the system **adds them all together**.
- **Multiple Collections**: If a shipping method is in more than one active Shipping Bonus Collections group, the system checks all of them and gives the bonus points set in each Collections group.


## Steps

### Step 1: Add Shipping Bonus Collections

1. Log in to the CYBERBIZ admin and go to **Marketing > Bonus for Specific Shipping**.
2. Enter the Collections Name and click **Add a new collection** on the right.

### Step 2: Set The Collections Basic Rules

Click the new Collections and fill in the following in the settings area below:

1. **Collection name**: Enter a Name for admin use (such as Eco Shipping Bonus Boost - Spring).
2. **Promotion dates**: Set the **Start Date** and **End Date**.
3. **Bonus points**: Enter the fixed number of points customers get when they choose this shipping method.
  > Points must be a **positive whole number**. If you set the validity days to `0`, the points never expire.
4. **Validity**: Enter how many days the bonus points can be used.

### Step 3: Select And Add Shipping Methods

1. In the **Search and Select Shipping** area on the left, type a shipping method Name in the search box (such as "convenience store").
2. Select the shipping methods to add to this Collections.
3. Click **Add**.
4. The added items appear in the Collections.

![](../../../assets/images/EC-後台-行銷活動-指定物流送紅利-設定群組與選擇商品01.png){ .screenshot }

## FAQ

??? quote "Why can't I find a shipping method in the list on the left?"
    Check whether the shipping method is turned on. If it isn't, it won't appear in the list.

??? quote "Does changing the bonus points during a promotion affect earlier orders?"
    No. Changes apply only to new orders placed **after the change**. Orders already placed or completed keep the rules in effect when they were placed.

??? quote "Can I give shipping bonus points only above a minimum spend?"
    No. Bonus Points for Specific Shipping Methods gives a fixed number of points with no threshold whenever the shipping method is chosen. If you need a spending threshold, use Bonus Points for Specific Products instead and explain it in your promotion copy.

## More Actions

<div class="grid cards" markdown>

- :lucide-wallet:{ .lg }
  [__coupon / Bonus Points Crediting Rules__](../references/coupon-and-bonus-credit-rules.md)
  Explains when purchase rewards are credited to accounts (import members), and how order completion and returns affect crediting of bonus points and coupons.

</div>