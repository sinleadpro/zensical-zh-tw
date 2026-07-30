---
title: 帳號狀態與購買權限對照表
description: ""
created: 2026-06-08 17:46
last_modified: 2026-06-08 20:11
lang: zh-TW
type: reference
status: update
author: Jase
tags:
  - EC
  - 會員等級
  - 購買權限
  - 帳號狀態
  - 限購商品
  - 登入限制
  - Reference
  - 對照表
version: ""
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: ""
tnb: ""
plans:
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/marketing/references/purchase-limit-account-status/"
comments: ""
search:
  exclude: ""
icon: lucide/table
hide:
---

### 帳號狀態與購買權限對照表 { #reference-purchase-limit-account }

顧客能否購買限購群組內的商品，取決於是否登入以及會員的帳號狀態。一般(非限購)商品不受此限制。

| 顧客狀態 | 能否購買限購商品 | 結帳時的系統提示 |
| :-- | :-: | :-- |
| 未登入(訪客) | ❌ | 購物車包含限量商品，必須登入才可以購買 |
| 帳號已啟用 | ✅ | —(正常結帳) |
| 已列為警示帳號 | ✅ | —(正常結帳) |
| 帳號已禁用 | ❌ | 您的帳號已被停用，若有任何問題請聯繫客服。 |
| 帳號未啟用 | ❌ | 您未啟用帳號，不能購買限量商品。 |
| 帳號未驗證 | ❌ | 您未啟用帳號，不能購買限量商品。 |
| 已邀請會員啟用 | ❌ | 您未啟用帳號，不能購買限量商品。 |
| 啟用邀請被拒絕 | ❌ | 您未啟用帳號，不能購買限量商品。 |

!!! note "註釋"
    * 只有「帳號已啟用」與「已列為警示帳號」兩種狀態能購買限購商品；「警示帳號」雖被標記，但仍可正常購買。
    * 其餘狀態(含未登入訪客)皆無法購買限購商品，並會在結帳時看到上方對應提示。
    * 此限制僅適用於已加入限購群組的商品，一般商品不受影響。

