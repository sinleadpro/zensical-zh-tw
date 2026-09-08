---
title: 使用黑貓快速到店出貨
description: 批次下載黑貓快速到店託運單並將訂單貨態更新為已出貨。
created: 2026-05-18 15:26
last_modified: 2026-07-15 14:40
lang: zh-TW
type: guide
author: Jase
reviewers: []
notes:
  - fix link 黑貓取件設定頁 configure-ezcat-cvs-shipping-note-sender
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 批次下載黑貓快速到店託運單
  - 黑貓快速到店出貨
  - 補印託運單
features:
  - 黑貓快速到店
  - 批次出貨
  - 自動呼叫黑貓司機
  - 補印託運單
prerequisites:
  - 領取黑貓三聯空白託運單貼紙
  - 設定黑貓寄件人地址
  - 確認 CYBER 幣餘額
related:
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/orders/home-delivery/tcat-auto-call-driver-v2/
  - ec/payments-and-logistics/setup-print-tcat-quick-store-waybill-v2/
  - ec/website-management/points-deposits/
  - ec/orders/home-delivery/shipping-status-tooltip/
  - ec/orders/home-delivery/partial-shipment-v2/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
tags:
  - 黑貓快速到店
  - 7-11
  - 託運單
  - 物流出貨
  - 批次出貨
  - 超商物流
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 更多操作
  - 下載黑貓快速到店託運單
  - 補印託運單
paths:
  - 金物流 > 黑貓快速到店託運單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2678
  - https://www.cyberbiz.io/support/?p=8844
permalink: "https://help.cyberbiz.io/ec/orders/tcat-quick-store/tcat-quick-store-shipping/"
comments: false
search:
  exclude: false
icon: lucide/truck
hide: []
---

![下載黑貓快速到店常溫託運單](../../../assets/images/EC-訂單-所有訂單-下載黑貓快速到店託運單-hero.png){ title="下載黑貓快速到店常溫託運單" .hero-page }

## 黑貓快速到店出貨說明 { #intro-tcat-cvs }

「黑貓快速到店」是商家將商品委由黑貓物流送至消費者指定的 7-11 門市進行取貨的服務，依商品溫層分為常溫、冷藏、冷凍三種。本文將引導您如何在新版訂單列表中批次處理訂單、下載託運單，並將貨態變更為「已出貨」。

!!! info "其他黑貓服務"
    * 若顧客選擇宅配，請見 [使用黑貓宅配出貨](../home-delivery/tcat-home-delivery-v2.md){ title="使用黑貓宅配出貨" }。
    * 自動呼叫黑貓司機到府收件，請見 [自動呼叫黑貓司機取件](../home-delivery/tcat-auto-call-driver-v2.md){ title="自動呼叫黑貓司機取件" }。

## 使用前提與限制 { #prerequisites-tcat-cvs }

在執行黑貓快速到店出貨前，請確保您的系統設定、訂單狀態與硬體設備皆符合以下規範。

### 適用訂單狀態 { #prerequisites-tcat-cvs-order-status }

系統僅允許符合以下條件的訂單執行出貨：

- [x] **配送方式**： 結帳選用對應的「黑貓快速到店」。
- [x] **付款狀態**： 顯示為「已收到款項」或「貨到付款」。
- [x] **配送狀態**： 顯示為「未出貨」、「部分出貨」或「準備出貨中」。

---

### 配送規範 { #prerequisites-tcat-cvs-shipping-rules }

下列為黑貓快速到店的物流規範，請於包裝與出貨前確認：

| 項目 | 內容 |
| :-- | :-- |
| 包裹重量上限 | 單件 10 公斤 |
| 包裹材積上限 | 長 ＋ 寬 ＋ 高 不超過 105 公分 |
| 配送區域 | 僅支援台灣本島，不支援離島 |
| 取貨期限 | 商品抵達超商後，常溫可放置 7 日；冷藏／冷凍僅可放置 4 日。黑貓會於 **包裹到店第一日** 與 **退貨前一日** 各發 1 封簡訊通知消費者，共 2 封。 |
| 託運單時效 | 產出託運單後須於 7 日內聯繫黑貓完成收貨，逾期單號將失效 |
| [逾期未取](#tcat-cvs-overdue-pickup){ title="到店逾期未取" } | 包裹退回商家，黑貓將 **加收一次回程運費** |

!!! tip "冷藏／冷凍出貨的包裝建議"
    * **預冷時間** ：冷藏商品建議預冷 6 小時以上、冷凍商品建議預冷 12 小時以上，以維持溫層至門市取貨時。
    * **託運單防水** ：建議使用防水貼紙列印託運單，或將託運單放入透明防水袋後再黏貼於包裹外，避免因冷凝水使條碼模糊導致司機無法掃描。

---

### 系統限制 { #prerequisites-tcat-cvs-system-contraints }

- **溫層分流（不可混批）**： 常溫、冷藏、冷凍分屬不同託運單。批次勾選出貨時，不同溫層的訂單不可混合勾選處理。
- **功能開通限制**： 商店須開通對應溫層的功能。若要使用冷藏與冷凍服務，系統必須額外開通「商品綁溫層」功能。
- **與峰潮物流互斥**：若商店已串接峰潮物流，則無法使用黑貓快速到店功能，兩者擇一。

## 操作步驟 { #tcat-cvs-operate }


### 出貨前準備 { #prerequisites-tcat-cvs-checklist }

執行黑貓快速到店出貨前，請完成以下準備：

- [x] **黑貓寄件人地址**： 至「金物流」>「[黑貓快速到店託運單](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#configure-ezcat-cvs-shipping-note-sender-setup){ title="設定寄件人資訊" }」設定寄件人地址，否則託運單上的寄件人資訊將不完整。
- [x] **耗材與設備**： 已備妥「黑貓三聯空白託運單貼紙」（可致電黑貓客服 02-412-8888 取得），並建議使用雷射印表機列印，以確保條碼清晰。
- [x] **商品預冷（低溫包裹）**： 冷藏商品須預冷 6 小時以上；冷凍商品須預冷 12 小時以上。
- [x] **確認餘額**：一般版商家請至 [儲值中心查看 CYBER 幣餘額](../../website-management/points-deposits.md#cyber-coin-balance){ data-preview }，確認餘額充足；PLUS版 / 企業版商家無此限制。

--- 

### 批次下載黑貓快速到店託運單 { #operate-tcat-csv-shipping-note }

以下以常溫託運單為例，冷藏與冷凍的操作步驟相同，僅在下拉選單步驟選擇對應的下拉項目即可。

1. **進入訂單列表**：前往後台「訂單」>「所有訂單」。
2. **勾選欲出貨的訂單**：在列表左側的核取方塊勾選一筆或多筆訂單。請確認所勾選的訂單為同一個黑貓快速到店類型（常溫、冷藏或冷凍其中之一），不可混選不同溫層。
3. **展開「更多操作」並選擇下載動作** ：點擊列表上方的 **更多操作** 下拉選單，依勾選的訂單溫層擇一：
    * 下載黑貓快速到店常溫 / 冷藏 / 冷凍託運單並將貨態改為「已出貨」

    ![下載黑貓快速到店常溫託運單](../../../assets/images/EC-訂單-所有訂單-下載黑貓快速到店託運單.png){ title="下載黑貓快速到店常溫託運單" }

4. **檢視託運資訊**：系統將彈出「下載黑貓快速到店 - 常溫／冷凍／冷藏 託運單」視窗，視窗內會列出本次出貨的訂單清單，請確認無誤。
5. **（選用）設定自動呼叫司機取件**：若商店已開通「[呼叫黑貓](../home-delivery/tcat-auto-call-driver-v2.md){ title="自動呼叫黑貓司機取件" }」功能，視窗中會出現「是否自動呼叫黑貓司機取件」選項，選擇 **是** 後會展開以下三個欄位：

    * **是否需在取件前事先電話聯絡**：選「是」時，司機抵達前會撥打「[黑貓寄取件設定頁](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#configure-ezcat-cvs-shipping-note-sender-setup){ data-preview }」中的聯絡電話與您確認。
    * **是否需黑貓司機準備推車**：若包裹數量較多，可請司機自備推車。
    * **備註**：可填寫特殊收件指示(例如門禁、樓層)，上限 **100 字**。

    ??? warning "呼叫截止時間"
        每日 **16:30** 為[呼叫截止時間](../home-delivery/tcat-auto-call-driver-v2.md#tcat-auto-call-driver-deadtime){ data-preview }，超過後此選項將自動鎖定為「否」，當天無法再透過系統呼叫，需自行致電黑貓安排。

6. **確認寄件地址**：視窗中會顯示「寄件人地址」欄位，預設帶入該物流上一次使用的寄件地址（首次帶入[黑貓快速到店設定](../../payments-and-logistics/setup-print-tcat-quick-store-waybill-v2.md#configure-ezcat-cvs-shipping-note-sender-setup){ title="設定寄件人資訊" }中的地址），如需更改可於視窗內點擊 **「更改」** 按鈕編輯[^2]。

    ![更改寄件地址](../../../assets/images/EC-訂單-所有訂單-下載黑貓快速到店常溫託運單-更改地址.png){ title="更改寄件地址" }

7. **勾選並同意服務條款** ：確認已勾選「我已閱讀並同意 CYBERBIZ 物流串接服務條款 與 黑貓合約規範」（預設為勾選狀態），按鈕「確認」才會啟用。
8. **確認下載**：點擊 **確認** ，系統會自動下載[^1] [託運單 ZIP 壓縮檔](#tcat-cvs-zip-contents){ title="託運單 ZIP 內容物" }。
9. **確認貨態已變更**：操作完成後，被勾選訂單的配送狀態會自動轉為 **已出貨** 。(詳見 [確認貨態變更](#tcat-cvs-verify-status){ title="確認貨態變更" })


[^1]: 若沒有正常下載，請確認瀏覽器是否阻擋了彈跳視窗或廣告，允許本站彈跳視窗後重新點擊下載。更多疑難排解參考 [常見問題：無法下載托運單](#faq-tcat-cvs-download-no-response)
[^2]: 修改後會同步更新黑貓快速到店設定頁面地址，不同物流間及公司物流地址互不影響。

---

### 呼叫黑貓司機取件 { #tcat-cvs-call-driver-pickup }

下載託運單後，需聯繫黑貓司機到貨取件:

* **電話呼叫**：撥打黑貓客服專線 (02-412-8888) 安排取件。
* **從後台直接呼叫**：若已開通 [呼叫黑貓功能](../home-delivery/tcat-auto-call-driver-v2.md){ title="自動呼叫黑貓司機取件" }，可在下載託運單時於彈出視窗內預約司機取件。

---

### 確認貨態變更 { #tcat-cvs-verify-status }

成功下載託運單後，可在兩個地方確認貨態：

- **訂單列表頁**：配送狀態欄位顯示 **已出貨**
- **訂單詳情頁**：狀態顯示為 [已出貨(待物流收件)](../home-delivery/shipping-status-tooltip.md#shipping-status-text-type){ data-preview }，表示託運單已產生但黑貓尚未收件

若貨態未更新，請檢查：

* 是否實際完成下載(瀏覽器是否阻擋了下載對話框)
* 是否所有勾選的訂單配送方式都符合「黑貓快速到店」

---

### 地址錯誤排除 { #tcat-cvs-address-error }

下載託運單時若出現「寄件人資訊不完整提示」，代表黑貓寄件地址未設定或不完整：

1. 前往 **金物流 > 黑貓快速到店託運單**，確認「黑貓快速到店設定」區塊內的 **寄件地址** 完整填寫(含縣市、區域)，儲存後系統會自動向黑貓查詢寄件人區碼。
2. 儲存後重新執行下載。

??? info "關於寄件地址的注意事項"
    * **地址來源**：寄件地址取自 **金物流 > 黑貓快速到店託運單** 中「黑貓快速到店設定」的地址。
    * **修改方式**：可在下載託運單的彈窗中點擊 **「更改」** 直接編輯，修改後會同步更新至黑貓快速到店設定頁面。

---

### 到店逾期未取 { #tcat-cvs-overdue-pickup }

包裹送達超商後，消費者有取貨期限：

* **常溫**：7 日內
* **冷藏 / 冷凍**：4 日內

黑貓會發送 **2 封簡訊** 提醒消費者：

| 簡訊 | 發送時機 |
| :-- | :-- |
| 第 1 封 | 包裹到店當日 |
| 第 2 封 | 退貨前 1 日(常溫第 6 日、冷藏/冷凍第 3 日) |

## 後續操作 { #nextstep-tcat-cvs }

<div class="grid cards" markdown>

<!-- - :lucide-printer:{ .lg }  
  [__補印託運單__](../../payments-and-logistics/reprint-waybills.md){ title="補印與加印託運單" }  
  若須重新列印（例如標籤受潮、列印不清），回到訂單列表勾選同筆訂單，於「更多操作」選擇補印託運單。 -->

- :lucide-truck:{ .lg }  
  [__自動呼叫司機__](../home-delivery/tcat-auto-call-driver-v2.md){ title="自動呼叫黑貓司機取件" }  
  開通「呼叫黑貓」功能者可於列印託運單時自動呼叫司機。

- :lucide-package-check:{ .lg }  
  [__部分出貨__](../home-delivery/partial-shipment-v2.md){ title="處理訂單部分出貨" }  
  若一筆訂單中只想先寄出部分商品，可改從訂單詳情頁勾選指定品項。

- :lucide-copy-plus:{ .lg }  
  [__加印託運單__](../../payments-and-logistics/setup-print-tcat-waybill-v2.md){ title="設定與加印黑貓託運單" }  
  若一筆訂單因商品多需拆分為多箱寄出，每箱需各自一張託運單。

</div>

## 常見問題 { #faq-tcat-cvs }

??? quote "下載沒反應 / 無法下載託運單" 
    [](){ #faq-tcat-cvs-download-no-response }

    通常為以下原因之一：

    * **瀏覽器阻擋彈跳視窗**：請檢查瀏覽器是否阻擋了彈跳視窗或廣告，允許本站彈跳視窗後重新點擊下載。
    * **CYBER 幣不足(一般版商家)**：請至 [儲值中心](../../website-management/points-deposits.md){ data-preview } 儲值。
    * **黑貓快速到店寄件地址未設定**：至 **金物流 > 黑貓快速到店託運單** 的「黑貓快速到店設定」區塊完成寄件地址填寫。
    * **未勾選同意條款**：確認彈出視窗下方「我已閱讀並同意 CYBERBIZ 物流串接服務條款 與 黑貓合約規範」已勾選。


??? quote "「更多操作」下拉中找不到「下載黑貓快速到店⋯」選項？"
    [](){ #faq-tcat-cvs-action-missing }

    通常為以下原因之一：

    * 勾選的訂單在結帳時並未選擇黑貓快速到店配送，或混合勾選了不同溫層／不同物流的訂單。請確保本批訂單為同一種黑貓快速到店類型。
    * 訂單貨態不在「未出貨」、「部分出貨」、「準備出貨中」範圍內（例如已退款、已取消），無法執行出貨。

??? quote "「是否自動呼叫黑貓司機取件」的選項是灰色／無法勾選？"
    [](){ #faq-tcat-cvs-call-disabled }

    可能為以下情況：

    * 目前時間已超過當日 **16:30** ，自動呼叫功能會自動關閉並停留在「否」，請於次日再使用，或自行致電黑貓安排當日取件。
    * 商店未開通「呼叫黑貓」功能，整個自動呼叫區塊不會顯示，請聯繫業務窗口或致電黑貓客服取件。

??? quote "付款狀態還是「等待付款」可以先下載託運單嗎？"
    [](){ #faq-tcat-cvs-payment-status }

    不行。出貨動作要求訂單付款狀態為「已收到款項」或「貨到付款」，且貨態為「未出貨」、「部分出貨」或「準備出貨中」。若付款尚未確認，請先處理收款後再執行出貨。

??? quote "託運單列印壞掉或遺失，可以重印嗎？"
    [](){ #faq-tcat-cvs-redownload }

    可以。請在訂單列表勾選該筆訂單，於「更多操作」選擇 **補印託運單** ，系統會以原託運單號重新產出檔案，不會重複建立單號。

??? quote "同一批訂單可以混合常溫與冷凍一起出貨嗎？"
    [](){ #faq-tcat-cvs-mixed-temperature }

    不行。常溫、冷藏、冷凍為三個獨立的下載動作，且訂單在結帳時即已綁定溫層。請依溫層分批勾選與出貨，避免出貨後因溫層不符影響商品品質。

??? quote "冷藏或冷凍商品出貨時有什麼注意事項？"

    冷藏與冷凍商品出貨時請注意以下事項：

    - **預冷時間**：冷藏商品建議預冷 6 小時以上，冷凍商品建議預冷 12 小時以上，以維持溫層至門市取貨時
    - **託運單防水**：建議使用防水貼紙列印託運單，或將託運單放入透明防水袋後再黏貼於包裹表面，避免因冷凝水使條碼模糊導致司機無法掃描

??? quote "一般版商家 CYBER 幣餘額不足時可以下載託運單嗎？"

    不行。下載託運單時系統會即時從 CYBER 幣餘額扣款，餘額不足時下載會失敗。請先至 [儲值中心](../../website-management/points-deposits.md){ data-preview } 儲值後再重新操作。

### 託運單 ZIP 內容物 { #tcat-cvs-zip-contents }

下載完成後，zip 內包含四份 PDF，分別供不同流程使用：

| 檔案 | 用途 | 收件對象 |
|---|---|---|
| **託運單** | 黑貓收件、配送依據；以黑貓三聯空白託運單貼紙列印後黏貼於包裹表面 | 司機 |
| **出貨明細** | 出貨包裹內附的明細單，含品項與數量 | 消費者(隨包裹) |
| **揀貨單** | 倉庫揀貨用的清單，依品項彙整方便揀料 | 內部倉務人員 |
| **訂單明細** | 訂單完整資訊，含金額、付款方式、消費者資料 | 內部存檔 / 客服 |


