---
title: "Add and Update Products"
description: "Take a product from creation, variants, and pricing to the product description, and then to later editing, copying, listing and delisting, plus multi-language and cross-border sales settings."
created: 2026-03-08 17:15
last_modified: 2026-09-29 15:30
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
  - US
  - JP
  - SG
  - MY
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 新增單一商品
  - 設定商品基本資訊
  - 上傳商品圖片與影片
  - 管理商品款式與規格
  - 設定價格與庫存管理
  - 設定預購商品
  - 設定物流材積與重量
features:
  - 商品基本設定
  - 商品圖片管理
  - 商品影片設定
  - 單一與多款式管理
  - 庫存水位通知
  - 預購商品
  - 物流材積計算
prerequisites: []
related:
  - ec/products/bulk-operations/excel-import-products/
  - ec/products/create-and-manage/edit-product-slogan-and-description/
  - ec/products/discoverability/product-search-visibility/
  - ec/products/references/product-statuses/
  - ec/products/create-and-manage/setup-product-videos/
  - ec/products/engagement/setup-back-in-stock-notifications/
  - ec/products/checkout/checkout-split-multi-cart/
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - ec/website-appearance/theme-and-layout/setup-theme-page-settings/
  - ec/products/references/product-temperature/
  - ec/website-management/setup-multi-language-and-multi-currency/
  - ec/products/pricing/setup-vip-member-pricing/
  - ec/integrations/google/setup-google-merchant-center/
  - ec/products/references/product-warehouse/
  - ec/products/create-and-manage/edit-product-description-settings/
  - ec/products/create-and-manage/create-and-setup-combo-products/
  - ec/products/bulk-operations/batch-update-product-descriptions-shipping/
tags:
  - "Product Settings"
  - "Add Product"
  - "Product Variants"
  - "Inventory Management"
  - "Pre-Order Products"
  - "Shipping Dimensions"
  - "Multi-Language Products"
acoiv: activate
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 款式管理
  - 批次操作選單
  - 媒體庫
paths:
  - 商品 > 所有商品 > 新增商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=11161
  - https://www.cyberbiz.io/helpcenter/?p=894
  - https://www.cyberbiz.io/support/?p=1958
  - https://www.cyberbiz.io/support/?p=20111
  - https://www.cyberbiz.io/support/?p=31357
  - https://www.cyberbiz.io/support/?p=7565
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/create-update-products/"
comments: false
search:
  exclude: false
icon: lucide/package-plus
hide: []
---

![Add a product](../../../assets/images/ec-create-new-product.zh-tw.en.png){ title="Add a Product: Products > All Products > Add Product" .hero-page }

## About Adding Products { #intro-product }

In the CYBERBIZ admin, every product you sell on your online storefront starts with **Add Product**. A product's settings are spread across the tabs at the top of the product edit page:

- **Product Information**: Core sales settings such as product name, images, variants, price, and inventory, which you can fill in when adding a product.
- **Product Description**: Descriptive content such as the product introduction, specifications, and delivery methods.
- **Settings**: Advanced settings (fulfillment method, temperature zone, tags, tax category, product collections) and SEO.

![Product edit page tabs](../../../assets/images/ec-商品-所有商品-編輯頁-分頁.en.png){ title="Product Edit Page Tabs" }

!!! info "Tip"
    The **Product Description** and **Settings** tabs appear only **after the product is saved**. When adding a product, fill in "Product Information" and save first. The system then switches to edit mode and shows the other tabs at the top.

??? tip "Adding or Updating Many Products?"
    To create or change many products at once, use Excel bulk import instead of editing them one by one. See [Bulk import products](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }.

---

## Prerequisites and Limits { #prerequisites-product }

Before you start, note that the following features affect which fields and options you see. Most are built in; some must be enabled or depend on the sites you operate, so not every store has all of them:
<!-- - [x] **Manage inventory (built in):** Available in variant management on all plans with no extra activation. -->
- [x] **Member-exclusive prices (VIP):** Create VIP groups first to set exclusive prices for each group in variant management.
- [x] **Product videos `PLUS/Enterprise`:** Shown correctly on the storefront only with the **drag-and-drop theme**.
- [x] **Storefront multi-language:** Once enabled, a **language switcher** appears in the upper-right corner of the product edit page so you can fill in product text for each language. See [Multi-language product content](#operate-product-edit-multilang).
- [x] **Cross-border / overseas sites:** If you operate an overseas site such as a Japan site, or have overseas warehousing enabled (such as Amazon fulfillment), additional settings such as tax category and fulfillment method appear. See [Cross-border sales settings](#operate-product-edit-crossborder).

---

## Steps { #operate-product }

The steps below cover two scenarios: **adding a product** and **editing an existing product**. When adding a product, complete "Product Information" and save it first. You can then add descriptions and settings in edit mode, and handle publishing, multi-language, and cross-border settings.

!!! tip "Tip"
    The **Save** button on the product edit page applies to all tabs. We recommend saving after you finish each tab so you don't lose content when switching tabs or languages.

### Add a Product: Basic Settings { #operate-product-create-basic }

In the admin, go to "Products" > "All Products", click **"Add Product"** in the upper-right corner to open the product edit page, and fill in the core information in the **Basic Settings** section:

1. **Enter the product name:** The name shown on the storefront. It's **required** and can't contain special characters such as `|` or line breaks.
2. **Set the product URL:** The URL path of the product page. We recommend English for better SEO and later performance analysis.
3. **Enter the product slogan and brief:** A short feature or promotional line shown near the product name, and a short description of the product ([customization guide](edit-product-slogan-and-description.md){ title="Edit the Product Brief and Product Slogan" }).
4. **Set the sell status:** Set **Publish on** and **Unpublish on**. Leaving both blank means the product launches immediately and is never taken off market[^status].
5. **Set product search:** Decide whether the product can be found by on-site search. If you set it to [excluded from search](../discoverability/product-search-visibility.md){ title="Set Product Search Visibility" }, customers can still buy it through the product link.

![Product basic settings](../../../assets/images/ec-商品-基本設定.en.png){ title="Product Basic Settings" }

[^status]: For what each sell status and publish status means, see the [product status reference](../references/product-statuses.md){ title="Product Status Reference" }.

---

### Add a Product: Product Images and Videos { #operate-product-create-media }

Upload images in the **Product Image** section:

1. **Upload images:** Click **Upload Image**, or drag files directly into the upload area.
2. **Check image specs:** The recommended size is 1000x1000px, and JPG / PNG / JPEG / GIF are accepted. We recommend keeping each image under 2 MB so the storefront loads faster.

![Set product images](../../../assets/images/ec-商品-商品圖片-上傳.en.png){ title="Set Product Images" }

??? info "Cross-Channel Advertising Reminder: Google Shopping Ads (GMC)"
    [](){ #reference-gmc-picture-specs }
    If you plan to sync products to Google for advertising, images must meet the [Google image requirements :lucide-external-link:](https://support.google.com/merchants/answer/6324350#Image_guidelines). Images that don't meet them can cause products to fail review.

    ??? example "View Google Image Restrictions and Examples"

        | Rule | Details |
        | :--- | :--- |
        | No price information | Don't show the price or discount amount in the image |
        | No promotional text | Such as "Free shipping", "On sale", or "Limited-time offer" |
        | No watermarks or logos | Product images must not be covered by brand marks |
        | Show the product clearly | Use a white or solid background, with the product taking up 85% or more of the image |

        <div class="grid" markdown>

        :lucide-check: Compliant
        ![GMC without watermark](../../../assets/images/ec-gmc-without-watermark.en.png){ title="GMC Without Watermark" .screenshot }

        :lucide-x: Non-compliant
        ![GMC with watermark](../../../assets/images/ec-gmc-with-watermark.en.png){ title="GMC With Watermark" .screenshot }

        </div>

!!! plan "Plan / Activation Requirements"
    [**Product Video**](setup-product-videos.md){ title="Set Up Product Videos" } is available only on PLUS / Enterprise plans and appears on the storefront only with the **drag-and-drop theme**.

---

### Add a Product: Variants, Prices, and Inventory { #operate-product-create-variants }

To set prices and inventory, you must first create **variants**. In the **Manage Variants** section, choose how to create them:

- **Create a single style product**: Use when the product has no other options (for example, a pen holder or storage bag).
- **Create a multiple variant product**: Use when the product has multiple options (for example, color or size).

![Choose how to create variants](../../../assets/images/ec-product-variants-choice.zh-tw.en.png){ title="Choose How to Create Variants" }

When creating a **multi-variant product**:

1. **Edit product options**: Click **Edit product options** to add options (such as "Color") and option values (such as "Red" and "Blue").
2. **Note the option limits:** A product can have up to 3 options. Each option needs at least 1 value, and values within the same option can't repeat.

![Edit product options](../../../assets/images/ec-product-variants-setup-specs.zh-tw.en.png){ title="Edit Product Options" }

Each variant has the following fields:

- **Price**: The actual selling price.
- **Compare-at price:** The suggested retail price (shown struck through).
- **Cost**: For internal analysis only; not shown on the storefront (requires activation).

    !!! info "The **Cost** field is available only on **all PLUS and Enterprise plans**."
    
- **SKU:** The product's internal item number, used to identify it at checkout and in inventory[^sku].
- **Weight (KG), Volume (CM):** At checkout, the system calculates shipping fees using the fee tiers in your logistics settings (volume is a plan-limited feature).

![Variant field settings](../../../assets/images/ec-product-variants-fields.zh-tw.en.png){ title="Variant Field Settings" }

??? tip "Tip: Apply Settings to Variants in Bulk"
    After creating a multi-variant product, you can apply the same settings to multiple variants at once. Above the variants section, choose an option such as **Edit price, Edit inventory, or Edit volume and weight**, select the variants to apply it to, enter the values, and click **Apply**. Fields left blank don't change the existing variant values.

    ![Bulk edit variants](../../../assets/images/ec-multiple-variants-product-batch-edit.zh-tw.en.png){ title="Bulk Edit Variants" }

[^sku]: Each plan has a limit on the total number of product SKUs. If you see a limit message when adding a product, your plan's product quota has been used up.

---

### Add a Product: Manage Inventory { #operate-product-create-inventory }

When you turn on **Inventory** for variants, these fields appear:

1. **Quantity**: The quantity available for sale. When inventory management is off, the quantity is treated as unlimited.
2. **Safety Stock**: The inventory alert threshold. When a variant's inventory drops to this quantity, the system sends a low-stock email so you can restock in time. Leave blank to turn off alerts.
3. **When out of stock:** Set whether customers can keep buying when inventory reaches zero.
    - **Stop selling**: Recommended for most products to avoid overselling. You must also choose this to use [**back-in-stock notifications**](../engagement/setup-back-in-stock-notifications.md){ title="Set Up Back-in-Stock Notifications" }.
    - **Continue selling**: Choose this to offer **pre-order products**.

!!! tip "Pre-Order Product Settings"
    [](){ #operate-product-preorder }
    Set "When out of stock" to **Continue selling** to let customers keep ordering a product after its inventory reaches zero, which works as pre-ordering. You don't need a separate pre-order product type; it works with your existing products. To automatically split pre-order and in-stock items at checkout, see [Set up automatic checkout splitting into multiple carts](../../products/checkout/checkout-split-multi-cart.md#operate-split-cart-preorder){ title="Check Out Pre-Order and In-Stock Items Separately" }.

![Manage inventory settings](../../../assets/images/ec-inventory-stop-selling.zh-tw.en.png){ title="Manage Inventory Settings" }

After filling in the product information, click **Save** in the lower-left corner. Once saved, the system switches to edit mode, and the **Product Description** and **Settings** tabs appear at the top so you can add more content.

---

### Edit an Existing Product: Open the Edit Page { #operate-product-edit-entry }

To change a product you've already created:

1. **Find the product:** Go to "Products" > "All Products" and find the product in the list.
2. **Open the editor:** Click the product name to open the product edit page, where you can switch between the **Product Information, Product Description, and Settings** tabs at the top.
3. **Save your changes:** After changing any tab, click **Save** in the lower-left corner to update the product.

![Product edit page overview](../../../assets/images/ec-edit-product.zh-tw.en.png){ title="Product Edit Page Overview" }

---

### Edit an Existing Product: Product Description { #operate-product-edit-description }

Switch to the **Product Description** tab and use the article editor to fill in three sections:

- **Product Description**: The main introduction of the product.
- **Specification Description**: Details such as product specifications, materials, and sizes.
- **Delivery Type**: Information about shipping and delivery.

When you're done, click **Save**.

![Edit the product description](../../../assets/images/ec-product-description.zh-tw.en.png){ title="Edit the Product Description" }

---

### Edit an Existing Product: Settings Tab { #operate-product-edit-settings }

Switch to the **Settings** tab to configure the following advanced settings:

![Product advanced settings](../../../assets/images/ec-product-settings.zh-tw.en.png){ title="Product Advanced Settings" }

=== "Product Type / Product Channel / Product Vendor"

    Used for categorizing and managing products in the admin.
    
    To remove a product type, first remove it from every product that uses it. When no products use the type, the system deletes it.

    ![Product type, channel, and vendor settings](../../../assets/images/ec-product-settings-type-channel-vendor.en.png){ title="Product Type, Channel, and Vendor Settings" }

=== "Tags"

    Add tags to products to make admin management and storefront categorization easier.

    ![Product tag settings](../../../assets/images/ec-product-settings-tags.en.png){ title="Product Tag Settings" }

=== "Delivery Temperature Zone and Logistics"

    Set room temperature, refrigerated, or frozen, and select the logistics options this product can use[^temperature].

    ![Product delivery temperature zone settings](../../../assets/images/ec-product-settings-temperature-zone.en.png){ title="Product Delivery Temperature Zone Settings" }

=== "SEO Settings"

    Fill these in based on the product's characteristics to help improve search engine rankings.

    ![Product SEO settings](../../../assets/images/ec-product-settings-seo.en.png){ title="Product SEO Settings" }

=== "Related Product Collections"

    Select an existing [**Customized Collections**](../categories-and-tags/custom-collections.md){ title="Set Up Customized Collections" } or [**Conditionalized Collections**](../categories-and-tags/smart-collections.md){ title="Set Up Conditionalized Collections" } collection. Products in that collection then appear in the [**related products section**](../../website-appearance/theme-and-layout/setup-theme-page-settings.md#operate-page-settings-related-products){ title="Set Up Related Products Display" } at the bottom of the product page.

    ![Related product collection settings](../../../assets/images/ec-product-settings-related-products.en.png){ title="Related Product Collection Settings" }

[^temperature]: For what each temperature zone means, see the [delivery temperature zone reference](../references/product-temperature.md){ title="Shipping Temperature Zone Reference" }.

---

### Edit an Existing Product: Publishing and Management Actions { #operate-product-edit-actions }

You can take the following management actions in the **upper-left corner** of the product edit page:

- **Published / Unpublished:** Switch whether the product is displayed for sale on the storefront. When set to **Unpublished**, it's hidden on the storefront and can't be bought through its link.
- **Duplicate**: Quickly create a new product using an existing product as a template. The system asks you to enter the new variants' **SKU** before duplicating[^copy-sku].
- **Go to product page**: Open the actual storefront product page to check what customers see.
- **Delete**: Remove the product from the admin. Deletion can't be undone, so proceed with care.

![Product management action shortcuts](../../../assets/images/ec-product-edit-page-shortcuts.zh-tw.en.png){ title="Product Management Action Shortcuts" }

[^copy-sku]: When you duplicate, an "Edit Product Number (SKU)" window appears. Because each variant's SKU must be unique, you need to enter new SKUs before duplication can finish.

---

### Multi-Language Product Content { #operate-product-edit-multilang }

If **[storefront multi-language](../../website-management/setup-multi-language-and-multi-currency.md)** is enabled, a **language switcher** menu appears to the right of the product edit page title so you can fill in product text separately for each language. Single-language stores can skip this section.

Before you start, understand **which fields are filled in per language and which are shared by all languages**:

- **Filled in per language (text):** Product name, product slogan, product brief, the text on the **Product Description** tab, and options.
- **Shared by all languages:** Price, variants, SKU, inventory, product images, product categories, tags, and so on. Set these once; switching languages doesn't change them.

Steps:

1. **Complete the product in your main language:** Choose a main language, enter the product name, price, variants, images, and other content as usual, and click **Save**.
2. **Switch languages:** In the language menu to the right of the title, click the language to edit. If you have unsaved changes, the system prompts you to save first[^lang-save].

    ![Language switcher menu](../../../assets/images/ec-商品-編輯商品-語言選單.en.png){ title="Language Switcher Menu" }

3. **Enter the translations:** After switching, enter the translations for that language in the text fields (content on the Product Description tab also needs to be filled in per language).

    ![Edit content in different languages](../../../assets/images/ec-商品-編輯商品-編輯不同預言內容.en.png){ title="Edit Content in Different Languages" }

4. **Save and switch to the next language:** Click **Save**, then repeat the steps above for other languages.


!!! info "Tip"
    Price, variants, inventory, and images are **shared fields**. Changes made in any language apply to all languages, so it's normal for the price to stay the same when you switch languages.

[^lang-save]: The system message reads "Save your changes before editing other languages."

---

### Cross-Border Sales Settings { #operate-product-edit-crossborder }

There's no separate "cross-border product" type. The settings needed for cross-border sales are **spread across regular fields**. If you operate overseas sites or use overseas warehousing, these settings directly affect cross-border sales:

- **Fulfillment method (Settings tab):** When shipping from overseas warehousing (such as Amazon fulfillment), choose the corresponding warehouse in **Fulfillment method**. For products shipped from that warehouse, the **SKU must exactly match the SKU in the warehouse** for orders to be sent successfully[^fba-sku].
- **Weight and volume (variants):** Overseas logistics usually charge by weight or volume, so be sure to fill in **Weight (KG)** and **Volume (CM)** for each variant.
- **Product tax category (Settings tab):** Taiwan merchants operating a **Japan site** can choose a product tax category on the Settings tab.
- **Google product category (Settings tab):** Specifies the product's category in the Google Merchant Center product feed, which helps Google Shopping ads exposure. If not set, Google assigns a category automatically.

!!! note "Customs Information Isn't Set on the Product Page"
    For cross-border shipments, the customs declaration method, duty responsibility, and similar details are filled in at the **shipping stage** based on the selected carrier, not on the product edit page.

[^fba-sku]: SKU mismatches are the most common reason cross-border warehouse orders fail to send.

---

## Important Rules and Limits { #specs-product }

- **Product name:** Required, up to 255 characters, and can't contain special characters such as `|` or line breaks.
- **Number of variant options:** A product can have up to 3 options, each with at least 1 value, and values within the same option can't repeat.
- **SKU:** Can't repeat within a store; must be reassigned when duplicating a product.
- **Multi-language fields:** Only text fields (name, slogan, brief, description) are filled in per language; price, variants, inventory, and images are shared by all languages.
- **POS store products:** Can't be set to "Published"; they're for use in stores only.
- **Product videos and variant images:** Shown on the storefront only with the drag-and-drop theme.

---

## Next Steps { #next-steps-product }

<div class="grid cards" markdown>

- :lucide-file-spreadsheet:{ .lg }  
  [__Bulk Import Products__](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }  
  Add or update many products and variants at once with Excel.

- :lucide-tags:{ .lg }  
  [__Set Member-Exclusive Prices (VIP)__](../pricing/setup-vip-member-pricing.md){ title="Set VIP Member-Exclusive Prices" }  
  Set exclusive prices for different VIP groups.

- :lucide-languages:{ .lg }  
  [__Set Up Multi-Language and Multi-Currency for Your Storefront__](../../website-management/setup-multi-language-and-multi-currency.md){ title="Set Up Multi-Language and Multi-Currency for Your Storefront" }  
  Build a multi-language online store with local currency display.

- :lucide-search:{ .lg }  
  [__Google Shopping Ads Settings (GMC)__](../../integrations/google/setup-google-merchant-center.md){ title="Set Up Google Merchant Center and Sync CYBERBIZ Products" }  
  Sync products to Google Merchant Center.

</div>

---

## FAQ { #faq-product }

??? quote "I have many products. Do I have to create them one by one?"
    [](){ #faq-product-bulk-import }
    No. When you have many products, we recommend **Excel bulk import** to create or update them all at once. See [Bulk import products](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }.

??? quote "Why does the storefront show 'Required' or not allow purchase even though I set a price?"
    [](){ #faq-product-no-price }
    Make sure you've **created variants** first. Price, inventory, and SKU all belong to variants, so without variants you can't set a price or sell the product. In variant management, choose "Create a single style product" or "Create a multiple variant product", then set them.

??? quote "Why can't I find the 'Product Description' and 'Settings' tabs after adding a product?"
    [](){ #faq-product-no-tabs }
    These two tabs appear only **after the product is saved**. Fill in the required product name in "Product Information" and click "Save". Once the system switches to edit mode, the other tabs appear at the top.

??? quote "Can't find the 'Volume (CM)' or 'Cost' field?"
    [](){ #faq-product-no-meas }
    Volume and cost are both plan-limited features and appear in variants only after they're enabled. If you see only "Weight (KG)" and "Price" without these fields, they aren't enabled yet; contact your sales representative.

??? quote "Can't find the language switcher menu?"
    [](){ #faq-product-no-language-switch }
    The language switcher appears to the right of the product edit page title only after **storefront multi-language** is enabled. If you don't see it, your store hasn't enabled this feature; contact CYBERBIZ customer service.

??? quote "What's the difference between setting a product to 'Unpublished' and 'Disable Search'?"
    [](){ #faq-product-hidden-vs-search }
    **Unpublished** hides the product completely from the storefront, and it can't be bought through its link. **Disable Search** only keeps the product out of on-site search results; customers can still buy it normally through the product link. See the [product status reference](../references/product-statuses.md#reference-product-statuses){ title="Product Status Reference" }.

---

## References { #reference-product }

- [Product Status Reference](../references/product-statuses.md){ title="Product Status Reference" }
- [Fulfillment Method Reference](../references/product-warehouse.md){ title="Fulfillment Method Reference" }
- [Shipping Temperature Zone Reference](../references/product-temperature.md){ title="Shipping Temperature Zone Reference" }

<!---->
<!-- --- -->
<!---->
<!-- Create a single product, set its basic information, images, videos, and variants, and launch it. -->
<!-- { .subtitle } -->
<!---->
<!-- ![Add a product](../../../assets/images/ec-create-new-product.zh-tw.en.png){ title="Add a Product: Products > All Products > Add Product" .hero-page } -->
<!---->
<!-- ## About Adding and Updating Products { #overview } -->
<!---->
<!-- In CYBERBIZ, you can add and update products in two ways: "[one at a time](#operate-product-add-single)" or "Excel bulk import". -->
<!---->
<!-- ??? info "Some Fields Must Be Enabled First"  -->
<!--     The following fields appear depending on your plan / add-on features, so not every store has all of them: -->
<!---->
<!--     - **Price, inventory:** Built into all plans; no activation needed. -->
<!--     - **Product Video** PLUS / Enterprise, and requires a **Drag-and-Drop Theme** theme. -->
<!--     - **Vol.(CM)** An add-on feature; appears in variants only after it's enabled. -->
<!--     - **Multi-language fields:** Requires **storefront multi-language**. -->
<!--     - **Amazon fulfillment (FBA):** Once enabled, Amazon fulfillment can be selected as the fulfillment method, and SKUs must match the Amazon warehouse. -->
<!---->
<!-- ## Add a Single Product { #operate-product-add-single } -->
<!---->
<!-- For listing a small number of products, with detailed control over each setting. -->
<!---->
<!-- 1. Sign in to the admin and go to "Products" > "All Products" > "Add Product". -->
<!-- 2. Set the product information in order: [Basic settings](#operate-product-basic-settings), [Product images](#reference-product-images), [Product videos](#reference-product-video), [Variants](#reference-product-variants), [Inventory management](#operate-product-inventory). -->
<!-- 3. Click **Save** to apply the changes. -->
<!---->
<!-- ![Add a product](../../../assets/images/ec-商品-新增商品.en.png) -->
<!---->
<!-- --- -->
<!---->
<!-- ### Basic Settings { #operate-product-basic-settings } -->
<!---->
<!-- | Field | Setting Details and Rules | Default / Notes | -->
<!-- | :--- | :--- | :--- | -->
<!-- | **Product Name** | The title shown to customers. | Avoid special characters (such as `|`, `"`, `'`) so the data is stored and read correctly. | -->
<!-- | **Product URL** | Defines the last segment of the product page path (slug).<br> We recommend all lowercase English, with words separated by hyphens `-`. | If left blank, the system uses the "product name" as the URL suffix. | -->
<!-- | **Product Slogan/Brief** | Enter a marketing phrase that appeals to customers.<br> Supports plain text, or you can [switch to HTML mode for advanced formatting](edit-product-slogan-and-description.md){ title="Edit the Product Brief and Product Slogan" }. | — | -->
<!-- | **Sell Status** | Set the product's active sales period (scheduling). | If left blank, the product is "launched permanently".<br>**Note:** If the current time is outside the period, the storefront shows a 404 page. | -->
<!-- | **Search** | Decides whether the product can be found by on-site search or search engines (such as Google). | When turned off, the product can only be accessed directly through the **product link**. | -->
<!---->
<!-- ![Product basic settings](../../../assets/images/ec-商品-基本設定.en.png){ title="Product Basic Settings" } -->
<!---->
<!-- --- -->
<!---->
<!-- ### Product Images { #reference-product-images } -->
<!---->
<!-- Click **Upload Image** or drag images to upload them. When uploading product images, follow these technical specs: -->
<!---->
<!-- | Item | Spec | Details | -->
<!-- | :--- | :--- | :--- | -->
<!-- | Size | 1000 × 1000 px | A square ratio works best | -->
<!-- | File size | Up to 10 MB; 2 MB or less recommended | Large images slow down loading | -->
<!-- | Supported formats | JPG / PNG / JPEG / GIF | JPG or PNG recommended | -->
<!---->
<!-- !!! info "Cross-Channel Advertising Reminder: Google Shopping Ads (GMC)" -->
<!--     If you plan to sync products to Google for advertising, images must meet the [Google image requirements  -->
<!-- :lucide-external-link:](https://support.google.com/merchants/answer/6324350#Image_guidelines). Images that don't meet them can cause products to fail review. -->
<!---->
<!--     ??? example "View Google Image Restrictions and Examples" -->
<!---->
<!--         | Rule | Details | -->
<!--         | :--- | :--- | -->
<!--         | No price information | Don't show the price or discount amount in the image | -->
<!--         | No promotional text | Such as "Free shipping", "On sale", or "Limited-time offer" | -->
<!--         | No watermarks or logos | Product images must not be covered by brand marks | -->
<!--         | Show the product clearly | Use a white or solid background, with the product taking up 85% or more of the image | -->
<!---->
<!--         <div class="grid" markdown> -->
<!---->
<!--         :lucide-check: Compliant -->
<!--         ![GMC without watermark](../../../assets/images/ec-gmc-without-watermark.en.png){ title="GMC Without Watermark" .screenshot } -->
<!---->
<!--         :lucide-x: Non-compliant -->
<!--         ![GMC with watermark](../../../assets/images/ec-gmc-with-watermark.en.png){ title="GMC With Watermark" .screenshot } -->
<!---->
<!--         </div> -->
<!---->
<!-- ![Set product images](../../../assets/images/ec-商品-商品圖片-上傳.en.png){ title="Set Product Images" } -->
<!---->
<!-- --- -->
<!---->
<!-- ### Product Videos { #reference-product-video } -->
<!---->
<!-- [:lucide-tag:{ title="Applicable Plans" }](conventions.md#適用方案) | PLUS / Enterprise   -->
<!-- [:lucide-bolt:{ title="Applicable Features" }](conventions.md#適用功能) | Drag-and-Drop Theme -->
<!---->
<!-- - Resolution: Up to 1280 × 1280 pixels. -->
<!-- - Recommended ratio: 9:16, optimized for Facebook ad placements. -->
<!-- - Video format: MP4 only. -->
<!-- - Video length: Up to 60 seconds. -->
<!-- - File size: Up to 30 MB. Loading speed depends on the viewer's network, so compress files as much as possible within the specs. -->
<!-- - Audio: Audio output isn't supported yet; uploaded videos play muted. -->
<!---->
<!-- !!! info "More about product videos](setup-product-videos.md)videos](setup-product-videos.md){ title="Set Up Product Videos" }." -->
<!---->
<!-- --- -->
<!---->
<!-- ### Variant Management { #reference-product-variants }  -->
<!---->
<!-- To set prices and inventory, you must first create **variants**: -->
<!---->
<!-- - **Single Variant** Set the price (actual selling price), compare-at price (suggested retail price), cost (for internal analysis, not visible on the storefront), and product number (SKU). -->
<!-- - **Multi-variant product:** Click **Edit product options** and add options such as color and size in order. Each option needs at least one value (up to 3 options). -->
<!-- - **Apply to all:** When multiple variants share the same price or inventory, choose **Edit price / Edit inventory / Edit volume and weight / Edit all** above the variants section, select the variants, enter the values, and click **Apply** to fill them in at once. -->
<!---->
<!-- !!! note "Cross-Border / Overseas Sites" -->
<!--     - **Use English for options:** For English-language sites such as the North America site, we recommend naming options and values in English. -->
<!--     - **Weight and volume:** Overseas logistics usually charge by weight or volume, so be sure to fill them in for each variant (volume is an add-on feature; the "Volume (CM)" field appears only after it's enabled). -->
<!--     - **Customs information:** Data needed for customs declarations (such as item name and country of origin) is filled in at the **shipping stage** based on the selected cross-border carrier, **not on the product page**. -->
<!---->
<!-- --- -->
<!---->
<!-- ### Manage Inventory { #operate-product-inventory } -->
<!---->
<!-- Once enabled, you can set the inventory quantity and a "safety stock level". When inventory reaches zero, you can choose "Stop selling" or "Continue selling (allow pre-orders)". -->
<!---->
<!-- --- -->
<!---->
<!-- ### Multi-Language: Fill In Product Content per Language { #specs-product-multilang } -->
<!---->
<!-- If your store has **storefront multi-language** enabled, a **language switcher** (a language icon and drop-down menu) appears to the right of the product edit page title so you can enter text separately for each language. -->
<!---->
<!-- Note **which fields are translated per language and which are shared by all languages**: -->
<!---->
<!-- - **Translated per language:** Product name, product slogan, product brief, product options, option values, and the content on the product description page (covered in [Edit Product Descriptions and Product Settings](edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }). -->
<!-- - **Shared by all languages:** Price, variants, SKU, inventory, product images, categories, and tags. Set these once; switching languages doesn't change them. -->
<!---->
<!-- How to do it: -->
<!---->
<!-- 1. Choose a **primary language**, fill in the product content as usual, and **Save**. -->
<!-- 2. Switch languages from the drop-down to the right of the title. If you have unsaved changes, the system shows "Save your changes before editing other languages"; save first. -->
<!-- 3. After switching, a label for the language being edited appears next to translatable fields. Enter the translated text in each field. -->
<!-- 4. Click **Save**, then switch to other languages and repeat. -->
<!---->
<!-- ## Update Existing Products { #operate-product-update } -->
<!---->
<!-- To change information for existing products, you can: -->
<!---->
<!-- === ":lucide-square-pen: Edit One Product" -->
<!---->
<!--     Click a product in the product list, change its content on the edit page, and be sure to click **Save** when done. For multi-language stores, make sure you switch to the correct language before editing. -->
<!---->
<!-- === ":lucide-import: Bulk Edit (Excel)" -->
<!---->
<!--     1. Go to "Products" > "All Products", select the items to change, and click **Export product**. -->
<!--     2. Open the downloaded Excel file and enter the changes in the corresponding columns (such as description, channel, temperature zone, or delivery method). -->
<!--     3. Go to the **"Import Products in Bulk from Excel"** page and upload the edited file. See [Import Products in Bulk from Excel](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }. -->
<!---->
<!-- === ":lucide-receipt-text: Edit Products in an Order" -->
<!---->
<!--     In "All Orders", you can use **"Edit Order"** on an order's details page to change product quantities or add "Off Market / Unpublished" products. -->
<!---->
<!-- ## Key Differences in Excel Bulk Operations { #operate-product-excel-diff } -->
<!---->
<!-- When you work in bulk with Excel, the system decides between "add" and "update" based on **hidden columns**: -->
<!---->
<!-- - **Add products:** Use the "Download Excel template" provided in the admin. Its hidden **column A (product ID) and column B (variant ID) are empty**. After upload, the system treats the rows as brand-new products. -->
<!-- - **Update products:** You must first **export existing products** from the "Product list". In the exported file, **columns A and B contain system-generated IDs**. After you upload it, the system matches the IDs and overwrites (updates) the existing product content. -->
<!---->
<!-- For full details, see [Import Products in Bulk from Excel](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }. -->
<!---->
<!-- ## Important Notes and Reminders { #specs-product-notes } -->
<!---->
<!-- - **Why SKUs matter:** If you use warehouse integration, a POS system, or Amazon FBA, **SKUs are required and must be unique**. When shipping with Amazon FBA, SKUs must match the Amazon warehouse for orders to be sent successfully. -->
<!-- - **Multi-language:** If your site has multi-language enabled, switch language tabs to fill in each language when listing products (name, brief, options, and other fields support multi-language editing). See [Multi-Language: Fill In Product Content per Language](#specs-product-multilang). -->
<!-- - **Exclude from sync:** To keep a product off Google, LINE shopping, or Facebook Shops, enter " **gift** " or " **exclude product feed** " in the tags field. -->
<!-- - **Import status:** Uploaded files are processed in a background job. Wait for the "Data import complete" email from the system. If the import fails, the email explains why. -->
<!---->
<!-- ## Next Steps { #next-steps } -->
<!---->
<!-- <div class="grid cards" markdown> -->
<!---->
<!-- - :lucide-import:{ .lg }    -->
<!--   [__Add Products in Bulk__](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }    -->
<!--   Import products in bulk with Excel and list them all at once. -->
<!-- - :lucide-boxes:{ .lg }    -->
<!--   [__Add Combo Products__](create-and-setup-combo-products.md#operate-combo-products){ title="Create and Set Up Product Combos" }   -->
<!--   Create specified or optional combo products. -->
<!-- - :lucide-edit-3:{ .lg }    -->
<!--   [__Edit Product Descriptions and Settings__](edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }    -->
<!--   Edit the product description and Settings tab information. -->
<!-- - :lucide-bell:{ .lg } ](../engagement/setup-back-in-stock-notifications.md)./engagement/setup-back-in-stock-notifications.md){ title="Set Up Back-in-Stock Notifications" }   -->
<!--   Set up back-in-stock notifications to tell customers when products they follow are restocked. -->
<!-- - :lucide-check-square:{ .lg }    -->
<!--   [__Bulk Edit Product Information__](../bulk-operations/batch-update-product-descriptions-shipping.md){ title="Batch Edit Product Descriptions and Shipping Settings" }   -->
<!--   Update information and settings for multiple products at once. -->
<!-- - :lucide-search-x:{ .lg }    -->
<!--](../discoverability/product-search-visibility.md)ty/product-search-visibility.md){ title="Set Product Search Visibility" }    -->
<!--   Keep products out of specific search results. -->
<!---->
<!-- </div> -->
<!---->
<!-- ## FAQ { #faq } -->
<!---->
<!-- ??? quote "Can product names use special characters or HTML?" -->
<!--     Product names **can't use special characters** (such as `|` or `"`) or **HTML tags**. Use plain text for product names. -->
<!---->
<!-- ??? quote "Is there a limit on options for multi-variant products?" -->
<!--     A product can have up to 3 options, and each option needs at least 1 value. For example, if you set a "Color" option, add at least one color. -->
<!---->
<!-- ??? quote "With multi-language on, why didn't the price in other languages change when I changed it?" -->
<!--     This is normal. Price, variants, inventory, and images are fields **shared by all languages** and only need to be set once. Only text fields (name, slogan, brief, options, description) are filled in per language. -->
<!---->
<!-- ??? quote "Can't find the language switcher drop-down menu?" -->
<!--     The language switcher appears to the right of the product edit page title only after **storefront multi-language** is enabled. If you don't see it, your store hasn't enabled this feature; contact CYBERBIZ customer service. -->
<!---->
<!-- --- -->
<!---->
<!-- Create a single product, set its basic information, images, videos, and variants, and launch it. -->
<!-- { .subtitle } -->
<!---->
<!-- ![Add a product](../../../assets/images/ec-create-new-product.zh-tw.en.png){ title="Add a Product: Products > All Products > Add Product" .hero-page } -->
<!---->
<!---->
<!-- ## About Adding and Updating Products -->
<!---->
<!-- In CYBERBIZ, you can add and update products in two ways: "[one at a time](#operate-product-add-single)" or "Excel bulk import". -->
<!---->
<!-- ## Add a Single Product -->
<!---->
<!-- For listing a small number of products, with detailed control over each setting. -->
<!---->
<!-- 1. Sign in to the CYBERBIZ admin and click "Products" > "All Products" > "Add Product". -->
<!-- 2. Set the product information in order: [Basic settings](#operate-product-basic-settings), [Product images](#reference-product-images), [Product videos](#reference-product-video), [Variants](#reference-product-variants), [Inventory management](#operate-product-inventory). -->
<!-- 3. Click **Save** to apply the changes. -->
<!---->
<!-- ![Add a product](../../../assets/images/ec-商品-新增商品.en.png) -->
<!---->
<!-- --- -->
<!---->
<!-- ### Basic Settings -->
<!---->
<!-- | Field | Setting Details and Rules | Default / Notes | -->
<!-- | :--- | :--- | :--- | -->
<!-- | **Product Name** | The title shown to customers. | Avoid special characters (such as `|`, `"`, `'`) so the database stores and reads the data correctly. | -->
<!-- | **Product URL** | Defines the last segment of the product page path (slug).<br> We recommend all lowercase English, with words separated by hyphens `-`. | If left blank, the system uses the "product name" as the URL suffix. | -->
<!-- | **Product Slogan/Brief** | Enter a marketing phrase that appeals to customers.<br> Supports plain text, or you can [switch to HTML mode for advanced formatting](edit-product-slogan-and-description.md){ title="Edit the Product Brief and Product Slogan" }. | — | -->
<!-- | **Sell Status** | Set the product's active sales period (scheduling). | If left blank, the product is "launched permanently".<br>**Note:** If the current time is outside the period, the storefront shows a 404 page. | -->
<!-- | **Search** | Decides whether the product can be found by on-site search or search engines (such as Google). | When turned off, the product can only be accessed directly through the [**product link**](#保留特定存取途徑). | -->
<!---->
<!-- <!-- -->
<!-- *   **Product name**: Enter the product title. Avoid special characters (such as `|`, `"`, `'`) so the database stores the data correctly. -->
<!-- *   **Product URL**: Defines the last segment of the product page URL. We recommend all English, lowercase letters, with words separated by hyphens `-`[^*]. -->
<!--     - **Default**: If not set, the system uses the "product name" as the URL suffix. -->
<!--     - **Product slogan/product brief**: Enter a marketing phrase that appeals to customers. Supports plain text, or switch to HTML mode for advanced formatting. [Advanced settings guide](edit-product-slogan-and-description.md){ title="Edit the Product Brief and Product Slogan" } -->
<!-- *   **Sell status (scheduling)**: Set the product's active sales period. If the current time is outside the period, the page shows a 404 Not Found page. -->
<!--     - **Default**: If not set, the product is "launched permanently". -->
<!-- *   **Search**: Decides whether the product can be found by on-site search or Google. When turned off, the product can only be accessed through a direct link to the product page. -->
<!---->
<!-- ![Product basic settings](../../../assets/images/ec-商品-基本設定.en.png){ title="Product Basic Settings" } -->
<!---->
<!-- [^*]: English URLs carry more weight in search engines (SEO) and avoid unreadable garbled text in analytics reports. -->
<!---->
<!-- --- -->
<!---->
<!-- ### Product Images -->
<!---->
<!-- Click **Upload Image** or drag images to upload them. When uploading product images, follow these technical specs: -->
<!---->
<!-- | Item | Spec | Details | -->
<!-- | :--- | :--- | :--- | -->
<!-- | Size | 1000 × 1000 px | A square ratio works best | -->
<!-- | File size | Up to 10 MB; 2 MB or less recommended | Large images slow down loading | -->
<!-- | Supported formats | JPG / PNG / JPEG / GIF | JPG or PNG recommended | -->
<!---->
<!---->
<!-- !!! info "Cross-Channel Advertising Reminder: Google Shopping Ads (GMC)" -->
<!--     If you plan to sync products to Google for advertising, images must meet the [Google image requirements :lucide-external-link:](https://support.google.com/merchants/answer/6324350#Image_guidelines). Images that don't meet them can cause products to fail review. -->
<!---->
<!--     ??? example "View Google Image Restrictions and Examples" -->
<!---->
<!--         | Rule | Details | -->
<!--         | :--- | :--- | -->
<!--         | No price information | Don't show the price or discount amount in the image | -->
<!--         | No promotional text | Such as "Free shipping", "On sale", or "Limited-time offer" | -->
<!--         | No watermarks or logos | Product images must not be covered by brand marks | -->
<!--         | Show the product clearly | Use a white or solid background, with the product taking up 85% or more of the image | -->
<!---->
<!--         <div class="grid" markdown> -->
<!---->
<!--         :lucide-check: Meets Requirements -->
<!--         ![GMC without watermark](../../../assets/images/ec-gmc-without-watermark.en.png){ title="GMC Without Watermark" .screenshot } -->
<!---->
<!--         :lucide-x: Doesn't Meet Requirements -->
<!--         ![GMC with watermark](../../../assets/images/ec-gmc-with-watermark.en.png){ title="GMC With Watermark" .screenshot } -->
<!---->
<!--         </div> -->
<!---->
<!-- ![Set up product images](../../../assets/images/ec-商品-商品圖片-上傳.en.png){ title="Set Up Product Images" } -->
<!---->
<!-- --- -->
<!---->
<!-- ### Product Videos -->
<!---->
<!-- [:lucide-tag:{ title="Applicable Plans" }](conventions.md#適用方案) | PLUS / Enterprise   -->
<!-- [:lucide-bolt:{ title="Applicable Features" }](conventions.md#適用功能) | Drag-and-Drop Theme -->
<!---->
<!-- - Resolution: Up to 1280 × 1280 pixels. -->
<!-- - Recommended ratio: 9:16, optimized for Facebook ad placements. -->
<!-- - Video format: MP4 only. -->
<!-- - Video length: Up to 60 seconds. -->
<!-- - File size: Up to 30 MB. Loading speed depends on the viewer's network, so compress the file as much as possible within the specs. -->
<!-- - Audio: Audio output isn't supported yet; uploaded videos play muted. -->
<!---->
<!-- !!!](setup-product-videos.md) video settings, see [Set Up Product Videos](setup-product-videos.md){ title="Set Up Product Videos" }." -->
<!---->
<!-- --- -->
<!---->
<!-- ### Variant Management -->
<!---->
<!-- === "Standard Products" -->
<!---->
<!--     *   **Single Variant**: Set the price (actual sale amount), compare-at price (suggested retail price), cost (for internal analysis; not visible to customers), and product number (SKU). -->
<!--     *   **Multi-variant products**: Click "Add option" and add items such as color and size in order. Each option needs at least one value. -->
<!--     *   **Apply to all**: If several variants share the same price or inventory, select them and choose "Apply to all" to enter the amount once. -->
<!---->
<!-- === "Cross-Border Products" -->
<!---->
<!--     *   **Single Variant**: Set the price (actual sale amount), compare-at price (suggested retail price), cost (for internal analysis; not visible to customers), and product number (SKU). -->
<!--     *   **Multi-variant products**: Click "Add option" and add items such as color and size in order. Each option needs at least one value. **For the North America site, use English option names**. -->
<!--     *   **Apply to all**: If several variants share the same price or inventory, select them and choose "Apply to all" to enter the amount once. -->
<!--     *   **Customs information**: If you use CYBERBIZ EXPRESS, also fill in customs information such as JANCODE, ingredients, and country of origin, preferably in Japanese or English. -->
<!---->
<!-- --- -->
<!---->
<!-- ### Manage Inventory -->
<!---->
<!-- When enabled, you can set the inventory quantity and a "safety stock level". When inventory reaches zero, you can choose "Stop selling" or "Continue selling (allow pre-orders)". -->
<!---->
<!-- ## Update Existing Products -->
<!---->
<!-- To change information for existing products, you can: -->
<!---->
<!-- === ":lucide-square-pen: Edit One Product" -->
<!---->
<!--     Click a product in the product list, change its content on the edit page, and be sure to click **Save** when done. For multi-language stores, make sure you switch to the correct language before editing. -->
<!---->
<!-- === ":lucide-import: Bulk Edit (Excel)" -->
<!---->
<!--     1. Go to "Products" > "All Products", select the items to change, and click **Export product**. -->
<!--     2. Open the downloaded Excel file and enter the changes in the corresponding columns (such as description, channel, temperature zone, or delivery method). -->
<!--     3. Go to the **"Import Products in Bulk from Excel"** page and upload the edited file. See [Import Products in Bulk from Excel](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }. -->
<!---->
<!-- === ":lucide-receipt-text: Edit Products in an Order" -->
<!---->
<!--     In "All Orders", you can use **"Edit Order"** on an order's details page to change product quantities or add "Off Market / Unpublished" products. -->
<!---->
<!-- ## Key Differences in Excel Bulk Operations -->
<!---->
<!-- When you work in bulk with Excel, the system decides between "add" and "update" based on **hidden columns**: -->
<!---->
<!-- *   **Add products**: Use the "Download Excel template" provided in the admin. Its hidden **column A (product ID) and column B (variant ID) are empty**. After upload, the system treats the rows as brand-new products. -->
<!-- *   **Update products**: You must first **export existing products** from the "Product list". In the exported file, **columns A and B contain system-generated IDs**. After you upload it, the system matches the IDs and overwrites (updates) the existing product content. -->
<!---->
<!-- ## Important Notes and Reminders -->
<!---->
<!-- *   **Why SKUs matter**: If you use warehouse integration or a POS system, **SKUs are required** and must be unique. -->
<!-- *   **Multi-language**: If your site has multi-language enabled, remember to switch language tabs when listing products (name, brief, options, and other fields support multi-language editing). -->
<!-- *   **Exclude from sync**: To keep a product off Google, LINE live shopping, or Facebook Shops, enter " **gift** " or " **exclude product feed** " in the tags field. -->
<!-- *   **Import status**: Uploaded files are processed in a background job. Wait for the "Data import complete" email from the system. If the import fails, the email explains why. -->
<!---->
<!---->
<!---->
<!-- ## Next Steps -->
<!---->
<!-- <div class="grid cards" markdown> -->
<!---->
<!-- - :lucide-import:{ .lg }    -->
<!--   [__Add Products in Bulk__](../bulk-operations/excel-import-products.md){ title="Import Products in Bulk from Excel" }    -->
<!--   Import products in bulk with Excel and list them all at once. -->
<!-- - :lucide-boxes:{ .lg }    -->
<!--   [__Add Combo Products__](create-and-setup-combo-products.md#operate-combo-products){ title="Create and Set Up Product Combos" }   -->
<!--   Create specified or optional combo products. -->
<!-- - :lucide-edit-3:{ .lg }    -->
<!--   [__Edit Product Descriptions and Settings__](edit-product-description-settings.md){ title="Edit Product Descriptions and Product Settings" }    -->
<!--   Edit the product description and Settings tab information. -->
<!-- - :lucide-bell:{ .lg }    -->
<!--   [__Back-in-Stock Notifications__](../engagement/setup-back-in-stock-notifications.md){ title="Set Up Back-in-Stock Notifications" }   -->
<!--   Set up back-in-stock notifications to tell customers when products they follow are restocked. -->
<!-- - :lucide-check-square:{ .lg }    -->
<!--   Update information and settings for multiple products at once. -->
<!-- - :lucide-search-x:{ .](../discoverability/product-search-visibility.md)../discoverability/product-search-visibility.md){ title="Set Product Search Visibility" }    -->
<!--   Keep products out of specific search results. -->
<!---->
<!-- </div> -->
<!---->
<!-- ## FAQ -->
<!---->
<!-- ??? quote "Can product names use special characters or HTML?" -->
<!--     Product names **can't use special characters** (such as `\|` or `”`) or **HTML tags**. Use plain text for product names. -->
<!---->
<!-- ??? quote "Is there a limit on options for multi-variant products?" -->
<!--     Each variant needs at least *1* item. For example, if you set a color option, add at least one color. -->
<!---->
<!-- [^1]: Volumetric calculation used by domestic logistics in Taiwan. -->
<!-- [^2]: Overseas logistics usually charge by weight. -->
<!---->
<!---->
