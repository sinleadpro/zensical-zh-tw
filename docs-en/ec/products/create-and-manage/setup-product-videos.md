---
title: "Set up Product Videos"
description: "Upload and manage product videos to make storefront product pages and pop-ups more engaging, with support for Meta catalog ad sync."
created: 2026-03-08 17:10
last_modified: 2026-07-12 18:49
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - 圖示-上傳商品影片
  - verify MBE
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
  - 網站外觀
sites:
  - TW
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 上傳商品影片
  - 管理商品媒體庫
  - 設定影片顯示順序
  - 同步 Meta 目錄廣告影片
features:
  - 影片上傳
  - 媒體庫管理
  - 影片規格限制
  - Meta 目錄型廣告同步
prerequisites:
related:
  - ec/website-appearance/theme-and-layout/setup-global-theme-settings/
  - ec/integrations/fb/meta-ads/sync-product-videos-meta-catalog/
tags:
  - "Product Videos"
  - "Media Gallery"
  - "Video Specifications"
  - "Meta Ads"
  - "Visual Marketing"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 媒體庫
  - 商品編輯頁
  - 全站設定
paths:
  - 商品 > 所有商品 > 新增商品
  - 商品 > 所有商品
  - 商品 > 媒體庫
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1830
  - https://www.cyberbiz.io/support/?p=984
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/setup-product-videos/"
comments: false
search:
  exclude: false
icon: lucide/play
hide:
---

![Set up product videos](../../../assets/images/ec-product-video.zh-tw.en.png){ title="Set Up Product Videos: Products > All Products > Product Name > Product Video" .hero-page }

## About Product Videos { #intro-product-video }

Adding videos to product pages makes product displays more visually appealing, and customers can watch them directly on the product page and in pop-ups. This document explains how to upload product videos, set where they appear in pop-ups, and manage all video files in the Media Gallery.

## Prerequisites and Limits

### Scope

=== "Supported"
	| Section/Page       | Video Supported |
	| --------------- | ------------ |
	| Product page          | :material-check: |
	| Home page product section pop-up        | :material-check: |
	| Product category page pop-up          | :material-check: |
	| New Buy X Get Y discount page pop-up       | :material-check: |
	| Multi-level product category page pop-up     | :material-check: |
	| Bonus Mall pop-up            | :material-check: |
	| Express Delivery pop-up            | :material-check: |
	| One-page store product section pop-up    | :material-check: |

=== "Not Supported"
	| Section/Page       | Video Supported |
	| --------------- | ------------ |
	| Collection page          | :material-close: |
	| Product zoom       | :material-close: |

---

### Video Specifications

To make sure videos upload, process, and play correctly on the storefront, follow these technical specifications:

- **Resolution**: Up to 1280 × 1280 pixels.
- **Recommended ratio**: 9:16, which is optimized for Facebook ad placements.
- **Video format**: MP4 only.
- **Video length**: Up to 60 seconds.
- **File size**: Up to 30 MB. Loading speed depends on the user's network, so compress files as much as possible within the specifications.
- **Audio**: Audio output is not currently supported. Uploaded videos play muted.

## Steps

### Upload Product Videos

=== "Upload a Video When Adding a Product"

	1. Log in to the CYBERBIZ admin and go to **Products > All Products > Add Product**.
	2. In the product video section, click **Upload** and select a video file from your computer.
	3. After checking the video and product information, click **Save**. The system processes the video upload. Wait for it to finish.
	4. Uploaded videos can be managed centrally in [Media Gallery video management](#media).

=== "Add a Video to an Existing Product"

	1. Log in to the CYBERBIZ admin and go to **Products > All Products**.
	2. In the product list, click the name of the product you want to edit to open the product edit page.
	3. In the product video section, click **Upload** and select a video file from your computer. If you have uploaded videos before, you can click **Select a video from the Media Gallery** instead.
	4. After checking the video, click **Save**. The system processes the video upload. Wait for it to finish.

!!! tip "After a video is uploaded, you can choose **Select a video from the [Media Gallery](#media)** when editing a product page to add it to the product directly."

---

### Video Pop-Up Display Settings

Set where videos appear in product pop-ups for all products to improve the storefront display.

1. Log in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting > Detail Settings > Global Settings**.
2. In the **Product Video Settings** section, choose where the video appears
	- `Before Product Images`: The video plays before the product images.  
	- `After Product Images`: The video plays after the product images.

![Video pop-up display](../../../assets/images/ec-product-video-display.zh-tw.en.gif){ title="Video Pop-Up Display" }

---

### Media Gallery Video Management { #media }

1. Log in to the CYBERBIZ admin and go to **Products > Media Gallery**.
2. Manage all video files in one place. You can **search videos :lucide-search:**, **delete videos :lucide-trash-2:**, and **Upload Video**.

![Media Gallery video management](../../../assets/images/ec-product-media-gallery.zh-tw.en.png){ title="Media Gallery Video Management" }


## Next Steps

<div class="grid cards" markdown>

- :lucide-settings-2:{ .lg }  
  [__Global Settings__](../../website-appearance/theme-and-layout/setup-global-theme-settings.md#product-display-layout){ title="Global Settings" }  
  Go to the global settings to adjust the order in which product videos appear in pop-ups

- :lucide-video:{ .lg }  
  [__Sync Product Videos to the Meta Catalog__](../../integrations/fb/meta-ads/sync-product-videos-meta-catalog.md){ title="Sync Product Videos to the Meta Catalog" }  
  Sync videos to the Meta catalog and create catalog ads

</div>

## FAQ
??? quote "Why don't my product videos have sound?"
    Product videos do not currently support audio output, so videos play muted.

??? quote "What should I do if a video upload fails?"
    - Check whether the video file is larger than 30 MB.
    - Make sure the video format is MP4.
    - If you still can't upload it, contact customer support.

??? quote "Can product videos appear only with the drag-and-drop theme?"
    Yes. Product videos are supported only in the drag-and-drop theme. Other themes cannot display videos.

??? quote "Can I change the order in which videos appear in pop-ups?"
    Yes. After uploading, you can set pop-up videos to appear in the first or last position in the admin.
    
