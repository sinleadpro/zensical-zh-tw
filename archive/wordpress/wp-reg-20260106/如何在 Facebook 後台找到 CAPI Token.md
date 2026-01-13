---
title: "如何在 Facebook 後台找到 CAPI Token"
last_modified: ""
categories: [第三方平台整合>Facebook相關設定]
tags: [#Facebook]
permalink: "https://www.cyberbiz.io/helpcenter/?p=3093"
id: "3093"
---

為了因應擁有許多廣告代理商的您之需求，且欲埋設於 CYBERBIZ 後台的 Pixel（像素）編號非您自己企業管理平台所擁有，您無法透過 FBE2.0
流程選到該組像素自動埋設於官網後台，我們特闢另外一條路給您。

您不管是 FBE2.0 或 走手動貼 CAPI Token 這兩條路，通通都會升級新版 UI，但客戶原本的功能不會變，已經開通 FBE2.0
的客戶也毋須擔心資料會被覆蓋或需要重啟設定。 頁面上所有的基本設定不變（包含 APP 應用程式、APP 應用程式密鑰、Facebook
登入、Facebook 商品評論、Facebook 文章評論、商品圖片選擇方式、產品動態網址、更新產品目錄、FB 商店＆即時客服等等）。

**操作流程**

＊請記住您「目前於 [CYBERBIZ](https://www.cyberbiz.io/support/?p=11704)
後台手動貼上的像素（Pixel）編號」，因為後續需要請您手動貼上該組像素的 CAPI 存取權杖（Token）。  
＊不同的像素會對應到不同的 Token

* 請至您的或廣告代理商之 Facebook 企業管理平台**（若您沒有廣告代理商之 Facebook 企業管理平台權限，您必須請廣告代理商做下列動作）** 後台選擇「資料來源」—>「像素」—>「客戶自己想要埋在 Cyberbiz 後台之該組像素」—> 點選「在事件管理工具開啟」。
![這張圖片的 alt 屬性值為空，它的檔案名稱為
截圖-2021-03-16-上午10.53.13-1024x562.png](https://www.cyberbiz.io/support/wp-content/uploads/2021/03/%E6%88%AA%E5%9C%96-2021-03-16-%E4%B8%8A%E5%8D%8810.53.13-1024x562.png)

* 請點選「您想要埋在 CYBERBIZ 後台之該組像素」—> 點按「設定」。（尚未開啟 CAPI，連結方式會顯示僅由「瀏覽器傳送」）
![這張圖片的 alt 屬性值為空，它的檔案名稱為
截圖-2021-03-16-上午11.15.43-1024x563.png](https://www.cyberbiz.io/support/wp-content/uploads/2021/03/%E6%88%AA%E5%9C%96-2021-03-16-%E4%B8%8A%E5%8D%8811.15.43-1024x563.png)

* 點按「設定」後 —> 滑動到下面「轉換 API」點選「立即開始」的按鈕並作設定。
![這張圖片的 alt 屬性值為空，它的檔案名稱為
截圖-2021-03-16-上午11.21.52-1024x562.png](https://www.cyberbiz.io/support/wp-content/uploads/2021/03/%E6%88%AA%E5%9C%96-2021-03-16-%E4%B8%8A%E5%8D%8811.21.52-1024x562.png)

* 設定完畢後，點選立即開始按鈕下藍色的「產生存取權杖」，並將代碼複製貼於 CYBERBIZ 後台。
![這張圖片的 alt 屬性值為空，它的檔案名稱為
截圖-2021-03-16-下午12.32.21-1024x562.png](https://www.cyberbiz.io/support/wp-content/uploads/2021/03/%E6%88%AA%E5%9C%96-2021-03-16-%E4%B8%8B%E5%8D%8812.32.21-1024x562.png)

* 請貼於 CYBERBIZ 後台畫面此處，並按下儲存設定即可完成 CAPI 開通。  
**後台路徑 : 「第三方整合」→ 「臉書 Facebook 設定(廣告/註冊登入)」 →「CAPI存取權杖(Token)」**

![](https://www.cyberbiz.io/support/wp-content/uploads/image-1024x521.png)

* 開通完畢後，您的「像素/轉換 API」」連結方式就會同步透過瀏覽器、瀏覽器、伺服器傳送。
![這張圖片的 alt 屬性值為空，它的檔案名稱為
截圖-2021-03-16-下午6.47.02-1024x544.png](https://www.cyberbiz.io/support/wp-content/uploads/2021/03/%E6%88%AA%E5%9C%96-2021-03-16-%E4%B8%8B%E5%8D%886.47.02-1024x544.png)

