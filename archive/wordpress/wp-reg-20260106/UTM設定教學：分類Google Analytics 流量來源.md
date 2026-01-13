---
title: "UTM設定教學：分類Google Analytics 流量來源"
last_modified: ""
categories: [第三方平台整合>Google相關設定]
tags: [GA,UTM]
permalink: "https://www.cyberbiz.io/helpcenter/?p=5156"
id: "5156"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png)
![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**看了此文件，您可以：**  

* 了解 UTM 是什麼，以及它如何幫助網站追蹤流量來源與行銷成效。
* 熟悉 UTM 各參數的功能與正確使用格式。
* 使用工具 Campaign URL Builder 快速產生可追蹤的 UTM 連結。
* 將產生的 UTM 應用於廣告、社群或 EDM 等連結中。
* 在 GA4 中查看 UTM 數據與來源媒介報表，分析各渠道成效與使用者行為。

**操作目錄：**

* 什麼是 UTM
* UTM 網址結構與參數介紹
* UTM 參數格式與使用技巧
* UTM 設定工具：Campaign URL Builder
* 於 GA4 中追蹤 UTM 數據

注意事項:  

* 此教學文件僅提供參考，詳細操作與最新後台畫面以 Google 官方為主。
* GA4 偵測到使用者行為後，需要時間進行資料收集與處理，**資料更新間隔為 24~48 小時不等** 。詳情可參考 [Google 官方文件：[GA4]資料更新間隔](https://support.google.com/analytics/answer/11198161)。



## 📌 什麼是 UTM


UTM（Urchin Tracking Module） 是一種用來在網址上標記來源資訊的小型參數。它能幫助網站分析工具（如 Google
Analytics）準確記錄使用者從哪個廣告、活動或媒介進入網站，是建立跨平台行銷成效分析、流量來源歸因的重要工具。以下為常見使用情境：  

使用情境 | 實際效果  
---|---  
**提升流量歸因準確性** | 將不同廣告、社群、EDM、聯盟行銷來源正確分類。  
**比較各渠道成效** | 分析 Facebook、LINE、Google、Email 各自帶來的點擊量、轉換數。  
**支援A/B測試** | 清楚比較不同廣告素材、文案版本的效果差異。  
**提升資料治理與報表自動化能力** | 配合統一命名規則，可搭配 GA4製作標準化成效報表。  

* * *

## 📌 UTM 網址結構與參數介紹


UTM 會附加在連結網址後，看起來格式如下：  
`https://www.example.com/``?utm_source=facebook&utm;_medium=social`常用參數欄位與對應功能：  
參數 | 功能說明 | 舉例  
---|---|---  
`utm_source` | 流量來源（如平台/網站） | facebook、google、newsletter  
`utm_medium` | 流量媒介（如廣告形式） | social、email  
`utm_campaign` | 行銷活動名稱 | summer_sale、blackfriday  
`utm_term` | 關鍵字 | shoes、new_arrival  
`utm_content` | 內容細節（可用於A/B版本區分） | banner1、textlink_b  

* * *

## 📌 UTM 參數格式與使用技巧



1. **參數英文大小寫一致** ：若出現 Facebook / facebook ，GA4 會分開統計。
2. **避免空格與特殊符號** ：以底線或短橫線代替空格，例如 summer_sale。
3. **使用英文與標準縮寫** ：避免中文參數亂碼或影響資料解析。
4. **建立 UTM 命名表** ：統一團隊內命名規則，便於資料整理與分析。

* * *

## 📌 UTM 設定工具：Campaign URL Builder


Campaign URL Builder 是 Google 提供的線上 UTM 生成器，當您輸入各欄位後，可自動產生可追蹤的連結。  


1. 進入 [Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/)，貼上想進行 UTM 追蹤的網址，依需求填入參數名稱。  
[![設定utm](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學02.png)](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學02.png)

2. 下方會即時生成含有 UTM 參數的網址。  
[![設定utm](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學03.png)](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學03.png)

* * *

## 📌 於 GA4 中追蹤 UTM 數據



1. 登入 [GA4](https://analytics.google.com/analytics/web/)，於側邊欄點選 「報表」→「業務目標」→「產生待開發客戶」→「流量開發」，選擇「工作階段來源/媒介」報表。 
* 請先確定完成 [ GA4 與官網的串接](https://www.cyberbiz.io/helpcenter/?p=678)，方可於 GA4 查看官網流量資訊。
[![設定utm](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學04.png)](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學04.png)



2. 可於報表中查看網站流量來源類型、使用者行為與 UTM 參數數據。  
[![設定utm](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學05.png)](https://www.cyberbiz.io/support/wp-content/uploads/UTM設定教學05.png)

* * *

