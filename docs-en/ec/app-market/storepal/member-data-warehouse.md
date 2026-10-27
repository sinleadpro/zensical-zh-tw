---
title: "Member Data Insights"
description: "Analyze members' purchase history, VIP levels, and current assets in depth, and use data insights to support sales decisions and suggest add-on purchases."
created: 2026-05-05 11:15
last_modified: 2026-06-27 13:40
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
  - 查看會員等級
  - 分析消費數據
  - 查看購物車未結商品
  - 紀錄會員註記
features:
  - 紅利點數
  - 優惠券
  - "Store Assistant"
  - "Purchase Analysis"
prerequisites: []
related:
  - ec/marketing/bonus-and-gifts/setup-registration-gift/
  - ec/marketing/bonus-and-gifts/limited-time-first-purchase-gift/
  - ec/marketing/bonus-and-gifts/setup-birthday-gift/
  - ec/profit-sharing/referrer-profit-sharing/
  - ec/members/vip/setup-exclusive-vip-discounts/
  - ec/marketing/conditional-send/send-coupons-for-specific-products/
  - ec/marketing/other-tools/interactive-games/
  - ec/members/manage-member-profiles/
tags:
  - 門市助理
  - "Data Insights"
  - 消費分析
  - "Membership Benefits"
  - "Add-On Suggestions"
acoiv: operation
apis: []
devices:
  - tablet
  - mobile
ui_components:
  - 會員權益
  - 消費概況
  - 會員註記
  - 累積消費金額
  - 購物車未結商品
paths:
  - 設定 > 功能設定 > 前台功能設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8669
  - https://www.cyberbiz.io/support/?p=41022
  - https://www.cyberbiz.io/support/?p=41833
  - https://www.cyberbiz.io/support/?p=41853
  - https://www.cyberbiz.io/support/?p=41889
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/member-data-warehouse/"
comments: false
search:
  exclude: false
icon: lucide/users
hide: []
---

# Member Data Insights
Analyze members' purchase history, VIP levels, and current assets in depth, and use data insights to support sales decisions and suggest add-on purchases.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

!!! tip "Use Cases"
    - **Targeted Add-On Suggestions**: See how much more a customer needs to spend to reach the next VIP level, and suggest add-on items to raise the average order value.
    - **Recover Sales from Carts**: When a customer has unpurchased items in their online cart, ask whether they want to try them on or test them in store to close the sale faster.
    - **Keep Personal Service Notes**: Use member notes to record a customer's special preferences (for example, dislikes fragrance or is allergic to certain materials) for more thoughtful service.

## How to Use { #operate-member-data }

This module is in the middle of the interface and provides multi-dimensional data analysis to support sales decisions.

![](../../../assets/images/門市助理-前台-會員資訊-畫面總覽02.en.png){ .screenshot }

### Membership Benefits { #operate-member-data-member-benefits }

This tab brings together the member's online store VIP status and assets. Store staff can use this data for targeted selling or to help with redemption.

![](../../../assets/images/門市助理-前台-會員資訊-會員權益-畫面總覽01.en.png){ .screenshot }

#### View Member Levels and Benefits { #operate-member-data-view-member }


=== "Store Assistant Frontend"

	##### Metrics { #operate-member-data-section-3 }

	- **Current Level**: Shows the member's current VIP level, validity period, and bonus point multiplier.
	- **Upgrade Progress**: Shows how much more the member needs to spend to reach the next level. Use it as a talking point to encourage customers to **add items and Upgrade**.

	![](../../../assets/images/門市助理-前台-會員資訊-會員權益-VIP等級01.en.png){ .screenshot }


=== "Online Store (EC) Sync"

	##### VIP Level Sync { #operate-member-data-vip-sync }

	The levels and Upgrade conditions shown in the frontend are synced with the VIP system in **Customer Management > VIP Settings**.

	!!! warning "VIP Version Compatibility"
		Store Assistant supports only the new online store VIP system. The old VIP system is not supported.


#### In-Store Discounts and Redemption { #operate-member-data-redemption }

=== "Store Assistant Frontend"

	##### Common Actions { #operate-member-data-common-operate }

	- **Asset Details**: View the member's bonus points and exclusive coupon in real time.
	- **bonus redemption**: Click **Use Points**, enter the discount amount, and confirm. The system deducts the points immediately.
	- **coupon Redemption**: Next to the coupon, click **Apply now**, then click **Confirm** to complete the redemption (this cannot be undone).
	- **Redemption History**: Click **Usage History** to view coupon records redeemed through Store Assistant, including the name, discount, channel, and date.

	![](../../../assets/images/門市助理-前台-會員資訊-會員權益-紅利點數與優惠券01.en.png){ .screenshot }


=== "Store Assistant Admin"

	##### Display Settings { #operate-member-data-section-7 }

	Go to **設定 > 功能設定 > 前台功能設定** to choose whether to hide bonus points or coupon information in the interface.

	![](../../../assets/images/門市助理-後台-設定-功能設定-行銷活動01.en.png){ .screenshot }

	##### Coupon Redemption Permission { #operate-member-data-coupon-permissions }

	Go to **Store Management**, select a store, click the **Roles and Permissions** tab, and set whether staff can perform **coupon redemption**.

	![](../../../assets/images/門市助理-後台-門市管理-角色與權限-優惠券01.en.png){ .screenshot }

=== "Online Store (EC) Sync"

	##### **Applicable Campaigns** { #operate-member-data-section-9 }

	If your store has set up any of the following coupon types, store staff can view and use them here.

	- Task-based coupon

		- [registration gift](../../marketing/bonus-and-gifts/setup-registration-gift.md)
		- [first-purchase gift](../../marketing/bonus-and-gifts/limited-time-first-purchase-gift.md)
		- [birthday gift](../../marketing/bonus-and-gifts/setup-birthday-gift.md)
		- [Referral sign-up](../../profit-sharing/referrer-profit-sharing.md)
		- [VIP member day, VIP Upgrade gift, VIP birthday gift](../../members/vip/setup-exclusive-vip-discounts.md)

	- Purchase-earned coupon

		- [Specific-product coupon](../../marketing/conditional-send/send-coupons-for-specific-products.md)
		- [store-wide discount]() spend-threshold coupon
		- [Interactive game](../../marketing/other-tools/interactive-games.md) coupon

	##### Asset Change Records { #operate-member-data-asset-history }

	Bonus points and coupon redeemed in the frontend are updated in the [member data](../../members/manage-member-profiles.md#operate-member-profiles-assets) in the EC admin.


### Purchase Overview { #operate-member-data-consumption }

This tab analyzes the member's online store purchase history. Store staff can use it to build a member profile and recommend products accurately.

![](../../../assets/images/門市助理-前台-會員資訊-消費概覽-畫面總覽01.en.png){ .screenshot }


#### Member Purchase Analysis { #operate-member-data-member }

=== "Store Assistant Frontend"

	##### Metrics { #operate-member-data-section-13 }

	The system automatically pulls purchase data from **the past year up to the day of the search** to help store staff gauge the member's spending power and activity:

	- **Total Spending**: The member's total amount paid on the online store.
	- **Total Number of Purchases**: The member's total number of successful orders on the online store.
	- **Average Order Amount**: The average order value calculated by the system, reflecting the member's typical spend per purchase.


=== "Online Store (EC) Sync"

	##### Data Source { #operate-member-data-sync }

	The analysis data shown in the frontend is synced with **Orders > All Orders**.

	> Only **valid orders** are counted. Canceled or returned orders are not included in the totals.

#### Recently Purchased Items and Cart { #operate-member-data-recent-purchases }

=== "Store Assistant Frontend"

	##### Metrics { #operate-member-data-section-16 }

	- **Recently Purchased Online Items**: Shows the **10** most recently purchased items from the past year (duplicates are listed once), sorted from newest to oldest.
	- **Unpurchased Cart Items**: Shows the images and names of items the member has added to the online store cart but not yet checked out, in real time.

	!!! tip "Sales Tip"
		If a member has unpurchased items in their cart, store staff can ask whether they want to try them in store or buy them on the spot to close the sale faster.

=== "Online Store (EC) Sync"

	##### Data Source { #operate-member-data-section-19 }

	- **Recently Purchased Items**: Matches the member's **order history** in the EC admin.
	- **Cart Information**: Matches the **cart contents** on the EC storefront.

	!!! warning "Data Scope Limitation"
		The purchase overview uses **online EC orders only** and does not include offline POS purchases.



### Member Notes { #operate-member-data-member-notes }

Store staff can use this tab to record and view members' offline purchase traits and preferences, seamlessly integrating online and offline information.

![](../../../assets/images/門市助理-前台-會員資訊-會員註記-畫面總覽01.en.png){ .screenshot }

#### Store Tags and Text Notes { #operate-member-data-store-notes }

=== "Store Assistant Frontend"

	##### Record Types { #operate-member-data-logs-types }

	- **Store Tags**: View and update the offline **group tags** preset by headquarters.
	- **Member Notes**: View and edit **text notes** synced with EC member notes.

	##### Steps { #operate-member-data-operate-step }

	1. Click **Edit Tags** or **Edit Notes**.
	2. Select tags or enter a text description based on what you observe in store.

	    <div class="grid cards borderless two-columns" markdown>

		- ![Store Tags](../../../assets/images/門市助理-前台-會員資訊-會員註記-門市標籤01.en.png){ title="Store Tags" }
		- ![Member Notes](../../../assets/images/門市助理-前台-會員資訊-會員註記-會員註記01.en.png){ title="Member Notes" }

		</div>

	3. Click **Save Changes**. The information syncs immediately to all brand stores and the online store admin.

=== "Store Assistant Admin"

	##### Tag Settings { #operate-member-data-content-settings }

	Go to **設定 > 功能設定 > 前台功能設定**. Headquarters can define tag groups in advance (up to 5 groups, with up to 10 tags in each).

	![](../../../assets/images/門市助理-後台-設定-功能設定-門市標籤01.en.png){ .screenshot }

	##### Edit Permissions { #operate-member-data-edit-permissions }

	Go to **Store Management**, select a store, click the **Roles and Permissions** tab, and set whether staff can edit tags and notes.

	![](../../../assets/images/門市助理-後台-門市管理-角色與權限-會員備註01.en.png){ .screenshot }

=== "Online Store (EC) Sync"

	##### Two-Way Sync { #operate-member-data-bidirectional-sync }

	**Member Notes** in the frontend is fully synced with **Customer Management > All Customers > 個別會員頁 > 會員備註** in the EC admin. Changes on either side overwrite the existing content.
	![](../../../assets/images/EC-後台-會員-所有會員-顯示會員備註01.en.png){ .screenshot }

	##### Remarketing { #operate-member-data-remarketing }

	Tags added by store staff are sent back to the EC system, so headquarters can run targeted EDM or SMS remarketing.

!!! note "Before You Start"
	Store tag permissions are set to **Close** by default. To use this feature, turn it on manually in the Store Assistant admin first.
