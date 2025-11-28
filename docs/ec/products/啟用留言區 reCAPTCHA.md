---
title: 啟用留言區 reCAPTCHA
description: 啟用 Google reCAPTCHA、防止機器人及垃圾留言
module:
  - 網站設定
tasks:
  - 防止垃圾留言
  - 防止機器人訊息
type: tutorial
product:
  - EC
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
surfaces:
  - 網站外觀 > 管理商品評論
  - 會員 > 顧客回饋&建議
system:
  - 後台
lang: zh-TW
sites: 台灣
status: review
activ: configure
listen: assets/audios/設定留言區 reCAPTCHA 聽讀.mp3
tags:
  - 資安
  - Google
note:
  - verify FAQ
  - update internal links
---

# 啟用留言區 reCAPTCHA

:lucide-lock:{ title="適用方案" } | PLUS 企業  
:lucide-toggle-right:{ title="適用功能" } | 拖拉版型 

啟用 Google reCAPTCHA 防止機器人訊息及垃圾留言，保護留言區，提升網站安全性及顧客互動品質。  

![](../../assets/audios/設定留言區%20reCAPTCHA%20聽讀.mp3)
![](../../assets/videos/e-ticket-reconciliation-computer.mp4)

### 為什麼要用 reCAPTCHA
- 防範垃圾留言：保護商品評論區與聯絡我們頁面免受機器人攻擊。  
- 提升網站安全性：有效辨識非人類操作，減少濫用行為與詐欺風險。  
- 維護互動品質：確保留言內容真實有效，改善顧客互動體驗。  

!!! quote "什麼是 reCAPTCHA？"
	reCAPTCHA 是 Google 提供的安全驗證服務，用於區分真人與機器人，保護網站表單、留言區與交易流程免受自動化攻擊。它能有效防止垃圾訊息、刷單或惡意程式操作，並提升網站整體安全性。了解更多，請參考[官方網站 :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=zh_tw)。

## 使用須知

### 適用範圍

- [x] 商品頁面評論區。
- [x] 聯絡我們頁面。

<div class="grid cards" markdown>

- ![商品評論區建立 reCAPTCHA 安全驗證機制](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00.png){ title="商品頁面評論區" }
- ![聯絡我們頁面建立 reCAPTCHA 安全驗證機制](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA01.png){ title="聯絡我們頁面" }

</div>

### 費用
- Google reCAPTCHA 提供免費用量配額，若超出免費用量，顧客將無法進行留言。
> 達到免費用量上限前，Google 會透過電子郵件通知商家。
- 更多資訊，請看[配額與限制 :material-open-in-new:](https://docs.cloud.google.com/recaptcha/quotas?hl=zh-tw)

## 操作步驟

### 申請 Google reCAPTCHA 金鑰

1. 前往 [Google reCAPTCHA 管理控制台 :material-open-in-new:](https://www.google.com/recaptcha/admin/)，並登入您的 Google 帳號。
2. 依序填寫註冊資訊。
> **標籤**：依您的需求命名此 reCAPTCHA （例如：`您的商店名稱_reCAPTCHA`）。  
> **reCAPTCHA 類型**：選擇「驗證問題」，並勾選「隱形 reCAPTCHA 標記」[^隱形 reCAPTCHA]。  
> **網域**：輸入您的官網網址。  
> **Google Cloud Platform**：依您的需求選擇專案。  
	
	??? warning "網址填寫注意事項"
		請勿填入網址前綴 `https://` 與後綴 `/...`。例如：若您的官網網址為 `https://_demo1234.cyberbiz.co_ /zh-TW`，請僅填入 `_demo1234.cyberbiz.co_`。

2. 點擊 **提交** 按鈕，取得 Google reCAPTCHA 的 **網站金鑰 (sitekey)** 與 **密鑰 (secretkey)**。

3. 複製並妥善保存 **網站金鑰** 跟 **密鑰**，後續將用於綁定步驟。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA03.png){ .screenshot }


### 將 reCAPTCHA 金鑰綁定商品評論區
:lucide-lock:{ title="適用方案" } | PLUS 企業

!!! note "方案限制"
    商品評論功能僅供 **企業版**、**PLUS 版** 商家使用，若需啟用此功能，請聯絡客服開通。了解如何[商品評論指南](商品評論指南.md)。

1. 登入 CYBERBIZ 電商後台，前往 **網站外觀 > 管理商品評論**。
2. 點擊 Google reCAPTCHA 開關 :material-toggle-switch:，以開啟功能（ON）。
3. 貼上金鑰。
> **reCAPTCHA sitekey**：將在申請過程中取得的 **網站金鑰** 填入此欄位。  
> **reCAPTCHA secretkey**：將在申請過程中取得的 **密鑰** 填入此欄位。  
4. 點擊「更新」套用變更。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA04.png){ .screenshot }


### 將 reCAPTCHA 金鑰綁定聯絡我們頁面

1. 登入 CYBERBIZ 電商後台，前往 **會員 > 顧客回饋 & 建議**。
2. 點擊 **啟動機器人阻擋** 開關 :material-toggle-switch:，以開啟功能（ON）。
3. 貼上金鑰
> **sitekey** 將申請過程中取得的 **網站金鑰** 填入此欄位。  
> **secret key** 將申請過程中取得的 **密鑰** 填入此欄位。
4. 點擊 **儲存所有設定** 套用變更。

![](../../assets/images/ec-members-customer-feedback-enable-reCAPTCHA.png)

## 常見問題
??? quote "一組 Google reCAPTCHA 帳號可以綁定多個網域嗎？"
    是的，一組 Google reCAPTCHA 帳號可以綁定多個網域。您可以使用同一組密鑰綁定商品評論與聯絡我們頁面。

??? quote "Google reCAPTCHA 有免費用量配額嗎？"
    Google reCAPTCHA 提供免費用量配額。當達到免費用量上限前，Google 會透過電子郵件通知商家。若超出免費用量，顧客將無法進行留言，請自行向 Google 升級方案。了解相關[費用](#費用)。

??? quote "如果金鑰填寫錯誤會怎麼樣？"
    請確保金鑰填寫正確，否則留言功能將無法正常使用。如有錯誤訊息 (如下圖)，請檢查金鑰是否填寫無誤。

    [![reCAPTCHA 金鑰填寫錯誤](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)

??? quote "此 reCAPTCHA 功能是否適用於所有版型網站？"
    此功能僅限拖拉版型網站使用。

## 延伸閱讀

- [設定商品評論功能](#)

[^隱形 reCAPTCHA]: 隱形 reCAPTCHA 可在顧客互動時自動判斷是否為機器人，通常不會打斷顧客操作，僅在系統判斷為可疑時才出現驗證題目。這能同時減少顧客操作干擾，並提升網站防護力。