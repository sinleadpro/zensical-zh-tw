---
title:
hide:
  - toc
  - path
  - feedback
---

# 智能 POS

<div class="grid" markdown>
 
 <br>  
<big>__開始使用__</big>    
開始建立與管理您的門市系統。  
完成門市設定、商品上架、收銀與會員管理，一步步帶您啟動營運。  
<br>
[新手上路 :lucide-circle-arrow-right:](get-started.md)

![](../assets/images/pos-hero.png)

</div>

---

### 常見問題 :lucide-message-circle-question-mark:

=== "門市設定"

	??? quote "SKU 長度限制？"
		 每個 SKU 欄位最多可輸入 255 個字元。
	
	??? quote "EXCEL 大量修改商品資訊的功能，無法刪除款式是正常的嗎？"
		匯入沒有刪除的功能。 [Excel 大量匯入商品](Excel 大量匯入商品){ data-preview }

	??? quote "Excel 匯入商品如何判斷是否成功？"
	    匯入結果可依通知信判斷：

	    - *僅收到「失敗」信*：表示匯入在前期檢查即失敗，常見原因為檔案格式不符（非 `.xlsx`）。
	    - *先收到「成功」，再收到「失敗」*：表示匯入已通過前期檢查，但在逐列匯入時出現錯誤。可能原因包括欄位格式錯誤、匯入值不合法或指定 ID 不存在，請參考失敗通知信說明。
	    - *先收到「成功」，再收到「完成」*：表示匯入完成成功。但若 Excel 某列全空，該列及後續列將未被匯入，需商家自行修正。  
	      [Excel 大量匯入商品](Excel 大量匯入商品#匯入-excel-檔案){ data-preview }

=== "商品管理"

	??? quote "如果串倉的話，我可以將同一支商品建立出兩個不一樣的 SKU 嗎？"
		可以請峰潮以 *加工品* 的方式，將建立一個 *加工品品項* 後將原本商品加入此加工品中。

	??? quote "使用黑貓快速到店，商品到店時系統是否會發送簡訊或 Email 給消費者？"
		系統完全不會發送任何簡訊或 email 就算有開樣版也不包含在內，到店只有黑貓會傳簡訊通知消費者。

=== "訂單結帳"

	??? quote "前台導覽列的商品的分類一次最多可以顯示幾個？"
		最多 20 個。[設定商品分類群組](設定商品分類群組){ data-preview }

	??? quote "商品標籤已沒有綁定任何商品，但商品加價購仍有顯示未使用的商品標籤？"
		*一般版* 的商品標籤是無法完全刪除的，只有企業版能夠完全刪除。所以會導致一般版的商家在商品加價購會出現所有新增過的商品標籤。
		
=== "商品銷售"


---


=== "門市設定"

	<div class="grid cards" markdown>
	
	-   :lucide-store: __門市設定__
	    
	    ---
	    
	    設定門市資訊、營業時間、付款方式及店員權限
	    
	    [:octicons-arrow-right-24: 開始設定](#)
	
	-   :lucide-truck: __庫存同步__
	    
	    ---
	    
	    與中央倉庫或供應鏈連動，確保門市商品數量正確
	    
	    [:octicons-arrow-right-24: 參考指南](#)
	
	-   :lucide-palette: __收銀介面__
	    
	    ---
	    
	    自訂 POS 介面、顏色、字體與按鈕配置
	    
	    [:octicons-arrow-right-24: 客製化設定](#)
	
	-   :material-scale-balance: __權限管理__
	    
	    ---
	    
	    管理門市人員帳號、角色與操作權限
	    
	    [:octicons-arrow-right-24: 參考文件](#)
	
	</div>

=== "商品管理"

	<div class="grid cards" markdown>
	
	-   :lucide-package: __商品上架__
	    
	    ---
	    
	    新增、編輯與批次更新商品資訊
	    
	    [:octicons-arrow-right-24: 開始上架](#)
	
	-   :lucide-barcode: __條碼掃描__
	    
	    ---
	    
	    使用 POS 條碼掃描快速完成銷售與庫存管理
	    
	    [:octicons-arrow-right-24: 參考指南](#)
	
	-   :lucide-ticket: __促銷與優惠券__
	    
	    ---
	    
	    設定折扣、優惠券及限時促銷活動
	    
	    [:octicons-arrow-right-24: 設定優惠](#)
	
	-   :material-scale-balance: __商品分析__
	    
	    ---
	    
	    查看門市商品銷售數據與庫存報表
	    
	    [:octicons-arrow-right-24: 查看報表](#)
	
	</div>

=== "訂單與結帳"

	<div class="grid cards" markdown>
	
	-   :lucide-workflow: __訂單管理__
	    
	    ---
	    
	    處理門市訂單、退換貨與付款狀態
	    
	    [:octicons-arrow-right-24: 開始管理](#)
	
	-   :lucide-credit-card: __收銀與付款__
	    
	    ---
	    
	    支援現金、信用卡與行動支付收款
	    
	    [:octicons-arrow-right-24: 參考指南](#)
	
	-   :lucide-receipt: __電子發票__
	    
	    ---
	    
	    開立與管理電子發票，符合稅務規範
	    
	    [:octicons-arrow-right-24: 查看設定](#)
	
	-   :material-scale-balance: __報表統計__
	    
	    ---
	    
	    查看每日、每週與每月銷售分析報表
	    
	    [:octicons-arrow-right-24: 查看報表](#)
	
	</div>

=== "會員管理"

	<div class="grid cards" markdown>
	
	-   :material-clock-fast: __會員註冊與登入__
	    
	    ---
	    
	    管理會員資料、積分與帳號安全
	    
	    [:octicons-arrow-right-24: 開始管理](#)
	
	-   :lucide-gift: __會員優惠__
	    
	    ---
	    
	    設定會員專屬折扣與紅利點數
	    
	    [:octicons-arrow-right-24: 設定優惠](#)
	
	-   :lucide-users: __會員分群__
	    
	    ---
	    
	    按消費行為或會員等級分類，方便行銷推廣
	    
	    [:octicons-arrow-right-24: 查看指南](#)
	
	-   :material-scale-balance: __會員報表__
	    
	    ---
	    
	    查看會員活躍度與消費紀錄分析
	    
	    [:octicons-arrow-right-24: 查看報表](#)
	
	</div>

=== "行銷與成長"

	<div class="grid cards" markdown>
	
	-   :lucide-megaphone: __行銷工具__
	    
	    ---
	    
	    設定門市活動、通知與推播訊息
	    
	    [:octicons-arrow-right-24: 開始使用](#)
	
	-   :lucide-trending-up: __銷售成長分析__
	    
	    ---
	    
	    追蹤門市營收與促銷效果
	    
	    [:octicons-arrow-right-24: 查看分析](#)
	
	-   :material-scale-balance: __客戶回饋__
	    
	    ---
	    
	    收集顧客意見與滿意度調查
	    
	    [:octicons-arrow-right-24: 查看指南](#)
	
	</div>

=== "系統整合"

	<div class="grid cards" markdown>
	
	-   :lucide-layout-grid: __POS App 市集__
	    
	    ---
	    
	    安裝門市系統支援的插件與應用
	    
	    [:octicons-arrow-right-24: 參考指南](#)
	
	-   :lucide-webhook: __第三方服務整合__
	    
	    ---
	    
	    串接外部支付、物流、會員與行銷平台
	    
	    [:octicons-arrow-right-24: 查看文件](#)
	
	-   :lucide-plug: __API__
	    
	    ---
	    
	    使用 POS API 自動化操作與資料串接
	    
	    [:octicons-arrow-right-24: 查看指南](#)
	
	-   :material-scale-balance: __系統權限__
	    
	    ---
	    
	    管理 POS 系統角色與存取權限
	    
	    [:octicons-arrow-right-24: 查看設定](#)
	
	</div>
