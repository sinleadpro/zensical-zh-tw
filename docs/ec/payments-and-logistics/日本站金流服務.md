---
title: 日本站金流服務
description: 日本站提供在地化的金流解決方案，包含主流信用卡支付與日本特有的 Pay-Easy 便利服務，幫助商家順利進軍日本電商市場。
created: 2026-03-03 00:00
last_modified: 2026-05-28 14:48
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結：購物車相關設定、訂單相關設定、3D驗證門檻
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - JP
audiences:
  - admin
difficulty: intermediate
tnb: branch
plans:
  - Pro
  - Business
cyb_extensions: []
intents:
  - 開通日本信用卡支付
  - 設定_Pay-Easy_付款
features:
  - 日本站
  - 信用卡支付
  - Pay-Easy
prerequisites: []
related: []
tags:
  - Pay-Easy
acoiv: integration
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 金物流 > 金流設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=33442
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/lock
hide: []
---

# 日本站金流服務

日本站提供在地化的金流解決方案，包含主流信用卡支付與日本特有的 Pay-Easy 便利服務，幫助商家順利進軍日本電商市場。
{ .subtitle }


[:lucide-layers:{ title="適用方案" }](../../resources/conventions#適用方案) | 跨境電商（日本站）
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }

## 金流選項說明

| 付款方式 | 支援種類 | 手續費率 | 最低結帳門檻 |
| :--- | :--- | :--- | :--- |
| **信用卡** | 信用卡<br>簽帳金融卡 (VISA、MasterCard、JCB) | 3.6% (每筆) | 50 JPY |
| **Pay-Easy** | ATM<br>網路銀行轉帳 | 1.5% (每筆) | 無 |


- **帳務對帳**：相關金流手續費將列於每期對帳單。
- **最低結帳門檻**：系統設有預設之最低結帳門檻，商家無需手動配置；單筆訂單金額須達該門檻，結帳頁面始會顯示對應之付款選項。


## 步驟 1：信用卡支付設定

前往 **金物流 > 金流設定**，點擊 **CYBERBIZ PAYMENTS** 右側 :lucide-file-pen-line: **設定**。

![](../../assets/images/日本站-後台-金物流-金流設定-啟用金流01.png)

- **啟用功能**：開啟 **信用卡**。
- **3D 驗證門檻**：設定訂單金額超過多少時需進行 3D 驗證。
- **金流門檻設定**：設定可使用信用卡的 **最小金額** 與 **最大金額**。

![](../../assets/images/日本站-後台-金物流-金流設定-設定信用卡01.png)

## 步驟 2：Pay-Easy 支付設定

前往 **金物流 > 金流設定**，點擊 Pay-Easy 右側 :lucide-file-pen-line: **設定**。

- **啟用功能**：開啟 **Pay-Easy 支付**。
- **金流門檻設定**：設定可使用 Pay-Easy 的 **最小金額** 與 **最大金額**。

![](../../assets/images/日本站-後台-金物流-金流設定-設定Pay-easy01.png)