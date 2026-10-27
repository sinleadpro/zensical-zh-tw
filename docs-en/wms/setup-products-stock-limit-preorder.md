---
title: "Set up Products (In Stock, Limited, Preorder)"
description: "When you connect to the e-commerce warehouse (WMS), set how stock is synced for each sales strategy: in stock, limited quantity, or preorder."
created: 2026-03-19 00:00
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 使用須知恢復同步為ai製作，是否符實
ga_views: 0
feedback: 0
products:
  - WMS
  - EC
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
  - 設定限量銷售
  - 設定預購模式
  - 管理同步開關
features:
  - 現貨銷售
  - 限量銷售
  - 預購銷售
  - 庫存同步
prerequisites:
  - 需已開通 CYBERBIZ 電商倉儲服務
  - 商品必須已填寫商品 SKU（不可為空）
related: []
tags:
  - "In Stock"
  - "Limited Quantity"
  - Preorder
  - WMS
  - "Stock Settings"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 官網管理後台
  - 商品編輯頁面
paths:
  - 商品管理 > 商品列表 > 編輯商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5714
  - https://www.cyberbiz.io/helpcenter/?p=5720
  - https://www.cyberbiz.io/support/?p=9658
permalink: "https://help.cyberbiz.io/wms/setup-products-stock-limit-preorder/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Set up Products (In Stock, Limited, Preorder)
When you connect to the e-commerce warehouse (WMS), set how stock is synced for each sales strategy: in stock, limited quantity, or preorder.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## Before You Start { #prerequisites-stock-modes }

- **One mode per order**: Each order supports only **one shipping mode**. If an order contains products of different types (such as in stock + preorder), the system cannot handle mixed or split shipping.
- **Turn sync back on**: When a campaign ends or a product goes back to normal in-stock sales, be sure to **turn on** warehouse inventory sync again to restore the true stock level.

!!! warning "Setup Risk"
    If overselling happens because a preorder or limited-quantity setting was wrong (for example, sync was turned off by mistake and the numbers drifted apart), CYBERBIZ cannot offer compensation beyond advice on system operation. Check your settings carefully before you launch a sales campaign.


## In-Stock Sales Mode { #specs-stock-in-stock }

The normal sales flow. Use it when the product has physical stock in the warehouse.

1. **Basic setup**: The product has a **product SKU**, and the initial stock sync between the online store (EC) and the warehouse (WMS) is done.
2. **How it works**:
    - Turn on **Sync inventory with warehouse**.
    - When a customer places an order and the system confirms WMS has available stock, the order is passed to WMS right away for shipping.


## Limited Sales Mode { #specs-stock-limited }

Use this for flash sales or a set allocation, when you want to release only part of the warehouse stock to the online store.

1. **Adjust stock**: Manually change **Quantity** to the **quantity available for this sale**.

    > For example, total physical stock is 200, but you set only 100 for this campaign.

2. **Set the sales rule**: Set the **Insufficient Stock** field to **Stop selling**.
3. **Turn off sync**: **Turn off** warehouse inventory sync so that WMS physical stock does not overwrite the limited quantity.
4. **Result**: The product is taken off the online store automatically once the limited quantity sells out, which prevents overselling.

![](../assets/images/EC-後台-商品-所有商品-款式管理-串倉商品設定限量預購01.en.png){ .screenshot }


## Preorder Sales Mode { #specs-stock-preorder }

Use this when products are not in the warehouse yet but you want to take orders now. There are two types: limited preorder and unlimited preorder.

### 1. Limited Preorder { #specs-stock-preorder-limited }

1. **Set stock**: Change the stock to the **expected preorder quantity** (the total you expect to receive later).
2. **Sales rule**: Set **Insufficient Stock** to **Stop selling**.
3. **Turn off sync**: **Turn off** warehouse inventory sync.
4. **Result**: Orders are passed to WMS, but because WMS has no stock yet, they stay in **Insufficient Stock**. After the goods arrive at the warehouse, the orders can be fulfilled automatically or manually.

![](../assets/images/EC-後台-商品-所有商品-款式管理-串倉商品設定限量預購01.en.png){ .screenshot }

### 2. Unlimited Preorder { #specs-stock-preorder-unlimited }

1. **Set stock**: Set the stock to **0** or to the **expected preorder quantity**.
2. **Sales rule**: Set **Insufficient Stock** to **Continue selling**.
3. **Turn off sync**: **Turn off** warehouse inventory sync.
4. **Result**: Customers can keep ordering. WMS receives the orders but holds shipping because of the shortage.

![](../assets/images/EC-後台-商品-所有商品-款式管理-串倉商品設定不限量預購01.en.png){ .screenshot }
