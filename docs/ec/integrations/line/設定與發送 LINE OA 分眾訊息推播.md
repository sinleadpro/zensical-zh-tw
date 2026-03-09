---
title: 設定與發送 LINE OA 分眾訊息推播
description: ""
created: 2026-03-09 09:48
last_modified:
lang: ""
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
  - merchant
difficulty: ""
tnb: ""
plans:
cyb_extensions:
  - AUTOMATION
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
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/message-square-share
hide:
aliases: []
id: 設定與發送 LINE OA 分眾訊息推播
---

# 設定與發送 LINE OA 分眾訊息推播


{ .subtitle }

[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | AUTOMATION 
{ .doc-badge }

{ .hero-page }

## LINE OA 分眾訊息推播說明

**「LINE OA 分眾訊息推播」** 功能讓商家可以針對特定標籤的會員發送精準訊息，提升轉換率並節省不必要的訊息費用。

以下為詳細的操作說明與教學：

## 前置必要作業

在使用分眾推播功能前，必須確保完成以下設定：

- [x] [**串接 Messaging API**](串接 LINE Messaging API.md){ data-preview }：商家必須先完成 LINE Messaging API 的串接設定，方可透過 CYBERBIZ 後台發送訊息。
- [x] **收集會員 UID**：訊息僅能發送給曾透過 **「[LINE 快速登入](設定 LINE 快速登入.md){ data-preview }」** 或 **「[已綁定 LINE OA](綁定 LINE 官方帳號與官網會員.md){ data-preview }」** 的官網會員，因為這些行為才會在官網系統留下發送訊息所需的 UID。
- [x] **好友狀態確認**：僅有 **LINE OA 的好友**（且未封鎖官方帳號者）才能成功收到訊息。
- [x] **訊息費用**：LINE 推播服務會根據您在 LINE 官方帳號設定的訊息方案計費，手動推播與自動通知皆屬付費項目，僅發送成功的訊息會計費。

## 手動發送分眾訊息步驟

1.  **後台路徑**：進入管理後台，點選 **訊息推播 > LINE OA 發送訊息**。
2.  **設定顧客標籤**：在「顧客標籤」欄位勾選您欲傳送的對象（此為必填）。系統會自動篩選出符合標籤且具備 UID 的會員。
3.  **選擇發送類型**（一次僅能選擇一種模式）：
    *   **文字訊息**：支援換行與 **emoji**，不限制字元數。點擊送出後會立即排程發送。
    *   **圖片訊息**：上傳單張圖片（建議規格：**1MB 以內、1000x1000px**，支援 JPG/PNG/JPEG/GIF），並可設定圖片點擊後導轉的連結。

## 進階自動化推播 (CYBERBIZ AUTOMATION)

若您使用的是 **企業版** 或 **PLUS 版**，可利用自動化工具進行更精準的再行銷：

*   **應用場景**：可設定自動發送訊息給「VIP 會員」、「潛在忠誠顧客」、「沉睡客戶」或針對「未結帳購物車」進行提醒。
*   **操作限制**：透過自動化流程發送時，一次最多可發送 **3 組** 訊息模組（圖片或文字不限）。
*   **設定路徑**：前往「APP MARKET」>「我的擴充服務」>「**CYBERBIZ AUTOMATION**」建立流程。

## 常見未收到訊息之原因

如果您發現有 UID 紀錄但會員未收到訊息，通常為以下原因：

*   會員目前並非該 LINE OA 的好友。
*   會員已封鎖該官方帳號。
*   商家 LINE OA 的訊息額度已用盡。

您是否需要我進一步說明如何從 LINE OA 後台取得正確的標籤名單，或是如何操作「CYBERBIZ AUTOMATION」來建立自動推播流程？

## 後續操作

<div class="grid cards" markdown>

- :lucide-import:{ .lg }   
  [____]()     
  。

- :lucide-ban:{ .lg }     
  [____]()  
  。

</div>

## 常見問題

??? quote ""

