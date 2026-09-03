---
title: 設定管理員登入安全防護
description: 透過 IP 白名單、二階段驗證 (2FA)、自動登出與密碼規則設定，強化後台帳號安全，防止未經授權的登入與帳號盜用。
created: 2026-08-12 10:59
last_modified: 2026-08-12 10:59
lang: zh-TW
type: guide
status: ""
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
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 加強後台安全性
  - 防範後台帳號盜用
  - 設定登入驗證
  - 設定 IP 白名單
features:
  - 管理員登入安全
  - IP白名單
  - 瀏覽器Cookie驗證
  - 自動登出時間
  - reCAPTCHA驗證
  - 二階段驗證(2FA)
  - 管理員密碼規則
prerequisites:
  - 先確認自己的 IP
related:
  - ec/website-management/member-security-settings/
  - ec/website-management/bot-protection-settings/
  - ec/website-management/add-admin-set-permissions/
  - ec/website-management/setup-manage-two-factor-auth/
tags:
  - 管理員安全
  - IP 白名單
  - 2FA
  - 二階段驗證
  - 自動登出
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 安全性設定 > 管理員登入
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3214
  - https://www.cyberbiz.io/support/?p=14334
  - https://www.cyberbiz.io/support/?p=472
permalink: "https://help.cyberbiz.io/ec/website-management/admin-security-settings/"
comments: false
search:
  exclude: false
icon: lucide/shield-check
hide: []
---

# 設定管理員登入安全防護

「管理員登入」設定提供多層次的防護機制，確保只有獲得授權的人員能存取您的商店後台。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 全方案
{ .doc-badge }

![安全性設定頁面-hero](../../assets/images/ec-管理中心-安全性設定.png){ .hero-page }

## 安全性設定說明 { #intro-security }

「安全性設定」是 CYBERBIZ 後台的資安控制中心，協助你降低帳號被盜用、顧客個資外洩與惡意造訪的風險。頁面位於後台「管理中心」>「安全性設定」，並分為三個主要防護領域：

- **[會員安全](member-security-settings/)**：負責保護網站與顧客資料。
- **管理員登入**：負責保護你與員工登入後台的安全。
- **[機器人防護](bot-protection-settings/)**：負責過濾惡意訪客，在簡訊發送前建立第一道防線。


## 使用前提與限制 { #prerequisites-security }

開始設定前，請先確認下列條件：

- [x] **「設置」權限**：除了二階段驗證（每位管理員都能為自己設定）之外，其餘區塊都需要您的帳號在 **網站權限** 中具備 **設置** 權限，才能檢視與編輯。您可[修改管理員權限](add-admin-set-permissions/#管理者權限設定與修改)。


## 操作步驟 { #operate-security }

前往後台 **管理中心 > 安全性設定** 後，點選上方 **管理員登入** 分頁即可開始設定。

### 設定 IP 白名單 { #operate-security-ip-whitelist }

啟用後，只有名單內的 IP 位址能登入後台，適合在固定辦公室或固定網路環境營運的商家。

1. **進入區塊：** 在 **管理員登入** 分頁，找到 **白名單** 區塊。
2. **確認目前 IP：** 區塊會顯示 **您目前的 IP**，請先記下，稍後務必把它加入名單，避免把自己擋在門外。
3. **新增信任 IP：** 點擊 **新增 IP** ，在 **增加 IP 位址** 視窗輸入要放行的位址，按 **增加** 完成。[^ip-format]

    - 務必先把 **目前所在的 IP 加入名單**，否則啟用後會立即被登出且無法登入。

        !!! warning "工程救援費用"
            若因白名單鎖定而無法進入後台，請洽 CYBERBIZ 客服協助，若有開啟客服進入後台權限則無需工程介入。若有工程介入之必要，將酌收 2,000 元服務工本費。

    - 若貴公司IP為浮動IP，**請勿使用浮動 IP** 新增白名單（如：手機WiFi分享）。請使用 **固定 IP** 增設白名單，否則將導致後續無法登入問題。

4. **啟用白名單：** 開啟 **啟用白名單** 開關。若你目前的 IP 不在名單內，系統會跳出提醒[^whitelist-lockout]，確認後才會生效。
5. **管理名單：** 名單以表格列出（每頁 5 筆），點擊每列的刪除圖示可移除位址。

![](../../assets/images/ec-管理中心-安全性設定-白名單.png)

[^ip-format]: 支援 IPv4、IPv6 與 CIDR 網段格式；格式錯誤時欄位會顯示「IP 位址格式錯誤」。
[^whitelist-lockout]: 啟用提醒文字為「您目前的IP位址不在白名單內，啟用後將立即被登出無法登入後台，確認要啟用？」。若你刪除的是目前所在的 IP，系統同樣會再次確認，避免把自己鎖在門外。



### 瀏覽器 Cookie 驗證 IP 白名單 { #operate-security-cookie-whitelist }

這項功能與上方的 IP 白名單不同：它不是限制誰能登入，而是讓你把「會頻繁變動的可信任 IP」加入名單，避免在同一瀏覽器操作時因 IP 跳動而被強制重新登入。

> **判斷是否需要**：若登入後因 IP 頻繁變動，導致反覆被登出，才需設定；固定 IP 或 IP 穩定時不需開啟。

1. **進入區塊：** 在 **管理員登入** 分頁找到 **瀏覽器 Cookie 驗證 IP 白名單** 區塊。
2. **新增可信任 IP：** 點擊 **新增 IP** ，於 **增加 IP 位址** 視窗輸入位址，按 **增加** 完成。
3. **啟用功能：** 開啟 **啟用瀏覽器 Cookie 驗證 IP 白名單** 開關即可。

![](../../assets/images/ec-管理中心-安全性設定-cookie whitelist.png)



### 設定自動登出時間 { #operate-security-logout-timer }

設定後台閒置多久就自動登出，降低電腦無人看管時被他人誤用的風險。

> 若多人共用電腦或在公共空間操作後台，建議選擇較短的閒置時間（如 4 小時），安全性較高。

1. **進入區塊：** 在 **管理員登入** 分頁找到 **自動登出時間** 區塊。
2. **選擇時間：** 從五個選項中擇一：**4小時**、**8小時**、**1天**、**3天**、**7天**。
3. **儲存設定：** 點擊 **更改** 套用。

![](../../assets/images/ec-管理中心-安全性設定-自動登出時間.png)


### 後台登入 reCAPTCHA 驗證 { #operate-security-recaptcha }

在後台登入頁加上 Google reCAPTCHA 機器人驗證，減少自動化腳本嘗試破解帳號的風險。

1. **進入區塊：** 在 **管理員登入** 分頁找到 **reCAPTCHA 驗證** 區塊。
2. **開啟驗證：** 開啟 **啟用 reCAPTCHA 驗證** 開關，設定即時生效。下次登入後台時就會出現 reCAPTCHA 驗證。

![](../../assets/images/ec-管理中心-安全性設定-reCAPTCHA 驗證.png)


### 二階段驗證 { #operate-security-2fa }

二階段驗證（2FA）是防止帳號被盜用最有效的防線：即使密碼外洩，沒有手機驗證器產生的動態驗證碼也無法登入。

1. **進入區塊：** 在 **管理員登入** 分頁找到 **二階段驗證設定** 區塊。
2. **開啟功能：** 開啟 **啟用二階段驗證步驟** 開關，畫面會展開 **安裝步驟**。
3. **安裝驗證器：** 在手機安裝 Authenticator 應用程式（提供 iOS 與 Android 下載）。
4. **綁定帳號：** 用 Authenticator 掃描畫面上的 QR code，或手動輸入畫面提供的代碼。
5. **完成驗證：** 將 Authenticator 顯示的六位數驗證碼填入 **驗證碼** 欄位，即完成啟用。
6. **保存備用碼：** 啟用後系統會產生「驗證備用碼」，請妥善保存，當無法使用驗證器時可用來登入。

    !!! warning "備用碼保存與使用須知"
        為了安全，備用碼只會顯示這一次，請在啟用當下立即保存。每組僅能使用一次，遺失時可在區塊內「重新產生備用碼」。停用二階段驗證時，需先輸入使用者密碼確認。

![](../../assets/images/ec-管理中心-安全性設定-2FA.png)


<div class="grid cards" markdown>

- :lucide-shield-check:{ .lg } [__二階段驗證設定教學__](setup-manage-two-factor-auth.md)

</div>




## 常見問題 { #faq-security }

??? quote "「白名單」和「瀏覽器 Cookie 驗證 IP 白名單」有什麼不同？"
    [](){ #faq-security-two-whitelists }
    兩者用途完全不同：

    - **白名單**：限制「誰能登入後台」，只有名單內的 IP 才能登入，是主動的存取控管。
    - **瀏覽器 Cookie 驗證 IP 白名單**：解決「同一瀏覽器 IP 跳動時被強制重新登入」的困擾，屬於便利性設定。


??? quote "更換手機後收不到二階段驗證碼怎麼辦？"
    [](){ #faq-security-2fa-lost-phone }
    若您已更換手機或遺失原本的驗證裝置，將無法自行產生 2FA 驗證碼。請聯繫網站擁有者或具備權限的管理員，至「管理中心 > 安全性設定 > 二階段驗證」協助關閉該帳號的 2FA，關閉後再重新綁定新裝置即可。
