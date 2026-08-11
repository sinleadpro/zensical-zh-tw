---
title: Promotion/Demotion/Membership Renewal Rules
description: This article provides an in-depth analysis of the new VIP system's rolling calculations, real-time trigger judgments, and backtracking logic for upgrades and downgrades, helping merchants establish a precise membership operation concept.
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
# Promotion/Demotion/Membership Renewal Rules

## Execution rules

### Promotion mechanism
* **Immediate Effect:** Upon reaching the required level, the VIP rank will change immediately, and the benefits are available instantly.

* **Validity Calculation:** The VIP start date displayed on the front end is calculated from the day after the upgrade date.

* **Cross-Level Upgrade:**

* 0 "Cross-Level within the Same Group"

Assuming the **All VIPs** group has three levels: Gold Member (Lv1), Platinum Member (Lv2), and Diamond Member (Lv3).

If a member was originally a "Gold Member" and upgraded directly to "Diamond Member" with a single large purchase, the reward distribution logic will depend on your backend settings:

- **Backend Path:** Members > VIP Settings > Edit VIP > Benefit Settings tab

- **Function Location:** In the **Upgrade Gift Settings** section, enable "Whether to accumulate upgrade gifts when crossing levels."

- **Enabled:** The member will receive both the "Platinum Member" and "Diamond Member" upgrade gifts simultaneously. - Closed: Members will only receive the upgrade gift for the target "Diamond Member" level.

=== "Cross-Group Upgrade"

Assume the system has two independent groups: **All-Entry VIP** and **High-End VIP**.

If a member is originally at "All-Entry VIP (Level 1)" and has the "High-End VIP" tag, but remains at "All-Entry VIP" because they haven't met the upgrade threshold for "High-End VIP",

When a large purchase occurs, making the member eligible for both "All-Entry VIP (Level 2)" and "High-End VIP (Level 1)", the member will upgrade to "High-End VIP (Level 1)" across groups and will only receive the "High-End VIP (Level 1)" upgrade gift. The system will not reissue rewards for other levels of "All-Entry VIP".

### Downgrade mechanism
* **Instant Correction:** When an order becomes invalid, the system immediately recalculates. If the remaining balance is insufficient, a downgrade will be implemented.

* **Recalculation Retrospectively:** The validity period after downgrading will be recalculated from the date of the member's **last valid order**.

* **No Reclaim of Benefits:** Upgrade gifts or bonus points already given will **not be automatically deducted** after a downgrade.

### Renewal Mechanism
When a VIP membership expires, the system will evaluate the member's performance during that period to decide whether to renew or downgrade.

* **Determination Timing:** Automatically performed at 00:00 the day after the VIP membership expires.

* **Calculation Start Date:** Renewal fees only begin accumulating from the **day after upgrade**; the order placed at the time of the upgrade is not included.

* **Optimal Retention:** Prioritizes checking if the VIP renewal conditions for that tier are met. If met, renewal is successful. If not, it will continue comparing the renewal settings of all VIP levels across the entire system and prioritize applying the highest tier that meets the conditions as the renewal result.

* **Revert to Regular Membership:** If all VIP requirements are not met, the member's status will revert to regular membership.

## How to perform promotion/demotion/renewal of membership
When planning a VIP system, two questions need to be considered:

1. **Looking Back:** How far back in time should the system calculate consumption records? (Going backward)

2. **Considering the Future:** How long can VIP status be maintained after upgrading or renewing? (Validity period)

These two considerations are set up in different versions as follows:

### Version setting differences comparison
| Your Considerations | System Logic | Other Versions | Enterprise Edition |

| :--- | :--- | :--- | :--- |

| **Looking Back** | Number of Days to Rewind | **Membership Validity** | Upgrade: **Upgrade Calculation Period** Renewal: **Membership Tier Validity Period** |

| **For the Future** | Number of Days to Extend | **Membership Validity** | **Membership Tier Validity Period** |

| **Setting Features** | - | Set a Unique Number of Days | Can be Set Separately for Rewind and Validity Period |

### Different operational methods
Having understood the field correspondence, let's look at how the system calculates time when performing different actions:

**0** "Other Versions"

**Simplest Logic: Set a number of days, applicable to both.**

The number of days you set in "Membership Validity" determines how many days the system looks back, and the same number of days of validity are given after upgrading.

| Action Execution | How long does the system look back? | How long is the validity period after upgrading? |

| :--- | :--- | :--- |

| **Upgrade / Downgrade** | Membership Validity | Membership Validity |

| **Renewal** | Membership Validity | Membership Validity |

**1** "Enterprise Edition"

**Most Flexible Logic: Backtracking time and validity period can be set separately.**

For example: You can have the system look back for one year (365 days), but only give a six-month validity period (180 days) after upgrading.

| Action Execution | How long does the system look back? | How long is the membership level valid after upgrading? |

| :--- | :--- | :--- |

| **Upgrade/Downgrade** | Calculation Period for Upgrade Requirements | Validity Period of Membership Level |

| **Renewal** | **Validity Period of Membership Level** | Validity Period of Membership Level |

### Upgraded Example
=== "Other Versions"

A member placed a valid order on April 1, 2020. The system needs to determine if this meets the requirements for upgrading to "Gold Card".

**Prerequisites**

- Upgrade Threshold: Accumulated spending of 10,000 RMB or more.

- Membership Validity: 360 days.

**System Judgment Steps**

1. **Triggering Event**: A valid order was placed on April 1, 2020.

2. **Backtracking Period**: Counting back 360 days from April 1, 2020, the calculated period is April 7, 2019 to April 1, 2020. Check if the total spending within this period is ≥ 10,000 RMB.

3. **Calculation of New Validity Period**: If eligible, the new validity period will be extended from April 1, 2020 to March 27, 2021, after a 360-day period.


![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip04.png)

=== "Enterprise Edition"

If a member places a valid order on May 1, 2026, the system needs to determine if they meet the requirements for upgrading to "Gold Card".

**Prerequisites**

* Upgrade Threshold: Accumulated spending of 10,000 RMB or more.

* Upgrade Calculation Period: 365 days (retrospective period).

* Membership Level Validity Period: 180 days (new benefits period).

**System Judgment Steps**

1. **Triggering Event**: Valid order placed on May 1, 2026.

2. **Backtracking Period**: Count back 365 days from May 1, 2026, calculating the period from May 1, 2025 to May 1, 2026. Determine if the total consumption within this period is ≥ 10,000 yuan.

3. **Calculate the New Validity Period**: If it meets the requirement, calculate 180 days from May 1, 2026.

![](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-升等機制01.png)

### Downgraded examples
=== "Other Versions"

If a member placed an "invalid order" (e.g., a full refund) on 2021/05/06, the system needs to reassess the member's level.

**Prerequisites**

* Membership level threshold: Accumulated spending of 10,000 RMB must be maintained during the retrospective period.

* Membership validity: 360 days.

**System Judgment Steps**

1. **Triggering Event**: An invalid order was placed on 2021/05/06, resulting in the deduction of the original accumulated amount. The last valid order placed by the member during the retrospective period is 2026/04/30.

2. **Retrospective Period**: Counting back 30 days from 2021/04/30, the calculated period is 2021/04/01 to 2021/04/30. Check if the total spending within this period is ≥ 10,000 RMB. If the total amount after deducting the refund amount is lower than the threshold, a downgrade will be applied.

3. **Setting a New VIP Level Validity Period**: The system will downgrade the customer back to VIP1 and recalculate the validity period from the "last valid order (i.e., the order on April 30th)". The new expiration date will be adjusted to 2021/05/31.

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip23-2.png)

=== "Enterprise Edition"

If a member has an "invalid order" (such as a full refund) on 2026/05/15, the system will need to reassess the member's VIP level.

**Prerequisites**

* VIP level threshold: Accumulated spending of NT$10,000 must be maintained during the rollback period.

* Upgrade calculation period: 365 days (rollback period).

* VIP level validity period: 180 days (new benefit period).

**System Judgment Steps**

1. **Triggering Event**: An invalid order was placed on May 15, 2026, resulting in the deduction of the accumulated amount. The last valid order placed by the member is traced back to May 1, 2026.

2. **Tracing Period**: Counting back 365 days from May 1, 2026, the calculated period is May 1, 2025 to May 1, 2026. The total spending within this period is checked to see if it is ≥ 10,000 yuan. If, after deducting the refund amount, the total amount is below the threshold, a downgrade is applied.

3. **Setting the New Level Validity Period**: The downgraded level will be valid for 180 days starting from May 1, 2026.

![Establish a VIP System for the Entire Store](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-降等機制01.png)

### Renewal Example
=== "Other Versions"

The original membership level was scheduled to expire on February 28, 2021. The system automatically performed a renewal check on March 1, 2021, the day after the expiration date.

**Prerequisites**

* VIP Level Renewal Threshold: Accumulated spending of NT$1,500.

* MEMBER Level Renewal Threshold: Accumulated spending of NT$500.

* Membership Validity: 360 days (retroactive period / new benefits period).

**System Judgment Steps**

1. **Trigger Event**: The membership validity expires on March 1, 2021, and the system re-evaluates the membership validity.

2. **Retroactive Period**: Calculate the spending within the membership validity period, i.e., March 6, 2020 ~ March 1, 2021. Check whether the customer has met the renewal threshold within these 360 ​​days.

3. **Multi-level Comparison and Extension**:

* **VIP Threshold Check**: Customer's accumulated spending is 800 RMB, below the 1,500 RMB threshold, renewal fails.

* **MEMBER Threshold Check**: Customer's accumulated spending is 800 RMB, above the 500 RMB threshold, renewal succeeds.

4. **Effective Result**: The system automatically renews the customer's membership to the **MEMBER** level, with the new validity period extended for 360 days from 2021/03/01.

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/05/new_vip09.png)

=== "Enterprise Edition"

The membership level was originally scheduled to expire on 2026/04/30. The system automatically performed the renewal check on 2026/05/01, the day after the expiration date.

**Prerequisites**

* This membership level threshold: Accumulated spending of 10,000 RMB must be maintained during the rollback period. * Membership Tier Validity Period (Y): 180 days (Retroactive Period / New Benefit Period).

**System Judgment Steps**

1. **Trigger Event**: Membership expires on April 30, 2026; membership validity is reassessed on May 1, 2026.

2. **Retroactive Period**: Unlike the previous two, renewal only calculates consumption within the "validity period of this tier," i.e., November 2, 2025 ~ May 1, 2026, checking whether accumulated consumption within these 180 days meets the requirements.

3. **Extension Period**: If it meets the requirements, the membership will be extended for 180 days (Y) from the original expiration date.

![Establish a VIP system for the entire store](https://www.cyberbiz.io/support/wp-content/uploads/圖示範例-EC-會員-VIP-續會機制01.png)
