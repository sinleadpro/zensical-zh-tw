---
title: "Application Of Referral Code Links"
description: "Once you obtain a referral code, you can integrate the referral link into various marketing channels (such as Facebook, Instagram, LINE, or physical promotional materials) by creating a shortened URL, QR code, or setting UTM parameters, and accurately track the sales performance of different sources."
created: 2026-02-06 00:00
last_modified: 2026-06-30 10:52
lang: en-US
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
  - POS
modules:
  - 行銷活動
sites:
  - TW
audiences:
  - admin
difficulty: intermediate
tnb: branch
plans:
  - Enterprise
  - Advanced
  - Expert
cyb_extensions: []
intents:
  - 製作推薦連結
  - 產生_QR_Code
  - 設定_UTM_參數
  - 測試推薦連結
features:
  - 推薦人分潤
  - UTM_追蹤
prerequisites: []
related: []
tags:
  - "Recommended Links"
  - "QR Code"
  - UTM
  - "Shortened URL"
  - "Marketing Tracking"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 分潤 > 分潤查詢
  - 行銷活動 > 推薦人分潤
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=4051
permalink: "https://help.cyberbiz.io/ec/profit-sharing/referral-link-applications.en"
comments: false
search:
  exclude: false
icon: lucide/share-2
hide: []
---
After obtaining a referral code through # , you can integrate the referral link into various marketing channels (such as Facebook, Instagram, LINE, or physical promotional materials) by creating a shortened URL, QR code, or setting UTM parameters, and accurately track the sales performance of different sources.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | Brand Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Advanced / Expert / All PLUS / Enterprise
{ .doc-badge }

!!! tip " Application Scenarios "
	-  **Social Media Promotion**: Shorten long URLs and place them in IG news feeds or Facebook posts to enhance visual appeal and increase click-through rates.
	-  **In-Store Event Traffic Generation**: Create exclusive QR codes and print them on in-store posters or product tags to guide customers to scan the code and receive discounts.
	-  **Precise Ad Tracking**: Differentiates conversion rates between different influencers (KOLs) or ad placements using UTM parameters.


## What Is A Referral Code Link?

Referral Code Link refers to a special link that embeds a unique "referral code (rcode)" parameter at the end of the official website URL.

-  **Identity Recording**: After a consumer clicks the link, the browser will automatically record the consumer's identity information for that promotion.
-  **Auto-Input**: When checking out via the link, the system will automatically populate the referral code field, eliminating the need for manual input by the consumer.


## Operating Procedures

### Step 1: Obtain And Process The Referral Code Link
Before starting the promotion, please copy the original link containing the referral code from the backend. Log in to the CYBERBIZ management backend and go to **Profit Sharing > Referral Search**. Search for and select your target partner to find their unique **revenue sharing code/link**. Click the **copy and share link** icon next to the link. Create the following applications according to your promotion needs: Generate a shortened URL. If the link is too long to share in the community, you can use an external URL shortening tool. **Step**: Paste the copied **complete referral link** into the tool's output. **Note:** Never shorten the URL first and then manually concatenate the referral code. **QR Code Generation:** Generate a QR Code. **Application:** Suitable for offline printing or live streaming. **Steps:** Paste the link into any QR code generator to generate the corresponding image. **Applications:** It is recommended to place the QR code at checkout counters, on package inserts, or in magazine advertisements. **Using:** Set UTM parameters. **Using:** To differentiate the performance of the same referrer across different channels. **Manual Rule Setting**: Add the symbol `&` after the recommended link (e.g., `.../?rcode=xxx`), followed by the UTM parameter. **Correct Example**: `https://.../?rcode=xxx&utm_medium=fb&utm_source=kol_a`
        -  **Incorrect Example**: `https://.../?rcode=xxx?utm_medium=fb` (Do not use two question marks)


### Step 2: Test The Validity Of Recommended Links
Before officially publishing the link, please be sure to test the tracking function according to the following steps:

1.  Go to **Marketing > With Referrers** and confirm that **Enable display of referral code field on checkout page** is enabled.
2.  Copy the promotional link you created.
3.  Open your browser's **incognito window**.
4.  Paste the promotional link and go to the website, randomly adding any item to your cart.
5.  Go to the checkout page and confirm that the **referral code** field has automatically entered the correct code.
    -  If the field has entered the code: the link tracking function is working properly and you can officially promote it.
    -  If the field is empty: please double-check that the link format is correct.



## Frequently Asked Questions
Why does my referral code become invalid after shortening the URL? This is usually because you entered the **official website homepage URL without the referral code** into the URL shortening tool. Please ensure that the input source for the URL shortening tool is the complete string containing `?rcode=...`. Is the UTM parameter necessary? It is not. The referral code (rcode) is responsible for **calculating who receives the performance bonus**, while the UTM is responsible for **analyzing where the traffic comes from**. If you do not need to analyze the traffic source, you can simply use the original referral link.
