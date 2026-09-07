---
title: Set up birthday gift
description: Set up member birthday gift, including send rules for bonus points and coupon, automatic scheduling, and early-send settings.
created: 2026-05-27 12:35
last_modified: 2026-07-14 17:10
lang: zh-TW
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
  - "VIP 等級與專屬生日禮設定"
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
permalink: "https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-birthday-gift/"
comments: false
search:
  exclude: false
icon: lucide/cake
hide: []
---

# Set up birthday gift
Set up member birthday gift, including send rules for bonus points and coupon, auto-schedule logic, and early-send settings.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan differences"
    "birthday gift" is an optional "Marketing B" module in the PLUS plan (pick 2 of 11). Merchants must Confirm that the module is already selected. Then they can use it. Enterprise includes this feature.

![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-生日禮01.png){ .hero-page }

!!! tip "Use cases"
	- **Member retention**: Auto-send gifts in the birthday month. This builds brand goodwill and drives repeat purchases.
	- **Automated operations**: Set it once. The system then schedules and sends, which saves staff time.
	- **Tiered rewards**: Combine with the VIP program. Give high-value members more generous birthday gift perks.


## birthday gift rules

### Send schedule

- **Send time**: By default, the system sends that month's birthday gift on the 1st.
- **Early send**: To send birthday gift early, finish setup at least **2 days** before the send date. Then the system can scan the list correctly.

    Example: To send the July birthday gift 5 days early, set "5 days early send the birthday gift" by June 24. The system can then send the July birthday gift on June 26.

- **Scan time**: At 3:00 a.m. that day, the system starts checking eligible members and sends in order.

    > The exact time members get the birthday gift may vary slightly with system processing.

- **Notice send time**: If you turned on birthday gift notices in **Notifications Email Notification Template** or **SMS Notification Template**. The system sends all notices to members at 12:00 noon that day.

### Member claim rules

- **Register in birthday month**: If a new member registers in their birthday month, the system will send the birthday gift right after signup. The **N days early send the birthday gift** setting does not apply.
- **One-claim rule**: In the birthday gift send window (from the early-send date to the end of the birthday month), each member can claim **one regular-member birthday gift**.

### Related actions

- **Stack per**: If you also set a [VIP birthday gift](../../members/vip/setup-exclusive-vip-discounts.en.md#4-生日禮設定) in **Members VIP Settings**, the system sends both the regular birthday gift and the VIP birthday gift.
- **Delete birthday gift**: Go to **Members All Members**, click the member page, and [manually reclaim](../../members/manage-member-profiles.en.md#任務四資產配置) the coupon or bonus points.
- **Batch import members**: During import, use the **perbirthday gift** field to choose whether to send that month's birthday gift to these new members.

    | Field value | System behavior |
    | ------ | ------- |
    | Yes | If the admin birthday gift feature is on, the import-month birthday gift is sent |
    | No | The import-month birthday gift is not sent. Other months follow the admin settings |

## Setup steps

### 1. Set birthday gift content

1. Log in to the CYBERBIZ Admin Panel. Go to **Marketing store-wide discount – Bonus & coupon > Member Birthday Coupons/Bonus Points (Vouchers)**.
2. Switch the feature to `開啟`.
3. Set the send rules:
    - **birthday gift title**: Default is `年月+生日禮` (keep the `{{date}}` variable so the date fills in).
    - **Monthly early per**: Set whether to send before the 1st of the birthday month (for example, 5 days early).
4. Set per content:
    - **bonus points**: Enter the per points (0 means do not per).

        - **Valid from**: bonus points take effect as soon as they are sent. They stay valid until the end of the birthday month.

    - **coupon**: Set the type (Amount/Percentage), discount value, use count, spend threshold, and stacking limits.

        - **Valid from**: The coupon can only be used in the birthday month.


## FAQ

??? quote "Can I edit the birthday gift notice?"
    > Yes. Go to **Notifications Email Notification Template** or **SMS Notification Template**. In the "Customer-related" category, find "Customer received a personal birthday coupon notice" and edit it.

??? quote "I set 15 days early send the birthday gift on July 20. Why did August birthday members not get it?"
    July 20 is only 12 days before August 1, so it misses your "15 days early" cutoff. The system already scanned August birthday members on July 17 (15 days before August 1). Lower the days (for example, 10 days) to send the next day.

??? quote "If I change the early-send days, will people who already claimed then claim again?"
    Yes. The system sends based on "meets next month's birthday rule". If you shorten the early-send days after a send, the send logic can run again. Eligible members will claim twice.


