---
title: "Set Up the Shared Link Thumbnail (OG Image)"
description: "Specify Open Graph (OG) share images for products, collections, posts, or the whole site to control the thumbnail and preview shown when links are shared on social media."
created: 2025-03-03 00:00
last_modified: 2026-06-30 11:01
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify 一般版型 og image 設定路徑
  - inform 商品自訂分類群組圖片上傳 編輯器 URL 遺失問題
  - verify faq test weight
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 商品
sites: []
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定社群分享縮圖
  - 自訂商品轉貼圖片
  - 解決 Facebook 縮圖不更新問題
  - 優化 LINE 分享預覽
  - 更新全站 OG Image
  - 修正部落格文章分享圖
features:
  - OG Image
  - 商品圖片
  - 部落格文章縮圖
  - 商品群組縮圖
  - 全站縮圖
  - 社群分享快取解決方案
prerequisites: []
related: []
tags:
  - "OG Image"
  - "Social Sharing"
  - "Thumbnail Settings"
  - Facebook
  - LINE
  - "Cache Refresh"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
  - 商品 > 商品自訂分類 >
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3843
  - https://www.cyberbiz.io/support/?p=19718
permalink: "https://help.cyberbiz.io/ec/website-appearance/site-settings/setup-og-image/"
comments: false
search:
  exclude: false
icon: lucide/image-plus
hide:
---

![Shared link thumbnail settings](../../../assets/images/ec-網站外觀-og-image.en.png){ title="Shared Link Thumbnail Settings" .hero-page }

## About the Default Shared Link Image { #intro-og-image }

The **default shared link image (OG image)** is the thumbnail that platforms such as Facebook and LINE fetch and show automatically when you paste your website link there. A well-chosen OG image makes your brand look more professional and makes customers more likely to click the link.

Here is how to set it up for each page type:

## Thumbnail Settings by Page Type { #operate-og-image }

### Product Pages { #operate-og-image-product }

- **Path**: Sign in to the CYBERBIZ admin, go to **Products > All Products**, and click the name of the product you want to set up to open its editing page.
- **Steps**: Switch to the **Product Information** tab and upload the default link image in the **Product Image** section.
- **Automatic setting**: The system automatically uses the product's **first product image** as the shared link thumbnail.

![Product page thumbnail settings](../../../assets/images/ec-商品-商品編輯頁-商品圖片-第一張.en.gif){ title="Product Page Thumbnail Settings" }

---

### Product Collection Pages <small>Custom Categories</small> { #operate-og-image-collection }
    
- **Path**: Sign in to the CYBERBIZ admin, go to **Products > Customized Collections >**, and click the **Edit :lucide-square-pen:** button for the collection you want to set up.
- **Steps**:
	- Switch to the **Collection Description** tab and upload the image.
	- Switch to the **Image Info** tab, click **Browse Server**, and select the image you uploaded.
	- Click **Save** to apply the changes. This image serves as both the collection page visual and the shared link thumbnail.

![Product collection thumbnail settings](../../../assets/images/ec-網站外觀-商品自訂分類-群組圖片.en.gif){ title="Product Collection Thumbnail Settings" }

---

### Blog Posts { #operate-og-image-blog }
    
- **Path**: Sign in to the CYBERBIZ admin and go to **Website Appearance > Blog Management > select a post**.
- **Steps**: Select an image in the post settings. This image is used as the blog cover on the storefront and as the thumbnail when the link is shared.

![Blog post thumbnail](../../../assets/images/ec-網站外觀-部落格文章圖片.en.gif){ title="Blog Post Thumbnail" }

---

### Other Website Pages / Site-Wide Settings { #operate-og-image-global }
    
- **Path**:

	<!--
	- **Standard themes**: "Website Appearance" > "Theme Management" > "Site Settings" > "Detailed Settings (Homepage Settings)" > "Default Shared Link Image (OG image)."
	-->
	
	- **Drag-and-drop themes**: Sign in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Theme Setting > Global Settings > "Shared Image (OG Image)" in "Icon Settings"**.

- **What it does**: If a shared page is not one of the products, collections, or posts above (for example, the homepage or other pages), the general thumbnail set here is shown.

![Site-wide OG image settings](../../../assets/images/ec-網站外觀-全站設定-og-image.en.png){ title="Site-Wide OG Image Settings" }

## Fix Thumbnails That Don't Update When You Share Links { #operate-og-image-cache }

If you updated an image on a page but Facebook or LINE still shows the old information when you share it, it is because the platform keeps an old cached copy.

### Update Facebook Link Information Manually { #operate-og-image-fb }

1. Make sure the new image on your page has finished updating.
2. Open the **[Facebook Sharing Debugger :lucide-external-link:](https://developers.facebook.com/tools/debug/)**, paste the link you want to update, and click "Debug."
3. If it still shows the old information, click **"Scrape Again"** to force Facebook to read the page data again.
4. After the update succeeds, post the link on Facebook again to see the correct thumbnail and information.

![Scrape again in the Facebook debugger](../../../assets/images/ec-fb-share-debugger-再次抓取.en.png){ title="Scrape Again in the Facebook Debugger" }

<!--

### Update LINE Link Information Manually { #operate-og-image-line }

- Use LINE's official **[LINE Page Poker](https://poker.line.biz/)** tool: enter the URL and click "Clear" to clear the cache.

-->

## FAQ { #faq-og-image }

??? quote "Why don't I see a thumbnail when I share on LINE or Facebook even though I uploaded an image?"

	There are usually two reasons:

	1. **Cache issue**: Social platforms keep old data. See [Fix Thumbnails That Don't Update When You Share Links](#operate-og-image-cache) in this article and use the debugging tool to force an update.
	
	2. **Wrong image size**: If the image file is too large (over 8 MB) or the resolution is too low, the platform may fail to fetch it. Use the recommended specs.

??? quote "What is the recommended OG image size?"

	To make sure the image displays well without cropping on every social platform (Facebook, LINE, Instagram), use these specs:

	- **Recommended size**: 300 x 300 pixels (px).
	
	- **Aspect ratio**: 1:1.
	
	- **File format**: JPG, PNG, or GIF.
	
	- **File size**: Keep it under **1 MB** so platforms can fetch it quickly.

??? quote "What does the system show if I don't set an OG image for a product?"

	The system picks an image in this order:
	
	1. The product's **first product image**.
	
	2. If the product has no images, the OG image uploaded in **[Site-Wide Settings](#operate-og-image-global)**.
	
	3. If no site-wide image is set, the social platform picks a random image from the page (this usually looks worse, so at least complete the site-wide setting).

??? quote "Why did the product collection (custom category) image stop working in the editor?"

	If the URL is missing or the image does not display correctly when you edit the "Collection Description," check the following:
	
	* The image was first uploaded to the server successfully through the "Image Info" tab.
	
	* Avoid pasting image links directly from external websites. Always click **Browse Server** and select a file on your site to keep the link stable.

??? quote "I updated the site-wide OG image, but the homepage thumbnail is still the old one. What should I do?"

	The homepage carries the most weight, and its cache is the most stubborn. Besides using the Facebook debugger, try adding a random parameter to the end of the URL (for example, `https://yourstore.com/?v=1`) to test. If the URL with the parameter shows correctly, the cache for the plain URL is still waiting for the platform to update it automatically (usually within 24–48 hours).
