---
title: "Set up Customized Collections"
description: "Hand-pick products by campaign or theme to build a collection that serves as a storefront category page, menu link, or ad landing page."
created: 2026-01-08 00:00
last_modified: 2026-07-22 17:23
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
  - "next steps 整合串接: POS 前台選單設定 link"
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
  - 如何建立商品分類群組
  - 如何管理商品分類結構
  - 商品群組 SEO 優化
features:
  - 商品自訂分類
  - 分類群組排序
  - 分類群組 SEO 設定
  - 多國語系
prerequisites: []
related:
  - ec/products/categories-and-tags/smart-collections/
  - ec/products/categories-and-tags/secret-collection/
  - ec/website-appearance/theme-and-layout/storefront-collection-sorting/
  - ec/website-management/setup-multi-language-and-multi-currency/
tags:
  - Collections
  - "Customized Collections"
  - SEO
  - "Product Management"
  - "EC Admin"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 商品自訂分類
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=11167
  - https://www.cyberbiz.io/helpcenter/?p=9175
  - https://www.cyberbiz.io/helpcenter/?p=985
  - https://www.cyberbiz.io/support/?p=20142
  - https://www.cyberbiz.io/support/?p=31938
  - https://www.cyberbiz.io/support/?p=3330
  - https://www.cyberbiz.io/support/?p=43330
permalink: "https://help.cyberbiz.io/ec/products/categories-and-tags/custom-collections/"
comments: false
search:
  exclude: false
icon: lucide/folder-edit
hide: []
---

![Customized collections](../../../assets/images/ec-product-customized-collections.zh-tw.en.png){ title="Customized Product Collections: Products > Customized Collections" .hero-page }

## About Customized Collections { #intro-custom-collections }

"Customized Collections" let you build collections from a **hand-picked list of products** (for example, "Summer Sale", "New Arrivals", or "Holiday Gift Boxes"), each with its own storefront collection page URL. Unlike "Conditionalized Collections" (which **automatically include** products that match conditions such as product tags, product type, or price), the members of a customized collection are chosen entirely by you.

Each collection can have its own:

- Collection name and storefront URL
- Collection description (shown on the storefront collection page; supports images and formatting)
- Page title, description, and keywords (SEO meta tags)
- Sort order for products in the collection

## Page Overview { #overview-custom-collections }

!!! path "Admin Path: Products > Customized Collections"

The "Customized Collections" page is split into two columns:

| Section | Content |
| :-- | :-- |
| **Left column** | A search table of all your products. Filter and select products to add them to the currently selected collection. |
| **Right column** | A collection sort dropdown, the collection list (expandable), and the "Add a new collection" form at the bottom of the page. |


- Click a collection title in the list to select it and expand its details (collection name, URL, and the products in the collection).
- Click the green edit button next to a collection to switch to editing its description and SEO.

![Customized collections page](../../../assets/images/ec-products-custom-collections-page.en.png){ title="Customized Collections Page" }

## Prerequisites and Limits { #prerequisites-custom-collections }

- [x] **Collection limit by plan**: Depending on your plan, the total number of customized collections may be capped. If you reach the limit, the system blocks new collections and shows a message.
- [x] **Multi-language (optional)**: To show different collection names, descriptions, and SEO on storefronts in different languages, the multi-language feature must be enabled separately. Details in [Multi-language settings](#operate-custom-collections-multilingual).

## Steps { #operate-custom-collections }

### Add a Collection { #operate-custom-collections-create }

1. **Enter a collection name:** In the "Enter a new collection name" field at the bottom of the right column, enter the name of the collection to create.
2. **Create it:** Click **Add a new collection**. The system creates the collection immediately and adds it to the top of the list in the right column.

![Add a customized collection](../../../assets/images/EC-商品-自訂商品分類-新增群組.en.png){ title="Add a Customized Collection" }

!!! tip "The Add Form Has Only a Name Field"
    You only need a name to add a collection. The system generates the URL from the name, and you can change it to a more readable URL later in the collection settings.

---

### Edit the Collection Name, URL, and Product Sort Order { #operate-custom-collections-edit-basic }

1. **Expand the collection:** In the collection list in the right column, click the title of the collection to edit to expand and select it.
2. **Edit the fields:** When the collection is expanded, you'll see these fields:
    - **"Collection Name"**: The name shown on the storefront and in the admin.
    - **Collection URL**: The last part of the storefront collection page URL. For example, with `summer-sale`, the storefront URL is `your-shop.com/collections/summer-sale`.
    - **Listing Order**: Choose how products in the collection are sorted (manually or automatically).
3. **Changes save automatically:** The system saves your edits automatically. If the URL duplicates another collection's or has an invalid format, an error appears next to the field.

![Expand the collection menu](../../../assets/images/EC-商品-自訂商品分類-展開群組選單.en.png){ title="Expand the Collection Menu" }

---

### Add Products to a Collection { #operate-custom-collections-add-products }

1. **Expand the target collection:** In the collection list in the right column, click the collection to add products to, and make sure it's selected.
2. **Search for products:** In the product search table in the left column, enter a product name or number, or set filters, to find the products to add.
3. **Select and add:** Select the products to add (one or several at a time) and click the add button above the table. The selected products appear in the collection's product list in the right column.

![Add products to a collection](../../../assets/images/EC-商品-自訂商品分類-加入商品至群組.en.png){ title="Add Products to a Collection" }

!!! tip "A Product Can Be in Multiple Collections"
    A product can belong to any number of customized collections at once. For example, "Summer Sale" and "Best-Selling Tops" can both include the same shirt without affecting each other.

??? info "How to Filter Products"
    Click the **filter button :lucide-filter:** to open the filter panel and combine multiple conditions:

    - **Product Type**: Filter by product type. You can select multiple types.
    - **Product Vendor**: Filter by vendor. You can select multiple vendors.
    - **Tag**: Filter products that have the specified tags. You can select multiple tags.
    - **Shop**: The product source. Filter products by POS or storefront source.

    ??? example "Filter Logic and Example"
        The system filters using **AND across different categories (all must match) and OR within the same category (any can match)**.

        - **Example settings:**
          - **Product Type**: Stress-relief items, Piano
          - **Product Vendor**: Genben, YAMAHA
          - **Tag**: stress relief, piano
          - **Source**: Storefront

        - **Logic applied:**
          (type `Stress-relief items` or `Piano`) + (vendor `Genben` or `YAMAHA`) + (tag `stress relief` or `piano`) + (source: storefront)

        - **Result:**
          The system shows products that "match all four categories at the same time". For example, an **online store** product tagged **piano** from vendor **YAMAHA**.

---

### Remove Products from a Collection { #operate-custom-collections-remove-products }

1. **Expand the collection:** Click the title of the collection to edit, and make sure it's selected.
2. **Find the product row:** In the collection's product list in the right column, find the product to remove.
3. **Click remove:** Click the red **"X"** icon on the right of the product row, and the product is removed from the collection.

!!! warning "Removing a Product Doesn't Delete the Product"
    Removing a product from a collection only unlinks it from that collection. The product still exists, and its membership in other collections isn't affected.

---

### Reorder Products in a Collection { #operate-custom-collections-reorder-products }

The display order of products in a collection directly affects how the storefront collection page looks. Use the "Listing Order" field to switch between manual and automatic sorting.

#### Switch to Manual Sorting { #operate-custom-collections-reorder-products-manual }

1. With the collection expanded, change **Listing Order** to the manual sorting option.
2. After switching, each product in the collection's product list shows a drag handle and a position number field on the left.

---

#### Drag to Reorder { #operate-custom-collections-reorder-products-drag }

Hold the drag handle (four-way arrow icon) on the left of the product row, drag it up or down to the target position, and release.

---

#### Enter a Position Number { #operate-custom-collections-reorder-products-input }

Click the "#" position field of the product row, enter the target number, and press ++enter++ or click a blank area. The product moves to that position.

![Enter a product position number](../../../assets/images/EC-商品-自訂商品分類-商品排序-輸入序號.en.png){ title="Enter a Product Position Number" }

!!! info "Manual Dragging Isn't Available with Automatic Sorting"
    If "Listing Order" is set to an automatic option such as by name or by price, the drag handles and position fields don't appear, and products are sorted automatically by that rule.

---

### Edit the Collection Description <small>Storefront Collection Page Copy</small> { #operate-custom-collections-description }

The collection description appears below the title on the storefront collection page. Use it for brand stories, campaign rules, or campaign images and text.

1. **Enter edit mode:** In the collection list in the right column, click the **green edit (pencil)** button to the right of the collection title.
2. **Stay on the "Collection Description" tab:** This tab opens by default in edit mode.
3. **Write the description:** Use the rich text editor to write text, adjust styles, and insert images or hyperlinks.
4. **Save**: Click **Save**, and a "Collection description saved" message appears in the upper-right corner.
5. **Return to the collection list:** Click the **Return to collections list** button in the upper left to go back to the collection list.

![Edit the collection description](../../../assets/images/EC-商品-自訂商品分類-編輯群組-群組描述.en.png){ title="Edit the Collection Description" }

!!! warning "Save Before Switching Languages or Going Back"
    If you've changed the description without saving, switching languages or clicking "Return to collections list" shows the prompt "Unsaved data will be lost. Are you sure you want to continue?" Be sure to save before confirming.

??? tip "Set Up a Top Banner"
    On the **Collection Description** tab, you can use the editor to customize the pinned content at the top of the collection page:

    - **Media support**: Insert campaign images or YouTube videos as a top banner.
    - **Marketing copy**: Write sales copy for the collection to improve conversion.

    ![Top banner setup example](../../../assets/images/ec-商品-商品自訂分類-前台置頂橫幅設定.en.gif){ title="Top Banner Setup Example" }

---

### Set up SEO <small>Search Engine Optimization</small> { #operate-custom-collections-seo }

Each collection page can have its own SEO meta tags, which affect how the collection page appears in search engines such as Google.

1. **Enter edit mode:** Click the **green edit (pencil)** button to the right of the collection title.
2. **Switch to the "Meta Tag Settings" tab:** Use the tabs at the top.
3. **Fill in the three SEO fields:**
    - **"Page Title"**: The title shown at the top of a search result. We recommend 50–60 characters or fewer.
    - **"Page Description"**: The summary shown below a search result. We recommend 150 characters or fewer.
    - **"Page Keywords"**: A list of keywords for search engines. **This field isn't shown on the storefront or in the preview**.
4. **Check the preview:** The "Search Result Preview" section at the bottom of the page shows in real time how the page appears in Google search results.
5. **Save**: Click **Save**, and a "Settings saved" message appears in the upper-right corner.

![Edit meta tags](../../../assets/images/EC-商品-自訂商品分類-編輯群組-metatag.en.png){ title="Edit Meta Tags" }

!!! tip "The Collection URL Also Affects SEO"
    The URL shown in the SEO preview (`your-shop.com/collections/{handle}`) comes from the "Collection URL" in the collection settings. To improve the URL structure, change the URL to a more meaningful string in the collection edit area (not the Meta Tag tab).

---

### Publish or Hide a Collection { #operate-custom-collections-publish }

New collections are published by default. To take one down temporarily (for example, while a campaign is being prepared or when a seasonal collection is out of season), switch it to hidden.

1. **Find the collection:** Find the target collection in the collection list in the right column.
2. **Click the eye icon:** To the right of the collection title is an eye icon that shows the current publish status:
    - **Eye open** means the collection is **Published**: Click it to hide the collection.
    - **Eye closed** means the collection is **hidden**: Click it to publish the collection.
3. The change takes effect immediately; you don't need to save.

![Publish or hide a collection](../../../assets/images/EC-商品-自訂商品分類-群組公開狀態設定.en.png){ title="Publish or Hide a Collection" }

!!! warning "Hiding Isn't Deleting"
    A hidden collection keeps all its settings and products. It isn't shown on the storefront, but you can publish it again from the admin at any time.

---

### Preview a Collection <small>View on the Storefront</small> { #operate-custom-collections-browse }

1. **Click the "View collection" button:** In the collection list, click the **pink globe icon** to the right of the collection title.
2. The system opens the collection's storefront page in a new tab so you can check the product order, collection description, and overall look right away.

![View a collection](../../../assets/images/EC-商品-自訂商品分類-瀏覽群組.en.png){ title="View a Collection" }

---

### Delete a Collection { #operate-custom-collections-delete }

1. **Click the delete button:** In the collection list, click the **red X icon** to the right of the collection title.
2. **Confirm the deletion:** The system shows the confirmation "Are you sure you want to delete this collection?" Click confirm to delete it.

![Delete a collection](../../../assets/images/EC-商品-自訂商品分類-刪除群組.en.png){ title="Delete a Collection" }

!!! warning "Deletion Can't Be Undone"
    After you delete a collection, its settings and storefront URL stop working immediately and can't be restored. If external links, ads, or social posts point to the storefront URL, redirect that traffic first. **The products in the collection aren't deleted**; they just no longer belong to the collection.

---

### Sort the Collection List { #operate-custom-collections-sort-list }

A sort dropdown menu at the top of the right column changes the display order of the collection list:

| Option | Description |
| :-- | :-- |
| **by creation date: latest to earliest** | The most recently created collection is listed first (**Default**). |
| **by creation date: earliest to latest** | The earliest created collection is listed first. |
| **by alphabetical order: A-Z** | Collection names are sorted alphabetically. |
| **by alphabetical order: Z-A** | Collection names are sorted in reverse alphabetical order. |

This setting is remembered in your browser, so your last choice is kept the next time you open the page.

![Collection list sorting](../../../assets/images/EC-商品-自訂商品分類-群組列表排序.en.png){ title="Collection List Sorting" }

---

### Multi-Language Settings { #operate-custom-collections-multilingual }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案){ title="Icon Conventions" } | PLUS / Enterprise
{ .doc-badge }

!!! plan "Prerequisites"
    The multi-language feature **must be enabled separately on every plan**; contact your account manager. Once enabled, a **"Select Language"** dropdown menu appears in the upper-right corner of the page. Stores without it enabled don't see this menu and can't edit content in multiple languages.

#### Language Behavior of Each Field { #operate-custom-collections-multilingual-fields }

After you switch languages, the editable fields fall into two types:

- **Saved separately**: Saved per language.
- **Shared across languages**: Set once, and all languages use the same data.

| Field | Saved Separately? | Storefront Behavior When Not Filled In for That Language |
| :-- | :-- | :-- |
| Collection name | Separate | Shows the **default language** content automatically |
| Collection description | Separate | Shows the **default language** content automatically |
| Page title / page description / page keywords | Separate | **Blank**; the default language content isn't filled in automatically |
| Collection URL | Shared | All languages use the same URL |
| Added products | Shared | All languages show the same products |

!!! warning "The Three SEO Fields Don't Fall Back to Default Content"
    The collection name and description show the default language content when left blank, but **page title, page description, and page keywords (the three SEO fields) don't**. For collection pages in non-default languages to have complete SEO, switch to that language and **fill in each field** and save. Otherwise, that language's page will have empty SEO meta tags.

---

#### Edit Content in Another Language { #operate-custom-collections-multilingual-edit }

1. **Switch to the target language:** On the "Products/Customized Collections" page, select the language to edit in the **"Select Language"** dropdown menu in the upper-right corner. The system loads the content saved for that language.

    ![Multi-language menu](../../../assets/images/EC-商品-自訂分類-多國語系選單.en.png){ title="Multi-Language Menu" }

2. **Edit the collection name and description:**
    - **Collection name**: Follow the steps in [Edit the Collection Name, URL, and Product Sort Order](#operate-custom-collections-edit-basic) to change the name for that language (changes save automatically).
    - **Collection Description**: Follow the steps in [Edit the Collection Description](#operate-custom-collections-description) to open the edit page, enter the content for that language on the **Collection Description** tab, and click **Save**.
3. **Fill in the SEO meta tags:** Follow the steps in [Set Up SEO](#operate-custom-collections-seo) to fill in the information for that language, and click **Save**.
4. **Repeat for other languages:** Open the "Select Language" dropdown again, switch to the next language, and repeat steps 2–3 until every language you need to support is filled in.

!!! tip "Recommended Order"
    Fill in all fields in the default language (Traditional Chinese for most stores) first, then switch to other languages. That way, even if you forget the "Collection Name" or "Collection Description" in another language, the storefront shows the default language content instead of leaving it blank.

## Important Rules and Limits { #specs-custom-collections }

- **Collection limit depends on your plan**: Your plan limits the total number of customized collections you can create. Once you reach the limit, the system blocks new collections.
- **Collection URLs must be unique**: Each collection in a store must have a unique URL.
- **No system limit on products**: There's no hard limit on the number of products in a single collection.
- **Deleting a collection can't be undone**: A deleted collection can't be restored, and its storefront URL stops working at the same time.
- **Collection description and SEO are separate per language**: The collection name and description automatically **fall back** to the default language when left blank, but the three SEO fields don't. Details in [Multi-language settings](#operate-custom-collections-multilingual).

## Next Steps { #reference-custom-collections }

<div class="grid cards" markdown>

- :lucide-sparkles:{ .lg }  
  [**Conditionalized Collections**](smart-collections.md){ title="Set Up Conditionalized Collections" }  
  A collection type that adds products automatically by conditions, complementing the features in this article.

- :lucide-eye-off:{ .lg }  
  [**Secret Collections**](secret-collection.md){ title="Set Up a Secret Collection" }  
  Create a hidden product collection that only specific customers can buy from through an exclusive link.

- :lucide-arrow-up-down:{ .lg }  
  [**Set the Storefront Collection Order**](../../website-appearance/theme-and-layout/storefront-collection-sorting.md){ title="Set the Homepage Product Collection Order" }  
  Adjust the order of collections on the storefront homepage and set how many collections the homepage can show.

- :lucide-languages:{ .lg }  
  [**Enable Multi-Language**](../../website-management/setup-multi-language-and-multi-currency.md){ title="Set Up Multi-Language and Multi-Currency for Your Storefront" }  
  Enable the multi-language feature.

</div>

## FAQ { #faq-custom-collections }

??? quote "What's the difference between 'Customized Collections' and 'Conditionalized Collections'?"
    [](){ #faq-custom-collections-vs-smart }
    Both are product collections. They differ in how member products are determined:

    - **Customized Collections**: You **pick** the member products **manually**. Best for marketing themes, holiday campaigns, limited bundles, and other cases that need specific product picks.
    - **Conditionalized Collections**: Products matching the conditions you set (such as product tags, product type, or price range) are **added automatically**. New products are added automatically when they match.

??? quote "Can a product be added to multiple collections?"
    [](){ #faq-custom-collections-multi-group }
    Yes. A product can belong to any number of customized collections at once without affecting each other.

??? quote "Are products deleted when I delete a collection?"
    [](){ #faq-custom-collections-delete-products }
    No. Deleting a collection only removes the link between the collection and its products. The products still exist, and their membership in other collections isn't affected.

??? quote "Why does the system say I've reached the limit when I add a collection?"
    [](){ #faq-custom-collections-limit-reached }
    Your plan limits the total number of customized collections you can create. If you've reached the limit, delete collections you no longer use, or contact your account manager to upgrade your plan or buy more collections.

??? quote "Why can't I see the 'Select Language' dropdown in the upper-right corner?"
    [](){ #faq-custom-collections-no-language-selector }
    The multi-language feature **must be enabled separately on every plan**. The "Select Language" menu appears in the upper-right corner only after multi-language is enabled, and then you can edit in multiple languages.

??? quote "I filled in SEO after switching languages. Why is the storefront still blank?"
    [](){ #faq-custom-collections-seo-empty }
    The three SEO fields (page title, page description, page keywords) **don't** fall back to the default language. Make sure each SEO field for that language is filled in and saved. Details in [Multi-language settings](#operate-custom-collections-multilingual).

??? quote "Can a collection URL use Chinese characters?"
    [](){ #faq-custom-collections-handle-chinese }
    The system doesn't restrict characters, but we recommend lowercase English letters, numbers, and hyphens (for example, `summer-sale`) to make sharing and SEO easier and to avoid encoded, garbled text in the browser address bar.


