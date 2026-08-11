---
title: Establish a VIP system for the entire museum
description: Gradually establish VIP membership levels, upgrade thresholds, and renewal conditions to build a membership system that aligns with the store's brand image.
created: 2026-01-23 00:00
last_modified: 2026-06-30 12:30
lang: zh-TW
type: tutorial
status: ""
version: 1.1.2
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
difficulty: beginner
tnb: trunk
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 建立 VIP 等級
  - 設定升等條件
  - 設定續會條件
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
ui_components: []
paths:
  - 會員 > VIP 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7509
  - https://www.cyberbiz.io/support/?p=12291
permalink: https://help.cyberbiz.io/ec/members/vip/setup-store-wide-vip-system
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---
# Establish a Storewide VIP System

Gradually set VIP membership levels, upgrade thresholds, and renewal conditions to build a membership system that aligns with the store's brand image.

{ .subtitle }

![](../../../assets/images/EC-後台-會員-VIP設定-畫面總覽01.png){ .hero-page }

After completing the initial planning, you can begin building the VIP tiers in the backend. This guide will walk you through the entire process from tier naming to threshold setting.

## Step 1: Basic Data Setup
Go to the backend, select **Members > VIP Settings**, and then click **Add Membership Tier** under **All VIPs**.

=== "Other Versions"

1. **Tier Name**: Enter an easy-to-understand name (e.g., Silver Member, Premium VIP).

2. **Membership Validity Period**: It is recommended to set a consistent validity period for all tiers (commonly 365 days) for easy management.

3. **Member Card Image**: This image will be displayed on the front-end screen of the Member Center, enhancing brand exclusivity.

* **Suggested Size**: 320x210px (within 1MB).

![](../../../assets/images/EC-後台-會員-VIP設定-新增會員層級01.png)

=== "Enterprise Version"

1. **Tier Name**: Enter an easy-to-understand name (e.g., Silver Member, Premium VIP).

2. **Member Card Image**: This image will be displayed on the front-end screen of the Member Center, enhancing brand exclusivity. **Recommended Size:** 320x210px (under 1MB)

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-會員-VIP設定-新增會員層級01.png)

## Step 2: Set the upgrade threshold
=== "Other Versions"

Upgrade thresholds determine how members achieve that level of membership.

* **Single Transaction Amount**: The amount a customer spends in a single checkout. Suitable for attracting high-spending customers for direct upgrades.

* **Total Spending During Validity Period**: The sum of all valid orders within your set validity period (e.g., the past 365 days).

=== "Enterprise Version"

1. Set **Upgrade Calculation Period**

- **Limited Validity Period (Default)**: Select the number of days for the validity period from the drop-down menu.

- **Unlimited Validity Period**: Uses all of the member's historical records as the calculation range for membership upgrade conditions.

2. Set **Upgrade Threshold**

- **Single Transaction Amount**: The amount a customer spends in a single checkout within your set validity period.

- **Total Spending During Validity Period**: The sum of all valid orders within your set validity period.

!!! tip "Creating a Cumulative Upgrade Mechanism"

- **Setting Method**: Set the upgrade period to **unlimited**

- **Operating Mechanism**: The system will automatically retrieve all historical transaction records of the member since their **first order on this website**, and determine upgrade eligibility based on your specified thresholds:

- Single Transaction Amount: Detects whether the member's single order amount since their first order on this website meets the threshold.

- Total Spending within the Validity Period: Reviewes whether the member's total spending since their first order on this website meets the threshold.

!!! note "Priority Determination"

If you set both "single transaction" and "cumulative" thresholds, the system will determine the upgrade based on the **most beneficial outcome for the consumer**.

## Step 3: Set renewal thresholds
=== "Other Versions"

Renewal conditions are used to determine whether a member can maintain their original level after the expiration of their membership period.

* **Single Transaction Amount**: The amount a customer spends in a single checkout. Suitable for attracting high-spending customers to upgrade directly.

* **Total Spending During the Validity Period**: The sum of all valid orders within the validity period you set (e.g., the past 365 days).

![](../../../assets/images/EC-後台-會員-VIP設定-新增會員層級02.png)

=== "Enterprise Version"

1. Set **Membership Level Validity Period**

**Membership Level Validity Period** is the **Membership Validity Period** for that level. The system will also use the spending records within this period to calculate whether the member meets the **renewal eligibility**.

- **With Validity Period (Default)**: Select the number of days for the membership validity period from the drop-down menu.

- **No Validity Period**: The membership validity period has no expiration date; the system will not check renewal eligibility. 2. Setting **Renewal Thresholds**

Based on the previous step's setting of the membership level's validity period, determine how to fill in the renewal thresholds:

- ****Limited-Term (Default)**:** **Please be sure to fill in the renewal threshold.** If no renewal threshold is set, the system will not perform a renewal condition check when the membership expires, and the member will lose their VIP status.

- ****Unlimited-Term**:** Renewal thresholds can be left blank (the system will not perform a renewal check, and the renewal condition thresholds will not take effect).

Setting Thresholds:

- ****Single Transaction Amount**:** The amount a customer reaches in a single checkout within the validity period you set.

- ****Total Transactions within the Validity Period**:** The sum of all valid orders within the validity period you set.

4. "Creating a Permanent Renewal Mechanism"

- **Setting Method**: Set the renewal period to **Unlimited**

- **Operation Method**: The system will not initiate **expiration renewal checks** for this level. Once a member is upgraded to this level, they will not be downgraded due to renewal checks.

:lucide-triangle-alert: If a member places an invalid order (e.g., a cancelled order or a return), the downgrade mechanism will still be triggered, and they may still be downgraded.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-會員-VIP設定-新增會員層級03.png)

!!! note "Priority of Determination"

If you set both "single order" and "cumulative" thresholds, the system will use the result that is **most beneficial to the consumer** for the upgrade determination.
