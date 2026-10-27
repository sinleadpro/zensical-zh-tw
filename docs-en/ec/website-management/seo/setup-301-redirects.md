---
title: "Set up 301 Redirects"
description: "Set up 301 redirects to send traffic to a new URL when a page URL stops working or changes, so you keep your SEO ranking."
created: 2026-03-20 13:59
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
  - 設定_301_轉址
  - 網站轉址
  - 維護_SEO_排名
features:
  - 301 重定向
  - 網站轉址
  - Excel 匯入
prerequisites: []
related:
  - ec/website-management/seo/submit-sitemap-to-gsc/
  - ec/website-management/seo/seo-guide/
tags:
  - "301"
  - Redirects
  - SEO
  - "Website Migration"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 網站轉址
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3490
  - https://www.cyberbiz.io/support/?p=15390
permalink: "https://help.cyberbiz.io/ec/website-management/seo/setup-301-redirects/"
comments: false
search:
  exclude: false
icon: lucide/signpost
hide: []
---

![URL Redirection settings](../../../assets/images/ec-管理中心-網站轉址.en.png){ title="URL Redirection Settings" .hero-page }

## About 301 Redirects { #intro-seo-redirect }

A **301 redirect** sends visitors from one URL to another. When a URL no longer works or is no longer updated, a redirect lowers the risk that search engine crawlers can't find your content after you switch systems or move your website, which would cause your **SEO ranking to drop**.

!!! example "When to Use It"

    This feature is especially useful when you **move your website** or when **event pages expire**. It sends traffic from popular old articles or products to the matching new pages, and it is the best way to protect your website's organic search ranking.

## Requirements and Limits { #prerequisites-seo-redirect }

- [x] **Domain requirement**: To set up 301 redirects, you must use **your own domain**.
- [x] **When it takes effect**: By design, **the redirect only runs and sends visitors to the new URL when the old URL shows a 404 page**.
- [x] **What to redirect**: Focus on valuable, popular pages. You don't need to redirect every page.
- [x] **Chinese URLs**: If a page has a Chinese URL, **don't use the encoded (garbled) form** when you set up the redirect.

## Steps { #operate-seo-redirect }

### Method 1: Add Redirects One by One { #operate-seo-redirect-single }

1.  **Open the page**: Log in to the CYBERBIZ admin panel and go to **Website Management** > **Redirection**.
2.  **Enter the details**: Click **Add Redirect URL** and fill in the following fields:
    *   **Name (required)**: Name this redirect so you can find it easily later.
    *   **Old URL**: The left side shows your primary domain by default. On the right, enter the path of the original page (for example, `/products/old`).
    *   **New URL**: The left side also shows your primary domain. On the right, enter the path of the new page you have already created (for example, `/products/new`).
3.  **Save**: Check the details and save.

![Add redirect URL](../../../assets/images/ec-管理中心-網站轉址-新增轉址網址.en.png){ title="Add Redirect URL" }

---

### Method 2: Add in Bulk (Excel Import) { #operate-seo-redirect-bulk }

1.  **Open the page**: Log in to the CYBERBIZ admin panel and go to **Website Management** > **Redirection**.
2.  **Download the template**: Click **Download Excel Example**.
3.  **Fill in the data**: Open the file and fill in each column:
    *   **Column A**: Name this redirect so you can find it easily later.
    *   **Column B**: The old URL path.
    *   **Column C**: The new URL path.
4.  **Import**: Click **Import Excel Redirect List** to upload the file. The system sets up all the redirects automatically.

![Excel redirect template](../../../assets/images/ec-管理中心-網址轉址-excel範本.en.png){ title="Excel Redirect Template" }

## Next Steps { #next-steps-seo-redirect }

<div class="grid cards" markdown>

- :lucide-map:{ .lg }
  [__Submit Your Sitemap__](submit-sitemap-to-gsc.md){ title="Submit a Sitemap to Google Search Console" }
  Submit the sitemap that the system generates automatically to Google Search Console.

- :lucide-search:{ .lg }
  [__SEO Settings and Optimization__](seo-guide.md){ title="SEO Settings and Optimization Guide" }
  Learn about all of the SEO settings in the CYBERBIZ system.

</div>

## FAQ { #faq-seo-redirect }

??? quote "How long does a 301 redirect take to work?"

    A 301 redirect usually takes **a few hours to 24 hours** to take effect. The next time Google's crawler visits your website, it detects the redirect and updates its index.

??? quote "Can I redirect several old URLs to the same new URL?"

    Yes. You can point several source URLs (old URLs) to the same target URL (new URL). This is especially useful when you move your website or remove products.

??? quote "Can I just delete a page instead of setting up a redirect?"

    We recommend that you don't delete pages directly. If a page has built up SEO ranking, deleting it causes a 404 error and loses that ranking. Set up a 301 redirect to a related page instead to keep its SEO value.
