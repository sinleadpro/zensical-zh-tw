---
title: "Coupon (Code) And Bonus Points Expiry Notifications"
description: "Set expiry reminders for coupon (codes) and bonus points. Notify customers by email, SMS, or LINE OA to use them early and drive repeat purchases."
created: 2026-05-27 18:04
last_modified: 2026-07-06 17:00
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
  - 設定優惠券到期通知
  - 設定紅利點數到期提醒
  - 提升行銷活動回購率
features: 
  - 優惠券到期通知
  - 紅利點數到期通知
  - 訊息推播
prerequisites: []
related: []
tags: 
  - coupon
  - "bonus points"
  - "Expiry Notification"
  - "Marketing Automation"
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: []
paths: 
  - 行銷活動 > 全館折扣 – 紅利&優惠券 > 優惠券/紅利點數到期通知
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=11115
permalink: "https://help.cyberbiz.io/ec/marketing/purchase-restrictions/coupon-and-bonus-points-expiry-notification.en/"
comments: false
search:
  exclude: false
icon: lucide/bell
hide: []
---
# Coupon (Code) And Bonus Points Expiry Notifications
Set expiry reminders for coupons (codes) and bonus points. Notify customers by email, SMS, or LINE OA to use them early and drive repeat purchases.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }


## Set The Reminder Days

1. Log in to the CYBERBIZ admin and go to **Marketing > Shop-wide Discount – Bonus & Coupons > 優惠券/紅利點數到期通知**.
2. Set the notification to send **N days** before expiry.

    > To change the setting, finish before 23:59 the day before sending so the system can build the recipient list correctly.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知01.png){ .screenshot }

## How The System Sends Reminders

- **Expiry time**:
    - **coupon (code)**: 23:59:59 on the end date.
    - **bonus points**: The exact time set when the bonus points were created.
- **Schedule**: Every day at **3:00 AM**, the system checks for eligible members. It sends all notifications at **12:00 PM**.


    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知07.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知08.png){ .screenshot }

    </div>

## Turn On Notification Channels

Make sure to turn on the matching notification switches at these paths:

=== "Email"

    > Admin path: Messaging Email Notification Templates > Customer

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知02.png){ .screenshot }

=== "SMS"

    > Admin path: Messaging SMS Notification Templates > Customer

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知03.png){ .screenshot }

=== "LINE OA"

    > Admin path: Messaging LINE OA Notification Templates > Customer

    ![](https://www.cyberbiz.io/support/wp-content/uploads/行銷活動-優惠券紅利點數到期通知04.png){ .screenshot }