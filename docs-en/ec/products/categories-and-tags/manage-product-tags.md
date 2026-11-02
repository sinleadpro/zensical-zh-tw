---
title: "Manage Product Tags"
description: "Create and manage custom product tags for categorizing, filtering, marketing, and controlling sync to third-party platforms."
created: 2026-03-08 10:00
last_modified: 2026-07-22 17:32
lang: en-US
permalink: "https://help.cyberbiz.io/ec/products/categories-and-tags/manage-product-tags/"
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
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: intermediate
intents:
  - 建立商品標籤
  - 新增商品標籤
  - 將商品加入標籤群組
  - 從編輯頁設定商品標籤
  - 從標籤群組移出商品
  - 刪除商品標籤
  - 排除商品上傳至第三方平台
features:
  - 商品標籤管理功能
  - 手動加入商品至標籤
  - Excel 匯入商品標籤
  - 商品編輯頁標籤設定
  - 第三方平台同步排除機制
  - 預設排除標籤 (排除product feed, 贈品)
  - 商品分類與篩選應用
  - 行銷活動應用 (促銷, 組合)
prerequisites:
related:
  - ec/integrations/google/setup-google-merchant-center/
  - ec/integrations/fb/meta-ads/sync-product-videos-meta-catalog/
  - ec/integrations/line/apply-setup-line-shopping-guide/
  - ec/integrations/setup-shop-com/
  - pos/check/print-product-labels/
  - ec/products/bulk-operations/batch-update-product-descriptions-shipping/
  - ec/products/create-and-manage/edit-product-description-settings/
tags:
  - "Product Tags"
  - "Product Management"
  - "Third-Party Platforms"
  - GMC
  - "Facebook DPA"
  - "LINE Shopping"
  - "Market America"
  - Gifts
  - "Exclude from Product Feed"
  - "Product Categories"
  - "Marketing Campaigns"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 商品標籤管理
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8576
  - https://www.cyberbiz.io/support/?p=3521
comments: false
search:
  exclude: false
icon: lucide/tags
hide:
---

![Manage product tags](../../../assets/images/ec-product-tag-management.zh-tw.en.png){  title="Manage Product Tags Page"  .hero-page }

## About Product Tags

Product tags help you manage products and marketing campaigns more effectively:

- Product categorization: Quickly tag different types of products for easier filtering and bulk management.
- Marketing campaigns: Add products to tag groups in bulk for promotions, combos, or bundle sales.
- Faster search and operations: Find products quickly by tag to speed up admin tasks and management.
- Exclude from third-party platform sync: Set specific tags to exclude products from the system's third-party platform data sync (such as GMC, Facebook DPA, LINE, and Market America).

## Steps

### Add Product Tags

1. Log in to the CYBERBIZ admin and go to **Products > Product Tag Management**.
2. Click **Add Tags** and enter the tag name in the Tag Name field (for example, Clothing). If you don't see the add button, scroll down to the bottom of the tag list.
3. Click **Save** to apply the changes.

![Add product tags](../../../assets/images/ec-add-product-tag.zh-tw.en.png){ title="Add Product Tags" }

---

### Add Products to a Tag Group

You can add products to a tag group in two ways:

=== "Add Manually"

	1. Log in to the CYBERBIZ admin and go to **Products > Product Tag Management**.
	2. In the tag list on the right, click to expand the tag group you want to edit.
	3. Use **Search** :lucide-search: or **Filter** :lucide-funnel: to find the products you want to add to the tag group.
	4. Click **Add** to finish.

	![Add products to a tag manually](../../../assets/images/ec-add-product-to-tag-collection.zh-tw.en.png){ title="Add Products to a Tag Manually" }

=== "Excel Import"

	!!! warning "Notes"
		- When you add products through Excel import, you cannot add products to a tag that doesn't exist.
		- When you use Excel import, products already in the group are skipped without a warning.

	1. Log in to the CYBERBIZ admin and go to **Products > Product Tag Management**.
	2. Click to download **商品標籤管理範本.xlsx** (the product tag management template).
	3. Edit the template columns:
		- Action: Choose whether to add or remove the product.
		- Tag name: Enter the product tag name. The tag must already exist in the admin.
		- SKU: Enter the product SKU.
		- All stores: `是` (yes; the store column can be left empty) or `否` (no; the store column is required).
	4. Click **Choose file** to upload the edited product tag Excel file.
	5. Click **Confirm Upload** to import.

	![Excel import product tags](../../../assets/images/ec-product-tag-sample.zh-tw.en.png){ title="Excel Import Product Tags" }

---

#### Set Product Tags from the Edit Page

1.  Log in to the CYBERBIZ admin and go to **Products > All Products**.
2.  Click the product you want to set up and open the **Settings** page.
3.  Set the tags for the main purchase product.

![Set product tags from the edit page](../../../assets/images/ec-product-settings-tag.zh-tw.en.png){ title="Set Product Tags from the Edit Page" }

---

### Remove Products from a Tag Group

1. Log in to the CYBERBIZ admin and go to **Products > Product Tag Management**.
2. In the tag list on the right, click to expand the tag group you want to edit, or use search and filters to find the products you want to edit.
3. In the product list, click :lucide-x: or **Remove Product** to remove products.

![Remove products from a tag group](../../../assets/images/ec-remove-product-from-tag-collection.zh-tw.en.png){ title="Remove Products from a Tag Group" }

---

### Delete Product Tags

1. Log in to the CYBERBIZ admin and go to **Products > Product Tag Management**.
2. Find the tag group you want to delete in the tag group list.
3. Click **Delete** next to the tag group.

![Delete product tags](../../../assets/images/ec-product-tag-collection-delete.zh-tw.en.png){ title="Delete Product Tags" }

!!! warning "After you delete a tag, all products bound to it are unbound automatically."

---

### Tags for Excluding Products from Third-Party Platforms

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions.md#conventions-plans) | Enterprise

Set specific tags to exclude products from the system's third-party platform data sync. After you apply an exclusion tag, the product's data is not uploaded to the following third-party platforms:

<div class="grid cards" markdown>

- :lucide-tags: [__Google Merchant Center__](../../integrations/google/setup-google-merchant-center.md){ title="Set Up Google Merchant Center and Sync CYBERBIZ Products" }  
- :simple-facebook: [__FB Dynamic Product Catalog__](../../integrations/fb/meta-ads/sync-product-videos-meta-catalog.md){ title="Sync Product Videos to the Meta Catalog" }
- :simple-line: [__LINE Shopping__](../../integrations/line/apply-setup-line-shopping-guide.md){ title="Apply for and Set Up LINE Shopping Referrals" }
- :simple-stryker: [__Market America SHOP.COM__](../../integrations/setup-shop-com.md){ title="Integrate the Market America Channel" } Supports only the `贈品` tag
</div>

1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
2. In the product list, click the **product name** of the product you want to exclude to open the product edit page.
3. Click the **Settings** tab and enter one of the following exclusion tags in the **Product Tags** field:
	 - `排除product feed` ("exclude product feed"): Applies to GMC, the Facebook Dynamic Product Catalog (DPA), and LINE Shopping.
	 - `贈品` ("gift"): Applies to all third-party platforms, including Market America.

    !!! warning "Do not add a space between `排除` and `product`."

4. Click **Save** to apply the settings.

![Tags for excluding products from third-party platforms](../../../assets/images/ec-remove-upload-to-third-party-platform-tag.zh-tw.en.png){ title="Tags for Excluding Products from Third-Party Platforms" }

## Next Steps

<div class="grid cards" markdown>

- :lucide-printer:{ .lg }  
  [__Print Product Labels__](../../../pos/check/print-product-labels.md){ title="Print Product Labels" }  
  Print product labels.  
- :lucide-file-spreadsheet:{ .lg }  
  [__Batch Edit Product Descriptions and Shipping Settings__](../bulk-operations/batch-update-product-descriptions-shipping.md){ title="Batch Edit Product Descriptions and Shipping Settings" }  
  Update the descriptions, temperature zones, and shipping methods of many products at once with Excel.
- :lucide-square-pen:{ .lg }  
  [__Edit Product Descriptions and Product Settings__](../create-and-manage/edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }  
  Set up product content, channels, and logistics attributes so products display correctly on the storefront.

</div>

## FAQ

??? quote "What happens if I set both the `排除product feed` and `贈品` tags?"
    If you set both tags, the system applies the `贈品` tag rules first, so the product is not uploaded to any supported third-party platform.
