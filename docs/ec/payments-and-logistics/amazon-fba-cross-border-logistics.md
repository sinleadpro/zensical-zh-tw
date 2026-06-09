---
title: Amazon FBA 跨境物流
description: 透過 Amazon FBA 服務，您可以將官網訂單交由 Amazon 物流團隊代為包裝與配送。系統將自動拋轉訂單、同步貨態並更新庫存，實現跨境營運的自動化。
created: 2026-03-03 00:00
last_modified: 2026-05-28 14:48
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結：網站外觀、商品大量填補SKU教學
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 金物流
sites:
  - US
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
  - 安裝_FBA_插件
  - 授權_Amazon_帳號
  - 綁定商品_SKU
features:
  - Amazon FBA
prerequisites:
  - 需具備 Amazon Seller Central 賣家帳號
  - 商品需已入 Amazon FBA 倉庫
related: []
tags:
  - 跨境物流
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 第三方整合 > 我的擴充服務
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=20676
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/lock
hide: []
---

# Amazon FBA 跨境物流

透過 Amazon FBA 服務，您可以將官網訂單交由 Amazon 物流團隊代為包裝與配送。系統將自動拋轉訂單、同步貨態並更新庫存，實現跨境營運的自動化。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 跨境電商 (北美站 / 日本站 / 東南亞站)
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Pro / Business
{ .doc-badge }



## 使用須知

- **自動出貨**：官網訂單成立後，系統自動將資料拋轉至 Amazon 安排發貨。
- **庫存聯動**：一旦綁定，官網庫存將鎖定，無法手動修改，強制以 Amazon FBA 實際庫存為準。

## 啟用物流

### 步驟 1：安裝 FBA 擴充應用與帳號授權

#### 1. 安裝應用程式

1. 登入 CYBERBIZ 後台，前往 **第三方整合 > 我的擴充服務**。
2. 找到 **Fulfillment by Amazon (FBA)** 並點擊 **立即安裝**。
    ![](../../assets/images/北美站-後台-APPMARKET-我的擴充服務-啟用AmazonFBA01.png)

#### 2. 完成帳號授權

1. 點擊 **前往設定**。
    ![](../../assets/images/北美站-後台-APPMARKET-我的擴充服務-啟用AmazonFBA02.png)
2. 系統將導向 Amazon 授權頁面。
3. 輸入您的 Amazon Seller Central 帳號與密碼完成綁定。
    - 建議使用管理者帳號 (Admin User) 進行操作，以確保權限完整。

### 步驟 2：商品 SKU 綁定

若要讓 Amazon 正確識別官網訂單對應的商品，**CYBERBIZ 的商品 SKU 必須與 Amazon 的商品 SKU 完全一致**。

#### 1. 查詢 Amazon 端 SKU

1. 登入 [Amazon Seller Central](https://sellercentral.amazon.com/)。
    ![](../../assets/images/Amazon-後台-查看訂單資訊01.png)
2. 前往 **Inventory > Manage FBA Inventory**。
    ![](../../assets/images/Amazon-後台-查看Amazon商品SKU01.png)
3. 紀錄下該商品的 **Seller SKU**。
    ![](../../assets/images/Amazon-後台-查看Amazon商品SKU02.png)

#### 2. 在 CYBERBIZ 設定對應

1. 前往 **商品 > 所有商品**，進入目標商品的編輯頁。
2. 下滑至 **款式管理** 區塊。
3. 在 **SKU** 欄位填入與 Amazon 完全相同的字元（含大小寫、符號）。
4. 點擊儲存。

![](../../assets/images/EC-後台-商品-所有商品-編輯商品SKU01.png)

## 訂單監控與貨態追蹤

### 1. 在 Amazon 查看官網訂單

官網成立之 FBA 出貨訂單也會同步顯示在 Amazon 後台：

1. 登入 [Amazon Seller Central](https://sellercentral.amazon.com/)。
    ![](../../assets/images/Amazon-後台-查看訂單資訊01.png)
2. 前往 **Orders > Manage Orders**。
    ![](../../assets/images/Amazon-後台-查看訂單資訊02.png)
3. 在 Sales Channel 篩選器勾選 **Non-Amazon**，即可看到來自官網的訂單。
    ![](../../assets/images/Amazon-後台-查看訂單資訊03.png)

### 2. 貨態同步機制

- 當 Amazon 倉庫準備出貨時，官網訂單狀態會同步更新。
- 當 FBA 完成配送，官網配送狀態將自動轉為 **已出貨** 並正式入帳。



## CYBERBIZ 與 Amazon FBA 貨態對照表

| Amazon FBA 狀態 | CYBERBIZ 配送狀態 | 備註 |
| :--- | :--- | :--- |
| Receiving → Processing | 未出貨 | 消費者與商家可取消訂單 | 
| Processing | 準備出貨 | 訂單已拋轉，等待 Amazon 處理<br>進入此狀態後不得取消訂單 |
| COmplete | 已出貨 | Amazon 已寄出，系統自動入帳 |
| Cancelled | 已取消 | 訂單於 Amazon 端取消 |

