---
title: "VIP Feature Guide"
description: "An in-depth guide to the new VIP system's rolling calculations, real-time evaluation triggers, and retroactive logic for upgrades and Downgrade, helping merchants build a clear understanding of member operations."
created: 2026-01-23 00:00
last_modified: 2026-06-30 12:30
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
  - 會員
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 規劃 VIP 制度
  - 理解 VIP 計算邏輯
features:
  - VIP 制度
  - 會員分級
prerequisites: []
related:
  - ec/members/vip/setup-store-wide-vip-system.en/
  - ec/members/vip/create-exclusive-vip-groups.en/
  - ec/members/vip/vip-upgrade-downgrade-renewal-rules.en/
  - ec/members/vip/setup-exclusive-vip-discounts.en/
  - ec/products/pricing/setup-vip-member-pricing.en/
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
permalink: "https://help.cyberbiz.io/ec/members/vip.en/"
comments: false
search:
  exclude: false
icon: lucide/crown
hide: []
---

# VIP Feature Guide

Use a flexible tier system and automated calculation engine to identify high-value customers accurately, offer differentiated VIP benefits, and build long-term customer loyalty.

## Choose Your Membership System

Based on your operating strategy, choose a general system for the entire store and set custom thresholds and benefits for specific customer groups.

<div class="grid cards" markdown>

- :lucide-users:{ .lg }
  [__All VIP System__](setup-store-wide-vip-system.md)
  Create a unified tier system for the entire store, allowing all members to advance through tiers as their purchases accumulate.

- :lucide-tag:{ .lg }
  [__Exclusive VIP Groups__](create-exclusive-vip-groups.md)
  Set independent tier rules and thresholds for specific Tags members, such as KOLs, employees, and high-value customers.

</div>

## Which Purchases Count

Not all orders count toward the cumulative VIP purchase amount. The system only counts orders with completed transactions and no return concerns:

### Valid Orders That Count Toward VIP Status

*   **Paid orders**: The payment status is **Paid**.
*   **Received cash-on-delivery orders**: The payment status is **Cash on Delivery**, and the delivery status is **Received**. For custom cash-on-delivery orders, the delivery status is **Shipped**.
*   **Completed orders that have been shipped**: The order status is **Completed**, and the delivery status is neither **Not Shipped** nor **Preparing to Ship**.

> For the three order types above, the order status must not be **Canceled**, and the return status must be **No Return Required**. Otherwise, the order is considered invalid.

*   **Orders with rejected returns**: The order had a return dispute but was ultimately marked as **Return Rejected**.

### Invalid Orders That Do Not Count Toward VIP Status

*   **Canceled orders**: The order status is **Canceled**.
*   **Returned orders**: Orders with a return status other than **Return Rejected** or **No Return Required**.
*   **Partially returned orders**: If an order is **Partially Returned**, the system excludes the entire order amount by default.

## When The System Updates Membership Tiers

### 1. Evaluation Triggers

Whenever a member performs any of the following actions, the system immediately recalculates that member's tier:

*   **Order status changes**: A valid or invalid order is created.
*   **Data changes**: A new member registers, a merchant manually changes a member's Tags, or a merchant manually increases or decreases the member's **Valid Orders from Other Channels**.
*   **Version activation**: A merchant publishes a new version of the VIP system, and it reaches its effective date.

### 2. Rolling Lookback Calculation

The system does not use the calendar year. Instead, it looks back over a specific validity period from the time the recalculation is triggered.

*   **Rolling window**: Imagine a fixed-width time window, such as 365 days. Whenever a member's tier is recalculated, the system looks back from that moment and includes all orders within the window.
*   **Rolling turnover**: New orders enter the window and increase the total. Orders older than 365 days leave the window and no longer count toward the total.

!!! info "Why Did a Member's Cumulative Purchase Amount Decrease?"
    If a high-value order from one year ago expires and leaves the calculation window while newer orders have smaller amounts, the member's cumulative purchase amount may decrease.

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }
  [__Upgrade / Downgrade / Renewal Rules__](vip-upgrade-downgrade-renewal-rules.md)
  Learn how the validity period for VIP Upgrade is calculated, how Downgrade are recalculated retroactively, and when Renewal are evaluated.

</div>


## Rule Activation And Version Management

To protect consumer rights and give merchants time to announce changes, the system applies effective-date restrictions to changes in core rules.

*   **Basic settings (D+2 rule)**: Changes to core logic, such as tier names and Upgrade/Renewal thresholds, take effect **2 days later**, except for the initial publication.
*   **Benefit settings (effective immediately)**: Changes to benefits, such as discount rates and bonus points issued, take effect immediately after saving.
*   **Version management**: Use **Copy Version** to plan the next phase of your membership strategy without affecting the currently active version.

## Applying Exclusive VIP Benefits
Turn your VIP system into a marketing driver. Use exclusive offers and differentiated pricing to increase average order value and repeat purchase rates among members.

<div class="grid cards" markdown>

- :lucide-ticket:{ .lg }
  [__Exclusive VIP Offers__](setup-exclusive-vip-discounts.md)
  Set order-level discounts, exclusive free-shipping thresholds, bonus point multipliers, and issue VIP birthday gift and Upgrade gifts.

- :lucide-banknote:{ .lg }
  [__Member-Exclusive Pricing__](../../products/pricing/setup-vip-member-pricing.md)
  Set exclusive prices for specific products by VIP tier, giving higher-tier members the most direct pricing benefits.

</div>
