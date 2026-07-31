---
title: 門市助理安裝與導入
description: 了解門市助理（Store Assistant）的安裝流程與前置設定，包含 LINE 認證、會員註冊規範及門市資料準備，協助商家順利完成 OMO 整合。
created: 2026-06-18 16:00
last_modified: 2026-07-01 12:00
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
  - 門市助理
sites: 
  - TW
audiences: 
  - merchant
difficulty: intermediate
tnb: branch
plans: 
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents: 
  - 安裝門市助理
  - 設定門市助理前置資料
  - 串接 LINE Certified Provider
features: 
  - 門市助理
  - LINE 整合
  - 會員綁定
prerequisites: 
  - "需為企業版方案商家"
  - "需啟用新版 VIP 制度"
related: 
  - "門市助理 – 會員等級"
tags: 
  - 門市助理
  - 安裝導引
  - LINE 認證
  - OMO
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - 我的擴充服務
  - 顧客註冊設定
  - 簡訊通知樣板
paths: 
  - APP MARKET > 我的擴充服務 > 門市助理
  - 管理中心 > 顧客註冊設定
  - 訊息推播 > 簡訊通知樣板
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=41626
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/install-and-setup-storepal/"
search:
  exclude: false
icon: lucide/store
hide: []
---

# 門市助理安裝與導入
了解門市助理（Store Assistant）的安裝流程與前置設定，包含 LINE 認證、會員註冊規範及門市資料準備，協助商家順利完成 OMO 整合。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | 門市助理
{ .doc-badge }

!!! tip "應用情境"
	- **OMO 會員整合**：透過門市助理 QR Code，讓顧客在門市一次完成加入 LINE 好友、官網註冊與推薦人綁定。
	- **門市業績追蹤**：將官網會員歸戶至特定門市或人員，精準計算門市貢獻度。
	- **即時數位服務**：門市人員可透過行動裝置查看會員資產，提供個人化服務。


## 使用須知

- **申請方式**：若您尚未購買門市助理服務，請聯繫您的 CYBERBIZ 客服顧問或填寫[申請表單](https://docs.google.com/forms/d/e/1FAIpQLScAzqU3OckpsS-XBy3yvioKksDBazronFTuEl_RBonxCATHaQ/viewform)。
- **系統限制**：門市助理僅支援 **新版 VIP 制度**，舊版 VIP 商家不適用。
- **LINE 認證建議**：強烈建議申請 **LINE Certified Provider**。具備此認證後，顧客掃碼可直接觸發 LIFF 網址，大幅簡化註冊與綁定流程。
- **簡訊提醒**：啟用手機驗證功能將發送簡訊。



## 操作流程

### 步驟一：確認安裝狀態

完成購買後，CYBERBIZ 顧問團隊將協助初始安裝。

1. 登入 CYBERBIZ 管理後台，前往 **APP MARKET > 我的擴充服務**。
2. 確認 **門市助理** 已顯示於已安裝清單中。
3. 點擊 **設定**，即可進入專屬管理介面。

	![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置01.png){ .screenshot }

### 步驟二：LINE 前置設定

為確保掃碼綁定流程順暢，需完成 LINE 相關認證與連動。

1. **LINE 開發者設定**：前往 [LINE Developers](https://developers.line.biz/)，確保 LINE OA 與 LINE Login Channel 已完成連動。
2. **啟用 LINE 快速登入**：於管理後台 **第三方整合 > LINE 註冊登入** 完成 [快速登入設定]()。
3. **官方帳號認證**：LINE 官方帳號認證官方帳號已完成認證為藍盾或綠盾。
    - [LINE認證官方帳號說明文件](https://tw.linebiz.com/column/line-lac-id-0418/)
4. **申請LINE Certified Provider 認證**：可洽詢您配合的 [LINE合作夥伴](https://tw.linebiz.com/partner/sales-partner/)，或依照下方文件流程，進行認證申請 [申請檔案下載](https://drive.google.com/file/d/1S2OoIPlmlwzyqE3h1vQldLXrcgf1sCO5/view?usp=sharing)。
  - **按照 LINE 規範，一間公司僅能申請一個 Certified Provider。若有重覆將無法申請通過。**
5. 若商家已取得 LINE Certified Provider 認證，請開啟 **自動產生LIFF網址**。  
  - **使用情境**：後續會員進行門市助理註冊綁定時，可透過 QRCODE 完成加入 LINE 官方帳號好友、官網註冊以及門市助理推薦人綁定。  
  - **操作路徑**：第三方整合 > LINE 註冊登入。
      ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置05.png)
  - **注意事項**：**若商家尚未取得 LINE Certified Provider 認證，先不要開啟 「自動產生LIFF連結」。**  
      無「自動產生LIFF連結」功能時，會員進行門市助理註冊綁定，會先以 QRCODE 加入 LINE官方帳號好友，並請引導會員進入手機驗證頁面、取得手機號碼，完成官網註冊以及門市助理推薦人綁定。



### 步驟三：會員註冊設定

門市助理需仰賴手機號碼作為會員唯一識別碼。

1. 前往 **管理中心 > 顧客註冊設定**。
2. **註冊規範**：將「註冊方式」設定為 **快速結帳並註冊**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置04.png){ .screenshot }

3. **手機驗證**：在手機欄位勾選 **必填**、**驗證** 及 **註冊時驗證電話**。

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置02.png){ .screenshot }

### 步驟四：簡訊通知設定

確保會員能順利接收註冊驗證碼。

1. 前往 **訊息推播 > 簡訊通知樣板**。
2. 在「顧客相關」類別中，開啟 **顧客請求發送驗證碼通知**。

	  ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-安裝與前期資料設置03-1.png){ .screenshot }


## 資料準備

門市助理帳號以一間門市為單位申請，開通帳號時會請商家提供以下資訊，由 CYBERBIZ 預先建立門市與群組，後續若需要更改，可至門市助理後台編輯。

| 類別 | 資訊 | 備註 |
| :--- | :--- | :--- |
| **門市資訊** | **門市名稱** | 名稱不可重複<br>此名稱會影響會員綁定時顯示的門市名稱 |
| **群組資訊** | **群組名稱** | 名稱不可重複<br>此名稱會影響會員綁定時顯示的群組名稱 |
|  | **門市歸屬** | 每個門市僅能隸屬於一個群組 |

  

