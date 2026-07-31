---
title: 快速開店新手指南
description: CYBERBIZ 網站初步設定與基本功能導覽，協助商家快速完成開店準備。
last_modified: 2026-07-22 17:33
lang: zh-TW
permalink: "https://help.cyberbiz.io/ec/get-started/"
wp_url:
  - https://www.cyberbiz.io/helpcenter/?page_id=3610
  - https://www.cyberbiz.io/helpcenter/?page_id=1933
  - https://www.cyberbiz.io/support/?page_id=17972
  - https://www.cyberbiz.io/support/?page_id=29441 
type: tutorial
status: update
author: Jase
reviewers: []
notes: []
products:
  - EC
modules:
  - 管理中心
  - 金物流
  - 商品
  - 網站外觀
  - 行銷活動
  - 第三方整合
  - 訂單
  - 會員
  - 訊息推播
  - 分析報表
  - 分潤
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans:
  - 企業
  - 專業
  - 專業PLUS
  - 進階
  - 進階PLUS
  - 高手
  - 高手PLUS
devices:
  - desktop
paths: []
intents:
  - 快速開店
  - 系統初步設定
features: []
prerequisites: []
related: []
tags:
  - 開店指南
  - 新手教學
  - 快速設定
icon: lucide/rocket
hide:
search: 
  exclude: 
---

本指南將帶您從基本資訊填寫、網域設定、金物流串接、商品上架、網站外觀設計，一路到行銷活動、第三方整合與訂單管理，協助您快速完成 CYBERBIZ EC 網站的初步設定。

<!-- 想看影音版教學文件，請至 [影片教學資源總覽](../resources/video-tutorials.md){ title="影片教學資源總覽" }。在您使用 CYBERBIZ 系統服務期間，CYBERBIZ 提供一組「客戶專屬登入帳號」，透過此組帳號即可免費觀看部分付費課程。 -->

## 初步設定

### 步驟一：設定基本資訊

- 【管理中心】>【一般設定】填寫「[公司聯絡資訊](../ec/website-management/setup-store-basic-info.md#operate-general-preferences-company-info)」
- 【管理中心】>【網站權限 / 方案】設定「發票類型」、「管理員列表」
- 【訊息推播】>【[Email 通知樣版](../ec/notifications/manage-email-templates.md)】可設定其他管理員收到訂單成立等相關通知信件

<div class="grid cards" markdown>

- :lucide-store:{ .lg } [__網站資料設定說明__](website-management/setup-store-basic-info.md){ title="設定網站基本資訊" }

</div>

!!! tip "發票提醒"
    若在後台儲值或續約，開立發票後將以您設定的發票類型寄送至您的信箱。

---

### 步驟二：網域 & SSL 安全憑證設定

- 【管理中心】>【網域管理】確認主網域名稱
- CYBERBIZ 提供的免費網域 `_____.cyberbiz.co` 已附有 SSL 無須加裝
- 若想更換為其他網域名稱，請至 [Gandi](https://www.gandi.net/zh-Hant)、[GoDaddy](https://tw.godaddy.com/) 官網註冊購買
- 轉址完成後，系統將於 24 小時內自動加裝 SSL 安全憑證

<div class="grid cards" markdown>

- :lucide-globe:{ .lg } [__網域設定教學文件__](website-management/domain-management.md){ title="網域管理" }

</div>

---

### 步驟三：設定金流

【金物流】>【結帳頁 & 物流設定】

<div class="grid cards" markdown>

- :lucide-credit-card:{ .lg } [__金流設定說明__](payments-and-logistics/payments/index.md){ title="結帳頁與物流設定總覽" }
<!-- - :lucide-wallet:{ .lg } [__指定付款方式限定金額設定__](payments-and-logistics/index.md){ title="付款金流" } -->
<!-- - :lucide-coins:{ .lg } [__全館最低消費金額功能設定__](payments-and-logistics/payments/order-settings.md){ title="訂單相關設定" } -->

</div>

!!! tip "什麼是金流"
    金流意即您向消費者收錢的各種支付方式，如信用卡、虛擬 ATM、超商代碼繳費、LINE Pay、街口…等。您可以自由選擇想提供的支付方式。

---

### 步驟四：設定物流

- 【金物流】>【宅配物流】設定「宅配」運費規則
- 【金物流】>【超商物流】設定「超商取貨」功能

<div class="grid cards" markdown>

- :lucide-truck:{ .lg } [__如何設定運費__](payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md){ title="建立宅配貨到不付款/自訂物流" }
- :lucide-store:{ .lg } [__超商店到店寄件（C2C）設定__](payments-and-logistics/setup-cvs-c2c-shipping.md){ title="設定超商店到店 C2C 物流串接" }
- :lucide-warehouse:{ .lg } [__超商大宗寄倉（B2C）設定__](payments-and-logistics/setup-cvs-b2c-bulk-shipping.md){ title="設定超商大宗寄倉 B2C" }
- :lucide-banknote:{ .lg } [__黑貓 / 宅配通貨到付款設定方式__](payments-and-logistics/home-delivery-cash-on-delivery.md){ title="宅配貨到付款物流（黑貓/宅配通/新竹物流）" }
- :lucide-truck:{ .lg } [__黑貓宅到店貨到付款設定方式__](orders/tcat-quick-store/tcat-express-payment-settings.md){ title="設定黑貓快速到店付款方式" }
- :lucide-settings-2:{ .lg } [__宅配貨到不付款設定（自訂物流）__](payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md){ title="建立宅配貨到不付款/自訂物流" }

</div>

!!! tip "什麼是物流"
    物流意即您將商品寄送到客人手上並使對方收取貨物的運送方式，如宅配、超商取貨…等。您可以自由選擇想提供的運送方式及合作廠商，如黑貓、宅配通、7-11、全家…等。

---

### 步驟五：建立商品

- 【商品】>【所有商品】新增您的商品
- 【行銷活動】設定特定商品的優惠活動
- 或以「商品自訂分類」、「商品條件分類」（設定首頁連結列表時可能會用到）

<div class="grid cards" markdown>

- :lucide-package:{ .lg } [__如何單筆上架商品__](products/create-and-manage/create-update-products.md){ title="新增與更新商品" }
- :lucide-file-spreadsheet:{ .lg } [__如何大量上架商品__](products/bulk-operations/excel-import-products.md){ title="Excel 大量匯入商品" }
- :lucide-ruler:{ .lg } [__排除超商材積限制設定__](products/shipping/cvs-shipping-restrictions-exclusions.md){ title="設定超商配送限制與物流排除" }
- :lucide-folder-tree:{ .lg } [__商品自訂分類設定__](products/categories-and-tags/custom-collections.md){ title="設定商品自訂分類群組" }
- :lucide-list-filter:{ .lg } [__商品條件分類設定__](products/categories-and-tags/smart-collections.md){ title="設定商品條件分類群組" }

</div>

!!! tip "行銷活動搭配"
    許多指定商品優惠活動如任選折扣、加價購、滿額贈、紅配綠組合、紅利加碼送、限購商品、紅利商城、首購禮…等皆於【行銷活動】設定，可根據您的商品特性設計適合的活動。

---

### 步驟六：網站外觀 & 內容設計

- 【網站外觀】>【套版主題管理】選擇您喜歡的網站設計
- 【網站外觀】>【套版主題管理】>【網站設定】編輯首頁圖片 / 文字內容
- 【網站外觀】>【CSS/HTML 編輯器】修改語法內容（非必要）
- 首頁上方選單連結內容，請至【網站外觀】>【選單 / 導覽列設定】設定

<div class="grid cards" markdown>

- :lucide-palette:{ .lg } [__如何套用 / 更換主題套版__](website-appearance/theme-and-layout/apply-and-switch-theme.md){ title="套用與更換網站主題" }
- :lucide-menu:{ .lg } [__首頁上方選單連結設定（連結列表）__](website-appearance/navigation/setup-menus-navigation.md){ title="設定選單與導覽列" }
- :lucide-map-pin:{ .lg } [__如何設定網站下方 Google Map 地圖__](website-appearance/customer-interaction/setup-edit-customer-service-info.md){ title="設定與修改客服中心資訊" }
- :material-sitemap:{ .lg } [__如何設定 SiteMap 增加網站曝光機會__](website-management/seo/submit-sitemap-to-gsc.md){ title="將 Sitemap 提交至 Google Search Console" }
- :lucide-file-text:{ .lg } [__如何編輯部落格文章__](website-appearance/pages-and-content/blog-management-publishing-guide.md){ title="部落格管理與文章發佈指南" }

</div>

!!! tip "加值服務需求"
    若有素材設計、網站語法修改等需求，CYBERBIZ 提供第三方合作廠商媒合服務，請洽您的開店顧問。

---

### 步驟七：設定全館行銷活動

- 【行銷活動】>【全館折扣-紅利 & 優惠券】設定全館活動（折扣 / 折價券 / 會員紅利點數…等）
- 【金物流】>【宅配運費設定】設定全館免運
- 【會員】>【VIP 設定】設定會員 VIP 優惠活動

<div class="grid cards" markdown>

- :lucide-percent:{ .lg } [__設定全館折扣__](marketing/discounts/storewide-discounts.md){ title="設定全館折扣" }
<!-- - :lucide-truck:{ .lg } [__設定全館免運__](payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md){ title="建立宅配貨到不付款/自訂物流" } -->
- :lucide-ticket:{ .lg } [__設定全館贈送優惠券__](marketing/coupon/setup-coupons.md){ title="設定優惠券" }
- :lucide-gift:{ .lg } [__設定全館贈送會員紅利__](marketing/bonus-and-gifts/setup-bonus-points.md){ title="設定紅利點數" }
- :lucide-cake:{ .lg } [__設定生日禮送紅利__](marketing/bonus-and-gifts/setup-birthday-gift.md){ title="設定生日禮" }
- :lucide-user-plus:{ .lg } [__設定註冊禮送紅利__](marketing/bonus-and-gifts/setup-registration-gift.md){ title="設定註冊禮" }
- :lucide-crown:{ .lg } [__會員 VIP 制度設定__](members/vip/setup-store-wide-vip-system.md){ title="建立全館VIP制度" }

</div>

---

### 步驟八：設定第三方廠商串接

【第三方整合】選擇您需要設定的項目：

<div class="grid cards" markdown>

- :lucide-share-2:{ .lg } [__Facebook 相關設定__](integrations/fb/index.md){ title="Facebook 總覽" }
- :simple-google:{ .lg } [__Google 相關設定__](integrations/google/index.md){ title="Google 整合" }
- :lucide-message-circle:{ .lg } [__LINE 相關設定__](integrations/line/index.md){ title="LINE 整合總覽" }
- :lucide-shopping-bag:{ .lg } [__美安 Shop.com 相關設定__](integrations/setup-shop-com.md){ title="串接美安通路" }

</div>

!!! tip "初步設定完成"
    截至步驟八，您已經完成了網站初步設定！接下來的步驟九至步驟十三，要帶您了解網站正式經營後會經常使用到的功能，請您繼續閱讀下方說明。

## 進階設定

### 步驟九：了解訂單作業流程

【訂單】查看您的訂單並於此操作出貨、退貨流程：

<div class="grid cards" markdown>

- :lucide-truck:{ .lg } [__單筆 / 批次訂單出貨流程__](orders/basics/order-fulfillment-flow.md){ title="訂單出貨流程" }
- :lucide-help-circle:{ .lg } [__訂單出貨方式說明及常見問題__](orders/basics/order-fulfillment-flow.md){ title="訂單出貨流程" }
- :lucide-search:{ .lg } [__如何搜尋及篩選訂單__](orders/basics/search-filter-orders.md){ title="如何搜尋與篩選訂單" }
- :lucide-clipboard-list:{ .lg } [__單一訂單頁面介紹__](orders/basics/order-management-interface.md){ title="訂單管理介面說明" }
- :lucide-printer:{ .lg } [__如何補印託運單__](payments-and-logistics/setup-print-tcat-waybill-v2.md){ title="設定與加印黑貓託運單" }
- :lucide-x-circle:{ .lg } [__取消訂單說明__](orders/basics/cancel-order.md){ title="如何取消訂單" }
- :lucide-check-circle:{ .lg } [__結案訂單說明__](orders/order-settings/manual-order-close.md){ title="如何手動結案訂單" }
- :lucide-undo-2:{ .lg } [__一般退貨退款流程說明__](orders/order-return-process.md){ title="訂單退貨流程" }
- :lucide-rotate-ccw:{ .lg } [__部份退貨退款流程說明__](orders/order-refund-process.md){ title="訂單退款流程" }
- :lucide-truck:{ .lg } [__如何透過後台系統請物流人員收取退貨（黑貓 / 宅配通）__](orders/order-return-process.md){ title="訂單退貨流程" }
- :lucide-clock-alert:{ .lg } [__超商訂單逾期未取退貨流程__](orders/returns-refunds/cvs-unclaimed-order.md){ title="處理超商訂單逾期未取" }
- :lucide-calendar-x:{ .lg } [__超過您設定之退貨申請期限的退貨流程__](orders/returns-refunds/overdue-return-handling.md){ title="處理超過退貨期限的訂單" }

</div>

---

### 步驟十：了解客服問答功能

【會員】>【所有客服問題】客人透過前台「聯絡我們」發送訊息及訂單下方留言將收集至此處，您可於此區回覆顧客並管理訊息。

<div class="grid cards" markdown>

- :lucide-headset:{ .lg } [__客服問答功能說明__](members/member-customer-service-system.md){ title="會員客服系統" }

</div>

---

### 步驟十一：了解推播工具 EDM & 簡訊

進入【訊息推播】>【發送簡訊】&【發送 EDM】發送網站相關訊息給顧客，如優惠活動、重大提醒…等。

<div class="grid cards" markdown>

- :lucide-smartphone:{ .lg } [__簡訊發送設定教學__](notifications/send-sms-notifications-v2.md){ title="設定與發送簡訊通知" }
- :lucide-mail:{ .lg } [__EDM 發送設定教學__](notifications/send-edm-newsletters-v2.md){ title="設定與發送 EDM 電子報" }

</div>

---

### 步驟十二：了解分析報表

進入【分析報表】依不同數據了解您的網站營運狀況：

<div class="grid cards" markdown>

- :lucide-chart-no-axes-column:{ .lg } [__營運圖表相關說明__](business-intelligence/index.md){ title="報表分析" }

</div>

### 步驟十三：其他特殊功能

- 進入【行銷活動】>【一頁式商店】設定一頁式商店為指定商品建立快速購買連結

<div class="grid cards" markdown>

- :lucide-shopping-bag:{ .lg } [__一頁式商店設定說明__](marketing/one-page-store/one-page-store.md){ title="一頁式商店" }

</div>

- 進入【行銷活動】>【定期定額活動頁】設定讓消費者可以訂閱制方式自動定期購買您的商品

<div class="grid cards" markdown>

- :lucide-repeat:{ .lg } [__定期定額活動設定說明__](marketing/other-tools/subscription-campaign-page.md){ title="定期訂購活動頁" }

</div>

- 進入【分潤】設定與第三方、員工、顧客合作的分潤方案

<div class="grid cards" markdown>

- :lucide-share-2:{ .lg } [__推薦分潤設定 – 第三方__](profit-sharing/referrer-profit-sharing.md){ title="推薦人分潤" }
- :lucide-user-check:{ .lg } [__推薦分潤設定 – 員工__](profit-sharing/referrer-profit-sharing.md){ title="推薦人分潤" }
- :lucide-users:{ .lg } [__推薦分潤設定 – 顧客__](profit-sharing/referrer-profit-sharing.md){ title="推薦人分潤" }
- :lucide-user-plus:{ .lg } [__註冊分潤設定 – 員工__](profit-sharing/registrant-profit-sharing.md){ title="註冊人分潤" }

</div>

!!! tip "分潤應用"
    若與網紅、團媽合作即可透過此功能設定專屬連結、折扣碼，且合作對象能自行透過密碼查詢業績及應得分潤金額。也可設定您的會員或內部員工若有促成訂單，即可獲取獎金或紅利的制度。
