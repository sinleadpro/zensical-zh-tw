---
title: "Remove Specific Pages or Subdirectories from Google Search Results"
description: "Use the Google Search Console Remove URLs tool to exclude specific pages or subdirectories from appearing in Google Search results."
created: 2026-03-24 17:04
last_modified: 2026-07-02 17:02
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
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 移除 Google 搜尋結果
  - 排除網頁索引
features:
  - Google Search Console
  - 移除網址工具
prerequisites:
  - ec/integrations/google/setup-google-search-console/
related:
  - ec/integrations/google/setup-google-search-console/
  - ec/products/discoverability/product-search-visibility/
tags:
  - "Google Search Console"
  - "Remove URLs"
  - "Search Results"
  - SEO
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > Google > 移除搜尋結果
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12105
  - https://www.cyberbiz.io/support/?p=25441
permalink: "https://help.cyberbiz.io/ec/integrations/google/remove-urls-from-google-search/"
comments: false
search:
  exclude: false
icon: lucide/search-x
hide: []
---

![GSC Remove URLs](../../../assets/images/ec-第三方整合-google-gsc移除網址.en.png){ .hero-page }

## Excluding Pages from Google Search Results

If your brand website shows subdirectory pages in Google Search results that you do not want to expose, such as old campaign pages, content not yet ready for the public, or structural pages that do not help SEO, you can use the tool that Google provides. To learn more, see the [Google official guide :lucide-external-link:](https://support.google.com/webmasters/answer/9689846).

## Understanding Subdirectories in Google Search Results

Subdirectories in Google Search results are extension pages of your site that appear below a search result. Google usually identifies and crawls these pages automatically. They may include common paths such as `/products`, `/faq`, `/campaign`, `/showcase`, and so on.

![](../../../assets/images/ec-第三方整合-google-google搜尋子目錄.en.png)

## Steps

### Use the Google Remove URLs Tool

Site owners can use the "Remove URLs" tool in **Google Search Console (GSC)** to temporarily exclude specific pages or subdirectories from appearing in search results.

1.  **Sign in to GSC**: Sign in to [Google Search Console :lucide-external-link:](https://search.google.com/search-console/).
2.  **Select a property**: Select a site property that you manage (if it is not yet verified, first complete [Google Search Console registration and verification](setup-google-search-console.md){ title="Register and verify Google Search Console" }).
3.  **Go to the removal feature**: In the sidebar, click **"Indexing" ** > ** "Removals"**.
4.  **Create a new request**: On the **Temporary removals** tab, click **New request**.
5.  **Enter the URL and type**:
    *   Enter the URL path you want to remove.
    *   Select either **Remove this URL only** or **Remove all URLs with this prefix**.
6.  **Submit the request**: After you confirm that the information is correct, click **Next**, and then click **Submit request**.

![](../../../assets/images/ec-第三方整合-google-gsc移除網址.en.gif)

## Important Notes and Limitations

*   **Temporary hiding**: This feature only hides the URL from search results **temporarily, for approximately 6 months**.
*   **Effective time**: After you submit the request, it usually takes effect within **a few hours to a few days**. The actual timing depends on Google's processing.
*   **The page still exists**: This feature only hides the page in search results. **The page can still be accessed through a direct link**.
*   **Secret group pages**: If you created a secret store group page and do not want Google to index it, be sure to configure page exclusion in GSC to keep it from appearing in search results.
*   **Customer support**: This operation is a feature of Google's official tool, and processing progress is determined by Google. CYBERBIZ does not provide customer support for this operation.

## Next Steps

<div class="grid cards" markdown>

- :lucide-eye-off:{ .lg }  
  [__Turn Off Product Search__](../../products/discoverability/product-search-visibility.md){ title="Set product search visibility" }  
  Use the **Product Search** feature in backend product management to keep specific products from appearing in search results.

</div>

## Frequently Asked Questions

??? quote "Can I permanently delete a page by using the Google Remove URLs tool?"

    It cannot be permanently deleted. This feature only **temporarily hides** the URL in search results, for approximately **6 months**. To exclude the page for the long term, add the `noindex` meta tag to the page or set up robots.txt rules.

??? quote "How long does it take for a removed URL to take effect?"

    After you submit the request, it usually takes effect within **a few hours to a few days**. The actual timing depends on Google's processing.

??? quote "Do secret store group pages need special handling?"

    If you created a secret store group page and do not want Google to index it, be sure to set up page exclusion in Google Search Console to keep it from appearing in search results.

