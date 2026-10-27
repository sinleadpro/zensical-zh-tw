---
title: "Member Filters And Groups"
description: "Precisely target customer segments with multidimensional criteria and create segmented lists for efficient remarketing."
created: 2026-05-28 10:15
last_modified: 2026-05-28 10:20
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 確認：是否有手機、是否有email、自訂欄位標配或選配
  - 內部連結
ga_views: 0
feedback: 0
products:
  - EC
  - POS
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
  - 篩選會員
  - 建立會員分群
  - 尋找特定客群
  - 再行銷名單
features: 
  - 會員篩選器
  - ORFM 分析
  - 智慧篩選
  - 會員標籤
prerequisites: []
related:
  - ec/website-management/customer-registration-flow-and-fields.en/
tags: 
  - "Member Management"
  - "Member Filtering"
  - Remarketing
  - "Segmented Marketing"
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
permalink: "https://help.cyberbiz.io/ec/members/member-filters-and-groups.en/"
comments: false
search:
  exclude: false
icon: lucide/filter
hide: []
---
# Member Filters And Groups
Precisely target customer segments with multidimensional criteria and create segmented lists for efficient remarketing.
{ .subtitle }


!!! tip "Use Cases"
    - **Targeted Marketing**: Filter members who have saved specific products and send an exclusive coupon.
    - **Re-Engage Lost Customers**: Identify inactive members who have not placed an order for more than 90 days and send an SMS or email reminder.
    - **VIP Management**: Filter members whose cumulative spending meets the threshold, then manually upgrade their membership level or send a gift.
    - **Event Segmentation**: Send invitations to offline events to members in a specific area, such as those whose shipping address contains "Taipei."



## Important Notes

- **Valid Order Calculation**: When filtering member purchase records by criteria such as "Shopping Behavior" or "Purchase History," calculations always use historical data from **valid orders**.
- **Filter Logic**:
    - **Intersection (AND)**: When you add multiple filter criteria, the system selects members who meet all criteria.
    - **Union (OR)**: When you select multiple options within the same filter criterion, members who meet any option are included.



## Use Member Filters

### 1. Add Filter Criteria

Go to **Customer Management > All Customers** and click **Add Filter** in the top-right corner.

![](https://www.cyberbiz.io/support/wp-content/uploads/會員-會員篩選器01.png){ .screenshot }

### 2. Configure And Apply Criteria

1. Select a filter category in the pop-up window, such as Member Status or Shopping Behavior.
2. Set specific parameters, such as registration date or cumulative purchase amount.
3. Click **Apply**. The list below immediately displays members who meet the criteria.

### 3. Perform Bulk Actions

Select members, then perform bulk actions such as **Send coupon**, **Export Report**, or **Edit Tags**.

![](https://www.cyberbiz.io/support/wp-content/uploads/會員-會員篩選器02.png){ .screenshot }


## Use Member Groups

### Create A Group

After setting criteria in the filter and clicking **Apply**, create a group:

1. **Create a Member Profile**: Click **Save** and name the list, such as High-Value Repeat Customers. This defines the filtered member pool as a group with a specific profile. You can reuse it later without configuring the filter criteria again.
2. **Enable Automatic Updates**: After you save the list as a group, it is monitored dynamically. The system continuously checks member statuses and automatically adds new members who meet the criteria. This keeps your marketing list up to date.

![](../../assets/images/EC-後台-會員-所有會員-建立會員分群01.png){ .screenshot }

### Use Cases

After creating a member group, perform the following operational tasks directly for that group:

- **Targeted Message Delivery**: When sending SMS, email, or LINE messages, select a specific **Member Group** as the audience. This ensures that messages reach only interested members, prevents unnecessary disruptions, and reduces messaging costs.
Targeted Marketing Campaign Delivery:
- **coupon Distribution**: Send win-back coupon in bulk to the "Inactive Members" group, or automatically sent an exclusive gift to the "Birthday" group.
- **Bonus Mall Traffic Generation**: Filter members whose points will expire soon and save them as a group. Send regular redemption reminders to increase point usage.
Performance Tracking and Strategy Analysis: Monitor changes in purchase frequency and average order value for a specific segment, such as members interested in a particular product. Use these insights to evaluate conversion performance and optimize future segmented marketing strategies.



## Filter Criteria

The system provides six filter dimensions to help analyze members from different perspectives:

!!! info "Plan Availability"
    Member Filter fields are categorized as "Standard" or "Optional":

    - Standard: Available to merchants on all plans.
    - Optional: Available by default to Enterprise plan users. PLUS plan users must add the **Member Module** to use these fields.


### Member Status

Filter members by basic account status.

| Criteria | Description | Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Registered date** | Members who joined within a specified date range | ✓ | ✓ |
| **Member Tags** | Members who include or exclude specific tags | ✓ | ✓ |
| **Account Status** | Accounts that are enabled, disabled, unverified, or flagged | ✓ | ✓ |
| **VIP Level** | Members by their current VIP level | ✓ | ✓ |
| **Asset Status** | Members who hold valid coupon or bonus points, or whose assets will expire soon | ✕ | ✓ |
| **Social Account Connection** | Members who have or have not completed LINE or Facebook Quick Login or connected LINE OA | ✕ | ✓ |


### Shopping Behavior

Analyze member shopping behavior and intent.

| Criteria | Description | Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Most Recent Order Cancellation** | Members whose most recent order cancellation occurred within a specified period | ✓ | ✓ |
| **Shopping Cart/Wish List** | Members whose shopping cart or wish list contains specific products or groups | ✕ | ✓ |
| **Days Since Last Purchase** | Members who have not placed a completed (valid) order for more than N days | ✕ | ✓ |
| **Activity Status** | Members classified as "Active," "Inactive," or "Lost" based on the interval between orders | ✕ | ✓ |
| **Abandoned Checkout Behavior** | Members who added items to their cart but did not check out within N days (must have visited the checkout page) | ✕ | ✓ |

### Purchase History

Filter members by historical transaction data.

| Criteria | Description | Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Cumulative Purchase Amount** | Members whose cumulative purchase amount reached the threshold during a specified period | ✓ | ✓ |
| **Number of Orders** | Members whose cumulative number of orders reached the threshold during a specified period | ✓ | ✓ |
| **Average spending** | Members whose average order value reached the threshold during a specified period | ✕ | ✓ |
| **Purchase Quantity** | Members who purchased a specified quantity or amount of specific products or groups | ✕ | ✓ |
| **Payment and Logistics** | Members who have used LINE Pay, JKOPay, or convenience store pickup | ✕ | ✓ |
| **Channel Source** | Members who have made purchases on the official website or at specific physical stores (POS) | ✕ | ✓ |
| **Referral Code** | Members who completed a purchase using a profit-sharing referral code | ✕ | ✓ |
| **Recurring Payment Sub-Orders** | Members who placed recurring payment orders | ✕ | ✓ |

### Basic Member Information

Filter members by the personal information they provided.

| Criteria | Description | Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Subscribes to Marketing** | Members who agreed to receive newsletters (EDM) | ✓ | ✓ |
| **Birthday month** | Members whose birthday is in the current or specified month | ✓ | ✓ |
| **Recipient's address contains** | Members in a specific shipping area or location | ✕ | ✓ |
| **Gender** | Members of a specific gender | ✕ | ✓ |
| **Age** | Members within a specific age range | ✕ | ✓ |
| **Mobile** | Members with a saved mobile number | ✕ | ✓ |
| **Email** | Members with a saved email address | ✕ | ✓ |



### Smart Filtering (ORFM)

Use a big data model to automatically analyze member value.

| Criteria | Description | Standard | :lucide-lock: Optional |
| :--- | :--- | :--- | :--- |
| **Most Recent Purchase Date (Recency)** | Time since the last purchase | ✕ | ✓ |
| **Purchase Frequency (Frequency)** | Number of purchases during a specified period | ✕ | ✓ |
| **Purchase Amount (Monetary)** | Total purchase amount during a specified period | ✕ | ✓ |


> Use ORFM scores to quickly identify high-value core customers or customers who require priority re-engagement.

### Custom Fields

If you [add a custom field](../website-management/customer-registration-flow-and-fields.md#步驟-4-建立與管理自訂欄位) in **Website Management > Member Registration Setting**, filter entries by their field values in this section.

- Supported field formats: text input, checkbox, drop-down list, and date.
- Unsupported field format: image upload.



## Frequently Asked Questions

??? quote "Why does the number of filtered members differ from what I expected?"
    Check the following:
    1. **Conflicting Criteria**: Multiple criteria use an "AND" relationship. Adding more criteria narrows the list.
    2. **Valid Order Definition**: Some criteria count only "valid orders." See the definition in [Important Notes](#使用須知).
    3. **Data Synchronization**: If a member just completed an action, the system may need several minutes to synchronize the data.

??? quote "How do I filter new members who have never purchased anything?"
    Use **購買經驗 > 訂單數量** and set the criterion to `等於 0`.


