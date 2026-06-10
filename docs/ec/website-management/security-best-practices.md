---
title: 資安防護總覽與最佳實務
description: 概述各項安全措施、後台設定路徑及資安事件應變指南，全面保障您的網站與顧客個資。
created: 2026-06-09 17:07
last_modified: 2026-06-10 12:24
lang: zh-TW
type: guide
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
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3549
  - https://www.cyberbiz.io/support/?p=14216
permalink: ""
comments: ""
search:
  exclude: ""
icon: lucide/shield
hide:
---

{{ subtitle(page.meta.description) }}

{{ badge(page.meta) }}

## 資訊防護說明 { #intro-security-guide }

資訊安全需要商家一起配合執行各項設定，才能有效降低風險。本頁屬「總覽與最佳實務」，協助你一次掌握該做哪些防護。各功能的詳細操作步驟，請點對應連結前往教學。多數功能集中在後台「管理中心」>「安全性設定」，部分則位於「網站權限」、付款或網域相關設定。

!!! tip "建議優先順序"
    若你剛開始盤點資安，建議先完成三件事：開啟 **二階段驗證**、設定 **IP 白名單**、開啟 **後台登入 reCAPTCHA**，這三項對防止帳號被盜用最有效。

## 資安防護總覽 { #overview-security-guide }

| 防護措施 | 用途 | 設定位置 |
| :-- | :-- | :-- |
| 二階段驗證（2FA） | 登入時加上動態驗證碼，防止帳號被盜用 | 安全性設定 > 管理員登入 |
| IP 白名單 | 只允許名單內 IP 登入後台 | 安全性設定 > 管理員登入 |
| 後台登入 reCAPTCHA | 後台登入加上機器人驗證 | 安全性設定 > 管理員登入 |
| 瀏覽器 Cookie 驗證 IP 白名單 | 避免同瀏覽器 IP 跳動被強制登出 | 安全性設定 > 管理員登入 |
| 自動登出時間 | 後台閒置自動登出 | 安全性設定 > 管理員登入 |
| 會員個資部分隱碼 | 遮蔽顧客姓名、手機、地址等個資 | 安全性設定 > 會員安全 |
| 訪問限制地區黑名單 | 封鎖特定地區顧客造訪前台 | 安全性設定 > 會員安全 |
| 網站密碼 | 顧客需輸入密碼才能瀏覽網站 | 安全性設定 > 會員安全 |
| 匯出權限控管 | 將顧客匯出、訂單匯出權限縮到最小 | 網站權限 |
| 信用卡 3D 驗證 | 消費者需簡訊驗證，降低盜刷 | 付款設定（加值） |
| SSL 安全性憑證 | 加密網站與顧客間的資料傳輸 | 隨方案提供或於網域設定 |

## 核心登入防護 { #operate-security-guide-core }

這三項是防止帳號被盜用與惡意攻擊最有效的防線，建議優先全部開啟。

<div class="grid cards" markdown>

-   :lucide-shield-check:{ .lg .middle } __二階段驗證（2FA）__

    ---

    輸入帳密後，還需手機驗證器產生的動態驗證碼才能登入。即使密碼外洩，駭客也無法突破第二層驗證。

    [:lucide-arrow-right: 設定步驟](security-settings.md#operate-security-2fa)

-   :lucide-network:{ .lg .middle } __IP 白名單__

    ---

    限制只有名單內的 IP 位址才能登入後台。請勿使用手機 WiFi 分享等浮動 IP，否則可能導致無法登入。

    [:lucide-arrow-right: 設定步驟](security-settings.md#operate-security-ip-whitelist)

-   :lucide-bot:{ .lg .middle } __後台登入 reCAPTCHA__

    ---

    在後台登入頁加上機器人驗證，減少自動化腳本攻擊。

    [:lucide-arrow-right: 設定步驟](security-settings.md#operate-security-recaptcha)

</div>

---

## 進階存取控管 { #operate-security-guide-access-control }

當核心防護完成後，可再依需求加強登入與存取控管。

<div class="grid cards" markdown>

-   :lucide-cookie:{ .lg .middle } __瀏覽器 Cookie 驗證 IP 白名單__

    ---

    當同一瀏覽器操作時 IP 變動，系統會要求重新登入，防止他人盜取 Cookie 偽裝身分；若你的網路 IP 頻繁跳動造成困擾，可把可信任 IP 加入此名單。

    [:lucide-arrow-right: 設定步驟](security-settings.md#operate-security-cookie-whitelist)

-   :lucide-clock:{ .lg .middle } __自動登出時間__

    ---

    設定後台閒置多久自動登出（可選 4 小時至 7 天），降低電腦遭他人誤用的風險。

    [:lucide-arrow-right: 設定步驟](security-settings.md#operate-security-logout-timer)

-   :lucide-globe-off:{ .lg .middle } __境外 IP 登入限制__

    ---

    若你有跨境經營或海外登入需求，可評估限制境外登入。此項涉及帳號授權，建議直接聯繫 CYBERBIZ 客服確認開通方式。

</div>

---

## 資料安全與權限管理 { #operate-security-guide-data }

保護顧客個資、收斂高風險權限，並養成稽核習慣。

<div class="grid cards" markdown>

-   :lucide-download:{ .lg .middle } __匯出權限最小化__

    ---

    建議將「顧客匯出」與「訂單匯出」權限縮到最小，僅開放給必要人員。設定位置：後台「網站權限」。

-   :lucide-eye-off:{ .lg .middle } __會員個資部分隱碼__

    ---

    在網站前台、後台或訂單明細列印時，將會員姓名、手機、地址等以隱碼遮蔽。

    [:lucide-arrow-right: 設定步驟](security-settings.md#operate-security-pdpa)

-   :lucide-search:{ .lg .middle } __定期稽核登入者__

    ---

    定期檢查「網站權限」中的管理員名單，並留意是否有異常操作或不明 IP 登入。

</div>

---

## 交易與網域安全 { #operate-security-guide-transaction }

保護交易過程與網站傳輸安全。

<div class="grid cards" markdown>

-   :lucide-credit-card:{ .lg .middle } __信用卡 3D 驗證__

    ---

    消費者需輸入簡訊驗證碼才能完成付款，可降低盜刷風險。是否開通與適用的金流，建議向 CYBERBIZ 客服確認。

    [:lucide-arrow-right: 設定教學](../payments-and-logistics/設定信用卡%203D%20驗證門檻.md)

-   :lucide-lock:{ .lg .middle } __SSL 安全性憑證__

    ---

    保護網站與顧客間的資料傳輸安全。使用 CYBERBIZ 網域已包含 SSL；若使用自有網域，SSL 通常隨方案提供或需另行續購。

-   :lucide-copyright:{ .lg .middle } __網頁防複製保護__

    ---

    部分佈景／前台設定可限制顧客複製文字或下載圖片，保護原創內容。實際是否提供，依你的佈景設定為準。

    [:lucide-arrow-right: 設定教學](../website-appearance/site-settings/設定網頁鎖右鍵保護圖文版權.md)

</div>

---

## 事故發生時的應變 { #operate-security-guide-incident }

若發現網站疑似被盜用或發生資安事故，建議同時從「品牌端」與「自身帳號」兩方面處理。

- **品牌端應對**：於官網重要頁面（如 Banner、結帳頁）新增防詐騙提醒，記錄受害顧客資訊，並通報 165 反詐騙專線與報警處理。
- **自身帳號措施**：透過後台檢視是否有異常 IP 登入並保留紀錄、全面更改所有帳號密碼、清除瀏覽器 Cookie 暫存，並確認已開啟二階段驗證與 IP 白名單。

## 常見問題 { #faq-security-guide }

??? quote "我只有時間做一件事，先做哪個最有效？"
    [](){ #faq-security-guide-priority }
    優先開啟 **二階段驗證**。即使密碼外洩，沒有手機驗證器的動態驗證碼也無法登入，是 CP 值最高的防線。行有餘力再加上 IP 白名單與後台登入 reCAPTCHA。

??? quote "這些防護會影響顧客購物或我自己操作後台嗎？"
    [](){ #faq-security-guide-impact }
    視功能而定：

    - 影響「你與員工登入後台」：二階段驗證、IP 白名單、自動登出、後台登入 reCAPTCHA。
    - 影響「顧客瀏覽前台」：網站密碼、訪問限制地區黑名單、會員個資部分隱碼。
    - 設定前請先確認影響範圍，例如啟用 IP 白名單前務必先把自己的 IP 加入名單。

??? quote "發現可疑登入或疑似被盜用，第一時間該做什麼？"
    [](){ #faq-security-guide-incident-first }
    建議立即：

    - 更改所有後台帳號密碼，並確認已開啟二階段驗證與 IP 白名單。
    - 保留異常登入紀錄，於官網張貼防詐騙提醒，通報 165 並報警。
    - 聯繫 CYBERBIZ 客服協助確認帳號狀態。

## 參考資料 { #reference-security-guide }

- [安全性設定：保護後台帳號與顧客資料](security-settings.md)
- [二階段驗證設定教學](https://www.cyberbiz.io/support/?p=12650)

