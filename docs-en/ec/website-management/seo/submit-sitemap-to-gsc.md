---
title: "Submit a Sitemap to Google Search Console"
description: "Submit the sitemap that CYBERBIZ generates automatically to Google Search Console to get your pages indexed faster and improve SEO performance."
created: 2026-03-20 13:43
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
  - 提交_Sitemap
  - Google_Search_Console
  - 加快網頁收錄
  - SEO_優化
features:
  - Sitemap
  - "Google Search Console"
  - XML
prerequisites:
  - ec/integrations/google/setup-google-search-console/
  - ec/integrations/google/ga/setup-google-analytics/
related:
  - ec/integrations/google/setup-google-search-console/
  - ec/integrations/google/ga/setup-google-analytics/
tags:
  - Sitemap
  - SEO
  - Google Search Console
  - "Website Indexing"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > SEO
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=467
  - https://www.cyberbiz.io/support/?p=3807
permalink: "https://help.cyberbiz.io/ec/website-management/seo/submit-sitemap-to-gsc/"
comments: false
search:
  exclude: false
icon: lucide/map
hide: []
---

![Sitemap submission settings](../../../assets/images/ec-第三方整合-google-gsc-sitemap.en.png){ title="Sitemap Submission Settings" .hero-page }

## About Sitemaps { #intro-sitemap-gsc }

A sitemap is an XML file that lists the URLs of all the important pages on your website. Search engines (such as Google) use it as a guide for crawling and indexing.

In the CYBERBIZ system, the platform generates a sitemap for every website automatically, so you don't need to create the file yourself. Just submit the sitemap to Google Search Console (GSC) to help search engines understand and index your website content more efficiently.

!!! note "For more about sitemaps, see [Google's official documentation :lucide-external-link:](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview?hl=zh-tw)."

!!! tip "Why Submit a Sitemap"

    When you submit a sitemap, you can:

    *   **Get new pages indexed faster**: Search engines find your new products or event pages sooner.
    *   **Speed up content updates**: When you change page content, search engines can pick up the update more efficiently.
    *   **Improve SEO performance**: Search engines understand your website structure better.

## Requirements and Limits { #prerequisites-sitemap-gsc }

Before you submit, make sure you have completed the following:

- [x] [**Register for Google Search Console**](../../integrations/google/setup-google-search-console.md){ title="Register and Verify Google Search Console" } and verify ownership of your website.
- [x] [**Connect Google Analytics (GA4)**](../../integrations/google/ga/setup-google-analytics.md){ title="Create and Connect Google Analytics" }: We recommend managing GSC and GA4 with the same Google account.

## Steps { #operate-sitemap-gsc }

### Check Your Sitemap File { #operate-sitemap-gsc-check }

To check that the file exists, enter your website URL in the browser address bar and add `/sitemap.xml` to the end.

*   For example: `www.yourname.com/sitemap.xml`.
*   If the page shows XML code, your website has a sitemap.

![Check the sitemap URL](../../../assets/images/ec-行銷活動-seo-sitemap-url.en.png){ title="Check the Sitemap URL" }

---

### How to Submit { #operate-sitemap-gsc-submit }

1.  **Log in to GSC**: Open [Google Search Console :lucide-external-link:](https://search.google.com/search-console/).
2.  **Open the Sitemaps page**: In the left menu, click **Indexing**」>「**Sitemaps**.
3.  **Enter the file name**: In the **Add a new sitemap** field, enter `sitemap.xml`.
4.  **Submit**: Click **Submit**.
5.  **Finish**: When a **Sitemap submitted successfully** dialog appears, you are done.

![Submit the sitemap](../../../assets/images/ec-行銷活動-googlesearchconsole-提交sitemap.en.png){ title="Submit the Sitemap" }

## Important { #prerequisites-sitemap-gsc-notes }

*   **Waiting time**: After you submit, Google needs time to analyze and rank your pages. All updates follow Google's schedule.
*   **Domain settings**: Set your own domain as the primary domain in the admin panel and turn on **Always redirect** so that indexed URLs stay consistent.

## FAQ { #faq-sitemap-gsc }

??? quote "What if the status shows "Couldn't fetch" or "Fetch failed" after I submit?"
    This is usually temporary. First check that you entered the URL correctly (you only need to enter sitemap.xml). If the URL is correct, Google's crawler usually just hasn't processed it yet.

    * What to do: Wait 24–48 hours and check again. If it keeps failing, check whether your website has a setting turned on that blocks search engine indexing (for example, on a test site).

??? quote "I updated products or categories. Do I need to submit sitemap.xml again?"
    No. CYBERBIZ generates the sitemap dynamically, so the file updates automatically when you add products or pages. Google revisits your sitemap regularly to pick up new data, and submitting it again manually doesn't speed this up.

??? quote "Why is the number of URLs in the sitemap different from the number Google actually indexes?"
    This is normal. A sitemap is a list of pages you suggest Google should crawl, but Google decides whether to index each page based on page quality, duplicate content, and crawl budget.

    * Possible reasons: Some pages have too little content, there are duplicate URLs, or new pages are still waiting to be crawled.

??? quote "Should I enter the full URL when submitting?"
    No. In the Google Search Console sitemap field, your website's root URL is already shown at the front. Just enter sitemap.xml in the input box after it.
