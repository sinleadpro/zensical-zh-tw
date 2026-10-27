---
title: "Search and Create Members"
description: "Store staff can use Store Assistant to look up member information, help customers register, and link them to a store referrer for referral commission tracking."
created: 2026-05-04 14:14
last_modified: 2026-07-01 12:00
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
  - 查詢會員資訊
  - 協助顧客註冊
  - 建立推薦人綁定
features:
  - 門市助理 會員查詢
  - 快速註冊
  - "Referrer Linking"
prerequisites: []
related: []
tags:
  - "Member Registration"
  - 推薦人綁定
acoiv: operation
apis: []
devices:
  - mobile
  - desktop
ui_components:
  - QRCode
  - 註冊簡訊
  - 代客建立會員
paths:
  - APP MARKET > 我的擴充服務 > 門市助理
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=41747
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/search-and-create-members/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

# Search and Create Members
Store staff can use Store Assistant to look up member information, help customers register, and link them to a store referrer for referral commission tracking.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

![](../../../assets/images/門市助理-前台-會員查詢-畫面總覽01.en.png){ .hero-page }

## Before You Start { #prerequisites-member-search }

- We recommend having LINE Certified Provider status so customers can add your LINE account as a friend and register with a single scan.
- Before you begin, make sure you have completed [installation and initial data setup]().

## How to Use { #operate-member-search }


### Search for Members and Register Quickly { #operate-member-search-query-member }

1. On the Store Assistant frontend, search for a member **by mobile number** or **by email or name**.

	![](../../../assets/images/門市助理-前台-會員查詢-查詢會員01.en.png){ .screenshot }

2. Take the action that matches the search result:

	=== "No Results for the Mobile Number"

		Sign the customer up as a member, guide them through registration, and complete the link.

	=== "No Results for the Email or Name"

		If no results are found for the email or name, enter a mobile number to sign the customer up.

		> Members can only sign up with a mobile number. Name and email are for searching only.


3. The system offers 3 flexible ways to sign customers up as brand members:

	=== "Scan a QR Code"

		Store staff can show a QR code for customers to scan to sign up and link to a store referrer.

		!!! tip "Create QR Code Stands for Your Store"
			**Store managers** can download and print [staff QR codes]() in the Store Assistant admin. Turn them into display stands for staff so customers can scan to link to a staff member for sales tracking and performance credit.

	=== "Send a Registration SMS"

		Click **Send Registration SMS** to send a registration link to the customer's phone. Ask them to open the message and tap the link to register.

		> The SMS template currently uses a fixed format.


	=== "Create a Member for the Customer"

		If the customer cannot complete sign-up on the spot, click **Create Member for Customer**. The system creates the member account immediately and opens the information page, greatly shortening the wait.

		!!! tip "Follow-Up"
			We recommend that staff click **Send Binding SMS** at the top to guide the customer to complete full registration on their phone, so sales and member benefits are tracked correctly.

	![](../../../assets/images/門市助理-前台-會員查詢-建立會員01.en.png){ .screenshot }

4. On the member information page, take the action that matches the member's status:

	=== "Member Without a Verified Mobile Number"

		If the member has only an email address, staff must first guide them to log in to the online store and verify their mobile number before linking a store referrer.


	=== "Member Without a Store Referrer"

		Click **Send Binding SMS** to guide the customer to link a store referrer.

		![](../../../assets/images/門市助理-前台-會員資訊-綁定門市推薦人01.en.png){ .screenshot }


	=== "Linked Member"

		View the member's benefits, purchase history, bonus points, and coupon.




### View Search History { #operate-member-search-query-logs }

1. Go to the **Search History** section on the right.
2. Select a **time range** to see members whose information pages were opened from searches.


![](../../../assets/images/門市助理-前台-會員查詢-查詢歷史紀錄01.en.png){ .screenshot }

