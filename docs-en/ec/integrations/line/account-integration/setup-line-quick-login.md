---
title: "Set up LINE Quick Login"
description: "Enable LINE Quick Login to simplify member registration, track Official Account friends, and support member data sync and LIFF one-tap login."
created: 2026-02-16 00:00
last_modified: 2026-06-26 10:05
lang: en-US
permalink: "https://help.cyberbiz.io/ec/integrations/line/account-integration/setup-line-quick-login/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 第三方整合
sites: []
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 啟用 LINE 快速登入
  - 簡化顧客註冊流程
  - 整合 LINE 帳號
  - 透過 LINE 取得顧客 Email
  - 增加 LINE OA 曝光
features:
  - LINE 快速登入
  - OpenID Connect
  - Callback URL 設定
  - Channel ID/Secret 管理
  - 串接 LINE 官方帳號加入好友
  - 會員手機號碼同步
  - LIFF 一鍵登入
prerequisites:
  - LINE 帳號（開發者用）
  - 顧客 LINE 帳號已綁定 Email
  - LINE Login 與 Messaging API Channel 使用相同的 Provider
related:
  - ec/integrations/line/account-integration/setup-line-quick-login-phone-number/
  - ec/integrations/line/account-integration/setup-liff-auto-login-member-binding/
tags:
  - LINE
  - Quick_Login
  - Account_Integration
  - Members
  - OAuth
  - OIDC
  - API
  - Third_Party_Integration
acoiv: ""
apis:
  - LINE Login API
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=865
  - https://www.cyberbiz.io/support/?p=675
comments: false
search:
  exclude: false
icon: lucide/log-in
hide: []
---

![](../../../../assets/images/ec-第三方整合-line 註冊登入.en.png){ .hero-page }

## What Is LINE Quick Login { #intro-line-quick }

**LINE Quick Login** lets customers log in or register as members directly with their LINE accounts. The system automatically retrieves the "Email" linked to the customer's LINE account to match accounts. This not only simplifies the shopping process but also increases the exposure of your official account, and lets merchants filter members who log in through LINE in the admin.

The following is a detailed setup tutorial for LINE Quick Login:

## Setup Prerequisites and Notes { #prerequisites-line-quick }

- **Email Binding**: The customer's LINE account **must first have an Email bound** before they can use LINE Quick Login.

- **Provider Consistency**: If you already have a LINE Official Account (Messaging API), make sure the **LINE Login Channel** and the **Messaging API Channel** are under the **same Provider (service provider)**. [Learn About Providers and Channels :lucide-external-link:](https://tw.linebiz.com/manual/line-official-account/line-porvider-and-channel-intro/).

- **Hinet Email Restriction**: If a customer registers with a Hinet email address, they may be unable to reset their password because Hinet blocks the messages.


## LINE Developers Setup Steps { #operate-line-quick }

!!! info "You need a LINE account first. Learn [how to create a LINE Official Account :lucide-external-link:](https://help2.line.me/official_account_tw/web/pc?contentId=20013137&lang=zh-Hant)"

1. **Create a Login Channel**: Log in to [LINE Developers :lucide-external-link:](https://developers.line.biz/), select the correct Provider, then click **Create a LINE Login channel**.

2. **Enter Basic Information**:

	- **Region**: Select "Taiwan" (Taiwan site) / "Japan" (Japan site).

	- **App types**: Select the "Web app" checkbox.

	- Enter the channel name, channel description, Email, and the website's privacy policy and terms of service URLs.

	![](../../../../assets/images/ec-第三方整合-line login channel.en.gif)

3. **Apply for OpenID Connect**:

	- At the bottom of the "Basic settings" tab, find "OpenID Connect" and click "Apply".

	- Select the content as needed, upload the merchant logo, and then click Submit. This step is critical for **ensuring the customer's Email can be retrieved**.

	![](../../../../assets/images/ec-第三方整合-line login channel-openid connect.en.gif)

4. **Set the Callback URL (Critical Step)**:

	- Switch to the "LINE Login" tab, and enter the following in the **Callback URL** field:`https://your-store-url/customer/auth/line/callback`.

	- **Tip**: If you have your own domain, be sure to enter both the CYBERBIZ domain and your own domain. Cross-border customers only need to enter the general domain, without adding `zh-TW`.

	![](../../../../assets/images/ec-第三方整合-line login channel-callback url.en.png)

5. **Publish the Channel**: Change the channel status from "Developing" to "**Published**".

	![](../../../../assets/images/ec-第三方整合-line login channel-publish.en.png)

## CYBERBIZ Back-End Integration Steps { #operate-line-quick-cyberbiz-backend-connect-step }

1. **Get the Keys**: On the "Basic settings" tab in LINE Developers, copy the **Channel ID** and **Channel Secret**.

2. **Enter Credentials in the Back Office**: Go to the CYBERBIZ admin **Third-Party Integration > LINE Login**.

3. **Enable the Feature**: Paste the Channel ID and Channel Secret, turn on the "**Enable LINE Login**" toggle, and save. The login button then appears on the storefront.

![](../../../../assets/images/ec-第三方整合-line login channel-channel id and secret-copy and paste.en.gif)

## Advanced and Value-Added Features { #intro-line-quick-advanced }

### Prompt Customers to Add Friends { #intro-line-quick-advanced-overview-line-quick }

- In the **Basic settings > Linked LINE Official Account** in LINE Developers, select the Official Account under the same Provider.

	![](../../../../assets/images/ec-第三方整合-line login-add friend.en.png)

- After setup, the "Add Friend" option appears on the customer's screen during quick login.

	![](../../../../assets/images/ec-第三方整合-line login-加入好友前台.en.png)

## Next Steps { #next-steps-line-quick }

<div class="grid cards" markdown>

- :lucide-phone:{ .lg }   
  [__Sync Member Phone Numbers__](setup-line-quick-login-phone-number.md){ title="Set up retrieval of member phone numbers during LINE quick login" }       
  After you apply for LINE verification permissions, the system uses the phone number as the primary identifier. This ensures the accuracy and uniqueness of the member database.

- :lucide-link:{ .lg }     
  [__Configure LIFF One-Tap Login__](setup-liff-auto-login-member-binding.md){ title="Set up LIFF auto-login and member binding" }    
  Enable LIFF redirect technology so customers can log in automatically by tapping a link inside LINE. This also completes friend tracking and account linking.

</div>

## FAQ { #faq-line-quick }

??? quote "A 400 Bad Request Error Page Appears"
	This is usually caused by an incorrect **Callback URL** configuration. Check the settings in the LINE Developers admin, and make sure the URL you enter exactly matches the path provided by the system, including the correct `https://` protocol and trailing format. Even minor character differences, such as extra spaces or slashes, can cause API verification to fail and return a 400 error.

??? quote "Customers report that they cannot automatically jump to the LINE App on iOS devices"
	This is caused by the privacy protection mechanism in iOS browsers. We recommend guiding customers to use the **Safari browser** first. When the system displays the prompt "Open in LINE?", be sure to tap "Open". If the automatic redirect fails, customers can also tap the "Log in with LINE App" button at the bottom of the page to start authorization manually.

??? quote "How the System Handles Account Linking Logic Across Social Accounts"
	The system uses **Email** as the unique identifier. When a customer's Facebook and LINE accounts are registered with the same Email, the system automatically consolidates them into one member identity and links them together. If the two Emails are different, the system treats them as separate member accounts. Merging accounts across different Emails is not currently supported.
