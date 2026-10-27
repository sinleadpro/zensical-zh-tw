---
title: "Account Management"
description: "Create staff accounts in the CYBERBIZ e-commerce warehouse system, set login credentials, assign job roles, and suspend accounts or update account data."
created: 2026-03-25 20:30
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 設定
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
  - 如何新增WMS帳號
  - 編輯員工Email與密碼
  - 帳號停權與啟用操作
  - 指派使用者角色
features:
  - 帳號管理
  - 角色指派
  - 帳號狀態控管
prerequisites:
  - wms/permission-settings/
related:
  - wms/permission-settings/
tags:
  - "Account Maintenance"
  - "Permission Assignment"
  - WMS
  - "Staff Management"
  - "Security Control"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 新增帳號
  - 啟用帳號開關
  - 使用者角色選單
paths:
  - 設定 > 帳號管理
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/account-management/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Account Management
Create staff accounts in the CYBERBIZ e-commerce warehouse system, set login credentials, assign job roles, and suspend accounts or update account data.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-設定-帳號管理-畫面總覽01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Onboarding**: Create an account for a new employee and assign a default role (such as Admin or a custom role).
    - **Security upkeep**: Check the last login time regularly to find accounts that have not been used for a long time, and decide whether to remove their access.
    - **Instant suspension**: When someone leaves or changes jobs, turn off the switch to cut off their system access right away.


## Before You Start { #prerequisites-accounts }

- **Unique email**: Each account must use a unique email address as its login. The same email cannot be registered twice.
- **Password security**: Passwords must meet the system's complexity rules. The admin should ask the user to change the password after the first login.
- **Permissions first**: Before you assign a user role, [create the role and define its permissions](permission-settings.md).


## Create an Account { #operate-accounts-create }

1. Log in to the CYBERBIZ e-commerce warehouse admin panel and go to **設定 > 帳號管理**.
2. Click **+ Add Account** in the upper-right corner of the page.
3. Fill in the account details as described in the table below:

    | Field | Description | Required |
    | :--- | :--- | :--- |
    | **Name** | The employee name or code shown in the system | Required |
    | **Email** | The account's login and the address for system notifications | Required |
    | **User Role** | The job role template for this account (such as Admin) | Required |
    | **Password** | The account's initial login password | Required |
    | **Confirm Password** | Enter the password again to confirm it | Required |
    | **Subscribe to Email?** | Whether the account receives operating or feature notifications from the system. | Single choice (Subscribe / Do not subscribe) |

4. Click **Save** to create the account.

![](../assets/images/WMS-後台-設定-帳號管理-新增帳號01.en.png){ .screenshot }

## Maintain Accounts and Control Status { #operate-accounts-maintain }

After you create accounts, manage them from the account list.

1. **Search and filter**: Enter a keyword in the search box to find a specific employee.
2. **Turn accounts on or off**:
    - Use the switch in the **Enable Account** column to change the status.
    - :lucide-toggle-right: means the account is active.
    - :lucide-toggle-left: means the account is suspended, and the user cannot log in.
3. **Edit account data**: Click **:lucide-pen: Edit** in the **Actions** column to change the name, role, or email subscription setting, or to reset the password.



## FAQ { #faq-accounts }

??? quote "Why Does It Say "Email Already in Use" When I Add an Account?"
    That email address is already registered in the system. Search for the account first to see whether it already exists (it may be suspended), or register with a different email address.

