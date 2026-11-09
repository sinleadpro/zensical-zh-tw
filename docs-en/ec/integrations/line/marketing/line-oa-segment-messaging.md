---
title: "Set up and Send LINE OA Segment Messages"
description: "Set up and send LINE OA segment messages to members with specific tags."
created: 2026-03-09 09:48
last_modified: 2026-06-26 10:05
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
  - 第三方整合
  - 訊息推播
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
  - AUTOMATION
intents:
  - 如何發送 LINE 分眾訊息
  - LINE OA 推播教學
features:
  - LINE OA 分眾推播
  - 顧客標籤篩選
  - 文字訊息發送
  - 圖片訊息發送
prerequisites:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
  - ec/app-market/automation/automation-push-flow/
tags:
  - segment_messaging
  - push_messaging
  - LINE_Messaging_API
  - LINE_OA
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訊息推播 > LINE OA 發送訊息
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7324
  - https://www.cyberbiz.io/support/?p=25964
permalink: "https://help.cyberbiz.io/ec/integrations/line/marketing/line-oa-segment-messaging/"
comments: false
search:
  exclude: false
icon: lucide/message-square-share
hide: []
---

![LINE OA Segment Messaging](../../../../assets/images/ec-訊息推播-lineoa-訊息.en.png){ .hero-page title="LINE OA Segment Messaging" }

## LINE OA Segment Messaging Guide { #overview-line-segment }

**LINE OA Segment Messaging** lets merchants send targeted messages to members with specific tags, improving conversion rates and reducing unnecessary messaging costs.

Below are detailed instructions and a walkthrough:

## Prerequisites { #prerequisites-line-segment }

Before using segment messaging, make sure you complete the following setup:

- [x] [**Connect Messaging API**](../account-integration/connect-line-messaging-api.md){ title="Connect LINE Messaging API" }: Merchants must first complete the LINE Messaging API connection setup before they can send messages from the CYBERBIZ admin.
- [x] **Collect member UIDs**: Messages can only be sent to website members who have previously completed **"[LINE Quick Login](../account-integration/setup-line-quick-login.md){ title="Set up LINE Quick Login" }"** or **"[Linked LINE OA](../account-integration/bind-line-oa-store-members.md){ title="Bind LINE Official Account to Website Member" }"**, because only these actions leave the UID needed for sending messages in the website system.
- [x] **Confirm friend status**: Only **LINE OA friends** (who have not blocked the Official Account) can successfully receive messages.
- [x] **Messaging fees**: The LINE push service bills according to the message plan you set for your LINE Official Account. Manual pushes and automated notifications are both paid items, and only successfully sent messages are billed.

## Steps to Send Segment Messages Manually { #operate-line-segment }

1.  **Admin path**: Go to the admin dashboard and click **Push Notifications > LINE OA Send Messages**.
2.  **Set customer tags**: In the "Customer Tags" field, select the tags for the audience you want to message (required). The system automatically filters members who match the tags and have a UID.
3.  **Select a Sending Type** (only one mode can be selected at a time):
    *   **Text Message**: Supports line breaks and **emoji**, with no character limit. Click Send to schedule the message for immediate delivery.
    *   **Image message**: Upload a single image (recommended: **within 1MB, 1000x1000px**; supports JPG/PNG/JPEG/GIF). You can also set a link that opens when the image is clicked.

![Segment message sending steps](../../../../assets/images/ec-訊息推播-lineoa訊息-操作.en.gif){ title="Segment Message Sending Steps" }

## Next Steps { #next-steps-line-segment }

<div class="grid cards" markdown>

- :lucide-zap:{ .lg }   
  [__Advanced Automated Messaging__](../../../app-market/automation/automation-push-flow.md){ title="Create automated messaging flows with AUTOMATION" }  
Set up automatic messages to "VIP Members," "Potential Loyal Customers," or "Dormant Customers," or send reminders for "Abandoned Carts."

</div>

## Frequently Asked Questions { #faq-line-segment }

??? quote "Why do members have UID records but not receive LINE push messages?"
    Message delivery failures usually fall into three main causes. Check them in order:

    1. Customer Status Restrictions (User Side)

        - **Friend relationship ended**: The member once bound a UID, but has since **blocked** the Official Account or **Delete** it from their friend list.
        - **Account is not a friend**: The member only signed in to the website with LINE but has never added your LINE Official Account.

    2. Merchant Settings and Quotas (Merchant Side)

        - **LINE message quota used up**: Check "Message Usage" in the LINE Official Account Manager dashboard. If the free or paid quota for the month has reached its limit, messages cannot be sent.
        - **API connection failure**: Confirm that the Messaging API Channel Access Token is valid. Also check whether a setting was changed in the LINE console and caused the connection to break.

    3. Sending Logic Filters (System Side)

        - **Duplicate sending limit**: If you use an AUTOMATION flow, check whether "Do not resend within a specified number of days" is set. The system automatically excludes members who have recently received a message.

??? quote "How are message quotas calculated for manual sends and AUTOMATION sends?"
    Whether you send a manual push or trigger one through AUTOMATION, both count as Messaging API push messages.

    * Billing follows the LINE Official Account plan you signed up for (low, medium, or high usage).
    * Only successfully sent messages are billed. Messages that fail to send because the member blocked the account are not billed.
