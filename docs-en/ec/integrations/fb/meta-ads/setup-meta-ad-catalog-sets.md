---
title: "Set up Catalog Product Sets for Meta Ads"
description: "Create catalog product sets with the CYBERBIZ Meta Ads App, filter specific products, and run them in Meta catalog or image ads."
created: 2026-04-20 21:10
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
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 建立目錄商品組合
  - 投放 Meta 廣告
  - 管理商品同步
features:
  - 目錄商品組合
  - 手動更新目錄
  - 商品排除機制
prerequisites:
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
related:
  - ec/integrations/fb/meta-ads/setup-meta-ad-campaign/
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
  - ec/app-market/install-meta-ads-app/
  - ec/products/categories-and-tags/manage-product-tags/
  - ec/products/create-and-manage/product-management-interface/
tags:
  - "Meta Ads"
  - "Facebook Integration"
  - "Catalog Ads"
  - "Product Sync"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 目錄商品組合
  - 創建目錄商品組合
  - 選取限制
paths:
  - 第三方整合 > 臉書 Facebook 設定（廣告/註冊登入） > 目錄商品組合
  - 第三方整合 > 臉書 Facebook 設定（廣告/註冊登入） > 基本設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=10789
  - https://www.cyberbiz.io/support/?p=46480
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/setup-meta-ad-catalog-sets/"
comments: false
search:
  exclude: false
icon: lucide/shopping-basket
hide: []
---

![MAA-Catalog Product Set](../../../../assets/images/ec-第三方整合-fb-maa-目錄商品組合.en.png){ .hero-page }

## Meta Ad Catalog Set Overview

The **Meta Ad Catalog Set** feature lets merchants filter specific product sets directly from the CYBERBIZ back office for special promotions or specific sales needs, and precisely run them in Meta's [catalog ads or image ads](setup-meta-ad-campaign.md#廣告呈現效果){ title="Set Up a Meta Ad Campaign" }.

## Prerequisites and Restrictions

Before you add a product set, make sure you complete the following:

- [x] **[Reconnect FBE](../mbe/setup-fbe-authorization.md){ title="Set Up FBE Account Authorization and Asset Linking" }**: Due to Meta feature updates, merchants must reconnect the "New Facebook Business Extension" at least once.
- [x] **[Create and Top Up an Ad Account](create-meta-ad-account-top-up.md){ title="Create a Meta ad account and add ad funds" }**: Create an ad account and add ad funds before you set up delivery.

## Steps to Add a Catalog Product Set

1.  **Access Meta Ads App**: Log in to the CYBERBIZ admin, then go to **Third-Party Integration > Facebook > Product Set**.

    - If not yet connected: Click "Connect Now" to initialize (see [Install Meta Ads App](../../../app-market/install-meta-ads-app.md){ title="Install Meta Ads App" }).
    - If already connected: Click "**Go Now**."

2.  **Start Creating**: Click Catalog Product Sets > Create Catalog Product Set in the left navigation menu.

    ![MAA](../../../../assets/images/ec-maa-創建目錄商品組合.en.png)

3.  **Name and Add**: Enter "Catalog Product Set Name," click "Add Products," and select how to add products:

    - **Quick Add**: Directly select the system-calculated TOP 10 / 20 / 50 popular products.
    - **Custom Product Selection**: Click it to open the advanced filter interface.


    ![MMA-Catalog Product Set-Add Products](../../../../assets/images/ec-maa-創建目錄商品組合-新增商品.en.png)

4.  **Filters and Limits**: If you select "Custom Product Selection," filter products precisely with the following logic:

    - **Flexible Filtering**: First, switch the scope to All Products or Popular Products, then search by type, tag, vendor, or keyword.
    - **Selection Limits**: You can only select products whose status is "Public" and "Listed."
    - **Automatic Exclusion**: Products tagged "Gift" or "Exclude product feed" can't be selected. Learn how to set up exclusion tags in [How to Set Up Product Exclusion Tags](../../../products/categories-and-tags/manage-product-tags.md#排除上傳至第三方平台標籤){ title="Manage Product Tags" }

    ![MMA-Catalog Product Set-Add Products-Filter Products](../../../../assets/images/ec-maa-創建目錄商品組合-新增商品-篩選商品.en.png)

    !!! info "For filter logic, see [Product Filter Settings in the Back Office](../../../products/create-and-manage/product-management-interface.md#篩選器使用邏輯){ title="Manage Products" }."

5.  **Confirm and Save**: Check that the product list is correct, click "Confirm Add" in the bottom-right corner, then click "Save" to finish creating the set.
6. **Manage and View**: After you save, view, edit, or delete the sets you created in the list on the Catalog Product Sets home page.

    ![MAA-Catalog Product Set-Product List](../../../../assets/images/ec-maa-目錄商品組合-商品列表.en.png)

## Product Sync and Troubleshooting

### Manually Update the Catalog

If you just updated product data in the back office, the change may not appear in Meta right away. If selecting products causes an update to fail, follow these steps to manually update the catalog:

1.  **Access the Operation Page**: Log in to the CYBERBIZ admin, then go to **Third-Party Integration > Facebook > Basic Setting**.
2.  **Run a Manual Update**: In the "Product Catalog" section, click "Manual Update." The system immediately pushes the latest product data to Meta.

![MBE-Manually Update Catalog](../../../../assets/images/ec-第三方整合-fb-基本設定-手動更新目錄.en.png)

---

### Update on the Meta Side

If the sync still fails after you update on the CYBERBIZ side, you can also go to Meta Business Manager to force a data source update:

1.  **Access Meta Business Manager**: Log in to [Meta Business Manager](https://business.facebook.com/commerce_manager), then click the target catalog.
2.  **Select the Data Source**: After you open the target catalog, click **Catalog > Data Source**.
3.  **Request an Update**: Click "**Update**" to force a sync of product data.

![MBM-Catalog Update](../../../../assets/images/ec-第三方整合-mbm-目錄-更新.en.png)

## Use in Ad Campaigns

After you create a catalog product set, you can create ads based on it:

1.  In the **Campaign** tab in Meta Ads App, click "**Create Campaign**."
2.  In **Ad Creative Settings**, select the product set you just created in the "**Catalog Product Set**" field.
3.  You can also pair this with Meta's Advantage+ Shopping Campaign (ASC) to let AI automatically optimize audiences and placements.

![MAA-Create Ad Campaign-Catalog Product Set](../../../../assets/images/ec-maa-創建廣告活動-目錄商品組合.en.png)

## Next Steps

<div class="grid cards" markdown>

- :lucide-package-x:{ .lg }   
  [__Exclude Product Sync__](../../../products/categories-and-tags/manage-product-tags.md#排除上傳至第三方平台標籤){ title="Manage Product Tags" }       
  If you don't want a specific product to sync to Meta, add "Gift" or "Exclude product feed" to its tags. The system excludes it automatically.

- :lucide-rocket:{ .lg }   
  [__Create Ad Campaign__](./setup-meta-ad-campaign.md){ title="Set Up Meta Ad Campaign" }       
  After you finish setting up the catalog product set, create a Meta ad campaign. Choose "Catalog" or "Image" as the creative source to run ads.

</div>

## Frequently Asked Questions

??? quote "Which products can't be added to a catalog product set?"

    - Products whose status is not "Public" or "Listed"
    - Products tagged "Gift" or "Exclude product feed"

??? quote "How long after a catalog product set is created does it sync to Meta?"

    The system syncs automatically. If the change doesn't appear right away, go to "[Manually Update the Catalog](#手動更新目錄)" to force an update.

??? quote "How do I confirm that products have synced to the Meta catalog?"

    When you create an ad campaign, if you can select the products in "Catalog Product Set," they have synced successfully. You can also check the catalog data in [Meta Business Manager](https://business.facebook.com/commerce_manager).

