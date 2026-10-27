---
title: "Connect CHAT BOX to a LINE Official Account"
description: "Connect your LINE Official Account to CHAT BOX for real-time conversation sync and member data matching."
created: 2026-05-28 13:50
last_modified: 2026-05-28 13:50
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - APP MARKET
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions:
  - "CHAT BOX"
intents:
  - 串接 LINE 官方帳號
  - 同步 LINE 對話至 CHAT BOX
  - 設定 LINE Messaging API
features:
  - CHAT BOX
  - LINE 整合
  - "Messaging API"
  - Webhook 設定
prerequisites:
  - 需擁有 LINE 官方帳號管理員權限
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
tags:
  - "LINE Integration"
  - CHAT BOX
  - Messaging API
  - "Third-Party Integration"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - LINE Official Account Manager
  - LINE Developers 控制台
paths:
  - APP MARKET > CHAT BOX
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12966
  - https://www.cyberbiz.io/support/?p=52927
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/connect-chat-box-to-line-oa/"
comments: false
search:
  exclude: false
icon: simple/line
hide: []
---

# Connect CHAT BOX to a LINE Official Account
Link your LINE Official Account to CHAT BOX to sync conversations in real time and match customers with member data.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }

!!! tip "Use Cases"
    - **Manage Conversations in One Place**: Reply to LINE customers directly in the CYBERBIZ admin without logging in to LINE Manager.
    - **Identify LINE Members**: The system automatically matches LINE accounts with store members so customer service can see each customer's background.
    - **Reply Faster**: Real-time Webhook pushes make sure you never miss a LINE inquiry.


## Before You Start { #prerequisites-chat-line }

### How the Connection Works { #prerequisites-chat-line-section }

CHAT BOX uses **automatic import**. The system automatically pulls the official account you linked in **Third-Party Integration > LINE OA Settings**.

- **LINE OA Already Connected**: Just turn on the sync switch in CHAT BOX.
- **LINE OA Not Yet Connected**: Complete the Messaging API connection first.

### Permission Requirements { #prerequisites-chat-line-permissions }

- **Admin Permission**: The operator must have **Admin** permission for the LINE Official Account.
- **Irreversible Link**: Once a LINE Official Account is linked to a Provider, you cannot change or unlink it yourself.
- **Webhook Reliability**: Make sure the **Webhook URL** in LINE Developers is correct and **Use webhook** is turned **on**. This is the only channel for message pushes.


## Connection Steps { #operate-chat-line }

### 1. Open CHAT BOX Settings { #operate-chat-line-1-chat-box }

1. Log in to the CYBERBIZ admin and go to **APP MARKET > CHAT BOX**.
2. Click the **Settings** icon at the bottom of the left menu.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-設定01.png){ .screenshot }

### 2. Turn on LINE Sync { #operate-chat-line-2-enable-line }

Follow the steps for the status shown in your LINE section:

#### Status a: Shows "Connected" { #operate-chat-line-status-a-link }

The system has connected to your LINE Official Account.

1. Click **Settings** in the LINE section.
2. Turn on the official account's **Enable switch**. The system starts syncing conversations after you turn it on.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-line啟用01.png){ .screenshot }

#### Status B: Shows "Not Connected" { #operate-chat-line-status-b-link }

You have not linked a LINE Official Account in the admin yet.

1. Click **設定 > 新增官方帳號**.
2. The system takes you to **Third-Party Integration > LINE OA Settings**.
3. Follow [LINE Official Account Connection Settings](../../integrations/line/account-integration/connect-line-messaging-api.md) to complete the Messaging API connection.


## FAQ { #faq-chat-line }

??? quote "A customer sent a LINE message and it shows in the LINE Official Account manager, but no new conversation or message appears in CHAT BOX. Why?"
    The usual cause is that the Webhook is not enabled or the Webhook URL is wrong.

    CHAT BOX receives LINE messages mainly through the LINE Messaging API Webhook. If the Webhook is not enabled, or the Webhook URL is not the correct URL provided by CYBERBIZ, CHAT BOX may not receive messages even though they appear in the LINE Official Account manager.

    Check the following:

    1. Open the LINE Official Account manager.
    2. Click "Settings".
    3. Open "Response settings".
    4. Make sure Webhook is "Enabled".

    Also check the following in the LINE Developers Console:

    - The Webhook URL is the correct URL provided by CYBERBIZ.
    - The Webhook URL is verified.
    - **Use webhook**  is enabled.

??? quote "Will past LINE OA conversations appear in CHAT BOX?"
    Not automatically. After you connect LINE, CHAT BOX usually receives only new messages sent **after the connection is complete and the Webhook takes effect**. Past conversations already in the LINE Official Account manager are not synced to CHAT BOX. After connecting, have a regular LINE user send a new test message to make sure CHAT BOX receives it.

??? quote "If I already use an external service, how can I connect both that service and CYBERBIZ CHAT BOX?"
    LINE currently allows only one Webhook setting. Normally, if you point the LINE Webhook to CYBERBIZ CHAT BOX, your existing external service may stop receiving LINE messages.

    If you want both CHAT BOX and other external services to receive LINE messages, use the LINE Webhook forwarding service provided by CYBERBIZ.

    After setup, the LINE Webhook sends data to CYBERBIZ first, and CYBERBIZ forwards it to your other external services. This way, both CYBERBIZ CHAT BOX and your other services receive LINE messages.

    For details, see [LINE Webhook Forwarding Service](../../integrations/line/account-integration/connect-line-messaging-api/#operate-line-messaging-enable-webhook).

??? quote "Why doesn't CHAT BOX show LINE stickers?"
    LINE does not officially support full sticker display on connected platforms.

    As a result, messages that reach CHAT BOX through LINE may not show stickers the way the LINE Official Account manager does.

??? quote "Are there fees for replying to LINE conversations in CHAT BOX?"
    LINE message fees are based on your LINE Official Account plan. CHAT BOX does not charge extra message fees for LINE conversations. If your LINE Official Account plan has message limits or overage fees, LINE's rules still apply.

??? quote "Why don't messages from LINE OA appear in CHAT BOX?"
    Replies you send to customers from the LINE OA manager do not appear in CHAT BOX.