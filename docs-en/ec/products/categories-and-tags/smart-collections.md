---
title: "Set up Conditionalized Collections"
description: "Automatically sort products that match your rules into a specified collection based on product attributes and conditions."
created: 2026-01-15 00:00
last_modified: 2026-07-22 17:40
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - POS 前台選單設定
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
  - 如何設定商品條件分類群組
  - 自動商品分類設定
features:
  - 商品群組
  - 商品條件分類
prerequisites: []
related:
  - ec/products/references/smart-collections-rule-columns/
  - ec/products/references/smart-collections-rule-relations/
  - ec/products/references/smart-collections-sort-order/
  - ec/products/references/multi-language-supported/
  - ec/website-appearance/navigation/setup-menus-navigation/
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 商品條件分類
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=11174
  - https://www.cyberbiz.io/helpcenter/?p=9185
  - https://www.cyberbiz.io/support/?p=43379
  - https://www.cyberbiz.io/support/?p=7291
permalink: "https://help.cyberbiz.io/ec/products/categories-and-tags/smart-collections/"
search:
  exclude: false
icon: lucide/sparkles
hide: []
comments: false
---

![Conditionalized collections hero](../../../assets/images/ec-product-conditionalized-collections.zh-tw.en.png){ title="Automatic Product Collections: Products > Conditionalized Collections" .hero-page }

## About Conditionalized Collections { #intro-smart-collections }

"Conditionalized Collections" let you set a group of product filter conditions so that every product matching them is added to the collection automatically, without hand-picking products one by one. When you later add products, change prices, or inventory changes, the system automatically adds products that match
and removes products that no longer match, so the collection always stays up to date.

Compared with "customized collections" (products picked manually), the differences are:

| Type | How Products Are Added | Best For |
| :-- | :-- | :-- |
| Conditionalized collection | Set conditions; matching products are added or removed automatically | Collections that keep changing, such as "Under NT$1,000", "New for Summer", or "Specific vendor" |
| Customized collection (manual) | Pick products manually one by one | Fixed collections whose members need precise control, such as campaign picks |

!!! info "Tip"
    A product can match multiple conditionalized collections and can be in both customized and conditionalized collections at the same time without conflict.

---

## Prerequisites and Limits { #prerequisites-smart-collections }

Before you set up a conditionalized collection, check the following:

- [x] **Your store has products**: Conditionalized collections filter existing products. If the store has no products or none match the conditions, the collection will be empty.
- [x] **Product data is complete**: Filtering compares fields such as product name, type, vendor, tags, price, and inventory. The more complete these fields are, the more accurate the collection.

!!! plan "Plan / Activation Requirements"
    [Multi-language translation settings](#operate-smart-collections-multi-language), described later in this article, is optional and requires the multi-language store feature. Without it, the collection edit page has no language menu, and you can create content only in the default language (Traditional Chinese). If you're not sure whether it's enabled, contact your CYBERBIZ sales representative.

---

## Steps { #operate-smart-collections }

The following explains, in order, how to create a conditionalized collection, set filter conditions, adjust product sorting, publish it, and provide translations for each language.

### 1. Create a Conditionalized Collection and Fill in Basic Details { #operate-smart-collections-create }

1. **Open the Conditionalized Collections page:** In the admin's left menu, click "Conditionalized Collections" to open the collection list.
2. **Add a collection:** Click **Add a new collection** in the upper-right corner to open the "Collection Settings" page.
3. **Enter the collection name:** Enter a name for the collection in **"Collection Name"**, for example, "New for Summer".
4. **Set the collection URL:** Customize the link path of the collection page in **"Collection URL"**. If left blank, the system generates one automatically.
5. **Enter the collection description (optional):** In the **"Collection Description"** editor, enter the text to show on the collection page.
6. **Save**: Click **Save** at the bottom of the page. After saving, the **Product** tab appears at the top of the page so you can set filter conditions.

![Add a conditionalized collection](../../../assets/images/ec-smart-collections-create.en.png)

!!! note "Notes"
    Collection URLs must be unique within a store, and "all" is a reserved word that can't be used as a collection URL.

---

### 2. Set Product Filter Conditions { #operate-smart-collections-rules }

The core of a conditionalized collection is its "product rules". A rule has three parts: **filter field**, **condition**, and **value**, for example: Product price → Less than →
1,000. When you set multiple rules, the system decides whether to include products based on the combination you choose.


1. **Switch to the "Product" tab:** At the top of the collection settings page, click the **Product** tab.
2. **Choose how to combine conditions:** In the **Product Rules** section, under **Filter Results**, select **Match all conditions** or **Match any condition**.
3. **Add a rule:** Click **Create a new product rule**, and the system adds a new rule row.
4. **Set up a rule:** In the row, select a **filter field**, then a **condition**, and enter a **value**. For the available fields and conditions, see the [filter fields reference](../references/smart-collections-rule-columns.md#reference-smart-collections-columns){ title="Conditionalized Collection Filter Fields Reference" data-preview } and
[filter conditions reference](../references/smart-collections-rule-relations.md#reference-smart-collections-relations){ title="Conditionalized Collection Filter Conditions Reference" data-preview }.
5. **Add or remove rules:** Repeat the previous step to add more rules. To remove a rule, click the delete icon on the right of the row.
6. **Save the rules:** Click **Save** below the "Product Rules" section, and the system immediately recalculates the matching products based on the rules.

![Set filter conditions](../../../assets/images/ec-smart-collections-rules.en.png)

!!! info "How Rules Combine"

    * **Within a single rule**: Always a single comparison of "filter field + condition + value".
    * **Between multiple rules**: Decided by "Filter Results". Select **Match all conditions** to require products to match **all** rules **at the same time**, or **Match any condition** to include products that **match any one** rule.
    * A collection can use only one of "Match all conditions" or "Match any condition"; you can't mix logic rule by rule.

    !!! tip "Tip"
        If you choose a numeric field (product price, compare-at price, or inventory in stock), enter a number as the value. These fields can only be used with "equals", "greater than", and "less than".

---

### 3. Review Matching Products and Set the Sort Order { #operate-smart-collections-sort }

1. **Review matching products:** After you save the rules, **Matching Products** below lists the products that currently match, including product name, price, product type, and vendor, so you can confirm the conditions are correct.
2. **Choose a sort order:** In the sort drop-down menu, choose the order of products on the storefront collection page, such as "Price: High to Low" or "Best Selling". For all options, see the
[product sort order reference](../references/smart-collections-sort-order.md#reference-smart-collections-sort){ title="Conditionalized Collection Product Sort Order Reference" data-preview }.
3. **Manual sorting (optional):** If you choose "Manual", drag product rows to change their order.

![Review product sorting](../../../assets/images/ec-smart-collections-sort.en.png)

!!! note "Notes"
    Products in a conditionalized collection are dynamic. Whenever a product's data changes so that it matches or no longer matches the rules, the system adds or removes it automatically, so you don't need to maintain the members manually.

---

### 4. Set up SEO and Publish the Collection { #operate-smart-collections-publish }

1. **Fill in SEO settings (optional):** Return to the **Settings** tab and fill in the page title, page description, and page keywords in **SEO Setting** below to help search engines index the collection page.
2. **Publish the collection:** Return to the "Conditionalized Collections" list and switch the collection's status to **Published**. When set to **Unpublished**, the collection isn't shown on the storefront.

![SEO and publishing settings](../../../assets/images/ec-smart-collections-publish.en.png)

!!! note "Notes"
    The SEO settings section appears only **after the collection is created and saved**. It isn't shown while you're adding a new collection.

---

### 5. Multi-Language Translation Settings { #operate-smart-collections-multi-language }

!!! plan "Plan / Activation Requirements"
    This feature requires the multi-language store feature. Without it, there's no language menu next to the title on the collection edit page. For supported languages, see the [Multi-Language Supported Languages Reference](../references/multi-language-supported.md#reference-multi-language){ title="Multi-Language Supported Languages Reference" data-preview }.

If your store has multi-language enabled, you can provide a version of each conditionalized collection's **collection name** and **collection description** in each language so customers see the matching translation on the storefront.

1. **Open the collection to translate:** Click the collection in the "Conditionalized Collections" list to edit it. Note that the language menu appears only for collections **already created**; you can't switch languages while adding a new collection.
2. **Switch languages:** Click the **"Select Language"** drop-down menu next to the title on the collection edit page and switch to the language to translate.

    ![Switch languages](../../../assets/images/ec-smart-collections-lang-switch.en.png)

3. **Enter content in that language:** After switching, the **"Collection Name"** and **"Collection Description"** fields show the current language. Enter the translation for that language. Editing works the same way as in
[Create a Conditionalized Collection and Fill In Basic Details](#operate-smart-collections-create).

    ![Multi-language input](../../../assets/images/ec-smart-collections-lang-input.en.png)

4. **Save**: Click **Save** to save that language version, then switch to the next language and repeat.

!!! note "Notes"
    * Only the **collection name** and **collection description** can be translated per language. The **collection URL** and **SEO Setting** are shared across the site and don't vary by language.
    * Switching languages reloads the content for that language. Save your current changes before switching so you don't lose unsaved content.

---

## Important Rules and Limits { #specs-smart-collections }

* **Conditions take effect immediately**: Once rules are saved, the system immediately recalculates the matching products, and later product data changes update the collection automatically.
* **Collection URLs are unique and have a reserved word**: Collection URLs can't repeat within a store, and "all" can't be used as a collection URL.
* **Numeric and text conditions use different operators**: Numeric fields (product price, compare-at price, inventory in stock) can only use "equals", "greater than", and "less than". Only text fields have "contains", "does not contain", "starts with", and "ends with".
* **Limited multi-language translation scope**: Only the collection name and collection description can be translated. URLs and SEO don't vary by language.
* **Shown on the storefront only after publishing**: The collection must be set to "Published" for customers to see it.

---

## Next Steps { #next-steps-smart-collections }

<div class="grid cards" markdown>

<!-- - :lucide-package:{ .lg }  
  [__Check Product Data__](../products/index.md)  
  Make sure product names, types, vendors, tags, and prices are complete so conditionalized collections match correctly. -->

- :lucide-layout-template:{ .lg }  
  [__Set Up Menus and the Navigation Bar__](../../website-appearance/navigation/setup-menus-navigation.md){ title="Set Up Menus and the Navigation Bar" }  
  Add your conditionalized collections to the storefront menu or navigation bar so customers can browse them.

- :lucide-languages:{ .lg }  
  [__View Supported Languages__](../references/multi-language-supported.md){ title="Multi-Language Supported Languages Reference" }  
  Check the list of languages available for multi-language translation.

</div>

---

## FAQ { #faq-smart-collections }

??? quote "Why can't I find the language menu when adding a collection?"
    [](){ #faq-smart-collections-language-selector-missing }
    The language menu appears only when both of these are true:

    * Your store has the multi-language store feature enabled.
    * The collection has been **created and saved** (it doesn't appear while you're adding a new collection).

    If both are true and you still don't see it, contact your CYBERBIZ sales representative to confirm multi-language is enabled.

??? quote "Why do products in the collection increase or decrease on their own?"
    [](){ #faq-smart-collections-auto-update }
    This is normal for conditionalized collections. The system **automatically** adds products that match your rules and removes those that don't. When product data such as price, inventory, or tags changes, the collection members update accordingly, so you don't need to maintain them manually.

??? quote "I set conditions, but no products match?"
    [](){ #faq-smart-collections-no-match }
    Check the following in order:

    * Whether you chose the wrong combination: With multiple rules, "Match all conditions" requires **all** rules to be met **at the same time**. Too many conditions can leave no matching products, so try "Match any condition" instead.
    * Whether the values are correct: Numeric fields need numbers. For text fields, use the same wording as the product data.
    * Whether the product fields themselves (type, vendor, tags, and so on) are actually filled in.

??? quote "If I translate the collection name, does the storefront URL change?"
    [](){ #faq-smart-collections-url-not-translated }
    No. The **collection URL** and **SEO Setting** are shared across the site and don't change by language. Switching languages applies only the translated collection name and collection description.

??? quote "What's the difference between 'Conditionalized Collections' and 'Customized Collections'?"
    [](){ #faq-smart-collections-vs-custom }
    **Conditionalized Collections** use conditions so the system filters products automatically, while **customized collections** have products picked manually one by one. The former suits collections that keep changing (such as "Under NT$1,000"), and the latter suits collections whose members need precise control (such as campaign picks).

??? quote "Can I manually add or remove products in a conditionalized collection?"
    [](){ #faq-smart-collections-manual-add-remove }
    No. The products in a conditionalized collection are **determined entirely by the filter rules**, so you can't manually add or remove individual products. To adjust products manually, use a **customized collection** instead.

??? quote "How often are products in a conditionalized collection updated?"
    [](){ #faq-smart-collections-update-frequency }
    Conditionalized collections update immediately or automatically when:

    - Product data (price, inventory, tags, and so on) changes
    - The collection's filter conditions are changed and saved

    The system re-matches product data and updates the collection, with no manual sync needed.

??? quote "Can conditionalized collections be used in multi-level categories?"
    [](){ #faq-smart-collections-multi-level }
    Yes. A conditionalized collection can serve as the **bottom-level collection source in multi-level categories**, used with main categories and subcategories to build a clear category structure.

??? quote "Can marketing campaigns be applied to conditionalized collections?"
    [](){ #faq-smart-collections-marketing }
    Yes. Conditionalized collections can be used for many marketing campaigns, for example:

    - Threshold discounts
    - Collection discounts
    - Limited-time single-product deals

    As long as a product matches the conditions and is included in the collection, the corresponding campaign rules apply automatically.

??? quote "Do conditionalized collections affect product sorting on the storefront?"
    [](){ #faq-smart-collections-sort-impact }
    Conditionalized collections only determine "**whether a product is included in the collection**", not the sort order. The display order of products on the storefront is controlled by:

    - The collection's **product sort order (automatic/manual)**
    - The sorting logic settings of the storefront page

---

## References { #reference-smart-collections }

* [Conditionalized Collection Filter Fields Reference](../references/smart-collections-rule-columns.md)
* [Conditionalized Collection Filter Conditions Reference](../references/smart-collections-rule-relations.md)
* [Conditionalized Collection Product Sort Order Reference](../references/smart-collections-sort-order.md)
* [Multi-Language Supported Languages Reference](../references/multi-language-supported.md)

