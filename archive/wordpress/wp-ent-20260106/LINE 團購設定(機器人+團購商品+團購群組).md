---
title: "LINE 團購設定(機器人+團購商品+團購群組)"
last_modified: ""
categories: [第三方整合>LINE相關設定]
tags: [LINE團購]
permalink: "https://www.cyberbiz.io/support/?p=29174"
id: "29174"
---

此功能需依序完成下方三個教學文件 [![機器人主視覺](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人.png)](https://www.cyberbiz.io/support/?p=29174&page=2)
[![團購主視覺](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品.png)](https://www.cyberbiz.io/support/?p=29174&page=3)
[![商品主視覺](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-商品群組.png)](https://www.cyberbiz.io/support/?p=29174&page=4)
![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購分頁圖-1024x193.png)
![](https://www.cyberbiz.io/support/wp-content/uploads/企業版.png) LINE團購設定 -
機器人設定  

**功能說明：**  

* LINE團購功能將協助您在LINE群組內進行團購活動，在您或團購主將設定完成的團購機器人加入群組內之後，群組成員即可流暢的進行購物活動。
* LINE團購功能亦協助引導群組成員加入您的品牌官方帳號好友。
* 團購機器人設定為LINE團購功能的基礎設定。
**操作目錄：**

* Messaging API設定(團購機器人專用)
* 機器人選單設定
* LIFF 設定
* 操作影片
注意事項:  

* 此功能僅能在LINE群組/多人聊天室上使用，因LINE社群(OpenChat)為匿名性故不可使用。
* 建議您將原本的品牌 LINE官方帳號與團購機器人 LINE官方帳號分開建立，以避免干擾原品牌官方帳號使用messaging API的相關功能。
* 建立團購機器人LINE官方帳號時，請選擇與您品牌LINE官方帳號相同的服務提供者(LINE Provider)，如此一來LINE用戶資料便可在兩個官方帳號間流通，請參考架構如下。 [![機器人設定01](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定01.jpg)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定01.jpg)

Messaging API設定(團購機器人專用)

1. 進入[LINE OA Manager ](https://account.line.biz/login?redirectUri=https%3A%2F%2Fmanager.line.biz%2F)後台，創建一個專屬團購用的LINE官方帳號。  
請依照下方步驟建立

[![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定02.png) [![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定03.png) [![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定04.png) [![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定05.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定05.png)

2. 於 LINE OA Manager管理畫面點選右上「設定」  
[![機器人設定06](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定06.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定06.png)



3. 左側欄選單點選「帳號設定」，在最上方「功能切換 ─ 加入群組或多人聊天室」設定為「接受邀請加入群組或多人聊天室」  
[![機器人設定07](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定07.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定07.png)



4. 左側欄選單點選「回應設定」，確認設定如下：  
【回應模式】 : 聊天機器人  
【加入好友的歡迎訊息】: 停用  
【自動回應訊息】 : 停用  
[![機器人設定08](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定08.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定08.png)



5. . 左側欄選單點選「Messaging API」，點選「啟用Messaging API」  
[![機器人設定09](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定09.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定09.png) ![](https://www.cyberbiz.io/support/wp-content/uploads/fountain-pen.png)

* 若您所服務的品牌商家已建立服務提供者(LINE Provider)，請選擇貴司原本的服務提供者(LINE Provider)，如此一來消費者身分便可在團購機器人官方帳號及品牌官方帳號間流通。若您從未建立過服務提供者(LINE Provider)，可於此建立。
[![機器人設定10](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定10.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定10.png)



6. 啟用Messaging API後，請將 Channel 資訊複製至 CYBERBIZ 後台，複製 CYBERBIZ 提供的 Webhook網址，貼回 LINE Official Account Manager ，(依圖中步驟執行)  
以上設定完成後點選「LINE Developers」進入LINE Developer後台。  
後台路徑 : 「第三方整合」→「LINE團購機器人設定」  
[![機器人設定11](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定11.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定11.png)



7. 進入LINE Provider後台，點選貴司使用的LINE Provider。  
[![機器人設定12](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定12.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定12.png)



8. 進入該 Provider 管理畫面，找到您剛啟用的Messaging API(名稱為您的團購機器人官方帳號)，點選進入。  
[![機器人設定13](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定13.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定13.png)



9. 進入「Messaging API」頁籤，向下滑確認以下設定：   
【Use webhook】 : 開關開啟。(請至 CYBERBIZ 後台複製 Webhook 貼至此)  
【Channel access token(long-lived)】點選「Issue」，複製該串token至 CYBERBIZ
後台，確認無誤後點選「儲存設定」。  
後台路徑 : 「第三方整合」→「LINE團購機器人設定」  
[![機器人設定13](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定15.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定15.png)  
[![機器人設定13](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定16.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定16.png)



* * *

機器人選單設定

* 若您已有經營中的品牌LINE官方帳號，請填入您的帳號ID於此欄位，在LINE團購情境中，我們會協助引導LINE用戶加入該官方帳號好友，協助您經營更多會員。  
(「加入好友」在LINE團購情境的曝光：(1)主選單 (2)訂單完成頁 (3)感謝下單訊息)
[![機器人設定19](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定19.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定19.png)



* * *

LIFF 設定

1. 進入[LINE Provider](https://developers.line.biz/console/)管理後台，點選您的LINE Provider進入管理畫面，點選「+Create a new channel」，選擇「LINE Login」 [![機器人設定20](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定20.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定20.png)



2. 進入Create a new channel設定，請確認設定欄位如下：   
【Region】：Taiwan  
【Company or owner’s country or region】：Taiwan  
[![機器人設定22](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定22.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定22.png)




3. 進入該Login Channel，進入「Basic settings」頁籤，滑至最下方「OpenID Connect」下的「Email address permission」點選「Apply」  
勾選以下欄位，上傳貴司隱私權條款截圖畫面，點選「Submit」
[![機器人設定25](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定23.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定23.png)  




4. 進入**「LIFF」頁籤** ，點選「Add」進行LIFF設定  
[![機器人設定25](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定25.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定25.png)  

* 【LIFF app name】: 自訂名稱
* 【Size】 : 選擇「Tall」
* 【Endpoint URL】 : [商家domain]/liff
[![機器人設定26](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定26.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定26.png)  

* 【Scopes】：全選  
***記得將 view all 裡面的 chat_message.write 打開。**  
[![機器人設定26](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定27.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定27.png)

5. 進入**「Basic settings」頁籤** ，下方找 Linked OA ，設定團購機器人官方帳號。  
【Linked OA】：選擇您的團購機器人官方帳號，點選「Update」。  
[![機器人設定28](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定28.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定28.png)



6. 完成以上設定後，至最下方點選「Back」，回到LIFF列表。  
[![機器人設定29](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定29.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定29.png)



7. 並將LIFF ID以及LIFF URL貼至CYBERBIZ後台。  
[![機器人設定30](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定30.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定30.png) [![機器人設定31](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定31.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定31.png)



8. 完成後回到 LINE Developers 點選「Developing」讓狀態變成「Published」，即正式發布。  
[![機器人設定32](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定32.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-機器人設定32.png)

* * *

操作影片  


* * *

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購分頁圖-1024x193.png)
![](https://www.cyberbiz.io/support/wp-content/uploads/企業版.png) LINE團購設定 -
團購商品設定  
**功能說明：**  

* LINE團購功能將協助您在LINE群組內進行團購活動，在您或團購主將設定完成的團購機器人加入群組內之後，群組成員即可流暢的進行購物活動。
* LINE團購功能亦協助引導群組成員加入您的品牌官方帳號好友。
* 團購商品設定：從EC商城公開商品中選取並建立團購商品分類，可編輯商品團購價錢。
* 若同樣團購商品分類欲設定不同價格，請善用「複製團購商品」功能減少設定時間。
**操作目錄：**

* 新增團購商品分類
* 複製團購商品分類
* 操作影片
注意事項:  

* 團購商品分類設定完成後無法更改名稱，若需更換請新增或複製該商品分類並更改名稱。

新增團購商品分類 後台路徑 : 「第三方整合」→「LINE 團購設定」  


1. 進入 LINE 團購設定，點擊「新增團購商品分類」  
[![團購商品設定01](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類01.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類01.png)



2. 命名團購商品分類名稱，請注意，該名稱儲存後不可再修改，儲存後進入新增的團購商品分類。  
[![團購商品設定02](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類02.png)



3. 選取欲團購的商品，選取後編輯團購價錢。  
(若商品有不同款式，則不同款式皆會個別出現在列表中。)  
[![團購商品設定03](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類03.png) [![團購商品設定02](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類04.png)



* * *

複製團購商品分類(可用於同團購商品不同團主的狀況)  

1. 若您選取相同商品內容但價格不同，可善用「複製團購商品分類」功能編輯不同價錢。  
[![團購商品設定05](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類05.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類05.png)



2. 替複製的團購商品分類命名，可依照不同團主做命名，以便於辨識。  
[![團購商品設定06](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類06.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類06.png)



3. 成功複製團購商品分類，可再依照不同團主的優惠價格去做變更。   
[![團購商品設定07](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類07.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購商品分類07.png)

* * *


操作影片  


* * *

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購分頁圖-1024x193.png)
![](https://www.cyberbiz.io/support/wp-content/uploads/企業版.png) LINE團購設定 -
團購群組設定  
**功能說明：**  

* LINE團購功能將協助您在LINE群組內進行團購活動，在您或團購主將設定完成的團購機器人加入群組內之後，群組成員即可流暢的進行購物活動。
* LINE團購功能亦協助引導群組成員加入您的品牌官方帳號好友。
* 團購群組設定：設定LINE群組對應之分潤人、分潤代碼，並管理團購活動內容、查看群組歷史團購紀錄。
* 團購功能請至[LINE 團購 – 消費者如何操作LINE團購](https://www.cyberbiz.io/support/?p=29461)
**操作目錄：**

* 如何新增 LINE 群組
* 編輯群組內容
* 如何結束團購活動 (3種情況)
* 歷史團購紀錄
* 品牌如何後台查看LINE團購訂單？
* 操作影片
注意事項:  

* 編輯群組內容前，請先完成 
1. LINE團購機器人設定([連結教學文件](https://www.cyberbiz.io/support/?p=29174&page=2))
2. 推薦分潤代碼設定( [分潤 : 推薦人分潤](https://www.cyberbiz.io/support/?p=39234))
3. 團購商品分類設定([連結教學文件](https://www.cyberbiz.io/support/?p=29174&page=3)) 
* 請確認LINE群組內無其他機器人(LINE群組一次只能有一支機器人)。
* 若團購活動時間尚未開始，則可隨時更新活動時間。(若已開始後則無法變更，僅能提前結束活動。)
* 團購主若要查看下單情形， 請使用[分潤報表下載](https://www.cyberbiz.io/support/?p=1859#recommend_link)連結。

如何新增 LINE 群組
完成LINE團購機器人設定(教學文件連結)後，請團購主加入「團購機器人LINE官方帳號」好友，再由團購主將團購機器人加入團購群組，加入時系統會自動於群組列表新增該群組名稱及群組ID。  
[![團購群組設定01](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定01.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定01.png) [![團購群組設定02](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定02.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定02.png)

* * *

編輯群組內容

1. 選定您要進行團購活動的群組，點選編輯，進入「基本設定」頁   
[![團購群組設定03](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定03.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定03.png)



2. 選取該群組團購活動對應「推薦分潤方案、推薦人、推薦碼」  

* 選取該團購活動套用的「團購商品分類」
* 選取該團購活動的起始時間，若無修改系統預設的「指定開始時間」，則團購活動時間從點選「儲存」開始計算。
[![團購群組設定04](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定04.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定04.png)

* * *

如何結束團購活動 (3種情況)

1. 點選「基本設定」之「結束團購活動」，結束團購活動後，僅保留「LINE團購群組名稱」及「LINE群組ID」，若須設定下個團購活動，為確保正確性，請重新設定其餘欄位。   
[![團購群組設定05](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定05.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定05.png)



2. 原本團購活動時間「指定結束時間」到期。


3. 團購機器人被退出團購群組。

* * *

歷史團購紀錄

* 結束團購活動後，團購歷史紀錄會新增該筆活動資料，您未來能查看該LINE團購群組經歷過的所有團購活動。   
[![團購群組設定06](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定06.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定06.png)



* * *

品牌如何後台查看LINE團購訂單？ 後台路徑 :「訂單」→「所有訂單」  

* 展開「所有」選擇「LINE團購」，即可查看 LINE團購的訂單。   
[![團購群組設定07](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定07.png)](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購-團購群組設定07.png)


![](https://www.cyberbiz.io/support/wp-content/uploads/fountain-pen.png)

* 團購主若要查看下單情形， 請使用[分潤報表下載](https://www.cyberbiz.io/support/?p=1859#recommend_link)連結。

* * *

操作影片  


* * *

![](https://www.cyberbiz.io/support/wp-content/uploads/LINE團購分頁圖-1024x193.png)

