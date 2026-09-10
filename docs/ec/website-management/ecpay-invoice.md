---
title: 設定綠界電子發票
description: 了解如何將 CYBERBIZ 系統與綠界科技（ECPay）電子發票服務串接，設定自動開立時機與管理發票作廢規則。
created: 2026-06-26 18:40
last_modified: 2026-06-26 18:40
lang: zh-TW
type: guide
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
  - merchant
difficulty: beginner
tnb: branch
plans: 
  - 進階
  - 高手
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
cyb_extensions: []
intents: 
  - 串接綠界電子發票
  - 設定發票自動開立
  - 解決發票開立失敗問題
features: 
  - 電子發票
  - 綠界串接
  - 自動開立
prerequisites: 
  - "申請綠界科技帳戶"
related: 
  - "ec/website-management/manage-system-issued-consumer-invoices"
tags: 
  - 綠界
  - 電子發票
  - ECPay
  - 金流整合
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 發票設定
  - 結帳發票設定
paths: 
  - 管理中心 > 發票設定
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=3274
permalink: "https://help.cyberbiz.io/ec/website-management/ecpay-invoice/"
search:
  exclude: false
icon: lucide/receipt-text
hide: []
---

# 設定綠界電子發票
了解如何將 CYBERBIZ 系統與綠界科技（ECPay）電子發票服務串接，設定自動開立時機與管理發票作廢規則。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 進階 / 高手 / 所有 PLUS
{ .doc-badge }

## 申請條件

- [X] 商家需具備確實營利登記，且綠界帳戶需為 **商務會員** 或 **特約會員** 以上等級。
- [X] 在本國境內有確實 **營利登記** 的公司。
- [X] 無積欠已確定之營業稅及罰鍰、營利事業所得稅及罰鍰。

## 使用須知

- **字軌管理**：請務必定期至綠界後台確認「發票字軌」是否充足。若字軌用罄，系統將無法自動開票。
- **客服支援**：關於綠界帳戶權限、字軌上傳等問題，請洽綠界客服：02-2655-1775。



## 申請流程


1. 請先進行 [綠界服務申請](https://member.ecpay.com.tw/MemberReg/MerchantRegister)，相關申請流程可參考 [綠界網頁說明](https://www.ecpay.com.tw/Business/einvoice_knowledge_flow)。
2. 完成註冊且確認電子發票開通完成後，可進行以下設定。

## 串接流程

### 步驟一：取得綠界串接資訊

在開始設定前，請先備妥綠界端的金鑰資訊。

1. 登入 [綠界廠商管理後台](https://vendor.ecpay.com.tw/)。
2. 前往 **系統開發管理 > 系統介接設定**。
3. 複製頁面中的 **商店代號 (MerchantID)**、電子發票的 **介接 HashKey** 與 **介接 HashIV**。

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-綠界02.png){ .screenshot }

### 步驟二：後台資訊串接

將取得的資訊填入 CYBERBIZ 系統。

1. 登入 CYBERBIZ 管理後台，前往 **管理中心 > 發票設定**。
2. 找到「綠界發票設定」區塊，填入對應的 **綠界廠商編號**、**HashKey** 與 **HashIV**。

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-綠界01.png){ .screenshot }

3. 在「結帳發票設定」區塊，將 **已啟用結帳頁顯示發票** 切換為 `開啟 (ON)`。
4. 在「發票開立方式」下拉選單中選擇 **綠界電子發票**。

    ![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/電子發票-綠界03.png){ .small-image }

### 步驟三：設定發票開立時機

根據您的出貨流程選擇自動開票的時間點。

- **付款時**：訂單狀態變更為「已收到款項」時立即開立。
- **出貨時**：訂單配送狀態變更為「已出貨」時開立。

    > 建議以此時作為發票開立時間點，可避免在未出貨前客戶取消訂單而需作廢發票。

- **取貨時**：訂單配送狀態變更為「已收貨」時開立。

!!! note "取貨時開立限制"
    此功能僅支援有串接貨態回傳的物流方式（如：黑貓、宅配通、綠界/EZShip 超取）。若使用 **非串接系統的自訂物流**，系統無法得知準確收貨時間，將無法觸發此時機。


## 系統邏輯說明

### 取消與退貨處理

系統會根據訂單狀態自動連動綠界執行發票異動：

| 訂單異動情境 | 系統自動化動作 |
| :--- | :--- |
| **全單取消 / 全單退貨** | 系統將自動向綠界發送指令，**作廢** 該筆電子發票。 |
| **部分退貨** | 系統將自動針對退貨金額產生 **折讓單**。 |



## 常見問題

??? quote "為什麼發票顯示「開立失敗」？"
    請前往該訂單頁面，查看左下角的 **訂單操作紀錄**。
    
    常見原因如下：
    - **查無可使用字軌**：請至綠界後台補上傳發票字軌，再回到 CYBERBIZ 訂單手動點選開立。
    - **金鑰錯誤**：請重新核對並更新後台填寫的廠商編號與 HashKey/IV。
