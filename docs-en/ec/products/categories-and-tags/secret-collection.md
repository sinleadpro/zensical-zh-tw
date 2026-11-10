---
title: "Set up a Secret Collection"
description: "Create a hidden collection and offer it to specific customers through an exclusive link."
created: 2026-01-08 00:00
last_modified: 2026-07-22 17:37
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
  - merge 商品排除搜尋
  - add 推薦人分潤 doc link
  - add batch edit 關閉商品搜尋
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
  - 如何設定秘密商品群組
  - 隱藏商品群組設定
features:
  - 商品自訂分類
  - 商品排除搜尋
prerequisites: []
related:
  - ec/profit-sharing/referrer-profit-sharing/
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/discoverability/exclude-keyword-products-search/
  - ec/website-appearance/code-customization/restore-code-theme-editor/
tags:
  - "Secret Collection"
  - "Hidden Products"
  - "Exclusive Link"
  - "Marketing Campaigns"
  - "Product Categories"
  - SEO
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 商品自訂分類
  - 商品 > 所有商品
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3872
  - https://www.cyberbiz.io/support/?p=20280
permalink: "https://help.cyberbiz.io/ec/products/categories-and-tags/secret-collection/"
comments: false
search:
  exclude: false
icon: lucide/eye-off
hide: []
---

![Secret collection](../../../assets/images/ec-商品-商品自訂分類-秘密群組.en.png){ title="Secret Collection" .hero-page }

## About Secret Collections { #intro-secret-collection }

A **secret collection** (also called a secret store) is mainly used to give specific groups of customers (such as distributors, group-buy organizers, and staff) a link that is not public so they can make purchases.

!!! example "Use Cases"

    Secret collections are often used with the Referral Program feature as a shopping referral tool for KOLs or specific group-buy organizers:

    - **Exclusive referral link:** Add a referrer code to the secret collection URL (for example, `www.yourshop.com/collections/secret-collection?rcode=RAYTEST`) and share it with specific people.
    - **Purchases by specific users:** Only users with the full link can open the page and order. Regular customers cannot find the section through search.

    <div class="grid cards" markdown>

    - :lucide-hand-coins:{ .lg } [__Referral Program__](../../profit-sharing/referrer-profit-sharing.md){ title="Referral Program" }

    </div>

## Steps { #operate-secret-collection }

To set up a secret collection, first create a customized collection, and then hide the products in it and turn off search for them. The details are explained in two stages below.

### Set up a Secret Collection <small>Secret Store</small> { #operate-secret-collection-setup }

1. **Create a product collection:** In the admin, go to **Products > Customized Collections**.
2. **Add a new collection:** Click "Add a new collection" in the lower-right corner and enter a custom name (for example, VIP Secret Store).
3. **Add products:** In the product list on the left, select the products you want to sell and add them to the collection.

![Create a secret collection](../../../assets/images/ec-商品-建立秘密群組.en.gif){ title="Create a Secret Collection" }

<div class="grid cards" markdown>

- :lucide-folder-edit:{ .lg } [__Set Up Customized Collections__](custom-collections.md){ title="Set Up Customized Collections" }

</div>

---

### Hide Products and Keep Them Out of Search { #operate-secret-collection-hide }

To make sure regular customers cannot find the products in the secret collection on your storefront, complete the following settings:

- [x] **Turn off site search for the product:**
    - Go to **Products > All Products** and open the product's **Product Information** tab, or click a product name in the secret collection to open the page.
    - Set "**Product search**" to **Off**.
    - **Effect:** The product cannot be found in the storefront search box, does not appear on the storefront "All Products (Collection/All)" page, and is not indexed by Google.

	![Turn off product search](../../../assets/images/ec-商品-秘密群組-關閉商品搜尋功能.en.gif){ title="Turn Off Product Search" }

- [x] **Navigation bar rule:** After you create a secret store, **do not** add a link to this collection in your storefront navigation bar or menus, so regular users do not open it by mistake.
- [x] **Exclude specific keywords (advanced):** By editing the `search.liquid` code, you can keep [products containing specific words out of search results](../discoverability/exclude-keyword-products-search.md){ title="Exclude Products with Specific Keywords from Search Results" }  .

## Notes and Recommendations { #prerequisites-secret-collection }

- **External search engine risk:** Even with site search turned off for the products, the secret collection page may still be indexed by Google.
- **SEO exclusion:** To keep the page out of Google search results completely, exclude the secret collection page in **Google Search Console** to block external search.
- **Recovery:** If something goes wrong while you edit the code, use the editor's "View a previous version" feature to [roll back to the default version](../../website-appearance/code-customization/restore-code-theme-editor.md){ title="Restore Web Page Code with the Template Editor" }  .


## Related Tasks { #next-steps-secret-collection }

<div class="grid cards" markdown>

- :lucide-folder-edit:{ .lg }  
  [__Customized Collections__](custom-collections.md){ title="Set Up Customized Collections" }  
  Customize product collections.

</div>


## FAQ { #faq-secret-collection }

??? quote "Are products automatically excluded from search after I create a secret collection?"
    No. A secret collection only groups products. You still need to open each product's edit page and set "Product search" to `OFF` to exclude it from site search.

??? quote "Can regular customers buy products in a secret collection?"
    If a regular customer gets the direct link to a secret collection and the products in it are not set to "turn off site search", they can still visit the page and buy. To keep the collection exclusive, set its products to be excluded from search.
