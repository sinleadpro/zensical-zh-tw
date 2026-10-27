---
title: "Set Up Birthday Gift"
description: "Set up the member birthday gift, including sending rules for bonus points and coupon, automatic scheduling, and early sending."
created: 2026-05-27 12:35
last_modified: 2026-07-14 17:10
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
  - 行銷活動
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents: 
  - 設定生日禮
  - 自動發送生日優惠券
  - 生日紅利點數
features: 
  - "birthday gift"
  - "bonus points"
  - coupon
prerequisites: []
related:
  - ec/members/vip/setup-exclusive-vip-discounts.en/
  - ec/members/manage-member-profiles.en/
tags: 
  - 生日禮
  - 紅利點數
  - 優惠券
  - "Marketing Automation"
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
permalink: "https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-birthday-gift.en/"
comments: false
search:
  exclude: false
icon: lucide/cake
hide: []
---

# Set Up Birthday Gift
Set up the member birthday gift, including sending rules for bonus points and coupons, automatic scheduling, and early sending.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    On PLUS plans, the birthday gift is part of the Marketing B add-on module (choose 2 of 11). Confirm that you've selected this module before using it. The Enterprise plan includes it by default.

![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-生日禮01.png){ .hero-page }

!!! tip "Use Cases"
	- **Member retention**: Send a gift automatically in the birthday month to build goodwill and drive repeat purchases.
	- **Automation**: Set it up once and the system schedules and sends gifts automatically, saving staff time.
	- **Tiered rewards**: Combine it with VIP tiers to give high-value members a better birthday gift.


## Birthday Gift Rules

### Sending Schedule

- **Send date**: By default, the system sends each month's birthday gift on the 1st of that month.
- **Early sending**: To send the birthday gift early, finish the setting at least **2 days** before the send date so the system can build the recipient list correctly.

    Example: To send the July birthday gift 5 days early, set "send the birthday gift 5 days early" by 6/24 at the latest. The system can then send the July birthday gift on 6/26.

- **Check time**: At 3:00 AM on the send date, the system checks for eligible members and sends gifts in turn.

    > The exact time members receive the birthday gift may vary slightly depending on system processing.

- **Notification time**: If you've turned on the birthday gift notification in **Push Notifications > Email Notification Template** or **SMS Notification Templates**, the system sends all notifications to members at 12:00 PM that day.

### Claim Rules

- **Sign-up in the birthday month**: If a new member signs up in their birthday month, the system will send the birthday gift right away, regardless of the **send the birthday gift N days early** setting.
- **One per cycle**: Within each birthday gift cycle (from the early send date to the end of the birthday month), each member can claim **one regular member birthday gift**.

### Related Actions

- **Stacking (one gift per tier)**: If you've also set up a [VIP birthday gift](../../members/vip/setup-exclusive-vip-discounts.md#4-生日禮設定) in **Customer Management > VIP Settings**, the system sends both the regular birthday gift and the VIP birthday gift.
- **Delete a birthday gift**: Go to **Customer Management > All Customers**, open the customer's page, and [manually take back](../../members/manage-member-profiles.md#任務四資產配置) the coupon or bonus points.
- **Bulk import members**: When importing, use the **birthday gift (per member)** field to decide whether to send the current month's birthday gift to the new members.

    | Field Value | System Behavior |
    | ------ | ------- |
    | Yes | If the birthday gift feature is on, the birthday gift for the import month is sent |
    | No | The birthday gift for the import month isn't sent. Other months follow the admin settings |

## Steps

### 1. Set Up The Birthday Gift

1. Log in to the CYBERBIZ admin and go to **Marketing > Shop-wide Discount – Bonus & Coupons > 會員生日贈送優惠券/紅利點數**.
2. Switch the feature to `開啟`.
3. Set the sending rules:
    - **birthday gift Title**: The default is `年月+生日禮` (keep the `{{date}}` variable so the date is filled in automatically).
    - **Monthly Early Sending (days per month)**: Choose whether to send before the 1st of the birthday month (for example, 5 days early).
4. Set what to send (per member):
    - **bonus points**: Enter the number of points (per member). Enter 0 to send none (per).

        - **Effective from**: bonus points take effect as soon as they're sent and expire at the end of the birthday month.

    - **coupon**: Set the type (Amount/Percentage), discount value, number of uses, minimum spend, and stacking limits.

        - **Effective from**: The coupon can be used only in the birthday month.


## FAQ

??? quote "Can I edit the birthday gift notification?"
    Yes. Go to **Push Notifications > Email Notification Template** or **SMS Notification Templates**, find "Customer Birthday Personal coupon Notification" under Customer, and edit it.

??? quote "I set it to send the birthday gift 15 days early on 7/20. Why didn't August birthday members get it?"
    Because 7/20 is only 12 days before 8/1, which is past your 15-day setting. The system had already checked August birthday members on 7/17 (15 days before 8/1). Lower the number of days (for example, to 10) and the system will send the next day.

??? quote "If I change the number of early sending days, will members who have already claimed it claim again?"
    Yes. The system sends gifts based on whether a member qualifies for next month's birthday. If you shorten the early sending days after gifts are sent and this triggers sending again, eligible members will get the gift again.


