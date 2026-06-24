---
title: 全館折扣
description: 對全站所有商品統一套用折扣優惠。此活動同步支援 EC 與 POS，可依方案指定線上、線下或全通路開啟。
created: 2026-06-24 16:30
last_modified: 2026-06-24 16:30
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
    - EC
    - POS
modules: 
    - 行銷活動
sites: 
    - TW
audiences: 
    - admin
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents: 
    - 了解全館折扣規格
    - 搜尋與篩選全館折扣活動
    - 自定義全館折扣列表欄位
    - 建立全館折扣活動
    - 編輯全館折扣活動
    - 查看全館折扣編輯紀錄
features: 
    - 全館折扣
    - 折扣門檻
    - 折扣累積
    - 優惠券折扣
    - 編輯紀錄
    - 活動通路設定
prerequisites: []
related: []
tags: 
    - 全館折扣
    - 行銷活動
    - 促銷優惠
    - EC
    - POS
acoiv: configure
apis: []
devices: []
ui_components: 
    - 編輯欄位
    - 篩選
    - 搜尋
    - 編輯紀錄
paths: 
    - 行銷活動 > 全館折扣
layouts: []
wp_url:
    - https://www.cyberbiz.io/helpcenter/?p=1165
    - https://www.cyberbiz.io/support/?p=30011
permalink: ""
comments: false
search:
  exclude: false
icon: lucide/layers
hide: []
---
# 全館折扣
對全站所有商品統一套用折扣優惠。此活動同步支援 EC 與 POS，可依方案指定線上、線下或全通路開啟。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | EC / POS
{ .doc-badge }

## 全館折扣規格

「全館活動」是行銷模組中的一項特定活動，設定後將針對 **全站所有商品** 統一套用折扣優惠。  
  
此活動同步支援 EC 與 POS，系統將依據您所使用的方案類型，提供對應的通路選擇權限：  
  

| 系統方案 | 適用通路 |
| ------- | ------- |
| **純 EC（線上商城）** | 僅限官方購物網站使用 |
| **純 POS （線下門市）** | 僅限實體門市 POS 端使用 |
| **EC +POS** | 可指定活動通路<br>- **線上**：僅限官方購物網站使用<br>- **線下**：僅限實體門市 POS 端使用<br>- **全通路**：線上與線下通路同步開啟優惠 | 


## 列表管理  

### 搜尋

前往 **行銷活動 > 全館折扣**，您可依活動名稱查詢指定活動。  

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-搜尋01.png){ .screenshot }

### 篩選

您可依以下條件篩選指定活動：  
  

*   **適用通路**：「線上」、「線下」、「全通路」  
    (僅限同步啟用 EC + POS 的站台使用，純 EC 或 純 POS 站台不顯示此篩選條件。)
  
*   **狀態**：「排程中」、「進行中」、「已結束」

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-篩選01.png){ .screenshot }

### 自定義列表欄位

您可依據個人閱覽需求，彈性調整列表的欄位排序。  
  
**操作方式**

1.  點擊右方「編輯欄位」按鈕。
2.  於選單中勾選欲顯示的欄位，或取消不需顯示的欄位。
3.  點擊 ⁝⁝，拖曳排序欄位。
4.  列表將根據您的勾選結果即時更新顯示。

    <div class="grid cards borderless two-columns" markdown>

    - ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯列表欄位01.png){ .screenshot }
    - ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯列表欄位02.png){ .screenshot }

    </div>


## 建立全館折扣 

### 步驟一：填寫基本設定

前往 **行銷活動 > 全館折扣**，依序填寫以下欄位：

*   折扣活動名稱
*   活動期間：可選「無期限」或「指定期限」
*   適用通路：若站台同步啟用 EC +POS，可指定活動適用通路。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-基本設定01.png){ .screenshot }

### 步驟二：填寫折扣設定

請依據您選擇的 **折扣類型**，設定對應欄位：

=== "金額"
    
    *   **折扣門檻**：填寫觸發折扣的最低消費金額。
    *   **折扣金額**：設定具體的折抵數額。
    *   **是否折扣累積**：勾選是否支援隨門檻倍增而重複累計折扣。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-金額設定01.png){ .screenshot }
    
=== "百分比"
    
    *   **折扣門檻**：填寫觸發折扣的最低消費金額。
    *   **折扣百分比**：設定具體的折扣百分比。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-百分比設定01.png){ .screenshot }
    
=== "優惠券"
    
    *   **折扣門檻**：填寫獲得優惠券的最低消費金額。
    *   **優惠券金額**：填寫優惠券的折抵金額。
    *   **使用天數**：設定優惠券的有效期限。
    *   **消費使用門檻**：規定訂單需滿多少金額，才能在結帳時套用優惠券。
    *   **綁定商品標籤**：指定特定標籤的商品，方可套用優惠券折抵。
    *   **與其他行銷活動併用限制**：設定此券是否可與其他行銷活動同時使用。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-優惠券設定01.png){ .screenshot }
    



## 編輯全館折扣

您可依需求編輯已建立的活動，系統將根據「活動狀態」開放不同的編輯權限：  
  

| 活動狀態 | 可編輯欄位 |
| ------- | ---------- |
| **排程中** | 全部欄位 | 
| **進行中** | - 全館折扣名稱<br>- 結束時間 `註一`<br>- 優惠券使用天數 `註二` |

點擊活動名稱，即可進入編輯頁。調整內容前，請先確認目前活動狀態及其對應的可修改項目。  
![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯活動01.png){ .screenshot }

- `註一`：
    - 結束時間需不可早於於儲存編輯時的時間。  
    - 如果在建立活動時選擇 **無期限**，後續不能編輯活動期間。
    - 如果在建立活動時選擇 **指定期間**，則可以編輯結束時間。
- `註二`：當折扣類型設定為「優惠券」時，方有此欄位可供編輯。


## 查看編輯紀錄 
  
您可於活動編輯頁下方查看編輯紀錄，系統會依據「活動狀態」決定是否建立記錄：  
  
| 活動狀態 | 是否建立編輯紀錄 |
| 排程中 | ✕ |
| 進行中 | ✓ |


排程中活動的調整不留紀錄，而進行中活動的異動則會留存以供備查。  
![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-全館折扣-編輯紀錄01.png){ .screenshot }