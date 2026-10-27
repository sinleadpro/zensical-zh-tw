---
title: "CHAT BOX Messaging"
description: "Bring messages from multiple channels into one interface, see customer background and purchase history in real time, and deliver a seamless customer service experience."
created: 2026-05-28 11:45
last_modified: 2026-07-13 11:45
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
difficulty: beginner
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
  - 管理社群訊息
  - 整合客服對話
  - 查看會員訂單
  - 跨平台客服
features: 
  - CHAT BOX
  - 訊息整合
  - AI 建議回覆
  - 會員資料同步
prerequisites: 
  - "CHAT BOX 串接第三方平台 (LINE•Meta)"
related:
  - ec/app-market/chatbox/connect-chat-box-to-line-oa/
  - ec/app-market/chatbox/connect-chat-box-to-facebook-page/
  - ec/app-market/chatbox/chat-box-ai-suggested-replies/
  - ec/app-market/chatbox/line-message-format-spec/
  - ec/app-market/chatbox/meta-message-format-spec/
tags: 
  - "Customer Service Management"
  - Messaging
  - CHAT BOX
  - "Social Integration"
  - CRM
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 訊息分類選單
  - 對話列表
  - 訊息聊天室
  - 會員資訊欄位
paths:
  - APP MARKET > CHAT BOX
  - LINE OA > 設定 > 回應設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12960
  - https://www.cyberbiz.io/support/?p=52916
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/"
comments: false
search:
  exclude: false
icon: lucide/message-square-text
hide: []
---

# CHAT BOX Messaging
Bring messages from multiple channels into one interface, see each customer's background and purchase history in real time, and deliver seamless customer service.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽01.png){ .hero-page }

!!! tip "Use Cases"
    - **Multi-Platform Messaging**: Receive and reply to conversations from Facebook, LINE, and other channels in one place without switching windows.
    - **Instant Customer Context**: Social accounts are matched with member data automatically, so customer service can see the customer's phone, email, and recent orders right away.
    - **Faster After-Sales Service**: Check shipping progress and return status right in the conversation to shorten wait times.
    - **Cross-Platform History**: See whether a customer asked the same question on different platforms so everyone has the same information.



## Before You Start { #prerequisites-chatbox }

- **Prerequisite**: Connect your third-party platforms before you start.
- **Supported Platforms**: LINE and Facebook are currently supported.
    - [Connect a LINE Official Account](connect-chat-box-to-line-oa.md)
    - [Connect a Facebook Page](connect-chat-box-to-facebook-page.md)
- **Data Sync**: Changes you make on the member details page sync to CHAT BOX instantly.


## Interface Tour { #overview-chatbox }

Go to **APP MARKET > CHAT BOX** to open the management interface. It has four main areas:

| Area | **Left** | **Center (Top)** | **Center (Bottom)** | **Right** |
| ---- | -------- | --------- | ---------- | ------- |
| Name | **Message Category Menu** | **Conversation List** | **Chat Room** | **Member Info Panel** |
| Description | Sorts messages by read status | Shows incoming conversation cards with the source platform icon, customer name, and last message | Shows the full conversation history and lets you type text, upload images/videos, and send stickers | Shows the customer's basic info, 5 most recent orders, and cross-platform conversation history |

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽01.png){ .screenshot }



## How to Use { #operate-chatbox }

### 1. Manage and Filter Messages { #operate-chatbox-1-manage-message }

Use the left menu and the center list to find conversations that need attention:

- **Status Categories**: Handle "Unread" messages first so you reply on time.
- **Search**: Search by name, phone, or email (partial matches supported).
- **Filter and Sort**: Filter by message source (LINE/Meta) or sort by time received (newest first/oldest first).

<div class="grid cards borderless two-columns" markdown>

- ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽02.png){ .small-image }
- ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽03.png){ .small-image }

</div>

!!! info "Read Status Sync"
    The **Read** status in CHAT BOX is for internal customer service use only. The system does not sync it to the customer's LINE chat.

    To control whether customers see a read receipt, change the setting in the LINE OA manager:

    - Show read automatically: Go to **設定 > 回應設定** and set **Chat** mode to `關閉`.
    - Do not show read automatically: Set **Chat** mode to `開啟`.

    ![](../../../assets/images/lineoa-後台-設定-回應設定-chatbox已讀狀態同步設定01.en.png){ .small-image }


### 2. Reply to Customers { #operate-chatbox-2-reply }

In the chat room, you can:

- **Send Media**: Click the icon to upload images, videos, or files.
- **Use the AI Assistant**: With [CHAT BOX AI Suggested Replies](chat-box-ai-suggested-replies.md), AI drafts custom replies based on your knowledge base.
- **View History**: Scroll up to see all past conversations.

!!! warning "Message Format Limits"
    Each platform supports different message formats and policies. Before you start, see:

    - [LINE Message Format Specifications](line-message-format-spec.md)
    - [Meta Message Format Specifications](meta-message-format-spec.md)

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽04.png){ .small-image }

### 3. View Member and Order Information { #operate-chatbox-3-member-order }

When you select a conversation, member information appears on the right:

- **Basic Info**: Name, phone, email, and shipping address. Click "Go to Edit" to change the member details directly.
- **Recent Orders**: Shows the number, status, amount, and time of the 5 most recent orders. Click an order number to open its details page.
- **More Orders**: To see the full history, click the link at the bottom right to open it in a new tab.

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽05.png){ .small-image }



## FAQ { #faq-chatbox }

??? quote "When are conversations from different platforms combined?"
    When the same member contacts you through LINE, Facebook Messenger, and the store's "Contact Us" form, these records are combined under "All Conversations" as long as the system can match the member (for example, through binding or the same contact details).

??? quote "If one person uses different LINE accounts, will their conversations appear together?"
    No. Each store member account can be bound to only one LINE account, so if a customer contacts you from a different LINE account, the system treats it as a different source.

??? quote "What does "No conversations yet" under "All Conversations" mean?"
    It means the customer has contacted you through only one channel, or has not yet contacted you through LINE, Facebook, or the store's contact form.

