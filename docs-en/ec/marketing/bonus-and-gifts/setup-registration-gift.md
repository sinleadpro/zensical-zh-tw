---
title: "Set Up Registration Gift"
description: "Set up the member registration gift, including sending rules for bonus points and coupon, to encourage new customers to sign up and make their first purchase."
created: 2026-05-27 12:30
last_modified: 2026-05-27 12:30
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
  - 會員
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 設定註冊禮
  - 會員註冊獎勵
  - 發送註冊優惠券
features: 
  - "registration gift"
  - "bonus points"
  - coupon
prerequisites: []
related: []
tags: 
  - 註冊禮
  - 紅利點數
  - 優惠券
  - "New Customer Marketing"
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
  - 會員 > 所有會員
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=3816
  - https://www.cyberbiz.io/support/?p=6234
permalink: "https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-registration-gift.en/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

# Set Up Registration Gift
Set up the member registration gift, including sending rules for bonus points and coupons, to encourage new customers to sign up and make their first purchase.
{ .subtitle }


![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-會員註冊贈送優惠券-紅利積點01.png){ .hero-page }

!!! tip "Use Cases"
	- **Onboard new customers**: Give bonus points or a coupon at sign-up to lower the barrier to a first purchase.
	- **Grow your member list**: Offer a reward so visitors share their details and become members.
	- **Make a good first impression**: Show new members your appreciation on their first purchase.

---

## Before You Start

- **Frequency**: Each account gets the registration gift only once.
- **import members limitation**: For customers added by Excel bulk import, the system **does not automatically send the registration gift** (per imported account). Send it manually.
- **automatically sent**: As soon as a customer signs up, the system automatically adds the reward to their account.


## Steps

### 1. Set Up The Registration Gift Coupon

!!! info "Plan Availability"
    **registration gift coupon** is available only on the Expert, PLUS, and Enterprise plans.

1. Log in to the CYBERBIZ admin and go to **Marketing > 全館折扣-紅利 & 優惠券 > 會員註冊贈送優惠券**.
2. Switch the feature to `開啟`.
3. Set up the coupon:
    - **Coupon type**: Select `Amount` or `Percentage`.
    - **Discount value**: Enter the discount Amount or rate (for 88% of list price, enter 88).
    - **Usage limits**: Set the number of uses, the threshold (Applicable only on orders that are), Link to product tag, and stacking limits.
    - **Validity**: Set how many days the coupon stays valid after it's claimed (enter 0 for no expiry).

![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-會員註冊贈送優惠券-紅利積點01.png){ .screenshot }


### 2. Set Up The Registration Gift Bonus Points


1. Go to **Marketing > 全館折扣-紅利 & 優惠券 > 會員紅利點數**.
2. In the **Gift** field, enter the number of points to give (per new member).

    > To turn on bonus points without a registration gift, set this field to 0.

3. Set the bonus point validity period (enter 0 for no expiry).

    ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數註冊.png){ .screenshot }


!!! info "Plan Availability"
    **bonus redemption Minimum Spend** and **Single Order Discount Limit** are available only on the PLUS and Enterprise plans.



## FAQ

??? quote "Can I take back a registration gift after it's sent?"
    Once a coupon is in a customer's account (import members), you can only delete it one by one from each customer's page in **Customer Management > All Customers**. The same applies to bonus points.

??? quote "If I turn on both coupons and bonus points, do members get both?"
    Yes. If both features are on, the system sends the coupon and the bonus points together when a customer signs up.


