---
title: 設定 LINE 團購機器人
description: ""
created: 2026-03-11 17:27
last_modified:
lang: zh-TW
type: tutorial
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=29174
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/bot
hide:
---

# 設定 LINE 團購機器人


{ .subtitle }

{ .doc-badge }

{ .hero-page }

## 什麼是 LINE 團購機器人

**LINE 團購機器人設定** 是執行 LINE 群組團購功能的基礎。透過設定專屬的團購機器人並將其加入 LINE 群組，成員即可在群組內直接進行購物。

以下是 **LINE 團購機器人設定** 的詳細教學：

## 功能說明與限制

*   **功能目的**：協助商家在 LINE 群組內進行團購活動，並引導成員加入品牌官方帳號好友。
*   **適用環境**：僅限於 **LINE 群組** 或 **多人聊天室**。由於匿名性限制，不支援 LINE 社群 (OpenChat)。
*   **建議做法**：建議將「品牌官方帳號」與「團購機器人帳號」分開建立，以避免功能干擾。兩者應選擇 **同一個服務提供者 (LINE Provider)**，以便用戶資料流通。

---

## 機器人專用 Messaging API 設定

1.  **建立帳號**：至 LINE OA Manager 創建一個專屬團購用的 LINE 官方帳號。
2.  **帳號設定**：於「設定」>「帳號設定」中，將「加入群組或多人聊天室」設為「**接受邀請加入群組或多人聊天室**」。
3.  **回應設定**：在「回應設定」中，將【回應模式】設為「**聊天機器人**」，並**停用**「加入好友的歡迎訊息」與「自動回應訊息」。
4.  **啟用 Messaging API**：點選「啟用 Messaging API」，並選擇與品牌官網相同的 **LINE Provider**。
5.  **串接後台**：

    *   將 LINE 的 Channel 資訊複製到 CYBERBIZ 後台（路徑：**第三方整合** > **LINE 團購機器人設定**）。
    *   將 CYBERBIZ 提供的 **Webhook 網址** 貼回 LINE OA Manager 的 Messaging API 設定中。

6.  **取得 Access Token**：至 LINE Developers 進入該帳號，在「Messaging API」頁籤將 **Use webhook** 開啟，並點擊 Issue 取得 **Channel access token**，貼回 CYBERBIZ 後台並儲存。

---

## 機器人選單設定

*   若您已有經營中的品牌 LINE 官方帳號，請在後台填入其**帳號 ID**。
*   系統會在團購過程中（如主選單、訂單完成頁、感謝訊息）協助引導用戶加入該品牌好友，增加會員數。

---

## LIFF 設定（關鍵步驟）

此設定用於讓機器人能在群組中開啟購物介面：

1.  **建立 Login Channel**：在同一個 LINE Provider 下點選「Create a new channel」，選擇「**LINE Login**」。
2.  **申請權限**：進入該 Channel 的「Basic settings」，在 OpenID Connect 下的「Email address permission」點選 Apply，並勾選項目、上傳隱私權條款截圖後 Submit。
3.  **新增 LIFF**：進入「LIFF」頁籤點選 Add，設定如下：
    *   **Size**：選擇「Tall」。
    *   **Endpoint URL**：輸入 `[您的網址]/liff`。
    *   **Scopes**：全選，且務必將 view all 裡的 **`chat_message.write`** 打開。
4.  **連動 OA**：在「Basic settings」下方的 **Linked OA** 選擇您的「團購機器人帳號」並點擊 Update。
5.  **發布上線**：將取得的 **LIFF ID** 與 **LIFF URL** 貼至 CYBERBIZ 後台，最後將 LINE Developers 狀態由「Developing」改為「**Published**」。

## 後續操作

完成機器人設定後，您還需要接續完成以下兩項設定才能正式營運：

<div class="grid cards" markdown>

- :lucide-package:{ .lg }   
  [__團購商品設定__](){ data-preview }  
  從官網選取商品並設定團購價。

- :lucide-users:{ .lg }     
  [__團購群組設定__](){ data-preview }  
  將機器人加入群組，並設定分潤方案與活動時間。

</div>

## 常見問題

??? quote ""

