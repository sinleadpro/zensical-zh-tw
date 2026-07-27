---
title: CYBERBIZ EXPRESS 日到台跨境宅配
description: 一站式日本跨境直送台灣物流服務，涵蓋開通設定、跨境商品報關資訊填寫及訂單出貨流程。
created: 2026-03-03 00:00
last_modified: 2026-07-27 14:30
lang: zh-TW
type: tutorial
status: ""
version: 1.1.2
author: Ann
reviewers: []
notes:
  - 跨境GL版本徽章
  - 內部連結：購物車相關設定、訂單相關設定
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - APP MARKET
sites:
  - JP
audiences:
  - admin
difficulty: intermediate
tnb: branch
plans:
  - global_advanced
cyb_extensions:
  - EXPRESS
intents:
  - 設定跨境出貨地址
  - 填寫跨境商品資訊
  - 建立跨境託運單
features:
  - 日到台跨境物流
  - EZWAY_報關
  - 跨境運費自動計算
prerequisites:
  - 需向開店顧問團隊申請開通服務
  - 需具備日本出貨地址 (倉庫或商家處)
related: []
tags:
  - 跨境電商
  - EZWAY 報關
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - App Market > 我的擴充服務 > CYBERBIZ EXPRESS
  - 商品 > 所有商品
  - 訂單 > 所有訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=51481
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/lock
hide: []
---

# 使用 CYBERBIZ EXPRESS 日到台跨境宅配

CYBERBIZ EXPRESS 是專為日台電商設計的一站式跨境物流服務。您可以輕鬆將日本製產品送達台灣消費者手中，系統並自動整合 EZWAY 報關流程與運費自動核帳。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 跨境電商 (日到台)
{ .doc-badge }

## 使用須知

- **配送溫層**：僅支援 **常溫** 配送。
- **付款限制**：僅支援 **貨到不付款**（需先完成線上支付）。
- **交貨條件**：採 **DDU (未完稅交貨)** 模式，進口稅金由台灣收件人支付。
- **收貨方式**：支援 **上門取件** 與 **商家自行寄至日本倉庫** 兩種方式。實際運費會依合作方案與取件方式不同而有所差異。
- **運費計費**：系統會以商品重量與材積，於建立託運單時自動計算並預扣 CYBER 幣；每月5號會依實際收取運費，多退少補 CYBER幣。

## 跨境物流運送流程

日到台宅配包含以下五個關鍵階段，商家須配合完成報關文件寄送：

1. **收件入庫**：物流商前往商家地點/日本倉庫取件。商家須預先將提單清單與發票寄至指定信箱 `manifest_express@cyberbiz.io`。
2. **理貨集運**：依海關規定，須所有消費者完成 EZWAY 申報相符，整袋貨物方能放行。
3. **航空轉運**：依每週航班排程配送，集運時間約需 1~2 個工作日。

    >  實際的最終配送時程，則將以該週確認的航班時間為準

4. **海關報關**：包裹進入報關階段時，消費者需 **下載 EZWAY App**，[完成 **申報相符** 回報](https://web.customs.gov.tw/singlehtml/3150?cntId=cus1_3150_3150_1471)。

    !!! warning "若消費者一直沒有在 EZWAY 申報？"
        - **滯報費**：超過 15 天未申報，海關將自第 16 天起收取每日 **NT200元** 滯報費。
        - **變賣處置**：累積滿 20 日仍未申報，[海關有權變賣貨物](https://web.customs.gov.tw/singlehtml/1207?cntId=cus1_93451_1207)。商家應主動提醒消費者完成申報。

5. **本地配送**：包裹抵台後由本地物流送達消費者手中。

    !!! warning "關稅支付提醒"
        單筆包裹價值若超過 NT 2000 元，海關可能課徵關稅與相關稅費；稅金將由物流商派送包裹時，向收件人收取。


## 申請啟用

1. 聯繫您的開店顧問申請開通。
2. 前往 **APP MARKET > 我的擴充服務 > CYBERBIZ EXPRESS**。

    ![](../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-開始設定01.png){ .screenshot }

3. 勾選同意 **跨境運送服務契約**。

    ![](../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-開始設定02.png){ .screenshot }

4. 選擇託運單列印方式。

5. 填寫 **日本出貨地址**。
    - **建議以中文填寫**，以利台灣海關審核。
    - 若未填寫此地址，系統將無法產出報關發票與提單清單。

    ![](../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-開始設定03.png){ .screenshot }


## 跨境商品資訊設定

欲使用此服務，所有參與跨境銷售的商品必須補齊以下報關資訊：

| 欄位名稱 | 欄位資訊 | 填寫語言 | 填寫規則 |
| ------- | -------- | ------- | ------- |
| **GTIN(Barcode)** | JANCODE | 日文 | 必填 |
| **Item Name(Local)** | 商品名稱 | 日文 | 必填 |
| **Ingredients** | 成分 | 日文 | 必填 |
| **Category** | 品目說明 | 日文 | 必填 |
| **Country of Origin** | 原產國 | 日文 | 必填 |
| **Item Name(English ONLY)** | 商品名稱 | 英文(標點符號須為半形) | EXPRESS 宅配：無須填寫<br>EMS 物流：必填 | 


### 編輯方式

=== "單筆編輯"

    前往 **商品 > 所有商品** ，進入明細頁填寫。

    ![](../../assets/images/EC-後台-商品-所有商品-日到台站台報關用商品欄位01.png){ .screenshot }

=== "批次編輯"

    1. [匯出商品 Excel](../../products/bulk-operations/excel-import-products/#下載-excel-範本或匯出商品)。
    2. 填寫報關用對應欄位，儲存檔案。
    3. [匯入商品 Excel](../../products/bulk-operations/excel-import-products/#匯入-excel-檔案)，完成批次編輯。

    ![](../../assets/images/EC-後台-商品-所有商品-日到台站台報關用商品欄位02.png){ .screenshot }

## 訂單出貨操作

### 建立與列印託運單

1. 前往 **訂單 > 所有訂單**。
2. 勾選欲出貨訂單。
    - `付款狀態`須為 `已收到款項`
    - `配送壯派`須為 `未出貨`/`準備出貨`/`部分出貨`
    - `退貨狀態`須為 `不需退貨`
3. 點選 **更多操作 > 建立託運單**。

    ![](../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單01.png){ .screenshot }

4. 於彈出視窗中指定所需的配送管道。

    - **文件預覽與列印**：系統將根據您的勾選項目（如下列清單）開啟網頁預覽，確認無誤後即可列印。
        - **託運單**
        - **揀貨單**
        - **訂單/出貨明細**
    - **批次下載支援**：系統支援同步下載上述所有文件。
    - **自動排序邏輯**：執行批次建立時，系統會產出包含所有訂單明細的單一 PDF 檔案，並自動依「訂單編號」由小至大進行排序。
    - **即時資料校驗**：系統會針對訂單中商品進行欄位檢查，若缺少重量、跨境商品必填欄位，請先補填後再操作出貨。

    ![](../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單02.png){ .small-image }

5. 建立成功後，訂單狀態將自動轉為 `已出貨`。

### 寄送報關文件

通知物流商取件前，請務必完成以下動作：

1. 下載並列印 **提單清單** 與 **報關發票**。

    - 為方便報關行報關，提單清單中的商品金額，會採固定匯率自動轉換為台幣。

        > 日幣：台幣=5：1

    ![](../../assets/images/EC-後台-訂單-所有訂單-建立EXPRESS託運單03.png){ .screenshot }

2. 通知物流商前往收件前，請將當天出貨訂單對應的提單清單與報關發票檔案，以 E-mail 寄送至 `manifest_express@cyberbiz.io`。

    - **郵件主旨**：【跨境通-商家名稱】YYYY/MM/DD 出貨資料。

## 補印託運單

在 **訂單列表** 勾選狀態為 `已出貨` 的訂單，選擇 **補印託運單** 即可重新下載相關文件。

![](../../assets/images/EC-後台-訂單-所有訂單-補印EXPRESS託運單01.png){ .screenshot }

## 運費計費與對帳

- **預扣機制**：建立託運單時，系統依重量與材積預扣 CYBER 幣。
- **多退少補**：每月 5 號依物流商實際收取的運費進行結算，多退少補至您的 CYBER 幣帳戶。
- **費用對帳查詢**：前往 **APP MARKET > 我的擴充服務 > CYBERBIZ EXPRESS**，進入 **物流單號** 頁籤，即可核對各筆託運單之預定收取與實際收取運費。

    ![](../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-查看託運單運費01.png){ .screenshot }

## 貨態追蹤

=== "商家端"

    1. 前往 **前往APP MARKET > 我的擴充服務 > CYBERBIZ EXPRESS**。
    2. 進入 **物流單號** 頁籤，點擊單號連結。
    3. 進入 [CYBERBIZ EXPRESS 貨態查詢頁面](https://www.cyberbiz.express/zh-TW) 查詢。
        - 單次可查詢至多10筆託運單。
        - 系統支援中/英/日語言。


=== "消費者端"

    1. 登入 **會員中心**，在 **訂單明細** 頁點擊 **託運單號**。

        ![](../../assets/images/EC-前台-訂單查詢-訂單明細-查看託運單號01.png){ .screenshot }

    2. 進入 [CYBERBIZ EXPRESS 貨態查詢頁面](https://www.cyberbiz.express/zh-TW)，輸入託運單號。
        - 單次可查詢至多10筆託運單。
        - 系統支援中/英/日語言。

        ![](../../assets/images/EC-後台-APPMARKET-我的擴充服務-CYBERBIZEXPRESS-查看託運單配送狀態02.png){ .screenshot }

    