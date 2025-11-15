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
啟用 Google reCAPTCHA、防止機器人訊息及垃圾留言
{ .page-subtitle }

[:material-tag-text:](){ .badge-icon title="適用方案" }[PLUS | 企業](){ .badge-text } 
[:material-toggle-switch:](){ .badge-icon title="適用功能" }[拖拉版型](){ .badge-text } 
[:material-arrow-left-circle:](){ .badge-icon title="相關操作" }[[使用商品評論功能]]{ .badge-text }

---

## 說明概述
??? example "AI 摘要"
    ![[設定留言區 reCAPTCHA 聽讀.mp4]]{ .audio-small }

### 為什麼要用 reCAPTCHA
允許顧客留言的頁面，容易遭受機器人攻擊與垃圾訊息干擾。啟用 Google reCAPTCHA 驗證，可有效識別非人類操作，保護網站免受垃圾內容、濫用行為和詐欺侵擾，維護留言區品質。更多 reCAPTCHA 功能，請參考[官方網站 :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=zh_tw)。

!!! quote "為什麼要用 reCAPTCHA？"
	允許顧客留言的頁面可能遭受機器人攻擊與垃圾訊息干擾。啟用 Google reCAPTCHA 驗證，可有效識別非人類操作，保護網站免受垃圾內容、濫用行為及詐欺侵擾，維護留言區品質。了解更多 reCAPTCHA 功能，請參考[官方網站 :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=zh_tw)。

=== ":material-information-outline: 使用須知"

    - [x] Google reCAPTCHA 提供免費用量配額，若超出免費用量[^超出免費 reCAPTCHA 額度]，顧客將無法進行留言。詳情請看[配額與限制 :material-open-in-new:](https://cloud.google.com/recaptcha/quotas?hl=zh-tw)。
    - [x] 支援「商品頁面」的評論區跟 `聯絡我們` 頁面。 

	<div class="grid cards" markdown>
	
	- ![商品評論區建立 reCAPTCHA 安全驗證機制](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00.png){ title="商品頁面評論區" }
	- ![聯絡我們頁面建立 reCAPTCHA 安全驗證機制](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA01.png){ title="聯絡我們頁面" }
	- 
	</div>

=== ":material-lightbulb-outline: 使用情境"

    - 防範垃圾留言：保護官網的商品評論區與聯絡我們頁面免受機器人自動發送的垃圾訊息干擾。
    - 提升網站安全性：透過 reCAPTCHA 驗證機制，有效識別非人類操作，增加網站防護層級。
    - 維護顧客互動品質：確保留言區塊的內容真實有效，提升顧客互動體驗。



---

## 操作流程
### 步驟一：申請 Google reCAPTCHA 金鑰

=== ":material-numeric-1-circle: 進入控制台"

    - [ ] 前往 [Google reCAPTCHA 管理控制台 :material-open-in-new:](https://www.google.com/recaptcha/admin/)，並登入您的 Google 帳號。

=== ":material-numeric-2-circle: 註冊網站"

    - [ ] 依序填寫註冊資訊。

    - 標籤：依您的需求命名此 reCAPTCHA （例如：`您的商店名稱_reCAPTCHA`）。
	 - reCAPTCHA 類型：選擇「驗證問題」，並勾選「隱形 reCAPTCHA 標記[^隱形 reCAPTCHA]」
    - 網域：輸入您的官網網址。

    ??? warning "網址填寫注意事項"
        請勿填入網址前綴 `https://` 與後綴 `/...`。例如：若您的官網網址為 `https://_demo1234.cyberbiz.co_ /zh-TW`，請僅填入 `_demo1234.cyberbiz.co_`。

    - Google Cloud Platform：依您的需求選擇專案。
    - [ ] 點擊「提交」按鈕，您將會取得 Google reCAPTCHA 的「網站金鑰 (sitekey)」與「密鑰 (secretkey)」。

    ![[Google reCAPTCHA 設定欄位.png]]

=== ":material-numeric-3-circle: 複製金鑰"

    複製並妥善保存「網站金鑰」跟「密鑰」，後續將用於[[啟用留言區 reCAPTCHA#步驟二：將 reCAPTCHA 金鑰綁定商品評論區|綁定官網頁面]]。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA03.png){ .screenshot }


### 步驟二：將 reCAPTCHA 金鑰綁定商品評論區 :material-lock-outline:
??? note "商品評論功能僅供 `企業版`、`PLUS 版` 商家使用，如有使用商品評論需求，請洽客服開通功能。了解如何[[使用商品評論功能]]。"

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA04.png){ .screenshot }

=== ":material-numeric-1-circle: 進入操作頁面"
    - [ ] 登入 CYBERBIZ 電商後台，前往「網站外觀」→「管理商品評論」。

=== ":material-numeric-2-circle: 開啟功能"
    - [ ] 點擊 Google reCAPTCHA 開關 :material-toggle-switch:，以開啟功能（ON）。

=== ":material-numeric-3-circle: 貼上金鑰"
    - [ ] reCAPTCHA sitekey：將您在步驟一取得的「網站金鑰」填入此欄位。
    - [ ] reCAPTCHA secretkey：將您在步驟一取得的「密鑰」填入此欄位。

=== ":material-numeric-4-circle: 儲存變更"
    - [ ] 點擊「更新」套用變更。

### 步驟三：將 reCAPTCHA 金鑰綁定聯絡我們頁面
![[EC-會員-顧客回饋-reCAPTCHA 啟用.png]]

=== ":material-numeric-1-circle: 進入操作頁面"
    - [ ] 登入 CYBERBIZ 電商後台，前往「會員」→「顧客回饋 & 建議」。

=== ":material-numeric-2-circle: 開啟功能"
    - [ ] 點擊「啟動機器人阻擋」開關 :material-toggle-switch:，以開啟功能（ON）。

=== ":material-numeric-3-circle: 貼上金鑰"
    - [ ] `sitekey` 將您在步驟一取得的「網站金鑰」填入此欄位。
    - [ ] `secret key` 將您在步驟一取得的「密鑰」填入此欄位。

=== ":material-numeric-4-circle: 儲存變更"
    - [ ] 點擊「儲存所有設定」套用變更。

---

## 常見問題
??? question "一組 Google reCAPTCHA 帳號可以綁定多個網域嗎？"
    是的，一組 Google reCAPTCHA 帳號可以綁定多個網域。您可以使用同一組密鑰綁定商品評論與聯絡我們頁面。

??? question "Google reCAPTCHA 有免費用量配額嗎？"
    Google reCAPTCHA 提供免費用量配額。當達到免費用量上限前，Google 會透過電子郵件通知商家。若超出免費用量，顧客將無法進行留言，請自行向 Google 升級方案。詳情參考 [reCAPTCHA-配額與限制](https://cloud.google.com/recaptcha/quotas?hl=zh-tw)。

??? question "如果金鑰填寫錯誤會怎麼樣？"
    請確保金鑰填寫正確，否則留言功能將無法正常使用。如有錯誤訊息 (如下圖)，請檢查金鑰是否填寫無誤。

    [![reCAPTCHA 金鑰填寫錯誤](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)

??? question "此 reCAPTCHA 功能是否適用於所有版型網站？"
    此功能僅限拖拉版型網站使用。

---

## 延伸閱讀
=== ":material-page-next-outline: 導向連結"
    - [[設定商品評論功能]]
    - [Google reCAPTCH 控制台 :material-open-in-new:](https://www.google.com/recaptcha/admin/)
    - [Google reCAPTCH 功能介紹 :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=zh_tw)
    - [Google reCAPTCH 配額與限制 :material-open-in-new:](https://cloud.google.com/recaptcha/quotas?hl=zh-tw)

=== ":material-page-previous-outline: 引用連結"

=== ":material-update: 相關更新"

=== ":material-book-outline: 相關詞彙"

=== ":material-map-outline: 相關圖表"


[^超出免費 reCAPTCHA 額度]: 達到免費用量上限前，Google 會透過電子郵件通知商家。
[^隱形 reCAPTCHA]: 隱形 reCAPTCHA 可在顧客互動時自動判斷是否為機器人，通常不會打斷顧客操作，僅在系統判斷為可疑時才出現驗證題目。這能同時減少顧客操作干擾，並提升網站防護力。