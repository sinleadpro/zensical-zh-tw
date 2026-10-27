---
title: "Season Groups"
description: "Create and manage season groups in the e-commerce warehouse to group products with the same attributes or sales wave, so you can monitor the inventory age report more efficiently."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：庫齡報表
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 商品
sites:
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 建立季別群組
  - 將商品加入群組
  - 維護群組清單
features:
  - 季別群組
  - "Inventory Management"
  - 庫齡分析
  - 商品歸類
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
related:
  - wms/inventory-records/
tags:
  - WMS
  - 庫存管理
  - "Inventory Age Report"
  - "Product Management"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 季別群組列表頁
  - 新增/編輯群組頁面
  - 單一品項列表頁
paths:
  - 商品 > 季別群組
  - 商品 > 單一品項
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=8920
permalink: "https://help.cyberbiz.io/wms/seasonal-groups/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Season Groups
Create and manage season groups in the e-commerce warehouse to group products with the same attributes or sales wave, so you can monitor the inventory age report more efficiently.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-商品-季別群組-畫面總覽01.en.png){ .hero-page }

## Use Cases { #intro-seasonal-groups }

- **Targeted monitoring**: Filter the inventory age report by **season** to quickly see which sales waves have been in stock too long.


## Create a Season Group { #operate-seasonal-groups-create }

1. Go to **Products > 季別群組**.
2. Click **Create Product Seasons** in the upper-right corner.
3. Enter a group name (for example, 2026 Spring/Summer or Christmas Limited Edition).
4. Enter the item numbers of the products for this season. The system links the products automatically.
5. Click **Done** to save.

![](../assets/images/WMS-後台-商品-季別群組-新增季別群組01.en.png){ .screenshot }

## Add Products to a Season Group { #operate-seasonal-groups-add }

After you create a group, add products to it from the single product list.

1. Go to **Products > 單一品項**.
2. Click the product you want to add to the group.
3. In the **Season Group** field, select the group name.
5. Click **Save** to finish.

![](../assets/images/WMS-後台-商品-單一品項-綁定季別群組01.en.png){ .screenshot }

## Manage Groups { #operate-seasonal-groups-maintain }

You can change groups or remove products that do not fit at any time.

- **Edit or delete a group**: On the **Season Group** details page, click **Edit** next to a group to rename it, or click **Delete** to remove the whole group (physical products are not affected).
- **Remove products**: In the group details, remove specific products from the group.
- **View the data**: Go to **庫存紀錄 > [庫齡報表](inventory-records/#operate-inventory-turnover)** to see the season information in the matching column.

![](../assets/images/WMS-後台-商品-季別群組-編輯與刪除01.en.png){ .screenshot }

## Next Steps { #next-steps-seasonal-groups }

<div class="grid cards" markdown>

- :lucide-file-chart-pie:{ .lg }
  [__View Inventory Analysis Reports__](inventory-records/)
  See how inventory turns over and review its change history.

</div>
