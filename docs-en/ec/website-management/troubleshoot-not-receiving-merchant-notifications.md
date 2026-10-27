---
title: "Troubleshoot Missing Merchant Notification Emails"
description: "If emails from CYBERBIZ, such as order notifications and system announcements, are being sorted into Spam, this guide helps you change your settings so that you receive important notifications on time."
created: 2026-06-01 15:25
last_modified: 2026-06-30 08:02
lang: en-US
type: troubleshooting
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: []
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
  - 解決收不到系統信問題
  - 設定 Gmail 篩選器
  - 避免信件進入垃圾桶
features: 
  - 系統通知信
  - Gmail 篩選器
prerequisites: []
related: []
tags: 
  - "Notification Emails"
  - Spam
  - Gmail
  - "Missing Email Troubleshooting"
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - Gmail 設定
  - 篩選器
paths: 
  - Gmail > 設定 > 篩選器和封鎖的地址
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4964
  - https://www.cyberbiz.io/support/?p=31664
permalink: "https://help.cyberbiz.io/ec/website-management/troubleshoot-not-receiving-merchant-notifications/"
comments: false
search:
  exclude: false
icon: lucide/mail-x
hide: []
---

# Troubleshoot Missing Merchant Notification Emails
If emails from CYBERBIZ, such as order notifications and system announcements, are being sorted into Spam, this guide helps you change your settings so that you receive important notifications on time.
{ .subtitle }

## Before You Start { #prerequisites-merchant-notify }

- This guide only covers basic setup. For details, see Google's official article [Report spam in Gmail](https://support.google.com/mail/answer/1366858).


## Method 1: Report Not Spam { #operate-merchant-notify-not-spam }

When you find an email from CYBERBIZ in your Spam folder, do the following:

1. Open the email.
2. Click **Report not spam** at the top.
3. Gmail moves the email back to your inbox and learns that the sender is safe.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件08.jpg){ .screenshot }



## Method 2: Set up a Gmail Filter (Recommended) { #operate-merchant-notify-filter }

With a filter, you can make sure that emails from specific addresses are **never** sent to Spam.

### 1. Open Gmail Settings { #operate-merchant-notify-enter }

Log in to Gmail on the web and click **Settings (gear icon) > See all settings** in the upper-right corner.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件02.png){ .screenshot }

### 2. Create a New Filter { #operate-merchant-notify-create }

Go to the **Filters and Blocked Addresses** tab and click **Create a new filter**.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件03.png){ .screenshot }

### 3. Enter the Senders { #operate-merchant-notify-senders }

In the **From** field, enter the following official CYBERBIZ email addresses:

(We recommend entering all of them, separated by semicolons `;`.)

- **support@cyberbiz.io**
- **noreply@cyberbiz.co**
- **support@cyberbiz.co**

When you are done, click **Create filter**.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件04.png){ .screenshot }

### 4. Choose the Filter Actions { #operate-merchant-notify-exclude }

Select these three key options so the emails show up correctly:

- **Apply the label**: Choose or create a label (such as CYBERBIZ) so you can view these emails together in the left menu.
- **Never send it to Spam**: This is the most important setting. It makes sure the emails are not blocked.
- **Always mark it as important**: Makes sure the emails appear in your Priority Inbox.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件05.png){ .screenshot }

### 5. View Your Filters { #operate-merchant-notify-apply }

After setup, go to **Filters and Blocked Addresses** to see all of your filters.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件06.png){ .screenshot }

Open the **CYBERBIZ** label to see all the filtered emails.

![](https://www.cyberbiz.io/support/wp-content/uploads/如何避免未收到-CYBERBIZ-商家通知信件07.png){ .screenshot }

