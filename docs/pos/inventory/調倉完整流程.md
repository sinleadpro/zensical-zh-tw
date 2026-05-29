---
title: 調倉完整流程
description: 由需求方發起申請，透過系統自動化產單與雙向確認機制，確保門市間調撥的庫存一致性。
created: 2026-04-09 18:00
last_modified: 2026-05-28 14:48
lang: zh-TW
type: guide
status: ""
version: 1.0.0
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 庫存
  - 所有POS門市
  - 全通路庫存管理
sites:
  - TW
audiences:
  - admin
  - clerk
difficulty: intermediate
tnb: branch
plans:
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 理解調倉機制
  - 執行跨店調撥
  - 追蹤調倉進度
features:
  - 調倉管理
  - 自動轉單
prerequisites:
  - [[調倉單]]
related: []
tags:
  - 調倉流程
  - 跨店調撥
  - 庫存移轉
  - POS_調倉
acoiv: operation
apis: []
devices:
  - desktop
ui_components:
  - 調倉單
  - 出倉單
  - 進倉單
paths:
  - POS 功能 > 所有 POS 商店 > 庫存管理 > 調倉單
layouts: []
wp_url: []
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/refresh-cw
hide: []
---

# 調倉完整流程
由需求方發起申請，透過系統自動化產單與雙向確認機制，確保門市間調撥的庫存一致性。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 進階 PLUS / 高手 PLUS / 企業
{ .doc-badge }


調倉是由 **需求方** 發起申請：

- **發起端(缺貨方)**：建立調倉單並待對方同意核准，由系統自動產出進倉單後接續執行後續收貨流程。
- **接收端(調撥方)**：核准接收到的調倉申請，由系統自動產出對應的出倉單作為扣庫與實體撥貨憑據。



```mermaid
sequenceDiagram

participant 缺貨方
participant 調撥方
Note over 缺貨方: 1. 建立調倉單
缺貨方->>調撥方: 系統通知庫存充足門市
Note over 調撥方: 2. 同意調倉
調撥方 ->>缺貨方: 缺貨方自動產生進倉單
Note over 缺貨方: 3. 確認進倉
缺貨方->>調撥方: 調撥方自動產生出倉單
Note over 調撥方: 4. 確認出倉
調撥方 ->>缺貨方: 實際配送
Note over 缺貨方: 5. 收貨清點
缺貨方<<->>調撥方: 系統調整雙邊庫存
Note over 缺貨方,調撥方: 6. 庫存異動完成
```



1. [[缺貨方] 建立調倉單]()
2. [[調撥方] 同意調倉]()
3. [[缺貨方] 確認進倉]()
4. [[調撥方] 確認出倉]()
5. [[缺貨方] 收貨清點]()
