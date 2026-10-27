---
title: "Report Notification Settings"
description: "Send key operating data and low-stock alerts to chosen email addresses. The right people get the information without logging in to export reports every day."
created: 2026-03-19 00:00
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
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定報表接收對象
  - 配置報表發送頻率
  - 調整報表資料範圍
features:
  - 報表自動化
  - 郵件通知
  - 定時發送
  - 庫存預警
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 接收者需具備有效的電子郵件地址
related: []
tags:
  - WMS
  - Automation
  - "Email Subscription"
  - "Operating Data"
acoiv: integration
apis: []
devices:
  - desktop
ui_components:
  - 報表通知列表頁
  - 報表通知編輯頁面
paths:
  - 設定 > 報表通知設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=48336
permalink: "https://help.cyberbiz.io/wms/report-notification-settings/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Report Notification Settings
Send key operating data and low-stock alerts to chosen email addresses. The right people get the information without logging in to export reports every day.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-設定-報表通知設定-畫面總覽01.en.png){ .hero-page }


!!! tip "Why Automate Reports"
    - **Delivered to you**: Key data arrives in your inbox on schedule, so you can make decisions faster.
    - **Right recipients**: Send each report to the people responsible, by user role or to outside email addresses.
    - **Less overload**: Turn each report on or off to filter out what you do not need.


## View the Report Notification List { #operate-report-notify-list }

The report notification list shows every report you can subscribe to and whether it is turned on.

1. Go to **設定 > 報表通知設定**.
2. Review the list:
    - **Report name**: Such as the order summary, inventory change report, or product inventory report.
    - **Subscription status**: Shows whether automatic sending is turned on.
3. Click :lucide-pencil: **Edit** in the Actions column to open the detailed settings.



## Set up Standard Report Notifications { #operate-report-notify-general }

Standard reports have basic subscription settings, mainly for choosing recipients and turning sending on or off.

1. **Subscription Role**: Select user roles in the admin panel (such as Admin or Logistics Staff). The system sends the notification to the email of every account with that role.
2. **Subscription email**: Enter extra email addresses manually. Use this for outside people who need the data but do not log in to the admin panel.
3. **Enable Notification**: Turn the switch on or off.
    - **Note**: Standard reports are **on** by default.

![](../assets/images/WMS-後台-設定-報表通知設定-一般報表設定01.en.png){ .screenshot }


## Set up Advanced Report Notifications { #operate-report-notify-advanced }

Advanced reports (such as the inventory change report, order summary, and product inventory report) offer flexible send schedules and data filters.

!!! info "Advanced Report Defaults"
    Unlike standard reports, advanced reports are **off** by default. You must set them up manually before you can turn them on.

### 1. Set the Send Time { #operate-report-notify-time }

Set the report to send on a specific date or schedule each month:

- **Send Time Type**: Choose how the schedule is set: **Current Month Date** or **Countdown Workday**.
- **Current Month Date**: Enter a number X. The system sends the report on day X of every month.
- **Countdown Workday**: Enter a number X. The system sends the report on the Xth-to-last workday of every month.

### 2. Set the Data Range { #operate-report-notify-range }

In **Report Data Time Type**, set the period of data the report file covers:

- **Current Month**: Set the **Data Date Range** from day X to day Y. The report covers that range within the month.
- **Cross Month**: Set the **Data Date Range** from day X to day Y of the next month. The report covers the continuous period from day X of this month to day Y of the next month.

![](../assets/images/WMS-後台-設定-報表通知設定-進階報表設定01.en.png){ .screenshot }

## Tips { #prerequisites-report-notify }

- **Role permissions**: If you send by **Subscription Role**, make sure the accounts with that role have the correct email address in the system.
- **Troubleshooting delivery**: If you have not received reports for a long time, check your spam folder first, or check whether your mailbox is full.
