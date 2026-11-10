---
title: "Copy Products to POS Stores"
description: "Learn how to batch copy storefront products to POS stores, either through the batch operation flow or by assigning stores directly when you add a product."
created: 2026-06-28 00:00
last_modified: 2026-07-08 12:43
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 商品
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 批次複製商品至 POS 門市
  - 建立新商品時直接指定 POS 門市
features:
  - 批次複製商品至 POS 商店
  - 新增商品時指定門市
prerequisites:
  - "POS (in-store sales) is enabled"
  - 'The account has the "Can copy products to POS shops" permission'
  - "Product variants have SKUs set"
related:
  - pos/inventory/
  - ec/products/create-and-manage/create-update-products/
  - pos/get-started/bulk-update-product-skus/
tags:
  - POS
  - "Store Products"
  - "Batch Copy"
  - "Product Management"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 商品列表 > 批量操作
paths:
  - 商品 > 所有商品
  - 商品 > 新增商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=11985
permalink: "https://help.cyberbiz.io/ec/products/bulk-operations/copy-products-to-pos-stores/"
comments: false
search:
  exclude: false
icon: lucide/copy
hide: []
---

![Copy products to POS stores](../../../assets/images/pos-copy-products-hero.en.png){ title="Copy Products to POS Stores" .hero-page }

## About Copying Products to POS Stores { #intro-copy-to-pos }

"Copy products to POS stores" lets you copy existing products in bulk to one or more POS stores at once, so your stores quickly get the same product data. Typical cases include products already published on your storefront, setting up the same items in a newly opened physical store, or syncing best-selling products to several stores.

!!! info "Tip"
    Copying "creates a new set of product data" in the target store that is independent of the original product. After copying, the store's price, inventory, and publishing status can be adjusted separately without affecting each other.

## Prerequisites and Limits { #prerequisites-copy-to-pos }

The requirements depend on the method you use. Check the following first:

- [x] **POS (in-store sales) enabled**: Your store must have POS enabled for this option to appear in the bulk actions menu.
- [x] **Account permission**: The account must have the "Can copy products to POS shops" permission. If the option isn't in the menu, ask your store admin to turn it on in permission settings.
- [x] **SKUs set for product variants**: The SKU is the unique identifier for each product variant. Make sure every product you want to copy has a SKU.

!!! plan "Two Methods and Applicable Plans"
    * **Bulk copy existing products**: Available to all stores with POS enabled. Select products in the product list and copy them in batches. Details in [Batch Copy Existing Products to POS Stores](#operate-copy-to-pos-bulk).
    * **Specify stores when creating a product**: Available only on the **POS Only** plan. Choose the stores to sell in directly on the Add Product page. Details in [Specify POS Stores When Creating a Product](#operate-copy-to-pos-on-create).

## Steps { #operate-copy-to-pos }

### Batch Copy Existing Products to POS Stores { #operate-copy-to-pos-bulk }

!!! path "Admin Path: Products > All Products"

1. **Select products:** In the product list, select the products to copy. You can select single products, a whole page, or all products that match the current search.
2. **Open the copy menu:** Click the bulk actions menu above the list and select **Copy products to POS stores**.

    ![Open the copy menu](../../../assets/images/ec-products-copy-to-pos-open-menu.en.png)

3. **Select target stores:** In the **POS Shops** field of the dialog, select the stores to copy to. You can select several. To select all at once, select **"All POS shops"**.

    ![Select target stores](../../../assets/images/ec-products-copy-to-pos-select-stores.en.png)

4. **Decide whether to copy images:** Select **with product images** as needed[^media]. If unchecked, the products in the store will have no images. We recommend turning it on so store staff can identify products.

    ![Decide whether to copy images](../../../assets/images/ec-products-copy-to-pos-include-images.en.png)

5. **Submit:** Click **Confirm**. The system queues the job[^queued] and emails your account when it finishes.
6. **Check the results:** After you receive the email, refresh the product list to see the new products that belong to the store. If any products fail to copy, the email includes a **"Failed product copy list"** file that lists the reason for each failure[^failreason].

[^media]: If your store also has Product Videos enabled, this option appears as "with product images / videos" and copies product videos too.
[^queued]: After you submit, the system shows "Product copy has been queued. Do not repeat the operation." Don't click again, or duplicates may be created.
[^failreason]: The most common reason for failure is that the target store already has a product with the same SKU. Details in [Important Rules and Limits](#specs-copy-to-pos).

---

### Specify POS Stores When Creating a Product { #operate-copy-to-pos-on-create }

!!! plan "Plan Limits"
    This method is available only on the **POS Only** plan. On other plans, use the [batch copy](#operate-copy-to-pos-bulk) method above.

!!! path "Admin Path: Products > Add Product"

1. **Add a product:** Open the Add Product page and fill in basic details such as the product name, variants, and SKU.
2. **Specify stores:** In the **POS shops to copy to** section, select **Specified POS shops** and choose stores, or select **All POS shops** to sync to all stores.
3. **Save the product:** After you save, the system creates the product in the selected stores. This takes some time, and the system automatically sends an email when it finishes.

---

## Important Rules and Limits { #specs-copy-to-pos }

- **SKUs must be unique:** A POS store can't have products with the same SKU. If the target store already has the same SKU, that product isn't copied and is added to the failure list with the reason "The specified shop already has a product with the same SKU". Other products without conflicts are still copied normally.
- **Inventory starts at zero:** Products copied to a POS store always start with an inventory of 0. You need to build actual store inventory through the inventory process (such as creating a stock receipt) before the products can be sold in the store.
- **Unpublished by default:** Copied products are "Unpublished" in the store by default. Publish them yourself after checking the data and inventory.
- **Images must be selected:** Images aren't copied automatically. They're included only if you select "with product images" when copying.
- **Copies are independent:** Copied products are independent of the original products, so later changes to one don't affect the other.

---

## Next Steps { #next-steps-copy-to-pos }

After copying, we recommend completing the following settings so the products can be sold in the store:

<div class="grid cards" markdown>

- :lucide-package-plus:{ .lg }  
  [__Build Store Inventory__](../../../pos/inventory/index.md){ title="Omnichannel Inventory Management Guide" data-preview }  
  Inventory is 0 after copying. Add the store's actual inventory through inventory processes such as stock receipts.

- :lucide-eye:{ .lg }  
  [__Publish Products__](../../products/create-and-manage/create-update-products.md){ title="Add and Update Products" }  
  Copied products are unpublished by default. Publish them after checking the data.

- :lucide-tag:{ .lg }  
  [__Bulk Fill Product SKUs__](../../../pos/get-started/bulk-update-product-skus.md){ title="Bulk Fill Product SKUs" }  
  If products fail to copy because of missing or duplicate SKUs, clean up the SKUs in batches and copy them again.

</div>

---

## FAQ { #faq-copy-to-pos }

??? quote "I can't find the 'Copy products to POS stores' option"
    [](){ #faq-copy-to-pos-no-option }
    Check the following in order:

    - Whether your store has POS (in-store sales) enabled.
    - Whether the account has the "Can copy products to POS shops" permission. Ask an admin to turn it on in permission settings.
    - Whether you have selected products in the list first, using "whole page" or "all" selection.

??? quote "What if some products weren't copied?"
    [](){ #faq-copy-to-pos-partial-fail }
    The email sent when the job finishes includes a **"Failed product copy list"** file. The most common reason is that the target store already has a product with the same SKU. Adjust the SKU, then copy the failed products again.

??? quote "Products don't appear in the store or can't be sold after copying"
    [](){ #faq-copy-to-pos-not-visible }
    This is the normal default behavior. Copied products are by default:

    - **Unpublished**: Publish the products yourself in the product list.
    - **Inventory of 0**: Add inventory through processes such as stock receipts before they can be sold.

??? quote "Product images weren't copied"
    [](){ #faq-copy-to-pos-no-image }
    Images are included only if you select **with product images** when copying. If you didn't, copy again or add images to the products in the store yourself.

??? quote "Can I click copy more than once?"
    [](){ #faq-copy-to-pos-duplicate-submit }
    Not recommended. After you submit, the job is queued and the screen shows "Product copy has been queued. Do not repeat the operation." Clicking again may create duplicates, so wait for the email.

