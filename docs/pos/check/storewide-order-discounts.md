---
title: 整筆訂單折扣
description: 門市人員在結帳時能針對整筆訂單進行彈性改價。管理員可決定是否開放此權限給一般店員，並能追蹤每一筆手動改價的備註紀錄。
created: 2026-04-27 15:00
last_modified: 2026-04-27 15:00
lang: zh-TW
type: tutorial
status: update
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
    - POS
modules: 
    - 結帳
sites: 
    - TW
audiences: 
    - admin
    - clerk
difficulty: beginner
tnb: branch
plans: 
    - 進階PLUS
    - 高手PLUS
    - 企業
cyb_extensions: []
intents: 
    - 設定 POS 整筆訂單折扣
    - POS 前台彈性改價
    - 管理 POS 店員改價權限
features: 
    - POS_整筆訂單折扣
    - 店長改價權限
    - 改價備註記錄
prerequisites: []
related: []
tags: 
    - POS_折扣
    - 整筆改價
    - 權限管理
    - 結帳優惠
acoiv: operation
apis: []
devices: 
    - desktop
    - tablet
ui_components: 
    - 新增整筆訂單折扣
    - 改價備註
    - POS 權限管理
paths: 
    - POS 前台 > 結帳頁面
    - POS 後台 > POS 功能 > POS 權限管理
layouts: []
wp_url: 
    - https://www.cyberbiz.io/support/?p=35401
permalink: "https://help.cyberbiz.io/pos/check/storewide-order-discounts/"
comments: false
search:
  exclude: false
icon: lucide/badge-percent
hide: []
---

# 整筆訂單折扣
門市人員在結帳時能針對整筆訂單進行彈性改價。管理員可決定是否開放此權限給一般店員，並能追蹤每一筆手動改價的備註紀錄。
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | 智能 POS
{ .doc-badge }

!!! tip "應用情境"
    - **臨櫃特殊優惠**：當顧客符合特殊促銷條件或老客戶到店時，店員可手動套用折扣。
    - **零頭處理**：結帳金額出現零頭時，透過整筆改價功能進行去零頭處理。
    - **店長授權核價**：店員無權限時，由店長介入輸入折扣，強化改價行為的管控。



## 使用須知

- **權限限制**：本功能預設僅開放給 **店長** 身分。一般店員需由管理員從後台下放權限。
- **改價記錄**：每一筆整筆折扣都必須輸入 **改價備註**，系統會記錄備註內容以供後續對帳查核。
- **備註快選**：系統會自動記錄最近 5 筆的改價備註，方便店員快速點選。


## 操作流程

### 任務一：POS 前台執行整筆折扣

店員在結帳過程中，可隨時針對購物車內的總金額進行調整。

1. 在 POS 前台 **結帳頁面**，依改價形式選擇操作位置：
    - **整筆訂單改價**：選擇商品，開啟下拉選單，點擊 **店長改價** 欄位。
    - **指定商品改價**：點選列表右方 **新增整筆訂單折扣**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS前台-整筆訂單折扣01.png){ .screenshot }

2. 選擇折扣形式並輸入數值：

    - **常用折扣**：系統自動紀錄店員輸入的近 5 筆折扣紀錄，以利門市人員快速套用折扣。

    === "金額"

        輸入欲折抵的固定金額。
        
        ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台-結帳-整筆訂單折扣01.png){ .screenshot }

    === "百分比"
        
        輸入折扣比例（如：輸入 10 代表 9 折）。

        ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-前台-結帳-整筆訂單折扣01.png){ .screenshot }

3. 在 **改價備註** 欄位輸入改價原因（如：去零頭、店長特惠）。
4. 點擊 **確認** 套用折扣。
    - 若需修改，可點擊折扣金額旁的 **編輯** 圖示重新設定。

!!! tip "如何查閱訂單改價紀錄"
    若需查看手動調整價格的紀錄，可登入管理後台，前往 **訂單 > [訂單報表匯出](../../ec/orders/reports/export-order-report.md)**，選擇匯出 **整筆訂單折扣**、**整筆訂單折扣備註** 欄位，即可查看資訊。
    


### 任務二：後台開啟店員改價權限

若需讓一般店員也能執行改價，請由管理員在後台完成設定。

1. 登入 CYBERBIZ 管理後台，前往 **POS 功能 > 權限管理**。
2. 點選 **設定身分權限**。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS前台-店長改價06.png){ .screenshot }

3. 選擇目標員工的職位或身分。
4. 找到 **整筆訂單折扣** 選項，將開關切換為 `開啟`。

    ![](https://www.cyberbiz.io/support/wp-content/uploads/POS前台-整筆訂單折扣06.png){ .screenshot }

5. 點擊 **更新身分** 完成授權。

## 更多操作

<div class="grid cards" markdown>

- :lucide-hash:{ .lg }
    [__員工權限與帳號管理__](../store/staff-permissions-and-account-management.md)
    了解門市人員功能權限的完整設定與管理流程。

</div>
