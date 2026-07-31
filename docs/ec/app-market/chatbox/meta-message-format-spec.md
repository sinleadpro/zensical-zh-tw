---
title: Meta 訊息格式規範
description: 掌握 Meta (Facebook Messenger) 平台的訊息支援規格與多媒體檔案限制，確保客服溝通順暢無阻。
created: 2026-05-28 12:05
last_modified: 2026-05-28 12:00
lang: zh-TW
type: reference
status: update
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
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: 
  - CHAT BOX
intents: 
  - 確認_Meta_訊息支援類型
  - 了解_Facebook_檔案限制
  - Meta_客服規格
features: 
  - Chat Box
  - Meta 整合
  - 訊息格式
prerequisites: 
  - "ec/app-market/chatbox/index"
related: 
  - "ec/app-market/chatbox/line-message-format-spec"
  - "Chat Box 串接第三方平台 (LINE•Meta)"
tags: 
  - Meta
  - Facebook
  - Messenger
  - 訊息規範
  - 檔案限制
  - ChatBox
acoiv: integration
apis: []
devices: 
  - desktop
ui_components: 
  - 訊息聊天室
paths: 
  - APP MARKET > ChatBox
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

# Meta 訊息格式規範
掌握 Meta (Facebook Messenger) 平台的訊息支援規格與多媒體檔案限制，確保客服溝通順暢無阻。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
{ .doc-badge }


!!! tip "應用情境"
    - **多媒體互動**：利用圖片、影片或語音訊息與顧客進行深度溝通，提升服務品質。
    - **檔案傳輸**：接收或發送 PDF、Excel 等文件，處理訂單證明或產品說明。
    - **規格確認**：在發送行銷素材前，確認檔案大小是否符合 Meta 平台的傳輸限制。



## 使用須知

- **自動轉換**：部分接收的圖片格式（如 GIF）會由系統自動轉換為 JPG 格式以確保相容性。
- **貼圖處理**：顧客傳送的貼圖將自動轉為靜態圖片顯示，且預覽文字會標註為「對方傳送圖片」。



## 支援格式覽表

下表彙整了 Chat Box 訊息通與 Meta 顧客對話時的支援狀況：

| 訊息類型 | 接收 <br>(顧客➔商家) | 發送<br> (商家➔顧客) | 規格與限制 |
| :--- | :---: | :---: | :--- |
| **純文字** | ✓ | ✓ | 支援標準文字與 Emoji |
| **圖片** | ✓ | ✓ | **大小**：< 5 MB<br>**接收**：JPG, JPEG, PNG, GIF (自動轉為 JPG)<br>**發送**：JPG, JPEG, PNG |
| **貼圖** | △ | △ | **接收**：自動轉為靜態圖片。<br>**發送**：僅支援標準 Emoji |
| **語音** | ✓ | ✕ | **格式**：M4A, MP3 |
| **影片** | ✓ | ✓ | **大小**：< 10 MB<br>**格式**：MP4, MOV |
| **檔案** | ✓ | ✓ | **大小**：< 10 MB<br>**格式**：TXT, PDF, DOC/X, XLS/X, PPT/X |




## 各類訊息操作說明

### 圖片與影片

- **放大檢視**：點擊聊天室中的圖片或影片可開啟彈窗放大顯示。
- **多功能操作**：放大彈窗中支援「下載」、「播放速度切換（僅影片）」與「關閉」功能。

### 貼圖訊息

- **靜態顯示**：顧客透過 Facebook 傳送的貼圖僅以圖片形式呈現，無法顯示動態效果。
- **預覽標示**：左側對話列表的預覽文字將統一顯示為「對方傳送圖片」。

### 語音訊息

- **即時播放**：點擊語音訊息條即可直接在介面上播放。
- **進階功能**：支援「播放速度切換」與「下載」功能。

### 檔案傳輸

- **下載儲存**：點擊收到的檔案圖示即可下載至電腦端查看。


