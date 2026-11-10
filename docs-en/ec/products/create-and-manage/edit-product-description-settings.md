---
title: "Edit Product Descriptions and Product Settings"
description: "Set up product content, channels, and logistics attributes so products display correctly on the storefront and support search and marketing."
created: 2026-03-08 10:00
last_modified: 2026-07-22 17:21
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
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 編輯商品描述
  - 設定商品資訊
  - 設定商品通路
  - 設定物流屬性
  - 設定商品SEO
  - 設定相關商品
features:
  - 商品描述編輯器
  - 商品設定管理 (類型, 通路, 廠商, 群組, 標籤)
  - 物流與溫層設定
  - SEO 設定
  - 相關商品設定
  - 快速操作按鈕 (公開, 前往, 複製, 刪除)
prerequisites: []
related:
  - ec/products/create-and-manage/create-update-products/
  - ec/website-appearance/code-customization/text-editor/
  - ec/products/categories-and-tags/custom-collections/
  - ec/marketing/discounts/mix-and-match-discounts/
  - ec/products/categories-and-tags/manage-product-tags/
  - ec/products/checkout/checkout-split-multi-cart/
  - ec/integrations/google/setup-google-merchant-center/
  - ec/products/shipping/setup-product-shipping-conditions/
  - ec/payments-and-logistics/home-delivery-cash-on-delivery/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
  - ec/website-management/seo/seo-guide/
  - ec/products/bulk-operations/batch-update-product-descriptions-shipping/
tags:
  - "Product Description"
  - "Product Settings"
  - Logistics
  - "Temperature Zone"
  - SEO
  - "Product Tags"
  - "Related Products"
  - "Product Types"
  - "Product Channels"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理後台 > 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7701
  - https://www.cyberbiz.io/support/?p=7497
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/edit-product-description-settings/"
search:
  exclude: false
icon: lucide/file-text
hide:
comments: false
---

![Edit product descriptions](../../../assets/images/ec-edit-product-hero.zh-tw.en.png){ title="Edit Product Descriptions" .hero-page }

## About Product Descriptions and Settings { #intro-product-desc-settings }

On the product edit page (Products > All Products > the name of the product to edit), you can edit and set the product's information and attributes for admin management and storefront display. Product information settings are organized into three tabs:

- [Product Information](create-update-products.md#operate-product){ title="Add and Update Products" }: [Core settings](create-update-products.md#operate-product-create-basic){ title="Add and Update Products" } such as the product name, options, price, and inventory.
- [Product Description](#operate-desc-settings-body): The product description, specifications, and shipping information shown to storefront customers.
- [Settings](#operate-product-desc-settings): Type, channel, vendor, collections, tags, logistics, and SEO, for managing admin attributes and marketing settings.

!!! tip "Quick Action Buttons"

    - :lucide-eye: Published: Set whether the product is published.
    - :lucide-external-link: Go to Product Page: Open the product's storefront page.
    - :lucide-copy: Copy: Copy the product for quick editing.
    - :lucide-trash-2: Delete Product: Delete the product.

## Product Description { #operate-desc-settings-body }

Use the text editor to edit the following fields:

- **Product Introduction**: Provide detailed product information
- **Product Specifications**: Describe the product specification details
- **Delivery Type**: Describe the product's shipping information

To learn more about the text editor, see [Edit Content with the Text Editor](../../website-appearance/code-customization/text-editor.md){ title="Edit Content with the Text Editor" }.

![Edit the product description](../../../assets/images/ec-product-description.zh-tw.en.png){ title="Edit the Product Description" }

??? info-clean "Where It Appears on the Storefront"
    ![Storefront product description](../../../assets/images/ec-product-description-frontend.zh-tw.en.png){ title="Storefront Product Description" }

## Product Settings { #operate-product-desc-settings }

![Product settings page](../../../assets/images/ec-product-settings.zh-tw.en.png){ title="Product Settings Page" }

### Advanced Settings { #operate-product-desc-settings-advanced }

- **Customized collections**: Add the product to existing collections. Details in [Set Up Customized Collections](../categories-and-tags/custom-collections.md){ title="Set Up Customized Collections" }.
- **Buy X Get Y Discount Collection**: Add the product to an existing Buy X Get Y discount collection. Details in [Buy X Get Y Discount](../../marketing/discounts/mix-and-match-discounts.md){ title="Buy X Get Y Discount" }.
- **Tags**: Add tags to the product for marketing campaigns (for example, a product-specific coupon). Learn [how to set product tags](../categories-and-tags/manage-product-tags.md){ title="Manage Product Tags" }.
- **Product Type**: Set a type label for the product for management and filtering. This information also appears on the storefront, and the label content can be customized.
- **Product distribution channel**: Set the channels where the product can be sold. Products from different channels (pre-order, in stock, room temperature) are automatically [split into multiple carts](../checkout/checkout-split-multi-cart.md#intro-split-cart){ title="Set Up Automatic Checkout Splitting into Multiple Carts" } at checkout.
- **Product Vendor**: Add a vendor label to the product for management and filtering. This information also appears on the storefront, and the content can be customized.
- **Google product category**: Set the product category to override Google's automatic classification and improve ad targeting. Learn [how to sync products to GMC](../../integrations/google/setup-google-merchant-center.md){ title="Set Up Google Merchant Center and Sync CYBERBIZ Products" }.

    ![GMC product category](../../../assets/images/ec-商品-商品編輯-設定-google產品類別.en.gif){ title="GMC Product Category" }

!!! warning "Once added, product types, product channels, and product vendors cannot be deleted. Proceed with care."

---

### Temperature Zone and Logistics Settings { #operate-product-desc-settings-ship }

Set the product's shipping temperature zone and available logistics methods.

- **Shipping Temperature**: Specify the shipping temperature zone the product accepts. Details in [standard home delivery](../shipping/setup-product-shipping-conditions.md){ title="Set Up Product Shipping Conditions (Logistics, Temperature Zone, and Fulfillment Channel)" } and [home delivery cash on delivery](../../payments-and-logistics/home-delivery-cash-on-delivery.md){ title="Home Delivery Cash on Delivery Logistics (T-Cat/Pelican/Hsinchu Logistics)" } for linking a product's logistics, temperature zone, and sales channels.
- **Logistics link status**: Specify the logistics methods available for the product. For details, see how to [set up convenience store delivery restrictions and logistics exclusions](../shipping/cvs-shipping-restrictions-exclusions.md){ title="Set Up Convenience Store Delivery Restrictions and Logistics Exclusions" }

![Temperature zone and logistics settings](../../../assets/images/ec-shipping-temperature-logistics-setting.zh-tw.en.png){ title="Temperature Zone Logistics Settings" }

!!! tip "We recommend completing the [logistics method settings](../shipping/setup-product-shipping-conditions.md){ title="Set Up Product Shipping Conditions (Logistics, Temperature Zone, and Fulfillment Channel)" } before this step, so you can select the applicable logistics methods directly."

---

### Set up Related Products { #operate-product-desc-settings-related }

By setting a **Related Collection**, you can customize the relationships between products to improve the *Related Products* section below the product page and increase cross-selling.

![Related products settings](../../../assets/images/ec-related-collection.zh-tw.en.png){ title="Related Products Settings" }

??? info-clean "Where It Appears on the Storefront"
    ![Storefront related products](../../../assets/images/ec-product-related-collection-frontend.zh-tw.en.png){ title="Storefront Related Products" }

---

### SEO Settings { #operate-product-desc-settings-seo }

Setting product SEO can improve the page's ranking in search engines. Set it based on the product's characteristics.

- **Meta Title**: Shown in the web browser. It affects the title customers see when they find this product page in search.
- **Meta Description**: Shown in the web browser. It affects the description customers see when they find this product page in search.
- **Meta Keywords**: Usually not shown in the web browser. It affects the keywords customers use to find this product page in search.

![SEO settings](../../../assets/images/ec-product-seo-setting.zh-tw.en.png){ title="SEO Settings" }

<div class="grid cards" markdown>

- :lucide-search:{ .lg } [__SEO Settings and Optimization Guide__](../../website-management/seo/seo-guide.md){ title="SEO Settings and Optimization Guide" }

</div>

## Next Steps { #next-steps-product-desc-settings }

<div class="grid cards" markdown>

- :lucide-import:{ .lg }  
  [__Batch Edit Product Descriptions and Settings__](../bulk-operations/batch-update-product-descriptions-shipping.md){ title="Batch Edit Product Descriptions and Shipping Settings" }  
  Import an edited product Excel file to update the product descriptions and shipping settings of many products at once.

- :lucide-ban:{ .lg }  
  [__Logistics Restrictions and Exclusion Options__](../shipping/cvs-shipping-restrictions-exclusions.md){ title="Set Up Convenience Store Delivery Restrictions and Logistics Exclusions" }  
  Set the product's shipping logistics conditions to limit which logistics methods are shown and used at checkout.

</div>

## FAQ { #faq-product-desc-settings }

??? quote "Can I use HTML tags in product descriptions?"
    The product description sections (Product Introduction, Product Specifications, and Delivery Type) support the text editor, which lets you format text and edit images and links. For more advanced layouts, we recommend the drag-and-drop theme.

??? quote "What should I watch for when setting product temperature zones and logistics?"
    We recommend setting up your logistics methods before you set product temperature zones and logistics, so you can select the matching logistics options directly.
