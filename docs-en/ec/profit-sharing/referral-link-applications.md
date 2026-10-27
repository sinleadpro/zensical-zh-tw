---
title: "Using Referral Code Links"
description: "Once you have a Referral Code, you can create short URLs or QR codes, or add UTM parameters, to use your referral link across marketing channels (such as Facebook, Instagram, LINE, or printed materials) and accurately track sales from each source."
created: 2026-02-06 00:00
last_modified: 2026-06-30 10:52
lang: en-US
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
  - 分潤
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
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
  - "Referral link"
  - "QR Code"
  - UTM
  - "Short URL"
  - "Marketing tracking"
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
# Using Referral Code Links

Once you have a Referral Code, you can create short URLs or QR codes, or add UTM parameters, to use your referral link across marketing channels (such as Facebook, Instagram, LINE, or printed materials) and accurately track sales from each source.
{ .subtitle }

[:lucide-layers:{ title="適用產品" }](../../resources/conventions#適用產品) | Brand Website / Smart POS
[:lucide-tag:{ title="適用方案" }](../../resources/conventions#適用方案) | Advanced / Expert / All PLUS / Enterprise
{ .doc-badge }

!!! tip "Use cases"
	- **Social media**: Shorten long URLs for your Instagram bio or Facebook posts. They look cleaner and get more clicks.
	- **In-person events**: Print a dedicated QR code on in-store posters or product tags so customers can scan it to claim an offer.
	- **Ad tracking**: Use UTM parameters to compare conversions from different influencers (KOLs) or ad placements.


## What Is A Referral Code Link?

A Referral Code link is your store URL with a dedicated "Referral Code (rcode)" parameter added at the end.

- **Tracks the referrer**: When a customer clicks the link, the browser automatically records who referred them.
- **Fills in the code**: When the customer checks out after using the link, the system fills in the Referral Code automatically, so the customer doesn't have to type it.


## Steps

### Step 1: Get And Customize The Referral Code Link

Before you start promoting, copy the original link with the Referral Code from the admin.

1. Log in to the CYBERBIZ admin and go to **Profit Sharing > Referral Search**.
2. Search for and click the partner, then find their **profit-sharing code/link**.
3. Click the **copy share link** icon next to the link.
4. Depending on how you'll promote it, do one of the following:

    === "Create a short URL"

        If the link is too long to share on social media, use an external URL shortener.

        - **How**: Paste the copied **full referral link** into the tool.
        - **Note**: Never shorten the URL first and then add the Referral Code by hand.

    === "Create a QR code"

        Best for printed materials or livestreams.

        - **How**: Paste the link into any QR code generator to create the image.
        - **Where to use it**: Place the QR code at the checkout counter, on cards included in packages, or in magazine ads.

    === "Add UTM parameters"

        Use these to compare how one Referrer performs across different channels.

        - **Manual setup**: After the referral link (such as `.../?rcode=xxx`), add the `&` symbol, then the UTM parameters.
        - **Correct**: `https://.../?rcode=xxx&utm_medium=fb&utm_source=kol_a`
        - **Incorrect**: `https://.../?rcode=xxx?utm_medium=fb` (don't use two question marks)


### Step 2: Test The Referral Link

Before you publish the link, follow these steps to make sure tracking works.

1. Go to **Marketing > With Referrers** and make sure **Show referral code in checkout page** is turned on.
2. Copy the promotion link you created.
3. Open an **incognito window** in your browser.
4. Paste the link to open the site, then add any product to the cart.
5. Go to the checkout page and check that the **Referral Code** field shows the correct code.
    - If the code is filled in, tracking works and you can start promoting.
    - If the field is empty, check the link format again.



## FAQ

??? quote "Why does my Referral Code stop working after I shorten the URL?"
    This usually happens when you shortened **your store's homepage URL without the Referral Code**. Make sure the URL you shorten is the full string that includes `?rcode=...`.

??? quote "Do I have to add UTM parameters?"
    No. The Referral Code (rcode) decides **who gets credit for the sale**, while UTM parameters show **where the traffic comes from**. If you don't need to analyze traffic sources, just use the original referral link.



