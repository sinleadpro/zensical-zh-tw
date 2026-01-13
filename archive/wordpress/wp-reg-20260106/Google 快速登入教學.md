---
title: "Google 快速登入教學"
last_modified: ""
categories: [第三方平台整合>Google相關設定]
tags: []
permalink: "https://www.cyberbiz.io/helpcenter/?p=4728"
id: "4728"
---

![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/一般版3.png)
![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/PLUS版3.png)
**功能說明：**  

* 消費者可於註冊會員時使用 Google 快速登入，系統將自動依消費者輸入的電子郵件信箱新增會員資料，或者將現有會員資訊綁定 Google 帳戶。

**操作目錄：**

* 啟用 Google 快速登入

注意事項:  

* 若消費者使用 Google、Line、Facebook 快速登入時輸入同一電子郵件信箱，在後台會被視為同一會員，並在會員明細頁的「帳號類型」中註明。

## 📌 啟用 Google 快速登入



1. 登入 [ Google Cloud Platform](https://console.cloud.google.com/)，點擊導覽列中「選取專案」按鈕。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入01.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入01.png)  

2. 於「選取專案」視窗中點選「新增專案」。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入02.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入02.png)  

3. 進入「新增專案」視窗，設定以下欄位。 
* 「專案名稱」：依需求命名。
* 「機構組織」：依需求選擇，若無機構組織，選擇「無機構」。
* 「位置」：設定專案上層機構或資料夾。
* 點擊「建立」。
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入03.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入03.png)  

4. 搜尋列中搜尋「Credentials」，選擇帶有「API & Services」說明的選項。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入04.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入04.png)  

5. 進入 OAuth 總覽頁，點擊「開始」。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入05.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入05.png)  

6. 進入專案設定頁，於「1 應用程式資訊」區域設定以下欄位。 
* 「應用程式名稱」：依需求命名。
* 「使用者支援電子郵件」：依需求輸入常用電子郵件地址。
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入06.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入06.png)  

7. 於「2 目標對象」區域選擇「外部」。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入07.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入07.png)  

8. 於「3 聯絡資訊」區域選輸入聯絡電子郵件地址。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入08.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入08.png)  

9. 於「4 完成」區域勾選同意。確認無誤後點擊「建立」。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入09.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入09.png)  

10. 於側邊欄中點選「總覽」，點擊「建立 QAUTH 用戶端」。   
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入10.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入10.png)  

11. 於「建立 OAuth 用戶端 ID」頁面中設定以下欄位。 
* 「應用程式類型」：選擇「網頁應用程式」。
* 「名稱」：依需求命名。
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入11.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入11.png)  

12. 於「已授權的重新導向 URL」區域中點擊「新增 URL」。 
* 輸入 https://{你的商店網址}/customer/auth/google_oauth2/callback* 點擊「建立」。
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入12.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入12.png)  

13. 網站會彈出「OAuth 用戶端已建立」彈窗。 [![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入13.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入13.png)  

14. 進入 CYBERBIZ 後台，找到「Google 註冊/登入」區域。  
後台路徑 :  「第三方整合」→「谷歌 Google 設定」  

* 將 Google Cloud「用戶端編號」輸入至 CYBERBIZ後台「應用程式 ID」欄位。
* 將 Google Cloud「用戶端密碼」輸入至 CYBERBIZ後台「應用程式 Secret」欄位。
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入14.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入14.png)  

* 若已關閉 Google 彈窗，可於側邊欄中點選 「API和服務」→「憑證」，於「OAuth2.0 用戶端 ID」區域中點擊所設定的用戶端名稱，即可查看編號和密碼。
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入18.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入18.png)  
[![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入19.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入19.png)  

15. 於側邊欄中點選「目標對象」，點擊「發布應用程式」。 [![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入15.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入15.png)  

16. 完成設定，消費者即可於官網前台以 Google 帳戶註冊/登入網站。 [![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入16.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入16.png)  

17. 消費者若透過 Google 帳戶註冊網站會員，會在會員明細頁中註記「帳號類型」為「Google 快速登入」。 [![文件名](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入17.png)](https://www.cyberbiz.io/support/wp-content/uploads/google快速登入17.png)  

