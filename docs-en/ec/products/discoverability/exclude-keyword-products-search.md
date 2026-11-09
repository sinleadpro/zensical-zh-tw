---
title: "Exclude Products with Specific Keywords from Search Results"
description: "Edit the Liquid template code to exclude products with specific keywords from online store search results."
created: 2026-02-25 00:00
last_modified: 2026-06-30 11:26
lang: en-US
permalink: "https://help.cyberbiz.io/ec/products/discoverability/exclude-keyword-products-search/"
type: guide
author: Jase
reviewers: []
notes:
  - verify faq tag
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
  - 網站外觀
sites:
  - TW
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
audiences:
  - developer
difficulty: advanced
intents:
  - 排除特定關鍵字商品
features:
  - 搜尋排除關鍵字
  - Liquid 語法修改
  - 商品名稱設定
prerequisites: []
related:
  - ec/website-appearance/code-customization/restore-code-theme-editor/
  - ec/products/categories-and-tags/secret-collection/
tags: 
  - "Search Exclusion"
  - "Keyword Exclusion"
  - Liquid
  - "Code Editing"
  - "Hidden Products"
  - SEO
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 套版主題管理
  - 商品 > 所有商品
layouts:
  - classic
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3852
search:
  exclude: false
icon: lucide/search-x
hide:
comments: false
---

![Search keyword exclusion settings](../../../assets/images/ec-網站外觀-樣板編輯器-search-liquid.en.png){ title="Search Keyword Exclusion Settings" .hero-page }

## About Excluding Products with Specific Keywords from Search { #intro-exclude-kw }

By editing the code, you can exclude products that contain specific keywords (for example, purchase-with-purchase products, group-buy exclusives, and secret store products) from storefront search results.

The steps to exclude specific keywords from search are as follows:

## Applicable Themes and Limits { #prerequisites-exclude-kw }

- **Theme limit**: This tutorial **only applies to the default theme (standard theme)**. It does not work with drag-and-drop themes.
- **Responsibility**: CYBERBIZ provides code editing access but does not offer syntax tutorials or coding services. If an edit goes wrong, use the restore feature to roll back to an earlier version.

## Steps { #operate-exclude-kw }

1. **Go to the editor**: Log in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > CSS/HTML Editor**.
2. **Find the file**: In the editor, search for and open the **`search.liquid`** file.
3. **Edit the code**:
    - Find this line in the file: `{% assign product_results = search.products %}`.
    - Change it to: `{% assign product_results = search.products | without: "title", "Keyword1" | without: "title", "Keyword2" %}`.
    - **How it works**: Any product whose name contains the words you set as "Keyword1" or "Keyword2" (such as VIP Exclusive) does not appear in storefront search results.

	```liquid title="search.liquid" hl_lines="6"
	<div id="search">
	  <!-- search container start -->
	  <div class="container">
	
	  <!-- resolve search.results -->
	  {% assign product_results = ssearch.products | without: 'title', 'VIP Exclusive' %}
	  {% assign article_results = search.results | related: 'item_type', 'Article' %}
	  {% assign results_sizes = product_results.size | plus: article_results.size %}
	  {% assign show_periodic_label = false %}
	  {% if settings.display_periodic_order_label and shop.plugins.periodic_order %}
	    {% assign show_periodic_label = true %}
	  {% endif %}
	  {% if search.performed and results_sizes != 0 %}
	  <!-- has search results -->
	```

4. **Set the product names**: Go back to **Products > All Products** and **rename** the products you want to exclude from search by adding the keyword you set in the code to the front of the product name (such as VIP Exclusive-Earth).

	![Product name keyword setting](../../../assets/images/ec-商品-商品名稱-秘密群組關鍵字.en.png){ title="Product Name Keyword Setting" }

5. **Test the result**: After you finish and save the settings, search for the keyword products with the magnifier on your storefront to confirm that they are hidden.

## Notes { #prerequisites-exclude-kw-notes }

- **Exact match**: Make sure the keyword in the code is exactly the same as the keyword in the product name.
- **Recovery**: If the page breaks after an edit, click **View a previous version** in the editor to [roll back to an earlier version](../../website-appearance/code-customization/restore-code-theme-editor.md#operate-restore-theme){ title="Restore Web Page Code with the Template Editor" }.


## Next Steps { #next-steps-exclude-kw }

<div class="grid cards" markdown>

- :lucide-eye-off:{ .lg }  
  [__Secret Collection__](../categories-and-tags/secret-collection.md){ title="Set Up a Secret Collection" }  
  Use it with a secret collection so specific customer groups can buy through a direct link, while regular shoppers cannot find the products with site search.

- :lucide-rotate-ccw:{ .lg }  
  [__Restore Web Page Code with the Template Editor__](../../website-appearance/code-customization/restore-code-theme-editor.md){ title="Restore Web Page Code with the Template Editor" }  
  Restore the template to a specific point in time from its version history.

</div>

## FAQ { #faq-exclude-kw }

??? quote "How do I write the code to exclude several different keywords?"
    Use the `| without: "title", "Keyword"` syntax several times in a row. For example, to exclude products containing both "Add-on" and "Test", use the following syntax:

    ``` liquid
    {% assign product_results = search.products | without: "title", "Add-on" | without: "title", "Test" %}
    ```

??? quote "Why can I still see the product in search results after editing the code?"
	Check the following three points:
	
	 1. **Exact keyword match**: The string in the code (such as "VIP") must be exactly the same as the words in the product name, including full-width or half-width characters and letter case.
	 2. **Variable override**: Make sure the part of `search.liquid` that renders the product list below uses the `product_results` variable, not the original `search.products`.
	 3. **Cache delay**: Browser or system cache can sometimes delay updates. Try testing again in an incognito window.

??? quote "Does excluding keywords affect crawling by search engines such as Google?"
    **No.** This edit only affects the CYBERBIZ site search logic (the Liquid rendering layer). External search engines such as Google still index your product pages. To fully prevent Google from crawling the page, set a `noindex` tag separately.

??? quote "Can I use product tags instead to exclude products?"
    Yes. To exclude by tag, change `"title"` in the syntax to `"tags"`. For example:
    ``` liquid
    {% assign product_results = search.products | without: "tags", "Hidden" %}
    ```
    Then any product whose tags contain `Hidden` does not appear in search results, and the product title shown on the storefront stays clean.

??? quote "Does this setting affect the 'All Products' category page?"
	**No.** This edit only applies to `search.liquid` (the search results page). If you also want to hide these products on "All Products" or specific category pages, edit the matching logic in `collection.liquid` as well.
