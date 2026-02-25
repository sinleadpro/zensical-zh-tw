---
title: LINE 整合應用
---

在 CYBERBIZ 系統中，LINE 的應用涵蓋了從會員登入、自動化通知到行銷導購的全方位功能。以下為 LINE 各項應用的詳細說明與操作教學：


## 開始使用

<div class="grid cards" markdown>

- :lucide-rocket:{ .lg }   
  [__LINE 整合應用新手指南__ :lucide-external-link:](https://drive.google.com/file/d/1DxbJDYoTFF1xKljcUFLoGVLnmJoLQZRi/view)    
  從零開始串接 LINE 官方帳號。包含 Messaging API 金鑰設定、自動回應與會員綁定流程，快速建立品牌與顧客的溝通渠道。

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


## 會員綁定與體驗優化 (LIFF)

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

- :lucide-ban:{ .lg }     
  [__物流限制與排除選項__](設定超商配送限制與物流排除.md)  
  設定商品的配送物流條件，限制特定物流方式於結帳流程中的顯示與使用。

</div>

1. **LINE OA 訊息提醒樣板：** 商家可開啟「訂單」、「物流」、「顧客」等樣板，在指定情境下自動回覆。

    - **物流通知：** 系統會在配送狀態更新為「已出貨 (配送中)」時，正式發送 LINE 通知。

    - **未付款提醒：** 針對下單未付款訂單，可設定間隔天數自動發送 LINE 訊息催單。

2. **分眾訊息推播：** 商家可透過「顧客標籤」篩選特定族群，發送文字或圖片推播訊息。

## 精準行銷與廣告追蹤

1. **LINE OA 受眾串接：** 商家可將篩選出的「已完成 LINE 綁定」會員名單，同步至 LINE OA 後台建立受眾，用於推播或廣告投放。

2. **LINE Tag 設定：** 類似於 FB Pixel，可用於追蹤官網上的轉換事件（如完成註冊、加入購物車、下單），並打包「網站流量受眾」進行再行銷。

3. **綁定送優惠券：** 開啟「LINE @ 綁定贈送優惠券功能」，以獎勵誘因吸引會員完成帳號綁定。

## 進階導購應用 (直播、購物、團購)

1. **LINE 直播：** 商家可在 LINE OA 執行購物直播，讓消費者「邊看邊買」，下單後的訂單可於後台「LINE OA 訂單」查看。

2. **LINE 購物：** 串接後可透過 LINE 購物入口（APP 或官方帳號）引導顧客至官網下單，並提供點數回饋。

3. **LINE 團購：** 透過「團購機器人」在 LINE 群組內進行活動，成員可直接在群組內透過機器人選單瀏覽商品並結帳。

## 虛實整合 (OMO) 應用

1. **會員條碼：** 配合 POS 系統，會員可從 LINE OA 圖文選單中調出「會員條碼」，供店員掃描以進行紅利與優惠券折抵。

2. **門市助理：** 門市店員可透過專屬 QR Code 引導顧客一次完成加入 LINE 好友、註冊與店員綁定。

**重要注意事項與成本**

- **訊息費用：** LINE 推播訊息（含手動推播與系統自動通知）將依 LINE 官方方案產生費用，僅發送成功的訊息會被計費。

- **好友狀態：** 會員必須是該官方帳號的好友且未封鎖，才能收到 LINE OA 訊息。

- **Email 綁定：** 顧客的 LINE 帳號必須先在 LINE App 中綁定 Email，方可使用快速登入功能。

## 常見問題
