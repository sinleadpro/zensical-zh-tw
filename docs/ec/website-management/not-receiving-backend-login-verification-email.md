---
title: 收不到後台登入 Email 驗證信
description: 當您登入後台卻收不到驗證信時，請參考本篇指南進行快速排解。
created: 2026-05-27 11:55
last_modified: 2026-05-27 12:00
lang: zh-TW
type: troubleshooting
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結：資安防護
ga_views: 0
feedback: 0
products: 
  - EC
  - POS
modules: 
  - 管理中心
  - 安全性設定
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 解決收不到驗證信問題
  - 了解後台登入安全機制
features: 
  - MFA_驗證
  - 2FA_驗證
  - 資安防護
prerequisites: []
related: []
tags: 
  - 無法登入
  - 驗證信
  - MFA
  - 2FA
  - 資安
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: []
paths: 
  - 管理中心 > 安全性設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12859
  - https://www.cyberbiz.io/support/?p=52847
permalink: "https://help.cyberbiz.io/ec/website-management/not-receiving-backend-login-verification-email/"
comments: false
search:
  exclude: false
icon: lucide/mail-warning
hide: []
---
# 收不到後台登入 Email 驗證信
當您登入後台卻收不到驗證信時，請參考本篇指南進行快速排解。
{ .subtitle }


!!! tip "應用情境"
	- **登入受阻**：輸入帳密後遲遲未收到信箱驗證碼。
	- **資安確認**：了解為什麼系統要求進行雙重驗證。
	- **防護升級**：學習如何透過 2FA 提升帳號安全性。

## 聯繫支援

若嘗試上述步驟後仍無法收到驗證信，請準備以下資訊並寄送 Email 至 **security-ts@cyberbiz.io**，我們將由專人協助您排除問題。

- **信件主旨**：【後台登入協助】公司名稱 / 官網名稱
- **信件內容**：
    - 官網網址
    - 登入帳號（Email）
    - 聯絡人姓名與電話


## 快速排解步驟

若您尚未收到驗證信或無法完成登入，請先執行以下檢查：

1. **檢查信箱分類**：確認信件是否被歸類至「垃圾信件」或「廣告信件」。
2. **確認信箱空間**：檢查信箱容量是否已滿，或是否存在收信異常。
3. **重新發送**：點擊登入頁面的 **重新發送驗證碼**。
4. **關鍵字搜尋**：在信箱中搜尋關鍵字 **後台登入驗證碼** 或 **驗證碼** 快速過濾信件。

![](https://www.cyberbiz.io/support/wp-content/uploads/Email信件-後台MFA驗證信.png){ .screenshot }



## 後台登入雙重驗證機制說明

為強化資安防護並阻絕跨境駭客攻擊，CYBERBIZ 已全面啟動後台登入雙重驗證機制。登入時將依據您的設定採取以下驗證方式：

=== "方式 A：2FA 行動 APP 驗證（推薦）"
    若您已啟用 [二階段驗證 (2FA)](setup-manage-two-factor-auth.md)，請開啟手機的 **Google Authenticator App**，獲取即時動態驗證碼。此方式具備最高層級的資安防護。

=== "方式 B：MFA 信箱驗證"
    若您尚未啟用 2FA，系統將自動寄送「身分驗證碼」至您的登入 Email。請於時限內輸入驗證碼以完成登入。



## 資安防護建議

為建構更嚴密的防禦體系，強烈建議商家完成以下配置，守護企業資產與消費者隱私：

### 1. 啟用 2FA 雙重身分驗證
這是防止帳號遭盜用的最強力防線。即便密碼遭竊，駭客仍無法突破第二層驗證。
> 前往設定：[設定與管理二階段驗證](setup-manage-two-factor-auth.md)

### 2. 進階登入安全防護
利用 **IP 白名單** 與 **reCAPTCHA 驗證機制**，有效阻斷自動化腳本攻擊。
> 前往設定：[安全性設定](security-settings.md)

### 3. 定期稽核與監測
養成定期檢查「網站登入者名單」與「登入紀錄」的習慣，監測是否有不明 IP 或非授權人員存取。
> 了解更多：[資安防護機制說明](security-best-practices.md)


