---
title: VIP 功能運作指南
description: 深度解析新版 VIP 系統的滾動式計算、即時觸發判定以及升降等回溯邏輯，協助商家建立精準的會員營運觀念。
created: 2026-01-23 00:00
last_modified: 2026-06-30 12:30
lang: zh-TW
type: guide
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 會員
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: trunk
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 規劃 VIP 制度
  - 理解 VIP 計算邏輯
features:
  - VIP 制度
  - 會員分級
prerequisites: []
related: []
tags: []
acoiv: activate
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > VIP 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7505
  - https://www.cyberbiz.io/support/?p=11860
permalink: https://help.cyberbiz.io/ec/members/vip
comments: false
search:
  exclude: false
icon: lucide/crown
hide: []
---
# VIP Feature Operation Guide

Through a flexible tiered system and automated calculation engine, we help you accurately identify high-value customers and provide them with differentiated, exclusive treatment, building long-term customer loyalty.

## Choose your membership system
Based on your operational strategy, you can choose to establish a universal system applicable to the entire site, and design exclusive thresholds and benefits for specific customer groups.

<div class="grid cards" markdown>

- :lucide-users:{ .lg }

  [__store-wide VIP System__](setup-store-wide-vip-system.md)

   Establish a unified tiered system across the entire site, allowing all members to gradually advance through accumulated spending.

- :lucide-tag:{ .lg }

  [__Exclusive VIP Group__](create-exclusive-vip-groups.md)

   Set independent level rules and thresholds for members with specific tags (such as: KOLs, employee purchasers, high-spending customers).

</div>

## Which expenses will be included?
Not all orders will be counted towards your VIP accumulated spending. The system only calculates orders that are "transactions that have been substantially completed" and "have no return concerns":

### "Valid orders" will be counted as VIP status.
* **Paid Orders**: Payment status is **Paid**.

* **Cash on Delivery Orders**: Payment status is **Cash on Delivery**, and delivery status is **Received**. (For self-ordered cash on delivery orders, the status is **Shipped**.)

* **Shipped and Closed Orders**: Orders with a **Closed** status and a delivery status other than **Not Shipped or Preparing to Ship**.

For the above three types of orders, the order status cannot be **Cancelled**, and the return status must be **No Return Required**; otherwise, the order is considered invalid.

* **Rejected Return Orders**: If this order had a return dispute but was ultimately marked as **Rejected Return**.

### "Invalid orders" not counted towards VIP status
* **Cancelled Orders**: Orders with a **cancelled** status.

* **Returned Orders**: Orders whose return status is neither **Return Rejected** nor **Return Not Required**.

* **Partially Returned Orders**: If an order is partially returned, the system will by default exclude the entire order amount.

## When will the system update its level?

### 1. Triggering the judgment timing
The system will immediately recalculate a member's VIP level whenever the following actions occur:

* **Order Status Changes:** Valid orders completed, invalid orders completed.

* **Data Changes:** New member registration, merchant-manually modified member tags, merchant-manually added or removed members (valid orders from other channels).

* **Version Activation:** When a merchant releases a new VIP system version and it reaches its effective date.

### 2. Rolling Backtracking Calculation Method
The system doesn't consider the "calendar year," but instead traces back a specific expiration period from the "triggering moment."

* **Moving Interval**: Imagine a fixed-width time interval (e.g., 365 days). Whenever membership levels are recalculated, all orders within that time interval are traced back to the current time.

* **Metabolism**: New orders "enter the interval," increasing the total; orders older than 365 days are "moved out of the interval" and no longer counted in the total.

*7. "Why does a member's accumulated spending amount decrease?"

*4. If a "large order" from a year ago has just expired and moved out of the calculation interval, while a new order is smaller, the member's accumulated spending amount may decrease.

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }

  [__Upgrade / Downgrade / Renewal Rules__](vip-upgrade-downgrade-renewal-rules.md)

  Understand the calculation of VIP Upgrade expiration date, the retrospective recalculation of Downgrade, and the timing of Renewal determination.

</div>

## Rule activation and version management
To protect consumer rights and provide merchants with a grace period for announcements, the system has an effective restriction on changes to core rules.

* **Basic Settings (D+2 Specification)**: Modifications to core logic such as tier names and Upgrade/Renewal thresholds will take effect **after 2 days** (except for initial releases).

* **Discount Settings (Immediate Effect)**: Modifications to discount rates, bonus points, and other reward content will take effect immediately after saving.

* **Version Management**: Through the "Copy Version" function, you can pre-plan the next phase of your membership strategy without affecting the current running version.

## VIP Exclusive Benefits Application
Transform the VIP system into a tangible marketing driver, increasing average order value and repurchase rate through exclusive offers and differentiated pricing.

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }

  [__VIP Exclusive Offers__](setup-exclusive-vip-discounts.md)

  Set up full order discounts, exclusive free shipping thresholds, bonus multipliers, and distribute VIP birthday gifts and Upgrade gifts.

- :lucide-banknote:{ .lg }

  [__Member Exclusive Prices__](../../products/pricing/setup-vip-member-pricing.md)

  Set exclusive prices for different VIP levels for specific products, allowing higher-level members to enjoy the most direct price advantages.

</div>
