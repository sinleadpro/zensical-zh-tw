---
title: Applications of Referral Code Links
description: After obtaining the Referral Code, create a short URL or QR Code, or set UTM parameters to integrate the referral link into marketing channels such as FB, IG, LINE, or printed materials. This also lets you accurately track the conversion performance of each source.
created: 2026-02-06 00:00
last_modified: 2026-06-30 10:52
lang: zh-TW
type: guide
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
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - 企業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 製作推薦連結
  - 產生 QR Code
  - 設定 UTM 參數
  - 測試推薦連結
features:
  - 推薦人分潤
  - UTM 追蹤
prerequisites: []
related: []
tags:
  - 推薦連結
  - QR Code
  - UTM
  - 短網址
  - 行銷追蹤
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
permalink: "https://help.cyberbiz.io/ec/profit-sharing/referral-link-applications/"
comments: false
search:
  exclude: false
icon: lucide/share-2
hide: []
---
# Applications of Referral Code Links

After obtaining the Referral Code, create a short URL or QR Code, or set UTM parameters to integrate the referral link into marketing channels such as FB, IG, LINE, or printed materials. This also lets you accurately track the conversion performance of each source.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | Brand Official Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Advanced / Expert / All PLUS Plans / Enterprise
{ .doc-badge }

!!! tip "Use Cases"
	- **Social Media Promotion**: Shorten the long URL and add it to an IG bio or FB post to improve its appearance and increase the click-through rate.
	- **Drive Traffic from In-Person Events**: Create a dedicated QR Code and print it on in-store posters or product tags to direct customers to scan the code and claim an offer.
	- **Precise Ad Tracking**: Use UTM parameters to distinguish the conversion performance of different influencers (KOLs) or ad placements.


## What Is an Referral Code Link?

An Referral Code link is a special link with a dedicated "Referral Code (rcode)" parameter embedded after the website URL.

- **Identity Tracking**: After a customer clicks the link, the browser automatically records the identity information for that promotion.
- **Automatic Population**: When a customer checks out through the link, the system automatically populates the field with the Referral Code. The customer does not need to enter it manually.


## Workflow

### Step 1: Obtain and Customize the Referral Code Link

Before starting a promotion, copy the original link containing the Referral Code from the admin panel.

1. Log in to the CYBERBIZ admin panel and go to **Profit Sharing Referral Search**.
2. Search and click the target partner. Find the partner's dedicated **Profit Sharing Code/Link**.
3. Click the **Copy Sharing Link** icon next to the link.
4. Create one of the following based on your promotional needs:

    === "Generate a Short URL"

        If the link is too long to share on social media, use an external URL shortener.

        - **Step**: Paste the copied **complete referral link** into the tool to generate a short URL.
        - **Warning**: Never shorten the URL first and then manually append the Referral Code.

    === "Generate a QR Code"

        Use this option for offline printed materials or livestream screens.

        - **Step**: Paste the link into any QR Code generator to generate the corresponding image.
        - **Application**: Place the QR Code at the checkout counter, on package inserts, or in magazine ads.

    === "Set UTM Parameters"

        Use UTM parameters to distinguish the performance of the same Referrer across different channels.

        - **Manual Setup Rule**: Add the `&` symbol after the referral link (for example, `.../?rcode=xxx`), and then enter the UTM parameters.
        - **Correct Example**: `https://.../?rcode=xxx&utm_medium=fb&utm_source=kol_a`
        - **Incorrect Example**: `https://.../?rcode=xxx?utm_medium=fb` (do not use two question marks)


### Step 2: Test the Referral Link

Before publishing the link, follow these steps to confirm that tracking works correctly.

1. Go to **Marketing Campaigns Referral Program** and confirm that **Show referral code in checkout page** is turned on.
2. Copy the promotional link you created.
3. Open an **incognito window** in your browser.
4. Paste the promotional link and open the website. Add any product to the cart.
5. Go to the checkout page and confirm that the **Referral Code** field is automatically populated with the correct code.
    - If the code appears in the field, link tracking works correctly and the link is ready for promotion.
    - If the field is blank, check the link format again.



## Frequently Asked Questions

??? quote "Why did the Referral Code stop working after I shortened the URL?"
    This usually happens because the URL entered into the URL shortener was the website's home page URL **without the Referral Code**. Confirm that the input for the URL shortener is the complete string containing `?rcode=...`.

??? quote "Are UTM parameters required?"
    No. The Referral Code (rcode) determines **who receives credit for the sale**, while UTM parameters identify **where the traffic came from**. If you do not need to analyze traffic sources, use the original referral link.



