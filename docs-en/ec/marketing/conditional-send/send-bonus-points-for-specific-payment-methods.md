---
title: "Bonus Points For Specific Payment Methods"
description: "Create a Bonus Points for Specific Payment Methods group to give bonus points for selected payment methods and steer customers toward low-cost or prepaid options."
created: 2026-01-21 00:00
last_modified: 2026-06-30 10:56
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
  - Enterprise
cyb_extensions: []
intents:
  - 設定指定金流送紅利
features:
  - 紅利點數
  - 金流設定
prerequisites: []
related:
  - ec/marketing/references/coupon-and-bonus-credit-rules.en/
tags:
  - "Payment Bonus Group"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 指定金流送紅利
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=3470
permalink: "https://help.cyberbiz.io/ec/marketing/conditional-send/send-bonus-points-for-specific-payment-methods.en/"
comments: false
search:
  exclude: false
icon: lucide/credit-card
hide: []
---
# Bonus Points For Specific Payment Methods

Create a Bonus Points for Specific Payment Methods group to give bonus points for selected payment methods and steer customers toward low-cost or prepaid options.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

![](../../../assets/images/EC-後台-行銷活動-指定金流送紅利-畫面總覽01.png){ .hero-page }

## About Bonus Points For Specific Payment Methods

Bonus Points for Specific Payment Methods rewards customers based on how they pay. When a customer pays with a payment method you select (such as credit card or ATM transfer), the system automatically gives a fixed number of bonus points. No minimum spend is needed. Use it to reduce operating costs and improve cash flow.

!!! tip "Use Cases"
    - **Increase online payments**: Give more bonus points for credit cards (such as 150 points) to reduce cash on delivery (COD) orders.
    - **Get paid faster**: Give a medium reward for ATM transfers (such as 100 points) to encourage prepayment and lower return risk.
    - **Lower operating costs**: Give fewer points for payment methods with higher fees to balance your costs.

## Before You Start

- **Reward rule**: If a payment method is in more than one payment bonus group, the customer gets the total bonus points from all of those groups.
- **Order display**: The "Estimated bonus points for member" on the order details page includes bonus points from payment, shipping, products, and the order.

## Steps

### Step 1: Create A Payment Bonus Group

1. Log in to the CYBERBIZ admin and go to **Marketing > Bonus for Specific Payment**.
2. Enter a **Collection name** (such as Credit Card Rewards 2024) and click **Add Group**.

### Step 2: Set The Promotion Period And Bonus Rules

Click the group to expand it and fill in the following:

1. **Basic Setup**:
    - **Collection name**: A name to identify the group in the admin.
    - **Start/End Date**: When the promotion takes effect. Leave the end date blank for an ongoing promotion.
2. **Rule settings**:
    - **Bonus Points**: Enter the number of points to give (for example, `150`).
    - **Validity**: Enter how many days the points stay valid (for example, `60`). Enter `0` for no expiry.

### Step 3: Select Payment Methods

1. In the **Payment Methods** list on the left, select the payment methods for this rule (such as credit card or ATM).
2. Click **Add to Group** and make sure the payment methods appear in the group list on the right.
3. To remove one, select it in the group list and click **Remove from Group**.

!!! info "Payment Method Status"
    Only payment methods turned on in **Payment Settings** appear in the list. If you don't see a payment method, turn it on in the admin first.


## More Actions

<div class="grid cards" markdown>

- :lucide-wallet:{ .lg }
  [__coupon / Bonus Points Crediting Rules__](../references/coupon-and-bonus-credit-rules.md)
  Explains when purchase rewards are credited to accounts (import members), and how order completion and returns affect crediting of bonus points and coupons.

</div>