---
title: "Set up LINE Group Buy Bot"
description: "Create and configure a LINE group buy bot, complete the Messaging API, Webhook, and LIFF integration, and let users shop group buys within LINE groups."
created: 2026-03-11 17:27
last_modified: 2026-07-02 11:17
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - wp 上有影片之後看要不要搬
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 第三方整合
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: advanced
tnb: branch
plans:
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定_LINE_團購機器人
  - LINE_Messaging_API_串接
  - LINE_團購功能設定
  - LIFF_設定
  - Webhook_設定
features:
  - LINE 團購機器人
  - Messaging API
  - Webhook
  - LIFF
  - LINE Provider
prerequisites: []
related:
  - ec/integrations/line/group-buy/setup-line-group-buy-products/
  - ec/integrations/line/group-buy/setup-line-group-buy-group/
tags:
  - "LINE OA"
  - "LINE group buy"
  - LIFF
  - "Messaging line-group-buy-shoppingAPI"
  - Webhook
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=29174&page=2
permalink: "https://help.cyberbiz.io/ec/integrations/line/group-buy/setup-line-group-bot/"
comments: false
search:
  exclude: false
icon: lucide/bot
hide: []
---

![LINE Group Buy Bot Setup](../../../../assets/images/ec-第三方整合-line團購機器人設定.en.png){ title="LINE Group Buy Bot Setup" .hero-page }

## What Is the LINE Group Buy Bot { #intro-line-group-bot }

**LINE Group Buy Bot Setup** is the foundation for running group buying in LINE groups. Set up a dedicated group buy bot and add it to a LINE group so that members can shop directly within the group.

The following is a detailed guide to **LINE Group Buy Bot Setup**:

## Use Cases and Limitations { #prerequisites-line-group-scope }

*   **Purpose**: Helps merchants run group buying activities in LINE groups and invites members to add the brand's official account as a friend.
*   **Supported environment**: Only **LINE groups** or **multi-person chats** are supported. LINE communities (OpenChat) are not supported due to anonymity restrictions.
*   **Recommended practice**: Create the brand official account and the group buy bot account separately to avoid functional conflicts. Both should use the **same LINE Provider (service provider)** so that user data can flow between them.

??? info-clean "LINE Official Account and Group Buy Bot Routing Diagram"
    ```mermaid
        graph LR
            %% Define Node Styles
            classDef provider fill:#76B947,stroke:#5E9639,color:#fff,font-weight:bold;
            classDef officialAccount fill:#5B9BD5,stroke:#4A80B1,color:#fff,font-weight:bold;
            classDef notes fill:none,stroke:none,color:#333,text-align:left;

            %% Nodes
            P("Service Provider<br>(LINE Provider)<br>ex. CYBERBIZ Provider"):::provider

            OA1("LINE Official Account 1<br>(Brand Official Account)<br>ex. CYBERBIZ Brand Official Account"):::officialAccount

            OA2("LINE Official Account 2<br>(Group-Buy Bot Official Account)<br>ex. CYBERBIZ Group-Buy Official Account"):::officialAccount

            N1("Member Management<br>Message Push<br>Segment Marketing<br>Interactive Games<br>FAQ..."):::notes

            N2("Group-Buy Campaign"):::notes

            %% Connections
            P --> OA1
            P --> OA2

            %% Attach Notes (Invisible lines to position text)
            OA1 -.- N1
            OA2 -.- N2
    ```

## Prerequisites { #prerequisites-line-group-setup }

Before you begin, make sure you have the following:

- [x] A LINE Provider
- [x] A brand LINE official account
- [x] A group buy bot LINE official account
- [x] CYBERBIZ admin access
---

## Bot-Specific Messaging API Setup { #operate-line-group-bot }

1.  **Create an account**: Go to [LINE OA Manager :lucide-external-link:](https://manager.line.biz/) and create a dedicated LINE official account for group buying.

    ![Create a new account](../../../../assets/images/ec-第三方整合-lineoa-Create New Account.en.png){ title="Create a new account" }

2.  **Account Settings**: In **Settings > Account Settings**, set **Accept Invitations to Groups or Multi-Person Chats** to **Accept Invitations to Groups or Multi-Person Chats**.

    ![Account settings: accept group invitations](../../../../assets/images/ec-第三方整合-lineoa-帳號設定-接受邀請加入群組或多人聊天室.en.gif){ title="Account settings: accept group invitations" }

3.  **Response settings**: In the Response settings section,
    - Enable the **Chat** feature.
    - Set **Response mode** to **Manual chat + automatic response messages**.
    - **Disable** the welcome message that is sent when users add the account as a friend.

    ![Group buy bot response settings](../../../../assets/images/ec-第三方整合-line團購機器人-回應設定.en.png){ title="Group buy bot response settings" }

4.  **Enable Messaging API**: Click "Enable Messaging API", and select the same **LINE Provider** as your brand website.

    ![Enable Messaging API](../../../../assets/images/ec-第三方整合-lineoa-messagingapi.en.png){ title="Enable Messaging API" }

    !!! warning "Ensure Consistent Customer Identity (UID)"
        If your brand already has a LINE Provider (service provider), select "Existing provider" and **do not create a new Provider**.

        **Reason**: LINE user identifiers (UIDs) are managed per Provider. If the bot and the brand official account belong to different Providers, the system cannot recognize them as the same user.

        **Impact**: Creating the brand official account and the group buy bot under the **same Provider** keeps member identity consistent and prevents data integration failures.

5.  **Connect to the back office**:

    *   Copy the LINE Channel information to the CYBERBIZ admin (path: **Third-Party Integrations ** > ** LINE Group Buy Bot Setup**).

        ![Copy and paste the Messaging API](../../../../assets/images/ec-第三方整合-line團購機器人-linemessageapi-複製貼上.en.gif){ title="Copy and paste the Messaging API" }

    *   Paste the **Webhook URL** provided by CYBERBIZ back into the Messaging API settings in LINE OA Manager, then click **Save**.

        ![Paste the Webhook URL](../../../../assets/images/ec-第三方整合-cyb-webhook-貼上lineoa.en.gif){ title="Paste the Webhook URL" }

6.  **Get the Access Token**:
    - Go to [LINE Developers Console :lucide-external-link:](https://developers.line.biz/console) and open the account, or click the guide link directly from the Messaging API page in LINE OA Manager.

        ![Open the Developers Console](../../../../assets/images/ec-第三方整合-lineoa-linedevelopersconsole-link.en.png){ title="Open the Developers Console" }

    - On the "Messaging API" tab, turn on **Use webhook**, and paste the Webhook URL copied from the CYBERBIZ admin.

        ![Turn on the Webhook and paste the URL](../../../../assets/images/ec-第三方整合-linedeveloperconsole-messagingapi-webhook.en.png){ title="Turn on the Webhook and paste the URL" }

    - Click **Issue** to get the **Channel access token**, paste it back into the CYBERBIZ admin, and save.

        ![Paste the Channel Access Token](../../../../assets/images/ec-第三方整合-line團購機器人-貼上linechannelaccesstoken.en.gif){ title="Paste the Channel Access Token" }

---

## Bot Menu Setup { #operate-line-group-bot-settings }

*   If you already operate a brand LINE official account, enter its **Account ID** in the admin.
*   During group buying (for example, in the main menu, the order completion page, and thank-you messages), the system guides users to add the brand as a friend, which helps grow your membership.

![Group buy bot official account settings](../../../../assets/images/ec-第三方整合-line團購機器人-官方帳號設定.en.png){ title="Group buy bot official account settings" }

## LIFF Setup <small>Key Steps</small> { #operate-line-group-bot-liff-settings-step }

This setting allows the bot to open the shopping interface within the group:

1.  **Create a Login Channel**: Sign in to [LINE Developers Console :lucide-external-link:](https://developers.line.biz/console), click "Create a new channel" under the same LINE Provider, and select "**LINE Login**".

    - **Region** and **Company or owner's country or region**: Select Taiwan.

    ![Create a LINE Login channel](../../../../assets/images/ec-第三方整合-linedevelopersconsole-建立linelogin-channel.en.gif){ title="Create a LINE Login channel" }

2.  **Request permissions**: Open the Basic settings tab of the channel. Under OpenID Connect, click **Apply** next to Email address permission, select the required items, upload a screenshot of the privacy policy, and then click **Submit**.

    ![Request OpenID Connect permissions](../../../../assets/images/ec-第三方整合-linedevelopersconsole-channel-openid.en.png){ title="Request OpenID Connect permissions" }

3.  **Add a LIFF app**: Open the LIFF tab, click Add, and configure the following:
    *   **Size**: Select Tall.
    *   **Endpoint URL**: Enter `[your-domain]/liff`.
    *   **Scopes**: Select all, and make sure to turn on **`chat_message.write`** under view all.
    - After you finish the settings, click **Add** to create the LIFF app.

    ![Add a LIFF app](../../../../assets/images/ec-第三方整合-linedevelopersconsole-channel-liffapp-basic-settings.en.png){ title="Add a LIFF app" }

4.  **Link the OA**: Under Basic settings, select your group buy bot account in **Linked OA**, and click Update.

    ![Linked OA setting](../../../../assets/images/ec-第三方整合-linedevelopers-liffapp-basic-settings-linkedoa.en.png){ title="Linked OA setting" }

5.  **Publish**: Paste the **LIFF ID** and **LIFF URL** into the CYBERBIZ admin. Finally, change the LINE Developers status from "Developing" to "**Published**".

    ![Copy and paste the LIFF ID and URL](../../../../assets/images/ec-第三方整合-line團購機器人-linedevelopers-copynpast-liffid-liffurl.en.gif){ title="Copy and paste the LIFF ID and URL" }

## Next Steps { #next-steps-line-group-bot }

After you finish the bot setup, complete the following two settings before going live:

<div class="grid cards" markdown>

- :lucide-package:{ .lg }   
  [__Group Buy Product Setup__](setup-line-group-buy-products.md){ title="Set Up LINE Group Buy Products" }  
  Select products from the website and set the group buy price.

- :lucide-users:{ .lg }     
  [__Group Buy Group Setup__](setup-line-group-buy-group.md){ title="Set Up LINE Group Buy Groups" }  
  Add the bot to a group, and set up the revenue-sharing plan and event schedule.

</div>

## FAQ { #faq-line-group-bot }


??? quote "Why can't the group buy bot be used in LINE communities (OpenChat)?"
    LINE communities anonymize member identities by default to protect privacy and do not support full Messaging API integration. As a result, the group buy bot currently supports only regular LINE groups and multi-person chats.

??? quote "Why does an error appear when I click Verify after setting up the Webhook?"
    Check the following two items:

    1.  URL accuracy: Make sure the Webhook URL copied from the CYBERBIZ admin is complete and has no extra spaces.
    2.  HTTPS certificate: Your website must have a valid SSL certificate (HTTPS) for LINE to deliver events successfully.
    3.  Save in the admin: Confirm that you have pasted the Channel information into the CYBERBIZ admin and clicked Save before you return to LINE to verify.

??? quote "Why can't customers open the shopping interface after tapping in the group?"
    This is usually related to the LIFF settings. Check the following:

    1.  Published status: The channel status in the LINE Developers Console must be Published (green), not Developing.
    2.  Scopes permission: Confirm that chat_message.write is selected in the LIFF settings and saved.
    3.  Linked OA: Confirm that the LIFF is linked to the official account of the group buy bot.

??? quote "Important: Why must the same Provider be used?"
    If the brand account is under Provider A and the group buy bot is under Provider B, the same user will have completely different UIDs (Unique IDs) on each side, from LINE's perspective. This causes the following:

    * The system cannot determine whether the person making a group purchase is an existing member of the website.
    * bonus points, coupon cannot be accumulated or redeemed across platforms.
    * Order data in the admin cannot be correctly attributed to customers.
