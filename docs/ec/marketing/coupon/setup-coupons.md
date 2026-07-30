---
title: 設定優惠券
description: 說明如何設定優惠券，包含全館發送、批次匯入發送及單一顧客發送的操作流程。
created: 2026-05-27 16:30
last_modified: 2026-06-30 10:56
lang: zh-TW
type: tutorial
status: update
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - 行銷活動
sites: 
  - TW
audiences: 
  - admin
difficulty: beginner
tnb: trunk
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents: 
  - 設定優惠券
  - 發送折價券
  - 批次匯入優惠券
  - 贈送註冊禮
features: 
  - 優惠券
  - 折價券
  - 消費回饋
  - 註冊贈禮
prerequisites: []
related: 
  - "[[設定優惠碼與贈品券]]"
  - "[[設定紅利點數與發送指南]]"
tags: 
  - 優惠券
  - 折價券
  - 行銷活動
  - 會員經營
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 優惠券設定欄位
  - 會員列表
paths: 
  - 行銷活動 > 全館折扣-紅利 & 優惠券
  - 行銷活動 > 促銷活動
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1779
  - https://www.cyberbiz.io/helpcenter/?p=3435
  - https://www.cyberbiz.io/helpcenter/?p=509
  - https://www.cyberbiz.io/helpcenter/?p=5686
  - https://www.cyberbiz.io/support/?p=11928
  - https://www.cyberbiz.io/support/?p=6207
permalink: "https://help.cyberbiz.io/ec/marketing/coupon/setup-coupons/"
comments: false
search:
  exclude: false
icon: lucide/ticket-percent
hide: []
---

# 設定優惠券
說明如何設定優惠券，包含全館發送、批次匯入發送及單一顧客發送的操作流程。
{ .subtitle }


!!! tip "應用情境"
	- **新客首購**：設定註冊即送優惠券，降低顧客首次下單的猶豫。
	- **滿額獎勵**：設定消費滿額回饋折價券，激勵顧客提高客單價以獲得下次折扣。
	- **精準行銷**：針對特定會員群組批次發送專屬優惠券，進行分眾經營。
	- **補償與關懷**：手動發送優惠券給單一顧客，作為服務補償或節慶驚喜。


## 使用須知

- **刪除限制**：優惠券一旦匯入會員帳戶，如需刪除，必須前往 [會員個人頁面逐筆操作](../../members/manage-member-profiles.md#2-優惠券派發與管理)，系統無法批次撤回。

### 取消與退貨處理

| 情境 | 處理規則 |
| :--- | :--- |
| **取消訂單** | 該訂單中使用的優惠券，系統將 **自動歸還** 至顧客帳戶 |
| **退貨處理** | 該訂單中使用的優惠券，系統 **不會自動歸還**<br>該訂單滿額所獲得的折價券，系統 **不會** 從顧客帳戶扣除 |
| **退貨點數扣除** | 該訂單滿額所獲得的折價券，系統 **不會自動從顧客帳戶扣除** |


## Excel 批次發送優惠券

1. 前往 **行銷活動 > 全館折扣-紅利 & 優惠券**，選擇 **批次發送會員專屬優惠券**。
2. 點擊 **下載範本**。填寫時請刪除範例內容，僅保留藍色標題區塊。
3. **Excel 範本欄位填寫說明**：

    | 欄位名稱 | 填寫規範與說明 |
    | :--- | :--- |
    | **贈送給顧客的 E-Mail** | 優先檢查，留空才檢查手機<br>- 發送所有會員：填入 `[all]` (半形小寫)<br>- 發送指定會員：填入指定會員 Email | 
    | **贈送給顧客的手機** | 若 Email 欄位留空，才執行檢查 <br>- 發送所有會員：填入 `[all]` (半形小寫)<br>- 發送指定會員：填入指定會員手機 | 
    | **優惠名稱** | 前台顯示給顧客看的名稱 (必填) |
    | **序號** | 8 碼大寫英數字組合 (必填) |
    | **折扣** | 可設定「固定金額」或「百分比」(如 8 折請輸入 `80%`) |
    | **可使用次數** | 此優惠碼總計可被使用的次數 (需 ≥ 1) |
    | **每個帳號使用次數** | 單一會員可使用的次數 (需 ≥ 1)，留空代表不限次數<br>(PLUS、企業版專用) |
    | **滿額門檻** | 訂單需達到的金額門檻才能使用 (輸入 `0` 代表無門檻) |
    | **有效時間** | 設定開始與結束時間；留空代表無期限限制 |
    | **綁定商品標籤** | 填入標籤名稱，則僅限購買含該標籤的商品時可折抵<br>(進階、高手、PLUS、企業版專用) |
    | **促銷活動併用方式** | 規範優惠券與其他行銷活動（如紅配綠、滿額折）的疊加規則：<br><br>**1. [unrestricted] （完全併用）**：優惠券可與所有活動疊加。不論商品是否已享有其他折扣，皆可進行折抵<br>- 後方活動欄位 [11]-[18] ：留空即可<br><br>**2. [restrict] （排除特定活動商品 — 商品級排除）**：若訂單中的 **單一商品** 已套用指定的行銷活動，則該商品 **不計入** 優惠券的折抵金額，但訂單內其他未參加活動的商品仍可正常折抵<br>- 後方活動欄位 [11]-[18] ：欲指定排除，填寫 `[true]排除`<br><br>**3. [forbidden] （包含活動即禁用 — 訂單級排除）**：只要購物車中包含任何一個套用指定活動的商品，**整筆訂單** 皆無法使用該優惠券<br>- 後方活動欄位 [11]-[18] ：欲指定排除，填寫 `[true]排除` |

    ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-批次-建立發送-優惠券碼05.png){ .screenshot }
    ![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-批次-建立發送-優惠券碼06.png){ .screenshot }

4. 儲存檔案後，回到後台點擊 **上傳檔案** 完成匯入。


### 批次發送優惠券通知規則

- **特定會員**：系統匯入後將自動發送 Email 或簡訊通知顧客。
- **所有會員 (all)**：系統會自動歸戶至會員中心，但 **不會** 發送通知。
- **對象限制**：僅限已在網站註冊的會員。若 Email 不存在於系統中，該筆資料將跳過。


## 手動篩選批次發送優惠券

前往 **會員 > 所有會員**，使用會員篩選器或針對特定個人 [手動發送或刪除優惠券](../../members/manage-member-profiles.md#2-優惠券派發與管理)。


## 更多操作

<div class="grid cards" markdown>

- :lucide-layers-2:{ .lg }
  [__設定多張優惠券(碼)併用__](multiple-coupons.md)
  設定單筆訂單可使用的優惠券數量上限。

- :lucide-bell-ring:{ .lg }
  [__設定優惠券到期通知__](../purchase-restrictions/coupon-and-bonus-points-expiry-notification.md)
  設定系統自動發送 Email、簡訊或 LINE 通知，提醒顧客及時使用即將到期的優惠。

</div>

