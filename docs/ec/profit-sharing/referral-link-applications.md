---
title: 推薦碼連結的應用
description: 為指定頁面建立分潤推薦連結，並透過短網址、QR Code 或 UTM 參數應用於社群、實體文宣與廣告等推廣管道，追蹤不同來源的導購成效。
created: 2026-02-06 00:00
last_modified: 2026-10-01 11:30
lang: zh-TW
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 分潤
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - 進階
  - 高手
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
plan_options: 
  - standard
  - optional
cyb_extensions: []
intents:
  - 製作推薦連結
  - 產生 QR Code
  - 設定 UTM 參數
  - 測試推薦連結
features:
  - 推薦人分潤
  - UTM 追蹤
prerequisites: []
related: 
  - ec/profit-sharing/query-profit-sharing-partners-and-codes/
  - ec/marketing/one-page-store/one-page-store/
tags:
  - 推薦連結
  - QR Code
  - UTM
  - 短網址
  - 行銷追蹤
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 分潤 > 分潤查詢
  - 行銷活動 > 推薦人分潤
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4051
permalink: "https://help.cyberbiz.io/ec/profit-sharing/referral-link-applications/"
comments: false
search:
  exclude: false
icon: lucide/share-2
hide: []
---
# 推薦碼連結的應用

為指定頁面建立分潤推薦連結，並透過短網址、QR Code 或 UTM 參數應用於社群、實體文宣與廣告等推廣管道，追蹤不同來源的導購成效。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 品牌官網 / 智能 POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 進階 / 高手 / 所有PLUS / 企業
{ .doc-badge }


## 什麼是推薦碼連結 { #referral-link-applications-definition }

推薦碼連結是指在官網網址後方嵌入專屬「推薦碼（rcode）」參數的特殊連結。

- **身分記錄**：消費者點擊連結後，瀏覽器將自動記錄該次推廣的身分資訊。
- **自動帶入**：當透過連結結帳時，系統會自動將推薦碼帶入欄位，無需消費者手動輸入。


## 為指定頁面建立分潤推薦連結 { #referral-link-applications-specific-page }

若要將消費者導向官網的特定商品頁、活動頁或一頁式商店，可在目標網址中加入推薦碼，建立對應的分潤推薦連結。

### 取得推薦碼 { #referral-link-applications-get-code }

製作連結前，請先查詢並取得分潤夥伴的推薦碼：

<div class="grid cards" markdown>

- :lucide-copy:{ .lg }
  [__一鍵複製推薦碼__](query-profit-sharing-partners-and-codes.md#任務三一鍵複製推薦碼)<br>
  前往 **分潤 > 推薦人分潤 > 第三方總表**，點擊複製圖示取得推薦人的推薦碼。

</div>

### 製作方式 { #referral-link-applications-create-link }

- **原始網址**：`https://store.com/xxx/yyy`
- **推薦碼後綴格式**：`?rcode=[推薦碼]`
- **推薦碼**：`abc123`
- **最終連結**：`https://store.com/xxx/yyy?rcode=abc123`


### 情境範例 { #referral-link-applications-example }

[一頁式商店](../marketing/one-page-store/one-page-store.md)可結合分潤功能，透過製作帶有推薦碼的網址，當消費者點擊含推薦碼之連結後，系統將自動於購物車帶入推薦碼。

- **原始網址**：`https://store.com/events/spring-sale`
- **推薦碼後綴格式**：`?rcode=[推薦碼]`
- **推薦碼**：`abc123`
- **最終連結**：`https://store.com/events/spring-sale?rcode=abc123`



## 加工推薦碼連結 { #referral-link-applications-processing }

在開始推廣前，請先從後台複製帶有推薦碼的原始連結，系統提供以下查詢方式：

<div class="grid cards" markdown>

- :lucide-search:{ .lg }
  [__查詢合作夥伴的分潤資訊__](query-profit-sharing-partners-and-codes.md#任務一查詢合作夥伴的分潤資訊)<br>
  適合查詢特定合作夥伴參與的分潤方案、分潤比例與推薦碼。

- :lucide-user-round-search:{ .lg }
  [__員工自我查詢分潤資訊__](query-profit-sharing-partners-and-codes.md#任務二員工自我查詢分潤資訊)<br>
  適合內部員工查詢所屬的分潤方案，取得個人推廣連結。

- :lucide-copy:{ .lg }
  [__一鍵複製推薦碼__](query-profit-sharing-partners-and-codes.md#任務三一鍵複製推薦碼)<br>
  適合從第三方推薦人名單快速取得合作夥伴的推薦碼。

</div>

### 製作方式 { #referral-link-applications-processing-methods }


=== "產生短網址"

    若連結過長不便於社群分享，可使用外部短網址工具。

    - **步驟**：將複製的 **完整推薦連結** 貼入工具產出。
    - **注意**：絕對不可先縮短網址再手動拼接推薦碼。

=== "產生 QR Code"

    適用於線下印刷或直播畫面。

    - **步驟**：將連結貼入任何 QR Code 產生器，即可生成對應圖像。
    - **應用**：建議將 QR Code 放置於結帳櫃檯、包裹隨附小卡或雜誌廣告中。

=== "設置 UTM 參數"

    用於區分同一個推薦人在不同管道的表現。

    - **手動設定規則**：在推薦連結（如 `.../?rcode=xxx`）後方加上 `&` 符號，接著填入 UTM 參數。
    - **正確範例**：`https://.../?rcode=xxx&utm_medium=fb&utm_source=kol_a`
    - **錯誤範例**：`https://.../?rcode=xxx?utm_medium=fb`（不可使用兩個問號）


## 測試推薦連結有效性 { #referral-link-applications-testing }

在正式發布連結前，請務必依以下步驟測試追蹤功能是否正常。

1. 前往 **行銷活動 > 推薦人分潤**，確認 **啟用結帳頁顯示推薦碼欄位** 已開啟。
2. 複製您製作好的推廣連結。
3. 開啟瀏覽器的 **無痕視窗**。
4. 貼上推廣連結並進入網站，隨機將任一商品加入購物車。
5. 前往結帳頁面，確認 **推薦碼** 欄位已自動帶入正確的代碼。
    - 若欄位已帶入代碼：代表連結追蹤功能正常，可正式推廣。
    - 若欄位為空：請重新檢查連結格式是否正確。



## 常見問題 { #referral-link-applications-faq }

??? quote "為什麼我縮短網址後，推薦碼就失效了？"
    通常是因為您在縮網址工具中輸入的是 **不含推薦碼的官網首頁網址**。請務必確認縮網址工具的輸入來源是包含 `?rcode=...` 的完整字串。

??? quote "UTM 參數一定要設定嗎？"
    不是必須。推薦碼（rcode）負責 **算業績給誰**，而 UTM 負責 **分析流量從哪來**。若您不需要分析流量來源，僅需使用原始推薦連結即可。



