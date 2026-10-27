---
title: "Customer Registration Mode Reference"
description: "Compares the Quick Checkout and Register mode with the Registration Required mode, including adding to cart, when customers register, and when to use each mode."
created: 2026-05-27 16:30
last_modified: 2026-07-02 18:56
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 管理中心
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
plan_options: []
cyb_extensions: []
intents:
  - 比較註冊模式差異
  - 了解快速結帳與必須註冊的適用情境
features:
  - 快速結帳並註冊
  - 必須註冊
  - 雙重驗證
prerequisites: []
related:
  - ec/website-management/setup-customer-email-phone-verification/
tags:
  - EC
  - "Customer Registration"
  - "Registration Mode"
  - "Quick Checkout"
  - "Members Only"
  - Reference
  - "Reference Table"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 顧客註冊
paths:
  - 管理中心 > 顧客註冊設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/references/customer-registration-modes-reference/"
search:
  exclude: false
icon: lucide/table
hide: []
comments: false
---

The **Member Registration** setting sits at the top of the Member Registration Setting page. It decides if customers must sign up before they can order. You can pick one of two modes.

| Mode | Add to cart | When customers register | When to use |
|:--|:--|:--|:--|
| **Fast checkout with registration** | No login needed; customers can add items anonymously | At checkout (customers can log in, or become members after checkout) | General online stores that want an easier checkout |
| **Registration required** | Customers must log in or register first | Customers must register before adding items to the cart | Membership stores, wholesale websites, and stores that need strict control over who can buy |

!!! note "Notes"
    * **Fast checkout with registration** is the default mode for most stores. Customers can add items to the cart without logging in. At checkout, they choose whether to become members.
    * When **Registration required** is combined with [dual email and mobile verification](../setup-customer-email-phone-verification.md){ title="Set Up Dual Email and Mobile Verification for Customers" }, customers must pass both checks before they can shop.
    * If you switch the mode, existing members aren't affected. They can still log in and shop as usual.

