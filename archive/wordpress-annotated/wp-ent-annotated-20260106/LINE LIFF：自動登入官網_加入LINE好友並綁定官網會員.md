【文件標題】LINE LIFF：自動登入官網/加入LINE好友並綁定官網會員
【適用版本】企業版
【來源連結】https://www.cyberbiz.io/support/?p=41333
【章節路徑】LINE LIFF：自動登入官網/加入LINE好友並綁定官網會員

---

[圖片說明：適用站別]

[[圖片說明：台灣站]](https://www.cyberbiz.io/support/?page_id=2490)

**功能說明：**

- 開啟此功能後，當會員在 LINE APP(手機版) 點選由 EC 後台生成的 LIFF 網址，會透過 LINE 內建瀏覽器開啟網頁，並自動套用會員 LINE 帳戶資訊。
- 消費者的 LINE 帳號**若有綁定官網會員，會自動登入** 並進入 EC 前台指定頁面。
- 消費者若**非商家 LINE 官方帳號好友、官網會員** ，可點選連結，**同時綁定 LINE 官方帳號與官網會員** ，並進入 EC 前台指定頁面。
- 商家可善用 LIFF 網址，例如：製作 QRCode 供消費者掃描、於官網與推播訊息中埋設連結。

**操作目錄：**

- 後台設定
- 前台流程影片
- 應用情境

注意事項:

- **商家若想使用 LINE LIFF 功能，請統一在 CYBERBIZ 後台生成 LINE LIFF 連結，並統一使用於 CYBERBIZ 後台生成的連結。**
- 商家具備 LINE Certified Provider 認證，才能在 LINE 用戶資料授權頁預勾選「加入好友」。
- 開啟此功能後，當會員在 LINE APP 不使用 LINE LIFF 連結，而是以其他網址進入官網，會先開啟 LINE 內建瀏覽器再跳轉至 LIFF 瀏覽器，以登入狀態進入 EC 前台指定頁面。關閉頁面時會需要關閉兩個瀏覽器，商家若考慮使用者體驗，可將導入官網的網址替換成LIFF 網址。
- 若 iOS 用戶在 LINE APP 有開啟「預設瀏覽器開啟連結」，則不適用此功能。
LINE APP 【後台路徑】設定 →  LINE Labs。 [(點擊查看 LINE設定位置)](https://www.cyberbiz.io/support/wp-content/uploads/LINE-快速登入-LIFF會員自動登入04.jpeg)


---

## 📌 後台設定

【後台路徑】第三方整合→「LINE 註冊登入」

1. 需先開啟 [LINE 快速登入](https://www.cyberbiz.io/support/?p=675) 與 [LINE OA 與 LINE Login Channel 的連動](https://www.cyberbiz.io/support/?p=675#lineoa)。

2. 開啟「自動產生 LIFF 網址」開關，點選「儲存設定」後，頁面下方自動產生全站 LIFF 網址。
[[圖片說明：LINE整合]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-快速登入-LIFF會員自動登入01.png)

3. 系統自動產生下方連結，可點擊藍色ICON複製連結。
[[圖片說明：產生連結]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-快速登入-LIFF會員自動登入02.png)

4. LINE Developers 後台會自動產生 LIFF 相關設定。
*請商家不要隨意調整此畫面。
[[圖片說明：developer畫面]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-快速登入-LIFF會員自動登入03.png)

5. 具備 LINE Certified Provider 資格商家，若想透過 LINE LIFF 取得 LINE 用戶手機資訊，請點擊指定 LINE LIFF，於「Scopes」欄位勾選「phone」選項。
- 依據LINE 政策，僅有具備 LINE Certified Provider 資格商家，才可蒐集用戶的手機號碼資訊。
- 如需申請 LINE Certified Provider ，可參考 [LINE Certified Provider申請說明文件](https://drive.google.com/file/d/1oSF07fHFdx_s4gXVhDv0zw81Su3usQKY/view)。
- LINE 僅開放「公司、商行、商號」申請，農場、個人、財團法人無法申請，敬請留意。
[[圖片說明：developer畫面]](https://www.cyberbiz.io/support/wp-content/uploads/LINE-Provider後台-Login-LIFF-LINE-Certified-Provider商家取得手機號碼01.png)

6. 商家可以透過 LINE LIFF 連結製作 EC 任一頁面網址。

以一頁式頁面連結為例：

- 原始網址：https://testtest.testcyb.info/events/qaq* LIFF 網址 : https://liff.line.me/20011118364-jwZ5bzq7/events/qaq規則說明:

- 若要自行設定任一網址，請將原始指定網址(紅色部分)替換成 LIFF URL 即可。
*其餘部分保持不變。
原 : https://testtest.testcyb.info/events/qaq新 : https://liff.line.me/20011118364-jwZ5bzq7/events/qaq* * *


---

## 📌 前台流程影片

可點選右下方 使用全螢幕觀看。

使用者開啟 LIFF 網址 流程

1. 首次開啟需經過 LINE 授權頁
2. 快速跳轉官網首頁 (顯示載入中)
3. 最後跳轉至目的頁面 (會員登入狀態)

- * *


---

## 📌 應用情境

商家可多多利用 LIFF 網址，例如在 LINE OA 圖文選單、LINE 訊息推播、LINE 群組、LINE 聊天室裡埋設 LINE LIFF
連結，或者製作 QRCode 供消費者掃描，以下為情境範例。

- 新增會員頁連結：讓消費者能一鍵查看自己的會員等級、紅利點數與優惠券等。
- 新增部落格文章頁連結：讓消費者能快速獲得最新的部落格文章資訊。
- 新增訂單紀錄連結：讓消費者能一鍵確認訂單的明細與出貨狀態。
- 新增互動遊戲頁連結：透過遊戲活動發送優惠券等優惠，提升會員對品牌的注意力與再下單意願。
- 新增定期定額活動頁連結：推廣定期定額優惠活動。
- 新增一頁式商店連結：推廣一頁式商店的特定行銷活動。
- 新增特定商品頁連結：對特定商品作曝光推播。