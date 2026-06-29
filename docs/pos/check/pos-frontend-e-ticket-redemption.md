---
title: POS 前台核銷電子票券
description: 說明如何使用 CYBERBIZ POS 前台進行電子票券核銷、查詢票券訂單與核銷紀錄，包含掃碼與手動核銷流程。
created: 2026-06-01 15:36
last_modified: 2026-06-01 15:36
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
  - POS
modules: 
  - POS 前台
sites: 
  - TW
audiences: 
  - clerk
difficulty: beginner
tnb: branch
plans: 
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: 
  - TICKET
intents: 
  - 核銷電子票券
  - 查詢票券紀錄
  - POS 票券操作
features: 
  - 電子票券
  - POS 核銷
prerequisites: 
  - "需先完成電子票券商品設定"
related: 
  - "[[e-ticket-setup-guide]]"
  - "[[電子票券優惠設定]]"
tags: 
  - POS
  - 電子票券
  - 核銷
  - 門市管理
acoiv: operation
apis: []
devices: 
  - tablet
  - desktop
ui_components: 
  - POS 電子票券選單
  - 掃碼核銷彈窗
paths: 
  - POS 前台 > 電子票券
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=31866
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/ticket-check
hide: []
---

# POS 前台核銷電子票券
透過 POS 前台介面，店員可快速為顧客核銷電子票券，並即時查詢票券訂單狀態與歷史核銷紀錄，確保門市營運流暢。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }

!!! tip "應用情境"
    - **現場兌換**：顧客出示手機 QR Code，店員使用掃碼槍快速核銷。
    - **手動核銷**：若顧客手機螢幕損壞無法掃描，可透過輸入票券序號完成兌換。
    - **紀錄排查**：當顧客對兌換狀態有疑義時，於 POS 前台即時查詢核銷歷史。

## 使用須知

- **人員權限**：直接使用 POS 人員帳號即可操作，無需額外設定。
> EC 商家需先於後台建立 [電子票券門市店員權限](../../ec/e-ticket/index.md#門市與人員權限)。
- **前置設定**：核銷前請確保已完成電子票券商品的建立與上架。


## 核銷操作流程

### 1. 進入電子票券選單

於 POS 前台左側選單，點擊 **電子票券** 進入管理介面。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台核銷電子票券01.png){ .screenshot }

### 2. 搜尋票券

您可以透過 **進階搜尋**（如訂單編號、顧客電話）找到對應票券。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台核銷電子票券02.png){ .screenshot }

### 3. 執行核銷

點選 **核銷票券**，系統提供兩種核銷方式：

- **掃碼核銷**：使用掃碼槍直接掃描顧客的 QR Code。
- **手動核銷**：手動輸入票券序號後，點擊 **確認送出**。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台核銷電子票券03.png){ .screenshot }

### 4. 確認數量
確認預計核銷的數量無誤後，點擊 **確認** 即可完成核銷動作。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台核銷電子票券04.png){ .screenshot }



## 查詢票券紀錄

在電子票券頁面中，您可以切換不同頁籤進行管理：

### 票券訂單與詳細內容

在 **票券訂單** 頁籤中，點擊訂單編號可進入明細頁面。

- **已核銷**：查看該訂單已兌換的紀錄。
- **未核銷**：查看尚可兌換的票券，並可在此頁面直接執行核銷。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台核銷電子票券05.png){ .screenshot }

### 核銷紀錄查詢

在 **核銷紀錄** 頁籤中，可查看門市過往所有的核銷歷程，包含核銷時間、操作人員及票券名稱。

![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台核銷電子票券06.png){ .screenshot }

