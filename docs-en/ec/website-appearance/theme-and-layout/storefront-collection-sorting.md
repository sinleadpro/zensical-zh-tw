---
title: "Set the Homepage Product Collection Order"
description: "Change the display order of product collections in the 'Product List' block on your storefront homepage."
created:
last_modified: 2026-07-01 10:35
lang: en-US
permalink: "https://help.cyberbiz.io/ec/website-appearance/theme-and-layout/storefront-collection-sorting/"
type: guide
author: Jase
reviewers: []
notes:
  - 設定首頁商品列表顯示群組數量 路徑更改確認
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 商品
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
  - 調整前台商品群組排序
  - 設定首頁商品群組顯示數量
features:
  - 商品列表群組排序
  - 首頁商品列表顯示數量
prerequisites:
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - 設定任選折扣群組
related:
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - ec/marketing/discounts/mix-and-match-discounts/
  - ec/products/references/collection-group-types/
tags:
  - "Product Collection Order"
  - "Homepage Product Collections"
  - "Collection Display Count"
  - "Navigation Bar Settings"
  - "Website Appearance"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 全站商品列表群組排序
  - 網站外觀 > 套版主題管理 > 導覽列 Navbar > 導覽列選單
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=995
  - https://www.cyberbiz.io/support/?p=2382
comments: false
search:
  exclude: false
icon: lucide/arrow-up-down
hide:
---

![Storefront product list collection sorting page](../../../assets/images/ec-website-appearance-collection-sorting-storefront.zh-tw.en.png){ title="Storefront Product List Collection Sorting Page" .hero-page }

## About Homepage Collection Sorting { #intro-collection-order }

"Storefront Product List Collection Sorting" decides which collection comes first and which comes later when customers see collections in the "Product List" section of your storefront homepage. Move featured campaigns or popular categories up front so customers see the collections you want to promote as soon as they land on the homepage.

!!! info "Tip"
    This page sorts the "order of collections," not the order of products inside a collection. To set how products are sorted within a collection, go to each collection's editing page. For the difference between the two, see [Collection Sorting vs. Product Sorting Within a Collection](#faq-collection-order-vs-product-order).

---

## Prerequisites and Limitations { #prerequisites-collection-order }

- [x] **At least one public collection**: The sorting list shows only collections set to "Public." Hidden collections do not appear here.
- [x] **Collection types**: You can sort three types of collections: "[custom collections](../../products/categories-and-tags/custom-collections.md){ title="Set Up Custom Product Category Collections" }," "[conditional product collections](../../products/categories-and-tags/smart-collections.md){ title="Set Up Conditional Product Category Collections" }," and "[pick-any discount collections](../../marketing/discounts/mix-and-match-discounts.md){ title="Pick-Any Discounts" }." For details, see the [collection types reference](../../products/references/collection-group-types.md#reference-collection-order-group-types){ title="Product Collection Types Reference" data-preview }.

---

## Steps { #operate-collection-order }

1. **Open the sorting page:** In the admin, go to "Website Appearance" > "Storefront Product List Collection Sorting."
2. **Check the collection list:** The page lists all collections that are currently "Public." Each collection has a type label on the right (custom collection, conditional product collection, or pick-any discount collection) so you can tell them apart.
3. **Drag to reorder:** Hold the drag icon on the left of a collection and drag it up or down to where you want it. The higher a collection is, the earlier it shows on the storefront.
4. **Automatic save:** When you release the mouse, the system records the new order automatically. You do not need to click a save button.
5. **Check the storefront:** Go to the "Product List" section on your storefront homepage and confirm that the collections appear in the same order as in the admin.

!!! tip "Tip"
    To remove a collection from the list (so it does not show on the storefront), you do not need to do anything here. Just [set its status to "Hidden" on the collection's editing page](../../products/categories-and-tags/custom-collections.md#operate-custom-collections-publish){ title="Set Up Custom Product Category Collections" }. Once hidden, it disappears from this sorting list automatically.

---

## How It Appears on the Storefront { #specs-collection-order-display }

The "Product List" on your storefront homepage shows product collections in the order set on the collection list page.

![Collection order on the storefront](../../../assets/images/ec-collection-sorting-storefront-zh-tw.en.png){ title="Collection Order on the Storefront" }

---

## Set How Many Collections the List Shows { #operate-collection-order-count }

You can set the maximum number of product collections shown in the homepage "Product List."

1. Sign in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Navigation Bar (Navbar) > Navigation Bar Menu**.
2. Adjust the **Number of Collections** field.
    
    - **Example**: If you set the number of collections to `4`, then even if `8` collections are currently public, the homepage shows only the first `4` collections.

 ![Navigation bar menu: number of collections (legacy)](../../../assets/images/EC-網站外觀-網站設定-導覽列選單-群組數量-舊版.en.png){ title="Navigation Bar Menu: Number of Collections (Legacy)" }

## Important Rules and Limitations { #specs-collection-order }

- The sort order applies to the "Product List" section on your storefront homepage and affects the order in which customers browse collections.
- Only "Public" collections are included in the sorting list. Hidden collections are not listed and do not appear on the storefront.
- This page adjusts only the order "between collections." To sort the "products inside" a collection, go to each collection's editing page.

---

## Next Steps { #next-steps-collection-order }

<div class="grid cards" markdown>

- :lucide-layout-grid:{ .lg }  
  __Manage Product Collections__  
  Add, edit, or hide [custom collections](../../products/categories-and-tags/custom-collections.md){ title="Set Up Custom Product Category Collections" }, [conditional product collections](../../products/categories-and-tags/smart-collections.md){ title="Set Up Conditional Product Category Collections" }, and [pick-any discount collections](../../marketing/discounts/mix-and-match-discounts.md){ title="Pick-Any Discounts" }.

- :lucide-arrow-down-up:{ .lg }  
  [__Sort Products Within a Collection__](../../products/categories-and-tags/custom-collections.md#operate-custom-collections-reorder-products-manual){ title="Set Up Custom Product Category Collections" }  
  Change the display order of products in a single collection (manual sorting, by price, by best sellers, and more).

</div>

---

## FAQ { #faq-collection-order }

??? quote "Why are some collections missing from the sorting list?"
    [](){ #faq-collection-order-missing-group }
    The sorting list shows only collections set to "Public." If a collection is missing, it is usually because it is currently "Hidden."

    Go to that collection's editing page and change its status to "Public." It then appears in the sorting list.

??? quote "How is this sorting different from sorting products within a collection?"
    [](){ #faq-collection-order-vs-product-order }
    They sort different things:

    - **Storefront Product List Collection Sorting** (this page): Sorts the order "between collections."
    - **Product sorting within a collection**: Sorts the display order of "each product inside a single collection." Set it on each collection's editing page.

??? quote "Do I need to click Save after dragging?"
    [](){ #faq-collection-order-auto-save }
    No. When you drag a collection and release the mouse, the system records the new order automatically. If the storefront does not update right away, refresh the storefront page and check again.

??? quote "Where does the sort order apply?"
    [](){ #faq-collection-order-where-applied }
    It applies to the "Product List" section on your storefront homepage. When customers browse that section, collections appear from top to bottom in the order you set here.


