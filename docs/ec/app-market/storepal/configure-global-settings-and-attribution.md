---
title: 全站功能與業績歸因設定
description: 協助總部管理者配置全品牌統一的門市助理功能開關，並引導各級管理員設定個別門市的業績歸因層級。
created: 2026-06-22  10:11
last_modified: 2026-06-22 10:11
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
  - 專業PLUS
  - 進階PLUS
  - 高手PLUS
  - 企業
cyb_extensions: []
intents:
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
  - 業績歸因
acoiv: configure
apis: []
devices: []
ui_components:
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
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/configure-global-settings-and-attribution/"
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---
# 全站功能與業績歸因設定
協助總部管理者配置全品牌統一的門市助理功能開關，並引導各級管理員設定個別門市的業績歸因層級。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | 門市助理
{ .doc-badge }

## 全站設定

**總部管理員** 可設置全門市規則。

### 前台功能開關

前往 **設定 > 功能設定 > 前台功能設定**，開啟或關閉 **門市助理前台** 各項功能。

* 優惠券

    若點選開啟，全品牌門市人員可在前台介面查看及使用優惠券區塊。  

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定17.png){ .screenshot }



* 全館優惠券

    若點選開啟，全品牌門市人員可在前台介面查看及使用全館優惠券區塊。  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定25.png){ .screenshot }



* 紅利點數

    分成「顯示紅利點數」和「使用紅利點數」。若點選開啟，全品牌門市人員可在前台介面查看或使用紅利點數區塊。  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定18.png){ .screenshot }



* 推薦商品
    
    若點選開啟，全品牌門市人員可在前台介面使用推薦商品功能。  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定19.png){ .screenshot }



* 業績報表

    若點選開啟，全品牌門市人員可在前台介面查看到該門市業績概況報表。  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定20.png){ .screenshot }



* 會員標籤  

    - **指定呈現會員標籤**

        若點選開啟，總部管理者可以選擇至多10指定會員標籤於門市助理前台；當會員在EC後台被設置符合的指定標籤時，全品牌門市人員可在前台查看其會員指定標籤。

    - **門市標籤設定** 

        * 開啟後，自訂的門市標籤將會顯示於門市助理前台，同時也要確認要開放使用的門市在 **角色與權限的設定頁面** 上有要開啟使用。
        * 當門市人員在前台的會員資訊頁面點選標籤後，全品牌的門市人員皆可以在前台查看該會員的標籤，同時也可以在 EC 的會員頁面上查看線下標籤。
        * 至多可設定 5 個標籤群組，每個標籤群組內至多可設定 10 個標籤。

    ![會員標籤](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定21.png){ .screenshot }

### 全站業績認列規則

前往 **設定 > 功能設定 > 業績歸因設定**，設定 **全品牌業績認列** 規則。

- 歸因有效期限

    依商家營運需求訂定綁定歸因有效期限；在期間內，會員自主於官方網站下的有效訂單，會自動歸因至綁定的門市或門市店員身上。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定22.png){ .screenshot }


- 推薦商品認列對象

    決定 **透過推薦連結成立的訂單** 的業績認列對象：

    - 綁定門市推薦人
    - 商品推薦人

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定23.png){ .screenshot }

!!! warning "修改限制"
    商家僅能自行修改業績歸因欄位 **1 次**。若需多次更改，請聯繫 CYBERBIZ 客服。

### 簡訊通知開關

前往 **設定 > 通知設定**，開啟或關閉 **通知類型** ，並編輯簡訊模板。

#### 簡訊通知類型

- 註冊通知 ：系統預設開啟，恕無法關閉
- 帳號啟用通知 ：系統預設開啟，恕無法關閉
- 門市推薦人綁定通知
- 商品推薦通知：同步做為 **發送簡訊** 的簡訊模板與 **分享商品連結** 的連結模板。

啟用通知後，門市人員即可發送該類型簡訊給顧客。  

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-設定-通知設定-簡訊列表01.png){ .screenshot }

#### 編輯簡訊模板

1. 點擊各通知類型的標題即可進入編輯頁面，自定義簡訊模板內容。
2. 在文字編輯區輸入您想要的簡訊內容，可自由調整文案語氣與風格。
3. 點擊 **儲存** 按鈕，立即套用至新發送的簡訊。
4. 如需還原，可使用 **還原初始樣板** 功能。

!!! warning "系統預設參數編輯限制"
    {{...}}為系統預設參數，您可移動參數位置或選擇刪除，但 **不可修改參數名稱內容**。

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-設定-通知設定-編輯簡訊模板01.png){ .screenshot }

### 查看操作紀錄

總部管理者可監控所有人員的登入紀錄與操作行為，確保營運安全性。

1. 前往 **設定 > 操作紀錄**。
2. 系統將列出包含群組管理者、門市店長及店員的登入紀錄與執行動作。

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-設定-操作紀錄-查看操作紀錄01.png){ .screenshot }

## 管理門市

### 設定門市業績歸因

門市管理列表會依角色權限顯示對應可設定的門市：

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定02.png){ .screenshot }

| 角色權限 | 顯示門市 |
| -------- | ------- |
| 總部管理者 | 旗下所有門市 | 
| 群組管理者 | 該帳號所屬群組範圍內的門市 |
| 門市店長 | 該帳號所屬的指定單一門市 |
| 門市店員 | 無 |




1. 在門市頁面的 **門市業績歸因設定** 區塊，選擇歸因層級（門市/店員）。
    - 當歸因至門市層級，店員業績將合併計算至門市層級（店績）。
    - 當歸因至店員層級，業績將依不同門市人員帳號分別計算（個績）。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定03.png){ .screenshot }

2. 點選 **儲存** 完成設定。



!!! warning "歸因層級修改限制"
    商家可自行修改歸因層級 1次，若需多次更改，請聯繫 CYBERBIZ 客服。