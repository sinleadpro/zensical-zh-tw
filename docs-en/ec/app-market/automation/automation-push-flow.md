---
title: "Create Automated Push Flows with AUTOMATION"
description: "Create automated flows in CYBERBIZ AUTOMATION, set up member segments, and send SMS, EDM, or LINE OA messages."
created: 2026-03-09 14:48
last_modified: 2026-07-22 15:47
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 行銷活動
  - APP MARKET
sites:
  - TW
audiences:
  - merchant
difficulty:
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
  - 建立自動化推播流程
  - 自動化行銷設定
  - 會員分群推播
features:
  - "SMS Sending"
  - EDM 發送
  - LINE OA 訊息發送
  - "Member Segments"
  - 成效追蹤
prerequisites:
  - ec/notifications/send-edm-newsletters-v2/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
related:
  - ec/notifications/send-edm-newsletters-v2/
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
tags:
  - AUTOMATION
  - "Marketing Automation"
  - "Push Flows"
  - 會員分群
  - 簡訊發送
  - EDM
  - "LINE OA"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - APP MARKET > 我的擴充服務 > CYBERBIZ AUTOMATION
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7955
  - https://www.cyberbiz.io/support/?p=38638
  - https://www.cyberbiz.io/support/?p=38837
permalink: "https://help.cyberbiz.io/ec/app-market/automation/automation-push-flow/"
search:
  exclude: false
icon: lucide/zap
hide: []
comments: false
---

![AUTOMATION App](../../../assets/images/ec-app-market-我的擴充服務-automation.en.png){ title="AUTOMATION App" .hero-page }

## About AUTOMATION Push Flows { #overview-automation-push }

**CYBERBIZ AUTOMATION** is an automated workflow tool built for merchants. It simplifies marketing and operations setup and makes your business more efficient.

## Before You Start: Create Custom Member Segments { #prerequisites-automation-push }

!!! warning "Improve Message Reach"
    AUTOMATION only pushes messages to members who have **opted in to the newsletter**. To make the preview count closer to the actual send, filter for members who are willing to receive promotions (Subscribed to Store Promotions) first when you set up member segments. The final reach may still vary slightly if customers unsubscribe in the meantime.

Before you create an automated flow, define your audience. The system only pushes messages to members who **opted in to the newsletter/store promotions**.

1.  **Admin Path**: "Members" > "All Members".
2.  **Set Conditions**: Click "Add Filter" or use a "Template" (such as loyal, dormant, or abandoned-cart members).

    ![Member segment templates](../../../assets/images/ec-會員-所有會員-會員分群範本.en.png){ title="Member Segment Templates" }

3.  **Save the Segment**: After you confirm the list, click "Save" and enter a segment name and description. If the filter includes LINE login or LINE binding, you can choose to upload the audience to LINE as well.

    ![AUTOMATION member segment](../../../assets/images/ec-會員-所有會員-automation會員分群.en.gif){ title="AUTOMATION Member Segment" }

## AUTOMATION Setup <small>SMS/EDM/LINE OA</small> { #operate-automation-push }

To open the settings, log in to the admin and go to **APP MARKET > My Apps > CYBERBIZ AUTOMATION**.

### SMS Settings { #operate-automation-push-send-sms }

*   **Create a Flow**: Click "Create Flow" and choose a preset segment flow (such as sending SMS to VIP or dormant customers).
*   **Edit Content**:
    *   **Schedule Trigger**: Set it to "Once" or "Recurring" (for example, send once a week).

        ![SMS schedule trigger](../../../assets/images/ec-app-market-automation-簡訊-排程觸發.en.png){ title="SMS Schedule Trigger" }

    *   **Member Filter**: Select a member segment you set up earlier.

        ![SMS member filter](../../../assets/images/ec-app-market-automation-簡訊-會員篩選.en.png){ title="SMS Member Filter" }

    *   **SMS Content**: Enter your text. Always use a **CYBERBIZ store URL** for links so you can track results, and click "Preview SMS" to check the length (up to 70 characters).

        ![SMS content editor](../../../assets/images/ec-app-market-automation-簡訊-簡訊內容.en.png){ title="SMS Content Editor" }

    *   **Repeat Sending**: Choose "Allow", "Do Not Allow", or "Do not resend within a set number of days" to the same recipients.


---

### EDM Settings { #operate-automation-push-edm-send-settings }

*   **Prerequisite**: You must first complete the [EDM basic settings](../../notifications/send-edm-newsletters-v2.md){ title="Set Up and Send EDM Newsletters" }.
*   **Steps**: The flow is the same as the [SMS settings](#operate-automation-push-send-sms).
    1.  Choose a preset EDM template (such as sending an EDM to VIPs or a custom segment).
    2.  Set the schedule and member filter.
    3.  **EDM Send Block**: Pick an EDM template you have already edited and complete the repeat-sending settings.

        ![EDM content selection](../../../assets/images/ec-app-market-automation-EDM-EDM內容.en.png){ title="EDM Content Selection" }

---

### LINE OA Message Settings { #operate-automation-push-line-oa-message }

*   **Requirements**: Members must have completed **LINE [login](../../integrations/line/account-integration/setup-line-quick-login.md){ title="Set Up LINE Quick Login" } or [binding](../../integrations/line/account-integration/bind-line-oa-store-members.md){ title="Link LINE Official Account and Store Members" }** and must be **LINE OA friends**. Make sure your LINE OA message quota is sufficient.
*   **Steps**: The flow is the same as the [SMS settings](#operate-automation-push-send-sms).
    1.  Choose a preset LINE OA template (such as an abandoned-cart reminder).
    2.  **Message Blocks**: Choose "Image" or "Text". You can send up to **3 blocks** at a time.
    3.  **URL Tracking**: As with SMS, use store URLs so you can analyze results.

        ![LINE OA message content](../../../assets/images/ec-app-market-automation-lineoa-lineoa內容.en.png){ title="LINE OA Message Content" }


## Start and Track Flows { #operate-flow-enable }

!!! tip "Tip"
    A complete automated workflow is built from trigger nodes (time/event), condition nodes (filters), and action nodes (specific actions).

1.  **Start the Flow**: When setup is complete, click "Start Flow". The system shows the estimated number of recipients.

    ![Start flow](../../../assets/images/ec-app-market-automation-lineoa-開始流程.en.png){ title="Start Flow" }

2.  **Monitor Status**:
    *   **Draft**: You can edit or delete it at any time.
    *   **Scheduled/Running**: To make changes, click "Pause Flow".
    *   **Completed/Failed**: After sending, the system sends a record to the "[notification email](#operate-notifications-settings)" addresses you set (up to 10 people).

    ??? note "Flow Status Details"
        | Status | Definition | Scenario |
        | :--- | :--- | :--- |
        | **Draft** | 流程還在可以編輯的狀態<br>右側按鈕為「開始流程」 | 1. 尚未點擊「開始流程」<br>2. 點擊「暫停流程」<br>3. 點擊「重新編輯」<br>4. **Only flows in Draft status can be deleted** |
        | **Scheduled** | The flow is scheduled<br>The button on the right is "Pause Flow" | You clicked "Start Flow" and the current time is earlier than the start time |
        | **Running** | The flow has started running<br>The button on the right is "Pause Flow" | You clicked "Start Flow" and the current time is later than the trigger node's start time |
        | **Failed** | The flow failed, and nodes cannot be edited<br>The button on the right is "Edit Again" | 1. API call failed (timeout, cannot reach EC, wrong response, batch sending failed, etc.)<br>2. Filter group not found<br>3. Sending failed for the reasons above<br>4. Later schedules must be canceled |
        | **Completed** | 流程執行完成，此時不可編輯節點<br>右側按鈕為 disabled 的「暫停流程」 | **Fixed schedule:** Sent successfully and the current time is later than the start time<br>**Other schedules:** Sent successfully and the current time is later than the end time<br>*If the SMS provider sends some messages successfully and some fail, the flow still counts as Completed |

3.  **Track Results**: Click "Performance Tracking" in the flow interface. Data updates within about **12 hours**.

    ![Performance tracking](../../../assets/images/ec-app-market-automation-成效追蹤.en.gif){ title="Performance Tracking" }

4. **View Flow Records**: Click "View Flow Records" in the flow interface to see the flow's run history.

    ![View flow records](../../../assets/images/ec-app-market-automation-查看流程紀錄.en.gif){ title="View Flow Records" }


## Notification Email Settings { #operate-notifications-settings }

After AUTOMATION sends messages, CYBERBIZ emails the "notification recipients" to report whether sending succeeded or failed.

1. Click "Notification Email Settings" > "Add Notification Email" on the left.
2. Add the email address and click Confirm.

![Notification email settings](../../../assets/images/ec-app-market-automation-notification-email-settings.en.png){ title="Notification Email Settings" }

!!! info "You can add up to 10 notification recipients."


## FAQ { #faq-automation-push }

??? quote "Why does my automated flow show "Completed" when members say they did not receive the SMS?"
    Check these three things:

    1. **Subscription Status**: The system only sends to members who "opted in to the newsletter/store promotions".
    2. **SMS Quota**: Make sure you have enough SMS credits in the admin.
    3. **Phone Blocklist**: Some customers may have asked their carrier to block marketing SMS.

??? quote "What are common reasons LINE OA messages fail to send?"
    The most common reasons are an **insufficient LINE Official Account message quota** or **the member has not linked (bound) a LINE account**. The system also cannot push messages to members who have blocked your official account.

??? quote "Can I change an automated flow after it is set up?"
    Yes. But you must first click "**Pause Flow**" to switch the status back to "Draft" before you can edit nodes. When you finish editing, be sure to click "**Start Flow**" again to resume the schedule.
