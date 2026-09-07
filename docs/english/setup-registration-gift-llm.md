---
title: Set up registration gift
description: Set up member registration gift, including send rules for bonus points and coupon, to attract new customers to complete their first registration and purchase.
created: 2026-05-27 12:30
last_modified: 2026-05-27 12:30
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
  - "設定紅利購物金說明"
  - "ec/marketing/bonus-and-gifts/setup-birthday-gift"
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
permalink: "https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-registration-gift/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

# Set up registration gift
Set up member registration gift, including send rules for bonus points and coupon, to attract new customers to complete their first registration and purchase.
{ .subtitle }


![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-會員註冊贈送優惠券-紅利積點01.png){ .hero-page }

!!! tip "Use cases"
	- **New customer onboarding**: Issue bonus points or coupon when customers register, to lower the first-purchase threshold.
	- **Member list collection**: Use rewards to encourage visitors to leave their details and become members.
	- **First brand experience**: Let new members feel the brand's sincerity on their first purchase.

---

## Before you start

- **Send frequency**: Each account receives registration gift only once.
- **import members limit**: For customers imported in an Excel batch, the system **does not automatically per registration gift**. Reissue them manually.
- **automatically sent**: When the customer completes registration, the system automatically imports the reward into the customer account.


## Procedure

### 1. Set up registration gift coupon

!!! info "Plan availability"
    **registration gift coupon** is a field limited to Master, PLUS, and Enterprise users.

1. Log in to the CYBERBIZ admin and go to **Marketing store-wide discount-Bonus & Coupons > Member Registration Coupon**.
2. Switch the feature to `開啟`.
3. Set the coupon content:
    - **Coupon type**: Select `Amount` or `Percentage`.
    - **Discount value**: Enter the redemption Amount or the discount (for 88% of list price, enter 88).
    - **Usage limits**: Set the usage count, Applicable only on orders that are threshold, Link to product tag, and stacking limits.
    - **Validity period**: Set how many days it stays valid after it is claimed (enter 0 for no expiry).

![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-會員註冊贈送優惠券-紅利積點01.png){ .screenshot }


### 2. Set up registration gift bonus points


1. Go to **Marketing store-wide discount-Bonus & Coupons > Member Bonus Points (Vouchers)**.
2. In the **Gift** field, enter the points to per.

    > If you only want to turn on bonus points and not send registration gift, set this field to 0.

3. Set the bonus points validity period (enter 0 for no expiry).

    ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數註冊.png){ .screenshot }


!!! info "Plan availability"
    **bonus redemption minimum spend threshold** and **Single Order Discount Limit** are fields limited to PLUS and Enterprise users.



## FAQ

??? quote "Can I reclaim registration gift after it is sent?"
    > Once coupon import members accounts, to delete them go to **Members All Members**, open the personal page, and edit each record. The same applies to bonus points.

??? quote "If I turn on both coupon and bonus points, does the member get both?"
    Yes. If both features are on, the system sends coupon and bonus points together when the customer registers.


