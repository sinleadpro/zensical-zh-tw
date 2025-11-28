---
title: 商品管理
description: 輕鬆管理商品資訊、分類與庫存，提升上架效率。
icon: lucide/package
notes:
  - 蝦皮商品搬站 link
hide:
  - toc
  - feedback
---


# 商品管理

<div class="grid" markdown>

<br>
<big>__開始使用__</big>  
管理商品與庫存資料。  
快速建立商品、管理分類與群組，並即時掌握庫存與補貨狀態。  
<br>
[認識商品管理介面 :lucide-circle-arrow-right:](get-started.md)  

![](../../assets/images/ec-products-hero.zh-tw.png)

</div>

---

### 上架商品

<div class="grid cards" markdown>

- :lucide-package-plus: __新增商品 & 商品更新__

	  ---
	  [建立單一商品](新增單一商品.md)  
	  [建立組合商品 :lucide-lock:](新增組合商品.md)  
	  [建立預購商品](設定多購物車.md#預購商品)

- :lucide-file-text: __商品內容設定__

	  ---
	  [設定商品標語與簡述](編輯商品標語與商品簡述.md)  
	  [編輯商品描述與設定](編輯商品描述與設定.md)  
	  [上傳商品影片 :lucide-lock:](設定商品影片.md)  
	  [商品其他設定](商品其他設定.md)

</div>

### 批次操作

<div class="grid cards" markdown>

- :lucide-import: __Excel 批次匯入與修改__

	  ---
	  [Excel 大量匯入商品](Excel 大量匯入商品.md)  
	  [批次修改商品資訊](批次修改商品資訊.md)  

- :lucide-refresh-cw: __第三方平台同步__

	  ---
	  [排除贈品不上傳至第三方平台](設定商品排除上傳至第三方平台.md)

</div>

### 分類與群組

<div class="grid cards" markdown>

- :lucide-tag: __商品標籤管理__

	  ---
	  [商品標籤管理](設定商品標籤.md)

- :lucide-layers: __商品群組__

	  ---
	  [自訂分類群組設定](設定商品分類群組.md)  
	  [條件分類群組設定](設定條件分類群組.md)  
	  [加價購設定](設定加價購群組.md)  
	  [不適用折扣群組設定](設定不適用折扣群組.md)  
	  [單品限時折扣設定](設定單品限時折扣群組.md)  

- :lucide-navigation: __多層級分類與排序__

	  ---
	  [商品多層級分類設定](設定多層級分類.md)  
	  [群組排序管理](群組排序.md)  
	  [群組篩選器](群組篩選器.md)

</div>

### 銷售與通知

<div class="grid cards" markdown>

- :lucide-circle-percent: __折扣與優惠__

	  ---
	  [VIP 專屬價格設定](設定 VIP 專屬會員價格.md)  
	  [任選折扣群組設定](設定任選折扣群組.md)  
	  [單品限時折扣群組](設定單品限時折扣群組.md)

- :lucide-bell: __商品到貨通知__

	  ---
	  [商品貨到通知](設定商品到貨通知.md)

- :lucide-shopping-cart: __多購物車設定__

	  ---
	  [多購物車設定](設定多購物車.md)

- :lucide-star: __管理商品評論與留言區__

	  ---
	  [啟用商品評論 :lucide-lock:](商品評論指南.md)  
	  [啟用留言區 reCAPTCHA :lucide-lock:](啟用留言區 reCAPTCHA.md)  

</div>

### 配送物流

<div class="grid cards" markdown>

- :lucide-truck: __配送物流設定__

	  ---
	  [商品配送設定](商品配送設定.md)  
	  [超商物流限制與排除設定](超商物流限制與排除設定.md)  
	  [一般宅配設定](商品上架管理-宅配.md)  
	  [宅配貨到付款設定](商品上架管理-宅配貨到付款.md)

</div>

### 電子票券
[:lucide-lock:{ title="適用方案" }](../../resources/conventions#適用方案) | PLUS 企業

<div class="grid cards" markdown>

- :lucide-rocket: __電子票券開始使用__

	  ---
	  [電子票券指南](電子票券指南.md)  
	  [電子票券設定](電子票券設定.md)  
	  [票券優惠設定](電子票券優惠設定.md)  
	  [門市權限功能](電子票券門市權限.md)

</div>


### 常見問題 (FAQ)

=== "商品上架"

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

=== "商品配送"

	??? quote "如果串倉的話，我可以將同一支商品建立出兩個不一樣的 SKU 嗎？"
		可以請峰潮以 *加工品* 的方式，將建立一個 *加工品品項* 後將原本商品加入此加工品中。

	??? quote "使用黑貓快速到店，商品到店時系統是否會發送簡訊或 Email 給消費者？"
		系統完全不會發送任何簡訊或 email 就算有開樣版也不包含在內，到店只有黑貓會傳簡訊通知消費者。

=== "商品分類"

	??? quote "前台導覽列的商品的分類一次最多可以顯示幾個？"
		最多 20 個。[設定商品分類群組](設定商品分類群組){ data-preview }

	??? quote "商品標籤已沒有綁定任何商品，但商品加價購仍有顯示未使用的商品標籤？"
		*一般版* 的商品標籤是無法完全刪除的，只有企業版能夠完全刪除。所以會導致一般版的商家在商品加價購會出現所有新增過的商品標籤。
