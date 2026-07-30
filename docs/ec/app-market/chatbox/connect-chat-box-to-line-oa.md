---
title: Chat Box 串接 LINE 官方帳號
description: 將 LINE 官方帳號連結至 Chat Box，實現即時對話同步與會員資料比對。
created: 2026-05-28 13:50
last_modified: 2026-05-28 13:50
lang: zh-TW
type: tutorial
status: update
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
  - 進階PLUS
  - 高手PLUS
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
  - 需擁有 LINE 官方帳號管理員權限
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
permalink: "https://help.cyberbiz.io/ec/app-market/chatbox/connect-chat-box-to-line-oa/"
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
3. 請參考 [LINE 官方帳號串接設定](../../integrations/line/account-integration/connect-line-messaging-api.md) 完成 Messaging API 串接。


## 常見問題

??? quote "顧客傳 LINE 訊息後，LINE 官方帳號後台有訊息，但 Chat Box 沒有出現新對話或新訊息？"
    常見原因是 Webhook 未啟用，或 Webhook URL 設定錯誤。

    Chat Box 接收 LINE 訊息主要依賴 LINE Messaging API Webhook。若 Webhook 沒有啟用，或 Webhook URL 不是 CYBERBIZ 提供的正確網址，即使 LINE 官方帳號後台看得到訊息，Chat Box 也可能收不到訊息。

    請依照以下方式檢查：

    1. 進入 LINE 官方帳號後台。
    2. 點選「設定」。
    3. 進入「回應設定」。
    4. 確認 Webhook 是否為「啟用」。

    同時也請至 LINE Developers Console 檢查：

    - Webhook URL 為 CYBERBIZ 提供的正確網址。
    - Webhook URL 驗證成功。
    - **Use webhook**  已啟用。

??? quote "LINE OA 的歷史對話紀錄會顯示在 Chat Box 嗎？"
    不會自動顯示。LINE 串接後，Chat Box 通常只會接收 **串接完成且 Webhook 生效之後** 的新訊息。串接前已存在於 LINE 官方帳號後台的歷史對話，不會自動同步到 Chat Box。建議串接完成後，請使用一般 LINE 用戶傳送一則新的測試訊息，確認 Chat Box 是否能正常收到新訊息。

??? quote "如果商家已經在使用外部服務，要如何同時串接外部服務與 CYBERBIZ Chat Box？"
    LINE 官方目前只提供一組 Webhook 設定，因此正常情況下，如果商家將 LINE Webhook 改為串接 CYBERBIZ Chat Box，原本的外部服務就可能無法再收到 LINE 訊息。

    若商家希望 Chat Box 與其他外部服務都能同時收到 LINE 訊息，可以使用 CYBERBIZ 提供的 LINE Webhook 轉拋服務。

    設定完成後，LINE Webhook 會先將資料送至 CYBERBIZ，再由 CYBERBIZ 將資料轉拋至其他外部服務。如此一來，CYBERBIZ Chat Box 與其他外部服務都能接收到 LINE 訊息。

    詳細設定可參考 [LINE webhook 轉拋服務](../../integrations/line/account-integration/connect-line-messaging-api/#步驟三開啟-webhook-功能)。

??? quote "為什麼 Chat Box 不會顯示 LINE 貼圖？"
    因為 LINE 官方目前沒有正式支援串接平台完整顯示貼圖內容。

    因此，透過 LINE 串接到 Chat Box 的訊息，可能無法像 LINE 官方帳號後台一樣完整顯示貼圖。

??? quote "透過 Chat Box 回覆 LINE 對話會產生費用嗎？"
    LINE 訊息費用會依照商家的 LINE 官方帳號方案計算，Chat Box 不會另外針對 LINE 對話收取額外訊息費用。若商家的 LINE 官方帳號方案有訊息量限制或超量費用，仍會依 LINE 官方規則計算。

??? quote "在 LINE OA 的留言Chatbox沒有出現？"
    在 LINE OA 後台回覆給客人的訊息不會進入到 Chatbox。