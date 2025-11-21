---
title: 設定 VIP 會員專屬價格
description: 為不同 VIP 會員群組設定專屬商品價格。
product:
  - EC
module:
  - product
activ: ""
surfaces:
  - backend
devices: []
apis: []
type: tutorial
features: []
tasks: []
tnb: branch
plans:
  - 高手
  - PLUS
  - 企業
lang: zh-TW
sites:
  - TW
status: doing
doc_next: ""
tags: []
difficulty: ""
notes:
  - doc-previous 設定 VIP 會員群組 link
---

# 設定 VIP 會員專屬價格 :material-lock-outline:
為不同 VIP 會員群組設定專屬商品價格。
{ .page-subtitle } 

[:material-tag-text:](){ .badge-icon title="適用版本" }[高手 | PLUS | 企業](){ .badge-text }
[:material-arrow-left-circle:](){ .badge-icon title="相關操作"}[[設定 VIP 會員群組]]{ .badge-text }

---

## 說明概述
> 請先設定顧客 VIP 群組，才能進行會員專屬價格設定。

=== ":material-information-outline: 使用須知"
	 - [ ] 若發佈新的 VIP 規則，請務必重新設定會員專屬價格，以確保價格正確套用。

=== ":material-lightbulb-outline:  使用情境"
	- 為不同 VIP 群組設定專屬的商品價格。
	- 透過單筆、多筆編輯或 Excel 匯入方式，靈活管理 VIP 專屬價格。
	- 開啟未登入顧客顯示 VIP 優惠提示，引導潛在 VIP 會員登入以查看專屬優惠。

---

## 操作流程
### 單筆設定會員專屬價格
=== ":material-numeric-1-circle: 進入操作頁面"   
	
	  - [ ] 登入 CYBERBIZ 電商後台，前往「商品」→「所有商品」。
	  - [ ] 選擇您要設定的商品，進入「商品資訊」分頁。	
	  - [ ] 在「款式管理」區塊，點擊「編輯會員專屬價格」按鈕，進入「編輯會員專屬價格」頁面。

	  <div class="grid cards two-columns" markdown>

	 - ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定01.png)

	- ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定02.png)
	
	</div>

=== ":material-numeric-2-circle: 選擇群組"
	 - [ ] 在下拉選單中選擇欲設定的 VIP 群組名稱。
	 - [ ] 點擊「新增會員價格」新增「選擇群組」欄位，可同時替商品設定不同會員群組的專屬價格。
	
	![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定03.png){ .screenshot }

=== ":material-numeric-3-circle:  編輯會員價格"

	- [ ] 點擊「新增會員價格」，選取 VIP 群組，點擊「編輯價格」以輸入專屬價格。
	
	> 每個款式可設定不同的價格。若不設定，系統將預設帶入商品售價。
	
	![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定04.png){ .screenshot }

=== ":material-numeric-4-circle: 刪除會員價格"
	- [ ] 若要刪除某個 VIP 群組的專屬價格欄位，點擊該欄位旁的「移除」。
	- [ ] 點擊「刪除」，確認刪除該會員價格。
	
	![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定05.png){ .screenshot }

### 多筆編輯會員專屬價格

=== ":material-numeric-1-circle: 選取操作商品"
	 - [ ] 登入 CYBERBIZ 電商後台，前往「商品」→「所有商品」。
	 - [ ] 選取欲新增專屬價格的商品（可單選或多選）。
	 - [ ] 點擊上方「操作選單」:material-arrow-down-drop-circle-outline:，選擇「編輯會員專屬價格」進入編輯頁面。

	![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定06.png){ .screenshot }

=== ":material-numeric-2-circle: 選取群組"
	 - [ ] 在下拉選單中選擇欲設定的 VIP 群組名稱。

	![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定07.png){ .screenshot }

=== ":material-numeric-3-circle: 編輯會員價格"
	 - [ ] 點擊「新增會員價格」，選取 VIP 群組，並編輯該群組的專屬價格。

	- [ ] 若要刪除某個 VIP 群組的專屬價格欄位，點擊該欄位旁的「移除」。

    > 每個款式可設定不同的價格。若不設定，系統將預設帶入商品售價。

	![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定08.png){ .screenshot }


### Excel 批次匯入/修改會員專屬價格

=== ":material-numeric-1-circle: 選取操作商品"
	 - [ ] 登入 CYBERBIZ 電商後台，前往「商品」→「所有商品」。
    - [ ] 點擊上方「操作選單」:material-arrow-down-drop-circle-outline:，選擇「匯出會員專屬價格」。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定09.png){ .screenshot }

=== ":material-numeric-2-circle: 編輯 Excel 檔案"
	- [ ] 系統將發送 Excel 檔案至您的信箱，請至信箱下載。

    ![](圖示-會員專屬價格設定10.png)

    - [ ] 開啟 Excel 檔案後，在對應欄位設定商品的專屬價格，並儲存檔案。

    ![[圖示-會員專屬價格設定11.png]]

=== ":material-numeric-3-circle: 匯入 Excel 檔案"
	- [ ] 返回 CYBERBIZ 電商後台，前往「商品」→「所有商品」。
	- [ ] 點擊上方「操作選單」:material-arrow-down-drop-circle-outline:，選擇「匯入會員專屬價格」。
    - [ ] 上傳已編輯的 Excel 檔案，並點擊「確認」按鈕。

	![[圖示-會員專屬價格設定12.png]]

=== ":material-numeric-4-circle: 確認匯入成功"
	- [ ] 系統成功上傳後，會自動發送通知信件至您的信箱。

    ![[圖示-會員專屬價格設定13.png]]

---

## 進階操作
#### 未登入 VIP 標籤顯示        
此功能旨在提醒未登入的 VIP 顧客，登入後可享有更優惠的價格。

- [ ] 登入 CYBERBIZ 電商後台，前往「網站外觀」→「套版主題管理」→「網站設定」。
- [ ] 切換至「商品頁面」頁籤，找到「基本設定」區塊。
- [ ] 勾選「會員專屬價格標籤」以啟用功能。若未開啟，未登入的消費者在前台商品頁將不會看到標籤提醒。
- [ ] 在「商品 VIP 標籤連結」欄位，可設定連結至商品註冊/登入網址，引導客戶進行登入。

![會員專屬價格設定14.png](https://www.cyberbiz.io/support/wp-content/uploads/會員專屬價格設定14.png){ .screenshot }

       
### 已登入會員顯示
已登入的會員，若其所屬的 VIP 群組有設定商品的會員專屬價格，則商品頁的商品售價將會顯示設定的會員專屬價格，並同時顯示該會員所屬的 VIP 群組名稱。

=== "未開啟功能"
    ![[圖示-會員專屬價格設定-未開啟功能.png]]

=== "開啟功能 會員未登入"
    商品頁面顯示登入/註冊會員連結

    ![[圖示-會員專屬價格設定未登入畫面.png]]

=== "開啟功能 會員登入"  
    商品頁面顯示會員等級

    ![[圖示-會員專屬價格設定開啟功能登入畫面.png]]

---

## 常見問題
??? question "設定會員專屬價格後，前台會如何顯示？"
    === ":material-alert-circle-outline: 原因"
        當會員登入後，若其所屬的 VIP 群組有設定專屬價格，前台商品頁會直接顯示該專屬價格。若未登入，則會顯示原價，並可選擇開啟「未登入 VIP 標籤顯示」功能，提示顧客登入以查看優惠。
    === ":material-lightbulb-on-outline: 解決方法"
        - **已登入會員：** 系統自動顯示 VIP 專屬價格。
        - **未登入會員：** 建議開啟「未登入 VIP 標籤顯示」功能，並設定登入/註冊連結，引導顧客登入。

??? question "如果一個商品有多個 VIP 群組的專屬價格，系統會如何判斷？"
    === ":material-alert-circle-outline: 原因"
        通常系統會根據會員所屬的最高等級 VIP 群組，或依據內部設定的優先順序來顯示價格。
    === ":material-lightbulb-on-outline: 解決方法"
        請參考 CYBERBIZ 官方文件或聯繫客服，確認多個 VIP 群組價格的優先級判斷邏輯。

---

## 延伸閱讀
=== ":material-page-previous-outline: 引用連結"

=== ":material-page-next-outline: 導向連結"
	- [[設定 VIP 群組]]

=== ":material-update: 相關更新"

=== ":material-book-outline: 相關詞彙"

=== ":material-map-outline: 相關圖表"


- [[商品多層級分類設定]]
- [[商品群組：單品限時折扣]]
