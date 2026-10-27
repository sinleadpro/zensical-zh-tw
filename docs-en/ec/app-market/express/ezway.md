---
title: "EZWAY Subscription Service"
description: "Turn on the EZWAY subscription service to track customs declaration progress for cross-border orders. Set up automated SMS reminders that guide customers through real-name verification, and track customs status and sending records in the admin in real time."
created: 2026-07-23 17:45
last_modified: 2026-07-23 17:45
lang: en-US
type: guide
status: ""
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
  - JP
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - global_advanced
plan_options: []
cyb_extensions:
  - EXPRESS
intents: 
  - 如何完成 EZWAY 認證
  - 解決海關申報問題
  - 實名認證註冊流程
features: 
  - EZWAY 實名認證
  - 海關申報相符
prerequisites: 
  - 需具備台灣手機門號與身分證件
related:
  - ec/app-market/express/cyberbiz-express-japan-to-taiwan-delivery/
  - ec/app-market/express/cyberbiz-express-711/
tags: 
  - EZWAY
  - "Real-Name Verification"
  - "Cross-Border Shopping"
  - Customs
acoiv: operation
apis: []
devices: []
ui_components: 
  - 申報相符
  - 實名註冊
paths:
  - APP MARKET > 我的擴充功能 > CYBERBIZ EXPRESS
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/express/ezway/"
comments: false
search:
  exclude: false
icon: lucide/shield-check
hide: []
---
# EZWAY Subscription Service
Turn on the EZWAY subscription service to track declaration progress for cross-border orders. Set up automated SMS reminders that guide customers through real-name verification, and track customs status and message history in the admin in real time.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Cross-Border E-Commerce (Japan to Taiwan)<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ EXPRESS
{ .doc-badge }

## Before You Start { #prerequisites-ezway }

- **Supported Delivery Methods**: [CYBERBIZ EXPRESS Home Delivery](cyberbiz-express-japan-to-taiwan-delivery.md), CYBERBIZ LINEX, and [CYBERBIZ EXPRESS Store Pickup](cyberbiz-express-711).
- **Unsupported Delivery Methods**: EMS Japan Post (no declaration confirmation required)



## About the EZWAY Subscription Service { #overview-ezway }

Customs procedures for **Japan-to-Taiwan** cross-border e-commerce can be complicated, so CYBERBIZ provides an automated EZWAY management tool. With it, you can track each parcel's declaration confirmation progress in one place and remind customers automatically at key moments, greatly reducing the risk of parcels getting stuck in customs.


- **Automatic Declaration Tracking**: The system syncs with Trade-Van and customs systems and turns complex customs procedures into easy-to-understand status labels.
- **Two-Step Reminders**: For customers who have not completed **declaration confirmation**, the system can send reminder SMS messages automatically, guiding them to confirm in the EZWAY app and speeding up clearance.
- **Lower Customer Service Costs**: With real-time update times and declaration stages in the admin, your customer service team can quickly see why a parcel is held and answer customer questions accurately.

## EZWAY Pricing { #specs-ezway }

This feature combines a subscription with pay-as-you-go fees:

| Item | Type | When Charged | Billing Model | Payment Method |
| ---- | ---- | ------- | ------- | -------- |
| **Monthly Fee** | Fixed fee | First subscription/resubscribing after expiration: When you subscribe<br>Auto-renewal/resubscribing before expiration: On the expiration date | Monthly | Included on your statement |
| **Order Lookup Fee** | Variable fee | When Trade-Van successfully receives the order data | Per order | CYBER Coins |
| **SMS Notification Fee** | Variable fee | When an SMS is sent | Per message sent | CYBER Coins |

> For detailed pricing plans, contact your CYBERBIZ store consultant.


## Subscribe { #operate-ezway }


1. Go to **APP MARKET > 我的擴充功能 > CYBERBIZ EXPRESS** and select the **EZWAY** tab.

2.  **Start the Subscription**: Click **Start Subscription**.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-訂閱EZWAY01.en.png){ .screenshot }

3.  **Confirm Fees and Check Out**: Review the subscription details and click **Confirm Checkout**.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-訂閱EZWAY02.en.png){ .screenshot }

4.  **Subscription Activated**:

    After checkout, the system turns on these features automatically:

    - **EZWAY Declaration Notifications**: Sends SMS reminders to customers.
    - **EZWAY Status Lookup**: Syncs declaration progress on the Tracking Number tab in real time.

5.  **Renewal and Validity**:
    - **Auto-Renewal**: Unless you cancel, the subscription renews automatically at the end of each period.
    - **Cancellation Rules**: After you cancel, the service stops at the **next billing cycle**. You can keep using features already paid for until the current period ends.



## Cancel Your Subscription { #intro-ezway }

To stop this feature, click **Cancel Subscription**:


*   **Renewal Stops**: Automatic charges stop from the next billing cycle.
*   **No Service Interruption**: For orders placed during the current period, the system keeps sending SMS notifications and syncing EZWAY declaration status until the current period ends.

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-取消訂閱EZWAY01.en.png){ .screenshot }


## Resubscribe { #intro-subscription-renew }

To restore the service, click **Resubscribe**. When you are charged depends on your service status:


*   **Resume Before Expiration (Service Not Yet Ended)**: The original subscription cycle continues. You are not charged again now, and normal charges resume at the next renewal.
*   **Restart After Expiration (Service Ended)**: This counts as a new subscription. Features turn on immediately, and the monthly fee for the current period is charged.

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-重新訂閱EZWAY01.en.png){ .screenshot }



## Send Declaration Confirmation Reminder SMS { #operate-compliance-sms }


### Two-Message Reminders { #operate-compliance-sms-sms-send }

After an order is placed, if the customer has not confirmed the declaration, the system can send two SMS reminders:


| **Item** | **How It Is Sent** | **When It Is Sent** |
| -------- | ----------- | ----------- |
| **First Message** | Sent automatically | When the customs broker uploads documents to the customs system (parcels without declaration confirmation cannot clear customs at this point) |
| **Second Message** | Optional, turned on by you | Sent at your chosen interval after the first message |

### Send a Second Message { #operate-compliance-sms-send-sms }

To turn on the second reminder, select "Enable second SMS reminder" and choose the interval between the two messages.

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-開啟第二次通知功能01.en.png){ .screenshot }

### SMS Notes { #operate-compliance-sms-section }

*   **Timing Variance**: Because of system scheduling, messages may be sent **5–10 minutes** earlier or later than your set interval.
*   **Quiet Hours**: To avoid disturbing recipients, messages are sent only between 08:00 and 22:00 Taiwan time.
    *   **Delayed Sending**: If a message is triggered outside service hours (22:01–07:59), the system schedules it and sends queued messages in batches after 08:00 the next day.
    *   **Scope**: This rule applies to both the first and second reminders.


## View SMS Notification History { #reference-ezway }

On the **Tracking Number** tab, track SMS history with these fields:

*   **SMS Notification Status**: Shows whether a notification was sent for the order and how many messages were sent in total.
*   **SMS Notification Time**: Records when the most recent message was sent successfully, so you can track reminder timing.

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-查看簡訊通知狀態01.en.png){ .screenshot }



### SMS Notification Status Reference { #reference-ezway-sms-notifications-status }

| **Option** | **Description** |
| ----------- | --------- |
| **Not Notified** | The system has not sent an EZWAY declaration reminder SMS |
| **First Notification** | The system sent the first EZWAY declaration reminder SMS to the recipient |
| **Second Notification** | The system sent the second EZWAY declaration reminder SMS to the recipient |
| **(Blank)** | This delivery method does not use EZWAY real-name declaration |


## View EZWAY Declaration Progress { #operate-ezway-status }

On the **Tracking Number** tab, track parcel declaration progress with these fields:

*   **EZWAY Status**: Shows the order's current declaration stage in real time so the parcel clears customs smoothly
*   **EZWAY Update Time**: Records when the system last synced customs information, so you can tell how current it is

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-查看EZWAY狀態01.en.png){ .screenshot }



## EZWAY Status and Customs Process Reference { #specs-ezway-status-flow }

| **Option** | **Customs Step** | **Customs Process/Description** |
| ----------- | ------------ | ---------------- |
| **Order Not Uploaded** | 1 | The order was placed; the system will upload the order information to Trade-Van shortly |
| **Order Uploaded** | 2 | The order data was sent to Trade-Van and is waiting for a response |
| **Confirmed by Trade-Van** | 3 | Trade-Van received the order data; waiting for the EZWAY declaration status to update |
| **Declaration Not Confirmed** | 4 | The customs broker uploaded the pre-authorization data, but the recipient has not tapped "Confirm Declaration" in the EZWAY app. Customs declaration can proceed only after this is done |
| **Declaration Confirmed** | 5 | The recipient tapped "Confirm Declaration" in EZWAY; waiting for customs review |
| **Authorization Confirmed by Customs** | 6 | Customs approved the pre-authorization; the customs broker can upload the formal declaration data |
| **Declaration Data Uploaded** | 7 | The customs broker uploaded the formal declaration data; customs can start clearance |
| **Overdue, Not Confirmed** | Special case | The recipient has not confirmed the EZWAY declaration for more than 14 days, which may affect customs processing and cause parcel holding fees |
| **Phone Mismatch** | Special case | The phone number in the declaration data uploaded by the customs broker does not match the order recipient's phone number. Check the EZWAY information |
| **Checking** | Special case | The system cannot get the latest EZWAY status right now and will check again automatically. Check back later |
| **(Blank)** | Other | This delivery method does not use EZWAY real-name declaration |

