---
title: "Exclude Products from Third-Party Platform Uploads"
description: "Set up exclusion tags so that products are not uploaded to third-party platforms."
created: 2026-06-29 16:30
last_modified: 2026-08-13 15:00
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - further reading links update
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
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
  - 排除商品上傳至第三方平台
  - 設定商品排除標籤
  - 避免商品出現在廣告動態
features:
  - 商品標籤
prerequisites: []
related:
  - ec/products/categories-and-tags/manage-product-tags/
  - ec/products/create-and-manage/edit-product-description-settings/
tags:
  - "Exclusion Tags"
  - "Product Feed"
  - GMC
  - "FB DPA"
  - "LINE Shopping"
  - "Market America"
  - "Dynamic Ads"
  - "Ad Exclusion"
acoiv: configure
apis: []
devices: []
ui_components: []
paths:
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=6626
permalink: "https://help.cyberbiz.io/ec/products/bulk-operations/exclude-products-from-third-party-platforms/"
comments: false
search:
  exclude: false
icon: lucide/package-x
hide: []
---
# Exclude Products from Third-Party Platform Uploads
Set up exclusion tags so that products are not uploaded to third-party platforms.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All Plans
{ .doc-badge }

CYBERBIZ automatically syncs product data to third-party sales and advertising platforms (such as Google Merchant Center, Facebook DPA, LINE Shopping, and Market America) to increase product exposure. If some products are not suitable for these platforms[^exclude-examples], you can exclude them with product tags, and the system will not upload their data to the specified platforms.

!!! example "Use Cases"
    - Gifts or internal test products that you do not want to show in dynamic ads.
    - Contract or licensing restrictions that prevent some products from appearing on certain platforms.
    - Keeping specific products from using up your ad budget.

## Platforms Covered by Exclusion Tags

After a product is given an exclusion tag, the system does not upload its data to the following third-party platforms:

- [x] Google Merchant Center
- [x] Facebook Dynamic Product Ads (DPA) catalog
- [x] LINE Shopping
- [x] Market America (`贈品` tag only)

## Steps
	
You can exclude a product from third-party platform uploads by adding a specific tag to it:

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. In the product list, click the **Product Name** of the product you want to exclude to open its edit page.
3. In the product tags field, enter either of the following exclusion tags:
	 - `排除product feed`: This tag applies to platforms such as Google Merchant Center, the Facebook DPA catalog, and LINE Shopping.
	 - `贈品`: This tag applies to all third-party platforms, including Market America.

	!!! warning "Notes on Entering Tags"
	    -   In the `排除product feed` tag, do not add a space between "排除" and "product".
	    -   Market America currently only supports excluding products with the `贈品` tag. The `排除product feed` tag is not supported.

4. Click **Save** to apply the settings.

![Product exclusion tag](../../../assets/images/ec-商品編輯頁-設定-商品標籤.en.png)

## FAQ

??? quote "What happens if I set both the `排除product feed` and `贈品` tags?"
    If you set both tags, the system applies the `贈品` tag rule first, so the product is not uploaded to any supported third-party platform.

??? quote "After I exclude a product, can customers still find and buy it in my CYBERBIZ store?"
    Yes. This exclusion only affects whether the product is uploaded to third-party platforms. It does not affect the product's visibility or purchase options in your CYBERBIZ store. Customers can still find and buy the product through store search or a direct link.

[^exclude-examples]: For example, gifts, internal test products, or products that must not be shown publicly due to contract restrictions.

## Next Steps

<div class="grid cards" markdown>

- :lucide-tag:{ .lg }  
  [__Manage Product Tags__](../categories-and-tags/manage-product-tags.md)  
  Learn how to add, edit, and manage product tags to organize your products effectively.

- :lucide-file-edit:{ .lg }  
  [__Edit Product Descriptions and Product Settings__](../create-and-manage/edit-product-description-settings.md)  
  Set up product content, channels, and logistics attributes so products display correctly on the storefront.

</div>
