---
title: 系統到期處理流程
description: 說明系統服務到期提醒規則、續約方式及不續約的資料處理流程，包含網域移轉步驟與緊急應變措施。
created: 2026-05-27 11:40
last_modified: 2026-06-30 08:02
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
  - 官網設定
  - 管理中心
sites: 
  - TW
audiences: 
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
  - 了解系統到期通知規則
  - 執行網域移轉
  - 處理到期緊急應變
features: 
  - 系統到期提醒
  - 網域移轉
  - 緊急網域切換
prerequisites: []
related:
  - ec/website-management/renewal-and-auto-subscription/
  - pos/store/renewal-and-add-on-plans/
tags: 
  - 系統到期
  - 續約
  - 網域移轉
  - SSL
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: []
paths: 
  - 管理中心 > 網域管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3988
  - https://www.cyberbiz.io/support/?p=21601
permalink: "https://help.cyberbiz.io/ec/website-management/system-expiry-handling-process/"
comments: false
search:
  exclude: false
icon: lucide/calendar-clock
hide: []
---

# 系統到期處理流程
說明系統服務到期提醒規則、續約方式及不續約的資料處理流程。
{ .subtitle }


!!! tip "應用情境"
	- **掌握續約時機**：了解系統何時發出到期通知，避免因忙碌遺漏續約資訊。
	- **管理網域移轉**：將 CYBERBIZ 代管的網域移轉至商家自有帳戶，實現自主管理。
	- **處理緊急故障**：當 SSL 或網域過期導致網站無法進入時，快速切換備用網域恢復營運。


## 使用須知

- **資料備份義務**：若決定不續約，請務必於服務終止前完成所有系統資料（如顧客、訂單、商品、圖片）的匯出與儲存。
- **後台存取限制**：網站到期後，商家將無法進入後台儲存或修改任何資料，消費者亦無法進入網站。
- **提醒觸發邏輯**：續約提醒以瀏覽器為基準。若在單一瀏覽器勾選「已閱讀」，系統將在下一個提醒日再次跳出通知；若更換瀏覽器或使用無痕模式，則會再次顯示。

## 操作流程

### 1. 了解各項服務續約方式

系統服務包含[網站系統與 SSL 安全性憑證](renewal-and-auto-subscription.md)、[POS 系統](../../pos/store/renewal-and-add-on-plans.md)、電子發票（[星益欣]()）及網域，可依需求於後台完成續約。


### 2. 系統到期提醒規則

系統將針對 **網站系統**、**POS 系統**、**SSL 安全性憑證** 及 **CYBERBIZ 代購網域** 發送提醒。

- **提醒時間點**：到期前 **90、60、30、15、7、3、1** 天。
- **操作方式**：當跳出提醒通知時，請勾選「我已閱讀並同意上述事項」。
- **備註**：若已申請移轉網域至商家自管，系統仍可能跳出提醒，屆時請點選「已閱讀」或忽略即可。

### 3. 執行網域移轉（代管轉自管）

若您的網域目前由 CYBERBIZ 代為管理，欲改為商家自行管理，請進行網域移轉。

> 下方以 Godaddy 作為範例

1. 前往 **Godaddy 官方網站** 申請個人帳號。
2. 提供您的 Godaddy **帳戶 Email** 與 **帳戶編號** 給 CYBERBIZ 續約顧問。
3. 查收來自 Godaddy 的網域移轉確認信，點擊連結並勾選 **跳過審核並批准所有信息**。

    !!! warning "重要注意事項"
        此階段請勿更改聯絡人資訊，否則可能導致移轉時間延長至 1 個月以上。
  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/系統到期通知說明02.png){ .screenshot }

4. 通知 CYBERBIZ 已完成確認，待系統執行轉出後，至 Godaddy 帳戶確認接受轉移。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/系統到期通知說明03.png){ .screenshot }


### 4. 處理網域或 SSL 到期緊急應變

當 SSL 憑證或網域過期導致網站顯示不安全或無法進入時，可採取以下緊急措施：

1. 登入 CYBERBIZ 管理後台，前往 **管理中心 > 網域管理**。
2. 將 **cyberbiz.co** 網域設為主網域。
3. 系統將暫時解除無法進入網站的問題，待續約完成後再恢復自有網域設定。

![](https://www.cyberbiz.io/support/wp-content/uploads/系統到期通知說明01.png){ .screenshot }


