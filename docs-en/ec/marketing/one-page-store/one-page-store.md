---
title: "Event Page"
description: "An Event Page puts product details, features, and checkout on a single page. It cuts drop-off from page switching and is an effective way to raise ad conversion and improve mobile shopping."
created: 2026-02-11 00:00
last_modified: 2026-06-30 10:56
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：文字編輯器、拖拉版型
  - 商品狀態：開賣通知 vs 未公開已下架商品
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 行銷活動
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 建立一頁式活動頁面
  - 設計自訂版面區塊
  - 配置活動商品與順序
  - 設定優惠倒數催單
features:
  - 一頁式商店
  - 網頁鎖右鍵
prerequisites:
  - "需準備欲推廣的商品與活動圖文素材.en"
related:
  - ec/website-appearance/theme-and-layout/theme-editor.en/
  - ec/website-appearance/code-customization/text-editor.en/
  - ec/profit-sharing/query-profit-sharing-partners-and-codes.en/
  - ec/profit-sharing/referrer-profit-sharing.en/
tags:
  - "Conversion Optimization"
  - "Single-Page Design"
  - "Ad Landing Page"
  - Multi-Country
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 行銷活動 > 一頁式商店
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=2076
  - https://www.cyberbiz.io/support/?p=1701
permalink: "https://help.cyberbiz.io/ec/marketing/one-page-store/one-page-store.en/"
comments: false
search:
  exclude: false
icon: lucide/file-text
hide: []
---
# Event Page (One-Page Store)

An Event Page (one-page store) puts product information, features, and checkout on a single page. Fewer page changes mean fewer drop-offs, making it an effective tool for ad conversions and mobile shopping.
{ .subtitle }

[:lucide-tag:{ title="適用方案" }](../../../resources/conventions#適用方案) | All PLUS / Enterprise
{ .doc-badge }

![](../../../assets/images/EC-後台-行銷活動-一頁式商店-畫面總覽01.png){ .hero-page }

!!! info "Version Differences"
    - On PLUS plans, Event Page is an add-on module (choose 2 of 11). Make sure you have selected this module before using it. Enterprise includes it by default.

!!! tip "Use Cases"
    - **Best-seller promotions**: Build a dedicated landing page for one star product or a limited-time bundle to focus on conversions.
    - **Holiday flash sales**: For events like 11.11 or Mother's Day, run promotions on a separate page without affecting your main store.
    - **KOL and affiliate promotion**: Create page links with affiliate codes to track sales from specific influencers or channels.


## Before You Start

Before you build, understand these limits and system rules:

- **Page limits**:
    - **Expert**: Up to 10 pages.
    - **Enterprise / PLUS add-on**: Unlimited pages.
- **Cart limits**: **Multiple carts aren't supported**. All products on a one-page store check out in the same cart.
- **temperature zone rules**: All products on a page must use the **same temperature zone**. Mixing products from different temperature zones blocks checkout.


## Steps

### Step 1: Create A Page

1. Log in to the CYBERBIZ admin and go to **Marketing > Event Page**.
2. Click **Add Page** in the top-right corner.
3. Fill in the following:
    - **Page Title**: A name to identify the promotion.
    - **URL Keyword**: A custom URL path (such as `spring-sale`).
    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-新增一頁式商店01.png)

4. Choose a **drag-and-drop theme** or a **classic theme**.
    - We recommend the **drag-and-drop theme** for the best cross-device layout and design flexibility.
    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-新增一頁式商店02.png)

### Step 2: Complete Basic Settings

On the **Basic Settings** tab of the edit page, set up the URL, visuals, and schedule:

1. Basic information

    - **URL and tag**: Customize the page URL keyword and the tag used to identify it in the admin.
    - **Search visibility**: To keep the page out of search engines (such as a private employee sale), set "Page Search" to Not Searchable. The system adds a noindex tag automatically.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-基本設定-活動內容設定01.png)

2. Navigation bar and visuals

    - **Logo and link**: Upload a logo for the Event Page and set where clicking it goes.
    - **Navigation bar background**: Set the color of the top navigation bar. Match your brand or promotion theme.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-基本設定-導覽列設定01.png)

3. Schedule and urgency tools

    - **Promotion period**: Set when the page opens and closes automatically.
    - **Pinned announcement**: Show important notices at the top of the page (such as free shipping over NT$1,000 or gifts remaining).

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-基本設定-活動時間設定置頂活動訊息01.png)

4. Discount countdown

    - Set a **fixed end time** or a repeating countdown of **N days after the first visit**.

    !!! info "How the Countdown Works"
        The countdown timer creates urgency. When it ends, products are **not** unlisted automatically, and customers can still order.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-基本設定-優惠時間倒數01.png)

5. SEO
    - **Page title and description**: Use precise keywords and a clear description to rank better on search engines like Google.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-基本設定-SEO設定01.png)

### Step 3: Add Products

=== "Drag-and-Drop Theme"

    1. Go to the **Page Settings / Sales Content Settings** tab.
    2. Click **Add Block** and choose **Product List**.
    3. Click **Product List** to edit it, then click **Add Product** in the **Select Products** section.
    4. In the pop-up, filter and select the products to sell, then click **Confirm Add**.
    5. Click **Manage** and drag the :lucide-grip-vertical: icon to reorder products on the storefront.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-新版-選擇商品01.gif)

=== "Classic Theme"

    1. Go to the **Select Products** tab.
    2. Filter and select the products to sell, then choose **Add to Promotion** in the `Select...下拉選單`.
    3. Drag the :lucide-move: icon to reorder products on the storefront.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-舊版-選擇商品01.png)

!!! info "Product Status Rules"
    Only **listed and published** products can be added. Unpublished or unlisted products can't.


### Step 4: Design The Product List Layout

=== "Drag-and-Drop Theme"

    1. Go to the **Page Settings / Sales Content Settings** tab.
    2. Click **Add Block** and choose the **Product List** you created.
    3. Click **Product List** to edit it.
    4. **Enter a group title**: Enter the block name in the **Title** field (such as Best Sellers or Limited-Time Add-Ons) to separate product types.
    5. **Choose how products expand**:
        - **Expand down**: Products are listed from top to bottom. Use this for many products so all are shown.
        - **Swipe sideways**: Shows up to four products at once; customers swipe to see more. Good for add-ons or recommendations to save vertical space.
    6. **Set product alignment**: When products don't exceed the limit (3 on desktop, 2 on tablet, 1 on mobile), choose the alignment. The default is **Left**.
    7. **Customize layouts by device**:
        - **Columns**: Set products per row separately for **desktop/tablet** and **mobile**.
        - **Margins**: Set **side margins** and **bottom margins** separately for **desktop/tablet** and **mobile** so content isn't crowded or uneven.
        - **Desktop category style**: Choose **Default**, **Show Partial Content**, or **Show All** to control how much product information appears.
    8. **Choose an image hover effect**: Add an effect when customers hover over a product image to encourage clicks.

        | Effect | Appearance and Tips |
        | ------- | ------------- |
        | **Quick Add to Cart button** | A buy button appears on the image, shortening the path to purchase |
        | **Image swap** | Switches to the second product image (such as a detail or lifestyle shot) to show more |
        | **Shadow border** | Adds a shadow so the product stands out and draws attention |
        | **Zoom** | Slightly enlarges the image for a refined, premium feel |

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-新版-設定商品列表佈局01.png)

=== "Classic Theme"

    1. Go to the **Product Settings** tab.
    2. **Customize sales copy**:
        - **Promo text next to products**: Enter a short promo phrase (such as "Special offer, buy now"). It appears next to the product name.
        - **Sale text**: Customize the sale label (such as "On Sale Now") to highlight the price.
    3. **Choose a product view**: Pick the best layout for your number of products and amount of detail.

      | View | Storefront Look | Best For |
      | ------- | ----------- | ----------- |
      | List view | Large images stacked vertically | A single featured product or products that need detailed images and text |
      | Grid view | Two side by side, saving vertical space | Many items (such as multiple colors or bundles) that customers scan quickly |

    4. **Set the product list theme color**:
        - **Theme color**: Sets the color of the **Buy Now** button, promo text, and prices.
        - **Content background color**: Sets the background of the product information area for visual contrast.
    5. **Set automatic options**:
        - Product summary: When ON, the **product description** is also shown.
        - Prefill cart: When ON, **all products** in the list are added to the cart as soon as customers open the page.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-舊版-設定商品列表佈局01.png)


### Step 5: Design The Page Layout And Content

=== "Drag-and-Drop Theme"

    1. Go to the **Page Settings / Sales Content Settings** tab.
    2. Click **Add Block** and choose a block style.

         > For how to use blocks, see [Drag-and-Drop Theme Guide](../../website-appearance/theme-and-layout/theme-editor.md).
    3. Click **Color Settings** to adjust the color scheme.

        !!! warning "Affects the Whole Site"
            Color changes here apply to your whole site. Check that colors stay consistent before changing them.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-新版-新增區塊元素01.png)

=== "Classic Theme"

    1. Go to the **Sales Content Settings** tab.
    2. **Add content blocks**: Click to add blocks as needed.

        - Insert image: Upload product images or marketing posters.
        - Insert video: Paste a YouTube link.
        - Insert text: Use the [text editor](../../website-appearance/code-customization/text-editor.md) to write product descriptions, specs, or your brand story.
        - Insert Buy Now button: Customize the button text (such as "Buy Now" or "View Details") to drive conversions.
    3. **Reorder blocks**: Drag the :lucide-move: icon to change the order of blocks.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-舊版-新增區塊元素01.png)


### Step 6: Set The Promotion Policy (Enterprise Only)

1. Go to the **Marketing Activity Settings** tab.
2. Choose the promotion policy for the Event Page.
  - **Sync storewide promotions**: The Event Page uses the same promotions as your online store.
  - **Customize Marketing Activities**: Add threshold gift or quantity gift promotions just for this Event Page.

!!! info "Gift Notes"
    - **Variant limits**: Gifts can only be linked by **product**, not by a specific **variant**.
    - **Priority**:
        - If you set several gifts, they're sent in order **from top to bottom**.
        - When the top gift is out of stock, the next gift is sent, and so on.
    - **Item limit**: Each promotion can have up to **10** gift options.

![](../../../assets/images/EC-後台-行銷活動-一頁式商店-行銷活動設定01.png)

## Advanced Uses

### 1. Create Affiliate Referral Links

Event Pages work with affiliate commissions. When customers click a URL with a referral code, the code is added to their cart automatically.

- **Original URL**: `https://store.com/events/spring-sale`
- **Referral code suffix**: `?rcode=[推薦碼]`
- **Referral code**: `abc123`
- **Final link**: `https://store.com/events/spring-sale?rcode=abc123`

> :lucide-info: [Look up an affiliate partner's referral code](../../profit-sharing/query-profit-sharing-partners-and-codes/#任務四一鍵複製推薦碼)

### 2. Disable Right-Click

To keep page images from being easily downloaded, paste a right-click blocking script into a **Custom HTML** block:


=== "Drag-and-Drop Theme"

    1. Go to the **Page Settings / Sales Content Settings** tab.
    1. Create a **Custom HTML** block and click Edit.
    2. Switch to **Source Code** mode.
    3. Paste the code and save.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-新版-貼上鎖右鍵腳本01.gif)

=== "Classic Theme"

    1. Go to the **Sales Content Settings** tab.
    2. Choose **Insert Text** and click **Edit Content**.
    3. Switch to **Source Code** mode.
    4. Paste the code and save.

    ![](../../../assets/images/EC-後台-行銷活動-一頁式商店-舊版-貼上鎖右鍵腳本01.gif)

```
<style type="text/css">
*:not(input):not(textarea) { 
-webkit-touch-callout:none;
-webkit-user-select:none;
-khtml-user-select:none; 
-moz-user-select:none;
-ms-user-select:none; user-select:none; } 
</style> 
<script> 
(function () { 
function stopEvent(event) { 
event.preventDefault(); 
event.stopPropagation(); }
['dragstart', 'selectstart', 'contextmenu'].forEach(function(event) { document.addEventListener(event, stopEvent);
}); } )();
</script>
```

### 3. Turn On Product Launch Times

The storefront shows a countdown to each product's launch to build anticipation and engagement.

- How to enable: Go to **Marketing > Event Page** and turn on **Product Launch Time Settings** on the right of the list.
- Applies to:
    - All products that are **not yet listed** show the countdown.
    - Whether a product is **published** or **unpublished**, the countdown shows until its listing time.


!!! info "Plan and Theme Availability"
    - This feature is available on **Enterprise** only.
    - It only works for Event Pages built with a **drag-and-drop theme**.

![](../../../assets/images/EC-後台-行銷活動-一頁式商店-商品開賣時間設定01.png)


## FAQ

??? quote "Why do customers see **No shipping method found** at checkout?"
    This usually happens when the page mixes products from different temperature zones (such as room-temperature cookies and frozen ice cream). One order can't handle multiple temperature zones, so make sure all products on the page use the same temperature zone.

??? quote "What if I reach the page limit?"
    If you're on Expert and have reached 10 pages, delete expired pages or contact support to upgrade to PLUS for unlimited pages.

??? quote "Can customers still buy after the countdown ends?"
    Yes. The countdown is only a visual urgency tool and doesn't unlist products. To stop selling, set the page to **Unpublished** manually.

---

## Further Reading

<div class="grid cards" markdown>

- :lucide-layout-template:{ .lg }
  [__Drag-and-Drop Theme Basics__](../../website-appearance/theme-and-layout/theme-editor.md)
  Learn to use each design element in the editor.

- :lucide-users:{ .lg }
  [__Set Up Referral Commissions__](../../profit-sharing/referrer-profit-sharing.md)
  Learn how to combine Event Pages with affiliate commissions to grow sales.

</div>
