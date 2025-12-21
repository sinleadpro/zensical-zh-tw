---
title: 商品管理
description: 輕鬆管理商品資訊、分類與庫存，提升上架效率。
icon: lucide/package
notes:
  - 蝦皮商品搬站 link
  - add doc [[折扣類型指南]]
hide:
  - feedback
---


# 商品管理

快速建立商品、管理分類與群組，並即時掌握庫存與補貨狀態。 
{ .subtitle }

![](../../assets/images/ec-products-hero.zh-tw.png){ .hero-page }

---

### 開始使用

<div class="grid cards" markdown>

-   :lucide-circle-play: __基礎操作__

	---
	- [檢索商品](quickstart.md#後台搜尋商品)  
	- [選取大量商品](quickstart.md#選取大量商品)   
	- [快速設定商品公開狀態](quickstart.md#快捷按鈕)    

-   :lucide-flame: __熱門主題__
	
	---
    - [將商品從搜尋中排除](設定商品排除搜尋)
    - [匯出商品資料 Excel 表格](批次修改商品資訊#匯出商品-excel-表格)

</div>


### 上架商品

<div class="grid cards" markdown>

- :lucide-package-plus: [__新增商品__](新增單一商品)  
  建立新商品或更新既有商品資訊與設定。  

- :lucide-pencil: [__編輯商品__](編輯商品描述與設定)  
  設定商品標題、描述、規格與多媒體資源。  

- :lucide-import: [__批次操作__](Excel 大量匯入商品)  
   以 Excel 大量建立或修改商品資料。  

- :lucide-refresh-cw: [__同步商品至第三方平台__](設定商品標籤#排除上傳至第三方平台標籤)  
   設定商品是否同步至外部平台。  

</div>

### 分類商品

<div class="grid cards" markdown>

- :lucide-group: [__商品群組__](設定商品分類群組)  
  設定條件或自訂分類管理商品集合。

- :lucide-tag: [__商品標籤__](設定商品標籤)  
   建立與管理商品標籤，以利搜尋與分組。  

- :lucide-navigation: [__導覽列與前台顯示__](設定商品多層級分類)  
   管理前台分類排序與篩選功能。  

</div>

### 銷售商品

<div class="grid cards" markdown>

- :lucide-circle-percent: [__優惠商品__](設定 VIP 會員專屬價格)  
   設定商品折扣、優惠與會員價格。  
	  
- :lucide-shopping-cart: [__多購物車結帳__](設定多購物車)  
   管理不同銷售通路與購物流程。  

- :lucide-bell: [__補貨通知__](設定商品到貨通知)  
   設定缺貨商品的到貨提醒。  

- :lucide-star: [__管理商品評論__](商品評論指南)  
   管理顧客評論與互動功能。  

- :lucide-tag: [__商品廣告__](設定 Google 購物廣告)  
   設定商品廣告串接與投放管理。
	
</div>

### 配送商品

<div class="grid cards" markdown>

- :lucide-settings-2: [__配送物流__](設定商品配送屬性（一般宅配）)  
   綁定商品適用物流。  

- :lucide-ban: [__配送限制__](設定商品超商物流限制與排除選項)  
   限制商品適用之物流選項。  

</div>

---

### 電子票券
[:lucide-lock:{ title="適用方案" }](../../resources/conventions#適用方案) | PLUS 企業

<div class="grid cards" markdown>

- :lucide-compass: [__票券指南__](電子票券指南)  
  電子票券的整體設定與操作流程。

- :lucide-circle-percent: [__票券優惠__](電子票券優惠設定)  
  設定與管理電子票券優惠活動。

- :lucide-key: [__門市權限__](設定電子票券門市權限)  
   門市存取及使用電子票券的權限。

</div>

---

### 常見問題

=== "資料與 Excel 匯入"

	??? quote "SKU 長度限制？"
		 每個 SKU 欄位最多可輸入 255 個字元。
	
	??? quote "Excel 大量修改商品資訊的功能，無法刪除款式是正常的嗎？"
		Excel 匯入商品沒有刪除的功能。 [Excel 大量匯入商品](Excel 大量匯入商品){ data-preview }
		
	??? quote "Excel 匯入商品如何判斷是否成功？"
	    匯入結果可依通知信判斷：

	    - *僅收到「失敗」信*：表示匯入在前期檢查即失敗，常見原因為檔案格式不符（非 `.xlsx`）。
	    - *先收到「成功」，再收到「失敗」*：表示匯入已通過前期檢查，但在逐列匯入時出現錯誤。可能原因包括欄位格式錯誤、匯入值不合法或指定 ID 不存在，請參考失敗通知信說明。
	    - *先收到「成功」，再收到「完成」*：表示匯入完成成功。但若 Excel 某列全空，該列及後續列將未被匯入，需商家自行修正。  
	      
	    [Excel 大量匯入商品](Excel 大量匯入商品#匯入-excel-檔案){ data-preview }

=== "配送與物流"

	??? quote "如果串倉的話，我可以將同一支商品建立出兩個不一樣的 SKU 嗎？"
		可以請峰潮以 *加工品* 的方式，將建立一個 *加工品品項* 後將原本商品加入此加工品中。

	??? quote "使用黑貓快速到店，商品到店時系統是否會發送簡訊或 Email 給消費者？"
		系統完全不會發送任何簡訊或 email 就算有開樣版也不包含在內，到店只有黑貓會傳簡訊通知消費者。

=== "分類與標籤"

	??? quote "前台導覽列的商品的分類一次最多可以顯示幾個？"
		最多 20 個。[設定商品分類群組](設定商品分類群組){ data-preview }

	??? quote "商品標籤已沒有綁定任何商品，但商品加價購仍有顯示未使用的商品標籤？"
		*一般版* 的商品標籤是無法完全刪除的，只有企業版能夠完全刪除。所以會導致一般版的商家在商品加價購會出現所有新增過的商品標籤。


