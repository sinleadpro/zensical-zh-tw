---
title: "商米P2 Pro刷卡機設定"
last_modified: ""
categories: [POS>POS後台>付款方式設定]
tags: []
permalink: "https://www.cyberbiz.io/support/?p=21480"
id: "21480"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)
![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)
**功能說明：**  

* 以平板、商米刷卡發票機兩項無線設備，實現移動式POS店點
* [結帳流程示範](https://drive.google.com/file/d/1n5Rtw6HfcnWes9KNXzyzmb6XK4HD7zjN/view?usp=sharing)
* [退款流程示範](https://drive.google.com/file/d/1_ePN6gcI-63uko4mknV8-RN71GrtlQFz/view?usp=sharing)
**操作目錄：**

* 設備認識與MYPAY金流設定
* MyPay刷卡機操作
* 紙捲廠商資訊
注意事項:  

* 請務必先行申請MYPAY金流，申請後才可進行後台設定。
* 請選擇正確紙捲（10m），避免因尺寸不合無法放入商米機台當中。
* 目前商米支援僅信用卡支付，若要使用Line Pay請參考[POS LINEPAY掃碼支付](https://www.cyberbiz.io/support/?p=11171)。
* 若您使用 MyPay 刷卡機方案，請勿安裝 POS 驅動程式。
* MyPay刷卡機僅作為刷卡機和發票「印表機」使用，並不包含發票開立服務，門市要開發票，必須購買 [盟立加值中心](https://www.cyberbiz.io/support/?p=5189) 服務 
* 請務必完成下方文件中的所有設定步驟後，再進行結帳測試，以確保資訊傳送正確。

📌 設備認識與MYPAY金流設定 使用商米P2
Pro刷卡機，只需要有Wifi，不需接線就可以完成付款和列印發票，適合搭配平板使用，請參考[平板模式教學文件](https://www.cyberbiz.io/support/?p=21520\(在新分頁中開啟\))。使用此款刷卡機，必須使用MyPay的金流服務。
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/image.png) ☝️
**前置步驟**

1. 選購MyPay刷卡機（請洽業務）
2. 需申請MyPay金流服務：[申請網址](https://query.onecardpass.com/application/cardreader/b7b68f)（審核時程約2週，審核結果會以信件通知到負責人，若失敗會採取重新申請的方式，若申請有疑問，請洽MyPay客服 04-23220267 #25）
3. 申請完成後，可取得**MYPAY特店商務代號** 、**MYPAY後台帳號**(MyPay會協助並提供相關資訊)
4. 收到刷卡機後，需將**MyPay卡機名稱** 填入自家POS系統後台(卡機名稱由MyPay提供，如下述設定)
**☝️ CYBERBIZ後台設定**

* 請登入 [MYPAY後台](https://biz.spay.com.tw/auth/login)
* 進入MYPAY後台**系統設定 > 金鑰管理**，取得**MYPAY特店金鑰**
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/image-7-1024x261.png)

* 於Cyberbiz POS系統後台，**POS商店列表 > 商店設定頁面**，填入**MYPAY特店商務代號** 和**MYPAY特店金鑰**
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/image-1.png)

* 於**POS商店列表 > POS商店頁面 > POS機設定**，填入MYPAY卡機名稱
* 請輸入：[您的統編]_01
* 例如：12345678_01
![](https://www.cyberbiz.io/support/wp-content/uploads/ShareX_2025-07-22_13-46-43.png)

* 於**POS商店列表 > POS商店頁面 > POS機設定**，發票設定選擇盟立發票，發票機設定選擇MYPAY發票機。
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/11/image.png)

* 於**POS商店列表 > POS商店頁面 > 付款方式，**將MYPAY的選項打開，並點儲存付款方式設定。若MYPAY為主要的付款方式，也可把此付款方式拖曳到較高順位。
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/image-3.png) ☝️
**交易回報網址設定**

1. 於[MyPay後台](https://biz.spay.com.tw/auth/login)，**系統設定 > 金流服務系統 > 連線通知設定**，於以下欄位填入相同網址：
* **即時交易回傳網址**
* **退款** /**取消交易回傳網址**
* 網址格式為：**https://Cyberbiz商家網址/mypay/notify**例：**https://shop123.cyberbiz.co/mypay/notify**

![](https://www.cyberbiz.io/support/wp-content/uploads/2021/11/image-1.png) 2.
輸入交易回傳網址後點擊測試按鈕，顯示連線成功跳窗，即完成設定。若無法成功設定，請先確認回傳網址是否正確，若仍無法完成設定，再請洽客服。
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/10/image-6.png) 3.
至POS前台確認付款方式是否有正常顯示MYPAY的支付方式，並測試下訂單。 📌 MyPay刷卡機操作 可下載
[教學文件](https://drive.google.com/file/d/1r7yUn55ci36ZcQytTHZm1aQuuOQb6Qp6/view?usp=sharing)
pdf檔 ☝️ **登入**

1. 開啟MyPay APP
2. 輸入商店資料登入
![商米P2-PRO刷卡機設定01](https://www.cyberbiz.io/support/wp-content/uploads/2021/11/商米P2-PRO刷卡機設定01.png) ☝️ **結帳**

1. 結帳時，選取MyPay支付方式
2. 按下付款按鈕，系統會自動喚起MyPay刷卡機，可使用感應、刷條碼方式信用卡支付
[su_image_carousel source="media: 22524,22525,22526" limit="20"
slides_style="default" controls_style="dark" crop="16:9" columns="3"
adaptive="yes" spacing="yes" align="none" max_width="none" captions="no"
arrows="yes" dots="yes" link="lightbox" target="blank" autoplay="5"
speed="medium" image_size="medium" class=""]  ☝️ **取消訂單**

1. 於訂單列表選取欲取消訂單
2. 點選取消訂單
3. 點選退款，MyPay刷卡機會列印簽單，供商家和商家客戶留底
[su_image_carousel source="media: 22527,22528" limit="20"
slides_style="default" controls_style="dark" crop="16:9" columns="2"
adaptive="yes" spacing="yes" align="none" max_width="none" captions="no"
arrows="yes" dots="yes" link="lightbox" target="blank" autoplay="5"
speed="medium" image_size="medium" class=""]  📌 紙捲廠商資訊 若您自CYBERBIZ購買商米P2
PRO，機器將內附上一捲紙捲，紙捲用完前，請您至[財政部電子發票感熱紙](https://invoice.ppmof.gov.tw/PSJ_Web/)添購，規格為10m公版感熱紙捲，寬度5.7cm，紙捲長度10m，外徑約3.6cm。
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/發票紙捲2.jpg)
![](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/發票紙捲.jpg)

