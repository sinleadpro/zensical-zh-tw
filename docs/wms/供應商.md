---
title: 供應商
description: 在電商倉儲中建立供應商資料，能讓商家更清晰地管理貨物來源。透過將商品與供應商綁定，在後續建立進倉單或進行庫存盤點時，系統能自動對接廠商資訊。
created: 2026-03-16 00:00
last_modified: 2026-05-28 14:48
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結：權限設定
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 供應商
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 建立供應商帳號
  - 編輯廠商基本資訊
  - 綁定商品來源廠商
features:
  - 供應商管理
  - 商品來源追蹤
  - 進倉資料對接
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
related: []
tags:
  - 來源廠商
  - 商品管理
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 供應商列表頁面
  - 供應商編輯頁面
  - 商品編輯頁面
paths:
  - 供應商
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=39949
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/factory
hide: []
---

# 供應商
在電商倉儲中建立供應商資料，能讓商家更清晰地管理貨物來源。透過將商品與供應商綁定，在後續建立進倉單或進行庫存盤點時，系統能自動對接廠商資訊。
{ .subtitle }

![](../assets/images/WMS-後台-供應商-畫面總覽01.png){ .hero-page }

!!! tip "應用情境"
    - **進倉來源追蹤**：商家需要區分不同品牌商或代工廠的到貨，以便於進倉驗收。
    - **庫存責任歸屬**：透過綁定供應商，在盤點異常時能快速追溯貨物來源。
    - **進銷存報表分析**：後續可根據供應商維度，分析不同來源的進貨成本與銷速。


## 使用須知

- **唯一性要求**：建議為每位供應商建立唯一的代碼或名稱，避免後續進倉單對接錯誤真實。


## 操作流程

### 任務一：建立供應商資料

商家可根據配合的工廠、品牌商或貿易商建立基礎資料，作為後續業務往來的識別。

1. 登入電商倉儲後台，前往 **供應商**。
2. 點擊右上角 **新增供應商**（或直接進入新增頁面）。
3. 輸入 **供應商名稱**、**聯繫人**、**電話**、**Email** 與 **地址** 等資訊。
4. 確認資訊無誤後，點擊 **儲存**。
5. 建立完成後，該廠商將顯示在列表頁中。

![](../assets/images/WMS-後台-供應商-新增供應商01.png){ .screenshot }

### 任務二：將商品與供應商綁定

建立供應商後，必須手動將對應的商品與廠商進行關聯，以便系統在進倉時自動對接。


1. 前往 **商品 > 單一品項**，點擊欲設定的 **商品名稱** 進入編輯頁。
2. 在頁面中找到 **供應商** 欄位。
3. 在下拉選單中選擇對應的供應商名稱。
4. 點擊 **儲存** 完成綁定。

![](../assets/images/WMS-後台-商品-單一品項-商品綁定供應商01.png){ .screenshot }

### 任務三：編輯與維護廠商資訊

若供應商聯繫資訊異動，需及時更新以防進倉溝通落差。

1. 前往 **供應商**，在列表中選擇欲修改的 **廠商名稱**。
2. 點擊 :lucide-pencil: 操作。
3. 修正相關資訊（如電話、地址）後，點擊 **儲存**。
