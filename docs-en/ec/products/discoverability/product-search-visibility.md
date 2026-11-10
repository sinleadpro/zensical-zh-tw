---
title: "Set Product Search Visibility"
description: "Control whether products appear in site search and Google search results to avoid unwanted exposure."
author: Jase
reviewers: []
acoiv: configure
paths:
  - 商品 > 所有商品
  - 商品 > Excel 大量匯入商品
devices:
  - desktop
  - mobile
apis: []
type: guide
intents:
  - 控制商品搜尋可見性
  - 隱藏商品
  - 設定商品排除搜尋
  - 批次設定商品搜尋狀態
features:
  - 商品可見性狀態比較
  - 排除搜尋效果說明
  - 所有商品頁面快速切換
  - 新增/編輯商品頁面設定
  - 商品操作選單批次調整
  - Excel 批次匯入設定
  - 常見問題
tnb: trunk
plans: []
plan_options: []
prerequisites:
  - "Sign in to the CYBERBIZ EC admin"
lang: en-US
sites:
  - TW
tags:
  - "Product Visibility"
  - "Exclude from Search"
  - "Delist Products"
  - "Unpublished Products"
  - "Google Search"
  - "Site Search"
  - "Product Management"
  - "Product Settings"
difficulty: beginner
audiences:
  - merchant
  - merchant
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1527
products: [EC]
notes:
  - add guide 商品可見性
  - verify
comments: ""
search:
  exclude: false
icon: lucide/eye
modules:
  - 商品
  - 行銷活動
permalink: "https://help.cyberbiz.io/ec/products/discoverability/product-search-visibility/"
---

![Product search visibility settings](../../../assets/images/ec-product-search-toggle.zh-tw.en.png){ title="Product Search Visibility Settings" .hero-page }

## Compare Product Visibility Statuses { #specs-search-visibility }

Product search visibility has three main statuses. Choose the one that fits your needs:

| Status | Description | Storefront/Search Impact |
|------|------|----------------|
| Exclude from search | The product still exists in the system but does not appear in site search or Google search results | Can be bought through a direct link; avoids exposure |
| Delist | The product is temporarily off sale and not visible on the storefront | Does not appear on the storefront and cannot be bought through a link |
| Unpublished | The product is visible only to specific channels or groups | Not visible on the regular storefront or in search; can be accessed under specific conditions |

!!! tip "Tip"
    Use "Exclude from search" to hide products for a short time or while preparing a campaign. Use "Delist" to pause sales. Use "Unpublished" for products limited to specific groups or channels.


## Effects of Excluding Products from Search { #intro-search-visibility }

After you enable search exclusion, the product does not appear on the following result pages:
	
- Google search results
- CYBERBIZ site search
- The storefront all-products collection page `collection all`
- Category pages :lucide-triangle-alert: If the product has been added to a specific category, it still appears


## Where to Exclude Products from Search { #operate-search-visibility }

You can set product search exclusion in the following places:

### All Products Page { #operate-search-visibility-list }

On the product list page, quickly switch the search status of individual products.

1. In the CYBERBIZ admin, go to **Products > All Products**.
2. In the product list, find the **Searchable** column (if it is not shown, drag the scroll bar at the bottom).
3. Switch the **Searchable** toggle.
	- `ON`: The product can be searched (it appears in search results).
	- `OFF`: The product is excluded from search (it does not appear in search results).
4. The system saves the setting automatically.

![Product list search toggle](../../../assets/images/ec-product-list-search-index-toggle.en.png){ title="Product List Search Toggle" }

---

### Add or Edit Product Page { #operate-search-visibility-edit }

When you add or edit a product, set its default search status.

1. In the CYBERBIZ admin, go to **Products > All Products**.
2. Click **Add Product** or an existing product to open the product edit page.
3. In the basic settings section, find the **Product search** toggle.
	- `ON`: The product can be searched (it appears in search results).
	- `OFF`: The product is excluded from search (it does not appear in search results).
4. Click **Save** in the upper-right corner to finish.

![Product edit search setting](../../../assets/images/ec-add-product-product-search-index.en.png){ title="Product Edit Search Setting" }

---

### Product Actions Menu { #operate-search-visibility-menu }

Select one or more products and change their search status from the actions menu.

1. In the CYBERBIZ admin, go to **Products > All Products**.
2. Select the products whose search status you want to change.
3. Click **Actions...**.
4. Select **Enable Search** or **Disable Search** to set the products' search status.

  ![Batch exclude from search in the actions menu](../../../assets/images/ec-product-list-selector-enable-search-exclude.en.png){ title="Batch Exclude from Search in the Actions Menu" }

---

### Excel Batch Import { #operate-search-visibility-excel }

When you need to add or update many products, set the search status with the Excel template.

1. In the CYBERBIZ admin, go to **Products > Import Products from Excel**.
2. Click to download the **advanced bulk product creation template**.
3. In the **Exclude from search** column of the Excel template, set each product (`是` (yes) or `否` (no)).
4. Upload the edited Excel file and click **Confirm Upload**.
5. The system applies the settings in a batch.

  ![Exclude from search setting in Excel import](../../../assets/images/ec-import-from-excel-if-exclude-search.en.png){ title="Exclude from Search Setting in Excel Import" }
	
## FAQ { #faq-search-visibility }

??? quote "Can customers still buy a product after it is excluded from search?"
    Yes. Excluding a product from search only hides it from search results. Customers can still open the product through its **product link** and complete the purchase.

??? quote "Does search exclusion affect Google indexing?"
    Yes. Products excluded from search are not indexed by Google, so they do not appear in Google search results.
