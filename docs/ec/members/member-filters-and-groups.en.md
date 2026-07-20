---
title: 篩選器與會員分群
description: 透過多維度條件精準鎖定目標客群，建立分眾名單以進行高效再行銷。
created: 2026-05-28 10:15
last_modified: 2026-05-28 10:20
lang: zh-TW
type: guide
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 確認：是否有手機、是否有email、自訂欄位標配或選配
  - 內部連結
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
  - 篩選會員
  - 建立會員分群
  - 尋找特定客群
  - 再行銷名單
features: 
  - 會員篩選器
  - ORFM_分析
  - 智慧篩選
  - 會員標籤
prerequisites: []
related: []
tags: 
  - 會員管理
  - 會員篩選
  - 再行銷
  - 分眾行銷
  - CRM
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 會員篩選器
  - 新增篩選條件
  - 會員分群
paths: 
  - 會員 > 所有會員
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=5773
  - https://www.cyberbiz.io/support/?p=6893
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/filter
hide: []
---

# Filter and Membership Segmentation
By accurately identifying target customer groups through multi-dimensional criteria, a segmented list Create for efficient remarketing.
{ .subtitle }


!!! tip &quot;Application Context&quot;
    - **Precision Marketing**: Select specific Products collectors and Send exclusive Coupon.
    - **Reclaim Lost Customers**: Identify inactive Membership who haven&#39;t placed an order in over 90 days and Send SMS Messages or Email Address reminder.
    - ** VIP Management**: Select Membership who have reached the cumulative Minimum spending and manually Upgrade their level or Send Gift.
    - **Targeted Event **: Send Offline Event invitations to Membership in specific Area(such as those Recipient&#39;s address contains &quot;Taipei&quot;).



## Instructions for Use

- **Principles for Statistics of Valid Orders **: When filtering Membership consumption records such as &quot; Purchase habit&quot;or&quot;Purchase experience &quot;, all Statistics are based on historical data of **valid Orders **.
- **Filtering Logic Specifications**:
    - **Intersection Operation (AND)**: When you Create multiple different Filter Rules , the system will filter out Membership who Match all conditions simultaneously.
    - **Union operation (OR):** When multiple options are selected within the same Filter Rules , Membership who match Mon of the options will be included.



## Use Membership Filter

### 1. Create Filter Rules

Goto shop to** Membership&gt; All Customers **, and click the ** Create Filter Rules ** button in the upper right corner of the Pages .

! [ ]( CYBERBIZ) { Filter}

### 2. Setting conditions and Apply

1. In the pop-up window, Select the desired filter Type(e.g., Member status, Purchase habit).
2. Setting specific parameters (e.g., Registered date, Cumulative spending).
3. Click ** Apply**, and the List below will immediately show the list of Membership who meet the criteria.

### 3. Bulk actions

After selecting Membership , Operation such as times Send Coupon, Export report , or Update Tags .

! [ ]( CYBERBIZ) { Filter}


## Use Membership groups

### Create groups

After you Setting the criteria in the Filter and click ** Apply**, the next step is to Create the groups:

1. ** Create Membership Profiles**: Click ** Save** and name this list (e.g., High-Value Repeat Buyers). Define the filtered Membership pool as a Group with specific profiles for easy access later without having to duplicate Setting Filter Rules.
2. **Enable Automated Update:** After Save as a group, the list will have a &quot;dynamic monitoring&quot; feature. The system will continuously compare Member status, and any New Members that meet the criteria will be automatically added to this group, ensuring that your marketing list is always up-to- Page publish status.

![](../../assets/images/EC - Backend- Membership- All Customers- Create ){ .screenshot }

### Application Context

After Create Membership groups, You can directly perform the less operational tasks for that specific group:

- **Precise Push Notifications :** When Send SMS Messages, Email , or LINE Message , directly select specific ** Membership segments** as the recipients. This ensures that Message are only delivered to Membership who are genuinely interested, avoiding unnecessary disturbances and saving on Push Notification Cost.
Targeted Marketing Campaign distribution:
- ** Coupon Distribution**: Send recall Coupon in bulk to &quot;dormant Membership &quot; groups, or automatically Send exclusive gifts to &quot; Birthday groups&quot;.
- ** Bonus Mall Traffic Generation**: Filter out Membership whose &quot; points are about to To &quot; and Save as groups, and regularly Push Notification redemption reminders to increase the points consumption rate.
Performance tracking and strategy analysis: By segmenting and observing changes in the purchase Frequency and Price per customer transaction of specific customer groups (such as fans of specific Products ), we can evaluate the conversion effect of the segmentation strategy and optimize subsequent marketing plans.



## Filter Rules Explanation

The system offers Sat filtering dimensions to help you analyze Membership From different perspectives:

!!! info &quot;Applicable Plan Explanation&quot;
    The Membership Filter supports two types of fields: &quot;Standard&quot; and &quot;Optional&quot;.

    - Standard configuration: Supports all Plan of Store software.
    - Optional: Enterprise User can use it directly; PLUS version User need to purchase the ** Membership Module** in order to use it.


### Member status

Filter Membership based on their basic Account information.

| Condition Name| Explanation| Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- | 
| ** Registered date ** | Filter Membership who Add within a Specify Date Range range | ✓ | ✓ |
| ** Customer tag ** | Membership who Contains or Excluded specific Tags | ✓ | ✓ |
| ** Account status** | Filter by Enabled, Disable, Unverified , or alerted Account| ✓ | ✓ |
| ** VIP Levels** | Filtered based on current VIP level | ✓ | ✓ | 
| **Asset Page publish status ** | Filter Membership Valid coupon available, Bonus Points, or whose assets are about to To | ✕ | ✓ | 
| **Social Media Linking** | Filter whether LINE, FACEBOOK fast login , or LINE OA linking is complete | ✕ | ✓ |
    

### Purchase habit

Analyze Membership&#39; shopping behavior and intentions.

| Condition Name| Explanation| Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Most Recent Delete order ** | Filter Membership most recent Delete order matches a specific Date | ✓ | ✓ |
| ** Cart/ Wishlist ** | Filter Membership whose Cart or Wishlist Contains specific Products or Group | ✕ | ✓ | 
| **Number of Days Without Purchase** | Filter Membership with more than N days without any valid Orders | ✕ | ✓ | 
| ** Active Page publish status ** | Determined as &quot; Active,&quot; &quot;Inactive,&quot;or&quot;Lost &quot; based on the order Date | ✕ | ✓ |
| ** Checkout Purchases** | Filter Membership who Add To Cart within N days but haven&#39;t Checkout (must have visited the Checkout Page) | ✕ | ✓ | 

### Purchase experience

Filtering is based on historical transaction data.

| Condition Name| Explanation| Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Cumulative Purchase Amount ** | Filter Membership who have reached the Cumulative spending within a Specify period | ✓ | ✓ |
| ** Number of ordrs ** | Filter Membership who have reached a certain cumulative Orders Number of records within a Specify period | ✓ | ✓ |
| ** Average spending ** | Filter Membership who reached the Average price per customer transaction within a Specify period | ✕ | ✓ |
| ** Quantity ** | Filter Membership who purchase a specific Count or Amount of Products(Group ) | ✕ | ✓ |
| **Payment &amp; Logistics** | Filter Membership who have previously used LINE Pay, JKO Pay , or CVS pickup | ✕ | ✓ |
| **Channel Order source ** | Screening Membership who have previously made purchases on the Official Website or at specific Offline stores (POS) | ✕ | ✓ |
| ** Referral Code ** | Filter Membership who have previously entered a Referral Code to make a purchase | ✕ | ✓ |
| ** Periodic Order Sub Orders ** | Filter Membership who want to establish Recurring order | ✕ | ✓ |

### Membership Basic information

Filtering based on the personal information filled in by Membership.

| Condition Name| Explanation| Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- | 
| ** Subscribes to Marketing ** | Filter Membership who are willing to receive newsletters ( EDM ) | ✓ | ✓ |
| ** Birthday month** | Filter by birthday month (current month or Specify Month)| ✓ | ✓ |
| ** Recipient&#39;s address contains ** | Filter Membership by specific shipping District or location | ✕ | ✓ |
| ** Gender ** | Filter Membership by specific Gender | ✕ | ✓ |
| ** Age ** | Filter Membership within a specific Age range | ✕ | ✓ | 
| ** Mobile ?** | Filter Membership who Save Phone Number information | ✕ | ✓ |
| **Does the Membership Email?** | Filter members who Save Email information | ✕ | ✓ |



### Smart segmentation(ORFM)

Utilize big data models to automatically analyze Membership value.

| Condition Name| Explanation| Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- | 
| **Recent Purchase Sun ** | Date since times purchase | ✕ | ✓ | 
| **Purchase Frequency ** | Number of purchases within a Specify period | ✕ | ✓ |
| **Purchase Amount (Monetary)** | Total spent within the Specify period | ✕ | ✓ |


ORFM scores can quickly identify high-value core customers or those who need to be re-engaged.

### Custom fields

If you Create a Custom fields in ** Website Management&gt; Customer Member Registration Setting ** (../website-management/customer-registration-flow-and-fields.md#Step-4-Create and manage Custom fields ), you can filter the Value you fill in in this Sections .

- Supports field formats: text input, checkboxes, drop-down menus, and Date Range.
- Field format not supported: Upload.



## Frequently Asked Questions

Why is the Number of members selected not as expected?
    Check, please:
    1. **Condition Conflict**: Multiple conditions are related by &quot; AND&quot;. The more conditions there are, the more concise the list becomes.
    2. **Definition of Valid Orders**: Some conditions only count &quot;valid Orders&quot;. Please refer to the definition in [Usage Instructions](#Usage Instructions).
    3. **Data Synchronization**: If a Membership has just completed an Operation, the system may need several minutes to Process the data synchronization.

How to filter out New Members who have &quot; From made a purchase&quot;?
    Please use ** Purchase experience&gt; Number of ordrs**, and Setting the condition to `Equals to 0`.


