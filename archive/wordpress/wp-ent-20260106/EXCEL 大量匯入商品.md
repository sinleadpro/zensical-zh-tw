---
title: "EXCEL 大量匯入商品"
last_modified: ""
categories: [商品>商品上架/管理,常見問題]
tags: []
permalink: "https://www.cyberbiz.io/support/?p=1960"
id: "1960"
---

![](https://www.cyberbiz.io/support/wp-content/uploads/適用站別.png)

![](https://www.cyberbiz.io/support/wp-content/uploads/台灣站.png)

**功能說明：**  

* 透過 Excel 大量匯入商品，可一次「上架」及「更新」N件商品，以利快速批量上架。
* 若貴公司商品圖片、描述圖片另有圖床儲存，亦可透過此方式批量上架。

**操作目錄：**

* 下載excel範例 或 匯出商品
* 新增商品 與 更新既有商品 操作差異
* 欄位說明
* 匯入excel 相關提醒

注意事項:  

* Excel檔案請勿使用粗體，會造成上傳格式錯誤。
* 填寫商品名稱，請勿使用特殊符號，如: | 和 ” “等符號，會導致您商品無法儲存。
* 部分欄位支援性質不同，如：限第一次上傳、可重複多次上傳、單一欄位、可逗號複選欄位、支援HTML等。
* 透過圖床連結（[什麼是圖床](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E7%9B%B8%E5%86%8C)）快速建立圖片，應注意以下資訊： 
1. 圖片格式僅支援：jpg, jpeg, png, gif, webp 等格式，且圖片大小最大不得超過 10MB，建議大小為 2MB。
2. 若在上傳過程中，因圖片大小或是圖片格式不符，而導致匯入失敗，則整個匯入會停止。原本已經上傳好的圖片不會消失，但上傳失敗後面的圖片，則需要另行上傳一次才行！
3. 記得將圖床權限公開，才能上傳。
4. 目前沒有支援中文名稱的圖床，建議先轉成 UTF 格式，再貼到 Excel 上面進行上傳動作。
5. 建議可使用 Imgur 進行上傳  
❗CYBERBIZ 不針對任何外部網站功能進行教學說明，若要使用請店家依使用需求自行評估。

* 若欲修改商品資訊，詳情請看[批次修改商品描述/溫層/配送方式/通路](https://www.cyberbiz.io/support/?p=44199)。



## 📌 下載excel範例 或 匯出商品


新增後台路徑 : 「商品」→「Excel大量匯入商品 」  
修改後台路徑 : 「商品」→「所有商品 」  


* 兩種下載 Excel 檔案的方式，進行編輯。  
![下載檔案](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品01.png)



* * *



## 📌 新增商品 與 更新既有商品 操作差異



* 下載Excel範例，解開隱藏的A、B欄位將發現為空值，此時更新後的Excel上傳後，為「新增商品」。
* 匯出商品的Excel表格，以新增商品隱藏的A、B欄位將帶有系統數值，更新後的Excel上傳後，為「更新既有商品」。
* 若欲修改商品資訊，詳情請看 [批次修改商品描述/溫層/配送方式/通路](https://www.cyberbiz.io/support/?p=44199)。
![操作差異](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品02.png)  

* * *



## 📌 欄位說明


![](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品03.png)

* C【商品名稱】: 填寫商品名稱，請勿使用特殊符號，如: | 和 ” “等符號，會導致您商品無法儲存。(必填)
* D【商品隸屬商店】: 官網名稱或POS商店名稱。 
1. 建立商品時可指定多個商店，請用逗號隔開
2. 更新商品只能指定一家商店
3. 沒有啟用POS功能請忽略此欄，有啟用為必填
* E【商品上架時間】: 請注意時間格式。(選填)
* F【商品下架時間】: 請注意時間格式。(選填)
* G【商品是否公開】: 是/否(選填)
* H【商品標語】: 可參考 [商品頁：商品標語/商品簡述](https://www.cyberbiz.io/support/?p=16893) 文字呈現修改 
* I【商品簡述類型】: html樣板文字 / 純文字 (必填)。
* J【商品簡述】: 依照 商品簡述類型 輸入內容。(選填)
* K【商品網址】: (選填) 
1. 格式：若商品網址為https://example.cyberbiz.io/products/範例商品網址，將「products/」之後的字串填入欄位。2. 留空預設為商品名稱。
* L【商品稅別】: 應稅/免稅 (無商品混稅功能可忽略)(選填)
* M【商品自訂群組】: 多個群組請用 ; 區隔。(選填)
* N【商品任選折扣群組】: (選填)

![](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品04.png)

* O【商品類型】: (選填)
* P【商品廠商】: (選填)
* Q【商品標籤】: 多個標籤請用 , 區隔 (選填)
* R【商品介紹】: 支援html。(選填)
* S【商品通路】: (選填)  
*留空表示適用全通路。 
* T【商品溫層】: 多溫層用 , 隔開，留空為常溫。(選填) 
* U【是否排除搜尋】: 是/否。(選填)
* V【商品運送名稱】: 多運送用 , 隔開。 
1. 建立時 : 留空表示適用所有配送方式。
2. 更新時 : 留空表示維持原配送方式。
* W【商品款式選項/內容】: (選填)

![](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品05.png)

* AC【商品款式售價】: 實際售價(必填)
* AD【商品款式定價】: 建議售價(選填)
* AE【商品款式成本】: 不對客戶顯示的成本價(選填)
* AF【商品款式紅利最高折抵】: (選填)
* AG【商品款式重量】: 填寫公斤。(選填)
* AH【商品款式SKU碼】: (EC選填、POS必填)
* AI【商品款式收貨地址是否需要填寫】: 是/否。(選填)
* AJ【商品款式管理庫存】: 使用POS功能請填是。(選填)

![](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品06.png)

* AK【商品款式庫存量】: 留空表示無限，使用POS功能、FBA庫存同步功能請忽略此欄位。(選填)
* AL【商品款式安全庫存水位】: (選填)
* AM【商品款式廠商編號】: (選填)
* AN【商品款式庫存不足時】: 填入 繼續銷售/停止銷售 (選填)
* AO【商品款式排序】: (選填)
* AP【商品款式材積】: (選填)
* AQ【SEO 設定網頁標題】 請至 [SEO 優化教學](https://www.cyberbiz.io/support/?p=16944#product) 查看操作。
* AR【SEO 設定網頁描述】請至 [SEO 優化教學](https://www.cyberbiz.io/support/?p=16944#product) 查看操作。
* AS【SEO 網頁設定關鍵字】請至 [SEO 優化教學](https://www.cyberbiz.io/support/?p=16944#product) 查看操作。

![](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品07.png)

* AT【商品圖片】: 圖片尺寸需小於10MB，支援 jpg, jpeg, png, gif, webp。(選填)(商品主圖)
* BC【規格說明】: (選填)
* BD【運送方式】: (選填)

* * *



## 📌 匯入excel 相關提醒


*可至後台「訊息推播」→「Email 通知樣板」→右側「商家通知設定」新增商家的通知信箱。 
1. 【失敗】：系統將提示失敗原因，請更正後重新上傳。
2. 【成功】：請稍待完成信件，未完成重複上傳將導致資訊混亂，請務必耐心等候。
3. 【完成】：匯入已確認完成，可查看更新成果或再次更新其他內容。
![](https://www.cyberbiz.io/support/wp-content/uploads/大量匯入商品08.png)  

