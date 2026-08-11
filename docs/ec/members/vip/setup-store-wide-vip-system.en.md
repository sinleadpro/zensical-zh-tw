---
title: 建立全館VIP制度
description: 逐步設定 VIP 會員層級、升等門檻與續會條件，建構符合商店品牌形象的會員體系。
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
# Establishing the store-wideVIP System

Gradually set VIP membership levels, Upgrade thresholds, and Renewal conditions to build a membership system that aligns with the store's brand image.

{ .subtitle }

![](../../../assets/images/EC-後台-會員-VIP設定-畫面總覽01.en.png){ .hero-page }

After completing the initial planning, you can begin building the VIP tiers in the backend. This guide will walk you through the entire process from tier naming to threshold setting.

## Step 1: Basic Data Setup
Go to the backend, select **Membership > VIP Settings**, and click **Add Membership Tier** under **store-wideVIP**.

=== "Other Versions"

    1. **Tier Name**: Enter an easy-to-understand name (e.g., Silver Member, Premium VIP).

    2. **Membership Validity Period**: It is recommended to set a consistent validity period for all tiers (commonly 365 days) for easy management.

    3. **Membership Card Image**: This image will be displayed on the front-end screen of the Membership Center, enhancing brand exclusivity.

        * **Suggested Size**: 320x210px (within 1MB).

    ![](../../../assets/images/EC-後台-會員-VIP設定-新增會員層級01.en.png)

=== "Enterprise Edition"

    1. **Tier Name**: Enter an easy-to-understand name (e.g., Silver Member, Premium VIP).     2. **Member Card Image**: This image will be displayed on the front end of the member center, enhancing brand exclusivity.

        * **Suggested Size**: 320x210px (within 1MB).

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-會員-VIP設定-新增會員層級01.png)

## Step 2: Set the Upgrade threshold
=== "Other Versions"

    Upgrade thresholds determine how members achieve this level of membership.

    * **Single Transaction Amount**: The amount a customer spends in a single checkout. Suitable for attracting high-spending customers for direct promotion.

    * **Total Spending During Validity Period**: The sum of all valid orders within your set validity period (e.g., the past 365 days).

=== "Enterprise Edition"

    1. Setting **Upgrade Calculation Period**

         - **Validity Period (Default)**: Select the validity period in days from the drop-down menu.

         - **Unlimited Validity Period**: Uses all of the member's historical records as the calculation period for the member's Upgrade criteria.

          
    2. Setting **Upgrade Threshold Conditions**

         - **Single Transaction Amount**: The total amount a customer spends in a single checkout within your set validity period.

         - **Total Transactions Within the Validity Period**: The sum of all valid orders within your set validity period.

        

    !!! Tip "Creating a Cumulative Upgrade Mechanism"

         - **Setting Method**: Set the Upgrade period to **unlimited**

         - **Operating Mechanism**: The system will automatically retrieve all historical transaction records of the member since **their first order on this website**, and determine Upgrade eligibility based on your specified thresholds:

             - Single Transaction Amount: Detects whether the amount of any single order placed by the member since their first order on this website meets the threshold.

             - Total Amount Consumption During the Validity Period: Retrospectively checks whether the member's total consumption amount since their first order on this website meets the threshold.

!!! note "Priority Determination"

     If you set both "single transaction" and "cumulative" thresholds, the system will use the **most beneficial to the consumer** result for Upgrade determination.

## Step 3: Set the Renewal threshold
=== "Other Versions"

    Renewal conditions are used to determine whether a member can maintain their original level after the expiration of their membership period.

    * **Single Transaction Amount**: The amount a customer spends in a single checkout. Suitable for attracting "high-spending" customers for direct promotion.

    * **Total Spending During the Validity Period**: The sum of all valid orders within the validity period you set (e.g., the past 365 days).

    ![](../../../assets/images/EC-後台-會員-VIP設定-新增會員層級02.en.png)

=== "Enterprise Edition"

    1. Setting the **Membership Level Validity Period**

      
         The **Membership Level Validity Period** is the **Membership Validity Period** for that level. The system will also use the spending records within this period to calculate whether the member meets the **Renewal eligibility**.       

         - **Expired Date (Default)**: Select the membership validity period in days from the drop-down menu.

         - **Unlimited Date**: Membership validity has no expiration date; the system will not check Renewal eligibility.

    2. Setting **Renewal Threshold Requirements**

         Based on the previous step's setting for the membership level's validity period, determine how to fill in the Renewal threshold:

         - **Expired Date (Default)**: **Please be sure to fill in the Renewal threshold.** If no Renewal threshold is set, the system will not perform Renewal condition checks when the membership expires, and the member will lose VIP status.

         - **Unlimited**: The Renewal threshold can be left blank (the system will not perform Renewal checks, and the Renewal condition threshold will not take effect).

         Threshold Setting:

         - **Single Transaction Amount**: The amount a customer reaches in a single checkout within the validity period you set.

         - **Total Transactions Within Validity Period**: The sum of all valid orders within the validity period you set.

    !!! tip "Creating a Permanent Renewal Mechanism"

         - **Setting Method**: Set the Renewal period to **Unlimited**.

         - **Operation Method**: The system will not initiate **Expiration Renewal Checks** for this level. Once a member reaches this membership level (Upgrade), they will not be downgraded by the system due to Renewal checks.

          
        :lucide-triangle-alert: If a member places an invalid order (e.g., order cancellation or return), the Downgrade mechanism will still be triggered for screening, and the member may still be subject to Downgrade processing.

    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-會員-VIP設定-新增會員層級03.png)

        
  
!!! note "Priority Judgment"

     If you set both "single order" and "cumulative" thresholds, the system will use the result that is **most beneficial to the consumer** for Upgrade judgment.
