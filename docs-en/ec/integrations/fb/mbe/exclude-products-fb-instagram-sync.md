---
title: "Exclude Products from FB and IG Shops"
description: "Exclude specific products from syncing to Facebook and Instagram shops using product tags or Meta Business Suite."
created: 2026-04-14 11:25
last_modified: 2026-07-03 11:45
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
  - 第三方整合
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 排除_FB_商店商品
  - 排除_IG_商店商品
features:
  - 商品排除標籤
prerequisites:
  - ec/integrations/fb/mbe/setup-fb-instagram-shop/
related:
  - ec/integrations/fb/mbe/setup-fb-instagram-shop/
  - ec/products/categories-and-tags/manage-product-tags/
tags:
  - FBE
  - "FB Shop"
  - "IG Shop"
  - "Product Sync"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 臉書_Facebook_設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=28419
permalink: "https://help.cyberbiz.io/ec/integrations/fb/mbe/exclude-products-fb-instagram-sync/"
comments: false
search:
  exclude: false
icon: lucide/package-x
hide: []
---

![Exclude products from third-party uploads](../../../../assets/images/ec-商品-商品標籤-排除上傳至第三方.en.png){ .hero-page }

## FB and IG Shop Product Exclusion Guide

After you enable the Facebook (FB) and Instagram (IG) shop integration, the system continuously updates catalog information through the product feed URL. If you have products you do not want to display, follow the steps below to configure and adjust them.

!!! info "System Update Time"
    Storefront product information usually syncs to the Facebook Shop automatically at **2:00 AM or 2:30 AM daily**. Content updated that day appears only after the sync is complete.

## Prerequisites and Restrictions

- [x] Complete [Facebook and Instagram Shop Integration](setup-fb-instagram-shop.md){ title="Set Up Facebook and Instagram Shops" }.

## Steps

### Exclude via Storefront Admin Tags <small>Automated</small>

If you have specific products (such as gifts or test products) that you do not want to sync to third-party platforms, the most direct method is to filter them with tags:

<div class="grid cards" markdown>

- :lucide-package-x:{ .lg } [__Set Up Product Exclusion Tags__](../../../products/categories-and-tags/manage-product-tags.md#排除上傳至第三方平台標籤){ title="Manage Product Tags" }     

</div>

---

### Adjust in Meta Business Suite <small>Manual Adjustment</small>

If the integration is complete, you can also adjust visibility directly in the management interface of Meta Business Suite:

#### Hide the Entire Shop

1. Go to “[Meta Business Suite :lucide-external-link:](https://business.facebook.com/commerce)” and select the business account.
2. Click **Settings** > **General**, and find the related shop under **Sales Channels**.
3. In the dropdown menu, select the visibility setting.

![FB-IG shop visibility setting](../../../../assets/images/ec-第三方整合-fb-fb-ig商店-設定商店能見度.en.png)

!!! note "For more steps and details, see the Meta official documentation: [Manage Shop Visibility on Facebook and Instagram :lucide-external-link:](https://zh-tw.facebook.com/business/help/23907275388927202)."

---

#### Hide Single or Partial Products

=== "Set from the Product Catalog"

    1. Go to “[Meta Business Suite :lucide-external-link:](https://business.facebook.com/commerce)” and select the business account.
    2. Click **Catalog** > **Products**.
    3. Select the checkbox next to the products you want to hide or show (up to 100 items).
    4. Click the **Shop** dropdown menu:
        - To show products, select **Show in Shop** and confirm.
        - To hide products, select **Hide in Shop** and confirm.
    5. Select the shop where you want to hide the products and confirm.

    ![Set visibility from the product catalog](../../../../assets/images/ec-第三方整合-fb-fb-ig商店-設定商品能見度-從商品目錄.en.gif)

=== "Set from Shop Inventory"

    1. Go to “[Meta Business Suite :lucide-external-link:](https://business.facebook.com/commerce)” and select your shop.
    2. In the left menu, click “Shop,” and then click “Edit Shop” next to the sales channel you want to edit (for example, Facebook).
    3. Click **Settings** > **Inventory**.
    4. Click **View Products in Shop**:
        - To hide products, click **Hide** :lucide-eye-off:.
        - To show products, click **Display** :lucide-eye:.

    ![Set FB-IG product visibility](../../../../assets/images/ec-第三方整合-fb-fb-ig商店-設定商品能見度-從商店庫存.en.gif)

!!! note "For more steps and details, see the Meta official documentation: [Manage Shop Products :lucide-external-link:](https://zh-tw.facebook.com/business/help/836266307249612)."

## Frequently Asked Questions

??? quote "How do I exclude specific products from syncing to the shop?"

    If you do not want a gift or test product to upload to the shop, enter **“排除product feed”** or **“贈品”** in the product tags field in the storefront admin (do not add a space between 排除 and product). The system automatically filters out that product.

??? quote "When does product sync happen?"

    Storefront product information syncs to the Facebook Shop automatically at **2:00 AM or 2:30 AM every day**. Content updated that day appears only after the sync is complete.

??? quote "What is the difference between excluding with tags and hiding in Meta Business Suite?"

    Excluding with product tags is an automated setting, and products are not uploaded to the catalog. Hiding products in Meta Business Suite is a manual setting, and products are still uploaded but do not appear in the shop.

