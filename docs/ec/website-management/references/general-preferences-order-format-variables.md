---
title: 訂單編號格式變數對照表
description: 彙整訂單編號格式可用的變數，包含訂單流水號、隨機數、日期時間等變數的說明與使用限制。
created: 2026-06-26 10:00
last_modified: 2026-06-26 10:00
lang: zh-TW
type: reference
status: ""
version: ""
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags:
  - 訂單編號
  - 格式變數
  - 訂單設定
  - 一般設置
  - 參考資料
acoiv: ""
apis: []
devices:
  - desktop
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/references/general-preferences-order-format-variables/"
comments: false
search:
  exclude: false
icon: lucide/table
hide: []
---

# 訂單編號格式變數對照表 { #reference-general-preferences-order-format-variables }

在「一般設置」的「調整標準和格式」區塊，可使用下列變數自訂訂單編號的呈現方式。系統會在訂單成立時，把變數替換成實際內容。

| 變數 | 代表內容 | 說明 |
| :-- | :-- | :-- |
| `{{number}}` | 訂單流水號 | 由系統自動遞增的編號，例如 `1234`。此變數為必填 |
| `{{random}}` | 6 位隨機數 | 隨機產生的 6 位數字 |
| `{{random:N}}` | N 位隨機數 | 指定位數的隨機數，最多 9 位(例如 `{{random:4}}` 為 4 位) |
| `{{date}}` | 訂單成立日期 | 訂單成立當天的完整日期 |
| `{{year}}` | 年 | 訂單成立的年份 |
| `{{month}}` | 月 | 訂單成立的月份 |
| `{{today}}` | 日 | 訂單成立當天是幾號 |
| `{{hour}}` | 小時 | 訂單成立的小時 |
| `{{minute}}` | 分鐘 | 訂單成立的分鐘 |
| `{{second}}` | 秒鐘 | 訂單成立的秒數 |
| `{{timestamp}}` | 時間戳記 | 訂單成立當下的時間戳記 |

!!! note "註釋"
    * 格式中 **必須包含** `{{number}}`，且整體長度不可超過 64 個字元，否則無法儲存。
    * 系統預設格式為 `#{{number}}`，顯示效果例如 `#1234`。
    * 變更格式只會影響日後新成立的訂單，已成立訂單的編號不會改變。
