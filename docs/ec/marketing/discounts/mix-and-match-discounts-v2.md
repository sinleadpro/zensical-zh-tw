---
title: 任選折扣
description: 建立「任選折扣群組」，設定件數門檻與折扣計價方式（固定金額、折數或折固定金額），並管理活動商品與有效期間。
created: 2026-01-21 00:00
last_modified: 2026-06-30 10:56
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
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 設定任選折扣
features:
  - 任選折扣
prerequisites: []
related: []
tags:
  - 多國
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 任選折扣
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1004
  - https://www.cyberbiz.io/helpcenter/?p=1065
  - https://www.cyberbiz.io/helpcenter/?p=1069
  - https://www.cyberbiz.io/helpcenter/?p=1072
  - https://www.cyberbiz.io/support/?p=1304
  - https://www.cyberbiz.io/support/?p=1335
  - https://www.cyberbiz.io/support/?p=1357
  - https://www.cyberbiz.io/support/?p=1380
  - https://www.cyberbiz.io/support/?p=7316
permalink: https://help.cyberbiz.io/ec/marketing/discounts/mix-and-match-discounts
comments: false
search:
  exclude: false
icon: lucide/tags
hide: []
---

# 新版任選折扣

建立「任選折扣群組」，設定件數門檻與折扣計價方式（固定金額、折數或折固定金額），並管理活動商品與有效期間。
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | 企業
{ .doc-badge }

!!! tip "介面改版說明"
    **任選折扣** 已推出新版介面，目前僅開放 **企業版**。其餘方案將陸續開放，敬請期待。


## 使用須知  

- 任選折扣支援 POS 系統。
- 為了支援單一商品可加入多個任選折扣活動，且避免設定衝突，商品頁的 **任選折扣群組** 欄位現已鎖定，**僅供查看、不可編輯**。

    > 後台路徑 : 商品 > 所有商品 > 點擊指定商品 > 點擊「設定」頁籤
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-商品-所有商品-綁定任選折扣群組01.png){ .screenshot }

    若想編輯商品的所屬活動，請至 「行銷活動」→「任選折扣」 設定。




## 任選折扣類型

| 類型 | 說明 | 範例 | 
| --- | ---- | ---- |
| **固定金額** | 任選 N 件，總共只要 $X 元 | 3 件 $599 | 
| **固定折扣** | 任選 N 件，組合內商品打 X 折 | 3 件 70%（即 7 折）| 
| **折固定金額** | 任選 N 件，總金額現折 $X 元 | 3 件折 $100 | 
| **每件折固定金額** | 任選 N 件，組合內每一件都折 $X 元 | 3 件每件折 $50 | 

## 任選折扣列表管理

登入電商官網後台，前往 **行銷活動 > 任選折扣**。

### 列表頁欄位說明

*   **活動名稱**：您的活動標題。點擊名稱即可進入編輯頁面修改內容。
*   **折扣類型**：顯示該活動採用的優惠邏輯。
*   **活動時間**：顯示活動的起迄日。
*   **狀態辨識**：系統會根據當前時間自動判定：
    *   **排程中**：活動尚未開始。
    *   **進行中**：活動優惠生效中。
    *   **已結束**：活動時間已過，優惠已失效。
    *   **未公開**：即便活動進行中，未公開也不會顯示活動。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-管理任選折扣群組02.png){ .screenshot }

### 搜尋活動

系統支援以下搜尋方式：

*   依 **活動名稱** 查找：輸入活動關鍵字，直接搜尋活動標題。（支援模糊搜尋）
*   依 **商品名稱** 查找：查看該商品參與的所有活動。
    *   模糊搜尋：輸入商品部分關鍵字或商品 SKU，並從下拉選單中選取符合的商品。
    *   直接選取：點擊搜尋框，由下拉選單中選取商品。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-排序活動01.png){ .screenshot }

### 篩選活動

系統支援以下條件篩選：

*   **折扣類型**：包含「固定金額」、「固定折扣」、「折固定金額」、「每件折固定折扣」
*   **活動狀態**：區分為「進行中」、「排程中」、「已結束」、「未公開」

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-篩選活動01.png){ .screenshot }

### 管理單一活動

*   :lucide-square-arrow-out-up-right: 前往任選折扣前台活動頁。
*   :lucide-eye: 將活動設為不公開。
*   :lucide-trash-2: 刪除活動。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-管理任選折扣群組01.png){ .screenshot }

## 建立任選折扣群組

### 步驟一：開啟建立流程

1.  點擊右上角 **新增任選折扣**。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立任選折扣活動01.png){ .screenshot }

2.  於彈窗中選擇活動類型，系統將帶領您進入「基本設定」頁面。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立任選折扣活動02.png){ .screenshot }

### 步驟二：完成基本設定

1.  **活動名稱**：請輸入活動標題。
2.  **網址**：您可以設定專屬的活動 URL 後綴（例如：`/summer-sale`），有利於社群分享與 SEO。
3.  **活動時間**：顯示活動的起迄日
    *   **無期限**：不指定開始與結束時間；適用於常態性活動。
    *   **指定活動期間**：指定開始與結束時間；適用於期間限定活動，時間一到系統將自動生效/下架。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立任選折扣活動03.png){ .screenshot }

### 步驟三：建立計價規則

1.  **確認計價規則**：可於此處編輯活動規則。
2.  **建立規則條件**：依活動類型設定規則。  
      
    !!! question "如何計算剩餘商品？"
        當消費者的件數「超過」組合（例如活動是 2 件一組，但買了 3 件），您可以設定：
    
        *   **以原價計算**：第 3 件恢復原價
        *   **以優惠計算**：第 3 件繼續享有折扣比例或扣減金額
    
        適用活動類型：**固定折扣、每件折固定金額**
    
3.  儲存基本設定。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立任選折扣活動04.png){ .screenshot }

## 單筆新增活動商品 

### 步驟一：開啟選品視窗

1.  點擊「選擇商品」頁籤，點擊「新增商品」。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立活動商品01.png){ .screenshot }

2.  系統將彈出商品選取視窗。您可以透過以下方式快速定位商品：
    
    *   **關鍵字搜尋**：輸入「商品名稱」或「SKU」。
    *   **進階篩選**：依照商品類型、廠商、標籤、溫層（常溫/冷藏/冷凍）或商店類別進行精確篩選。  
        註：若您的商店有使用 POS 功能，篩選器將自動顯示 POS 相關類別。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立活動商品02.png){ .screenshot }

### 步驟二：商品狀態辨識

為了避免活動衝突，系統會自動標註商品狀態：

*   **空白勾選框**：可自由選取加入。
*   **藍色勾選**：您目前選中的商品。
*   **置灰並顯示 ⓘ**：
    *   **此商品已存在其他活動群組**：該商品已在其他走期重疊的活動中，不可重複加入。
    *   **此商品已存在此活動群組**：該商品已經在此清單中，無需重複勾選。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立活動商品03.png){ .screenshot }

!!! info "活動走期重疊商品限制"
    當您欲將商品加入新的任選折扣活動，但該商品已綁定其他 **現有任選折扣活動** 時，系統判定如下：  

    *   **走期不重疊**：新舊任選折扣活動的生效期間完全錯開，商品可 **分別存在於不同時段的活動中**，系統將依時間自動切換。
    *   **走期有重疊**：若任選折扣活動期間重疊，系統 **禁止該商品重複綁定**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-走期重疊商品圖示01.png){ .screenshot }
  
    **💡 衝突解決方案：**  

    *   **方案 A：匯入時處理（批次模式）**  
        利用 **匯入活動** 功能，在匯入過程中勾選 **保留於目前活動**，將衝突商品綁定至新活動。
    
    *   **方案 B：手動調整（單品模式）**  
        於任選折扣列表頁，搜尋指定商品，即可查找到商品所屬活動。進入活動頁，解除商品綁定即可。 

    **注意事項：**

    - 系統僅比對商品是否同時存在於多個走期重疊的 **任選折扣活動**，不會檢查其他類型的行銷活動。
    

### 步驟三：勾選商品

*   **手動單選**：點擊指定商品左方勾選框。
*   **跨頁全選**：若商品眾多，您可以點擊標題列的勾選框展開選單，選擇「選取全部商品」，系統將一次勾選所有符合篩選條件的跨頁商品。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立活動商品04.png){ .screenshot }

### 步驟四：商品排程上傳

為確保前台頁面加載速度與活動品質，單一任選活動的手動新增的商品總數上限為 200 件。  
  
當您一次新增大量商品時，系統會啟動背景排程處理：

*   處理完成後，系統會自動發送電子郵件通知告知結果。
*   常見提示
    *   **走期相同**：若商品已參與其他同時間的活動，系統會要求移除該商品後方可儲存。
    *   **部分失敗**：若出現「共有 N 個商品儲存失敗」，請依照列表中的紅字提示修改後再重新儲存。

## 批次匯入活動商品

1.  點擊 **批次匯入任選折扣商品**。
2.  點擊 **下載任選折扣群組範例**。
3.  依表格格式填寫匯入商品資訊。
4.  與現有活動走期重疊的商品，選擇處理方式：
    *   **保留在目前活動**：商品綁定的折扣群組，一律依匯入檔案為主
    *   **從目前活動移除**：商品綁定的折扣群組，一律依現有後台設定為主(忽略匯入檔案)
5.  上傳檔案。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-建立活動商品05.png){ .screenshot }

## 管理活動商品

### 排序商品

您可以決定消費者在前台看到商品的先後順序。  
  

*   **自動排序**：從右上角下拉選單選擇系統自動排列方式。
    
    *   支援排序方式：標題拼音 (A-Z)、創建日期、售價高低、暢銷程度。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-排序商品01.png){ .screenshot }

*   **手動排序**：若想主打特定商品，請切換至「手動排序」模式。
    
    *   **拖拽調整**：點擊商品左側的 **⁝⁝ 六點圖示**，即可上下拖移位置。
    *   **數字輸入**：直接在排序框輸入數字（數字越小，排在越前面）。
    
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-排序商品02.png){ .screenshot }

### 移除商品

如果您想將商品退出此活動，有兩種方式：  
  

*   **單項移除**：點擊商品列末端的「刪除」圖示，並在確認視窗點擊確定。
*   **批次移除**：勾選多筆商品後，點擊頂部的 「移除商品」 按鈕，系統會再次確認預計刪除的總數量。

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-移除商品01.png){ .screenshot }


## 設定前台活動頁資訊
  
透過自定義活動描述，您可以向消費者傳遞更明確的優惠資訊與品牌視覺。  
  

1.  點擊 **活動描述** 頁籤。
2.  使用 [文字編輯器](../../website-appearance/code-customization/text-editor.md)，依品牌風格置入活動 banner、詳細說明或促銷文字。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台-行銷活動-任選折扣-編輯前台活動頁01.png){ .screenshot }
3.  儲存後，該活動專屬頁面（前台）將同步顯示您編輯的內容，協助引導消費者下單。
4.  可點擊 前往任選折扣頁，快捷前往前台活動頁。  
    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-任選折扣活動頁01.png){ .screenshot }

## 常見問題

??? quote "任選折扣群組都設定好了，為何前台還是顯示404？"
    請檢查以下條件是否都有設定正確：

    1.  已將活動設為 **已公開**
    2.  活動在有效期限內
    3.  已建立規則條件

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-行銷活動-任選折扣-檢查活動可顯示於前台01.png){ .screenshot }