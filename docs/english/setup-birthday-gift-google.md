---
title: 設定生日禮
description: 設定會員生日禮，包含紅利點數與優惠券的發送規則、自動排程邏輯及提前發送設定。
created: 2026-05-27 12:35
last_modified: 2026-07-14 17:10
lang: zh-TW
type: tutorial
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
  - 行銷活動
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: branch
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents: 
  - 設定生日禮
  - 自動發送生日優惠券
  - 生日紅利點數
features: 
  - 生日禮
  - 紅利點數
  - 優惠券
prerequisites: []
related: 
  - "[[VIP 等級與專屬生日禮設定]]"
tags: 
  - 生日禮
  - 紅利點數
  - 優惠券
  - 自動化行銷
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 優惠券
  - 紅利點數
paths: 
  - 行銷活動 > 全館折扣 – 紅利&優惠券 > 會員生日贈送優惠券/紅利點數
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8752
  - https://www.cyberbiz.io/support/?p=1461
permalink: https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-birthday-gift
comments: false
search:
  exclude: false
icon: lucide/cake
hide: []
---

# Set Birthday Gifts
Set member birthday gifts, including rules for sending bonus points and coupons, automatic scheduling logic, and early sending settings.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-生日禮01.png) { .hero-page }

!!! tip " Application Scenarios "
	- **Member Retention**: Automatically send gifts during the birthday month to increase brand favorability and attract repeat purchases.
	- **Automated Operations**: After setting once, the system automatically schedules the sending, saving labor costs.
	- **Tiered Rewards**: Combined with the VIP system, high-value members receive more generous birthday gifts.


## Birthday Gift Rules

### Send Schedule

- **Sending Time**: The system defaults to sending the birthday gift for the current month on the 1st.
- **Early Sending**: If you want your birthday gift to be sent early, you must complete the setting **2 days** before the sending date so that the system can correctly check the list.
  
    Example: If you want your July birthday gift to be sent 5 days early, please set "Send Birthday Gift 5 Days Early" no later than June 24th so that the system can send the July birthday gift on June 26th.

- **Checking Time**: At 3 AM on the same day, the system begins checking eligible members and sending gifts in order.

    >  The exact time a member receives their birthday gift may vary slightly depending on the system's operating hours.

- -  **Notification Sending Time**: If birthday gift notifications have been enabled in **Push Notifications Email Notification Template** or **SMS Notification Template**, the system will send a notification to members at 12:00 noon on the same day.

### Membership Claiming Rules

- **Register in Birthday Month**: New members who register in their birthday month will receive a birthday gift immediately upon completion, without being subject to the **birthday gift sent N days in advance** restriction.
- **Single Claim Policy**: During the birthday gift sending period (from the date of advance issuance to the end of the birthday month), each member is limited to **one general member birthday gift**.

### Related operations

- -  **Stacked Gifts**: If you have set up a [VIP Birthday Gift] (../../members/vip/setup-exclusive-vip-discounts.en.md#4-生日禮設定) in **Member VIP Settings**, the system will send both the regular birthday gift and the VIP birthday gift simultaneously.
- -  **Delete Birthday Gift**: Please go to **Member All Members**, select your personal page, and [Manually Reclaim] (../../members/manage-member-profiles.en.md#任務四資產配置) coupons or bonus points.
- **Batch Import of Members**: When importing new members, you can decide whether to send a birthday gift for the current month to the new members through the **Send Birthday Gift** section.

    | Field Value | System Behavior |
    | ------ | ------- |
    | Yes | If the birthday gift function is enabled in the backend, birthday gifts imported for the current month will be sent. |
    | No | Birthday gifts imported for the current month will not be sent; gifts for other months will be sent according to backend settings. |

## Operating procedures

### Birthday Gift Content
Log in to the CYBERBIZ management backend (
1. 1. ) and go to **Marketing Activities store-wide Discounts – Bonuses & Coupons > Member Birthday Gift Coupons/Bonus Points**. (
2. ) Switch the function to `開啟`. (
3. ) Set the sending rules: (
    - ) **Birthday Gift Title**: Default is `年月+生日禮` (Please retain the `{{date}}` variable to automatically fill in the date). (
    - ) **Monthly Early Gift**: Set whether to send it in advance before the 1st of the birthday month (e.g., 5 days in advance). (
4. ) Set the gift content: (
    - ) **Bonus Points**: Enter the number of points to give (0 means no points).

        - **Effect Start Date**: Bonus points will be effective immediately upon issuance and will be valid until the end of the month of your birthday.

    - **Coupon**: Set the type (amount/percentage), discount value, number of uses, minimum spending requirement, and usage restrictions.

        - **Effect Start Date**: Coupons are limited to use within the month of your birthday.


## Frequently Asked Questions

??? quote "Can I modify the birthday gift notification content? "
    > Yes. Please go to **Message Push Email Notification Templates** or **SMS Notification Templates**, and find "Customer Receives Personal Birthday Coupon Notification" in the "Customer Related" category to edit it.

??? quote "I set to send the birthday gift 15 days in advance on 7/20, why didn't the August birthday celebrants receive it? "
    Because there are only 12 days left between 7/20 and August 1, exceeding your set "15 days in advance" threshold. The system completed the check of August birthday celebrants on 7/17 (15 days before August 1). Please lower the number of days (e.g., 10 days) to receive the payment the following day.

??? quote "If I adjust the advance payment period, will those who have already received the payment receive it again? "
    Yes. The system sends payments based on whether the recipient meets the next month's birthday criteria. If you shorten the advance payment period after sending, causing the system to trigger the payment logic again, eligible members will receive the payment repeatedly.


