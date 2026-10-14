---
title: 設定出貨文件列印排序
description: 在結帳頁與物流設定選擇批次列印出貨文件時，依文件類型或依訂單編號排列。
created: 2026-09-17 16:50
last_modified: 2026-09-23 14:20
lang: zh-TW
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 訂單
  - 金物流
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
cyb_extensions: []
intents:
  - 設定出貨文件列印排序
features:
  - 列印出貨文件排序設定
prerequisites: []
related:
  - ec/orders/home-delivery/tcat-home-delivery-v2/
  - ec/orders/tcat-quick-store/tcat-quick-store-shipping/
tags:
  - 出貨文件
  - 列印排序
  - 黑貓
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 列印出貨文件排序設定
paths:
  - 金物流 > 結帳頁 & 物流設定
  - 訂單 > 所有訂單
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/orders/order-settings/setup-shipping-docs-sort/"
comments: false
search:
  exclude: false
icon: lucide/list-ordered
hide: []
---

![列印出貨文件排序設定](../../../assets/images/EC-後台-金物流-結帳頁物流設定-列印出貨文件排序01.png){ title="列印出貨文件排序設定" .hero-page }

## 出貨文件列印排序說明

批次列印多張訂單時，PDF 裡各張紙的順序會影響揀貨台怎麼拆、打包員能不能一次拿到同一筆訂單。請先依現場作業選排序，再從訂單列表出貨列印。

- **適用物流**：僅適用與 CYBERBIZ 直串的 **黑貓宅配**、**黑貓快速到店**。


### 選擇列印方式

=== "依文件類型（預設）"

    - **排列方式**：先列印全部訂單的揀貨單，次為託運單，接著為出貨明細，最後為訂單明細。

    - **適用情境**：適合分批或流水線作業，相同類型的文件可直接集中成一疊處理。

    - **列印範例**：

        - 第一步：揀貨單`訂單 A` > 揀貨單`訂單 B` > 揀貨單`訂單 C` > 揀貨單`訂單 D`
        - 第二步：託運單`訂單 A` > 託運單`訂單 B` > 託運單`訂單 C` > 託運單`訂單 D`
        - 第三步：出貨明細`訂單 A` > 出貨明細`訂單 B` > 出貨明細`訂單 C` > 出貨明細`訂單 D`
        - 第四步：訂單明細`訂單 A` > 訂單明細`訂單 B` > 訂單明細`訂單 C` > 訂單明細`訂單 D`

=== "依訂單編號"

    - **排列方式**：依據訂單編號分組排列。將單一訂單所勾選的所有文件連續印出後，再印下一筆訂單的文件，同一類型內的預設順序為：揀貨單 → 託運單 → 出貨明細 → 訂單明細。

    - **適用情境**：適合單筆訂單獨立打包作業，無需手動整理分類，同一訂單所需文件一次到位。

    - **列印範例**：

        - 第一步：揀貨單`訂單 A` ➔ 託運單`訂單 A` ➔ 出貨明細`訂單 A` ➔ 訂單明細`訂單 A` 
        - 第二步：揀貨單`訂單 B` ➔ 託運單`訂單 B` ➔ 出貨明細`訂單 B` ➔ 訂單明細`訂單 B`
        - 第三步：揀貨單`訂單 C` ➔ 託運單`訂單 C` ➔ 出貨明細`訂單 C` ➔ 訂單明細`訂單 C`
        - 第四步：揀貨單`訂單 D` ➔ 託運單`訂單 D` ➔ 出貨明細`訂單 D` ➔ 訂單明細`訂單 D`






## 操作步驟

1. 登入 CYBERBIZ 管理後台，前往 **金物流 > 結帳頁 & 物流設定**。
2. 展開 **列印出貨文件排序設定**。
3. 選擇一種排序。下次從訂單列表執行 **進行出貨/列印文件** 時，PDF 會依此排列。




## 後續操作

實際出貨與列印步驟請見：

<div class="grid cards" markdown>

- :lucide-cat:{ .lg }  
  [__黑貓宅配出貨__](../home-delivery/tcat-home-delivery-v2.md){ title="使用黑貓宅配出貨" }  
  從訂單列表進行出貨、列印或下載宅配出貨文件。

- :lucide-truck:{ .lg }  
  [__黑貓快速到店出貨__](../tcat-quick-store/tcat-quick-store-shipping.md){ title="使用黑貓快速到店出貨" }  
  從訂單列表進行出貨、列印或下載快速到店出貨文件。

</div>

