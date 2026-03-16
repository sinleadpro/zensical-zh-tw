---
title: "index"
description: "" 
created: "2026-03-16 19:00"
last_modified: 
lang: zh-TW
type: guide
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
wp_url: []
permalink: ""
comments: ""
search:
  exclude: ""
icon: fontawesome/brands-line
hide:
---

# LINE 整合應用

{ .subtitle }

{ .doc-badge }

{ .hero-page }


在 CYBERBIZ 系統中，LINE 的應用涵蓋了從會員登入、自動化通知到行銷導購的全方位功能。以下為 LINE 各項應用的詳細說明與操作教學：


## 開始使用

<div class="grid cards" markdown>

- :lucide-book:{ .lg }   
  [__LINE 整合應用新手指南__ :lucide-external-link:](https://drive.google.com/file/d/1DxbJDYoTFF1xKljcUFLoGVLnmJoLQZRi/view)    
  透過串接 LINE 官方帳號與電商系統，達成會員自動化管理、精準分眾行銷及線上線下（OMO）導購與支付整合 。

- :lucide-ban:{ .lg }     
  [__物流限制與排除選項__](設定超商配送限制與物流排除.md)  
  設定商品的配送物流條件，限制特定物流方式於結帳流程中的顯示與使用。

</div>

## 基礎串接：LINE 快速登入與 Messaging API

這是所有 LINE 應用的基礎，建議商家依序完成設定。

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }   
  [__LINE 快速登入__](設定 LINE 快速登入.md){ data-preview }       
  讓顧客能透過 LINE 帳號直接註冊或登入，系統會自動抓取 Email 進行帳號比對。

- :lucide-webhook:{ .lg }     
  [__LINE Messaging API__](串接 LINE Messaging API.md){ data-preview }    
  用於連接商家現有的官方帳號（LINE OA），實現系統與 OA 的整合，是發送自動化通知的前提。

</div>

!!! warning "「LINE 登入」與「Messaging API」務必設定於 LINE Developers 的 同一個 Provider（服務提供者） 中。"

## 會員綁定與體驗優化

為了能發送 LINE 訊息給會員，必須引導顧客完成「官網會員與 LINE OA」的綁定。

<div class="grid cards" markdown>

- :lucide-user-cog:{ .lg }   
  [__LINE 綁定官網會員__](綁定 LINE 官方帳號與官網會員.md){ data-preview }       
  會員需透過 LINE 快速登入進行綁定，商家可透過圖文選單或歡迎訊息設置專屬連結（`line_action=line_login`）來引導。。

- :lucide-zap:{ .lg }     
  [__LIFF 自動登入__](設定 LIFF 自動登入與會員綁定.md){ data-preview }    
  由 EC 後台生成的 LIFF 網址可讓會員點選後 **自動登入**。若顧客非好友或會員，點選 LIFF 連結可 **同時達成加入好友、註冊與綁定**。

</div>

## 自動化通知與訊息推播

<div class="grid cards" markdown>

- :lucide-layout-grid:{ .lg }   
  [__LINE OA 訊息提醒樣板__](../../notifications/設定與管理 LINE OA 通知樣板.md){ data-preview }       
  商家可開啟「訂單」、「物流」、「顧客」等樣板，在指定情境下自動回覆。

- :lucide-message-square-share:{ .lg }     
  [__分眾訊息推播__](設定與發送 LINE OA 分眾訊息推播.md){ data-preview }  
  商家可透過「顧客標籤」篩選特定族群，發送文字或圖片推播訊息。

- :lucide-zap:{ .lg }     
  [__AUTOMATION__](../../app-market/automation/使用 AUTOMATION 建立自動化推播流程.md#line-oa-訊息發送設定){ data-preview }  
  商家可建立自動化工作流程，例如針對「購物車未結帳」會員發送 LINE OA 提醒訊息。

</div>


## 精準行銷與廣告追蹤

<div class="grid cards" markdown>

- :lucide-split:{ .lg }   
  [__LINE OA 受眾串接__](設定 LINE OA 受眾串接.md){ data-preview }     
  商家可將篩選出的「已完成 LINE 綁定」會員名單，同步至 LINE OA 後台建立受眾，用於推播或廣告投放。

- :lucide-code:{ .lg }     
  [__LINE Tag 設定__](設定與管理 LINE Tag.md){ data-preview }  
  類似於 FB Pixel，可用於追蹤官網上的轉換事件（如完成註冊、加入購物車、下單），並打包「網站流量受眾」進行再行銷。

- :lucide-ticket-plus:{ .lg }     
  [__綁定送優惠券__](設定與管理 LINE Tag.md){ data-preview }  
  開啟「LINE @ 綁定贈送優惠券功能」，以獎勵誘因吸引會員完成帳號綁定。

</div>

## 進階導購應用

讓 LINE 不只是通訊工具，更是銷售平台：

<div class="grid cards" markdown>

- :lucide-radio:{ .lg }   
  [__LINE 直播__](申請與設定 LINE 直播功能.md){ data-preview }     
  商家可在 LINE OA 執行購物直播，讓消費者「邊看邊買」，下單後的訂單可於後台「LINE OA 訂單」查看。

- :lucide-book:{ .lg }   
  [__LINE 直播手冊__:lucide-external-link:](https://drive.google.com/file/d/1cOVeAlq9l55rjU2yR_8krxWafSXOzZ2P/view)。  
  透過 LINE 直播的高觸及率與互動功能，結合導購策略來提升電商轉換率與業績。
  
- :lucide-shopping-bag:{ .lg }     
  [__LINE 購物__](申請與設定 LINE 購物導購.md){ data-preview }  
  串接後可透過 LINE 購物入口（APP 或官方帳號）引導顧客至官網下單，並提供點數回饋。

- :lucide-users:{ .lg }     
  [__LINE 團購__](group-buy/index.md){ data-preview }  
  透過「團購機器人」在 LINE 群組內進行活動，成員可直接在群組內透過機器人選單瀏覽商品並結帳。
</div>

## 虛實整合 (OMO) 應用

<div class="grid cards" markdown>

- :lucide-book:{ .lg }   
  [__LINE OA 虛實整合教學__:lucide-external-link:](https://drive.google.com/file/d/1mOPY3hZorS99_cjPCZMy_zIEUUGrZTqf/view)     
  透過與電商及 POS 系統串接，落實會員註冊自動化、發送專屬優惠券，並優化門市現場的會員掃碼及優惠兌換流程。

- :lucide-barcode:{ .lg }   
  [__會員條碼__](批次修改商品描述與配送設定.md)     
  配合 POS 系統，會員可從 LINE OA 圖文選單中調出「會員條碼」，供店員掃描以進行紅利與優惠券折抵。

- :lucide-contact-round:{ .lg }     
  [__門市助理__](.md)  
  門市店員可透過專屬 QR Code 引導顧客一次完成加入 LINE 好友、註冊與店員綁定。

</div>

## 重要注意事項與成本

- **訊息費用：** LINE 推播訊息（含手動推播與系統自動通知）將依 LINE 官方方案產生費用，僅發送成功的訊息會被計費。

- **好友狀態：** 會員必須是該官方帳號的好友且未封鎖，才能收到 LINE OA 訊息。

- **Email 綁定：** 顧客的 LINE 帳號必須先在 LINE App 中綁定 Email，方可使用快速登入功能。

## 常見問題
