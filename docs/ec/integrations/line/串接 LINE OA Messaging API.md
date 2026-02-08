---
title: 串接 LINE OA Messaging API
version: ""
last_modified: 2026-02-08
description: ""
product:
  - EC
modules: []
activ: ""
paths: []
surfaces: []
ends: []
devices:
  - desktop
  - mobile
apis: []
type: tutorial
intents: []
features: []
tnb: ""
plans: []
prerequisites: []
lang: en-US
sites: []
status:
tags: []
difficulty: ""
audiences: []
wp_url: []
notes: []
comments: ""
search:
  exclude: ""
icon: ""
---

# 串接 LINE OA Messaging API

{ .subtitle }

[:lucide-lock:{ title="適用方案" }](../../resources/conventions#適用方案) | 專業PLUS / 進階PLUS / 高手PLUS / 企業
{ .doc-badge }

{ .hero-page }

## 串接 LINE OA Messaging API 說明

串接 LINE OA Messaging API 可以讓您的官方帳號與 CYBERBIZ 系統整合，實現自動回覆狀態訊息、分眾推播以及讓好友直接在 LINE 中搜尋商品等多元應用。

!!! note "Messaging API 說明"
	LINE 開放給開發者的技術通道。串接後，系統（如 CYBERBIZ）方能根據特定事件（如下單、未付款）**自動** 向顧客發送個人化訊息。

以下為串接 Messaging API 的步驟說明：

## 步驟一：建立與設定 LINE 官方帳號

1. **建立帳號：** 若尚未擁有官方帳號，請前往 [**LINE Official Account Manager** :lucide-external-link:](https://manager.line.biz/?status=success&status=success) 建立，並確保「國家/地區」選擇「台灣」。

2. **啟用 Messaging API：** 在 LINE 官方帳號管理頁面中，點選右上角「設定」→「Messaging API」→「啟用 Messaging API」。

3. **選擇服務提供者 (Provider)：** 選擇您已有的 Provider，或建立一個新的。**請注意：** 務必將「LINE 登入」及「Messaging API」設定於同一個 Provider 中，資料才能互通。

4. **基本資料填寫：** 視需求填入官網的「隱私權政策」與「服務條款」網址。

## 步驟二：取得串接金鑰並回填至 CYBERBIZ

1. **進入開發者後台：** 登入 **LINE Developers** 後台，點進您剛剛建立的 Messaging API 帳號。

2. **複製 Channel 資訊：**

    ◦ 在「Basic settings」頁籤下，複製 **「Channel ID」** 與 **「Channel secret」**。

    ◦ 在「Messaging API」頁籤下，滑到底部點擊「Issue」取得並複製 **「Channel access token」**。

3. **回填至 CYBERBIZ 後台：** 前往 CYBERBIZ 後台 **「第三方整合」→「LINE OA 設定」**，將上述三項金鑰貼入對應欄位並儲存。

## 步驟三：開啟 Webhook 功能（關鍵步驟）

1. **取得 Webhook 網址：** 在 CYBERBIZ 後台的「LINE OA 設定」頁面中，複製系統提供的 **「Webhook URL」**。

    ◦ 網址格式範例：`https://你的網址/line_chat_bots/send_event`。

2. **回填至 LINE 管理台：**

    ◦ 回到 **LINE Official Account Manager** 的「Messaging API」設定頁，貼入 Webhook 網址並儲存。

    ◦ 或是在 **LINE Developers** 的「Messaging API」頁籤下，編輯「Webhook URL」並將 **「Use webhook」** 開關開啟。

3. **回應設定調整：** 在 LINE 官方帳號的「回應設定」中，確認「回應模式」設為「聊天機器人」，並視需求決定是否關閉「自動回應訊息」。


## 後續步驟

<div class="grid cards" markdown>

- :lucide-import:{ .lg }   
  [__批次修改商品設定__](批次修改商品描述與配送設定.md)     
  匯入編輯過的商品 Excel 檔案，同步更新多筆商品的商品描述與配送相關設定。

- :lucide-layout-template:{ .lg }     
  [__LINE OA 訊息樣板設定__](設定超商配送限制與物流排除.md)  
  設定發送給綁定會員的各式 LINE 通知訊息樣板。

</div>

## 步驟四：進階功能應用（選擇性）

• **搜尋商品功能：** 串接完成後，若開啟此功能，LINE 好友可以直接在官方帳號視窗輸入關鍵字搜尋您的官網商品。

• **串接外部系統：** 若您有第三方客服平台（如 Omnichat）需要 LINE API 資料，可在 CYBERBIZ 後台點選「新增轉拋系統」，將資料拋接至其他平台（最多五組）。

• **訊息提醒樣板：** 串接後可開啟「訂單」、「物流」、「顧客」等樣板，當訂單狀態變動時，系統會自動發送 LINE 通知給已綁定會員。

**注意事項**

• **費用標準：** LINE 推播服務會根據 LINE 官方帳號的訊息方案計費，自動傳送的訂單通知亦屬付費項目。

• **會員綁定：** 消費者需先透過 LINE 快速登入或進行「官方帳號綁定官網會員」流程，系統才能收集到 UID 並發送訊息。

• **不可修改限制：** LINE Messaging API channel 與 Provider 綁定後便無法修改，請務必確認連動到正確的 Provider。

## 後續操作

## 常見問題