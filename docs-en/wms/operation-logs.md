---
title: "Operation Log List"
description: "The operation log list records what every user does in the e-commerce warehouse admin panel. Managers can track each account's actions, source IP address, and time."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 可以查看的同仁操作名單，會依登入者的權限不同而有差異嗎
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 操作紀錄列表
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 查看操作日誌
  - 稽核匯出行為
  - 追蹤帳號活動
features:
  - 操作紀錄
  - 系統審核
  - 安全性管理
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 需具備管理者或對應權限
related: []
tags: []
acoiv: integration
apis: []
devices:
  - desktop
ui_components:
  - WMS 管理後台
paths:
  - 操作紀錄列表
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/operation-logs/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Operation Log List
The operation log list records what every user does in the e-commerce warehouse admin panel. Managers can track each account's actions, source IP address, and time.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-操作紀錄列表-畫面總覽01.en.png){ .hero-page }


## View Operation Logs { #operate-operation-logs-view }

The system records key actions automatically and lists them newest first.

1. Log in to the **WMS admin panel**.
2. Click **Operation Log List** in the left menu.
3. Review the information in the list:
    - **Operation**: The specific action taken (such as logging in, exporting a report, or reading an announcement).
    - **Operator**: The account name or ID of the user who took the action.
    - **IP address**: The IP address used for the action. Use it to spot logins from unusual locations.
    - **Operation Time**: The exact time of the action.


## Common Logged Actions { #specs-operation-logs-events }

The operation log list mainly covers these kinds of activity:

- **Account activity**: Users' logins and logouts.
- **Data exports**: Downloads of reports or data (such as exporting bundle products, the product inventory summary, or the product information summary).
- **System interaction**: Reading system notices such as merchant admin announcements.
- **Data changes**: Key edits to modules such as products, orders, and vendors.



!!! tip "Security and Permission Reminders"
    - **Security audits**: If you see logins from unexpected IP addresses or large data exports outside working hours, check the account's security and change its password right away.
    - **Accountability**: For merchants with many staff, operation logs are an important way to check work processes and who did what.
    - **Permission limits**: Only admin accounts with specific permissions can see the full operation log list.
