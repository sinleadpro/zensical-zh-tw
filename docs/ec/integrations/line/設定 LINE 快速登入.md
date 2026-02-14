---
title: 設定 LINE 快速登入
version: ""
last_modified: 2026-02-14
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


# 設定 LINE 快速登入

{ .subtitle }

{ .doc-badge }

{ .hero-page }

## 什麼是 LINE 快速登入

**LINE 快速登入** 讓顧客能透過 LINE 帳號直接登入或註冊成為會員，系統會自動抓取客戶 LINE 綁定的「Email」進行帳號比對。這不僅簡化了購物流程，還能增加商家官方帳號的曝光度，並讓商家在後台篩選出透過 LINE 登入的會員。

以下為 LINE 快速登入的詳細設定教學：

## 設定前置注意事項

- **Email 綁定**：顧客的 LINE 帳號**必須先綁定 Email**，才可以使用 LINE 快速登入功能。

- **Provider 一致性**：若您已有 LINE 官方帳號（Messaging API），請務必確保 **LINE Login Channel** 與 **Messaging API** 處於**同一個 Provider（服務提供者）**之下。

- **Hinet 信箱限制**：若消費者使用 Hinet 信箱註冊，可能會因為 Hinet 阻擋訊息而導致無法重新設定密碼。


## LINE Developers 後台設定步驟

1. **建立 Login Channel**：登入 [LINE Developers :lucide-external-link:](https://developers.line.biz/)，選擇正確的 Provider 後，點擊「**Create a LINE Login channel**」。

2. **填寫基本資訊**：

    - **Region** 選擇「Taiwan」。

    - **App types** 勾選「Web app」。

    - 填寫商店名稱（Channel name）、商店簡述（Channel description）、Email 及網站隱私政策/服務條款網址。

3. **申請 OpenID Connect**：

    - 在「Basic settings」分頁最下方找到「OpenID Connect」，點擊「Apply」。

    - 勾選內容並依照需求上傳商家 Logo 後提交（Submit），這步是**確保能抓取顧客 Email** 的關鍵。

4. **設定 Callback URL（關鍵步驟）**：

    - 切換至「LINE Login」頁籤，在 **Callback URL** 欄位輸入：`https://你的商店網址/customer/auth/line/callback`。

    - **提示**：若您有自有網域，請務必將 CYBERBIZ 網域及自有網域都填入，跨境用戶則填寫一般網域即可，不需加上 `zh-TW`。

5. **正式發布**：將 Channel 狀態從「Developing」轉為「**Published**」。

## CYBERBIZ 後台串接步驟

1. **取得金鑰**：在 LINE Developers 的「Basic settings」頁籤複製 **Channel ID** 與 **Channel Secret**。

2. **回填後台**：前往 CYBERBIZ 後台「**第三方整合**」>「**LINE 註冊登入**」。

3. **啟用功能**：貼上 ID 與密鑰，並開啟「**啟用 LINE 登入**」開關後儲存，前台即可看到登入按鈕。

## 進階與增值功能

- **導引加入好友**：在 LINE Developers 的「Basic settings」>「Linked LINE Official Account」中選擇同 Provider 下的官方帳號。設定後，顧客在快速登入時介面會出現「加入好友」的選項。

- **取得手機號碼（企業版/PLUS專用）**：

    - **條件**：Provider 需認證為 **LINE Certified Provider**，且官方帳號需為藍盾或綠盾。

    - **設定**：在 LINE 後台的 Permissions 需包含「OC_PHONE_NUMBER」權限，系統會先進行手機比對再比對 Email，協助商家更新會員手機資訊。

- **自動產生 LIFF 網址**：開啟後可生成 LIFF 連結，消費者在 LINE App 內點擊可實現**自動登入、同時綁定好友與會員**。

## 常見問題排除 (FAQ)

- **出現 400 Bad Request**：通常是 **Callback URL** 填寫錯誤或不完整，請重新檢查網址格式。

- **iOS 無法直接跳轉**：建議消費者使用 **Safari 瀏覽器**，若出現「要在 LINE 中打開嗎？」的彈窗請選擇「打開」；或點擊畫面下方的「使用 LINE 應用程式登入」。

- **帳號綁定邏輯**：當 Facebook 與 LINE 使用同一組 Email 時，系統會自動相互綁定；若 Email 不同，則無法合併帳號。

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