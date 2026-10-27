---
title: "SEO Settings and Optimization Guide"
description: "A complete guide to SEO settings, including image ALT attributes, SEO for product and category pages, site-wide meta tags, and how to submit a sitemap and set up 301 redirects."
created: "2026-03-18 16:19"
last_modified: 2026-06-26 14:53
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
  - 管理中心
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - SEO_優化
  - 設定_Meta_Tag
  - 圖片_ALT_屬性
  - 商品頁_SEO
features:
  - SEO
  - "Meta Tag"
  - ALT 屬性
  - Sitemap
  - 301 轉址
prerequisites: []
related:
  - ec/website-management/setup-store-basic-info/
  - ec/website-appearance/site-settings/setup-site-title-seo/
  - ec/website-appearance/pages-and-content/blog-management-publishing-guide/
  - ec/website-appearance/pages-and-content/custom-pages/
  - ec/website-management/seo/submit-sitemap-to-gsc/
  - ec/website-management/seo/setup-301-redirects/
tags:
  - SEO
  - Meta Tag
  - "Search Engine Optimization"
  - "Search Ranking"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
  - 商品 > 商品自訂分類
  - 管理中心 > 一般設定
  - 網站外觀 > 套版主題管理
layouts: []
wp_url:
  - "https://www.cyberbiz.io/helpcenter/?p=3512"
  - "https://www.cyberbiz.io/support/?p=16944"
permalink: "https://help.cyberbiz.io/ec/website-management/seo/seo-guide/"
comments: false
search:
  exclude: false
icon: "lucide/search"
hide: []
---

## About SEO { #intro-seo-guide }

SEO (search engine optimization) is the process of improving your website's organic (non-paid) ranking. It makes it easier for search engines to find your website and rank it higher, which increases page visibility, traffic, and conversions.

SEO optimization in the CYBERBIZ system covers the **homepage, product pages, product collections, images, blog, and custom pages**.

!!! warning "Notes"

    *   SEO settings need some **waiting time** to take effect (depending on Google's schedule), so finish them as early as possible.
    *   For multi-language stores, you can set separate SEO content for each language.

## Image SEO Settings <small>ALT attribute</small> { #operate-seo-guide-images }

Adding ALT text to images improves the browsing experience. The text replaces the image when the image can't be displayed, and it helps search engines understand what the image shows.

*   **Path**: Log in to the CYBERBIZ admin panel and go to **Products** > **All Products** > click a product > **Product Description**.
- **How to set it**: In the **Product Introduction**, **Specifications**, or **Delivery Type** editor, right-click the image, select **Image Properties**, and enter a phrase that describes the image in the **Alternative Text** field.

![](../../../assets/images/ec-商品-商品編輯頁-商品描述-影響屬性編輯.en.gif)

## Product Page SEO Settings { #operate-seo-guide-product }

*   **Path**: Log in to the admin panel, go to **Products** > **All Products** > click a product > **Settings**, and scroll down to **SEO Setting**.
*   **What you can set**: You can edit the page title and description. Keep them to **225 characters** or fewer.

![](../../../assets/images/ec-商品-商品編輯頁-設定-seo設定.en.gif)

## Product Collection (Category Page) SEO Settings { #operate-seo-guide-collection }

This makes specific product categories (such as customized or conditionalized collections) easier to find in search results.

*   **Path**: Go to **Products** > **Customized Collections** (or **Conditionalized Collections**) > select a collection and click **Edit Collection**.
*   **How to set it**: Click **Meta Tag Setting** and fill in the title, short description, and keywords.

![](../../../assets/images/ec-商品-自訂分類-群組編輯頁-metatag設定.en.gif)

## Site-Wide SEO Settings { #operate-seo-guide-site }

These include the title and keywords for your whole website.


- **Name of website**: Go to **Website Management** > **General** to [set the website name](../../website-management/setup-store-basic-info.md#operate-general-preferences-company-info){ title="Set Up Basic Website Information" } (up to 15 Chinese characters or 30 English characters).
- **Meta Tag Setting**: Includes **Title**, **Description**, and **Keywords**.
    *   **Standard themes**: Go to **Website Appearance** > **Theme Setting** > **Website Settings** > **Company Brand**. Learn [how to set the website title in a standard theme](../../website-appearance/site-settings/setup-site-title-seo.md#operate-site-title-default){ title="Set the Website Title in a Standard Theme" }.

        ![](../../../assets/images/ec-網站外觀-套版主題-網站設定-網站簡述與關鍵字-一般版型.en.png)

    *   **Drag-and-drop themes**: Go to **Website Appearance** > **Theme Setting** > **Website Settings** > **Global Settings**. Learn [how to set the website title in a drag-and-drop theme](../../website-appearance/site-settings/setup-site-title-seo.md#operate-site-title-theme){ title="Set the Website Title in a Drag-and-Drop Theme" }.

!!! note "Further Reading"
    For detailed settings for the website title and SEO, see [Set Up the Website Title and SEO](../../website-appearance/site-settings/setup-site-title-seo.md){ title="Set Up the Website Title and SEO" }, or go directly to [search engine results page (SERP) settings](../../website-appearance/site-settings/setup-site-title-seo.md#operate-site-title-serp){ title="Search Engine Results Page (SERP)" }.

## Blog and Other Custom Page SEO { #operate-seo-guide-pages }

<div class="grid cards" markdown>

- :lucide-newspaper:{ .lg }
  [__Blog__](../../website-appearance/pages-and-content/blog-management-publishing-guide.md#meta-tags){ title="Blog Management and Publishing Guide" }
  Set meta tags for blog topics and individual articles.

- :lucide-files:{ .lg }
  [__Other Pages__](../../website-appearance/pages-and-content/custom-pages.md#operate-custom-pages-create){ title="Set Up and Manage Custom Pages" }
  For pages such as About Us or custom event pages, edit the page description and title in **Customized Pages Management**.

</div>

## Sitemap Submission and Redirect Maintenance { #next-steps-seo-guide }


<div class="grid cards" markdown>

- :lucide-map:{ .lg }
  [__Sitemap__](submit-sitemap-to-gsc.md){ title="Submit a Sitemap to Google Search Console" }
  The system generates a sitemap automatically. Just submit its URL to GSC to get your pages indexed faster.

- :lucide-signpost:{ .lg }
  [__301 Redirects__](setup-301-redirects.md){ title="Set Up 301 Redirects" }
  When the URL of a once-popular page stops working or changes, set up a 301 redirect to send traffic to the new URL and keep your SEO ranking from dropping.

</div>


## FAQ { #faq-seo-guide }

??? quote "How long does it take to see results after setting up SEO?"

    SEO results take time. It usually takes **2–4 weeks** to see changes in search results, because Google needs time to recrawl and index your pages.

??? quote "Can I set different meta tags for each product?"

    Yes. In the **SEO Setting** section of the product edit page, you can set a unique title, description, and keywords for each product.

??? quote "When do I need a 301 redirect?"

    When you delete or change the URL of a product page or category page, set up a 301 redirect from the old URL to the new one to keep the SEO ranking it has built up.
