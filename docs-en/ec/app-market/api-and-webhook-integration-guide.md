---
title: "API and Webhook Integration Guide"
description: "Learn how to connect external systems such as ERP and CRM through API and webhook services for automated data sync and real-time notifications."
created: 2026-06-11 14:45
last_modified: 2026-10-07 16:20
lang: en-US
type: guide
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
  - merchant
  - developer
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: 
  - optional
cyb_extensions: 
  - APP MARKET
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
related:
  - ec/website-management/add-admin-set-permissions/
tags: 
  - API
  - Webhook
  - "System Integration"
  - Automation
acoiv: integration
apis: []
devices: 
  - desktop
ui_components: 
  - 我的擴充服務
  - 網站權限
paths:
  - 管理中心 > 網站權限
  - APP MARKET > 我的擴充服務
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7875
  - https://www.cyberbiz.io/helpcenter/?p=8544
  - https://www.cyberbiz.io/support/?p=20739
  - https://www.cyberbiz.io/support/?p=40162
permalink: "https://help.cyberbiz.io/ec/app-market/api-and-webhook-integration-guide/"
search:
  exclude: false
icon: lucide/code-2
hide: []
---

# API and Webhook Integration Guide
Learn how to connect external systems (such as ERP or CRM) through API and Webhook services for automated data sync and real-time notifications.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

!!! info "Plan Differences"
    - On PLUS plans, the "API and Webhook Integration Service" is an add-on module (choose 2 of 11). Make sure you have selected this module before using it. Enterprise includes it by default.


## Before You Start { #prerequisites-api-webhook }

- **Technical Requirements**: API and Webhook integration must be developed by engineers. CYBERBIZ provides only the interfaces and documentation, not coding or other technical implementation services.
- **Activation Request**: If the feature does not appear in your admin, contact customer service to request activation.
- **Rate Limits**:
    - **Request Rate**: Up to 5 requests per second.
    - **Data Size**: Each request is limited to 2 MB.
- **Permissions**: The operator needs the **Custom APPs** permission. Go to **Website Management > User Account Settings** to [set permissions](../website-management/add-admin-set-permissions/).
  ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook10.png){ .screenshot }



## Key Concepts { #overview-api-webhook }

### API { #overview-api-webhook-api }

An API is a two-way way to exchange information. Your system can send requests to the CYBERBIZ server to get (Get), create (Post), update (Put), or delete (Delete) system data.

### Webhook { #overview-api-webhook-webhook }

A Webhook works like a "subscription." When a specific event happens in CYBERBIZ (such as an order being placed or a member signing up), the system immediately pushes the latest data to the URL you specify (Endpoint URL), so you can automate follow-up actions.



## Setup Steps { #operate-api-webhook }

### Step 1: Create a Custom App { #operate-api-webhook-step-create }

Create an app in the admin to get the credentials needed for integration.

1. Log in to the CYBERBIZ admin and go to **APP MARKET > My Apps**.
2. Switch to the **Custom** tab and click **Create Custom APPs**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook01.png){ .screenshot }

3. Enter an **App Name** and configure the **API scope** (permission scope):
    - **read_**: Can only get data (Get).
    - **write_**: Can create, update, and delete data (Post, Put, Delete).
4. When you finish, the system generates an **APP Secret** and an **API Token**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook02.png){ .screenshot }

### Step 2: Set up Webhook Events { #operate-api-webhook-step-settings-webhook }

To receive real-time notifications, set up Webhook subscriptions.

1. On the app settings page, find the **Webhook Events** field.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook08.png){ .screenshot }

2. Select the event types to subscribe to (such as `orders/create`, `customers/update`).
3. In the **Endpoint URL** field, enter the URL that will receive the data.

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/自訂擴充服務-串接-API-Webhook09.png){ .screenshot }

4. Click **Save**. The system starts pushing the related event data.


## Developer Reference { #reference-api-webhook }

### API Documentation { #reference-api-webhook-api-docs }

Log in to the API documentation center with the test account to view each API's parameters and data formats.

- **Documentation URL**: [https://api-doc.cyberbiz.co/v1/api_document](https://api-doc.cyberbiz.co/v1/api_document)
- **User Name**: `apidemo`
- **Secret**: `apidemo`

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/APIWebhook串接01.png){ .screenshot }

API items are color-coded by type:

- Blue [GET]: Get
- Green [POST]: Create
- Yellow [PUT]: Update
- Red [DELETE]: Delete

!!! tip "Documentation Tip"
    Click the **Model** tab in the documentation to see the Chinese name of each field, which helps developers understand the data structure quickly.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/2021/09/APIWebhook串接06.png){ .screenshot }

### How to Use a Token to Get Data from the API { #reference-api-webhook-api-token }

When calling the API, include the Access Token in the Request Header.

- **API Endpoint**: `https://app-store-api.cyberbiz.io/`
- **API Token**: Go to **APP MARKET > My Apps**, select the custom app on the **Custom** tab, and copy the **API Token**.

    ![](../../assets/images/EC-後台-appmarket-我的擴充服務-取得api_token01.en.png){ .screenshot }


Example

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

