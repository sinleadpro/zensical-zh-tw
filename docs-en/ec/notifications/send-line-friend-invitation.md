---
title: "Send LINE Friend Invitations"
description: "Send LINE Official Account friend invitations to unlinked members by SMS or email to grow your friends list and drive member linking and marketing conversions."
created: 2026-02-22 00:00
last_modified: 2026-07-01 12:00
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - "Push notifications"
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 如何發送 LINE 加入好友邀請
  - 如何增加 LINE 官方帳號好友數
  - 透過簡訊或 Email 進行 LINE 行銷
  - 提升會員互動率
features:
  - 簡訊邀請功能
  - Email 邀請功能
  - 取得 LINE OA 好友連結
  - 簡訊字數自動統計
  - 支援第三方縮網址
  - 優惠券功能整合
prerequisites:
  - LINE 官方帳號
related:
  - ec/integrations/line/account-integration/setup-line-binding-coupon-gift/
tags:
  - LINE
  - "Friend invitations"
  - 訊息推播
  - SMS
  - Email
  - Marketing
  - CRM
  - "LINE OA"
acoiv: operation
apis:
  - LINE Messaging API
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=739
permalink: "https://help.cyberbiz.io/ec/notifications/send-line-friend-invitation/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

![LINE OA friend request settings page](../../assets/images/ec-訊息推播-line oa 加入好友邀請.png){ .hero-page }

## About LINE Friend Requests

**LINE friend requests** let you reach out to members who haven't linked your LINE Official Account, sending friend invitations by **SMS** or **email**. This guides members to add you as a friend and link their accounts, growing your friend count and member engagement.

Here's how it works:

## Requirements And Scope

- **Plans:** This feature is mainly for **Enterprise** customers.

- **Audience:** The system automatically selects members who haven't linked LINE OA.

	- **SMS invitations:** Sent to members who have a mobile number and haven't linked LINE OA.

	- **Email invitations:** Sent to members who have an email address and haven't linked LINE OA.

## Step 1: Get Your LINE Official Account Friend Link {#get-line-oa-add-friend-link}

Before you set up the message, get your link from the LINE Official Account admin:

1. Log in to [**LINE Official Account Manager** :lucide-external-link:](https://manager.line.biz/).

2. Select your account and click **主頁 > 增加好友人數 > 增加好友工具** in the left menu.

3. Click **Create URL** to open the settings page, then click **Copy** to get the friend link.

![](../../assets/images/ec-訊息推播-line 加入好友網址.png)

## Step 2: Add A Message In The CYBERBIZ Admin

1. In the CYBERBIZ admin, go to **Push Notifications > LINE OA Friend Requests**.

2. Click **Add message**.

3. On the edit page, set the following:

	- **Message template:** Write text that encourages members to join, and paste the LINE friend link you copied.

	- **Sending method:** Select [SMS] or [E-mail] (or both).

4. When you're done, click **Save**.

![](../../assets/images/ec-訊息推播-line oa 加入好友邀請-建立好友邀請訊息.png)

## Step 3: Check And Send

1. **Check the length (SMS):** The character count appears at the bottom right of the SMS template. Domestic SMS messages are limited to **70 characters** each (including spaces, line breaks, punctuation, and links). Longer messages are split into several.

2. **Send now:** Click **Send now**. After you confirm in the pop-up, the invitations are sent.

!!! tip "If the LINE friend link is so long that the SMS goes over the limit, shorten it with a third-party URL shortener before pasting it into the template."

!!! warning "Notes"

	- **Check the account:** Before sending, make sure the link points to the right LINE OA so you don't send the wrong friend request.

	- **Avoid SMS blocking:** Avoid keywords that carriers often block (such as "股票" (stocks), "績優" (blue-chip), "加賴" (add on LINE), and "領取" (claim)), or the SMS may fail.

![](../../assets/images/ec-訊息推播-line oa 加入好友邀請-立即傳送.png)

## What Members See

=== "SMS"

	![](../../assets/images/ec-訊息推播-line oa 加入好友邀請-簡訊.png)

=== "Email"

	![](../../assets/images/ec-訊息推播-line oa 加入好友邀請-email.png)

## Next Steps

Pair this with **LINE linking coupon rewards**. Mentioning "add us as a friend and link your account to get a reward" in your invitation can noticeably raise conversions.

<div class="grid cards" markdown>

- :lucide-gift:{ .lg }
  [__LINE linking coupon rewards__](../integrations/line/account-integration/setup-line-binding-coupon-gift.md){ title="設定 LINE 綁定會員贈送優惠券" }
  Turn on "coupon on linking" to reward customers instantly for linking LINE OA with their website account.

</div>


## FAQ

??? quote "After I send friend requests, how does the system know a member has linked?"
	The system checks the link between website member data and LINE UIDs in real time. Once a member clicks the link, authorizes LINE, and links their website account, they're removed from the "to invite" list so they don't get the invitation again.

??? quote "What if an SMS fails to send?"

	If an SMS fails because of a carrier blacklist, a wrong number, or an invalid format, it won't be delivered. SMS messages that carriers block because of sensitive keywords won't be delivered either. Test with a small group first and make sure numbers are formatted correctly.

??? quote "Why can't the LINE link I pasted be tapped in the SMS?"
	For security, some phone systems (such as certain iOS or Android versions) treat text without a protocol as plain text. Make sure your URL starts with `https://` (for example, `https://line.me/R/ti/p/@yourid`).

??? quote "Does a shortened URL affect friend conversion tracking?"
	No. LINE friend links redirect based on the ID in the URL. A URL shortener (such as bit.ly or lihi) saves SMS characters and also gives you click statistics.
