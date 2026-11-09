---
title: "Verify Tracking Code Installation with Google Tag Assistant"
description: "Use Google Tag Assistant to verify that GA4, GTM, Google Ads, and other tracking codes are installed correctly and fire as expected."
created: "2026-03-17 21:36"
last_modified: 2026-07-02 16:19
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
  - Google Tag Manager
  - GA4 驗證
  - 代碼安裝
  - 追蹤除錯
features:
  - Google Tag Assistant
  - GA4
  - GTM
tags:
  - "Google Tag Assistant"
  - GA4
  - GTM
  - code_verification
  - tracking_code
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > GTM 設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=741
  - https://www.cyberbiz.io/support/?p=234
permalink: "https://help.cyberbiz.io/ec/integrations/google/verify-tracking-tag-installation/"
comments: false
search:
  exclude: false
icon: lucide/bug
hide: []
---

![Verify tracking code with Google Tag Assistant](../../../assets/images/ec-第三方整合-google設定-googletagassistantconsole.en.png){ title="Verify tracking code with Google Tag Assistant" .hero-page }

## Google Tag Assistant Overview

Use **Google Tag Assistant** to confirm that **Google Analytics (GA4)**, **Google Tag Manager (GTM)**, or **Google Ads** tracking codes are installed correctly on your site and check their status in real time.

This tool comes in two forms. We recommend using both to get a complete view of your site's tracking status:

!!! info "Differences Between the Tag Assistant Extension and the Web Version"

    *   **Chrome extension**: Best for **quickly checking** whether the tracking code loads and runs successfully.
    *   **Web version**: Best for **verifying event triggers and debugging**. It fully records user actions on your site and tag parameters.

## Steps

### Install and Use the Chrome Extension

1.  **Install the extension**: Go to the Chrome Web Store, search for **Tag Assistant**, open its listing page, and click **Add to Chrome**.
2.  **Confirm the icon**: After installation, a **blue tag icon** appears in the upper-right corner of your browser (or find it in the puzzle-piece extensions list).
3.  **Detect in real time**: Open the page you want to check, click the blue tag icon, and the system automatically displays a list of Google tracking codes detected on the page.

![Install Tag Assistant extension](../../../assets/images/ec-第三方整合-googletagassistant-install.en.gif){ title="Install Tag Assistant extension" }

!!! info "For more information and tutorials on the Tag Assistant Chrome extension, see the [official documentation :lucide-external-link:](https://support.google.com/tagmanager/answer/16463290?hl=zh-Hant&ref_topic=15213501&sjid=3100390479866986802-NC)."

---

### View Detailed Event Information in the Web Version

To further confirm that specific tags (such as checkout or add to cart) fire correctly, follow these steps:

1.  **Sign in and connect**: Sign in to the [Google Tag web version :lucide-external-link:](https://tagassistant.google.com/), click **Add domain**, enter your website URL, and click **Connect**.

    ![Add domain and connect](../../../assets/images/ec-第三方整合-googletagassistant-adddomain.en.png){ title="Add domain and connect" }

2.  **Simulate actions**: The system opens a new browser tab. In that tab, simulate customer actions, such as **clicking buttons** and **completing checkout**.
3.  **Review results**: Return to the Tag Assistant web page to view the detected **Google tags**, along with the **execution status** of each **event** and its parameters.

    ![Tag Assistant detection results](../../../assets/images/ec-第三方整合-googletagassistant-result.en.png){ title="Tag Assistant detection results" }

!!! info "For more information and tutorials on Tag Assistant, see the [official documentation :lucide-external-link:](https://support.google.com/tagmanager/answer/15212503?hl=zh-Hant&ref_topic=15213501&sjid=3100390479866986802-NC#)."

## Frequently Asked Questions

??? quote "How do I check whether Google Analytics (GA4) is installed correctly?"

    Open any page on your website and click the Tag Assistant icon on the Chrome toolbar. If it is installed correctly, the system automatically shows the detection status of the GA4 code.

??? quote "What is the difference between the Chrome extension and the web version?"

    The Chrome extension is best for quickly checking whether the tracking code is installed. The web version fully records user actions on your site, so it is best for verifying that events (such as checkout or add to cart) fire correctly.

??? quote "Why doesn't Tag Assistant detect the tracking code?"

    Make sure you have completed the following:

    - [x] The Chrome extension is installed correctly
    - [x] The page has been reloaded
    - [x] The tracking code is published to the live environment

    If it still cannot be detected, check that the GTM or GA4 back-end settings are correct.
