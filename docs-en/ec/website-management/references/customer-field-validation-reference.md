---
title: "Customer Field Validation Mode Reference"
description: "Describes the three verification modes for the email and mobile phone fields: optional, required, and required with verification."
created: 2026-05-27 16:04
last_modified: 2026-05-27 18:00
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 了解欄位驗證模式
  - 確認雙重驗證設定方式
features:
  - 選填
  - 必填
  - 必填且必須驗證
  - "Dual Verification"
  - 資料欄位設定
prerequisites: []
related: []
tags:
  - EC
  - "Customer Registration"
  - "Field Verification"
  - 雙重驗證
  - "Account Security"
  - OTP
  - Reference
  - "Reference Table"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 資料欄位設定
  - 顧客驗證方式
paths:
  - 管理中心 > 顧客註冊設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/references/customer-field-validation-reference/"
search:
  exclude: false
icon: lucide/table
hide: []
comments: false
---


On the Member Registration Setting page, the email and mobile fields can each be set to one of the following three states. Dual email and mobile verification simply means setting both fields to **Required and must be verified**.

| State | Customer must fill in | System verifies | When to use |
|:--|:--:|:--:|:--|
| **Optional** | ✗ | ✗ | The field is not essential, and customers decide whether to provide it |
| **Required** | ✓ | ✗ | You need the information from customers but don't check that it is genuine |
| **Required and must be verified** | ✓ | ✓ | Customers must provide it and pass email link or SMS OTP verification |

!!! note "Notes"
    * The **Required and must be verified** state takes two steps in the admin panel: first set the field to **Required** in **Member Field Setting**, and then turn on verification for that field in **Member Verification Setting**.
    * Email is **Required** by default, and mobile is **Optional** by default.
    * At least one of email or mobile must be required. The system doesn't allow both to be optional.
    * Email verification is free. Mobile verification incurs SMS charges.


