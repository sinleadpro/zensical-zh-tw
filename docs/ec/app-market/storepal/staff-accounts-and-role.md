---
title: 員工帳號與角色
description: 了解如何設定門市助理後台的基本功能、帳號權限、業績歸因原則，以及管理門市人員帳號與專屬 QR Code。
created: 2026-05-08 10:11
last_modified: 2026-06-18 10:11
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - EC
modules: 
  - APP MARKET
  - 門市助理
sites: 
  - TW
audiences: 
  - admin
difficulty: intermediate
tnb: branch
plans: 
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
cyb_extensions: []
intents:
  - 設定門市助理帳號權限
  - 建立門市人員帳號
  - 設定業績歸因規則
  - 編輯簡訊通知模板
features: 
  - 門市助理
  - 權限管理
  - 業績歸因
  - QR_Code
prerequisites: []
related: []
tags: 
  - 門市助理
  - 帳號設定
  - 權限管理
  - 業績歸因
acoiv: configure
apis: []
devices: []
ui_components: 
  - 門市角色與權限
  - 新增門市人員帳號
  - 專屬綁定 QRcode
  - 前台功能設定
  - 業績歸因設定
  - 通知設定
paths: 
  - 門市管理 > 特定門市
  - 設定 > 功能設定 > 前台功能設定
  - 設定 > 功能設定 > 業績歸因設定
  - 設定 > 通知設定
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=40979
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---

# 員工帳號與角色
門市助理讓您管理門市業績歸因、帳號權限及人員帳號，協助商家建構完整的門市營運體系。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
[:lucide-grid-2x2-plus: { title="適用擴充" }](../../resources/conventions#適用擴充) | 門市助理
{ .doc-badge }


!!! tip "應用情境"
	- **權限控管**：根據總部、區域或門市等不同層級，指派對應的管理權限，確保資料安全性。
	- **業績歸因**：設定業績歸屬於門市或個別店員，作為後續發放獎金或評估績效的依據。
	- **數位綁定**：透過店員專屬 QR Code，讓顧客在加入 LINE 好友時同步完成會員註冊與推薦人綁定。


## 使用須知

- 門市助理為付費擴充功能，需聯繫 CYBERBIZ 客服付費開通。
- 每間門市僅能有一位 **啟用中** 的店長，新增店長前須先停權舊有店長帳號。
- 已啟用的帳號無法刪除，僅能透過 **停權** 方式停止使用。
- 建議具備 LINE Certified Provider 資格，以實現 QR Code 一次性完成註冊與綁定。

## 角色登入權限說明

門市助理提供四種角色，各角色的登入權限如下表：

| 角色名稱 | 登入後台 | 登入前台 | 說明 |
| :--- | :---: | :---: | :--- |
| **總部管理者** | V | | 於後台管理全品牌門市 |
| **群組管理者** | V | | 於後台管理所屬群組內的門市 |
| **門市店長** | V | V | 於後台管理所屬門市並執行前台操作 |
| **門市店員** | | V | 僅執行前台會員服務與導購 |


## 管理帳號

### 管理角色階層授權表

| **帳號權限 \ 可建立的角色** | 總部管理者角色 | 群組管理者角色 | 門市店長角色 | 門市店員角色 | 
| ------------------------- | --------- | --------- | ------- | -------- |
| **總部管理者權限** | V | V | V | V |
| **群組管理者權限** |  | V | V | V |
| **門市店長權限** |  |  |  | V |
| **門市店員權限** |  |  |  |  | 

### 建立管理者角色

1. 前往 **設定 > 管理帳號設定**。
2. 點選 **新增管理帳號**，設定帳號、密碼並指派角色。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定13.png){ .screenshot }

    - 若角色為 **群組管理者**，需進一步選擇其負責的門市群組。
    - 角色一旦新增，可以編輯人員身份、名稱，但無法更改信箱。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-後台-門市管理-門市人員帳號-新增管理者帳號01.png){ .screenshot }
        


### 建立門市人員

1. 前往 **門市管理**，系統將自動顯示該角色權限下的門市列表。
2. 點選 **[特定門市]**，進入該店管理頁面。
3. 點選 **門市人員帳號** 頁籤，點擊 **新增門市人員帳號**。

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定05.png){ .screenshot }

### 管理門市人員

1. **編輯**
    可以編輯人員身份、名稱，但無法更改信箱。
2. **停權**
    門市人員遭停權後，將無法登入。
3. **使用專屬綁定 QR Code**
    - **操作方式**：點擊 **下載** 儲存 QR Code 圖檔，或點擊 **複製** 取得專屬綁定連結。
    - **使用情境**：店員於門市現場引導顧客掃碼，讓顧客在註冊會員的同時自動完成店員綁定。


![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定09.png){ .screenshot }


#### 批次建立

使用 Excel 批次建立或修改全品牌門市人員帳號。

1. 前往 **門市管理**，點選 **匯入 > 人員帳號與修改權限**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員01.png){ .screenshot }

2. 點選 **下載 Excel 範本**，填寫資料後點選 **上傳檔案**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員02.png){ .screenshot }

3. 可於 **上傳作業進度** 查看上傳紀錄。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員03.png){ .screenshot }


!!! warning "匯入時注意事項"
    - 請勿修改 Excel 表頭名稱。
    - 所屬門市：僅接受已存在且啟用中的門市。
    - 角色：請輸入「店長」或「店員」。
    - 姓名：不可空白。
    - 信箱：不可空白，同門市同角色信箱不可重複。
    - 密碼：請輸入6碼以上。

#### 批次編輯店員權限

若您需要管理多家門市的店員與權限設定，可透過 Excel 批次修改角色權限，大幅提升設定效率。  

1. 點擊 **匯出** 按鈕，系統將寄出 Excel 檔至您的登入 Email。  

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員04.png){ .screenshot }

2. 開啟下載的檔案，調整各門市的權限勾選設定（開啟/關閉）。  

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員05.png){ .screenshot }

3. 回到 **門市管理** 畫面，點選 **匯入 > 人員帳號與修改權限**。  

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員01.png){ .screenshot }

4. 點擊 **上傳檔案**，選擇 **角色與權限**。  

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員06.png){ .screenshot }

5. 選擇已修改的檔案，點擊 **確認**。


6. 可於「上傳作業進度」查看上傳紀錄。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員03.png){ .screenshot }

### 設定角色權限

商家可依經營需求，對每間門市的店長、店員角色設定不同的功能權限。

 
- 會員基本資訊 

    開啟後，帳號角色將能於會員資訊頁輯編輯 **會員基本資訊**。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-1.png){ .screenshot }

* 會員備註
    
    開啟後，帳號角色將能於會員註記編輯「會員備註」  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-2.png){ .screenshot }

* 門市標籤

    開啟後，帳號角色將能於會員註記編輯「門市標籤」  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-5.png){ .screenshot }

* 優惠券核銷
    
    開啟後，帳號角色將能於會員資訊頁內使用優惠券  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-3.png){ .screenshot }

* 輸入門市消費
    
    開啟後，帳號角色將在會員功能中看到「新增門市消費」功能按鈕  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-4.png){ .screenshot }



## 常見問題

??? quote "為什麼無法新增第二位店長？"
    每間門市僅能有一位啟用中的店長。若需更換店長，請先將原店長帳號狀態改為「停權」，即可新增新店長。

??? quote "店員帳號可以刪除嗎？"
    為了保留歷史操作紀錄與業績數據，系統不開放刪除帳號。若人員離職，請使用「停權」功能。

??? quote "如何查看人員的操作紀錄？"
    總部管理者可前往 **設定 > 操作紀錄**，查看所有人員的登入紀錄與前後台執行動作。

## 延伸閱讀

- [門市助理 - 註冊與綁定官網會員](註冊與綁定官網會員.md)
- [門市助理 - 查看門市與個人業績](查看門市與個人業績.md)
- [門市助理 - 商品推薦](商品推薦.md)
