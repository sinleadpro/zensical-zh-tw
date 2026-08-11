---
title: 升等 / 降等 / 續會規則
description: 深度解析新版 VIP 系統的滾動式計算、即時觸發判定以及升降等回溯邏輯，協助商家建立精準的會員營運觀念。
created: 2026-01-23 00:00
last_modified: 2026-06-22 11:15
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
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/crown
hide: []
---
# Upgrade / Downgrade / Renewal Rules

## Execution rules

### Upgrade Mechanism
* **Immediate Effect:** Upon reaching the required level, your current VIP level will change immediately, and the benefits are available for immediate use.

* **Validity Calculation:** The VIP start date displayed on the front end is calculated from the "next day" of the Upgrade activation date.

* **Cross-Level Upgrade:**

     === "Cross-Level Within the Same Group"

         Assumption: The store-wide VIP group has three levels: Gold Member (Lv1), Platinum Member (Lv2), and Diamond Member (Lv3).

If a member was originally a "Gold Member" and made a large single purchase that directly upgrades them to a "Diamond Member," the reward distribution logic will depend on your backend settings:

         - **Backend Path**: Members > VIP Settings > Edit VIP > Discount Settings tab

         - **Function Location**: In the **Upgrade Gift Settings** section, enable "Whether to accumulate Upgrade gifts when crossing levels."

             - Enabled: The member will receive both the "Platinum Member" and "Diamond Member" Upgrade gifts simultaneously.

             - Disabled: The member will only receive the Upgrade gift for the target "Diamond Member" level.

     === "Cross-Group Upgrade"

         Assume the system has two independent groups: **store-wide VIP** and **VIP**.

         If a member was originally in "store-wide VIP (Level 1)" and had the "VIP" tag, but remained in store-wide VIP because they did not meet the "VIP" Upgrade threshold,

        

         When a large purchase occurs, making the member meet the thresholds for both "store-wide VIP (Level 2)" and "VIP (Level 1)", the member will be upgraded to "VIP (Level 1)" across groups and will only receive the "VIP (Level 1)" Upgrade gift; the system will not issue rewards for other store-wide VIP levels.

### Downgrade Mechanism
* **Instant Correction:** When an order becomes invalid, the system immediately recalculates. If the remaining amount is insufficient, Downgrade will be executed.

* **Recalculation Retrospectively:** The validity period after Downgrade will be recalculated from the date of the member's **last valid order**.

* **No Reclaim of Benefits:** Upgrade gifts or bonus points already given will **not be automatically deducted** after Downgrade.

### Renewal Mechanism
When a VIP membership expires, the system will evaluate the member's performance during that period to decide whether to renew or downgrade.

* **Determination Timing:** Automatically performed at 00:00 the day after the VIP membership expires.

* **Calculation Start Date:** Renewal balances only begin accumulating from the day after Upgrade; the current Upgrade order is not included.

* **Optimal Retention:** Prioritizes checking if the VIP Renewal requirements for that tier are met. If met, the Renewal is successfully applied. If not, it continues to compare the Renewal settings for all VIP levels of store-wide, prioritizing the highest tier that meets the requirements as the Renewal result.

* **Revert to Regular Membership:** If all VIP requirements are not met, the member's status will revert to regular membership.

## How to execute Upgrade / Downgrade / Renewal
When planning a VIP system, two questions need to be considered:

1. **Looking Back:** How far back in time should the system calculate consumption records? (Going backward)

2. **Considering the Future:** How long can VIP status be maintained after Upgrade or Renewal? (Validity Period)

These two considerations are set up in different versions as follows:

### Version setting differences comparison
| Your Considerations | System Logic | Other Versions | Enterprise Edition |

| :--- | :--- | :--- | :--- |

| **Looking Back** | Number of Days to Reverse | **Membership Validity** | Upgrade: **Upgrade Condition Calculation Period** <br>Renewal: **Membership Tier Validity Period** |

| **For the Future** | Number of Days to Extend | **Membership Validity** | **Membership Tier Validity Period** |

| **Setting Features** | - | Set a Unique Number of Days | Can be Set Separately for Reverse Validity and Validity Period |

### Different operational methods
Having understood the field correspondence, let's look at how the system calculates time when performing different actions:

=== "Other Versions"

     **Simplest logic:** Set a number of days, applicable to both systems.

    : The number of days you set in "Member Validity" determines how many days the system looks back on. The same number of days is given after Upgrade.

     | Perform Action | How long does the system look back? | How long is the validity period after Upgrade? |     | :--- | :--- | :--- |

    | **Upgrade / Downgrade** | Membership Validity | Membership Validity |

    | **Renewal** | Membership Validity | Membership Validity |

=== "Enterprise Edition"

    ** Most flexible logic: Retrospective time and validity period can be set separately. **

     For example: You can have the system look back one year (365 days), but after Upgrade, only a six-month validity period (180 days) is given.

    | Execute Action | How long does the system look back? | How long is the validity period after Upgrade? |     | :--- | :--- | :--- |

    | **Upgrade / Downgrade** | Upgrade Calculation Period | Membership Level Validity Period |

    | **Renewal** | **Membership Level Validity Period** | Membership Level Validity Period |

### Upgrade Example
=== "Other Versions"

An        member placed a valid order on April 1, 2020. The system needs to determine if the member meets the "Gold Card" Upgrade requirements.

       **Prerequisites**

       - Upgrade Threshold: Accumulated spending of 10,000 RMB or more.

       - Membership Validity: 360 days.

       **System Judgment Steps**

       1. **Triggering Event**: A valid order was placed on April 1, 2020.

       2. **Backtracking Period**: Counting back 360 days from April 1, 2020, the calculation period is from April 7, 2019 to April 1, 2020. Check if the total spending within this period is ≥ 10,000 yuan.

      3. **Calculate the new validity period**: If it meets the requirement, the new validity period will be extended to 2021/03/27, 360 days from 2020/04/01.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip04.png)

=== "Enterprise Edition"

     If a member places a valid order on 2026/05/01, the system needs to determine if they meet the "Gold Card" Upgrade requirements.

      

     **Prerequisites**

    * Upgrade Threshold: Accumulated spending of 10,000 yuan or more.

    * Upgrade Calculation Period: 365 days (look-back period).

    * Membership Tier Validity Period: 180 days (New Benefit Period).

     **System Judgment Steps**

     1. **Trigger Event**: A valid order was established on 2026/05/01.

     2. **Look-back Interval**: Count back 365 days from 2026/05/01, the calculation interval is 2025/05/01 ~ 2026/05/01. Check if the total consumption within this interval is ≥ 10,000 yuan.

     3. **Calculate New Validity Period**: If it meets the criteria, then calculate 180 days from 2026/05/01.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-Upgrade機制01.png)### Downgrade Example
=== "Other Versions"

     members who placed an "invalid order" (e.g., a full return) on 2021/05/06 will have their membership level reassessed by the system.

     **Prerequisites**

    * Membership level threshold: A cumulative spending of NT$10,000 must be maintained during the retrospective period.

    * Membership validity: 360 days.

     **System Judgment Steps**

    

     1. **Triggering Event**: An invalid order was placed on 2021/05/06, resulting in the deduction of the original cumulative amount. The last valid order placed by the retrospective member is on 2026/04/30.

    2. **Backtracking Period**: Count back 30 days from April 30, 2021, calculating the period from April 1, 2021 to April 30, 2021. Check if the total spending within this period is ≥ 10,000 NTD. If, after deducting refunds, the total amount is below the threshold, a downgrade will be applied.

    3. **Setting a New VIP Level Expiry Date**: The system will downgrade the customer back to VIP1 and recalculate the expiry date from the "last valid order (i.e., the order placed on April 30th)". The new expiry date will be adjusted to May 31, 2021.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip23-2.png)

=== "Enterprise Edition"

     If a member has an "invalid order" (e.g., a full return) on 2026/05/15, the system needs to reassess the member's level.

  

    **Prerequisites**

    * Membership level threshold: Accumulated spending of NT$10,000 must be maintained during the retrospective period.

    * Upgrade Calculation period: 365 days (retrospective period).

    * Membership level validity period: 180 days (new benefit period).

    **System Judgment Steps**

     1. **Triggering Event**: An invalid order was established on 2026/05/15, resulting in the deduction of the original accumulated amount. The last valid order placed by the member is dated May 1, 2026.

    2. **Backtracking Period**: Counting back 365 days from May 1, 2026, the calculated period is May 1, 2025 to May 1, 2026. The total spending within this period is checked to see if it is ≥ 10,000 RMB. If, after deducting refunds, the total amount is below the threshold, a downgrade will be applied.

    3. **Setting the New Level Validity Period**: The downgraded level will be valid for 180 days starting from May 1, 2026.

    ![Establish store-wide VIP System](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-Downgrade機制01.png)

### Renewal Example
=== "Other Versions"

The      membership level was originally scheduled to expire on February 28, 2021. The system automatically performed the Renewal check the following day, March 1, 2021.

     **Prerequisites**

    * VIP Level Renewal Threshold: Accumulated spending of 1,500 RMB.

    * MEMBER Level Renewal Threshold: Accumulated spending of 500 RMB.

    * Membership Validity: 360 days (retroactive period / new benefits period).

     **System Check Steps**

     1. **Triggering Event**: Membership expires on March 1, 2021; the system re-checks membership validity.

    2. **Backtracking Period**: Calculates spending within the membership period, i.e., March 6, 2020 to March 1, 2021. Checks whether the customer has met the Renewal threshold within these 360 ​​days.

    3. **Multi-level Comparison and Extension**:

        * **Check VIP Threshold**: If the customer's accumulated spending is 800 yuan, which is less than the 1,500 yuan threshold, Renewal fails.

        * **Check MEMBER Threshold**: If the customer's accumulated spending is 800 yuan, which is more than the 500 yuan threshold, Renewal succeeds.

    4. **Effective Result**: The system will automatically upgrade the customer's Renewal to the **MEMBER** level, with the new validity period extended for 360 days starting from 2021/03/01.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip09.png)

=== "Enterprise Edition"

     The membership level was originally scheduled to expire on 2026/04/30. The system will automatically perform the Renewal determination the day after the expiration date, 2026/05/01.

      

     **Prerequisites**

    * This membership level threshold: A cumulative spending of NT$10,000 must be maintained during the rollback period.

    * Membership level validity period (Y): 180 days (rollback period / new benefits period).

     **System Judgment Steps**

     1. **Triggering Event**: Membership expires on April 30, 2026; membership validity is reassessed on May 1, 2026.

     2. **Backtracking Period**: Unlike the previous two, Renewal only calculates consumption within the "valid period of this level," i.e., November 2, 2025 to May 1, 2026, checking whether the accumulated consumption within these 180 days meets the requirements.

     3. **Extend Validity Period**: If it meets the requirements, the validity period is extended by 180 days (Y) from the original expiration date.

    ![Establish store-wide VIP System](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-Renewal機制01.png)
