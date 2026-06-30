---
title: 管理系統代開消費者發票
description: 了解 CYBERBIZ 代開消費者發票服務，包含發票開立方式、顧客與商家查詢流程，以及發票資訊修改的申請期限與費用說明。
created: 2026-06-10 16:30
last_modified: 2026-06-30 08:02
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
  - 管理中心
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: branch
plans:
  - 企業
cyb_extensions: []
intents: 
  - 了解系統代開發票服務
  - 查詢電子發票資訊
  - 修改發票統編資訊
features: 
  - 系統代開消費者發票
  - 電子發票載具
  - 發票修改申請
prerequisites: 
  - "需為企業版方案商家"
related: []
tags: 
  - 電子發票
  - 代開發票
  - 統編修改
  - 發票查詢
acoiv: operation
apis: []
devices: 
  - desktop
  - mobile
ui_components: 
  - 訂單詳情
  - 會員中心
  - 簡訊通知樣板
paths: 
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=2319
  - https://www.cyberbiz.io/support/?p=5769
permalink: https://help.cyberbiz.io/ec/website-management/manage-system-issued-consumer-invoices
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---

# 管理系統代開消費者發票
了解 CYBERBIZ 代開消費者發票服務，包含發票開立方式、顧客與商家查詢流程，以及發票資訊修改的申請期限與費用說明。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 企業
{ .doc-badge }

!!! warning "適用對象限制"
    此功能僅適用於 **企業版方案** 且 **由 CYBERBIZ 代開消費者發票** 的商家。若您的企業版站台「自行開立消費者發票」，則不適用本文件之設定指引。


## 使用須知

- **開立形式**：統一以 **電子發票** 形式開立，不提供紙本發票。
- **修改限制**：發票一經開立，除資訊錯誤需更正外，不得要求更換載具類型或改開個人/公司戶。

## 發票開立方式

顧客於結帳時可選擇以下發票類型，系統將依付款狀態自動開立：

1. **會員載具 (個人)**

    - **開立方式**：開立雲端發票，系統寄送 Email 通知，不提供紙本或電子檔案
    - **統一發票使用辦法**：
        - 個人發票一經開立，無法更改或改開公司戶發票。
        - 若需開立統編，請改選擇開立 **公司用(統編)** 類型發票。
        - 請務必確認選用之電子發票載具類型是否正確，一經開立不得要求更改。

2. **公司用 (統編)**

    - **開立方式**：以 PDF 格式寄送電子發票至顧客電子信箱。
    - **統一發票使用辦法**：
        - 公司戶發票一經開立，無法更改為個人發票。
        - 請務必確認輸入之公司統編是否正確，一經開立不得要求更改。

3. **手機載具**

    - **開立方式**：顧客需輸入手機載具代碼（如 `/ABC1234`）。
    - **統一發票使用辦法**：務必確認選用之電子發票載具代碼是否正確，一經開立不得要求更改。

4. **自然人憑證**

    - **開立方式**：顧客需輸入自然人憑證號碼。
    - **統一發票使用辦法**：務必確認選用之電子發票載具代碼是否正確，一經開立不得要求更改。

5. **捐贈發票**

    - **開立方式**：顧客需輸入捐贈碼。若號碼錯誤，系統將轉贈預設社福機構。
    - **統一發票使用辦法**：務必確認選用之電子發票載具代碼是否正確，一經開立不得要求更改。


## 發票開立時機

系統會根據訂單的 **付款狀態**，自動執行相對應的發票作業。當消費者 **完成付款** 後，系統即自動開立發票。

具體的處理邏輯如下：

| 付款狀態 | 發票執行動作 | 系統處理說明 |
| :--- | :--- | :--- |
| 已收到款項 | **開立發票** | 系統確認收到款項後，將自動開立電子發票 |
| 付款失敗 | **不予開立** | 訂單交易未成功，系統不會產生發票資訊 |
| 已退款 | **開立折讓** | 執行退款作業後，系統將自動產生折讓單 |



## 查詢發票資訊

### 顧客端查詢

=== "前台查詢"

    顧客登入會員後，前往 **訂單查詢 > 查看詳情**，即可在發票資訊欄位查看發票號碼。

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊07.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊08.png){ .screenshot }

    </div>

  
=== "信件查詢"

    系統開立發票後會寄送通知信，顧客可點選信中 **發票明細** 連結，查看並下載電子發票。

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊12.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊13.png){ .screenshot }

    </div>


### 商家端查詢

1. 登入 CYBERBIZ 管理後台，前往 **訂單 > 所有訂單**。
2. 在訂單清單中點擊 **發票號碼** 連結，即可查看發票詳情。

![](https://www.cyberbiz.io/support/wp-content/uploads/發票相關資訊16.png){ .screenshot }


## 修改發票資訊

若顧客需補打統編或修正發票資訊，商家需向 CYBERBIZ 提出申請，由平台委託加值中心（星益欣）進行異動。

### 申請流程與期限

- **申請方式**：請進線客服並提供需修改的訂單與發票資訊。
- **申請期限**：務必於 **發票開立月的次月 7 日前**（遇假日請提前）提出申請。

    > 範例：7 月份發票，最晚需於 8/7 前申請。

- **處理時間**：約 3-5 個工作天（不含假日）。

### 相關費用

- **人工作業處理費**：每筆酌收 **100 元 (含稅)**。


## 發票中獎通知

系統於單月 25 日開獎後，將自動比對中獎發票並發送通知給購買人。

### 通知發送邏輯

系統將根據發票內留存的聯絡資訊，決定通知管道與發送單位：

| **會員資訊** | **通知管道** | **發送單位** |
| :--- | :--- | :--- |
| 留有 Email | **電子郵件** | 星益欣 |
| 僅有手機號碼 | **簡訊** | CYBERBIZ |

!!! tip "簡訊通知設定"
    若您的商店設定為「手機必填、Email 選填」，請前往 **訊息推播 > 簡訊通知樣板**，開啟 **發票開立通知**。系統將於中獎時發送簡訊通知顧客。
    
    > **簡訊費用**：每封 NT$ 1 元（限 70 字元）。

### 領獎與列印方式

顧客收到通知後，可持中獎資訊至指定超商多媒體機台列印紙本發票進行兌獎：

- **星益欣發票**：前往 **全家便利商店 (FamilyMart)** 使用 **FamiPort** 機台列印。
- **綠界科技發票**：前往 **7-11 統一超商** 使用 **ibon** 機台列印。

> 超商 Ibon列印中獎發票的手續費會由 CYBERBIZ 負擔。

### 注意事項

- **無法補印**：依 [國稅局規定](https://www.etax.nat.gov.tw/etwmain/tax-info/innotative-tax-e-reference/startup/invoice/r5wmN0W)，中獎發票紙本若遺失或毀損，系統與超商機台皆無法提供補印服務。
- **資訊準確性**：若因顧客留存之聯絡資訊錯誤導致無法通知，系統將不另行通知、亦無法協助後續處理。


## 常見問題

??? quote "顧客如何索取紙本發票？"
    系統僅開立電子發票，恕不提供紙本。



