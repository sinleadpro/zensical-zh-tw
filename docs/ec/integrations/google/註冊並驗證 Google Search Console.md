---
title: "註冊並驗證 Google Search Console"
description: "" 
created: "2026-03-20 14:28"
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
tnb: trunk
plans: 
  - 專業
  - 進階
  - 高手
  - 專業 PLUS 
  - 進階 PLUS
  - 高手 PLUS
  - 企業
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
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/search-code
hide:
---

# 註冊並驗證 Google Search Console


{ .subtitle }

{ .doc-badge }

{ .hero-page }

## 註冊 Google Search Console 說明

註冊並驗證 **Google Search Console (GSC)** 是經營網站的重要步驟，這能協助您後續設定 Sitemap（網站地圖），讓搜尋引擎更有效地收錄您的網頁。

以下為註冊與驗證 Google Search Console 的詳細教學：

## 操作前準備

- [x] **帳號統一**：請確保登入 Google Search Console 的帳號與您的 Google Analytics (GA) 帳號為同一組，且具備該帳號管理員權限。
- [x] **網域設定**：建議先將官網後台的主網域設定為「自有網域」，並開啟「總是導向」功能，以確保搜尋引擎收錄的一致性。

## 註冊與驗證步驟

1. **進入 GSC**：前往 [Google Search Console](https://search.google.com/search-console/) 頁面，點選「立即開始」。
2. **輸入網址**：在資源類型選擇介面中，點選右側的**「網址前置字元」**，並輸入您的官網網址（需包含 https://）。
3. **選取驗證方式**：驗證方式請選擇**「HTML 標記」**，系統會產生一段程式碼，請點擊旁邊的按鈕複製該代碼。
4. **埋設代碼至 CYBERBIZ 後台**：
    * 進入管理後台路徑：**「網站外觀」** → **「套版主題管理」** → 選擇操作**「CSS/HTML 編輯器」** → 點擊左側的 **`theme.liquid`** 檔案。
    * 將剛才複製的 HTML 標記代碼貼在檔案內容中的 **`</head>`** 標籤前面，並儲存設定。
5. **完成驗證**：回到 Google Search Console 的頁面，點選**「驗證」**。驗證完成後會跳出「已驗證擁有權」的彈窗，點擊「前往資源」即可開始查看數據。

## 註冊後的建議操作

註冊與驗證完成後，最重要且優先的動作是進行 [**網站地圖 (Sitemap) 的提交**]()。CYBERBIZ 系統會自動產生 Sitemap 檔案，您只需在 GSC 的「Sitemap」選單中輸入 `sitemap.xml` 並提交，即可加速 Google 更新網站資料的速度。

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

