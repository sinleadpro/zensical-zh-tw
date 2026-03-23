【文件標題】LINE 快速登入教學
【適用版本】企業版, region_jp
【來源連結】https://www.cyberbiz.io/support/?p=675
【章節路徑】LINE 快速登入教學

---

[圖片說明：適用站別]

[[圖片說明：台灣站]](https://www.cyberbiz.io/support/?page_id=2490)

[]()

**功能說明：**

- 顧客可於「會員註冊」、「結帳頁」使用LINE快速登入，系統將自動抓取客戶LINE的「Email」做帳號比對。
- 透過 LINE快速登入 ，推播商家官方帳號，進而增加官方帳號曝光度。
- 使用LINE登入，可使其與 CYBERBIZ 顧客列表作關聯，企業版可篩選 透過 「LINE快速登入」 的會員。

**操作目錄：**

- 建立 LINE 登入資訊
- 填入【帳號ID】、【應用程式密鑰】至 CYBERBIZ 後台
- LINE 快速登入導引會員加入LINE官方帳號好友
- LINE 快速登入進階設定 : 取得會員手機號碼
- LINE Provider 設定

常見問題

- 無法於後台完成串接
- LINE 快速登入頁面出現 400 Bad Request
- iOS系統無法直接跳轉登入畫面

注意事項:

- 請商家參照以下文件操作，並填入應用程式ID、應用程式密鑰並開啟【啟用LINE登入】，方可使用LINE登入。
- 若您有已建立的LINE官方帳號，請確認您的LINE login channel與 LINE官方帳號下之 Messaging API channel的Provider為同一個。
- 消費者使用 Hinet信箱登入會員，若忘記密碼，會因為 Hinet 阻擋訊息而無法重新設定密碼，可建議客戶使用其他信箱註冊。 。
- 顧客的 LINE帳號 一定要綁定EMAIL，才可使用 LINE 登入。


---

## 📌 建立 LINE 登入資訊

1. 請先至[LINE Developers](https://developers.line.biz/en/) 登入帳號（需要有LINE帳戶），若已經登入可按「console」進入。
[[圖片說明：登入linedeveloper]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入01.png)

2. 進入畫面後，若您尚未有任何 Provider，請先按下方建立一個，
若已先設定好 串接 Messaging API了，請選擇對應的 Provider。
[[圖片說明：選擇/建立provider]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入02.png)
*若尚未建立過 Provider的客戶可自行建立一個。
[[圖片說明：無provider]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入03.png)

3. 點選【Create a LINE Login channel】。 (此設定以原有 Provider 用戶為範例)
[[圖片說明：新建loginchannel]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入04.png)

4. 選擇 LINE Login 功能。
[[圖片說明：login畫面]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入05.png)

5. 填寫下方欄位。

- 【Region to provide the service】: (台灣站)Taiwan /(日本站)Japan
- 【Company or owner’s country or region】 : Taiwan
[[圖片說明：新建channel]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入06.png)

- 【Channel icon】: 上傳網站 Logo
- 【Channel name】: 輸入商店名稱
- 【Channel description】: 輸入商店簡述。(內容不可以換行)
- 【App types】: 勾選 Web app
[[圖片說明：設定channel]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入07.png)

- 【Email address】: 輸入 email
- 【Privacy policy URL】: 輸入網站隱私政策網址
- 【Terms of use URL】: 輸入網站服務條款網址
- 勾選條款後點擊 Creat 按鈕
[[圖片說明：設定channel2]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入08.png)

6. 完成設定後，可先將狀態「Developing」轉至「Published」，
選擇頁籤「Basic settings」滑至最下方至「OpenID Connect」。
[[圖片說明：設定openID]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入09.png)

7. 點開 OpenID Connect 的「Apply」

- 若無法於後台完成 LINE 快速登入串接，請檢查已完成此步驟。

[[圖片說明：openID connect]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入10.png)

8. 設定【OpenID Connect】欄位資訊，確認狀態為「Applied」，
並勾選裡面的內容，依照需求上傳 商家Logo，並按下「Submit」。
[[圖片說明：openID connect2]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入11.png)

9. 點選 頁籤「LINE Login」設定 Callback URL，點選「Edit」。
[[圖片說明：callback]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入12.png)

10. 填入商家的 Callback URL。
若您的商店網址為：https://2020test.cyberbiz.co/則填入：https://2020test.cyberbiz.co/customer/auth/line/callback

- Callback URL 支援新增多個網域，**若您有購買自有網域，請務必將 CYBERBIZ 網域及自有網域都一併填入「Callback URL」。**
- 填入 CYBERBIZ 網域後，點擊 ENTER 鍵，即可新增自有網域。
- 若 LINE 快速登入頁面呈現 400 Bad Request，屆時顧客無法由 LINE 帳號登入或註冊會員，請商家確認此步驟網址填寫無誤。

[圖片說明：fountain-pen]

- 跨境用戶填入網址不需加上 zh-TW 等，僅需填寫一般的網域即可。
- 自有網域及 CYBERBIZ 網域設定邏輯相同。

[[圖片說明：callbackURL設定]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入13.png)

- * *


---

## 📌 填入【帳號ID】、【應用程式密鑰】至 CYBERBIZ 後台

1. 請先至[LINE Developers](https://developers.line.biz/en/) 選擇頁籤「Basic settings」，複製【Channel ID】【Channel secret】。
[[圖片說明：設定id，secret]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入14.png)

2. 至 CYBERBIZ 後台貼上並開啟「啟用LINE登入」
【後台路徑】第三方整合「LINE 註冊登入」
[[圖片說明：設定id，secret]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入15.png)

3. 設定完成後至商店前台即可使用「LINE 快速登入」
[[圖片說明：前台登入畫面]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入16.png)

- * *


---

## 📌 LINE 快速登入導引會員加入LINE官方帳號好友

請先至下方 LINE PROVIDER 設定 確認是否正確設定

1. 請先至[LINE Developers](https://developers.line.biz/en/) 選擇頁籤「Basic settings」，往下滑至「Add friend option」→「Linked LINE Official Account」，選擇 Edit。
[[圖片說明：linkoa]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入17.png)

2. 可選擇同個 Provider下的 LINE官方帳號。
[[圖片說明：linkoa選擇]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入18.png)

3. 前台畫面，使用 LINE快速登入，並可出現「加入好友」按鈕。
[[圖片說明：前台登入畫面19]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入19.png)
*會員若點擊「取消」，仍可登入但就不會自動加入 LINE官方帳號。
[[圖片說明：前台登入畫面20]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入20.png)

- * *


---

## 📌 LINE 快速登入進階設定 : 取得會員手機號碼

(此功能需先設定 LINE快速登入後，再前往設定相關功能。)
(商家可自行選擇是否要設定該功能)

[LINE 快速登入進階設定 : 取得會員手機號碼](https://www.cyberbiz.io/support/?p=35740)

- * *


---

## 📌 LINE Provider 設定

1. 請先至 [LINE OA 建立/MESSAGING API 串接設定](https://www.cyberbiz.io/support/?p=706) 建立好 LINE OA 官方帳號。
2. 並確認同個 Provider 下建立 LINE Login channel 和 LINE messaging API channel。
3. 設定完成 才可開始設定 LINE 快速登入導引會員加入LINE官方帳號好友。
[[圖片說明：provider]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入21.png)

- * *


---

## 📌 常見問題：iOS系統無法直接跳轉登入畫面

若 iOS系統無法直接跳轉登入畫面，請依照下方指示進行登入。

1. 建議使用 Safari 瀏覽器 進行操作。

2. 若出現 『要在「LINE」中打開嗎？』 的彈窗，請選擇 打開。
[[圖片說明：line打開]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入22.png)

3. 如果沒有出現彈窗，請點擊畫面下方 「使用 LINE 應用程式登入」。
[[圖片說明：line登入]](https://www.cyberbiz.io/support/wp-content/uploads/LINE快速登入23.png)