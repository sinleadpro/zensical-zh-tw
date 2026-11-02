---
title: "Set up Back-in-Stock Notifications"
description: "Learn how to turn on back-in-stock notifications. When an out-of-stock product is restocked, the system automatically emails customers who signed up to track it, boosting repeat purchases."
created: 2026-03-05 14:20
last_modified: 2026-07-03 11:44
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
sites:
  - TW
tnb: branch
plans:
  - Advanced
  - Expert
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 設定商品貨到通知
  - 補貨自動化通知
  - 提高缺貨商品轉化率
features:
  - 商品貨到通知
  - Email 通知樣板
  - 庫存管理自動化
prerequisites:
related:
  - ec/notifications/manage-email-templates/
  - ec/products/create-and-manage/edit-product-description-settings/
  - ec/products/create-and-manage/create-update-products/
tags:
  - "Back-in-Stock Notifications"
  - "Restock Notifications"
  - "Inventory Management"
  - "Member Engagement"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 款式管理
  - Email 通知樣板
  - 套版主題管理
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5661
  - https://www.cyberbiz.io/support/?p=18529
permalink: "https://help.cyberbiz.io/ec/products/engagement/setup-back-in-stock-notifications/"
comments: false
search:
  exclude: false
icon: lucide/bell-ring
hide: []
---

![Back-in-stock notifications](../../../assets/images/ec-product-restock-notification-hero.zh-tw.en.png){ title="Back-in-Stock Notifications" .hero-page }

## About Back-in-Stock Notifications

Back-in-stock notifications show a "Sold Out, Notify Me When Available" button for out-of-stock products on the storefront, and the system records each customer who clicks it. When the product is restocked, the system automatically emails the registered members. This helps you catch sales opportunities right after restocking and improves repeat purchases and the customer experience.

!!! example "Use Cases"
    - Popular products often sell out, and you want to notify waiting customers as soon as they are restocked.
    - For limited or seasonal products, use back-in-stock notifications to build anticipation and drive conversions.
    - Reduce customers lost to stockouts and turn waiting customers into real orders.

## Requirements and Limits

The following limits apply at the system level.

- This feature supports theme version 3.47.0 and later. Check that your theme version meets this requirement.
- Each member can receive only one back-in-stock notification per product. After the notification is sent, the system automatically stops tracking the product for that member. To be notified again, the member must sign up again.

!!! info "Notification Triggers"

    Back-in-stock notifications are triggered under the following conditions:

    - [x] The product must have [inventory management](#setup-restock-inventory-stop-selling) turned on, and its inventory must be `0`  
    - [x] The out-of-stock setting must be [Stop selling](#setup-restock-inventory-stop-selling) for the storefront product page to show the **Sold Out, Notify Me When Available** button  
    - [x] The product stock status must be set to [variants are clickable when out of stock](#setup-restock-variant-clickable). Only then does the **Notify Me When Available** option appear after a customer clicks a product variant.

## Turn on Back-in-Stock Notifications

### Set up Inventory Management and Stop Selling { #setup-restock-inventory-stop-selling }
1. In the CYBERBIZ admin, go to **Products > All Products**.
2. Click the name of the product you want to set up to open the product edit page.
3. In the **Manage Variants** section, make sure **Inventory** is turned on, and set the **Insufficient Stock** option to *Stop selling* .

![Set up inventory management and stop selling](../../../assets/images/ec-inventory-stop-selling.zh-tw.en.png){ title="Set Up Inventory Management and Stop Selling" }

---

### Make Variants Clickable When Out of Stock { #setup-restock-variant-clickable }

=== "Drag-and-Drop Theme"
	1. In the CYBERBIZ admin, go to **Website Appearance > Theme Setting > Detail Settings > Product Page > Basic Settings**.
	2. Under **Variant status when out of stock**, select **Variants are clickable**.

	![Clickable out-of-stock variants setting](../../../assets/images/ec-variant-clickable-contact-merchant.zh-tw.en.gif){ title="Clickable Out-of-Stock Variants Setting" }

=== "Standard Theme"
	1. In the CYBERBIZ admin, go to **Website Appearance > Theme Setting > Detail Settings > Collection and Product Page Settings**.
	2. Under **Show out-of-stock status**, select **Variants are clickable when out of stock**.
	
	![Back-in-stock notifications 02](https://www.cyberbiz.io/support/wp-content/uploads/商品貨到通知02.png){ title="Back-in-Stock Notifications 02" .screenshot }

---

### Members Sign up for Back-in-Stock Notifications

!!! warning "Restock Notifications Are Sent Only Once"
    Each member receives only one restock notification. After it is sent, the member's restock sign-up is canceled automatically. If the product sells out again, the member must click the **Sold Out, Notify Me When Available** button again to sign up.

This section explains what customers do on the storefront and how the system responds.
	
1. After a member clicks the **Sold Out, Notify Me When Available** button on the product page, the button changes to **Notification Enabled**.
2. When the product inventory changes from `0` to `> 0` or to unlimited inventory, the system automatically emails a restock notification to the registered members.

<div class="grid cards borderless two-columns" markdown>

- ![Back-in-stock notifications 03](https://www.cyberbiz.io/support/wp-content/uploads/商品貨到通知03.png){ title="Sold Out, Notify Me When Available" }
- ![Back-in-stock notifications 04](https://www.cyberbiz.io/support/wp-content/uploads/商品貨到通知04.png){ title="Notification Enabled" }

</div>

## Back-in-Stock Notification Email Template Settings

Customize the email template for back-in-stock notifications.

1. In the CYBERBIZ admin, go to **Push Notifications > Email Notification Template > Customers Related > Product Restock Notification**.
2. Under **Email body type**, select **HTML template body** or **Plain text**.
3. Edit the email body in **Email body**.
4. Click **:material-file-search-outline: Preview** to check your changes.
5. When everything looks right, click **Save** to apply the changes.

!!! warning "Do not change the text inside `{{}}`. These are variables the system fills in automatically, and changing them may break the feature."

![Back-in-stock notification email template settings](../../../assets/images/ec-product-restock-notification-template.zh-tw.en.gif){ title="Back-in-Stock Notification Email Template Settings" }

<div class="grid cards" markdown>

- :lucide-mail:{ .lg } [__Set Up and Manage Email Notification Templates__](../../notifications/manage-email-templates.md){ title="Set Up and Manage Email Notification Templates" }

</div>

## Next Steps

<div class="grid cards" markdown>

- :lucide-file-edit:{ .lg }  
  [__Edit Product Descriptions and Product Settings__](../create-and-manage/edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }  
  Set up product content, channels, and logistics attributes so products display correctly on the storefront and support search and marketing.
- :lucide-package-plus:{ .lg }  
  [__Add and Update Products__](../create-and-manage/create-update-products.md){ title="Add and Update Products" }  
  Complete the full flow of a product, from creation, variants, pricing, and descriptions to later editing, copying, listing, and delisting.

</div>
