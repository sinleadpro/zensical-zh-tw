---
title: Chat Box 訊息通
description: 透過單一介面整合多渠道訊息，即時掌握顧客背景與消費紀錄，打造無縫的客服體驗。
created: 2026-05-28 11:45
last_modified: 2026-06-08 17:50
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
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
  - admin
difficulty: beginner
tnb: branch
plans: 
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: 
  - CHAT BOX
intents: 
  - 管理社群訊息
  - 整合客服對話
  - 查看會員訂單
  - 跨平台客服
features: 
  - Chat_Box
  - 訊息整合
  - AI_建議回覆
  - 會員資料同步
prerequisites: 
  - "[[Chat Box 串接第三方平台 (LINE•Meta)]]"
related: 
  - "[[Chat Box AI 建議回覆]]"
  - "[[LINE 訊息格式規範]]"
  - "[[Meta 訊息格式規範]]"
tags: 
  - 客服管理
  - 訊息通
  - ChatBox
  - 社群整合
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
  - APP MARKET > ChatBox
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=12960
  - https://www.cyberbiz.io/support/?p=52927
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/message-square-text
hide: []
---

# Chat Box 訊息通
透過單一介面整合多渠道訊息，即時掌握顧客背景與消費紀錄，打造無縫的客服體驗。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
{ .doc-badge }

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽01.png){ .hero-page }

!!! tip "應用情境"
    - **多平台訊息整合**：統一接收並回覆來自 Facebook、LINE 等管道的對話，無需頻繁切換視窗。
    - **即時背景識別**：自動比對社群帳號與會員資料，客服人員可立即查看顧客電話、信箱及近期訂單。
    - **提升售後效率**：在對話中直接確認出貨進度與退貨狀態，縮短顧客等待時間。
    - **跨平台軌跡追蹤**：確認顧客是否在不同平台提出相同問題，確保資訊對齊。



## 使用須知

- **前置作業**：使用前請先完成第三方平台串接。
- **支援平台**：目前支援 LINE 與 Facebook。
    - [串接 LINE 官方帳號](connect-chat-box-to-line-oa.md)
    - [串接 Facebook 粉絲專頁](connect-chat-box-to-facebook-page.md)
- **資料同步**：在會員明細頁編輯的資料將即時同步至 Chat Box 介面。


## 介面導覽

前往 **APP MARKET > ChatBox** 即可進入管理介面。介面分為四大核心區塊：

| 區塊 | **左側** | **中間(上方)** | **中間(下方)** | **右側** |
| ---- | -------- | --------- | ---------- | ------- | 
| 名稱 | **訊息分類選單** | **對話列表** | **訊息聊天室** | **會員資訊欄位** |
| 說明 | 依據訊息的「讀取狀態」進行分類 | 顯示進線的對話卡片，包含來源平台 Icon、顧客名稱與最後訊息 | 顯示完整歷史對話，並提供文字輸入、圖片/影片上傳與貼圖功能 | 顯示該顧客的基本資料、近期 5 筆訂單及跨平台對話軌跡 |

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽01.png){ .screenshot }



## 操作流程

### 1. 管理與篩選訊息

客服人員可透過左側選單與中間列表快速定位待處理的對話：

- **狀態分類**：優先處理「未讀」訊息以確保回覆即時性。
- **搜尋功能**：支援透過姓名、電話、信箱進行模糊搜尋。
- **篩選與排序**：可依訊息來源（LINE/Meta）篩選，或依進線時間（新到舊/舊到新）排序。

<div class="grid cards borderless two-columns" markdown>

- ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽02.png){ .small-image }
- ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽03.png){ .small-image }

</div>

### 2. 回覆顧客對話

在聊天室中，您可以：

- **發送多媒體**：點擊圖示上傳圖片、影片或檔案。
- **使用 AI 助手**：搭配 [Chat Box AI 建議回覆](chat-box-ai-suggested-replies.md)，由 AI 根據您的資料庫生成客製化回覆草稿。
- **查閱歷史紀錄**：向上捲動即可查看過往所有對話軌跡。

!!! warning "訊息規格限制"
    不同平台支援的訊息格式與政策不一，操作前請參考：
    
    - [LINE 訊息格式規範](line-message-format-spec.md)
    - [Meta 訊息格式規範](meta-message-format-spec.md)

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽04.png){ .small-image }

### 3. 查閱會員與訂單資訊

選取對話後，右側將自動帶入會員資訊：

- **基本資料**：包含名稱、電話、信箱與收件地址。點擊「前往編輯」可直接修改會員明細。
- **近期訂單**：顯示最近 5 筆訂單的編號、狀態、金額與時間。點擊訂單編號可開啟明細頁。
- **更多訂單**：若需查看完整歷史，點擊右下角連結即可另開分頁查詢。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-APPMARKET-CHATBOX-介面導覽05.png){ .small-image }



## 常見問題

??? quote "什麼情況下不同平台的對話會被統整在一起？"
    當同一位會員分別透過 LINE、Facebook Messenger 以及「官網聯絡我們」聯繫時，只要系統能成功比對其會員身分（如透過綁定或相同通訊資料），這些紀錄就會彙整在「所有對話」中。

??? quote "同一個人使用不同 LINE 帳號，對話會出現在一起嗎？"
    不會。由於官網會員採一對一綁定機制（一個會員帳號僅能綁定一個 LINE 帳號），若顧客使用不同的 LINE 帳號聯繫，系統將視為不同來源。

??? quote "「所有對話」顯示「目前尚無對話」代表什麼？"
    代表該顧客目前僅透過單一通路聯繫，或尚未透過 LINE、Facebook 及官網聯絡表單與商家互動。

