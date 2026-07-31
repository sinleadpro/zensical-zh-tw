---
title: 訂單出貨流程
permalink: "https://help.cyberbiz.io/ec/orders/basics/order-fulfillment-flow/"
version: ""
author: Jase
reviewers: []
last_modified: 2026-07-13 12:02
description: ""
product:
  - EC
modules:
  - 訂單
activ: ""
paths: []
surfaces: []
ends: []
devices:
  - desktop
  - mobile
apis: []
type: tutorial
intents:
  - 執行單筆或批次訂單出貨
  - 下載並列印物流託運單與揀貨單
  - 了解宅配與超商取貨的交寄流程
  - 設定自訂物流與回填貨運單號
features:
  - 單筆出貨
  - 批次出貨
  - 託運單產出
  - 揀貨單與出貨明細
  - 自動呼叫司機 黑貓
  - 儲值中心
tnb: trunk
plans:
  - 專業
  - 進階
  - 高手
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
prerequisites:
  - 完成物流設定
  - 填寫公司物流地址
  - 確認儲值中心餘額充足_一般版
lang: zh-TW
sites: []
status: update
difficulty: ""
audiences: []
wp_url:
  - https://www.cyberbiz.io/support/?p=24829
  - https://www.cyberbiz.io/support/?p=952
products: [EC]
notes:
  - verify 宅配跟超取出貨流程
  - 篩選群組可以做出快結案訂單群組嗎
  - verify 批次出貨的確認條件步驟。
comments: ""
search:
  exclude: ""
icon: lucide/workflow
---

## 訂單出貨介紹 { #intro-fulfillment }

出貨是訂單成立、確認收款後的核心環節。在訂單列表，您可以勾選訂單後一次完成「產生託運單」與「更新配送狀態」兩件事，大幅縮短逐筆處理的時間。

依照配送方式不同，出貨主要分為三大類：

- **系統串接物流：** 黑貓、超商取貨、宅配通、新竹物流、順豐等，由系統自動向物流商取號並產生託運單。
- **自訂物流：** 您自行配送或與合作貨運出貨，手動標示出貨並填寫託運單號。
- **倉儲出貨：** 已串接[智慧倉儲(峰潮)](../../../wms/){ title="hide:" }的訂單，由倉庫端負責揀貨與出貨。

無論勾選一筆或多筆，新版訂單列表的出貨入口都相同，差別只在於您一次處理的訂單數量。

---

## 頁面功能總覽 { #overview-fulfillment }

| 出貨入口 | 位置 | 用途 |
| :-- | :-- | :-- |
| 單筆 / 批次出貨 | 訂單列表的「更多操作」 | 勾選訂單後選擇物流，產生託運單並將配送狀態改為「已出貨」 |
| 大量匯入自訂物流託運單號 | 訂單列表上方工具 | 以 Excel 一次匯入自訂物流的託運單號 |
| 逐項 / 部分出貨 | 訂單詳情頁的「出貨」區塊 | 同一筆訂單先寄出部分有現貨的商品 |

---

## 使用前提與限制 { #prerequisites-fulfillment }

正式出貨前，請先確認以下準備事項：

- [x] **Cyber幣 餘額：** 系統串接物流的運費由系統代收，出貨前請確認餘額充足[^billing]。
- [x] **寄件人地址：** 請至後台「金物流」左側選單下，各物流的託運單設定頁面填寫寄件人資訊（如黑貓託運單設定、新竹物流託運單設定等），否則產出的託運單寄件人資訊將不完整。
- [x] **印表機與耗材：** 建議使用雷射印表機，並備妥 A4 紙與託運單 / 超商標籤貼紙，以確保條碼清晰可判讀。

[^billing]: 一般版於下載託運單時即時預扣 Cyber幣；具備對帳中心的方案(PLUS版、企業版)則改為列入對帳單，於帳期結算。

---

## 計費規則 { #pricing-fulfillment }

系統串接物流(黑貓、超商取貨、宅配通、新竹物流、順豐等)的運費由系統代收，自訂物流則由您與物流商自行結算，不經過系統。

在出貨視窗中，您可以查看 **「運費收費表」** 了解各材積的費率。實際收取的金額會依您出貨給物流商的材積而定，並非固定金額。

- **一般版：** 下載託運單時即時預扣 Cyber幣。
- **具備對帳中心的方案：** 運費列入對帳單，於帳期結算，出貨當下不扣款。


---

## 操作步驟 { #operate-fulfillment }

新版訂單列表的出貨統一從訂單列表勾選訂單後操作。 **勾選一筆即為單筆出貨，勾選多筆即為批次出貨**，兩者流程相同。

!!! tip "技巧"
    批次出貨時，建議一次只勾選 **相同配送方式** 的訂單(例如全部為黑貓，或全部為 7-11)，系統才能用同一個動作完成整批出貨。

### 系統串接物流出貨 { #operate-fulfillment-carrier }

系統串接物流會自動向物流商取號並產生託運單。以下以黑貓為例，其他物流商(超商、宅配通、新竹物流、順豐等)操作方式基本相同：

1. **進入訂單列表：** 前往後台「訂單」>「所有訂單」。
2. **勾選訂單：** 在列表勾選欲出貨的訂單。
3. **選擇出貨動作：** 點擊上方 **「更多操作」**，選擇 **「下載黑貓託運單並將貨態改為『已出貨』」**。
4. **確認運費標準：** 在彈出視窗選擇運費計算標準，可查看 **「運費收費表」**，確認後點擊確認下載。
5. **下載並列印託運單：** 系統在背景產生 **託運單壓縮檔（ZIP）** 並自動下載，該批訂單的配送狀態同步更新為「已出貨」。解壓縮後即可列印託運單與明細（詳見 [託運單壓縮檔內容](#operate-fulfillment-zip)）。

<div class="grid cards" markdown>

- :lucide-cat: [**黑貓宅配**](../home-delivery/tcat-home-delivery-v2.md){ title="使用黑貓宅配出貨" }
- :lucide-bird: [**宅配通**](../home-delivery/pelican-shipping-v2.md){ title="使用宅配通出貨" }
- :lucide-truck: [**新竹物流**](../home-delivery/hct-shipping-v2.md){ title="使用新竹物流出貨" }
- :lucide-box: [**順豐速運**](../home-delivery/sf-express-shipping-v2.md){ title="使用順豐出貨" }

</div>

---

### 超商出貨 { #operate-fulfillment-cvs }

超商取貨屬於系統串接物流，出貨流程與[系統串接物流出貨](#operate-fulfillment-carrier)相同：勾選訂單 >「更多操作」> 選擇對應的超商出貨動作 > 產生託運單壓縮檔並將配送狀態改為「已出貨」。

<div class="grid cards" markdown>

- :lucide-store: [**超商 C2C 出貨教學**](../cvs-shipping/cvs-c2c-shipping.md){ title="操作超商店到店 C2C 出貨" }
- :lucide-factory: [**B2C 大宗寄倉**](../cvs-shipping/cvs-b2c-bulk-shipping.md){ title="使用超商大宗寄倉（B2C）出貨" }
- :lucide-snowflake: [**全家冷凍店到店**](../cvs-shipping/family-mart-frozen-c2c.md){ title="操作全家冷凍店到店 C2C 出貨" }

</div>

!!! warning "批次出貨請勾選同一種超商類型"
    超商的 B2C、C2C、冷鏈是不同的出貨動作。批次出貨時，請一次只勾選 **同一家超商、同一種類型** 的訂單（例如全部為「7-11 取貨付款」），系統才能用同一個動作完成整批出貨。

---

### 自訂物流出貨 { #operate-fulfillment-custom }

若使用未與系統串接的物流(自行配送或合作貨運)，改用自訂物流標示出貨：

1. **勾選訂單：** 在訂單列表勾選要出貨的訂單。
2. **開啟出貨視窗：** 點擊 **「更多操作」**，選擇自訂物流的出貨選項。
3. **選擇貨運公司：** 在 **「請選擇貨運公司」** 選單挑選物流商。
4. **確認出貨：** 可勾選 **「發送郵件通知顧客」**，確認後該訂單配送狀態轉為「已出貨」。

<div class="grid cards" markdown>

- :lucide-truck: [**自訂物流出貨教學**](../home-delivery/custom-logistic-shipping.md){ title="如何使用自訂物流出貨" }

</div>

訂單量大時，建議改用下方的「大量匯入自訂物流託運單號」一次帶入單號。

---

### 大量匯入自訂物流託運單號 { #operate-fulfillment-import }

有大量自訂物流訂單時，可用 Excel 一次匯入託運單號：

1. **開啟匯入工具：** 在訂單列表上方開啟 **「大量匯入自訂物流託運單號」**。
2. **下載並填寫範本：** 下載 Excel 範本，填入訂單編號、託運單號與物流商。
3. **上傳檔案：** 上傳後，匯入成功的訂單配送狀態會自動轉為「已出貨」並發信通知消費者[^import-partial]。

<div class="grid cards" markdown>

- :lucide-file-spreadsheet: [**大量匯入自訂物流單號教學**](../home-delivery/custom-logistic-shipping.md#excel-bulk-import){ title="如何使用自訂物流出貨" }

</div>

[^import-partial]: 大量匯入僅支援整筆全部出貨，不支援部分出貨。

---

### 逐項與部分出貨 { #operate-fulfillment-partial }

若一筆訂單只想先寄出部分有現貨的商品，需在訂單詳情頁的「出貨」區塊逐項勾選，而非在列表批次出貨。詳細流程請見 [訂單部分出貨](../home-delivery/partial-shipment-v2.md){ title="設定訂單部分出貨" }。

---

## 託運單壓縮檔 { #operate-fulfillment-zip }

系統串接物流的託運單並非單一 PDF，而是由系統在背景產生後， **打包成一個壓縮檔（ZIP）自動下載**。壓縮檔會以物流商命名（例如黑貓為 `ezcat`、7-11 為 `seven`、全家為 `family`），方便您一次取得整批出貨所需的文件。

解壓縮後，檔案內通常包含：

| 文件 | 用途 |
| :-- | :-- |
| 託運單 | 黏貼於包裹的物流標籤 / 條碼 |
| 出貨明細 | 隨包裹附上的出貨內容清單 |
| 揀貨單 | 倉庫揀貨備貨用 |
| 訂單明細 | 該批訂單的明細列印檔 |


??? example "壓縮檔內容範例"
    ![託運單壓縮檔內容](../../../assets/images/ec-訂單-所有訂單-託運單壓縮檔內容.png){ title="託運單壓縮檔內容" }

!!! info "為什麼是壓縮檔"
    批次出貨可能一次涵蓋多筆訂單與多份文件，系統統一打包成 ZIP，避免逐筆、逐份分開下載。下載完成後請先解壓縮，再列印所需的託運單與明細。

---

## 重要規範與限制 { #specs-fulfillment }

- **下載即標示已出貨：** 一旦下載系統串接物流的託運單，該批訂單的配送狀態會立即轉為「已出貨」，請確認商品已備妥再操作。
- **下載過程請勿離開頁面：** 託運單下載中若關閉或離開訂單頁面，會中斷下載，部分訂單仍可能已變更為「已出貨」而需要補印。
- **補印託運單：** 已出貨的訂單可在「更多操作」選擇 **「補印託運單」** 重新下載託運單 PDF。
- **離島超商與危險物品：** 配送商品到離島超商時，須遵守相關危險物品空運管理辦法。

---

## 後續操作 { #next-steps-fulfillment }

<div class="grid cards" markdown>

- :lucide-package-open:{ .lg }  
  [__訂單部分出貨__](../home-delivery/partial-shipment-v2.md){ title="設定訂單部分出貨" }  
  同一筆訂單先寄出有現貨的商品，剩餘的稍後再出。

</div>

---

## 常見問題 { #faq-fulfillment }

??? quote "下載沒反應 / 無法下載託運單"
    [](){ #faq-fulfillment-download-failed }
    若視窗出現「發生異常，無法產生 PDF 檔」或下載沒有反應，可依序檢查：

    - 確認瀏覽器未封鎖彈出視窗與檔案下載
    - 下載過程中請勿關閉或離開訂單頁面
    - 稍候片刻後再重新操作一次

??? quote "下載下來是壓縮檔，裡面有哪些文件"
    [](){ #faq-fulfillment-zip-contents }
    系統串接物流的託運單會打包成 ZIP 壓縮檔，內含託運單、出貨明細、揀貨單與訂單明細。請先解壓縮，再列印需要的文件。詳見 [託運單壓縮檔內容](#operate-fulfillment-zip)。

??? quote "運費怎麼計算？在哪裡查看"
    [](){ #faq-fulfillment-shipping-fee }
    出貨視窗中的「運費收費表」會列出各材積的費率。實際金額依出貨材積而定；一般版即時預扣 Cyber幣，具備對帳中心的方案則列入對帳單結算。

??? quote "已經下載過託運單，還能再列印嗎"
    [](){ #faq-fulfillment-redownload }
    可以。在「更多操作」選擇「補印託運單」，即可重新下載該訂單的託運單 PDF。

??? quote "訂單出貨後發生異常，可以重新出貨嗎"
    [](){ #faq-fulfillment-reship }
    無法重新出貨。若配送途中發生異常，除了 **超商門市關轉** 可修改配送門市外（見下一則），其餘情況只能請顧客重新下單。

??? quote "超商出貨後遇到「門市關轉」，怎麼處理"
    [](){ #faq-fulfillment-store-closed }
    依超商不同處理方式不同（詳見 [超商 C2C 門市關轉說明](../cvs-shipping/cvs-c2c-shipping.md#operate-cvs-c2c-exception-store-closed){ title="操作超商店到店 C2C 出貨" }）。

??? quote "同一位顧客有多筆訂單，可以合併出貨嗎"
    [](){ #faq-fulfillment-merge }
    依是否串接智慧倉儲(峰潮)而定：

    - **已串接智慧倉儲(峰潮)：** 不支援合併出貨。
    - **未串接：** 可手動操作合併， **僅限宅配且已收款的訂單**。

    以同一顧客的 A、B 兩張宅配訂單為例：

    1. **訂單 A** 依正常宅配出貨流程進行，揀貨時將 **訂單 B 的商品一起放入** 寄出。
    2. **訂單 B** 改以 **「自訂物流」** 標示出貨（實際不另外寄件，僅讓訂單狀態同步更新為已出貨）。

??? quote "顧客要自取商品（不經物流），要怎麼出貨"
    [](){ #faq-fulfillment-self-pickup }
    請改用 **「自訂物流」** 出貨流程。託運單號欄位可隨意填寫（系統不會追蹤自訂物流的貨態），配送狀態轉為 **「已出貨」** 即為最終貨態，並會列入對帳。詳見 [如何使用自訂物流出貨](../home-delivery/custom-logistic-shipping.md){ title="如何使用自訂物流出貨" }。

## 參考資料 { #reference-fulfillment }

- [配送狀態對照表](../references/fulfillment-statuses.md){ title="配送狀態對照表" }
- [超商物流部分出貨支援對照表](../references/cvs-partial-shipping-support.md){ title="超商物流部分出貨支援對照表" }
