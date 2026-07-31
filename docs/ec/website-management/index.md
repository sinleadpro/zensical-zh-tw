---
author: ""
reviewers: []
products: [EC]
notes: []
title: 管理中心
description: 管理商店基本設定、網域、顧客註冊、管理員權限、資安防護、發票對帳與方案續約。
lang: zh-TW
icon: lucide/settings
permalink: "https://help.cyberbiz.io/ec/website-management/"
hide:
  - feedback
---

## 網站基本設定

<div class="grid cards" markdown>

-   :lucide-store: __設定網站基本資訊__

    ---

    進行網站基本資訊、公司聯繫方式、物流地址及後台語系等核心設置。

    [:octicons-arrow-right-24: 前往](setup-store-basic-info.md)

-   :lucide-languages: __設定前台多國語言與多幣別__

    ---

    多國語言與多幣別功能可協助商家建立本地化的官方網站，透過提供母語介面與熟悉幣別，提升品牌國際化形象並優化海外消費者的購物體驗。

    [:octicons-arrow-right-24: 前往](setup-multi-language-and-multi-currency.md)

-   :lucide-globe: __網域管理__

    ---

    當您在第三方平台購買了專屬網域後，需要透過 DNS 設定將該網域指向您的 CYBERBIZ 商店，並在 CYBERBIZ 後台完成綁定。

    [:octicons-arrow-right-24: 前往](domain-management.md)

</div>

---

## 顧客註冊與會員

<div class="grid cards" markdown>

-   :lucide-user-plus: __顧客註冊流程與欄位__

    ---

    良好的註冊流程能大幅提升新客轉換率。您可以依據營運策略決定「必須註冊」或「快速結帳」模式，並透過自訂欄位蒐集更細緻的會員特徵。

    [:octicons-arrow-right-24: 前往](customer-registration-flow-and-fields.md)

-   :lucide-shield-user: __設定顧客 Email 與手機雙重驗證__

    ---

    要求新註冊顧客同時通過 Email 與簡訊驗證，確保會員資料真實性，降低空帳號與惡意註冊風險。

    [:octicons-arrow-right-24: 前往](setup-customer-email-phone-verification.md)

-   :lucide-mail: __特定網域信箱套用會員標籤__

    ---

    透過網域信箱設定，您可以讓特定組織（如：企業員工、學校機構成員）在註冊完成後，由系統自動為該會員貼上指定的標籤，以便後續提供專屬的行銷優惠或分眾服務。

    [:octicons-arrow-right-24: 前往](apply-member-tags-to-specific-email-domains.md)

</div>

---

## 管理員權限與資安防護

<div class="grid cards" markdown>

-   :lucide-user-plus: __新增網站管理員並設定權限__

    ---

    新增網站管理員、設定管理者權限，並管理帳號安全與二階段驗證。

    [:octicons-arrow-right-24: 前往](add-admin-set-permissions.md)

-   :lucide-shield-check: __保護後台帳號與顧客資料__

    ---

    管理後台登入防護與顧客資料保護，從 IP 白名單、自動登出到網站密碼，一頁完成你的網站資安設定。

    [:octicons-arrow-right-24: 前往](admin-security-settings.md)

-   :lucide-shield: __資安防護總覽與最佳實務__

    ---

    概述各項安全措施、後台設定路徑及資安事件應變指南，全面保障您的網站與顧客個資。

    [:octicons-arrow-right-24: 前往](security-best-practices.md)

-   :lucide-monitor-smartphone: __設定與管理二階段驗證__

    ---

    啟用與管理二階段驗證（2FA），包含驗證器綁定、備用碼使用，以及員工驗證重設與強制啟用。

    [:octicons-arrow-right-24: 前往](setup-manage-two-factor-auth.md)

-   :lucide-shield-ellipsis: __使用 Authy 啟用二階段驗證設定__

    ---

    使用 Authy App 設定 CYBERBIZ 帳號的二階段驗證 (2FA)，提升帳號安全性。

    [:octicons-arrow-right-24: 前往](authy-two-factor-authentication.md)

</div>

---

## 發票與對帳帳款

<div class="grid cards" markdown>

-   :lucide-receipt: __星益欣電子發票設定__

    ---

    教您在 CYBERBIZ 後台完成星益欣電子發票的購買、串接啟用、多站台共用與對帳發票設定。

    [:octicons-arrow-right-24: 前往](wixtar-e-invoice-setup.md)

-   :lucide-file-text: __管理系統代開消費者發票__

    ---

    了解 CYBERBIZ 代開消費者發票服務，包含發票開立方式、顧客與商家查詢流程，以及發票資訊修改的申請期限與費用說明。

    [:octicons-arrow-right-24: 前往](manage-system-issued-consumer-invoices.md)

-   :lucide-receipt: __一鍵開立請款發票__

    ---

    了解如何啟用並使用一鍵開立請款發票功能。企業版商家透過串接星益欣帳戶，即可在對帳中心一鍵完成發票開立，大幅提升請款與撥款效率。

    [:octicons-arrow-right-24: 前往](one-click-invoice-issuance.md)

-   :lucide-circle-check: __自動確認對帳帳款設定__

    ---

    當商家使用 CYBERBIZ PAYMENTS 金流服務時，系統預設需由商家手動確認帳款後方可撥款。啟用「帳款自動確認」功能後，系統將在帳款累計達設定門檻時，於帳期截止日自動完成確認，確保撥款流程不中斷。

    [:octicons-arrow-right-24: 前往](auto-confirm-reconciliation-accounts.md)

-   :lucide-credit-card: __欠款自動扣繳設定__

    ---

    使用 CYBERBIZ PAYMENTS 金流服務時，若當期帳單餘額為負值，系統將透過「欠款自動扣繳」機制從您綁定的信用卡中扣款，確保站台功能正常運作。

    [:octicons-arrow-right-24: 前往](auto-deduction-of-arrears.md)

</div>

---

## 方案續約與系統效期

<div class="grid cards" markdown>

-   :lucide-refresh-cw: __續購與自動續約__

    ---

    為了確保您的商店營運不中斷，您需要定期維護商店方案、SSL 安全性憑證及擴充服務的效期。CYBERBIZ 提供「手動續購」與「自動續約」兩種方式，幫助您彈性管理服務時限。

    [:octicons-arrow-right-24: 前往](renewal-and-auto-subscription.md)

-   :lucide-calendar-clock: __系統到期處理流程__

    ---

    說明系統服務到期提醒規則、續約方式及不續約的資料處理流程，包含網域移轉步驟與緊急應變措施。

    [:octicons-arrow-right-24: 前往](system-expiry-handling-process.md)

-   :lucide-wallet: __Cyber 幣儲值中心使用指南__

    ---

    Cyber 幣儲值中心使用指南，包含儲值步驟、發票資訊填寫、付款方式與使用明細查詢。

    [:octicons-arrow-right-24: 前往](points-deposits.md)

</div>

---

## 疑難排解

<div class="grid cards" markdown>

-   :lucide-mail-warning: __收不到後台登入 Email 驗證信__

    ---

    當您登入後台卻收不到驗證信時，請參考本篇指南進行快速排解。

    [:octicons-arrow-right-24: 前往](not-receiving-backend-login-verification-email.md)

-   :lucide-mail-x: __排除未收到商家通知信件__

    ---

    若 CYBERBIZ 寄出的訂單通知、系統公告等信件被誤歸類至「垃圾郵件」，本篇指南將協助您透過設定，確保能準時接收重要通知。

    [:octicons-arrow-right-24: 前往](troubleshoot-not-receiving-merchant-notifications.md)

-   :lucide-shield-alert: __Cloudflare SSL 衝突__

    ---

    Cloudflare 是全球知名的 DNS 代管與 CDN 加速服務商。若您的網域代管於 Cloudflare，在將網址指向 CYBERBIZ 時，必須針對 Proxy 功能進行特定設定，以確保網站能順利載入並正確套用 SSL 安全憑證。

    [:octicons-arrow-right-24: 前往](cloudflare-ssl-conflict.md)

-   :lucide-globe: __無法讀取 HTTPS 根網址__

    ---

    當網站從其他平台遷移至 CYBERBIZ 後，若出現 http://您的網址 可正常開啟，但 https://您的網址 無法讀取的情況，通常與網域商對「根網域（Naked Domain）」的轉址支援度有關。

    [:octicons-arrow-right-24: 前往](unable-to-read-https-root-url.md)

</div>