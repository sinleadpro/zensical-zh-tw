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

* **Cross-Level Upgrade Activation:**

* 0 === "Cross-Level Activation within the Same Group"

* 1 Assume the store-wide VIP group has three levels: Gold Member (Lv1), Platinum Member (Lv2), and Diamond Member (Lv3).

2. If a member was originally a "Gold Member" and directly upgraded to a "Diamond Member" through a single large purchase, the reward distribution logic will depend on your backend settings:

3. **Backend Path:** Member > VIP Settings > Edit VIP > Discount Settings tab

4. **Function Location:** In the **Upgrade Gift Settings** section, enable "Whether to accumulate Upgrade gifts when crossing levels."

5. **Enabled:** The member will receive both the "Platinum Member" and "Diamond Member" Upgrade gifts simultaneously.

6. **Disabled:** The member will only receive the Upgrade gift for the target "Diamond Member" level. 7. === "Cross-Group Upgrade"

8. Assume the system has two independent groups: **store-wide VIP** and **VIP**.

9. If a member was originally in "store-wide VIP (Level 1)" and has the "VIP" tag, but remains in store-wide VIP because they haven't met the "VIP" Upgrade threshold,

10.
11. When a large purchase occurs, making the member meet the thresholds for both "store-wide VIP (Level 2)" and "VIP (Level 1)", the member will be upgraded to "VIP (Level 1)" across groups and will only receive the "VIP (Level 1)" Upgrade gift. The system will not issue rewards for other store-wide VIP levels.

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

| **Looking Back** | Number of Days to Reverse | **Membership Validity** | Upgrade: **Upgrade Condition Calculation Period** 0 ≠ Renewal: **Membership Tier Validity Period** |

| **For the Future** | Number of Days to Extend | **Membership Validity** | **Membership Tier Validity Period** |

| **Setting Characteristics** | - | Set a uniform number of days | Can set separate values ​​for reverse and validity periods |

### Different operational methods
Having understood the field correspondence, let's look at how the system calculates time when performing different actions:

**12** "Other Versions"

**0** **Simplest logic: Set a number of days, applicable to both versions.**

**1** The number of days you set in "Member Validity" determines how many days the system looks back, and the same number of days will be given after Upgrade.

**2** | Perform Action | How long does the system look back? | How long is the validity period after Upgrade? |     | :--- | :--- | :--- |

    | **Upgrade / Downgrade** | Membership Validity Period | Membership Validity Period |

    | **Renewal** | Membership Validity Period | Membership Validity Period |

=== "Enterprise Edition"

     **Most Flexible Logic: Retrospective time and validity period can be set separately.**

     For example: You can have the system look back one year (365 days), but only give a six-month validity period (180 days) after Upgrade.

    | Execute Action | How long does the system look back? | How long is the validity period after Upgrade? |     | :--- | :--- | :--- |

    | **Upgrade / Downgrade** | Upgrade Calculation Period | Membership Level Validity Period |

    | **Renewal** | **Membership Level Validity Period** | Membership Level Validity Period |

### Upgrade Example
=== "Other Versions"

       If a member places a valid order on 2020/04/01, the system needs to determine if they meet the "Gold Card" Upgrade requirements.

       **Prerequisites**

       - Upgrade Threshold: Accumulated spending of 10,000 RMB or more.

       - Membership Validity: 360 days.

       **System Judgment Steps**

       1. **Triggering Event**: A valid order is placed on 2020/04/01.

       2. **Backtracking Period**: Counting back 360 days from 2020/04/01, the calculation period is 2019/04/07 ~ 2020/04/01. Check if the total spending within this period is ≥ 10,000 yuan.

9.3. **Calculation of New Validity Period**: If it meets the requirement, the new validity period will be extended from now until 2021/03/27, 360 days from 2020/04/01.

10. ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip04.png)

23. "Enterprise Edition"

11. If a member establishes a valid order on 2026/05/01, the system needs to determine if it meets the "Gold Card" Upgrade conditions.

12.

13. **Prerequisites**

14. * Upgrade Threshold: Accumulated spending of 10,000 yuan or more.

15. * Upgrade Condition Calculation Period: 365 days (retroactive period).     * Membership Tier Validity Period: 180 days (New Benefit Period).

    **System Judgment Steps**

    1. **Triggering Event**: A valid order was established on 2026/05/01.

    2. **Backtracking Interval**: Count back 365 days from 2026/05/01, calculating the interval as 2025/05/01 ~ 2026/05/01. Calculate whether the total consumption within this interval is ≥ 10,000 yuan.

    3. **Calculate New Validity Period**: If it meets the requirement, then calculate 180 days from 2026/05/01.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-Upgrade機制01.png)

### Downgrade Example
=== "Other Versions"

     If a member placed an "invalid order" (e.g., a full refund) on 2021/05/06, the system needs to reassess the member's level.

     **Prerequisites**

     * Membership Level Threshold: A cumulative spending of 10,000 yuan must be maintained during the retrospective period.

     * Membership Validity: 360 days.

     **System Judgment Steps**

    

     1. **Triggering Event**: An invalid order was placed on 2021/05/06, resulting in the deduction of the original cumulative amount. The last valid order placed by the retrospective member is on 2026/04/30.

9.2. **Backtracking Period**: Count back 30 days from April 30, 2021, calculating the period from April 1, 2021 to April 30, 2021. Check if the total spending within this period is ≥ 10,000 yuan. If, after deducting refunds, the total amount is below the threshold, a downgrade will be applied.

10.3. **Setting a New Level Validity Period**: The system will downgrade the customer back to VIP1 and recalculate the validity period from the "last valid order (i.e., the order on April 30th)," with the new expiration date adjusted to May 31, 2021.

11. ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip23-2.png)

24. "Enterprise Edition"

12. If a member places an "invalid order" (such as a full refund) on May 15, 2026, the system needs to re-evaluate the member's level. 13

14
**Prerequisites**

15
* Membership Level Threshold: A cumulative spending of 10,000 RMB must be maintained during the retrospective period.

16
* Upgrade Calculation Period: 365 days (Retrospective Period).

17
* Membership Level Validity Period: 180 days (New Benefits Period).

18
**System Judgment Steps**

19
1. **Triggering Event**: An invalid order was established on 2026/05/15, resulting in the deduction of the original cumulative amount. The last valid order established by the retrospective member was on 2026/05/01.

20. **Backtracking Period**: Count back 365 days from May 1, 2026, calculating the period from May 1, 2025 to May 1, 2026. Check if the total spending within this period is ≥ 10,000 yuan. If, after deducting refunds, the total amount is below the threshold, a downgrade will be applied.

21. **Setting the New Level Validity Period**: The downgraded level will be valid for 180 days starting from May 1, 2026.

22. [Establishing the store-wide VIP System](1)

### Renewal Example
=== "Other Versions"

     The original membership level was scheduled to expire on February 28, 2021. The system automatically performed the Renewal check the following day, March 1, 2021.

     **Prerequisites**

     * VIP Level Renewal Threshold: Accumulated spending of 1,500 RMB or more.

     * MEMBER Level Renewal Threshold: Accumulated spending of 500 RMB or more.

     * Membership Validity: 360 days (retroactive period / new benefit period).

     **System Check Steps**

     1. **Triggering Event**: The membership validity expired on March 1, 2021, and the system re-checked the membership validity.

9.2. **Backtracking Period**: Calculates spending within the membership period, i.e., March 6, 2020 to March 1, 2021. Checks whether the customer has met the Renewal threshold within these 360 ​​days.

10.3. **Multi-level Comparison and Extension**:

11. * **Check VIP Threshold**: If the customer's cumulative spending is 800 yuan, which is less than the 1,500 yuan threshold, Renewal fails.

12. * **Check MEMBER Threshold**: If the customer's cumulative spending is 800 yuan, which is more than the 500 yuan threshold, Renewal succeeds.

13.4. **Effective Result**: The system will automatically upgrade the customer's Renewal to the **MEMBER** level, with the new validity period extended for 360 days from March 1, 2021.

14. ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip09.png)

26. "Enterprise Edition"

15. The membership level was originally scheduled to expire on April 30, 2026. The system will automatically perform the Renewal determination on May 1, 2026, the day after the expiration date.

16.

17. **Prerequisites**

18. * Membership level threshold: A cumulative spending of NT$10,000 must be maintained during the retrospective period.

19. * Membership level validity period (Y): 180 days (retrospective period / new benefit period).

20. **System Judgment Steps**

21. **Triggering Event**: Membership expires on April 30, 2026; membership validity is reassessed on May 1, 2026.

22. **Backtracking Period**: Unlike the previous two, Renewal only calculates consumption within the "valid period of this level," i.e., November 2, 2025 to May 1, 2026, checking whether the accumulated consumption within these 180 days meets the requirements.

23. **Extension of Validity Period**: If it meets the requirements, the validity period is extended by 180 days (Y) from the original expiration date.

24. [Establishing the store-wide VIP System](1)
