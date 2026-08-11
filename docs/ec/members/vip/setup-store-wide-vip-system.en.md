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

Gradually set VIP membership levels, Upgrade thresholds, and Renewal conditions to construct a membership system that aligns with the store's brand image.

{ .subtitle }

![](../../../assets/images/EC-後台-會員-VIP設定-畫面總覽01.en.png){ .hero-page }

After completing the initial planning, you can begin building the VIP tiers in the backend. This guide will walk you through the entire process from tier naming to threshold setting.

## Step 1: Basic Data Setup
Go to the backend, select **Membership > VIP Settings**, and click **Add Membership Tier** under **store-wideVIP**.

11. "Other Versions"

2. 1. **Tier Name**: Enter an easy-to-understand name (e.g., Silver Card Member, Premium VIP).

3. 2. **Membership Validity Period**: It is recommended to set a consistent validity period for all tiers (commonly 365 days) for easy management.

4. 3. **Member Card Image**: This image will be displayed on the front end of the Membership Center, enhancing brand exclusivity.

5. **Recommended Size**: 320x210px (within 1MB).

6. ![](../../../assets/images/EC-後台-會員-VIP設定-新增會員層級01.en.png)

12. "Enterprise Version"

7. 1. **Tier Name**: Enter an easy-to-understand name (e.g., Silver Card Member, Premium VIP). 8.2. **Member Card Image**: This image will be displayed on the front-end screen of the member center, enhancing the brand's exclusivity.

9. **Suggested Size**: 320x210px (within 1MB).

10. ![](1)

## Step 2: Set the Upgrade threshold
17. "Other Versions"

0. The Upgrade threshold determines how a member obtains this level of status.

1. **Single Transaction Amount:** The amount a customer spends in a single checkout. Suitable for attracting high-spending customers for direct promotion.

2. **Total Spending During Validity Period:** The sum of all valid orders within your set validity period (e.g., the past 365 days).

18. "Enterprise Edition"

3. 1. Set the **Upgrade Calculation Period**

4. **Within Validity Period (Default):** Select the number of days for the validity period from the drop-down menu.

5. **No Validity Period:** Uses all of the member's historical records as the calculation period for the member's Upgrade criteria. 6

7
2. Setting **Upgrade Eligibility Thresholds**

8
- **Single Transaction Amount**: The amount a customer reaches in a single checkout within the validity period you set.

9
- **Total Transactions within the Validity Period**: The sum of all valid orders within the validity period you set.

10

11
!!! tip "Building a Cumulative Upgrade Mechanism"

12
- **Setting Method**: Set the Upgrade period to **Unlimited**

13
**Operating Mechanism**: The system will automatically retrieve all historical transaction records of the member since their **first order on this website**, and determine Upgrade eligibility based on the threshold you specify:

14
- Single Transaction Amount: Detects whether the amount of any single order placed by the member since their first order on this website meets the threshold.

15 - Total Spending During the Validity Period: This checks whether the member's total spending since their first order on the website has met the target.

19 - "Priority Decision"

16 - If you have set both "Single Transaction" and "Cumulative" thresholds, the system will use the result that is **most beneficial to the consumer** for Upgrade determination.

## Step 3: Set the Renewal threshold
=== "Other Versions"

     Renewal conditions are used to determine whether a member can maintain their original level after the expiration of their membership period.

     * **Single Transaction Amount**: The amount a customer reaches in a single checkout. Suitable for attracting "high-spending" customers to upgrade directly.

     * **Total Spending During the Validity Period**: The sum of all valid orders within the validity period you set (e.g., the past 365 days).

     ![](../../../assets/images/EC-後台-會員-VIP設定-新增會員層級02.en.png)

=== "Enterprise Edition"

     1. Setting the **Membership Level Validity Period**

      
         The **Membership Level Validity Period** is the **Membership Validity Period** for that level. The system will also use the spending records within this period to calculate whether a member meets the **Renewal eligibility**. 9. ****** ****** ****Expiration Date (Default):** Select the membership validity period in days from the drop-down menu.

11. ****** ****No Expiration Date:** Membership validity has no expiration date; the system will not check Renewal eligibility.

12. ****** ****** **Setting Renewal Eligibility Threshold****

13. Based on the previous step's setting for "Membership Level Validity Period," determine how to fill in the Renewal threshold:

14. ****** ****Expiration Date (Default):** **Please be sure to fill in the Renewal threshold.** If no Renewal threshold is set, the system will not perform Renewal eligibility checks when the membership expires, and the member will lose VIP status. 15 - **Unlimited**: The Renewal threshold can be left blank (the system will not perform an Renewal check, and the Renewal condition threshold will not take effect).

16 - Set Threshold:

17 - **Single Transaction Amount**: The amount a customer reaches in a single checkout within the validity period you set.

18 - **Total Transactions within the Validity Period**: The sum of all valid orders within the validity period you set.

19 - !!! tip "Creating a Permanent Renewal Mechanism"

20 - **Setting Method**: Set the Renewal period to **Unlimited**.

21 - **Operation Method**: The system will not initiate an **Expiration Renewal Check** for this level. Once a member has upgraded to this level using Upgrade, they will not be downgraded by the system due to an Renewal check.

          
        :lucide-triangle-alert: If a member generates an invalid order (e.g., order cancellation or return), the Downgrade mechanism will still be triggered for screening, and the member may still be subject to Downgrade processing.

    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-會員-VIP設定-新增會員層級03.png)

        
  
!!! note "Judgment Priority"

     If you set both "single" and "cumulative" thresholds, the system will use the result that is **most beneficial to the consumer** for Upgrade judgment.
