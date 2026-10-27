---
title: "Coupon / Bonus Points Crediting Rules"
description: "Explains when reward coupon and bonus points are import members, and how order completion, Return Status, and returns affect crediting."
created: 2026-08-19 12:35
last_modified: 2026-08-19 12:35
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 行銷活動
  - 訂單
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 紅利何時入帳
  - 優惠券何時歸戶
  - 結案與退貨對紅利的影響
features: 
  - 紅利歸戶
  - 優惠券歸戶
  - 訂單結案
  - 退貨狀態
prerequisites: []
related:
  - ec/marketing/discounts/storewide-discounts.en/
  - ec/marketing/bonus-and-gifts/setup-bonus-points.en/
  - ec/members/manage-member-profiles.en/
tags: 
  - "Bonus Points"
  - coupon
acoiv: operation
apis: []
devices: []
ui_components: []
paths: 
  - 訂單 > 訂單列表
  - 行銷活動 > 全館折扣-紅利 & 優惠券
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/marketing/references/coupon-and-bonus-credit-rules.en/"
comments: false
search:
  exclude: false
icon: lucide/wallet
hide: []
---

# Coupon / Bonus Points Crediting Rules

Explains when reward coupons and bonus points are credited to accounts (import members), and how order completion, Return Status, and returns affect crediting.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All plans
{ .doc-badge }

## Before You Start
- **Applies to**: bonus points and coupons rewarded to the Customer account for an Order.
- **Doesn't apply to**:
    - registration gifts, birthday gifts, and bonus points or coupons sent store-wide or manually right away
    - [store-wide discount: Send coupon](../discounts/storewide-discounts.md) (the coupon is sent when the Order is placed and activates after the Order is completed)
    - Bonus points or coupons that customers redeem at checkout

        > To see whether redeemed bonus points are returned after a return, see [Set Up bonus points: Return Handling](../bonus-and-gifts/setup-bonus-points.md#退貨處理).


## Crediting Conditions

Purchase rewards aren't credited when payment succeeds. The system adds bonus points or coupons to the Customer account only after you Confirm the Order as complete and the Order has no return.

To credit a purchase reward, the Order must meet **both** conditions:

- Order Status: **Completed**
- Return Status: **No Return Needed**


## Common Scenarios

| Scenario | Return Status at Completion | Result | Next Step |
| --- | --- | --- | --- |
| Shipped normally, no return request, completed after the return period | **No Return Needed** | **Credited** | - |
| Customer requested a return and the Order was completed during the return process | **Returning** | **Not credited** | - |
| Completed after the package was picked up but while it was still under inspection or review | **Return Under Review** | **Not credited** | - |
| Inspection failed, marked as **Return Rejected**, then completed | **Return Rejected** | **Not credited** | Send manually if needed |
| Return or exchange processed after the Order was **Completed** | **No Return Needed** | **Credited** (not deducted automatically) | Delete manually to take it back |

!!! tip "Recommended Timing"
    Wait until the Order's return period ends and you're sure no return is needed before you click **Complete Order**. This keeps bonus point rewards accurate and reduces manual fixes later.

## More Actions


<div class="grid cards" markdown>

- :lucide-coins:{ .lg }
  [__Manually Add or Remove Bonus Points__](../../members/manage-member-profiles.md#1-紅利點數派發與管理)
  Add or remove purchase reward bonus points.

- :lucide-ticket-percent:{ .lg }
  [__Manually Add or Remove coupons__](../../members/manage-member-profiles.md#2-優惠券派發與管理)
  Add or remove a Customer's personal coupons.

</div>

