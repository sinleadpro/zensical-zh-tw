---
title: "Connect CHAT BOX to a Facebook Page"
description: "Connect your Facebook Page to CHAT BOX through Meta authorization for real-time message sync and member data matching."
created: 2026-05-28 13:41
last_modified: 2026-05-28 13:41
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
  - 串接 Facebook 粉絲專頁
  - 授權 Meta 帳號
  - 管理 Facebook 訊息
features:
  - "Meta Authorization"
  - Facebook Messenger 整合
  - CHAT BOX
prerequisites:
  - 需擁有 Facebook 粉絲專頁管理員權限
related: []
tags:
  - "Facebook Integration"
  - Meta 授權
  - CHAT BOX
  - Messenger
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - Meta Business Suite
  - Facebook 授權視窗
paths:
  - Meta Business Suite > 設定 > 用戶 > 用戶
  - Meta Business Suite > 設定 > 帳號 > 粉絲專頁
  - APP MARKET > CHAT BOX
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12966
  - https://www.cyberbiz.io/helpcenter/?p=13010
  - https://www.cyberbiz.io/support/?p=52927
  - https://www.cyberbiz.io/support/?p=53334
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/connect-chat-box-to-facebook-page/"
comments: false
search:
  exclude: false
icon: simple/facebook
hide: []
---

# Connect CHAT BOX to a Facebook Page
Link your Facebook Page to CHAT BOX through Meta authorization to sync messages in real time and match customers with member data.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }

!!! tip "Use Cases"
    - **Unify Social Customer Service**: Reply to Facebook Messenger messages directly in the CYBERBIZ admin.
    - **Identify Potential Customers**: The system automatically matches Facebook accounts with store members so customer service can see each customer's background.
    - **Reply Faster**: Manage messages from multiple Pages in one place so you never miss a sales opportunity.



## Check Account Permissions Before Connecting { #prerequisites-chat-facebook }

Before you start, make sure the operator's Facebook account has the following permissions:

### 1. Page Admin Permission { #prerequisites-chat-facebook-1-manage-permissions }

The operator's Facebook account must have **Admin** permission for the Page.

**How to Check**: Log in to [Meta Business Suite](https://business.facebook.com/), go to **設定 > 用戶 > 用戶**, and review the list of people with access.

![](https://www.cyberbiz.io/support/wp-content/uploads/Meta-Business-Suite-設定-用戶-查看粉專權限名單01.png){ .screenshot }


### 2. Page Permission in Business Settings { #prerequisites-chat-facebook-2-assets-manage }

The operator's Facebook account must have **Full control** of the Page.

**How to Check**:

1. Log in to [Meta Business Suite](https://business.facebook.com/), go to **設定 > 帳號 > 粉絲專頁**, and click the Page you want to connect. Your account should appear in the people list.
    ![](../../../assets/images/Meta%20Business%20Suite-設定-帳號-粉絲專頁-chatbox串接01.en.png){ .screenshot }
2. Click **Manage** to the right of the people list and make sure you have **Full control**.
    ![](../../../assets/images/Meta%20Business%20Suite-設定-帳號-粉絲專頁-chatbox串接02.en.png){ .screenshot }


### 3. Facebook Page Access { #prerequisites-chat-facebook-3-facebook-manage }

The operator's Facebook account must be on the Page access list.

**How to Check**:

1. Log in to Facebook and go to "Settings & privacy" > "Settings" > "Page settings".
    ![](../../../assets/images/Facebook-設定與隱私-粉絲專頁設定-chatbox串接01.en.png){ .screenshot }
2. Make sure your account is listed under **Page access**.
    ![](../../../assets/images/Facebook-設定與隱私-粉絲專頁設定-chatbox串接02.en.png){ .screenshot }

### 4. Meta App Settings { #prerequisites-chat-facebook-4-meta-settings }

The operator's Facebook account must have "Apps, websites and games" turned on. If it is turned off, the connection authorization will break.

**How to Check**：登入Facebook，前往「設定與隱私」>「你的動態」>「應用程式和網站」，確認 **Apps, websites and games** is turned on.

![](https://www.cyberbiz.io/support/wp-content/uploads/Facebook-設定與隱私-應用程式與網站-開啟應用程式通知與網站01.png){ .screenshot }



## Connection Steps { #operate-chat-facebook }

### Step 1: Open the Admin Settings { #operate-chat-facebook-enable-settings }

1. Log in to the CYBERBIZ admin and go to **APP MARKET > CHAT BOX**.
2. Click the **Settings** icon at the bottom of the left menu.
3. Find the Facebook section and click the **Settings** button on the right.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-設定01.png){ .screenshot }

### Step 2: Authorize with Meta { #operate-chat-facebook-meta-authorize }

1. On the "Facebook Connection Settings" page, click **Continue with Facebook**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-FB串接01.png){ .screenshot }

2. The Meta (Facebook) authorization window opens. Complete these steps in order:

    - **Log In**: Log in with an account that has Page admin permission.
    - **Select Pages**: Select the Pages you want to give access to.
        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-FB串接02.png){ .small-image }

    - **Review Permissions**: Confirm that the requested permissions include "Manage Messenger conversations", then click **Save**.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-FB串接03.png){ .small-image }

### Step 3: Link the Page { #operate-chat-facebook-section }

1. After authorization, the page returns to the CHAT BOX admin automatically.
2. Select the Pages you want to connect and click **Confirm Binding**.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-FB串接04.png){ .screenshot }

### Step 4: Check the Connection Status { #operate-chat-facebook-link-status }

After linking, the list shows the Page's information. Make sure **Status** shows **Connected**.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-FB串接05.png){ .screenshot }



## FAQ { #faq-chat-facebook }

??? quote "Will past conversations from before the connection be synced?"
    **No.** The system only syncs conversations created after the connection is complete. Past messages on your Facebook Page are not imported into CHAT BOX.


