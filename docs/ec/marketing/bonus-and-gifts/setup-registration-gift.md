---
title: 設定註冊禮
description: 設定會員註冊禮，包含紅利點數與優惠券的發送規則，吸引新客完成首次註冊與消費。
created: 2026-05-27 12:30
last_modified: 2026-05-27 12:30
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
plans: []
cyb_extensions: []
intents: 
  - 設定註冊禮
  - 會員註冊獎勵
  - 發送註冊優惠券
features: 
  - 註冊禮
  - 紅利點數
  - 優惠券
prerequisites: []
related: 
  - "[[設定紅利購物金說明]]"
  - "[[設定生日禮]]"
tags: 
  - 註冊禮
  - 紅利點數
  - 優惠券
  - 新客行銷
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 優惠券
  - 紅利點數
paths: 
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 會員註冊贈送優惠券
  - 行銷活動 > 全館折扣-紅利 & 優惠券 > 會員紅利點數
layouts: []
wp_url: 
  - https://www.cyberbiz.io/helpcenter/?p=3816
  - https://www.cyberbiz.io/support/?p=6234
permalink: "https://help.cyberbiz.io/ec/marketing/bonus-and-gifts/setup-registration-gift/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

# 設定註冊禮
設定會員註冊禮，包含紅利點數與優惠券的發送規則，吸引新客完成首次註冊與消費。
{ .subtitle }


![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-會員註冊贈送優惠券-紅利積點01.png){ .hero-page }

!!! tip "應用情境"
	- **新客引導**：顧客註冊即送紅利或優惠券，降低首購門檻。
	- **會員名單收集**：以獎勵誘因鼓勵訪客留下資料成為正式會員。
	- **品牌初體驗**：讓新會員在首次消費時感受到品牌誠意。

---

## 使用須知

- **發送頻次**：每個帳號僅會獲得一次註冊禮。
- **匯入會員限制**：透過 Excel 批次匯入的顧客，系統 **不會自動贈送註冊禮**，需手動補發。
- **自動發送**：顧客完成註冊的當下，系統將自動將獎勵匯入至顧客帳戶。


## 操作流程

### 1. 設定註冊禮優惠券

!!! info "版本適用說明"
    **註冊禮優惠券** 為 高手版、PLUS 版、企業版用戶限定欄位。

1. 登入 CYBERBIZ 管理後台，前往 **行銷活動 > 全館折扣-紅利 & 優惠券 > 會員註冊贈送優惠券**。
2. 將功能切換為 `開啟`。
3. 設定優惠券內容：
    - **優惠券種類**：選擇 `金額` 或 `百分比`。
    - **折價數值**：輸入折抵金額或折扣（如 88 折輸入 88）。
    - **使用限制**：設定使用次數、訂單滿額門檻、綁定商品標籤及併用限制。
    - **有效期限**：設定領取後幾天內有效（輸入 0 代表永久有效）。

![](https://www.cyberbiz.io/support/wp-content/uploads/全館折扣-會員註冊贈送優惠券-紅利積點01.png){ .screenshot }


### 2. 設定註冊禮紅利點數


1. 前往 **行銷活動 > 全館折扣-紅利 & 優惠券 > 會員紅利點數**。
2. 在 **消費者註冊贈送** 欄位輸入欲贈送的點數。

    > 若只想啟用紅利功能但不送註冊禮，請將此欄位設為 0。
    
3. 設定紅利有效期限（輸入 0 代表永久有效）。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/紅利點數註冊.png){ .screenshot }


!!! info "版本適用說明"
    **紅利折抵最低消費門檻** 與 **單筆訂單折抵上限** 為 PLUS 版、企業版用戶限定欄位。



## 常見問題

??? quote "註冊禮發送後可以收回嗎？"
    優惠券一旦匯入會員帳戶，如需刪除，必須前往 **會員 > 所有會員** 進入個人頁面逐筆操作。紅利點數亦同。

??? quote "如果我同時開啟優惠券與紅利點數，會員會同時拿到嗎？"
    會的。若兩項功能皆開啟，顧客註冊時系統會一併發送優惠券與紅利點數。


