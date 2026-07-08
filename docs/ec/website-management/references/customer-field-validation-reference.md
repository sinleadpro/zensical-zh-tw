---

title: 顧客欄位驗證模式對照表
description: 說明 Email 與手機欄位的三種驗證模式：選填、必填、必填且必須驗證。
created: 2026-05-27 16:04
last_modified: 2026-05-27 18:00
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
modules: []
sites:
  - TW
audiences:
  - admin
difficulty: beginner
tnb: trunk
plans:
  - 專業
  - 進階
  - 高手
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents:
  - 了解欄位驗證模式
  - 確認雙重驗證設定方式
features:
  - 選填
  - 必填
  - 必填且必須驗證
  - 雙重驗證
  - 資料欄位設定
prerequisites: []
related:
  - "[[setup-customer-email-phone-verification]]"
  - "[[customer-registration-modes-reference]]"
tags:
  - EC
  - 顧客註冊
  - 欄位驗證
  - 雙重驗證
  - 帳號安全
  - OTP
  - Reference
  - 對照表
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 資料欄位設定
  - 顧客驗證方式
paths:
  - 管理中心 > 顧客註冊設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/references/customer-field-validation-reference"
search:
  exclude: false
icon: lucide/table
hide: []
comments: false
---


「顧客註冊設定」頁面中，Email 與手機欄位可設定為以下三種狀態。實際的「Email + 手機雙重驗證」即是把兩個欄位都設為「必填且必須驗證」。

| 狀態 | 顧客必須填寫 | 系統會驗證 | 適用情境 |
|:--|:--:|:--:|:--|
| **選填** | ✗ | ✗ | 該欄位非必要資訊，顧客可自行決定是否提供 |
| **必填** | ✓ | ✗ | 需要顧客提供資料，但不查驗真偽 |
| **必填且必須驗證** | ✓ | ✓ | 要求顧客提供且通過 Email 連結 / 簡訊 OTP 驗證 |

!!! note "註釋"
    * 「**必填且必須驗證**」狀態在後台是兩段操作：先在 **「資料欄位設定」** 將欄位設為「必填」，再到 **「顧客驗證方式」** 開啟該欄位的驗證開關。
    * Email 預設為「必填」，手機預設為「選填」。
    * 至少需有 Email 或手機其中一項為必填，系統不允許兩者皆為選填。
    * 「電子郵件驗證」屬於免費功能；「手機驗證」會產生簡訊費用。


