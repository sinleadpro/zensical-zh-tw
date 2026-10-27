---
title: "Store Settings"
description: "Set the store's display name, SMS sender name, and contact details so that the e-commerce warehouse system has the right basic data for logistics and messages."
created: 2026-03-25 20:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 設定
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 如何修改商店名稱
  - 設定簡訊顯示名稱
  - 配置WMS聯繫資訊
  - 國貿局英文公司名填寫
features:
  - "Store Settings"
  - 基礎資料管理
prerequisites: []
related: []
tags:
  - 商店設定
  - WMS
  - "Basic Information"
  - "SMS Settings"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 商店設定
  - 儲存按鈕
paths:
  - 設定 > 商店設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/store-settings/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Store Settings
Set the store's display name, SMS sender name, and contact details so that the e-commerce warehouse system has the right basic data for logistics and messages.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-設定-商店設定-畫面總覽01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Initial setup**: Fill in the store's basic details before you start using the e-commerce warehouse system.
    - **Contact changes**: Update the records right away when the store email or customer service phone number changes.
    - **Cross-border trade**: Enter the English company name registered with the Bureau of Foreign Trade (BOFT) for customs and international shipping.


## Before You Start { #prerequisites-store-settings }

- **Required fields**: Fields marked with a red asterisk `*` are needed for the system to work and cannot be left blank.
- **Length limit**: The SMS display name can be **10 characters** at most.


## Steps { #operate-store-settings }

1. Log in to the CYBERBIZ e-commerce warehouse admin panel and go to **設定 > 商店設定**.
2. Fill in each field as described below:

    | Field | Description | Required |
    | :--- | :--- | :--- |
    | **Store Name** | The store's display name inside the system | Required |
    | **SMS Display Name** | The sender name shown at the start of notification SMS messages | Required |
    | **BOFT Import/Export Company English Name** | The official English company name registered with the BOFT | Optional |
    | **Email** | The store's main contact email | Optional |
    | **Customer Service Phone** | The phone number for authorities or customers to contact | Optional |

3. Check the details, and then click **Save** at the bottom of the page.


## FAQ { #faq-store-settings }

??? quote "What Is the BOFT English Company Name For?"
    Fill in this field if your store ships across borders. The name is added to the related shipping labels and customs documents, so they match your government registration.


