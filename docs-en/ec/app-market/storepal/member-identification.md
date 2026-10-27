---
title: "Member Identification"
description: "Use Store Assistant to identify members quickly, see their tags, and offer personalized in-store service and greetings."
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
  - 識別會員身份
  - 查看會員標籤
  - 編輯會員資料
features:
  - "Member Tags"
  - "Store Assistant"
prerequisites:
  - "註冊與綁定官網會員"
related: []
tags:
  - 門市助理
  - "Customer Recognition"
  - 會員標籤
  - Identification
acoiv: operation
apis: []
devices:
  - tablet
  - mobile
ui_components:
  - 會員資訊頁
  - 編輯圖示
  - 儲存變更
  - 會員標籤
paths:
  - 設定 > 功能設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=41786
  - https://www.cyberbiz.io/support/?p=41951
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/member-identification/"
comments: false
search:
  exclude: false
icon: lucide/user-search
hide: []
---

# Member Identification
Use Store Assistant to identify members quickly, understand their tags, and give personalized in-store service and greetings.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

!!! tip "Use Cases"
    - **Greet Customers Right Away**: When customers walk in, quickly check their VIP level and tags (such as regular customer or preferred product categories) and greet them warmly.
    - **Update Member Data on the Spot**: If you notice missing or incorrect information while talking with a customer, update it right away to keep marketing data accurate.

## How to Use { #operate-member-id }

This module is at the top of the interface. Use it to confirm member identity and sync traits collected in store.

![](../../../assets/images/門市助理-前台-會員資訊-會員基本資料01.en.png){ .screenshot }

### View and Edit Basic Information { #operate-member-id-view-edit-data }

=== "Store Assistant Frontend"

	1. On the member information page, view basic details such as name, mobile number, gender, and birthday.
	2. Click the **Edit** icon in the upper-right corner to update member data other than the mobile number.

		> Mobile numbers are verified data, so store staff cannot change them.

	3. Click **Save Changes**.

	![](../../../assets/images/門市助理-前台-會員資訊-會員基本資料01.en.png){ .screenshot }


=== "Store Assistant Admin"

	**Permission Settings**: Go to **Store Management**, select a store, click the **Roles and Permissions** tab, and set whether staff can **edit member basic information**.

	![](../../../assets/images/門市助理-後台-門市管理-角色與權限-會員基本資料01.en.png){ .screenshot }

=== "Online Store (EC) Sync"

	**Data Sync**: Data edited in the frontend is updated in **Customer Management > All Customers** in real time.

### Identify Member Tags { #operate-member-id-member }

=== "Store Assistant Frontend"

	1. The **Member Tags** selected and approved for display by headquarters appear below the member's name automatically.
	2. Store staff can use the tags to understand member traits quickly and offer matching service.

	![](../../../assets/images/門市助理-前台-會員資訊-會員標籤01.en.png){ .screenshot }


=== "Store Assistant Admin"

	**Choose What to Display**: Go to **設定 > 功能設定**, scroll down to the **Member Tags** section, and select the tags to show in the frontend (up to 10).

	![](../../../assets/images/門市助理-後台-設定-功能設定-會員標籤01.en.png){ .screenshot }

=== "Online Store (EC) Sync"

	**Tag Source**: Tags shown in the frontend come from the member tag system in the EC admin, which headquarters uses for retargeting.

	![](../../../assets/images/EC-後台-會員-所有會員-單筆綁定會員標籤01.en.png){ .screenshot }