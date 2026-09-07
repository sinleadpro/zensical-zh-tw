---
title: 設定註冊禮
description: 設定會員註冊禮，包含紅利點數與優惠券的發送規則，吸引新客完成首次註冊與消費。
created: 2026-05-27 12:30
last_modified: 2026-05-27 12:30
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
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定註冊禮
  - 會員註冊獎勵
  - 發送註冊優惠券
features: 
  - 註冊禮
  - 紅利點數
  - 優惠券
prerequisites: []
related: 
  - "[[設定紅利購物金說明]]"
  - "[[設定生日禮]]"
tags: 
  - 註冊禮
  - 紅利點數
  - 優惠券
  - 新客行銷
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 優惠券
  - 紅利點數
paths: 
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 會員註冊贈送優惠券
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 會員紅利點數
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=3816
  - https://www.cyberbiz.io/support/?p=6234
permalink: https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-registration-gift
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

# Set up a registration gift.
Set up a membership registration gift, including rules for sending bonus points and coupons, to attract new customers to complete their first registration and purchase.
{ .subtitle }


![](https://www.cyberbiz.io/support/wp-content/uploads/store-wide折扣-會員註冊贈送優惠券-紅利積點01.png){ .hero-page }

!!! tip " Application Scenarios "
	- **New Customer Onboarding**: Customers receive bonuses or coupons upon registration, lowering the barrier to first purchase.
	- **Member List Collection**: Encourage visitors to leave their information and become official members with reward incentives.
	- **Brand First Experience**: Let new members feel the brand's sincerity during their first purchase.

---

## Instructions for Use

- **Sending Frequency**: Each account will only receive the registration gift once.
- **Membership Transfer Limit**: For customers transferring via Excel batch, the system **will not automatically send the registration gift**; it must be manually sent.
- **Automatic Sending**: The system will automatically transfer the reward to the customer's account upon completion of registration.


## Operating procedures

### Registration Gift Coupon

!!! info " Version Application Instructions "
    **Registration Gift Coupon** This field is limited to Advanced, PLUS, and Enterprise version users.

1. 1.  Log in to the CYBERBIZ management backend and go to **Marketing Activities store-wide Discounts - Bonuses & Coupons > Member Registration Gift Coupon**.
2. Switch the function to `開啟`.
3. Set coupon content:
    - **Coupon Type**: Select `Amount` or `Percentage`.
    - **Discount Amount**: Enter the discount amount or discount (e.g., enter 88 for 88% off).
    - **Usage Restrictions**: Set the number of uses, order minimum spending threshold, bound product tags, and usage restrictions.
    - **Validity Period**: Set the validity period after claiming (enter 0 for permanent validity).

![](https://www.cyberbiz.io/support/wp-content/uploads/store-wide折扣-會員註冊贈送優惠券-紅利積點01.png){ .screenshot }


### sets registration bonus points


1. 1.  Go to **Marketing Activities store-wide Discounts - Bonuses & Coupons > Member Bonus Points**.
2. Enter the number of points you want to award in the **Gift** field.

    >  If you only want to enable the bonus feature but not give a registration bonus, please set this field to 0.
    
3. Set the bonus validity period (enter 0 to mean it is valid indefinitely).

    ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數註冊.png){ .screenshot }


!!! info " Version Application Notes "
    **Minimum spending threshold for bonus redemption** and **Single Order Discount Limit** are fields limited to PLUS and Enterprise edition users.



## Frequently Asked Questions

??? quote "Can the registration gift be withdrawn after it's sent? "
    > OOnce a coupon is credited to a member's account, to delete it, you must go to **Members All Members** and operate on each item individually on their personal page. The same applies to bonus points.

??? quote "If I activate both coupons and bonus points at the same time, will the member receive them both? "
    Yes. If both functions are activated, the system will send both coupons and bonus points together when the customer registers.


