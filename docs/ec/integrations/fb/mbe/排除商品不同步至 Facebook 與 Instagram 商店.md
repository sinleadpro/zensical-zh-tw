---
title: 排除商品不同步至 Facebook 與 Instagram 商店
description: 說明如何透過商品標籤設定，排除特定商品不同步至 Facebook 與 Instagram 商店。
created: 2026-04-14 11:25
last_modified: 2026-04-14 10:30
lang: zh-TW
type: tutorial
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
sites:
  - TW
audiences:
  - admin
difficulty: beginner
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
intents:
  - 排除_FB_商店商品
  - 排除_IG_商店商品
features:
  - 商品排除標籤
prerequisites:
  - "[[設定 Facebook 跟 Instagram 商店]]"
related:
  - "[[設定 Facebook 跟 Instagram 商店]]"
  - "[[管理商品標籤]]"
tags:
  - FBE
  - Facebook_商店
  - Instagram_商店
  - 商品同步
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - "第三方整合 > 臉書_Facebook_設定"
layouts: []
wp_url: []
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/package-x
hide: []
---

{ .subtitle }

{ .doc-badge }

{ .hero-page }


## FB 與 IG 商店商品排除說明

在啟用 Facebook (FB) 與 Instagram (IG) 商店串接後，系統會透過產品動態網址持續更新目錄資訊，若您有不欲顯示的商品，可以依照以下說明進行設定與調整。

!!! info "系統更新時間"
    官網商品資訊通常於每日 **凌晨 2 點或 2 點半** 自動同步至 Facebook 商店，當日更新的內容需等候同步完成才會呈現。

## 前置作業

- [x] 完成 [Facebook 跟 Instagram 商店串接](設定 Facebook 跟 Instagram 商店.md){ data-preview }。

## 透過官網後台標籤排除（自動化）

若您有特定商品（如贈品或測試品）不希望同步至第三方平台，最直接的方法是利用標籤過濾：

<div class="grid cards" markdown>

- :lucide-package-x:{ .lg }   
  [__設定商品排除標籤__](../../../products/categorization/管理商品標籤.md#排除上傳至第三方平台標籤){ data-preview }     
  在商品標籤輸入「排除 product feed」或「贈品」，系統自動過濾不同步的商品。

</div>


## 於 Meta 商務管理工具中調整（手動調整）

若串接已完成，您也可以直接在 Meta 商務管理工具的管理介面調整能見度：

#### 隱藏整個商店

1. 進入「[商務管理工具 :lucide-external-link:](https://business.facebook.com/commerce)」。
2. 點擊「設定」> 「一般」，在 **銷售管道** 中找到相關商店。
3. 在下拉式功能表中選擇能見度設定。

![設定FB-IG商店能見度](../../../../assets/images/ec-第三方整合-fb-fb-ig商店-設定能見度.png)

!!! note "更多流程及相關說明，請參閱 Meta 官方文件：[管理商店在 Facebook 和 Instagram 上的能見度 :lucide-external-link:](https://www.facebook.com/business/help/23907275388927202)。"

#### 隱藏單一或部分商品

1. 進入「[商務管理工具 :lucide-external-link:](https://business.facebook.com/commerce)」。
2. 在商務管理工具中選擇「設定」。
3. 選擇 **「庫存」** 選項。
4. 找到欲隱藏的商品，點擊其旁的 **「眼睛圖示」** 並確認隱藏，即可關閉該商品的顯示。

!!! note "更多流程及相關說明，請參閱 Meta 官方文件：[管理商店商品 :lucide-external-link:](https://www.facebook.com/business/help/836266307249612)。"

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

