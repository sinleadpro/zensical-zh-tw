---
title: "FACEBOOK 快速登入異常 解決辦法"
last_modified: ""
categories: [第三方整合>Facebook相關設定,常見問題]
tags: []
permalink: "https://www.cyberbiz.io/support/?p=26854"
id: "26854"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)
[![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)](https://www.cyberbiz.io/support/?page_id=2490)
**問題連結：**

* 無法使用此功能：此應用程式目前不支援 Facebook 登入 
* Facebook 帳號為綁定信箱，無法登入/App dose not have Advanced public_profile permission
* FB登入功能已停用
注意事項:  

* Facebook 相關設定請依 Facebook 官方網站設定為主，CYBERBIZ 僅提供基礎設定教學。
* 若此篇文章無法解決您的問題，請洽 Facebook 客服，排除您的狀況
* 相關設定請至[ Facebook for Developers](https://developers.facebook.com/)

一、無法使用此功能：此應用程式目前不支援 Facebook 登入
[![電子票券設定01](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法01.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法01.png)  

因 Facebook 最近不定期的進行應用程式審核及更新，建議廠商可以定期至 Facebook for Developers 商店應用程式做檢查設定，

1. 查看網頁上方有無警示訊息。
2. 點選左側「提示→收件夾」檢查是否有需要更新的設定，可自行照網頁提示操作步驟，完成設定。
定期檢查為什麼發生錯誤!

1. 「年度資料檢查」未執行而被停用，請依照提示完成設定！
2. 「違反政策」，可以點擊「提交申訴」按鈕，請 Facebook 重新審查，並按照提示完成設定。
[![電子票券設定01](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法02.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法02.png)  
檢查API 版本是否過舊  
「設定」→「進階」→檢查API版本!  

[![電子票券設定01](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法03.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法03.png) 二、Facebook 帳號為綁定信箱，無法登入/App dose
not have Advanced public_profile permission [![FACEBOOK-快速登入異常-
解決辦法04](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法04.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法04.png)  


1. Facebook 程式版本、審核的部分，會通知您需要確認開啟應用程式的進階授權取得顧客的資料，  
請您至「應用程式審查」→「權限和功能」→取得email、public_profile存取權限。 [![FACEBOOK-快速登入異常-
解決辦法05](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法05.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法05.png)  


2. 完成設定為 Advanced Access 就代表已取得進階存取權限!  
[![FACEBOOK-快速登入異常-解決辦法06](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法06.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法06.png)  


三、FB登入功能已停用 [![FACEBOOK-快速登入異常-解決辦法07](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法07.png)](https://www.cyberbiz.io/support/wp-content/uploads/FACEBOOK-快速登入異常-解決辦法07.png)  
原因 : FACEBOOK政策(不再支援 Android 內嵌瀏覽器的「Facebook
登入」驗證)，[官方說明連結](https://developers.facebook.com/blog/post/2021/06/28/deprecating-support-fb-login-authentication-android-embedded-browsers/?locale=zh_TW)  
解法 : 請客戶下載 FACEBOOK APP。  
若客戶有下載 FACEBOOK APP ，使用內嵌瀏覽器開啟Facebook 登入則會自動跳轉至 FACEBOOK APP，即可避免此異常。

