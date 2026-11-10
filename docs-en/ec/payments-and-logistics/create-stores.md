---
title: "Create Stores"
description: "Before you offer in-store services, create store information in the admin panel, choosing a General Store or a POS Store based on your business needs and whether you use a POS system."
created: 2026-04-17 12:15
last_modified: 2026-05-28 14:48
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 批次匯入有支援只建立門市？建立空門市後設定快速到貨
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 金物流
  - 管理中心
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
plan_options: []
cyb_extensions: []
intents:
  - 建立官網門市
  - 管理門市資訊
  - 區分一般門市與POS門市
features:
  - 門市管理
  - POS 整合
  - 批量建立門市
prerequisites: []
related:
  - ec/payments-and-logistics/store-pickup/
  - ec/payments-and-logistics/cyberbiz-now/
  - ec/e-ticket/setup-e-ticket-store-permissions/
tags:
  - "Create Stores"
  - "General Store"
  - "POS Store"
  - "Store List"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 新增門市
  - 下載 Excel 範例
  - 門市取貨店家
  - POS 商店
paths:
  - 金物流 > 所有門市
  - 管理中心 > 網站權限
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=15619
  - https://www.cyberbiz.io/support/?p=10454
  - https://www.cyberbiz.io/support/?p=12804
permalink: "https://help.cyberbiz.io/ec/payments-and-logistics/create-stores/"
comments: false
search:
  exclude: false
icon: lucide/store
hide: []
---

# Create Stores
Before you offer in-store services, you need to create store information in the admin panel. Based on your business needs and whether you use a POS system, you can create a "General Store" or a "POS Store".
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Brand Website / Smart POS
[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Advanced PLUS / Expert PLUS / Enterprise
{ .doc-badge }

!!! tip "Use Cases"
    - **Offer in-store pickup on the storefront**: Create a store list so customers can choose a nearby store to pick up products at checkout.
    - **Integrate offline physical stores**: Sync your physical store information to the storefront and use those stores as redemption points for **Store Pickup** and **e-vouchers**.


## Store Type Comparison { #specs-create-stores }

Before you create a store, choose the correct store type using the table below:

| Store Type | Applicable To | Store Pickup | CYBERBIZ NOW Quick Delivery | E-Voucher Redemption |
| :--- | :--- | :--- | :--- | :--- |
| **General Store** | Online-only merchants<br>**Merchants using Quick Delivery with a POS system** | ✓ | ✓ | ✓ |
| **POS Store** | Merchants using the storefront with a POS system | ✓ | ✕ | ✓ |


## Setup Steps { #operate-create-stores }

### Create a Single Store { #operate-create-stores-single }

1. Log in to the CYBERBIZ admin panel and go to **Payment and Logistics > Store Pickup Settings**.
2. Click **Add Store** in the top-right corner.
3. Choose the **Store Type** based on your needs:
    - If you run an online-only store or need Quick Delivery, select **General Store**.
    - If you need to integrate a POS system for store pickup and redemption, select **POS Store**, then select the matching POS store name from the dropdown menu.
4. Enter the **Basic Store Information** (name, phone number, address, business hours, and so on).
5. Click **Save** to finish creating the store.

!!! tip "Set a Default Store"
    If you have multiple stores with the same shipping and payment rules, set one of them as the **Default Store**. When you create a new store later, click **Use default store data** to apply its settings quickly.

### Create Stores in Batch { #operate-create-stores-batch }

If you need to create multiple stores at once and turn on the **Store Pickup** feature, use **Bulk Import** to create them together.

1. Go to **Payment and Logistics > Store Pickup Settings** and click **Download Excel Example**.
2. Open the file and fill in the tab that matches your store type:
    - **General Store**: Fill in the **Store Pickup Stores** tab.
    - **POS Store**: Fill in the **POS Stores** tab, and make sure the store name matches the POS store name.
3. Fill in the basic store information.
4. Enter the payment methods.

    - **Supported options**: Store pickup orders support only **non-COD** options, and **cash on delivery (COD) is not supported**. If you select COD, the in-store barcode slip for POS stores cannot be printed.
    - **Format**: Separate values with a half-width comma `,`.

5. Complete the shipping fee settings.

    - **Input range**: Fill in the corresponding information in the **[4] Logistics Name**, **[5] Spending Amount**, and **[6] Shipping Fee** columns.
    - **Input format**: Use only Chinese characters, half-width numerals, and the tilde `~`.
    - **Tier setup**: If a single store needs multiple shipping fee tiers, add **blank rows** below that store's row and fill them in.

      > When you add tiers, the **[4] Logistics Name** field must stay the same.


6. Return to the admin panel, click **Import Store from Excel**, and select the file.
7. After a successful import, stores are turned off by default. Open each store's edit page one by one, confirm the information, and turn it on.

!!! warning "Notes"
    - When you run a batch import and need to add only one store type, clear the content of the other tab to avoid duplicate creation or import errors.


### Create a Default Store { #operate-create-stores-default }

If you have multiple stores that need the same shipping fees and payment methods, set one store up first as the **Default Store**. Each time you add a store, you can apply that store's settings with one click, so you don't need to re-enter the same values for every store.

!!! tip "Clarifying Concepts"
    This lets you quickly copy settings to other branches in the admin panel. It does not pre-select a pickup store for customers on the storefront checkout page.

1. Go to **Payment and Logistics > Store Pickup Settings** and select a store with configured rules to open its edit page.
2. In the **Basic Settings** section, select **Set as Default Store** and click **Save**.
3. When you create other stores later, select **Use default store data** on the edit page.
4. The system automatically fills in the **Payment Setting** and **Shipping Fee Setting** information from the default store.

## Add a Store Administrator { #operate-create-stores-admin }

1. Go to **Website Management > User Account Settings** and click **Add Store Administrator**.
2. Fill in the store administrator account information.
3. After the administrator is added, it appears in the administrator list.

## More Actions { #next-steps-create-stores }

After you create a store, click the links below to configure the services you want to offer:

<div class="grid cards" markdown>

- :lucide-package-check:{ .lg }
  [__Set Up Store Pickup Service__](store-pickup/index.md)
  Set shipping fee tiers, payment methods, and pickup dates.

- :lucide-truck:{ .lg }
  [__Enable Quick Delivery Service__](cyberbiz-now/index.md)
  Set delivery areas, shipping fees, and product inventory allocation.

- :lucide-ticket:{ .lg }
  [__Set Up E-Voucher Redemption__](../e-ticket/setup-e-ticket-store-permissions.md)
  Enable voucher scan redemption for store locations.

</div>

## FAQ { #faq-create-stores }


??? quote "After you enable the POS system, can you create **General Store** orders to process them?"
    Yes, but note that **General Store** orders do not have POS front-end operation permissions. These orders do not appear in the POS front-end interface, so administrators must log in to the admin panel to change their status (for example, to Arrived at Store or Received).
