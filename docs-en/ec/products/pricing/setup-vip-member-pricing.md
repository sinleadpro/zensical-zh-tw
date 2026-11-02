---
title: "Set up VIP Member Pricing"
description: "Set different product prices for each VIP member tier, and use storefront labels to prompt visitors to log in and boost conversions."
created: 2026-03-08 17:45
last_modified: 2026-09-18 14:10
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - doc-previous 設定 VIP 會員群組 link
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
  - 會員
sites:
  - TW
tnb: branch
plans:
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options:
  - standard
  - optional
cyb_extensions: []
audiences:
  - merchant
difficulty: intermediate
intents:
  - 設定會員等級價
  - 批次修改 VIP 價格
  - 顯示登入看 VIP 價標籤
features:
  - 會員專屬價格
  - 批次操作
  - Excel 匯入
  - Excel 匯出
  - 商品 VIP 標籤連結
prerequisites:
  - ec/members/vip/create-exclusive-vip-groups/
related:
  - ec/members/vip/create-exclusive-vip-groups/
tags:
  - VIP
  - "Member Marketing"
  - "Exclusive Offers"
  - "Conversion Optimization"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 款式管理
  - 操作選單
  - 網站設定
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5794
  - https://www.cyberbiz.io/support/?p=10289
permalink: "https://help.cyberbiz.io/ec/products/pricing/setup-vip-member-pricing/"
comments: false
search:
  exclude: false
icon: lucide/gem
hide: []
---

![VIP member exclusive prices](../../../assets/images/ec-product-edit-vip-exclusive-price-hero.zh-tw.en.png){ title="VIP Member Exclusive Prices" .hero-page }

## About VIP Member Exclusive Prices

**Member Exclusive Price** lets you set different prices for VIP members of different levels, making high-value members feel valued and encouraging purchases.

## Prerequisites and Limits

- [x] You have set up VIP groups. For details, see [Create Exclusive VIP Groups](../../members/vip/create-exclusive-vip-groups.md).
- [x] If you add VIP rules, set member exclusive prices again to make sure prices are applied correctly.

!!! plan "Plan Limits"
    **Member Exclusive Price** is built into the **Enterprise, Expert, and Expert PLUS** plans. Professional PLUS and Advanced PLUS require it as an add-on.

## Steps

### Set Member Exclusive Prices for a Single Product

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Select a product and open the **Product Information** tab.
3. In the **Manage Variants** section, click **Edit Member Exclusive Prices**.
4. Select a VIP group from the drop-down list.
5. Click **Create a Member Exclusive Price** to add a column for the group and set the exclusive price.

![Set member exclusive prices for a single product](../../../assets/images/ec-edit-member-exclusive-price-setting.zh-tw.en.gif){ title="Set Member Exclusive Prices for a Single Product" }

#### Edit Member Prices

- Click "Edit Price" and enter the exclusive price.  
- Each variant can have a different price. If none is set, the system uses the product's selling price.

![Edit member exclusive prices](../../../assets/images/ec-edit-member-exclusive-price-variants.zh-tw.en.gif){ title="Edit Member Exclusive Prices" }

---

#### Delete Member Prices

1. Click **Remove** in the group's column.
2. Click **Delete** to confirm.

![Delete member exclusive prices](../../../assets/images/ec-remove-member-exclusive-price-variants.zh-tw.en.png){ title="Delete Member Exclusive Prices" }
	
### Set Member Exclusive Prices for Multiple Products

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Select one or more products.
3. Click the actions menu at the top and choose **Edit Member Exclusive Prices**.
4. Select a VIP group from the drop-down list.

![Set member exclusive prices for multiple products](../../../assets/images/ec-batch-edit-member-exclusive-price.zh-tw.en.gif){ title="Set Member Exclusive Prices for Multiple Products" }

---

#### Edit and Delete Member Prices

- Click **Create a Member Exclusive Price**, select a VIP group, and edit the price.
- To delete a group price, click **Remove** in its column.

!!! info "Each variant can have a different price. If none is set, the product's selling price is used."

### Import or Update in Bulk with Excel

#### Step 1: Export Member Exclusive Prices

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. Select the products you want to edit.
3. Click the actions menu at the top and choose **Export Member Exclusive Prices**.

![Export member exclusive prices](../../../assets/images/ec-export-member-exclusive-prices.zh-tw.en.gif){ title="Export Member Exclusive Prices" }

---

#### Step 2: Edit the Excel File

1. The system emails the Excel file to you. Download and open it.
2. Set the product exclusive prices in the corresponding columns and save the file.

![Edit member price columns in Excel](../../../assets/images/ec-export-member-exlucisve-prices-column.zh-tw.en.png){ title="Edit Member Price Columns in Excel" }

---

#### Step 3: Import the Excel File

1. Go to **Products > All Products**.
2. Above the product list, select **Import Member Exclusive Prices**.
3. Upload the Excel file and click **Confirm**.
4. After the import succeeds, the system emails you a notification.

![Import member exclusive prices](../../../assets/images/ec-import-member-exclusive-prices.zh-tw.en.png){ title="Import Member Exclusive Prices" }

### Member Exclusive Price Label

The **member exclusive price label** works with the **product VIP label link** to prompt visitors who aren't logged in to log in for VIP exclusive prices, increasing sign-ups and conversions.

!!! example "Use Cases"

    - **Show a prompt label**: Show prompt text on the product page (for example, "Log in to see VIP prices") to remind customers to log in for exclusive offers.
    - **Guide members to log in**: Make the label a link that takes visitors to the **sign-up or login page**.
    - **Increase conversions**: Use the psychological effect of price differences to make visitors more willing to sign up and log in.

---

#### Steps

1. Log in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Detail Settings**.  
2. Select **Product Page > Basic Settings**.
3. Set the following fields:
    
    - **Member exclusive price label**: The label text on the storefront.  
    - **Product VIP label link**: The URL of the login or sign-up page.
 

![Member exclusive price label settings](../../../assets/images/ec-member-exclusive-price-label-setting.zh-tw.en.gif){ title="Member Exclusive Price Label Settings" }

---

## Storefront Display

If a member's VIP group has exclusive prices, the storefront product page shows the member exclusive price and the VIP group name.

=== "Feature Turned Off"

	No label is shown to customers who aren't logged in.
	
	![Storefront with the feature turned off](../../../assets/images/ec-member-exclusive-price-display-off.zh-tw.en.png){ title="Storefront with the Feature Turned Off" }

=== "Feature On, Member Not Logged In"
	A login or sign-up link is shown.

	![Feature on, member not logged in](../../../assets/images/ec-vip-exclusive-price-frontend-enable-not-login.zh-tw.en.png){ title="Feature On, Member Not Logged In" }

=== "Feature On, Member Logged In"
	The member level and exclusive price are shown.

	![Feature on, member logged in](../../../assets/images/ec-vip-exclusive-price-frontend-enabled-login.zh-tw.en.png){ title="Feature On, Member Logged In" }

## FAQ

??? quote "How does the storefront display member exclusive prices after I set them?"
	After a member logs in, the storefront shows the exclusive price directly if their VIP group has one. Visitors who aren't logged in see the original price, and you can turn on the VIP label for visitors who aren't logged in to prompt them to log in.
	
	- **Logged-in members:** The system shows the exclusive price automatically.  
	- **Members not logged in:** We recommend turning on the label prompt and setting a login or sign-up link.

??? quote "If a product has exclusive prices for several VIP groups, how does the system decide?"
	The system shows the price based on the member's highest level or the internal priority settings. For details on multi-group price priority, see [Create Exclusive VIP Groups](../../members/vip/create-exclusive-vip-groups.md).
