---
title: "Create Exclusive VIP Groups"
description: "Use the VIP group tags feature to bind tags to specific customer segments and set exclusive VIP rules for segmented customer management and targeted marketing."
created: 2026-01-23 00:00
last_modified: 2026-06-30 12:30
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 有效訂單連結
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
  - 建立 VIP 群組標籤
  - 設定標籤排序
features:
  - VIP 制度
  - VIP 群組標籤
prerequisites: []
related: []
tags:
  - VIP
  - "Member Tags"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > VIP 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8621
  - https://www.cyberbiz.io/support/?p=32733
permalink: "https://help.cyberbiz.io/ec/members/vip/create-exclusive-vip-groups.en/"
comments: false
search:
  exclude: false
icon: lucide/users
hide: []
---
# Create Exclusive VIP Groups

Use the VIP group tags feature to link tags to specific customer segments and set exclusive VIP rules for segmented customer management and targeted marketing.
{ .subtitle }

![](../../../assets/images/EC-後台-會員-VIP設定-新增VIP群組01.en.png){ .hero-page }

## About This Feature { #intro-vip-groups }

The "VIP Group Tags" feature lets merchants apply a set of tier rules separate from the "All VIP" rules to members with a specific **member tag**. This is useful for managing specific customer segments, such as employees, KOLs, and high-value customers.

### VIP Type Differences { #intro-vip-groups-types }

1.  **All VIP**: Applies to all members who are not assigned to a specific group.
2.  **VIP Group**: Links a specific **member tag** and is available only to members with that tag.


## Steps { #operate-vip-groups }

### Step 1: Create a VIP Group and Bind a Tag { #operate-vip-groups-create }

1. Log in to the admin panel and go to **Customer Management > VIP Settings**.
2. Click the **Version In Editing** tab.
3. Click **New VIP Group**.
4. From the **Bind member tags** dropdown menu, select a previously created member tag.
5. Set the tier thresholds and benefits for the group.

### Step 2: Adjust Group Order { #operate-vip-groups-sort }

1. On the VIP Settings list page, find the ordering controls on the right.
2. Drag the groups or adjust their numbers so that their priorities match your business strategy.
3. Click **Save Order**.


## How It Works and Evaluation Rules { #specs-vip-groups }

### 1. Recalculation Triggers { #specs-vip-groups-trigger }
The system recalculates a member's VIP tier in the following situations:

*   **Tag Changes**: When a merchant **adds** or **removes** a tag linked to a VIP group for a member.
*   **Valid Order**: When the member places a new valid order.

### 2. Priority and Order { #specs-vip-groups-priority }
If a member has multiple customer tags, and these tags are bound to different VIP groups:

*   **Order Determines Priority**: The system uses the **order** of the VIP list in the admin panel.
*   **Evaluation Logic**: The system evaluates groups upward from the **bottom** of the list. The first eligible group determines the rules that apply to the member.
*   **Recommendation**: Place the group with the strictest requirements and highest benefits at the bottom of the list.

### 3. Determine Member Eligibility { #specs-vip-groups-eligibility }
The system checks the upgrade requirements for the lowest tier, or entry tier, in the VIP group.

- **Meets the Threshold:** The member formally enters the VIP group and receives the corresponding tier based on their spending. The member can be upgraded directly to the highest tier.
- **Does Not Meet the Threshold:** Even if the member has the tag, the system determines that they are not eligible for the group's VIP status. The member retains their existing status, such as All VIP or regular member, until the next trigger event when their spending meets the threshold.

!!! tip "Key Concept"
    A tag only grants eligibility for an **entry ticket**, not a **direct pass**. The member must have the tag and also meet the group's spending threshold before the system formally upgrades them to a VIP in that group.



## Calculation Rules When Adding or Removing a Tag { #specs-vip-groups-tags }

When a merchant manually adjusts a member's tags, the system uses the following calculation logic:

| Action | Calculation Logic | Validity Start Date |
| :--- | :--- | :--- |
| **Add tags** | Treated as a **valid order** event. The system looks back from the current time to evaluate the threshold within the validity period. | Starts on the **date the tag is added**. |
| **Remove tags** | Treated as an **invalid order** event. The system looks back to the most recent valid event for the calculation. | Starts on the date of the most recent valid event. |

!!! warning "Risks of Manual Adjustments"
    Do not frequently "remove a tag and then add it back" for members to test the logic. Adding a tag triggers a new lookback calculation. If the member's spending is insufficient during the new lookback period, the member may be unexpectedly downgraded.



## FAQ { #faq-vip-groups }

??? quote "Why does a member with a tag not enter the corresponding VIP group?"
    Check whether the member meets the upgrade threshold for the "lowest tier" in the VIP group. Even with a bound tag, the member must meet the spending threshold, either for a single purchase or cumulative spending, before they are formally upgraded.

??? quote "Can I delete a tag that is currently used by a VIP group?"
    No. A tag can be deleted only when all of the following conditions are met: no customers use it, no products use it, **no VIP group is bound to it**, and no member-exclusive products use it.



