---
title: "Sales Conversion"
description: "Use asset redemption, recommended product links, and manually recorded in-store purchases to close sales on the spot and make sure sales are attributed accurately."
created: 2026-05-05 11:15
last_modified: 2026-06-27 13:40
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：vip
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - APP MARKET
  - 訂單
  - 會員
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
  - 核銷優惠券
  - 生成推薦商品連結
  - 紀錄門市消費
  - 查看全館優惠碼
features:
  - "Recommended Products"
  - "Store Assistant"
  - "Asset Redemption"
  - "Sales Attribution"
prerequisites: []
related:
  - ec/members/vip/vip-upgrade-downgrade-renewal-rules/
tags:
  - 門市助理
  - Monetization
  - 資產核銷
  - 推薦商品
  - 業績歸因
acoiv: operation
apis: []
devices:
  - tablet
  - mobile
ui_components:
  - 全館優惠碼
  - 推薦商品
  - 新增門市消費
  - 建立購買連結
  - QR Code
paths:
  - 設定 > 功能設定 > 前台功能設定
  - 設定 > 通知設定
  - 會員中心 > 訂單查詢 > 其他通路有效訂單
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=41868
  - https://www.cyberbiz.io/support/?p=41923
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/sales-conversion/"
comments: false
search:
  exclude: false
icon: lucide/shopping-cart
hide: []
---

# Sales Conversion
Use asset redemption, recommended product links, and manually recorded in-store purchases to close sales on the spot and make sure sales are attributed accurately.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

!!! tip "Use Cases"
    - **Turn Assets into Sales on the Spot**: Encourage customers to use bonus points or a coupon that will expire soon, increasing their willingness to buy.
    - **Attribute Sales After Customers Leave**: When a customer hesitates in store, generate a personal referral link for them to consider at home. If they buy online later, the sale is still credited to you automatically.
    - **Track Performance Without POS**: At pop-up stores or sales events without a POS connection, record purchase amounts manually to keep store performance and member benefits in sync.

## How to Use { #operate-sales-conversion }

This module is on the right side of the interface and provides tools to close sales directly.

![](../../../assets/images/門市助理-前台-會員資訊-導購轉化-畫面總覽01.en.png){ .screenshot }


### Storewide Coupon Codes { #operate-sales-conversion-store-coupon }

Store staff can help members redeem their personal assets (bonus points and coupon), or share storewide coupon codes with customers for reference.

=== "Store Assistant Frontend"

	1. Click **Storewide Coupon** on the frontend home page, or in **Membership Benefits**, click **More coupon**.

		> **Usage Limitation**: Storewide coupon codes are for staff reference only. Check manually that the promotion requirements are met before use.

	2. Click **View Details** below the coupon, review the details, and click **Confirm**. When the system asks you to confirm again, click **Confirm** to complete the redemption.

	![](../../../assets/images/門市助理-前台-會員資訊-導購轉化-全館優惠券01.en.png){ .screenshot }

=== "Store Assistant Admin"

	- **Display Settings**: Go to **設定 > 功能設定 > 前台功能設定** to choose whether to hide bonus points, coupon, or storewide coupon code information in the interface.

		![](../../../assets/images/門市助理-後台-設定-功能設定-行銷活動01.en.png){ .screenshot }

	- **coupon Redemption Permission**: Go to **Store Management**, select a store, click the **Roles and Permissions** tab, and set whether staff can perform **coupon redemption**.

		![](../../../assets/images/門市助理-後台-門市管理-角色與權限-優惠券01.en.png){ .screenshot }


=== "Online Store (EC) Sync"

	- **Immediate Deduction**: After redemption in the frontend, the coupon quantity in the EC admin decreases by 1 and **cannot be restored**.
	- **Record Sync**: Redemption records are updated in the member data and order records in the EC admin.


### Recommended Products { #operate-sales-conversion-product-recommendation }

Store staff can use this feature to quickly generate personal referral links to online store products and share them with members to guide online purchases, with sales attributed automatically.

=== "Store Assistant Frontend"

	1. On the member information page, click **Recommended Products**.
	2. Search for products by **Product Name** (fuzzy search) or **SKU** (exact search).
	3. Add products: Click the products you want.
	4. Create the link: Click **Create Purchase Link**, and the system generates a personal link.
	5. Share it: Show the **QR code**, **send an SMS**, or click **Copy Link**.

	![](../../../assets/images/門市助理-前台-會員資訊-導購轉化-推薦商品01.en.png){ .screenshot }

=== "Store Assistant Admin"

	- **Recommended Products Switch**: Go to **設定 > 功能設定 > 前台功能設定** to choose whether to turn on this feature.

		![](../../../assets/images/門市助理-後台-設定-功能設定-推薦商品01.en.png){ .screenshot }

	- **SMS Settings**: Go to **設定 > 通知設定** to turn SMS sending for recommended products on or off separately.

		![](../../../assets/images/門市助理-後台-設定-通知設定-推薦商品通知01.en.png){ .screenshot }

=== "Online Store (EC) Sync"

	- **Automatic Attribution**: For online store orders placed through this link, the system attributes the sale to the staff member automatically and records it in **Orders > All Orders**.
	- **Order Source**: The order details in the admin show that the order came from a Store Assistant recommendation.

### Add Store Purchases { #operate-sales-conversion-store-purchase }

Without a POS connection, store staff can use this feature to record members' in-store purchase amounts manually, so members earn VIP level benefits and store performance is tracked.

=== "Store Assistant Frontend"

	1. Click **Add Store Purchase**.
	2. Enter the **checkout amount** for the transaction.
	3. Click **Confirm**, check that the information is correct, and click **Confirm Add**.

	![](../../../assets/images/門市助理-前台-會員資訊-導購轉化-新增門市消費01.en.png){ .screenshot }

	!!! note "Feature Limitation"
		You can only record the **total purchase amount**. Specific products or line items cannot be recorded.

=== "Store Assistant Admin"

	- **Edit Permission**: Go to **Store Management**, select a store, click the **Roles and Permissions** tab, and set whether staff can use **Add Store Purchase**.

		![](../../../assets/images/門市助理-後台-門市管理-角色與權限-新增門市消費01.en.png){ .screenshot }

	- **Sales Report**: Admins can export the all-store summary from **績效報表 > 業績報表** and view all manually entered in-store purchases on the **Store Purchase Records** tab.

		> You can also go to **Store Management**, select a store, and click **Export Report** to export a report for that store.

		![](../../../assets/images/Excel 報表-門市助理-業績報表01.en.png){ .screenshot }


=== "Online Store (EC) Sync"

	- **Order Records**: Manually entered purchases sync to **Customer Management > All Customers > 個別會員頁 > 其他通路訂單** in the EC admin.
	- **Fields**: The admin shows the creation time, amount, data source, channel name, and operator.
	- **Membership Benefits**: This amount counts toward the member's total spending and can trigger [VIP Upgrade](../../members/vip/vip-upgrade-downgrade-renewal-rules.md#specs-vip-rules-upgrade) or [Renewal](../../members/vip/vip-upgrade-downgrade-renewal-rules.md#specs-vip-rules-renewal) rules.

	!!! tip "Protecting Customer Benefits"
		Customers can log in to the online store and view their in-store purchases in **會員中心 > 訂單查詢 > 其他通路有效訂單** to make sure their benefits were added.


## FAQ { #faq-sales-conversion }

??? quote "If Store Assistant is not connected to a POS system, how do I handle checkout with coupon code discounts?"
	When you apply an online coupon code or coupon discount in Store Assistant and then need to check out in a POS system, follow these steps:

	- **Create a Matching Discount**: Create a dedicated **discount barcode** in your POS system in advance.
	- **Keep Data Consistent**: Scan the discount barcode at checkout so accounting data can be checked and reconciled later.
