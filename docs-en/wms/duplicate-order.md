---
title: "Clone Orders"
description: "When you clone an order that came into WMS from an e-commerce platform (such as CYBERBIZ or Shopline), the system offers the **Link EC platform** option. It lets you decide whether the new order's shipping status is synced back to the original platform, or whether it is handled as a fully independent WMS order."
created: 2026-07-17 11:20
last_modified: 2026-07-27 17:00
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products: 
  - WMS
modules: 
  - 訂單
sites: 
  - TW
audiences: []
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents: 
  - 複製_WMS_訂單
  - 處理換貨與補出商品
  - 管理_EC_訂單關聯
features: 
  - "Clone Order"
  - 關聯 EC 平台
prerequisites: []
related: []
tags: 
  - 複製訂單
  - "Order Management"
  - "Shipping Status Sync"
acoiv: operation
apis: []
devices: 
  - desktop
ui_components: 
  - 複製訂單按鈕
  - 關聯_EC_平台勾選框
paths: 
  - 訂單 > 列表
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/duplicate-order/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---
# Clone Orders
When you need to change an existing order or ship it again, use Clone Order to create a new order quickly. You can also choose whether to keep its link to the original e-commerce platform (EC).
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

## Overview { #intro-duplicate-order }

- **One-click cloning**: When you need to correct an existing order or ship it again, use Clone Order to create a new order and edit its details.
- **Shipping status sync**: The system offers the **Link EC platform** option. It lets you decide whether the new order's shipping status is synced back to the original platform, or whether it is handled as a fully independent WMS order.


## Differences Between Clone Modes { #overview-duplicate-order-modes }

Whether you select Link EC platform changes what the new order inherits and how its shipping status is synced back:

=== "Link EC Platform"

    The cloned order **inherits the original order's EC platform link**:

    - **Status sync**: The new order takes over the original order's sync rights, so later shipping statuses are synced back to the EC platform as usual.
    - **Link transfer**: The original order is unlinked from the EC platform. This makes sure each EC transaction maps to only one order that syncs status back.
    - **Settings kept**: The order's sales channel and shipping method stay the same as on the original EC platform.

    !!! example "When to Use"
        Use this option when the original order needs to be **changed and shipped**, and you still want customers on the e-commerce platform to get the latest shipping updates.


=== "Do Not Link EC Platform"

    The cloned order is **fully unlinked from the EC platform**:

    - **No status sync**: None of the new order's shipping status updates (such as Shipped or Received) are **synced** back to the e-commerce platform.
    - **Original order unchanged**: The original order keeps its link to the EC platform.
    - **Channel change**: The new order's channel changes to **Other**, and its shipping method changes to the matching standard shipping type.

    !!! example "When to Use"
        Use this option when you clone an order to **exchange items** or **send missing items**. The new order only needs to ship from WMS and does not affect the original order's status. **Be sure to clear the Link EC platform checkbox.** Otherwise, the original order's shipping status can no longer be synced back to the e-commerce platform.

## Notes { #prerequisites-duplicate-order }

- **Default selection**: Each time you open the clone window, the checkbox is **selected** by default.
- **Specific channels**: This feature only applies to orders from integrated EC channels such as CYBERBIZ and Shopline. Standard orders are not affected.
- **Shipping**: Whether or not you select the option, a cloned order is always treated as a new order and ships through the normal process.
- **Deleted product warning**: If the original order contains a product that was deleted from the system, that product is not cloned, and the system shows a warning.
- **Manual handling risk**: If a wrong link setting stops the shipping status from syncing back, contact customer service to fix the order. Extra technical fees may apply.

## Steps { #operate-duplicate-order }

1. Log in to the e-commerce warehouse admin panel, go to **Orders > 列表**, and open the details page of the order you want to clone.
2. Click **Clone Order** in the upper-right corner of the page.
3. A clone confirmation window opens. If the order came from an EC integration, the window shows the **Link EC platform** checkbox.
4. Select or clear the checkbox based on your shipping needs, and then click **OK** to finish cloning.

    > Standard orders that are not from an EC integration (such as manually created orders) do not show this checkbox and use the usual clone process.

    === "Link EC Platform"

        ![](../assets/images/WMS-後台-訂單-列表-複製訂單01.en.png){ .screenshot }

    === "Do Not Link EC Platform"

        ![](../assets/images/WMS-後台-訂單-列表-複製訂單02.en.png){ .screenshot }

## FAQ { #faq-duplicate-order }

??? quote "What Is an EC Order?"
    An order that comes into WMS from an integrated e-commerce platform such as CYBERBIZ or Shopline.

??? quote "Is the Original EC Order Still There After Cloning?"
    Yes. Cloning creates a brand-new WMS order. It does not delete or overwrite the original order record.

??? quote "Has the Clone Process Changed for Standard (Non-EC) Orders?"
    No. Orders that are not from an EC integration use the same clone process as before, and the Link EC platform option does not appear.

??? quote "What Happens If I Choose the Wrong Option When Resending Items?"
    If you select Link EC platform by mistake when resending items, the original order's link to the e-commerce platform **moves** to the resend order. The original, complete order can then no longer sync its shipping status back correctly.
