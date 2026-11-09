---
title: "Check and Resolve Website Security Risks with Google Safe Browsing"
description: "Learn how to use the Google Safe Browsing site status checker to proactively detect security risks on your storefront and request a review through GSC to remove the warning."
created: 2026-03-25 21:29
last_modified: 2026-07-02 17:05
lang: en-US
type: guide
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules:
  - 第三方整合
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 檢查網站安全性
  - 申請解除不安全警示
  - 預防網站被標記為不安全
features:
  - Google 安全瀏覽
  - Google Search Console
  - 安全性問題審核
  - 安全警示解除
prerequisites:
  - ec/integrations/google/setup-google-search-console/
related:
  - ec/integrations/google/setup-google-search-console/
  - ec/website-management/setup-manage-two-factor-auth/
  - ec/website-management/admin-security-settings/
tags:
  - "Google Safe Browsing"
  - "Website Security"
  - "Unsafe Website"
  - GSC
  - "Remove Security Warning"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - Google_Search_Console > 安全性與人工判決處罰 > 安全性問題
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3129
  - https://www.cyberbiz.io/support/?p=24812
permalink: "https://help.cyberbiz.io/ec/integrations/google/google-safe-browsing-security-check/"
comments: ""
search:
  exclude: false
icon: lucide/shield-alert
hide:
---

![Google Safe Browsing website tool](../../../assets/images/ec-google-安全瀏覽網站狀態工具.en.png){ .hero-page }

## Safe Browsing Website Status Guide

Google provides the Safe Browsing Site Status Checker, which helps merchants proactively check whether their storefront has security risks. This helps avoid being classified as an unsafe website, which can hurt brand trust and search rankings.

??? info"Learn More About Google Safe Browsing and the Transparency Report"

    - **Google Safe Browsing** is a website security protection mechanism. It detects malicious sites, such as phishing sites, malware, and Trojans, and displays a warning when users visit risky pages to reduce security threats. [Learn more :lucide-external-link:](https://safebrowsing.google.com/)
    - **Google Transparency Report** is based on Safe Browsing detection results. It provides public safety data and lookup tools that let site administrators check whether their site is flagged as a risky site. [Learn more :lucide-external-link:](https://transparencyreport.google.com/?hl=zh_TW)

## Check Whether Your Site Has Security Risks

1.  **Go to the tool page**: Open the [Google Check Site Status :lucide-external-link:](https://transparencyreport.google.com/safe-browsing/search?hl=zh_TW) tool page.
2.  **Enter the URL**: Enter the storefront URL you want to check in the search box and run the search.
3.  **Review the results**:
    *   ✅ **"No unsafe content found"**: Google has not detected any security concerns for this URL.
    *   ⚠️ **"This is an unsafe website"**: Google displays a short explanation that the site may contain deceptive content, distribute malware, or have other policy violations. If the site is blocked, users see a clear [warning page :lucide-external-link:](https://web.dev/articles/hacked?hl=zh-tw) when they open it.

![Google Safe Browsing site status check](../../../assets/images/ec-google-安全瀏覽網站狀態-不安全網站.en.png)

## What to Do If Your Site Is Marked as Unsafe

If Google marks your site as unsafe, follow these steps to request a review and remove the warning:

1.  **Review the solutions**: First, read Google's [Request a review :lucide-external-link:](https://web.dev/articles/request-a-review?hl=zh-tw) guide to learn how to address each type of security issue.
2.  **Go to [Google Search Console :lucide-external-link:](https://search.google.com/search-console) (GSC)**:
    *   Sign in to GSC, then click **Security & Manual Actions ** > ** Security Issues** in the sidebar.
    *   *Note: If you have not added your site to GSC, you must first complete [Site Ownership Verification](setup-google-search-console.md){ title="Register and verify Google Search Console" } before you continue.*
3.  **Fix the issues**: Based on the warning details in GSC, follow Google's recommended steps to fix each site issue.
4.  **Submit a review request**: After you fix the issues, click **Request review** on the GSC page. Google rechecks the site's security status.

!!! info "After you submit the review request, Google usually needs some time to reassess the site. For the latest processing status, refer to Google's official information."

![GSC security issues](../../../assets/images/ec-第三方整合-google-gsc安全性問題.en.png)

## Next Steps

To strengthen your storefront's security, we recommend that you always enable the related security settings in the CYBERBIZ admin. This lowers the risk that a compromised account is used to inject malicious content into your site.

<div class="grid cards" markdown>

- :lucide-monitor-smartphone:{ .lg }  
  [__Two-Step Verification__](../../website-management/setup-manage-two-factor-auth.md){ title="Set up and manage two-step verification" }       
  Turn on 2FA to prevent account takeover and lower the risk of malicious content being injected into your site.

- :lucide-brick-wall-shield:{ .lg }  
  [__IP Whitelist__](../../website-management/admin-security-settings.md#operate-security-ip-whitelist){ title="Protect admin accounts and customer data" }       
  Restrict the IP sources that can log in to the admin so that only authorized IPs can access the management interface.

</div>

## Frequently Asked Questions

??? quote"How long does it take to clear the warning after I submit a review request?"

    Google usually needs some time to reassess the site. For processing status, refer to Google's official information.

??? quote"What happens if my site is marked as unsafe?"

    When Google marks a site as unsafe, visitors see a clear warning page, which can lead to:

    - Lower brand trust
    - Impact on search rankings
    - Customer churn and lower conversion rates

??? quote"How can I prevent my site from being marked as unsafe?"

    We recommend that you enable the related security settings in the CYBERBIZ admin to lower the risk that a compromised account is used to inject malicious content into your site:

    - Turn on **two-step verification** (2FA)
    - Set up an **IP whitelist** to restrict login sources

