---
title: "Google Tag Manager 教學"
last_modified: ""
categories: [第三方平台整合>Google相關設定]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=689"
id: "689"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png)
![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**看完此文件，您可以：**  

* 初步了解 Google Tag Manager。
* 建立 Google Tag Manager 帳戶。
* 將 Google Tag Manager 代碼綁定官網後台。

**操作目錄：**

* 什麼是 Google Tag Manager
* 如何建立 GMC 帳戶並串接官網後台

注意事項:  

* 此教學文件僅為協助參考之用，實際操作與設定方式請以 Google 官方資訊為準。若有疑問，請洽詢 Google 官方支援。

## 📌 什麼是 Google Tag Manager


Google Tag Manager（GTM） 是 Google
提供的一套免費標籤管理系統，專門用來協助網站管理者、行銷人員，在不需直接修改網站程式碼的情況下，快速安裝、管理、更新各種追蹤代碼（標籤）。  

這些追蹤代碼（標籤）通常包括：

* 網站分析工具
* 廣告轉換追蹤
* 再行銷代碼
* 事件追蹤（如點擊按鈕、滑動頁面、填寫表單）
➔ 在沒有 GTM 的情況下，每次需要新增、修改、或刪除這些追蹤設定，通常都需要請工程師協助進行網站原始碼調整。  
➔ 而使用 GTM，只需在網站上安裝一次 GTM 代碼，後續所有追蹤需求，都可以在 GTM 的後台進行設定與調整，大幅提升彈性與管理效率。  

**請注意！以下工具已由 CYBERBIZ 系統建置專屬串接方式。請商家務必依照後台提供的設定路徑進行串接** ，請勿另行使用 GTM
綁定，以確保資料紀錄的正確性。串接工具列表與教學連結如下：

* [Google Analytics](https://www.cyberbiz.io/helpcenter/?p=678)
* [Google Ads 轉換追蹤](https://www.cyberbiz.io/helpcenter/?p=756)
* [Meta Pixel](https://www.cyberbiz.io/helpcenter/?p=2870)

## 📌 如何建立 GMC 帳戶並串接官網後台



1. 登入 [Google Tag Manager](https://tagmanager.google.com)，點擊「建立帳戶」。
![Google Tag Manager 教學](https://www.cyberbiz.io/support/wp-content/uploads/Google-Tag-Manager-教學01.png)

2. 於「帳戶設定」輸入帳戶名稱，選擇國家/地區。  

* 帳戶是最上層的管理單位，通常對應到一家公司或品牌。帳戶底下主要管理多個網站或應用程式（即容器），不會影響實際追蹤功能。
* 商家可使用您的公司名稱或品牌名稱來命名帳戶。

於「容器設定」輸入容器名稱，選擇「網路」。  

* 容器是指實際要裝載追蹤標籤（Tag）的地方，通常對應到一個網站或應用程式。容器內可以設定所有想要安裝的追蹤工具。
* 商家可使用對應的官網網址或平台名稱來命名容器。
![Google Tag Manager 教學](https://www.cyberbiz.io/support/wp-content/uploads/Google-Tag-Manager-教學02.png)

3. 同意服務條款，點選「是」。
![Google Tag Manager 教學](https://www.cyberbiz.io/support/wp-content/uploads/Google-Tag-Manager-教學03.png)

4. 取得程式碼資訊，請找到 GTM 代碼並複製。
![Google Tag Manager 教學](https://www.cyberbiz.io/support/wp-content/uploads/Google-Tag-Manager-教學04.png)

5. 進入官網後台，找到「Google Tag Manager」區域，將 GTM 代碼貼至「追蹤編號含GTM」欄位。  
後台路徑 :  「第三方整合」→「谷歌Google設定」  

![Google Tag Manager 教學](https://www.cyberbiz.io/support/wp-content/uploads/Google-Tag-Manager-教學05.png)

