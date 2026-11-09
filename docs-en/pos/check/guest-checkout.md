---
title: "Guest Checkout"
description: "Guest checkout lets stores complete sales for non-member customers who do not want to register, using a default account so checkout stays smooth."
created: 2026-04-23 11:55
last_modified: 2026-06-30 21:55
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有POS商店
  - 結帳
  - 訂單
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 啟用訪客結帳
  - POS 訪客登入
  - 查詢訪客訂單
features:
  - POS 訪客結帳
  - 預設訪客帳號
prerequisites: []
related:
  - pos/check/
tags:
  - "POS Guest"
  - "Non-Member Checkout"
  - "Quick Checkout"
  - "Guest Order Lookup"
acoiv: operation
apis: []
devices:
  - tablet
  - desktop
ui_components:
  - 開啟訪客結帳功能
  - 訪客結帳按鈕
  - 會員查詢
paths:
  - POS 功能 > 所有 POS 商店
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=12638
permalink: "https://help.cyberbiz.io/pos/check/guest-checkout/"
comments: false
search:
  exclude: false
icon: lucide/user-minus
hide: []
---

# Guest Checkout
Guest checkout lets stores complete sales for customers who are not members and do not want to register. The system automatically applies a default account, so stores can check out smoothly without requiring membership.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }


!!! tip "Use Cases"
    - **Quick checkout**: When customers are in a hurry or do not want to provide personal information, staff can quickly enter guest mode to complete checkout and avoid long lines at the counter.
    - **Keep operational flexibility**: Customers are not required to become members, which preserves a good shopping experience, while orders can still be tracked through the default account.

## Usage Notes { #prerequisites-guest-checkout }

- **System default account**: Guest checkout always uses `pos-guest@cyberbiz.io` as the login email. This setting is fixed by the system and cannot be changed manually.
- **Member benefit limits**: Guest orders **cannot** accumulate spending totals, bonus points, or VIP levels, and cannot use registration gift or member-exclusive coupon.
- **Order assignment**: All guest orders are assigned to the same system default account. Use guest checkout only when the customer clearly states they do not want to join as a member.

## Procedure { #operate-guest-checkout }

### Step 1: Enable the Feature in the Back Office { #operate-guest-checkout-step-a-admin }

Before using guest checkout, you must first complete the authorization settings in the back office.

1. Log in to the CYBERBIZ back office and go to **POS > POS Store List**.
2. In the store list, click the target **POS store name** to open its store settings.
3. Scroll down, find **Enable Guest Checkout**, and select the checkbox.
4. Click **Save** at the bottom of the page to complete the setup.

![](../../../assets/images/EC-後台-所有POS商店-開啟訪客結帳功能01.en.png){ .screenshot }

### Step 2: Guest Login on the POS Front End { #operate-guest-checkout-step-b-pos }

After you complete the back office setup, the corresponding option appears on the POS front-end login screen.

1. Open the POS front-end login page.
2. Click the **Guest Checkout** button on the screen.
3. The system automatically signs in to the checkout screen with the `pos-guest@cyberbiz.io` account.

![](../../assets/images/POS-前台-結帳-訪客結帳01.en.png){ .screenshot }

### Step 3: Search Guest Orders { #operate-guest-checkout-step-c-query }

To look up past guest transactions later, filter them by the system account.

1. In the POS front end, click **Member Search** (or go to **Orders > All Orders** in the back office).
2. Enter the default account in the search field: `pos-guest@cyberbiz.io`.
3. The system lists all orders completed as a guest.

![](../../assets/images/POS-前台-會員-查詢訪客結帳01.en.png){ .screenshot }

## FAQ { #faq-guest-checkout }

??? quote "Can a customer become a member after guest checkout?"
    The system does not currently support retroactively transferring guest orders to a regular member account. If the customer needs member benefits, **be sure to complete** [member sign-up](../check/index/#operate-check-member-backfill) before checkout.

??? quote "Why don't I see the Guest Checkout button on the POS front end?"
    First, confirm that **Enable Guest Checkout** in the back office is saved correctly, then log back in to the POS front end or refresh the page.


