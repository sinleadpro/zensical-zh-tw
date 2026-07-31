---
title: 使用宅配通出貨
description: 使用宅配通出貨。包含批次下載託運單、單筆與部分出貨、補印託運單等操作，以及運費計價規則與常見問題。
created: 2026-05-19 21:30
last_modified: 2026-07-09 14:47
lang: zh-TW
type: guide
status: update
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
  - merchant
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
  - 宅配通出貨操作
  - 批次下載託運單
  - 補印託運單
  - 宅配通逆物流退貨
features:
  - 宅配通託運單
  - 批次出貨
  - 單筆出貨
  - 補印託運單
  - 加印託運單
  - 逆物流退貨
prerequisites:
  - "ec/payments-and-logistics/setup-pelican-waybill-v2"
tags:
  - 宅配通
  - 出貨
  - 託運單
  - 物流配送
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 訂單 > 所有訂單
  - 金物流 > 宅配通託運單
  - 宅配託運單管理 > 宅配通託運單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=63
  - https://www.cyberbiz.io/support/?p=975
permalink: "https://help.cyberbiz.io/ec/orders/home-delivery/pelican-shipping-v2/"
comments: false
search:
  exclude: false
icon: lucide/bird
hide: []
---

![下載宅配通託運單](../../../assets/images/EC-訂單-所有訂單-下載宅配通託運單-hero.png){ title="下載宅配通託運單" .hero-page }

## 宅配通出貨說明 { #intro-pelican }

開通與宅配通系統串接的物流功能後，您可以從後台直接產出宅配通官方託運單 PDF，並由系統自動把訂單貨態更新為「已出貨(待物流收件)」，免去手寫單與另行登錄追蹤的工作。

本文聚焦於 **日常出貨流程** ，包含批次下載託運單、單筆與部分出貨、補印託運單等操作。寄件人設定、加印託運單(同訂單多箱)、逆物流退貨等進階管理操作，請見 [宅配通託運單管理頁](../../payments-and-logistics/setup-pelican-waybill-v2.md){ title="設定宅配通託運單" }。

!!! info "重要規範" 
    * **嚴禁使用手寫單**：串接物流必須使用系統產出的託運單。手寫單無法回傳貨態，將影響對帳與客服處理。
    * **特殊區域與材積**：部分[離島、偏遠地區](#reference-pelican-exclusion)及特殊材積、特殊貨品內容，可能無法配送或需依宅配通公告另行加價，實際配送與費用以宅配通公告為準。
    * **冷鏈商品**：宅配通低溫配送目前暫不開放，請改用其他物流方案。

## 使用前提與限制 { #prerequisites-pelican }

### 計費方式 { #prerequisites-pelican-billing-mode }

| 商家類型 | 計費方式 | 印單前提 |
| :-- | :-- | :-- |
| 一般版 | 預扣 **Cyber 幣** ，自帳戶餘額扣除 | 餘額不足時無法列印，需先至儲值中心儲值 |
| PLUS版 / 企業版 | 列入每期 **對帳單** 統一收款 | 無須預先儲值 |

!!! info "提示"
    若不確定自家屬於哪一種計費方式，進入「宅配通託運單」頁面後，頁面上方若顯示「目前 Cyber 幣 餘額」即為一般版；若顯示對帳單說明文字即為 PLUS版 / 企業版。

---

### 出貨前置設定 { #prerequisites-pelican-preconfig }

首次使用宅配通出貨前，請先完成下列設定：

- [x] **宅配通寄件人地址**(批次出貨用)：至「金物流」>「[宅配通託運單](../../payments-and-logistics/setup-pelican-waybill-v2.md#configure-pelican-shipping-note-sender){ title="設定寄件人資料" }」設定寄件人地址，若無設定則會導致出貨時出現「寄件人資訊不完整」的通知。
- [x] **宅配通寄件人資料**(加印託運單與逆物流用)：至「金物流」>「宅配通託運單」頁面的「宅配通設定」區塊填寫，詳見 [宅配通託運單管理頁](../../payments-and-logistics/setup-pelican-waybill-v2.md#configure-pelican-shipping-note-sender){ title="設定寄件人資料" } 。

---

### 託運單貼紙與設備 { #prerequisites-pelican-preparations }

* 託運單必須列印於宅配通官方提供的 **「宅配通三連空白託運單貼紙」** 上，系統產出的內容才會對齊欄位。
* 領取貼紙：請先聯繫 CYBERBIZ 客服取得「客戶代號」，再致電宅配通索取貼紙。
* 列印設備建議使用 **雷射印表機** ，避免條碼掉色或模糊導致物流端掃描失敗。
* 嚴禁使用手寫單據出貨，否則系統無法追蹤貨態，後續對帳與客訴將無法處理。

---

### 訂單條件 { #prerequisites-pelican-order-status }

可使用宅配通出貨的訂單需符合下列條件：

* 訂單的 **配送方式為宅配通** (批次出貨時，若勾選的訂單包含其他物流類型將無法一次下載)。
* 付款狀態為「已付款」或「貨到付款」。
* 配送狀態為「未出貨」、「部分出貨」、「準備出貨」或「運送異常」。

## 操作步驟 { #operate-pelican }

### 批次下載託運單並更新貨態 { #operate-pelican-bulk-download }

當您有多筆宅配通訂單要一次出貨時，從訂單列表批次處理最有效率。

1. **進入訂單列表**：前往後台「訂單」>「所有訂單」。
2. **篩選宅配通訂單**：建議先用「配送方式」篩選為「宅配通」，確保勾選的訂單都是同一物流[^1]。
3. **勾選欲出貨訂單**：在訂單列表左側勾選要出貨的訂單(可跨頁勾選或全選當頁)。
4. **執行批次操作**：點選列表上方的「選擇操作」下拉，選擇 **「下載宅配通託運單並將貨態改為『已出貨』」** 。

    ![下載宅配通託運單](../../../assets/images/EC-訂單-所有訂單-下載宅配通託運單.png){ title="下載宅配通託運單" }

5. **檢視運費明細**：彈窗 中段會列出本批次要扣除的 Cyber 幣或對帳金額，請確認與預期相符。
6. **確認寄件地址**：預設帶入該物流上一次使用的寄件地址（首次帶入 [宅配通設定](../../payments-and-logistics/setup-pelican-waybill-v2.md#configure-pelican-shipping-note-sender){ title="設定寄件人資料" } 中的地址），如需更改可點擊 **「更改」** 按鈕編輯[^4]。

    ![確認寄件地址](../../../assets/images/ec-orders-pelican-waybill-popup-address.png){ title="確認宅配通託運單地址" }

7. **同意條款**：勾選頁面底部的 **「我已閱讀並同意 CYBERBIZ 物流串接服務條款 與 宅配通合約規範」** 。
8. **確認下載**：點擊 **「確認」**。系統會建立託運單、扣除運費，並將訂單貨態更新為「[已出貨(待物流收件)](shipping-status-tooltip.md#shipping-status-text-type){ title="出貨狀態物流提示文字說明" data-preview }」。

    !!! warning "印單後無法修改收貨資訊"
        一旦下載託運單，系統會將收貨資訊與託運單綁定，無法在後台修改。如需修改，只能取消該張託運單(請聯繫 CYBERBIZ 客服)後重新建立。

9. **接收託運單檔案**：系統會自動下載一個[壓縮檔](../references/order-filter-status-reference.md#reference-logistics-zip-contents){ title="託運單下載內容物說明" data-preview }，內含託運單 PDF 與相關出貨單據。請以「宅配通三連空白託運單貼紙」列印託運單並貼於紙箱。
10. **預約收件**：列印完成後請聯繫宅配通客服預約收件，或依您與宅配通約定的固定取件時段準備出貨。收件後，訂單詳情頁內狀態會顯示為「[已出貨(配送中)](shipping-status-tooltip.md#shipping-status-text-type){ title="出貨狀態物流提示文字說明" data-preview }」。

[^1]: 勾選的訂單若包含非宅配通訂單(例如混雜黑貓、超商取貨)，彈窗會無法開啟或在送出時跳錯。請先用「配送方式」篩選器確保批次內物流類型一致。
[^4]: 修改後會同步更新該物流頁面地址，不同物流間及公司物流地址互不影響。

---

### 單筆出貨與部分出貨 { #operate-pelican-single-shipment }

若您只想針對 **單一訂單** 出貨，或這筆訂單只有部分商品要先寄出，請改從訂單詳情頁操作。

1. 進入「訂單」>「所有訂單」，點選訂單編號進入訂單詳情頁。
2. 於右側「出貨」區塊勾選本次要出貨的商品。
3. 在「選擇出貨方式」下拉選單選擇「宅配通託運單」。
4. 在「請選擇費用」下拉選單挑選對應的配送尺寸。
5. 視需求調整「發送郵件通知顧客」勾選狀態。
6. 點擊 **「確認出貨」** ，系統會建立託運單並扣除運費。

詳細的部分出貨流程、不同物流的差異與 FAQ，請參閱 [訂單部分出貨](partial-shipment-v2.md){ title="設定訂單部分出貨" } 。

---

### 補印託運單 <small>損壞或遺失</small> { #operate-pelican-reprint }

如果託運單已下載過，但貼紙印壞、遺失，或想再列印一次同一張單，可以使用補印功能。**補印不會產生新單號，也不會重複扣費。**

1. 前往「訂單」>「所有訂單」。
2. 篩選或勾選狀態為「已出貨」的宅配通訂單。
3. 從「選擇操作」下拉中選擇 **「補印託運單」** 。
4. 系統會重新產出原本的託運單 PDF，請以宅配通三連空白託運單貼紙列印。

!!! info "提示"
     補印僅針對 **已產出過的單號** 重新印出 PDF 。若您需要為同一訂單產生 **新的單號** (例如拆箱分多件寄送)，請改用 [加印託運單](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-note-add-print){ title="加印託運單" } 功能。

## 後續操作 { #followup-pelican }

<div class="grid cards" markdown>

- :lucide-truck:{ .lg }  
  [__追蹤貨態__](shipping-status-tooltip.md#shipping-status-text-type){ title="出貨狀態物流提示文字說明" }  
  出貨後配送狀態會變為「已出貨(待物流收件)」，等宅配通實際收件並掃描後，會依物流回拋逐步更新為運送中、已送達等狀態。

- :lucide-receipt:{ .lg }  
  [__檢視對帳紀錄__](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-records){ title="查詢紀錄與對帳" }  
  「宅配通託運單」頁面下方的單號使用紀錄會列出每張託運單的訂單編號、單號、扣除金額與單號狀態，可用於對帳。

- :lucide-printer:{ .lg }  
  [__加印或處理退貨__](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-note-add-print){ title="加印託運單" }  
  同一筆訂單需要拆箱多寄，或處理顧客退貨時，請至宅配通託運單管理頁進行加印託運單或建立逆物流。

</div>

---

## 常見問題 { #faq-pelican }

??? quote "「下載宅配通託運單並將貨態改為『已出貨』」選項不見了？"
    [](){ #faq-pelican-action-missing }

    請依下列順序檢查：

    * 勾選的訂單是否包含 **非宅配通** 的物流類型(混合勾選時系統無法批次處理)
    * 訂單付款狀態是否為「已付款」或「貨到付款」

??? quote "Cyber 幣不足時要怎麼處理？"
    [](){ #faq-pelican-insufficient-points }

    若您是一般版商家，須先至「儲值中心」儲值 Cyber 幣後才能列印託運單。PLUS / 企業版商家無此限制，運費會列入每期對帳單。

??? quote "託運單下載後沒寄出，Cyber 幣會自動退嗎？"
    [](){ #faq-pelican-unused-refund }

    會。下載後 **兩週(14 日)內未實際寄出** ，系統會自動退回該張託運單的運費，並將單號狀態標記為「取消寄件」。若退費後仍使用該張託運單，系統會再次記錄運費。

??? quote "已經出貨了才發現收件地址打錯，怎麼辦？"
    [](){ #faq-pelican-modify-address }

    託運單一旦下載，後台 **無法自行修改** 收件資訊。如包裹尚未交付物流，建議：

    * 聯繫 CYBERBIZ 客服協助取消該張託運單
    * 修改訂單收件資料後，以新訂單資料重新下載託運單

    若包裹已被宅配通收走，請直接聯繫宅配通客服處理。

??? quote "一筆訂單要分多箱寄，應該用「部分出貨」還是「加印託運單」？"
    [](){ #faq-pelican-multibox }

    判斷標準：

    * 商品 **一次全部寄出，但裝不下一箱** > 使用 [加印託運單](../../payments-and-logistics/setup-pelican-waybill-v2.md#operate-pelican-shipping-note-add-print){ title="加印託運單" } ，可在同一筆訂單建立多張單號，每箱貼一張。
    * 商品 **分批寄出** (例如缺貨先寄一部分，後續到貨再寄)> 使用「部分出貨」，於訂單詳情頁勾選本次要寄的商品即可。
    * 貨到付款訂單若要分箱寄送， **必須** 使用加印託運單(代收款需綁定託運單號)。

??? quote "「補印託運單」和「加印託運單」有什麼差別？"
    [](){ #faq-pelican-reprint-vs-addprint }

    * **補印託運單**：針對 **已產生過的單號** 重新印一次 PDF，不會產生新單號，**不會重複扣費** 。適用情境：貼紙印壞、檔案遺失。
    * **加印託運單**：為同一筆訂單建立 **新的單號** ，每張單會 **各自扣費** ，系統會帶入原訂單資訊。適用情境：同訂單分多箱寄送。

??? quote "可以使用手寫的宅配通託運單嗎？"
    [](){ #faq-pelican-handwritten }

    不可以。串接物流必須使用系統產出的託運單，系統才能與宅配通介接回拋貨態。使用手寫單會導致系統無法追蹤包裹，對帳與客訴也無法處理。

??? quote "離島或偏遠地區可以使用宅配通嗎？"
    [](){ #faq-pelican-remote-area }

    部分離島(如澎湖、金門、馬祖等)、偏遠地區與特殊地址(如郵政信箱)可能無法配送，或需依宅配通公告另行加價。實際可配送範圍與運費請以宅配通官方公告為準，建議出貨前先與顧客確認。

## 參考資料 { #reference-pelican }



### 宅配通不支援地區 { #reference-pelican-exclusion }

以下區域恕不提供宅配通貨件配送服務：

- **澎湖地區**：望安鄉、七美鄉、虎井島、桶盤島、大倉嶼、員貝嶼、鳥嶼、花嶼、吉貝嶼。
- **金門地區**：烏坵、烈嶼、大膽、二膽。
- **馬祖地區(連江縣)**：南竿鄉、北竿鄉、莒光鄉、東引鄉。
- **其它**：蘭嶼、綠島、小琉球等外島及郵政信箱。

!!! info "貼心提醒"
    離島與偏遠地區之服務範圍可能調整而變動。最新且詳細的服務區域規範，請至 [宅配通官方網站 - 服務據點查詢 :lucide-external-link:](https://www.e-can.com.tw/m/search_Location.aspx) 進行確認。
