【文件標題】PLUS用戶 - LINE OA 受眾串接
【適用版本】進階PLUS版, 專業PLUS版, 高手PLUS版
【來源連結】https://www.cyberbiz.io/helpcenter/?p=5631
【章節路徑】PLUS用戶 - LINE OA 受眾串接

---

**功能說明：**

- 商家可透過 CYBERBIZ 後台會員篩選器，將「使用LINE快速登入」或「已綁定LINE OA」的會員傳送到LINE OA後台建立受眾，進行後續訊息推播或廣告投放之用。
- 需透過 CYBERBIZ 後台更新或刪除由此功能建立的受眾。

**操作目錄：**

- 建立受眾至LINE後台
- 更新受眾至LINE後台
- 刪除受眾
- 如何應用LINE受眾

注意事項:

- 請確認您已完成設定 [ LINE Messaging API ](https://www.cyberbiz.io/support/?p=706) 才可使用此功能。


---

## 建立受眾至LINE後台

【後台路徑】會員 → 「所有會員」

1. 進入會員列表，點選上方搜尋欄，出現「篩選器」。 [[圖片說明：line-oa-受眾串接01]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接01.png)

2. 篩選器：新增「已完成LINE登入」或「已完成LINE綁定」或「已完成LINE登入或LINE綁定」後點選「套用」。
*商家可根據此包受眾用途決定是否須帶入其他篩選器。
*LINE綁定為 LINE OA 官方帳號 綁定 官網會員。

[圖片說明：fountain-pen]

- 此功能篩選一定要選擇「已完成LINE登入」或「已完成LINE綁定」或「已完成LINE登入或LINE綁定」不然無法傳送至 LINE OA。

[[圖片說明：line-oa-受眾串接02]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接02.png)

3. 新增完成商家所需篩選器，點選右方區塊「儲存」。
並輸入【名稱】【描述】，勾選下方【欄位】，按下「確認」。

[[圖片說明：line-oa-受眾串接03]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接03.png)

[[圖片說明：line-oa-受眾串接04]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接04.png)

4. 儲存完成後，可查看相關資訊。
[[圖片說明：line-oa-受眾串接05]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接05.png)

5. 進入LINE OA後台查看受眾是否建立成功，受眾名稱為「(篩選條件名稱)_CYBERBIZ上傳」
(【後台路徑】點選帳號名稱 → 主頁 → 資料管理 → 受眾)[[圖片說明：line-oa-受眾串接06]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接06.png)

- * *


---

## 更新受眾於LINE後台

【後台路徑】會員 → 「所有會員」

1. 點選「更新受眾至LINE後台」，系統將同步該篩選條件最新搜尋結果至 LINE OA 後台受眾。
2. 由 CYBERBIZ 後台建立的受眾，不能於 LINE 後台更新及刪除，僅能透過 CYBERBIZ 同步處理。
[[圖片說明：line-oa-受眾串接07]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接07.png)

- * *


---

## 刪除受眾

【後台路徑】會員 → 「所有會員」

1. 點選欲刪除的篩選條件/受眾左下角之「刪除」按鈕。
[[圖片說明：line-oa-受眾串接08]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接08.png)

2. 彈窗提醒，若點選刪除，此處選取之篩選條件及LINE OA後台受眾，將同步刪除，商家確認後點選「刪除」。
[[圖片說明：line-oa-受眾串接09]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接09.png)

3. 至LINE OA後台查看原本建立之受眾已不存在。
[[圖片說明：line-oa-受眾串接10]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接10.png)

- * *


---

## 如何應用LINE受眾

一、[LINE OA Manager](https://manager.line.biz/) 受眾推播

【後台路徑】LINE OA → 群發訊息 → 建立新訊息

1. 點選傳送對象【篩選目標】，即可選擇受眾，並按下【筆符號】即可新增受眾。
[[圖片說明：LINE-OA-受眾串接11]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接11.png)

2. 選擇您在 CYBERBIZ 設定的受眾名稱並選擇【包含】or【不包含】，並新增受眾。
*若選擇不包含，則可對此受眾外的會員傳送訊息。 [[圖片說明：LINE-OA-受眾串接12]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接12.png)

3. 完成後即可繼續推播訊息。
[[圖片說明：LINE-OA-受眾串接13]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接13.png)

二、[Ad Manager](https://admanager.line.biz/home/) 受眾推播

【後台路徑】Ad Manager → 您的廣告帳號 → 左上角選單 → 受眾

1. 新增【分享自LINE官方帳號的使用者識別碼UID受眾】，將 CYBERBIZ 串接的受眾上傳至 Ad Manager。
[[圖片說明：line-oa-受眾串接14]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接14.png)

2. 當您要開始投放廣告時，建立廣告群組，可使用上述建立好的受眾。
[[圖片說明：LINE-OA-受眾串接15]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-OA-受眾串接15.png)

- * *