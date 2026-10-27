---
title: "Upgrade / Downgrade / Renewal Rules"
description: "An in-depth explanation of the new VIP system's rolling calculations, real-time trigger evaluations, and Downgrade lookback logic to help merchants develop a precise understanding of member operations."
created: 2026-01-23 00:00
last_modified: 2026-06-22 11:15
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
permalink: "https://help.cyberbiz.io/ec/members/vip/vip-upgrade-downgrade-renewal-rules.en/"
comments: false
search:
  exclude: false
icon: lucide/crown
hide: []
---
# Upgrade / Downgrade / Renewal Rules

## Execution Rules

### Upgrade Mechanism

*   **Takes Effect Immediately**: The member's level changes as soon as the requirements are met, and the benefits are available immediately.
*   **Validity Period Calculation**: The VIP start date displayed on the storefront is calculated from the day after the Upgrade date.
*   **Cross-Level Upgrade**:

    === "Crossing Levels Within the Same Group"

        Assume the **All VIP** group has three levels: Gold Member (Lv1), Platinum Member (Lv2), and Diamond Member (Lv3).

        If a Gold Member makes a single high-value purchase and directly Upgrade to Diamond Member, the reward issuance logic depends on your admin settings:

        - - **Admin Path**: Members VIP Settings > Edit VIP > Benefit Settings Tab
        - **Feature Location**: In the **Upgrade Gift Setting** section, turn on "Whether to Issue Gifts for All Intermediate Levels When Upgrade Crosses Levels."
            - On: The member receives both the Platinum Member and Diamond Member Upgrade gifts.
            - Off: The member only claims the Upgrade gift for the target level, Diamond Member.

    === "Cross-Group Upgrade"

        Assume the system has two separate groups: **All VIP** and **High-Value VIP**.

        The member is originally at "All VIP (Level 1)" and has the "High-Value VIP" Tags, but remains at All VIP because they have not met the "High-Value VIP" Upgrade threshold.

        When a high-value purchase makes the member eligible for both "All VIP (Level 2)" and "High-Value VIP (Level 1)," the member is upgraded across groups to "High-Value VIP (Level 1)" and only claims the Upgrade gift for "High-Value VIP (Level 1)." The system does not retroactively issue rewards for other All VIP levels.


### Downgrade Mechanism

*   **Immediate Adjustment**: When an order becomes invalid, the system recalculates immediately. If the remaining amount is insufficient, the system performs Downgrade.
*   **Retroactive Recalculation**: The validity period after Downgrade is recalculated based on the date of the member's **last valid order**.
*   **Benefits Are Not Reclaimed**: After Downgrade, the system **does not automatically deduct** any issued Upgrade gifts or bonus points.

### Renewal Mechanism

When a VIP validity period expires, the system evaluates the member's activity during that period to determine whether to renew or downgrade the membership.

*   **Evaluation Time**: The evaluation runs automatically at 00:00 on the day after the VIP validity period ends.
*   **Calculation Start**: The Renewal amount begins accumulating on the **day after Upgrade**. The order that triggered Upgrade is not included.
*   **Retain the Best Level**: The system first checks whether the member meets the VIP level's Renewal requirements. If so, Renewal succeeds. Otherwise, the system compares the Renewal settings for all store-wide VIP levels and applies the highest eligible level as the Renewal result.
*   **Return to Regular Member**: If the member does not meet any VIP threshold, their status returns to Regular Member.


## How To Perform Upgrade / Downgrade / Renewal

When planning a VIP program, consider two questions:

1.  **Look Back**: How far back should the system calculate purchase records? (Lookback period)
2.  **Plan Ahead**: After Upgrade or Renewal, how long should VIP status remain valid? (Validity period)

These two considerations are configured differently by plan:

### Comparison Of Plan Settings

| Your Consideration | System Logic | Other Plans | Enterprise Plan |
| :--- | :--- | :--- | :--- |
| **Look Back** | Number of days to look back | **Member Validity Period** | Upgrade: **Upgrade Condition Calculation Period**<br>續會：**Member Level Validity Period** |
| **Plan Ahead** | Number of days to extend | **Member Validity Period** | **Member Level Validity Period** |
| **Configuration** | - | Uses one number of days for both periods | Allows separate settings for the lookback and validity periods |



### How Each Mechanism Calculates Periods

Now that you understand the field mappings, see how the system selects time periods for different actions:

=== "Other Plans"

    **The logic is straightforward: configure one number of days for both periods.**

    The number of days set for "Member Validity Period" is both how far back the system looks and the validity period granted after Upgrade.

    | Action | How Far Back Does the System Look? | How Long Is the Validity Period After Upgrade? |
    | :--- | :--- | :--- |
    | **Upgrade / Downgrade** | Member Validity Period | Member Validity Period |
    | **Renewal** | Member Validity Period | Member Validity Period |

=== "Enterprise Plan"

    **The logic is flexible: configure the lookback and validity periods separately.**

    For example, the system can look back one year (365 days) but grant a validity period of only six months (180 days) after Upgrade.

    | Action | How Far Back Does the System Look? | How Long Is the Validity Period After Upgrade? |
    | :--- | :--- | :--- |
    | **Upgrade / Downgrade** | Upgrade Requirement Calculation Period | Member Level Validity Period |
    | **Renewal** | **Membership Level Validity Period** | Member Level Validity Period |



### Upgrade Example

=== "Other Plans"

      A member places a valid order on 2020/04/01. The system must determine whether the member meets the "Gold Card" Upgrade requirements.

      **Prerequisites**

      - Upgrade threshold: Cumulative purchases of at least 10,NT$000.
      - Member validity period: 360 days.

      **System Evaluation Steps**

      1.  **Trigger Event**: A valid order is placed on 2020/04/01.
      2.  **Lookback Period**: The system looks back 360 days from 2020/04/01. The calculation period is 2019/04/07–2020/04/01. It checks whether total purchases during this period are ≧ 10,NT$000.
      3.  **Calculate New Validity Period**: If the requirements are met, the 360-day period starts on 2020/04/01. The new expiration date is extended to 2021/03/27.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip04.png)

=== "Enterprise Plan"

    A member places a valid order on 2026/05/01. The system must determine whether the member meets the "Gold Card" Upgrade requirements.

    **Prerequisites**

    *   Upgrade threshold: Cumulative purchases of at least 10,NT$000.
    *   Upgrade requirement calculation period: 365 days (lookback period).
    *   Member level validity period: 180 days (new benefit period).

    **System Evaluation Steps**

    1.  **Trigger Event**: A valid order is placed on 2026/05/01.
    2.  **Lookback Period**: The system looks back 365 days from 2026/05/01. The calculation period is 2025/05/01–2026/05/01. It checks whether total purchases during this period are ≧ 10,NT$000.
    3.  **Calculate New Validity Period**: If the requirements are met, the 180-day period starts on 2026/05/01.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-升等機制01.png)


### Downgrade Example

=== "Other Plans"

    A member has an "invalid order" (such as a full-order return) on 2021/05/06. The system must reevaluate the member level.

    **Prerequisites**

    *   Member level threshold: Cumulative purchases of 10,NT$000 must be maintained during the lookback period.
    *   Member validity period: 360 days.

    **System Evaluation Steps**



    1.  **Trigger Event**: An order becomes invalid on 2021/05/06, so its amount is deducted from the cumulative total. The member's last valid order was placed on 2026/04/30.
    2.  **Lookback Period**: The system looks back 30 days from 2021/04/30. The calculation period is 2021/04/01–2021/04/30. It checks whether total purchases during this period are ≧ 10,NT$000. If the total falls below the threshold after the returned amount is deducted, the member is downgraded.
    3.  **Set the New Level Validity Period**: The system downgrades the customer to VIP1 and recalculates the validity period from the last valid order (the 4/30 order). The new expiration date is 2021/05/31.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip23-2.png)


=== "Enterprise Plan"

    A member has an "invalid order" (such as a full-order return) on 2026/05/15. The system must reevaluate the member level.

    **Prerequisites**

    *   Member level threshold: Cumulative purchases of 10,NT$000 must be maintained during the lookback period.
    *   Upgrade requirement calculation period: 365 days (lookback period).
    *   Member level validity period: 180 days (new benefit period).

    **System Evaluation Steps**

    1.  **Trigger Event**: An order becomes invalid on 2026/05/15, so its amount is deducted from the cumulative total. The member's last valid order was placed on 2026/05/01.
    2.  **Lookback Period**: The system looks back 365 days from 2026/05/01. The calculation period is 2025/05/01–2026/05/01. It checks whether total purchases during this period are ≧ 10,NT$000. If the total falls below the threshold after the returned amount is deducted, the member is downgraded.
    3.  **Set the New Level Validity Period**: The downgraded level begins a 180-day validity period on 2026/05/01.

    ![Create All VIP Program](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-降等機制01.png)

### Renewal Example

=== "Other Plans"

    The member level was scheduled to expire on 2021/02/28. The system automatically performs the Renewal evaluation on 2021/03/01, the day after expiration.

    **Prerequisites**

    *   VIP level Renewal threshold: Cumulative purchases of at least 1,NT$500.
    *   MEMBER level Renewal threshold: Cumulative purchases of at least NT$500.
    *   Member validity period: 360 days (lookback period / new benefit period).

    **System Evaluation Steps**

    1.  **Trigger Event**: The member validity period expires on 2021/03/01, and the system reevaluates the member validity period.
    2.  **Lookback Period**: The system calculates purchases during the member validity period, from 2020/03/06 to 2021/03/01. It checks whether the customer met the Renewal threshold during these 360 days.
    3.  **Multi-Level Comparison and Extension**:
        *   **Check the VIP Threshold**: The customer's cumulative purchases are NT$800, below the 1,NT$500 threshold, so Renewal fails.
        *   **Check the MEMBER Threshold**: The customer's cumulative purchases are NT$800, which meets the NT$500 threshold, so Renewal succeeds.
    4.  **Result**: The system automatically Renewal the customer to the **MEMBER** level. The new validity period starts on 2021/03/01 and is extended by 360 days.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip09.png)

=== "Enterprise Plan"

    The member level was scheduled to expire on 2026/04/30. The system automatically performs the Renewal evaluation on 2026/05/01, the day after expiration.

    **Prerequisites**

    *   Member level threshold: Cumulative purchases of 10,NT$000 must be maintained during the lookback period.
    *   Member level validity period (Y): 180 days (lookback period / new benefit period).

    **System Evaluation Steps**

    1.  **Trigger Event**: The member validity period expires on 2026/04/30 and is reevaluated on 2026/05/01.
    2.  **Lookback Period**: Unlike the previous two mechanisms, Renewal only calculates purchases made during the member's current level validity period, from 2025/11/02 to 2026/05/01. It checks whether cumulative purchases during these 180 days meet the threshold.
    3.  **Extend the Validity Period**: If the requirements are met, the validity period is extended by 180 days (Y) from the original expiration date.

    ![Create All VIP Program](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-續會機制01.png) 