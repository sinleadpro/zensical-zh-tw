---
title: 門市助理績效報表
description: 了解門市助理提供的推薦人報表與業績歸因報表，掌握線下會員綁定狀況與全通路業績歸因數據。
created: 2026-06-22 11:15
last_modified: 2026-06-22 11:15
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
cyb_extensions: 
  - STORE PAL
intents: 
  - 查看門市業績報表
  - 分析店員綁定成效
  - 掌握全通路業績歸因
features: 
  - 門市助理
  - 績效報表
  - 業績歸因
  - 推薦人綁定
prerequisites:
  - "ec/app-market/storepal/install-and-setup-storepal"
related:
  - "[功能與帳號設定]"
  - "ec/app-market/storepal/bulk-import-customer-referrers"
tags: 
  - 門市助理
  - 績效報表
  - 業績歸因
  - OMO
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 績效報表
  - 推薦人報表
  - 業績歸因報表
paths: 
  - 門市助理後台 > 績效報表
  - 門市助理後台 > 門市管理 > 匯出報表
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=41036
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/performance-reports/"
comments: false
search:
  exclude: false
icon: lucide/bar-chart-3
hide: []
---
# 門市助理績效報表
了解門市助理提供的推薦人報表與業績歸因報表，掌握線下會員綁定狀況與全通路業績歸因數據。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | 所有 PLUS / 企業
[:lucide-grid-2x2-plus:{ title="適用擴充" }](../../resources/conventions#適用擴充) | 門市助理
{ .doc-badge }

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表01.png){ .hero-page }


## 功能說明

- 門市助理提供以下兩種績效報表，供品牌查閱在線下通路收集會員的消費紀錄及離店後所帶來的線上業績，並可根據數據輪廓，對會員作進一步的推波、導購與促銷。



## 推薦人報表


品牌能透過推薦人報表了解 **各門市的綁定狀況** 和 **會員與門市人員的綁定關係**。


- **推薦人綁定總覽**：依門市顯示所有門市人員的總綁定會員數。
- **綁定會員的詳細資料**：依門市人員顯示所有與其有綁定關係的會員。
    - 綁定店員、姓名、手機號碼、email、綁定時間以及綁定類型。
![推薦人報表](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表02.png)

> 報表內容將視綁定歸因層級，呈現方式略有不同。


## 業績歸因報表


品牌能透過業績歸因報表，掌握綁定推薦人後的全通路的業績表現狀況，此報表共會產出四個工作表：  


1. **門市業績**

    全門市所有店員的業績加總，分為線上線下總業績、門市實體業績、官網業績總額，分別列出金額與所佔比例。 

    - **官網業績總額** 可分為 **官網消費歸因** 以及 **推薦商品歸因**，協助區分官網導購績效。
        -  **官網消費歸因**：綁定有效期間內，會員自主於官方網站上的消費金額歸因。
        -  **推薦商品歸因**：指定期間內，透過推薦商品連結產生的消費金額歸因。
  
    ![業績歸因報表-門市業績](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表03.png)



2. **個人業績**

    店員個別的業績，分為線上線下總業績、門市實體業績、官網總業績，分別列出金額與所佔比例。  

    !!! warning "資料顯示限制"
        本報表僅在「業績歸因層級」設定為 **店員** 時才會顯示數據。若歸因層級設定為門市，則將無資料。

 
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表04.png)



3. **EC 導購報表（線上）**

    綁定會員於可以有效歸因的線上消費之紀錄，將列出業績歸因層級、歸因類型、歸因對象、消費會員、訂單總額、訂單編號、訂單日期。  


    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表05.png)



4. **EC 導購報表（線下）**

    店員於線下手動輸入的門市消費，將列出操作人、消費會員、輸入日期、輸入金額、業績歸因層級。  

    !!! warning "資料顯示限制"
        本報表僅在「業績歸因層級」設定為 **店員** 時才會顯示數據。若歸因層級設定為門市，則將無資料。
  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表06.png)


## 門市報表

### 角色權限

根據身分可選擇匯出的資料範圍會有不同： 

- 總部管理者：可匯出所有門市，或選擇特定群組、特定門市
- 群組管理者：可匯出所屬群組內所有門市，或選擇所屬群組內特定門市
- 店長：僅能匯出所屬門市


### 所有門市報表

1. 登入門市助理後台，前往 **績效報表 > 推薦人報表/業績報表**。
2. 選擇要匯出的報表，點擊 **匯出**。  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表07.png)

3. 選擇時間區間。若選擇 **指定門市群組**，需繼續選擇特定群組或門市。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表08.png)



### 指定門市報表

1. 登入門市助理後台，前往 **門市管理 > 匯出報表**。
2. 選擇要匯出的報表，點擊 **匯出**。  
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表09.png)

3. 選擇時間區間。
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-業績報表10.png)