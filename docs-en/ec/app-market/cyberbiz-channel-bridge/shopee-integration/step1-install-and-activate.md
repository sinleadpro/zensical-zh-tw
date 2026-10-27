---
title: "Step 1: Install and Authorize Your Shop"
description: "With the Omnichannel Management Assistant, you can quickly sync products from your Shopee shop to your CYBERBIZ online store without creating them manually."
created: 2026-02-25 00:00
last_modified: 2026-07-08 17:32
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - APP MARKET
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions:
  - CHANNEL BRIDGE
intents:
  - 安裝全通路助手
  - 授權蝦皮商店
features:
  - 蝦皮商品搬站
  - 全通路管理助手
prerequisites:
  - "需具備蝦皮台灣站 (TW) 賣家帳號"
related:
  - ec/app-market/cyberbiz-channel-bridge/shopee-integration/step2-import-products-and-link/
tags:
  - "Product Import"
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - App Market > 擴充服務市集
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=365
  - https://www.cyberbiz.io/support/?p=3532
permalink: "https://help.cyberbiz.io/ec/app-market/cyberbiz-channel-bridge/shopee-integration/step1-install-and-activate/"
comments: false
search:
  exclude: false
icon: lucide/key
hide: []
---
# Step 1: Install and Authorize Your Shop

With the Omnichannel Management Assistant, you can quickly sync products from your Shopee shop to your CYBERBIZ online store and skip creating them by hand.
{ .subtitle }

[:lucide-lock:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | CYBERBIZ CHANNEL BRIDGE
{ .doc-badge }

![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-畫面總覽01.en.png){ .hero-page }



!!! tip "Use Cases"
    - **New Store Launch**: You are moving from Shopee to your own online store and need to move hundreds of products quickly.
    - **Running Both Channels**: You run your online store and Shopee at the same time and need to import new Shopee products into your store.
    - **Multiple Shops**: You have several Shopee accounts and need to import their products into the same online store admin in batches.


## Before You Start { #prerequisites-shopee-s1 }

- **Account Restriction**: Only **Shopee Taiwan (TW)** accounts are currently supported.
- **Data Security**: Authorization uses the official API. The system never receives your Shopee account password.
- **Multiple Accounts**: One online store admin can connect to only one Shopee account at a time. To move products from several shops, finish one shop, **cancel authorization**, and then connect the next account.


## Setup Steps { #operate-shopee-s1 }

### Step 1: Install the Omnichannel Management Assistant { #operate-shopee-s1-step-1-manage }

1. Log in to the CYBERBIZ admin, go to **APP MARKET > App Market**, and click **CYBERBIZ CHANNEL BRIDGE**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店01.en.png)
2. Click **Install App**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店02.en.png)
3. On the installation page, select the authorization option and click **Confirm installation**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店03.en.png)
4. Make sure **CYBERBIZ CHANNEL BRIDGE** appears, then click **Settings** to open the management interface.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店04.en.png)

### Step 2: Authorize Your Shopee Shop Account { #operate-shopee-s1-step-2-authorize }

1. In the Omnichannel Management Assistant, click **Request Authorization**.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店05.en.png)
2. On the Shopee authorization page that opens, select **TW** as the region.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店06.en.png)
3. Log in with your Shopee seller account and password.
4. Click **Confirm Authorization** to grant access.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店07.en.png)
5. For the duration, we recommend selecting **365 days** to keep syncing stable over the long term.
6. After authorization succeeds, the shop status shows `已連結`.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-授權商店09.en.png)


### Step 3: Manage and Renew Authorization { #operate-shopee-s1-step-3-manage }

- **Check Status**: On the **Shop Settings** tab, view the current **Shop Status** and **Expiration Date**.
- **Expiration Reminders**: The system sends email reminders 30, 15, 7, 3, and 1 days before authorization expires.
- **Reauthorize**: If authorization expires, click **Reauthorize** to restore the feature.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-重新授權01.en.png)
- **Switch Accounts**: To import products from another Shopee shop, click **Cancel Authorization** first, then repeat Step 2.
    ![](../../../../assets/images/EC-後台-APPMARKET-蝦皮商品-取消授權01.en.png)


## FAQ { #faq-shopee-s1 }

??? quote "Why does nothing happen when I click authorize?"
    Check whether your browser is blocking pop-up windows. We recommend using Chrome with ad blockers turned off.

??? quote "Will products I already moved disappear after authorization expires?"
    No. Expired authorization only affects "importing new products" and "data sync". Product data already moved to your online store is not affected.

??? quote "Can I connect two Shopee accounts at the same time?"
    No. The system can connect only one Shopee account at a time. Work in batches: **cancel the old authorization first, then connect the new account**.


## Next Steps { #next-steps-shopee-s1 }

<div class="grid cards" markdown>

- :lucide-arrow-right-circle:{ .lg }
  [__Shopee Product Migration Step 2: Import Products__](step2-import-products-and-link.md)
  After authorization, start selecting products and moving them to your online store.

</div>


