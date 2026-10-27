---
title: "LINE Message Format Specifications"
description: "Learn the message formats and media file limits supported on LINE to keep customer service communication running smoothly."
created: 2026-05-28 11:55
last_modified: 2026-05-28 11:52
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
  - 確認_LINE_訊息支援類型
  - 了解_LINE_檔案限制
  - LINE_客服規格
features: 
  - CHAT BOX
  - LINE 整合
  - 訊息格式
prerequisites:
  - ec/app-market/chatbox/
related: []
tags: 
  - LINE
  - "Message Specifications"
  - "File Limits"
  - "Customer Service Specifications"
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
  - https://www.cyberbiz.io/helpcenter/?p=12961
  - https://www.cyberbiz.io/support/?p=52921
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/line-message-format-spec/"
comments: false
search:
  exclude: false
icon: simple/line
hide: []
---

# LINE Message Format Specifications
Learn which message types and media file limits the LINE platform supports so customer service runs smoothly.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHAT BOX
{ .doc-badge }


!!! tip "Use Cases"
    - **Media Interaction**: Use images, videos, or voice messages to communicate in depth with customers and improve service.
    - **File Transfer**: Receive or send PDF, Excel, and other files for order proof or product information.
    - **Check Specifications**: Before sending marketing materials, make sure the file size is within LINE's transfer limits.


## Before You Start { #prerequisites-line-format }

- **Copyright Restrictions**: Due to LINE's policies, some copyrighted stickers may not display fully in third-party interfaces such as CHAT BOX.
- **Automatic Conversion**: Some received image formats (such as GIF) are converted to JPG automatically for compatibility.



## Supported Formats { #intro-line-format }

The table below shows what CHAT BOX supports in conversations with LINE customers:

| Message Type | Receive <br>(Customer➔Merchant) | Send <br>(Merchant➔Customer) | Specifications and Limits |
| :--- | :---: | :---: | :--- |
| **Text** | ✓ | ✓ | Supports standard text and emoji |
| **Image** | ✓ | ✓ | **Size**: < 5 MB<br>**Receive**: JPG, JPEG, PNG, GIF (converted to JPG)<br>**Send**: JPG, JPEG, PNG |
| **Sticker** | ✕ | △ | **Send**: Standard emoji only; LINE stickers are not supported |
| **Emoji Sticker** | ✕ | ✕ | Shows only the emoji sticker's name as text |
| **Voice** | ✓ | ✕ | **Format**: M4A, MP3 |
| **Video** | ✓ | ✓ | **Size**: < 10 MB<br>**Format**: MP4, MOV |
| **File** | ✓ | ✓ | **Format**: TXT, PDF, ZIP, DOC/X, XLS/X, PPT/X |
| **Contact Info** | ✕ | ✕ | Not supported yet |
| **Location** | ✕ | ✕ | Not supported yet |


## How Each Message Type Works { #operate-line-format }

### Images and Videos { #operate-line-format-section }

- **Enlarge**: Click an image or video in the chat room to open it in a larger pop-up.
- **More Actions**: The pop-up supports "Download", "Playback Speed (video only)", and "Close".

### Voice Messages { #operate-line-format-message }

- **Instant Playback**: Click the voice message bar to play it right in the interface.
- **More Features**: Supports "Playback Speed" and "Download".

### File Transfer { #operate-line-format-file }

- **Download**: Click a received file icon to download it to your computer.

### Unsupported Messages { #operate-line-format-support-message }

- **Stickers**: If a customer sends a LINE sticker, the system shows "Sticker messages cannot be displayed".
- **Emoji Stickers**: If a customer sends an emoji sticker, the system shows the sticker's name as text.


