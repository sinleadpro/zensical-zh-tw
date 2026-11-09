---
title: "Register and Verify Google Search Console"
description: "Register and verify website ownership in Google Search Console to monitor your site's search performance."
created: 2026-03-20 14:28
last_modified: 2026-07-03 11:44
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
  - 第三方整合
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
  - Google Search Console 驗證
  - 網站擁有權驗證
  - GSC 設定
features:
  - Google Search Console
  - GSC 驗證
  - HTML 標記驗證
prerequisites: []
related:
  - ec/website-management/seo/submit-sitemap-to-gsc/
tags:
  - GSC
  - SEO
  - "Search Engine Optimization"
acoiv: integration
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > Google Search Console 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3375
  - https://www.cyberbiz.io/support/?p=15362
permalink: "https://help.cyberbiz.io/ec/integrations/google/setup-google-search-console/"
comments: false
search:
  exclude: false
icon: lucide/search-code
hide: []
---

![Google Search Console registration and verification](../../../assets/images/ec-第三方整合-google-gsc.en.png){ title="Google Search Console registration and verification" .hero-page }

## Why Use GSC { #intro-search-console }

**Google Search Console (GSC)** is a free website management tool from Google. After verification, it can help you:

- **Monitor search performance**: View your site's clicks, impressions, and average rankings in Google Search.
- **Submit sitemaps**: Proactively tell Google about your site structure to speed up indexing.
- **Diagnose SEO issues**: Detect crawl errors, mobile usability issues, and page indexing status.
- **Optimize site performance**: Adjust your content strategy based on search data to increase organic traffic.

!!! info "For more information about Google Search Console, see [official documentation :lucide-external-link:](https://support.google.com/webmasters/answer/9128668?hl=zh-Hant)."

## Prerequisites and Limitations { #prerequisites-search-console }

- [x] **Consistent account**: Make sure the account you use to sign in to Google Search Console is the same as your Google Analytics (GA) account, and that you have admin permissions for it.
- [x] **Domain settings**: Set your primary domain in the storefront admin to "Own domain" and turn on "Always redirect" to keep search engine indexing consistent.

## Registration and Verification Steps { #operate-search-console }

1. **Go to GSC**: Go to the [Google Search Console :lucide-external-link:](https://search.google.com/search-console/) page and click **Get Started**.
2. **Enter URL**: On the property type selection screen, click **URL prefix** on the right and enter your storefront URL (must include https://).
3. **Select a verification method**: Select **HTML tag** as the verification method. The system generates a code snippet. Click the button next to it to copy the code.

    ![Copy HTML tag code](../../../assets/images/ec-第三方整合-google-gschtml標記複製.en.gif){ title="Copy HTML tag code" }

4. **Add the code to the CYBERBIZ admin**:
    * Go to the admin path: **Website Appearance** > **Theme Management** > Actions **CSS/HTML Editor** > Click the left **`theme.liquid`** file.
    * Paste the HTML tag code you copied just before the **`</head>`** tag in the file content, then save.

    ![Paste HTML tag code](../../../assets/images/ec-第三方整合-google-gschtml標記貼上.en.png){ title="Paste HTML tag code" }

5. **Complete verification**: Return to the Google Search Console page and click **Verify**. After verification, a pop-up titled "Ownership verified" appears. Click "Go to property" to start viewing your data.

## Next Steps { #next-steps-search-console }

<div class="grid cards" markdown>

- :lucide-map:{ .lg }   
  [__Submit Sitemap__](../../website-management/seo/submit-sitemap-to-gsc.md){ title="Submit your Sitemap to Google Search Console" }    
  After registration and verification, the most important next step is to submit your Sitemap.

</div>

## FAQ { #faq-search-console }

??? quote "Why verify Google Search Console?"

    Once GSC is verified, you can use the tool to monitor your site's performance in Google Search, submit your Sitemap, and review SEO data such as clicks and impressions. Verification is the foundation for running and optimizing your site.

??? quote "Can I use other verification methods?"

    Yes. GSC supports several verification methods, such as domain provider and DNS record verification. This guide uses **HTML tag** as the example because it is the most straightforward and widely applicable option.

??? quote "What if verification fails?"

    Confirm the following:

    - [x] The HTML tag is pasted before the `</head>` tag
    - [x] The code has been saved
    - [x] The website page has been reloaded

    If verification still fails, clear your browser cache and try again.
