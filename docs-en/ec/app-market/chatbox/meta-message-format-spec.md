---
title: "Meta Message Format Specifications"
description: "Learn the message formats and media file limits supported on Meta (Facebook Messenger) to keep customer service communication running smoothly."
created: 2026-05-28 12:05
last_modified: 2026-05-28 12:00
lang: en-US
type: reference
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
  - 確認_Meta_訊息支援類型
  - 了解_Facebook_檔案限制
  - Meta_客服規格
features: 
  - CHAT BOX
  - Meta 整合
  - 訊息格式
prerequisites:
  - ec/app-market/chatbox/
related: []
tags: 
  - Meta
  - Facebook
  - Messenger
  - "Message Specifications"
  - "File Limits"
  - CHAT BOX
acoiv: integration
apis: []
devices: 
  - desktop
ui_components: 
  - 訊息聊天室
paths: 
  - APP MARKET > CHAT BOX
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=12964
  - https://www.cyberbiz.io/support/?p=53079
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/meta-message-format-spec/"
comments: false
search:
  exclude: false
icon: simple/facebook
hide: []
---

# Meta Message Format Specifications
Learn which message types and media file limits the Meta (Facebook Messenger) platform supports so customer service runs smoothly.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }


!!! tip "Use Cases"
    - **Media Interaction**: Use images, videos, or voice messages to communicate in depth with customers and improve service.
    - **File Transfer**: Receive or send PDF, Excel, and other files for order proof or product information.
    - **Check Specifications**: Before sending marketing materials, make sure the file size is within Meta's transfer limits.



## Before You Start { #prerequisites-meta-format }

- **Automatic Conversion**: Some received image formats (such as GIF) are converted to JPG automatically for compatibility.
- **Sticker Handling**: Stickers sent by customers are shown as static images, and the preview text reads "Sent an image".



## Supported Formats { #intro-meta-format }

The table below shows what CHAT BOX supports in conversations with Meta customers:

| Message Type | Receive <br>(Customer➔Merchant) | Send<br> (Merchant➔Customer) | Specifications and Limits |
| :--- | :---: | :---: | :--- |
| **Text** | ✓ | ✓ | Supports standard text and emoji |
| **Image** | ✓ | ✓ | **Size**: < 5 MB<br>**Receive**: JPG, JPEG, PNG, GIF (converted to JPG)<br>**Send**: JPG, JPEG, PNG |
| **Sticker** | △ | △ | **Receive**: Converted to a static image.<br>**Send**: Standard emoji only |
| **Voice** | ✓ | ✕ | **Format**: M4A, MP3 |
| **Video** | ✓ | ✓ | **Size**: < 10 MB<br>**Format**: MP4, MOV |
| **File** | ✓ | ✓ | **Size**: < 10 MB<br>**Format**: TXT, PDF, DOC/X, XLS/X, PPT/X |




## How Each Message Type Works { #operate-meta-format }

### Images and Videos { #operate-meta-format-image-video }

- **Enlarge**: Click an image or video in the chat room to open it in a larger pop-up.
- **More Actions**: The pop-up supports "Download", "Playback Speed (video only)", and "Close".

### Sticker Messages { #operate-meta-format-message }

- **Static Display**: Stickers sent through Facebook appear only as images, without animation.
- **Preview Label**: The preview text in the conversation list on the left always reads "Sent an image".

### Voice Messages { #operate-meta-format-audio }

- **Instant Playback**: Click the voice message bar to play it right in the interface.
- **More Features**: Supports "Playback Speed" and "Download".

### File Transfer { #operate-meta-format-file }

- **Download**: Click a received file icon to download it to your computer.


