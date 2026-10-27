---
title: "Store Assistant"
description: "An OMO sales tool designed for physical stores. It brings together online store member data and assets so staff can recognize customers, gain deeper insights, and turn them into sales."
created: 2026-05-05 11:20
last_modified: 2026-07-09 10:29
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - "Store Assistant"
  - APP MARKET
sites:
  - TW
audiences:
  - merchant
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions:
  - STORE PAL
intents:
  - 了解門市助理功能
  - 開始使用門市助理
  - 導覽門市助理介面
features:
  - 門市助理
  - OMO 銷售
  - 會員數據
  - 資產核銷
prerequisites: []
related:
  - ec/app-market/storepal/search-and-create-members/
  - ec/app-market/storepal/member-identification/
  - ec/app-market/storepal/member-data-warehouse/
  - ec/app-market/storepal/sales-conversion/
  - ec/app-market/storepal/view-sales-performance/
tags:
  - 門市助理
  - OMO
  - "Targeted Selling"
  - Overview
acoiv: activate
apis: []
devices:
  - tablet
  - mobile
ui_components: []
paths:
  - APP MARKET > 我的擴充服務 > 門市助理
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?page_id=42126
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/"
comments: false
search:
  exclude: false
icon: lucide/users
hide: []
---

# Store Assistant
An OMO sales tool built for physical stores. It brings together your online store's member data and assets to help store staff recognize customers, gain deeper insights, and turn them into sales.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

Store Assistant connects your physical stores with your online store. On a tablet or phone, store staff can instantly see a member's purchase history across all channels and their available offers, turn walk-in shoppers into loyal fans, and use referral links to make sure every effort is credited through sales attribution.

---

## Interface Overview { #overview-storepal }

The Store Assistant frontend follows a sales flow that goes from simple to detailed and from left to right, with three main areas:

```mermaid
graph LR
    subgraph ClerkUI [門市助理前台介面]
        direction LR
        Mod1["<b>左側/頂端：精準識客</b><br/>(身份識別、標籤標註)"]
        Mod2["<b>中段：深度洞察</b><br/>(等級權益、消費分析、註記)"]
        Mod3["<b>右側：價值變現</b><br/>(核銷、推薦商品、手動紀錄)"]

        Mod1 --> Mod2
        Mod2 --> Mod3
    end
```

1.  **Customer Recognition (Left/Top)**: Quickly confirm who the customer is and see their tags.
2.  **Insights (Middle)**: See data on the customer's spending power, preferences, and current benefits.
3.  **Conversion (Right)**: Close the sale, including redeeming assets, generating referral links, or recording in-store purchases.

---

## Guides { #reference-storepal }

Choose the guide that matches what you need to do:

### Setup and Member Sign-Up { #reference-storepal-section }

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }
  __Sign Up and Link Store Members__
  Guide customers to scan a QR code to sign up, and link them to store staff as their referrer.<br>
  [View Guide](search-and-create-members.md)

</div>

### Member Management and Data { #reference-storepal-member }

<div class="grid cards" markdown>

- :lucide-search:{ .lg }
  __01. Customer Recognition__
  Identify members and use tags. Quickly confirm VIP levels and understand customer traits.<br>
  [View Guide](member-identification.md)

- :lucide-bar-chart-3:{ .lg }
  __02. Data Insights__
  Analyze spending and benefits. Review past orders and carts to find potential needs.<br>
  [View Guide](member-data-warehouse.md)

- :lucide-shopping-cart:{ .lg }
  __03. Sales Conversion__
  Redeem assets and recommend products. Apply points or coupon discounts and generate referral links.<br>
  [View Guide](sales-conversion.md)

</div>

### Performance Tracking and Reports { #reference-storepal-report }

<div class="grid cards" markdown>

- :lucide-file-text:{ .lg }
  __View Store and Staff Sales Reports__
  Track referral sales, in-store purchase records, and individual performance.<br>
  [View Guide](view-sales-performance.md)

</div>



!!! info "Next Step"
    If this is your first time, start with [Search and Create Members](search-and-create-members.md) to learn how to bring customers into your OMO system.
