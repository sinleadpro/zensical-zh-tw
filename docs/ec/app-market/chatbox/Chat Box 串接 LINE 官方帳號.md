---
title: Chat Box 串接 LINE 官方帳號
description: 將 LINE 官方帳號連結至 Chat Box，實現即時對話同步與會員資料比對。
created: 2026-05-28 13:50
last_modified: 2026-05-28 13:50
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: 
  - 內部連結
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - APP MARKET
sites: 
  - TW
audiences: 
  - admin
difficulty: intermediate
tnb: branch
plans: 
  - 專業PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: 
  - CHAT BOX
intents: 
  - 串接_LINE_官方帳號
  - 同步_LINE_對話至_Chat_Box
  - 設定_LINE_Messaging_API
features: 
  - Chat_Box
  - LINE_整合
  - Messaging_API
  - Webhook_設定
prerequisites: 
  - "需擁有 LINE 官方帳號管理員權限"
related: 
  - "[[Chat Box 訊息通]]"
  - "[[LINE 訊息格式規範]]"
tags: 
  - LINE_串接
  - ChatBox
  - Messaging_API
  - 第三方整合
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - LINE Official Account Manager
  - LINE Developers 控制台
paths: 
  - APP MARKET > ChatBox > 設定
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=12966
  - https://www.cyberbiz.io/support/?p=52927
permalink:
comments: false
search:
  exclude: false
icon: simple/line
hide: []
---

# Chat Box 串接 LINE 官方帳號
將 LINE 官方帳號連結至 Chat Box，實現即時對話同步與會員資料比對。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
{ .doc-badge }

!!! tip "應用情境"
    - **對話集中管理**：在 CYBERBIZ 後台直接回覆 LINE 顧客訊息，無需登入 LINE Manager。
    - **識別 LINE 會員**：系統自動比對 LINE 帳號與官網會員，協助客服掌握顧客背景。
    - **提升回覆時效**：透過 Webhook 即時推播，確保不遺漏任何 LINE 諮詢。


## 使用須知

### 串接邏輯說明

Chat Box 採 **自動導入** 機制。系統會自動抓取您於 **第三方整合 > LINE OA 設定** 中所綁定的官方帳號資訊。

- **已完成 LINE OA 串接**：僅需在 Chat Box 內開啟同步開關。
- **尚未完成 LINE OA 串接**：需先完成 Messaging API 串接流程。

### 權限要求

- **管理員權限**：操作人員必須具備該 LINE 官方帳號的 **管理員** 權限。
- **不可逆連動**：一旦 LINE 官方帳號與「服務提供者 (Provider)」連動後，即無法自行變更或解除。
- **Webhook 穩定性**：請務必確保 LINE Developers 中的 **Webhook URL** 正確，且 **Use webhook** 開關處於 **開啟** 狀態，這是訊息推播的唯一通道。


## 串接步驟

### 1. 進入 Chat Box 設定

1. 登入 CYBERBIZ 管理後台，前往 **APP MARKET > ChatBox**。
2. 點擊左側選單最下方的 **設定** 圖示。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-設定01.png){ .screenshot }

### 2. 啟用 LINE 同步

根據您的 LINE 區塊狀態進行操作：

#### 狀態 A：顯示為「已連結」

代表系統已成功對接您的 LINE 官方帳號。
1. 點擊 LINE 區塊內的 **設定**。
2. 開啟官方帳號的 **啟用開關**。開啟後，系統方可開始同步對話。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-line啟用01.png){ .screenshot }

#### 狀態 B：顯示為「未連結」

代表您尚未在後台完成 LINE 官方帳號綁定。

1. 點擊 **設定 > 新增官方帳號**。
2. 系統將自動引導您跳轉至 **第三方整合 > LINE OA 設定**。
3. 請參考 [LINE 官方帳號串接設定]() 完成 Messaging API 串接。






