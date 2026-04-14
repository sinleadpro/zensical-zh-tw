---
title: 排除商品不同步至 Facebook 與 Instagram 商店
description: ""
created: 2026-04-14 11:25
last_modified:
lang: zh-TW
type: tutorial
status: ""
author: Jase
version: ""
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
icon: lucide/package-x
hide:
---

{ .subtitle }

{ .doc-badge }

{ .hero-page }

## FB 與 IG 商店商品排除說明

在啟用 Facebook (FB) 與 Instagram (IG) 商店串接後，系統會透過產品動態網址持續更新目錄資訊，若您有不欲顯示的商品，可以依照以下說明進行設定與調整。

## 透過官網後台標籤排除（自動化）

若您有特定商品（如贈品或測試品）不希望同步至第三方平台，最直接的方法是利用標籤過濾：

<div class="grid cards" markdown>

- :lucide-package-x:{ .lg }   
  [__設定商品排除標籤__](../../../products/categorization/管理商品標籤.md#排除上傳至第三方平台標籤){ data-preview }     
  在商品標籤輸入「排除 product feed」或「贈品」，系統自動過濾不同步的商品。

</div>


## 於 Meta 商務管理工具中調整（手動調整）

若串接已完成，您也可以直接在 Facebook 的管理介面調整能見度：

*   **隱藏整個商店：**
    1. 進入「商務管理工具」並選擇正確的帳號。
    2. 點擊「商店」並進入「編輯商店」。
    3. 在「設定」中找到 **「能見度」** 並點擊編輯，即可切換商店顯示的開關。
*   **隱藏單一或部分商品：**
    1. 在商務管理工具中選擇「設定」。
    2. 選擇 **「庫存」** 選項。
    3. 找到欲隱藏的商品，點擊其旁的 **「眼睛圖示」** 並確認隱藏，即可關閉該商品的顯示。

## 重要提醒

*   **更新時間：** 官網商品資訊通常於每日**凌晨 2 點或 2 點半**自動同步至 Facebook 商店，當日更新的內容需等候同步完成才會呈現。
*   **第三方系統細節：** 由於 CYBERBIZ 主要是提供與第三方系統的串接，FB、IG 的操作細節請以 Meta 官方最新的教學文件為主。

## 後續操作

<div class="grid cards" markdown>

- :lucide-store:{ .lg }   
  [__設定 FB 與 IG 商店__](設定 Facebook 跟 Instagram 商店.md){ data-preview }       
  返回商店設定說明，了解完整的串接流程與商品同步機制。

</div>

## 常見問題

??? quote ""

