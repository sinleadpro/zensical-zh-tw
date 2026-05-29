---
title: 無法讀取 HTTPS 根網址
description: 當網站從其他平台遷移至 CYBERBIZ 後，若出現 http://您的網址 可正常開啟，但 https://您的網址 無法讀取的情況，通常與網域商對「根網域（Naked Domain）」的轉址支援度有關。
created: 2026-03-10 00:00
last_modified: 2026-05-28 14:48
lang: zh-TW
type: reference
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 管理中心
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 診斷_HTTPS_連線問題
  - 執行網域移轉流程
features:
  - SSL_憑證
  - 根網域轉址
  - 網域移轉
prerequisites:
  - [[需具備第三方網域商的管理權限]]
  - [[網域需已指向 CYBERBIZ]]
related: []
tags:
  - 疑難排解
  - HTTPS
  - SSL
  - 網域轉址
  - 根網域
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 網域管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=29144
permalink: ""
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# 無法讀取 HTTPS 根網址

當網站從其他平台遷移至 CYBERBIZ 後，若出現 http://您的網址 可正常開啟，但 https://您的網址 無法讀取的情況，通常與網域商對「根網域（Naked Domain）」的轉址支援度有關。
{ .subtitle }


## 問題診斷：為什麼 HTTPS 無法讀取？

在網站遷移過程中，為了確保搜尋引擎權重（SEO）與使用者體驗，通常會將「根網域（`example.com`）」自動轉址到「子網域（`www.example.com`）」。

然而，部分網域商（如：GoDaddy）的基礎轉址機制僅支援 HTTP 協議。當使用者強制使用 HTTPS 訪問根網址時，由於網域商端缺乏對應的 SSL 握手能力，會導致網頁顯示「連線逾時」或「無法連線」。

!!! tip "判斷標準"
    1.  輸入 `http://example.com` → **成功** 導向 `https://www.example.com`。
    2.  輸入 `https://example.com` → **失敗**，顯示無法讀取網頁。
    - *若符合上述兩點，代表您的網域商不支援根網域的 HTTPS 轉址。*


## 解決方案：移轉網域至支援完善的網域商

目前相對簡易且穩定的解決方案，是將網域移轉至對 HTTPS 轉址支援較完善的網域商（例如：Gandi）。以下以 GoDaddy 轉移至 Gandi 為範例：

### 步驟 1：從原網域商申請轉出（以 GoDaddy 為例）

1. 登入 **GoDaddy 管理介面**，進入 **網域管理**。
2. 找到欲轉移的網域，點選 **轉出網域**。
3. 依照系統提示點擊 **繼續轉移**。
4. 點擊 **按一下這裡即可檢視授權碼**，並將產生的 **授權碼** 複製備用。

### 步驟 2：於新網域商發起轉入（以 Gandi 為例）

1. 登入 **Gandi 管理介面**，選擇 **域名 > 移轉**。
2. 輸入您的網域並進行搜尋。
3. 在移轉流程中，填入第一步取得的 **授權碼**。
4. 完成結帳。
5. 依照 Gandi 指引完成後續的 **Email 驗證**。

### 步驟 3：重新設定 DNS

網域移轉完成後，請務必重新檢查並[設定 DNS 紀錄]()，確保網址正確指向 CYBERBIZ 伺服器。


## 常見問題

??? quote "移轉網域會導致網站暫時無法連線嗎？"
    若在移轉前已正確設定 DNS 且 TTL 值設定合理，移轉過程通常不會造成網站斷線。但網域資料更新（生效）可能需要 24-48 小時。

??? quote "操作遇到障礙該聯繫誰？"
    網域 DNS 管理屬於第三方服務，非 CYBERBIZ 直接管轄範圍。若在操作移轉過程中遇到技術障礙，建議優先聯繫您的網域商客服取得專業協助。


## 後續操作

<div class="grid cards" markdown>

- :lucide-move-right:{ .lg } 
  [__如何將域名轉入 Gandi (官方教學)__](https://docs.gandi.net/zh-hant/domain_names/transfer/description.html)
  由 Gandi 提供的技術文件，導引您將既有網域移轉至其平台進行管理。

- :lucide-globe:{ .lg } 
  [__Gandi 自訂網域完整設定__](../../管理中心/網域管理/自訂網域設定.md)
  完整指引 DNS 解析與代管設定流程，協助您順利完成官網對接。



</div>

