---
title: "Set up Frontend Auto-Logout Time"
description: "The system automatically logs out the account when the POS frontend is idle for the specified time, keeping the store's checkout system secure."
created: 2026-04-07 16:30
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：POS權限設定
ga_views: 0
feedback: 0
products:
  - POS
modules:
  - 所有POS商店
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
  - 設定 POS 自動登出
  - 提高門市收銀安全性
features:
  - 自動登出設定
  - POS 商店管理
prerequisites:
  - 需具備「網站擁有者」權限身份
related:
  - pos/store/staff-permissions-and-account-management/
tags:
  - POS
  - Auto-Logout
  - "Information Security"
  - "Store Management"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - POS 商店列表
  - 自動登出設定彈窗
paths:
  - POS 功能 > POS 商店
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=4259
permalink: "https://help.cyberbiz.io/pos/store/setup-frontend-auto-logout-time/"
comments: false
search:
  exclude: false
icon: lucide/log-out
hide: []
---

# Set up Frontend Auto-Logout Time
When the POS frontend has no activity for the specified time, the system automatically logs out the account to keep the store's checkout system secure.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart POS
{ .doc-badge }

!!! tip "Use Cases"
	- **Information Security Protection**: Prevents unauthorized people from operating the POS system after staff leave the checkout counter.
	- **Account Access Control**: Requires on-duty staff to log in again for each session, ensuring clear accountability.


## Before You Start { #prerequisites-auto-logout }

- **Permission Restriction**: Only users with the **Site Owner** role can configure this setting.
- **Scope**: This setting applies only to the **POS Frontend** interface and does not affect the admin back end.
- **Timer Logic**: The countdown restarts when the system detects any of the following actions:
    - Refreshing the web page
    - Moving the mouse cursor
    - Clicking the mouse

## Procedure { #operate-auto-logout }

### Step 1: Go to the POS Store List { #operate-auto-logout-1-pos-list }

Log in to the CYBERBIZ admin back end and go to **POS > POS Store List**.



### Step 2: Select the Target Store { #operate-auto-logout-2-store }

In the store list, select the POS store you want to configure for auto-logout.

![](../../assets/images/POS-後台-所有POS門市-設定自動登出時間01.en.png){ .screenshot }

### Step 3: Turn on Auto-Logout Settings { #operate-auto-logout-3-enable-auto }

Click the **Auto-Logout Settings** button above the list.

![](../../assets/images/POS-後台-所有POS門市-設定自動登出時間02.en.png){ .screenshot }

### Step 4: Set the Logout Time and Enable It { #operate-auto-logout-4-settings-logout }

1. In the dialog, enter the **Logout Seconds** you want to set.
2. Toggle the switch to **Enable**.
3. Click **Submit**.

![](../../assets/images/POS-後台-所有POS門市-設定自動登出時間03.en.png){ .screenshot }

### Step 5: Confirm the Update Was Successful { #operate-auto-logout-5-confirm-update }

After setup, **POS Auto-Logout Settings** changes to **Enabled**, and the auto-logout time is displayed.

![](../../assets/images/POS-後台-所有POS門市-設定自動登出時間04.en.png){ .screenshot }

### Step 6: Verify the Frontend Display { #operate-auto-logout-6-frontend }

Go to the POS frontend interface. The top-right corner displays the **Auto-Logout** countdown or status.

![](https://www.cyberbiz.co/support/wp-content/uploads/2019/11/自動登出6.png){ .screenshot }


## FAQ { #faq-auto-logout }

??? quote "Why can't I find the **Auto-Logout Settings** button?"
    Check whether you are logged in as the **Site Owner**. Users with standard administrator permissions cannot see or use this feature.


## More Actions { #next-steps-auto-logout }

<div class="grid cards" markdown>

- :lucide-shield-check:{ .lg }   
  [__Administrator Account and Permission Settings__](staff-permissions-and-account-management.md){ data-preview }       
  Create admin login accounts for employees and store staff, and assign the correct permission levels.

</div>

