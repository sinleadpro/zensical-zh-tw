---
title: 綁定 LINE 官方帳號與官網會員
version: ""
last_modified: 2026-02-13
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


# 綁定 LINE 官方帳號與官網會員

{ .subtitle }

{ .doc-badge }

{ .hero-page }

## 綁定 LINE 官方帳號與官網會員說明

**LINE OA 官方帳號綁定官網會員** 是整合線上與線下會員資料、進行精準行銷的核心功能。透過綁定，商家可以收集會員的 **LINE UID**，進而發送自動化的訂單/物流通知訊息。

以下為 LINE OA 官方帳號綁定官網會員的詳細說明與教學：

## 綁定前置作業

商家必須先完成以下系統串接設定，資料才能互通：

- [x] [**建立與串接 Messaging API**](串接 LINE Messaging API.md){ data-preview }  ：完成 LINE 官方帳號與 CYBERBIZ 後台的 API 串接。

- [x] **設定 LINE Login (快速登入)**：務必將「LINE 登入」與「Messaging API」設定在 **同一個 LINE Developers Provider (服務提供者)** 中。

- [x] **啟用 LINE 快速登入**：消費者需透過 LINE 快速登入註冊或登入，才能完成綁定流程。

## 商家後台設定方法

商家需提供特定連結引導顧客操作，主要有三種應用情境：

**1. 設定圖文選單 (Rich Menu)**

這是最常用的引導方式。

• **操作路徑**：進入 LINE Official Account Manager →「聊天室相關」→「圖文選單」。

• **設定連結**：建議使用「會員資料頁」作為跳轉頁，連結格式為：`https://你的網址/customer/auth/line?line_action=line_login`。

• **效果**：尚未綁定的顧客點擊後會先進行綁定動作，已綁定的顧客則直接進入登入狀態的指定頁面。

**2. 設定加入好友的歡迎訊息**

• **操作路徑**：進入 LINE Official Account Manager →「聊天室相關」→「加入好友的歡迎訊息」。

• **設定內容**：在訊息中加入上述的綁定連結。這對於首次加入官方帳號的會員最有效。

**3. 使用 LINE LIFF 自動綁定 (推薦方式)**

• **功能特色**：開啟後，消費者點選網址會自動套用 LINE 帳戶資訊。若顧客非好友或非會員，點選連結可**同時加入好友、註冊官網會員並完成綁定**。

• **操作路徑**：後台「第三方整合」→「LINE 註冊登入」→ 開啟「自動產生 LIFF 網址」。

• **應用**：商家可複製系統產生的 LIFF 網址，製作成 QR Code 供消費者掃描。


## 消費者端綁定流程

1. 點擊商家提供的**綁定連結**或 **LIFF 網址**。

2. 進入 **LINE 用戶資料授權頁面**，點擊許可。

3. 系統執行**快速跳轉**（顯示載入中）並導向官網首頁或指定頁面。

4. 最後跳轉至目的頁面，此時消費者已處於**會員登入狀態**且完成綁定。

--------------------------------------------------------------------------------

## 綁定後的進階功能與好處

• **自動發送提醒樣板**：可自動回覆訂單確認、貨物發送、到店提醒及未付款提醒等訊息。

• **綁定送優惠券**：可設定「LINE @ 綁定贈送優惠券功能」來增加顧客綁定意願。

• **顯示會員條碼 (OMO 應用)**：綁定後，顧客可於 LINE 選單調出會員條碼，供實體門市 POS 機掃描進行紅利或優惠券折抵。

• **受眾串接與推播**：商家可在後台篩選「已完成 LINE 綁定」的會員，將受眾上傳至 LINE OA 後台進行精準行銷訊息發送。

## 重要注意事項

• **非好友限制**：透過 LINE 快速登入的顧客**不一定有綁定 LINE OA**，且只有成為 LINE OA 好友且未封鎖的帳號，才能收到 LINE 推播訊息。

• **單一綁定規則**：顧客的 LINE 帳號必須先在 LINE App 中**綁定 Email**，才可順利執行 LINE 快速登入與綁定。

• **連結正確性**：若網址帶有 `/customer/auth/line?line_action` 參數，則每次點選皆會跳出綁定畫面；若不希望重複跳轉，僅需針對「首次綁定」的功能進行設定即可。

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