---
title: API 與 Webhook 串接指南
description: 了解如何透過 API 與 Webhook 服務串接外部系統（如 ERP、CRM），實現自動化數據同步與即時通知。
created: 2026-06-11 14:45
last_modified: 2026-06-27 13:40
lang: zh-TW
type: guide
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
  - APP MARKET
  - 管理中心
sites: 
  - TW
audiences: 
  - admin
  - developer
difficulty: intermediate
tnb: branch
plans: 
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents: 
  - 串接 API
  - 設定 Webhook
  - 整合外部系統
features: 
  - API
  - Webhook
  - 自訂擴充服務
prerequisites: 
  - "需為企業版方案或 PLUS 版加購 API 服務"
  - "需具備技術開發人員進行程式串接"
related: []
tags: 
  - API
  - Webhook
  - 系統整合
  - 自動化
acoiv: integration
apis: []
devices: 
  - desktop
ui_components: 
  - 我的擴充服務
  - 網站權限
paths: 
  - APP MARKET > 我的擴充服務 > 自訂
  - 管理中心 > 網站權限
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7875
  - https://www.cyberbiz.io/helpcenter/?p=8544
  - https://www.cyberbiz.io/support/?p=20739
  - https://www.cyberbiz.io/support/?p=40162
permalink: https://help.cyberbiz.io/ec/app-market/api-and-webhook-integration-guide
search:
  exclude: false
icon: lucide/code-2
hide: []
---

# API 與 Webhook 串接指南
了解如何透過 API 與 Webhook 服務串接外部系統（如 ERP、CRM），實現自動化數據同步與即時通知。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
{ .doc-badge }

!!! info "版本差異說明"
    - 「API 與 Webhook 串接服務」在 PLUS 方案中屬於選配模組（11 選 2），商家需確認已選配該模組方可使用。企業版則直接內建此功能。


## 使用須知

- **技術門檻**：API 與 Webhook 串接需由工程人員進行開發。CYBERBIZ 僅提供介面與文件，不提供程式撰寫等技術實作服務。
- **開通申請**：若您的後台未顯示相關功能，請聯繫系統客服提出開通需求。
- **流量限制**：
    - **頻率限制**：每秒至多 5 個請求 (Request)。
    - **資料限制**：每個請求上限為 2 MB。
- **權限要求**：操作人員需具備 **自訂應用程式** 權限，請前往 **管理中心 > 網站權限** [設定權限](../website-management/add-admin-set-permissions/)。
  ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook10.png){ .screenshot }



## 核心概念說明

### API

API 是一種雙向的資訊交換機制。您的系統可主動向 CYBERBIZ 伺服器發送請求，執行取得 (Get)、建立 (Post)、更新 (Put) 或刪除 (Delete) 系統資訊的操作。

### Webhook

Webhook 類似於「訂閱服務」。當 CYBERBIZ 系統發生特定事件（如訂單成立、會員註冊）時，系統會即時將最新資訊推送至您預設的網址 (Endpoint URL)，利於後續自動化判斷。



## 操作流程

### 步驟一：建立自訂應用程式

在後台建立應用程式以取得串接所需的憑證。

1. 登入 CYBERBIZ 管理後台，前往 **APP MARKET > 我的擴充服務**。
2. 切換至 **自訂** 分頁，點擊 **建立自訂應用程式**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook01.png){ .screenshot }

3. 設定 **應用程式名稱** 並配置 **API scope**（權限範圍）：
    - **read_**：僅能執行取得資料 (Get) 的操作。
    - **write_**：可執行建立、更新與刪除 (Post, Put, Delete) 的操作。
4. 設定完成後，系統將產生 **APP Secret** 與 **API Token**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook02.png){ .screenshot }

### 步驟二：設定 Webhook 事件

若需接收即時通知，請配置 Webhook 訂閱。

1. 在應用程式設定頁面中，找到 **Webhook Events** 欄位。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook08.png){ .screenshot }

2. 勾選欲訂閱的事件類型（如 `orders/create`, `customers/update`）。
3. 在 **Endpoint URL** 欄位填入接收資料的網址。

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook09.png){ .screenshot }

4. 點擊 **儲存**，系統將開始推送相關事件資訊。


## 開發參考資訊

### API 文件查詢

您可以透過測試帳號登入 API 文件中心，查看各項 API 的詳細參數與資料格式。

- **文件網址**：[https://api-doc.cyberbiz.co/v1/api_document](https://api-doc.cyberbiz.co/v1/api_document)
- **User Name**：`apidemo`
- **Secret**：`apidemo`

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/APIWebhook串接01.png){ .screenshot }

API串接項目依照顏色簡單分類：

- 藍色【GET】：取得
- 綠色【POST】：建立
- 黃色【PUT】：更新
- 紅色【DELETE】：刪除

!!! tip "文件使用技巧"
    在文件中點選 **Model** 標籤，可查看各欄位的中文對照名稱，協助開發人員快速理解資料結構。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/APIWebhook串接06.png){ .screenshot }

### 如何用 token 串接 API 取得資料

串接 API 時，請在 Request Header 中帶入 Access Token。

- **API Endpoint**：`https://app-store-api.cyberbiz.io/`

使用 Bearer Token Access API

`Authorization: Bearer {access_token got from /admin/oauth/token}`

範例

```
curl https://app-store-api.cyberbiz.io/shop \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODkxMzI0ODksImV4cCI6MTY4OTEzOTY4OSwic2hvcF9pZCI6NzEwOSwic2NvcGVzIjoicHVibGljIHNob3BfYXBpIiwic2hvcF9kb21haW4iOiJkZW1vLmN5YmVyYml6LmNvIn0.VyW3B2wA1b6uhH9pDfbzRvPjOmSQD7VHy-IiRmnof9g" \
    -H "Accept: application/json"
```

```
curl https://app-store-api.cyberbiz.io/v1/customers \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODkxMzI0ODksImV4cCI6MTY4OTEzOTY4OSwic2hvcF9pZCI6NzEwOSwic2NvcGVzIjoicHVibGljIHNob3BfYXBpIiwic2hvcF9kb21haW4iOiJkZW1vLmN5YmVyYml6LmNvIn0.VyW3B2wA1b6uhH9pDfbzRvPjOmSQD7VHy-IiRmnof9g" \
    -H "Accept: application/json"
```

```
curl https://app-store-api.cyberbiz.io/v2/product_feeds \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODkxMzI0ODksImV4cCI6MTY4OTEzOTY4OSwic2hvcF9pZCI6NzEwOSwic2NvcGVzIjoicHVibGljIHNob3BfYXBpIiwic2hvcF9kb21haW4iOiJkZW1vLmN5YmVyYml6LmNvIn0.VyW3B2wA1b6uhH9pDfbzRvPjOmSQD7VHy-IiRmnof9g" \
    -H "Accept: application/json"
```

