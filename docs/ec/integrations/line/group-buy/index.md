---
title: "LINE 團購功能總覽"
description: LINE 團購功能的運作方式，以及商家如何在 LINE 群組中建立團購活動並讓成員瀏覽商品與完成結帳。
created: "2026-03-12 18:23"
last_modified: "2026-03-12 18:30"
lang: zh-TW
type: guide
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 第三方整合
  - 商品
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: branch
plans:
  - 企業
cyb_extensions: []
intents:
  - LINE_團購
  - LINE_群組購物
features:
  - LINE_團購
  - LINE_機器人
prerequisites: []
related: []
tags:
  - LINE_團購
  - LINE_官方帳號
  - LINE_機器人
acoiv: operation
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
comments: false
search:
  exclude: false
icon: lucide/users
hide: []
---

# LINE 團購功能總覽

LINE 團購功能的運作方式，以及商家如何在 LINE 群組中建立團購活動並讓成員瀏覽商品與完成結帳。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 企業
{ .doc-badge }

{ .hero-page }

## LINE 團購說明

**LINE 團購功能** 旨在協助商家在 LINE 群組或多人聊天室中進行促銷活動，並引導群組成員成為品牌的官方帳號好友。此功能特別適用於社群經營，能讓群組成員在不離開 LINE 的情況下，直接流暢地選購商品與結帳。

以下為 LINE 團購功能的詳細總覽與操作教學：

## 功能環境與限制

*   **適用環境**：僅限於 **LINE 群組** 或 **多人聊天室** 使用。
*   **限制說明**：
    *   由於匿名性限制，**不支援 LINE 社群 (OpenChat)**。
    *   一個 LINE 群組一次只能存在一支團購機器人。
    *   團購購物車 **不開放搭配官網內的一般行銷活動**（如全館折扣、滿額贈等）使用，因為商品已設定獨立的團購優惠價。

## 商家後台設定流程

商家必須依序完成以下三個部分的設定，團購活動方可正式開始：

<div class="grid cards" markdown>

- :material-numeric-1-circle:{ .lg }   
  [__機器人設定__](設定 LINE 團購機器人.md){ data-preview }     
  建立 LINE Messaging API 機器人並完成 Webhook 與權限設定。
  
- :material-numeric-2-circle:{ .lg }     
  [__團購商品設定__](設定 LINE 團購商品.md){ data-preview }  
  從官網商品中建立團購商品並設定團購價格。

- :material-numeric-3-circle:{ .lg }     
  [__團購群組設定__](設定 LINE 團購群組.md){ data-preview }  
  建立團購群組活動並綁定 LINE 群組。

</div>

## 顧客端操作流程

群組成員主要透過關鍵字或選單與機器人互動：

<div class="grid cards" markdown>

- :lucide-megaphone:{ .lg }   
  [__喚起功能__](使用 LINE 團購進行購物.md#如何喚起團購功能){ data-preview }     
  在群組中輸入「**團購**」呼叫機器人選單，並點選「團購列表」開始瀏覽。

- :lucide-shopping-cart:{ .lg }     
  [__選購商品__](使用 LINE 團購進行購物.md#瀏覽與挑選商品){ data-preview }  
  消費者可查看商品詳情，選擇「加入購物車」繼續選購或「加入並結帳」直接購買。

- :lucide-credit-card:{ .lg }     
  [__完成結帳__](使用 LINE 團購進行購物.md#結帳與付款流程){ data-preview }  
  在結帳頁面確認數量與金額後完成付款。付款完成後，系統會自動引導成員加入品牌的官方帳號，幫助商家累積會員。


</div>

## 訂單與分潤管理

<div class="grid cards" markdown>

- :lucide-search-check:{ .lg }   
  [__查看訂單__](設定 LINE 團購群組.md#訂單查看與紀錄管理){ data-preview }  
  商家可至後台「所有訂單」，利用篩選器選擇「**LINE 團購**」來查看專屬訂單紀錄。

- :lucide-history:{ .lg }     
  [__歷史紀錄__](設定 LINE 團購群組.md#訂單查看與紀錄管理){ data-preview }   
  活動結束後（手動結束、時間到期或機器人被退群），資料會移至「團購歷史紀錄」供隨時查閱。

- :lucide-file-spreadsheet:{ .lg }     
  [__分潤查詢__](../../../profit-sharing/查詢分潤夥伴與代碼資訊.md#任務三提供第三方推薦人外部查詢連結){ data-preview }   
  團購主若需查看下單情形，商家可提供「分潤報表下載連結」供其下載 Excel 報表。

</div>

## 常見問題

??? quote "為什麼我在 LINE 群組輸入「團購」機器人沒有反應？"
    請檢查以下項目：

    1. 機器人是否已入群：請確認已將對接好的 LINE 官方帳號邀請進入該群組。
    2. Webhook 是否開啟：請至 LINE Developers 管理後台，確認該帳號的 Use webhook 選項已開啟，且 URL 驗證成功。
    3. 活動狀態：請確認商家後台的「團購群組設定」中，該活動是否處於「進行中」且未過期。

??? quote "為什麼團購機器人不支援「LINE 社群 (OpenChat)」？"
    這是由於 LINE 官方的技術限制。LINE 社群 為了保護個人隱私，並不會提供成員的唯一識別碼（User ID）給第三方系統，因此機器人無法辨識是誰在下單，也無法建立對應的購物車。

??? quote "可以設定不同的團購價格嗎？"
    可以。在「團購商品設定」中，您可以針對同一件商品設定專屬於該次團購的優惠價格，這個價格不會影響到官網原本的售價，僅會在群組內的團購選單中生效。

??? quote "消費者結帳時，可以使用官網的折價券或紅利點數嗎？"
    不支援。 團購購物車為了保持結帳流程的流暢與獨立性，目前不開放搭配官網的一般行銷活動（如全館折扣、滿額贈、折價券、紅利折抵），系統將統一以設定好的「團購優惠價」結算。

??? quote "如果群組成員沒有加入官方帳號好友，可以下單嗎？"
    可以下單。但系統會在結帳完成頁面強力導引成員點擊「加入好友」，這也是商家累積私域流量（轉化為官方帳號粉絲）的最佳時機。

??? quote "一個群組可以同時跑兩個團購活動嗎？"
    不可以。 為了避免系統邏輯衝突，一個 LINE 群組一次只能存在一個啟動中的團購活動。若要更換活動，需先結束當前活動或將舊的機器人請出群組。
