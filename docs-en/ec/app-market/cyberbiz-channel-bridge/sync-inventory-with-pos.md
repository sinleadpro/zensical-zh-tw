---
title: "Set up Shared Inventory Between POS and the Online Store"
description: "In Channel Bridge, sync inventory for selected POS stores so matching SKUs on the online store and in-store share one stock pool. You can cancel sync anytime."
created: 2026-09-16 16:35
last_modified: 2026-09-16 16:35
lang: en-US
type: guide
status: ""
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - APP MARKET
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions:
  - CHANNEL BRIDGE
intents:
  - 設定_POS_官網商品共庫
  - 同步門市庫存
  - 取消庫存同步
features:
  - 商品共庫
  - 同步庫存
  - 取消同步庫存
prerequisites:
  - 需同時使用官網與 POS
  - 需向客服申請開啟共庫功能
related:
  - pos/inventory/
  - ec/products/bulk-operations/copy-products-to-pos-stores/
tags:
  - POS
  - "Shared inventory"
  - "Inventory sync"
  - CHANNEL_BRIDGE
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 同步庫存
  - 取消同步庫存
  - 操作紀錄
  - 關聯平台
paths:
  - APP MARKET > 我的擴充服務 > CYBERBIZ CHANNEL BRIDGE
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app-market/cyberbiz-channel-bridge/sync-inventory-with-pos/"
comments: false
search:
  exclude: false
icon: lucide/warehouse
hide: []
---

# Set up Shared Inventory Between POS and the Online Store
Let selected POS stores share one inventory pool with matching SKUs on the online store. After you enable sync, inventory stays aligned on both sides; after you cancel, each side counts inventory separately again.
{ .subtitle }

[:lucide-layers:{ title="Applicable products" }](../../resources/conventions.md#適用產品) | Brand online store / Smart POS<br>
[:lucide-grid-2x2-plus:{ title="Applicable apps" }](../../resources/conventions.md#適用擴充) | CYBERBIZ CHANNEL BRIDGE
{ .doc-badge }

!!! tip "Use cases"
    - **Shared inventory**: The online store and the store have the same SKUs. After you enable shared inventory, both sides share one inventory pool.
    - **Cancel shared inventory**: After you cancel inventory sync, each side counts from the current quantity separately.

## Before You Start { #prerequisites-inventory-sync }

* **Supported systems**: This feature requires both the **online store (EC)** and the **POS system**.
* **How to enable**: Contact **CYBERBIZ support** to request access.
* **Prepare first**: Before you turn on inventory sync, **set EC stock to the quantity you want after shared inventory is enabled**.
* **Initial sync rule**: After sync starts, POS product stock is overwritten and synced to match **EC product stock**.
* **Scope**: Inventory sync applies only to **products that exist on both the online store and that POS store with matching SKUs**.

## Steps { #operate-inventory-sync }

### Enable Shared Inventory { #operate-inventory-sync-enable }

1. Sign in to the CYBERBIZ admin and go to **APP MARKET > My Apps**.
2. Next to CYBERBIZ CHANNEL BRIDGE, click **Settings**.

    ![](../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店04.en.png)

3. In the **CYBERBIZ POS store** section, click **Go to sync**.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-設定POS商品共庫02.en.png)

4. Open the **Store settings** tab and select the POS stores to share inventory with the online store.


5. Click **More actions**, then choose **Sync inventory**. The system syncs inventory for that store with the online store.

    ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-設定POS商品共庫03.en.png)


### Check Shared Inventory Status { #operate-inventory-sync-status }

1. Go to **Products > All Products**.
2. For POS products already sharing inventory with the online store, the **Linked platforms** field shows a blue POS icon.
3. For POS products not yet sharing inventory, the POS icon is gray.

![](../../../assets/images/EC-後台-商品-所有商品-設定POS商品共庫01.en.png)

### Cancel Shared Inventory { #operate-inventory-sync-cancel }

1. Go to **APP MARKET > My Apps**, then go to **CYBERBIZ CHANNEL BRIDGE > CYBERBIZ POS門市**.
2. Open the **Store settings** tab and select the POS stores to stop sharing inventory.
3. Click **More actions**, then choose **Cancel inventory sync**. The system cancels shared inventory for that store with the online store.

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-設定POS商品共庫04.en.png)

### View Activity Logs { #operate-inventory-sync-logs }

Open the **Activity log** tab to review **Sync inventory** and **Cancel inventory sync** records.

![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-設定POS商品共庫05.en.png)

  - **Progress status**: Shows sync progress.
  - **Details**: Review products that did not finish syncing and the reasons.

      ![](../../../assets/images/EC-後台-APPMARKET-我的擴充服務-設定POS商品共庫06.en.png)

## How Shared Inventory Works { #specs-inventory-sync }

POS stores set to share inventory with the online store share inventory for matching SKUs. After inventory changes on the online store or that store, both sides stay aligned. After you cancel inventory sync, each side resumes separate counts from the current quantity.

### Scenario 1: Enable Shared Inventory { #specs-inventory-sync-enable }

Starting state: online store inventory 10 / POS store inventory 5

- **Step 1｜** Start sync -> both sides are overwritten to 10

- **Step 2｜** Online store sells 1 unit -> both sides sync down to 9

- **Step 3｜** POS manually adds +5 stock -> both sides sync up to 14

### Scenario 2: Cancel Shared Inventory { #specs-inventory-sync-cancel }

Starting state: both sides are at 10

- **Step 1｜** Cancel sync -> each side counts independently again (both stay at 10)

- **Step 2｜** Online store sells 1 unit -> storefront inventory drops to 9; POS store inventory stays at 10 (no longer syncs down)


## FAQ { #faq-inventory-sync }

??? quote "Which products does inventory sync apply to?"
    Inventory sync applies only to SKUs that exist on both the online store and the selected POS store. SKUs missing from the store are not synced.

??? quote "Which side is the source of truth after sync?"
    After inventory sync, POS product inventory follows EC product inventory. Before you enable it, set online store inventory to the quantity you want after shared inventory starts.

??? quote "How can I tell whether a POS product already shares inventory?"
    Open the product list and check the **Linked platforms** field. A blue POS icon means shared inventory with the online store is on; gray means it is not.


## Next Steps { #next-steps-inventory-sync }

<div class="grid cards" markdown>

- :lucide-warehouse:{ .lg }
  [__Inventory management__](../../../pos/inventory/index.md)<br>
  Review warehouse split between the online store and stores, inbound/outbound transfers, and stock counts.

- :lucide-copy:{ .lg }
  [__Create POS products__](../../../pos/get-started/create-pos-products.md)<br>
  Sync-create EC products into POS stores to finish product setup before shared inventory.
  

- :lucide-file-spreadsheet:{ .lg }
  [__Bulk-fill product SKUs__](../../../pos/get-started/bulk-update-product-skus.md)<br>
  Use Excel to fill product SKUs in batches so online store and POS products can sync inventory on matching SKUs.
  
</div>

