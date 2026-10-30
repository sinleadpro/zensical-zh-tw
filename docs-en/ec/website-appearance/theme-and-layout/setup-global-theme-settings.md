---
title: "Global Settings"
description: "Set up site-wide settings for drag-and-drop themes, including pop-up ads, colors, brand identity, SEO, product display behavior, and dynamic labels."
created:
last_modified: 2026-10-21 14:00
lang: en-US
permalink: "https://help.cyberbiz.io/ec/website-appearance/theme-and-layout/setup-global-theme-settings/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
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
  - 設定全站共用設定
  - 自訂官網外觀
  - 管理商品顯示行為
  - 設定彈窗廣告
  - 優化網站SEO
features:
  - 全站共用設定
  - 彈窗廣告
  - 導覽列與頁腳
  - 顏色設定
  - SEO 設定
  - 商品顯示設定
  - 動態標籤
  - 品牌識別
prerequisites:
  - 已使用拖拉版型
  - 後台管理員權限
related:
  - ec/website-appearance/theme-and-layout/theme-editor/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/marketing/other-tools/interactive-games/
  - ec/website-appearance/theme-and-layout/configure-scheduled-carousels/
  - ec/website-appearance/theme-and-layout/setup-theme-page-settings/
  - ec/website-appearance/site-settings/setup-og-image/
  - ec/website-appearance/site-settings/setup-site-title-seo/
  - ec/website-appearance/site-settings/setup-right-click-protection/
  - ec/products/create-and-manage/edit-product-slogan-and-description/
  - ec/products/create-and-manage/product-swatches-variant-images-drag-drop/
  - ec/products/create-and-manage/setup-product-videos/
  - ec/products/categories-and-tags/manage-product-tags/
  - ec/website-appearance/references/theme-editor-sections/
tags:
  - "Drag-and-Drop Themes"
  - "Global Settings"
  - "Pop-Up Ads"
  - "Color Settings"
  - SEO
  - "Product Display"
  - "Dynamic Labels"
acoiv:
apis:
devices:
  - desktop
  - tablet
  - mobile
ui_components: []
paths:
  - 網站外觀 > 套版主題管理
layouts:
  - draggable
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-appearance/theme-and-layout/setup-global-theme-settings/"
comments: false
search:
  exclude: false
icon: lucide/settings-2
hide:
---

![Global settings](../../../assets/images/ec-網站外觀-拖拉版型-全域設定.en.png){ .hero-page }

## About Global Settings { #intro-global-settings }

Global settings don't belong to a single page. They apply to your **entire website**. At the bottom of the left panel in the drag-and-drop theme editor, you can click the navigation bar, pop-up ads, footer, color settings, and site-wide settings directly. There's no separate "Global Settings" button to click first.

Global settings are in the drag-and-drop theme editor. To learn how to open the editor, see [Drag-and-Drop Theme Site Settings](theme-editor.md){ title="Drag-and-Drop Theme Site Settings" }.

## Prerequisites and Limitations { #prerequisites-global-settings }

Before you start, make sure that:

- [x] **The drag-and-drop theme editor is open:** Open the drag-and-drop theme editor first. See [Open the Drag-and-Drop Theme Editor](theme-editor.md#operate-theme-editor-enter){ title="Open the Drag-and-Drop Theme Editor" }.
- [x] **You're using a drag-and-drop theme:** The settings in this article apply only to themes labeled "draggable."

!!! plan "Differences by Plan"
    Some settings (such as color settings) don't appear on the POS-only plan. The items you see depend on your plan and the features you have turned on.

---

## Navigation Bar and Footer { #operate-global-settings-navbar-footer }

The navigation bar and footer have more settings and are covered in a separate article:

<div class="grid cards" markdown>

- :lucide-menu:{ .lg }  
  [__Navigation Bar__](../navigation/setup-menus-navigation.md){ title="Set Up Menus and the Navigation Bar" }  
  Set the menu layout (default / side-by-side left / side-by-side right), whether the background is transparent, and whether submenus expand together.

- :lucide-arrow-down-to-line:{ .lg }  
  [__Footer__](../navigation/setup-menus-navigation.md#operate-menus-nav-footer-content){ title="Set Up Menus and the Navigation Bar" }  
  Choose a "top and bottom" or "left and right" layout, and turn on social media icons and their links.

</div>

---

## Pop-Up Ads { #operate-global-settings-popup }

Pop-up ads open automatically when customers visit your store. In global settings, you can choose one of the following content types and set display conditions:

1. At the bottom of the editor's left panel, click "Pop-Up Ad."
2. Choose the pop-up content type:

![Pop-up ad](../../../assets/images/ec-網站外觀-拖拉版型編輯器-彈窗廣告.en.png)

=== "Image Pop-Up"

    1. Upload desktop, tablet, and mobile images. (The desktop image is required. If you don't upload tablet or mobile images, the desktop image is used.)
    2. Set the **thumbnail size** (small / medium / large) to control the size of the small icon after the pop-up is minimized. If you don't upload one, the desktop image is used by default.
    3. Set the **image link** to go to a specific page or URL when the pop-up is clicked.
    4. To let customers open the link without leaving your website, select "Open link in new tab."

    ![Pop-up ad - image](../../../assets/images/ec-網站外觀-拖拉版型編輯器-彈窗廣告-圖片顯示.en.png)

    ??? note "How the Pop-Up Shows and Minimizes"
        Image pop-ups don't have a "display frequency" field. The system handles display automatically: the pop-up opens when customers visit, and after a customer minimizes it, it stays minimized for **24 hours**. Pop-ups don't appear on the cart or checkout pages.

        ![Pop-up ad - image minimized](../../../assets/images/ec-網站外觀-拖拉版型編輯器-彈窗廣告-圖片收合.en.png)

=== "Video Pop-Up"

    1. Paste a YouTube video link.
    2. Press ++enter++ to apply the change.

    ![Pop-up ad - video](../../../assets/images/ec-網站外觀-拖拉版型編輯器-彈窗廣告-影片.en.png)

=== "Interactive Game"

    1. Choose a "Spin the Wheel" or "Red Envelope Draw" game you created from the drop-down menu.
    2. Go to the [interactive games setup guide](../../marketing/other-tools/interactive-games.md){ title="Interactive Games (EC)" } to create a Spin the Wheel or Red Envelope Draw campaign.

    !!! info "Participation Restrictions"
        This feature is for website members only. Customers must sign in to take part.

    ![Pop-up ad - interactive game](../../../assets/images/ec-網站外觀-拖拉版型編輯器-彈窗廣告-互動遊戲.en.png)

=== "Scheduled Carousel"

    1. Choose the carousel content to load from the "Carousel Advanced Settings" group.
    2. Go to the [scheduled carousel setup guide](configure-scheduled-carousels.md){ title="Create and Manage Scheduled Carousels" } to set publish and unpublish times for ad campaigns.

    ![Pop-up ad - scheduled carousel](../../../assets/images/ec-網站外觀-拖拉版型編輯器-彈窗廣告-排程跑馬燈.en.png)

---

## Color Settings { #operate-global-settings-color }

Define the basic visual elements for your whole website:

1. At the bottom of the editor's left panel, click "Color Settings."
2. Choose a **primary color** to change the main color across your website.
3. Choose an **accent color**. The system applies it to several dynamic UI elements automatically (see below).
4. Adjust the **site-wide font color**.

![Color settings](../../../assets/images/ec-網站外觀-拖拉版型-顏色設定.en.png)

??? info "Where the Accent Color Applies"
    After you choose an "accent color" in color settings, the system applies it automatically to:

    - **Product labels:** Including the **subscription**, **sale**, and **out of stock** labels the system shows automatically, and your **5 custom labels**.
    - **Sale countdown:** If a product isn't on sale yet, the **countdown background color** on the storefront product page or collection list uses the accent color automatically.
    - **Order:** Labels appear from left to right in a set order (subscription > sale > out of stock > custom labels), all in the accent color.

??? note "Color Settings for Specific Blocks"
    Besides the site-wide colors, some blocks let you customize colors in more detail:

    - **[Pinned Post](../navigation/setup-menus-navigation.md#operate-menus-nav-announce){ title="Set Up Menus and the Navigation Bar" }:** Set the pinned post's **image link background color** and the **countdown text and background colors** separately.
    - **[Collapsible Content](setup-theme-page-settings.md#operate-page-settings-collapsible){ title="Page Settings Guide" }:** A block used for FAQs or shopping notes. You can set its display colors separately.
    - **[Image and Text](setup-theme-page-settings.md#operate-page-settings-graphic-intro){ title="Page Settings Guide" }:** You can customize the **button color** in this block.

---

## Site-Wide Settings { #operate-global-settings-shop }

Manage your website's core settings in one place, including its visual identity, search engine optimization (SEO), global product display behavior, and site protection.

### Visual Identity and Brand Assets { #brand }

1. In "Site-Wide Settings," set the **website icons**:
    - Upload a **favicon**, the small icon shown on the browser tab.

        ![Site-wide settings - favicon](../../../assets/images/ec-網站外觀-全站設定-favicon.en.png)

    - Upload an **OG image** (the default image for shared links) to set the default thumbnail shown when your website links are shared on Facebook or LINE. [See the setup guide](../site-settings/setup-og-image.md){ title="Set Up the Shared Link Thumbnail (OG Image)" }
    
        ![Site-wide settings - OG image](../../../assets/images/ec-網站外觀-全站設定-og-image.en.png)

2. Choose a **navigation bar icon** style (3 built-in styles), or upload your own icon file.

    ![Site-wide settings - navigation bar icons](../../../assets/images/ec-網站外觀-全站設定-navbar-icon.en.png)

    ??? info "One-Page Store Limitation"
        Custom navigation bar icons are supported only for one-page stores created **after July 2025**.

3. In "Font Settings," choose the font style for your whole website.

    ![Site-wide settings - font settings](../../../assets/images/ec-網站外觀-全站設定-fonts.en.png)

4. Set the **homepage entrance animation**:

    1. Find the **homepage entrance animation** setting and select it to turn it on.
    2. Choose an animation style from the drop-down menu:

        === "Rise and Fade In"

            ![](../../../assets/images/EC-後台-套版主題管理-全站設定-首頁進場動畫01.en.gif)

            - **Animation effect**: Blocks gently float up from below and fade in as they enter the screen
            - **Recommendation**: The most versatile effect. It doesn't distract from reading and suits most homepage blocks.

        === "Expand from Center"

            ![](../../../assets/images/EC-後台-套版主題管理-全站設定-首頁進場動畫02.en.gif)

            - **Animation effect**: Content expands outward from the center as the page scrolls.
            - **Recommendation**: More visual impact. Suits image-focused layouts.


    ??? quote "Why don't some blocks animate in "Expand from Center" mode?"

        Not every block uses it. Some blocks are harder to read with "Expand from Center," so the system doesn't animate them. Support by block:

        | Homepage block | Rise and Fade In | Expand from Center |
        | ------- | -------- | ------- |
        | Image and text | ✓ | ✓ (image area only, not text) |
        | Custom layout design | ✓ | ✓ |
        | Banner ad | ✓ | ✓ |
        | Carousel | ✓ | ✓ |
        | Video settings | ✓ | ✓ |
        | Product collection | ✓ | ✕ |
        | Featured product | ✓ | ✕ |
        | Text editor | ✓ | ✕ |
        | Collapsible content | ✓ | ✕ |
        | Tabs | ✓ | ✕ |
        | Custom HTML | ✕ | ✕ |

    ??? quote "I turned on animation, but I don't see it on my computer or phone. Why?"

        If your device has the accessibility setting **Reduce Motion** turned on, your website turns off animation automatically and shows content directly. This is expected behavior, not a bug.

        To see the animation, turn off that setting:

        - **Mac**: System Settings > Accessibility > Display > turn off "Reduce Motion"
        - **iPhone/iPad**: Settings > Accessibility > Motion > turn off "Reduce Motion"
        - **Windows**: Settings > Accessibility > Visual effects > turn on "Animation effects"


---

### Website SEO and Protection { #specs-global-settings-seo }

1. In "Site-Wide Settings," enter your website's **title**, **description**, and **keywords** to improve how search engines index and rank your website. If you leave the title blank, the system uses your store name as the title. [See the setup guide](../site-settings/setup-site-title-seo.md){ title="Set Up the Website Title and SEO" }

    ![Site-wide settings - website SEO](../../../assets/images/ec-網站外觀-全站設定-網站seo.en.png)

2. To protect your original content, select **"Disable Right-Click"** to stop visitors from downloading images or copying text with a right-click. [See the setup guide](../site-settings/setup-right-click-protection.md){ title="Disable Right-Click to Protect Images and Text" }

    ![Site-wide settings - right-click lock](../../../assets/images/ec-網站外觀-全站設定-右鍵鎖定.en.png)

---

### Global Product Display Behavior { #operate-global-settings-shop-product }

!!! plan "Feature Limitations"
    Some features require specific plans. These are noted in each item's title.

These settings **apply to every product list and product page on your website** (homepage product blocks, product collection pages, multi-level categories, search pages, product detail pages, and more). They keep product cards and prices consistent, so you don't have to set each product individually. For related settings, see [Basic Display Options](#operate-global-settings-product-display-basic), [Layout and Style Settings](#operate-global-settings-product-layout), and [Images and Hover Effects](#operate-global-settings-product-image-effects).

#### Basic Display Options { #operate-global-settings-product-display-basic }

Turn on the following as needed:

- **Show product taglines:** Show product features or promotional taglines below the product image or name. [See the setup guide](../../products/create-and-manage/edit-product-slogan-and-description.md){ title="Edit Product Summaries and Taglines" }

    ![Show product taglines](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-顯示商品標語.en.png)

- **Show product color swatches `Enterprise`:** Show small variant color images on product collection pages and multi-level category pages. [See the setup guide](../../products/create-and-manage/product-swatches-variant-images-drag-drop.md){ title="Set Up Product Color Swatches and Variant Images (Drag-and-Drop Themes)" }

    ![Show product color swatches](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-顯示商品色票小圖.en.png)

- **Show quantity sold:** Show the total quantity sold below the product name to build a sense of popularity.

    ![Product display behavior - quantity sold](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-顯示商品已銷售數量.en.png)

- **Show product sale start time `PLUS / Enterprise`:** When a product has a publish time but isn't on sale yet, the storefront shows a countdown to the sale (except on the Bonus Mall page).

    ![Product display behavior - sale start time](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-顯示商品開賣時間.en.png)

- **Show product price range:** When variants have different prices, the sale price shows as a "lowest–highest" range and the list price is hidden. If this is off, the lowest sale price and the list price are shown.

    ![Product display behavior - price range](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-顯示商品價格區間.en.png)

    !!! warning "Important"
        This doesn't apply to product pages with "Select the first variant by default" turned on, product pop-ups, or homepage featured products.

---

#### Layout and Style Settings { #operate-global-settings-product-layout }

- Choose the **Text Alignment** (left / center / right; left by default).

    === "Left"
        ![Text alignment - left](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-文字排列-置左.en.png)
    === "Center"
        ![Text alignment - center](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-文字排列-置中.en.png)
    === "Right"
        ![Text alignment - right](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-文字排列-置右.en.png)

- Choose the **variant menu** style (drop-down / buttons; buttons by default).

    === "Buttons"
        ![Buttons](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品款式選單-按鈕式.en.png){ title="Product variant menu - buttons" }
    === "Drop-Down"
        ![Drop-down](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品款式選單-下拉式.en.png){ title="Product variant menu - drop-down" }

- Set whether the **product video** appears before or after the product images `PLUS / Enterprise`. [See the setup guide](../../products/create-and-manage/setup-product-videos.md){ title="Set Up Product Videos" }

    ![Product video display order](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品影片顯示順序.en.png)

- Set the **maximum purchase quantity**, the maximum number of each variant that can be added to the cart (leave it blank or enter 0 for no limit).

    ![Maximum purchase quantity](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品購買數量上限.en.png)


---

#### Images and Hover Effects { #operate-global-settings-product-image-effects }

- Choose the **image aspect ratio** (1:1 / 3:4; 1:1 by default).

    === "1:1"
        ![Image aspect ratio - 1:1](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-圖片寬高比例-1比1.en.png)

    === "3:4"
        ![Image aspect ratio - 3:4](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-圖片寬高比例-3比4.en.png)

- Choose a **product image hover effect**:

    === "Quick Add to Cart Button"
        ![Quick add to cart button](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品圖懸停效果-加入購物車.en.png){ title="Product image hover effect - add to cart button" }
    === "Image Swap"
        ![Image swap](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品圖懸停效果-圖片切換.en.png){ title="Product image hover effect - image swap" }
    === "Shadow and Border Highlight"
        ![Shadow and border highlight](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品圖懸停效果-陰影邊框.en.png){ title="Product image hover effect - shadow and border" }
    === "Zoom"
        ![Zoom](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品圖懸停效果-放大效果.en.png){ title="Product image hover effect - zoom" }

- Set the **product image corner radius**. We recommend 0–20px.

    ![Product image corner radius](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品圖圓角.en.png)

[^1]: And when the "Product Labels" feature isn't in use.

---

### Product Label Stickers { #operate-global-settings-product-labels }

=== "Professional (incl. PLUS), Advanced (incl. PLUS), Expert"

    - **Show subscription campaign labels**: Shown automatically when a product is linked to a subscription campaign.
    - **Discount stickers (sale labels)**: Shown automatically when the sale price of any variant is lower than the list price. If you select **Show subscription campaign labels**, this setting doesn't apply.
    - **Image aspect ratio**: Choose the display ratio that matches the product images you upload. (If some products have blank space above and below, try changing the display ratio.)

    ![Discount stickers](https://www.cyberbiz.io/support/wp-content/uploads/拖拉版型-功能介紹13.png)


=== "Expert PLUS, Enterprise"


    #### Label Types and Supported Plans { #specs-global-settings-product-labels-types }

    | Label type | Supported plans | Number allowed | Style options |
    | ------- | ------- | ---------- | ------- |
    | **Discount Label** | Expert PLUS<br>Enterprise | 1 | Image<br>Text<br>Discount rate |
    | **Out-of-Stock Label** | Expert PLUS<br>Enterprise | 1 | Image<br>Text |
    | **Periodic Event Label** | Expert PLUS<br>Enterprise | 1 | Image<br>Text |
    | **Custom labels** | Enterprise | Up to 30<br>Up to 5 labels per product[^2] | Image<br>Text |

    #### Application Rules { #specs-global-settings-product-labels-rules }

    | Label type | Application rule | Label category | Description |
    | ------- | ------- | ------- | ------- |
    | **Discount Label** | Shown when the sale price of any variant is lower than the list price | Default label | Can be set to public / private<br>Can't be added or deleted |
    | **Out-of-Stock Label** | Single-variant products: shown when stock is 0 and the product is set to stop selling at 0 stock<br>Multi-variant products: shown only when every variant has 0 stock and is set to stop selling at 0 stock | Default label | Can be set to public / private<br>Can't be added or deleted |
    | **Periodic Event Label** | Shown automatically when the product is linked to a subscription campaign | Default label | Can be set to public / private<br>Can't be added or deleted |
    | **Custom labels** | A custom label must be linked to a product tag in the admin. After you link it, the custom label applies automatically to every product with that product tag<br> [See the setup guide](../../products/categories-and-tags/manage-product-tags.md){ title="Manage Product Tags" } | Custom label | Can be set to public / private<br>Can be added or deleted |


    #### Steps { #operate-global-settings-product-labels-step }

    1. In "Site-Wide Settings," click **Product Label List** to open the settings page.

        ![Product label list](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品標籤列表-入口.en.png)

    2. [Turn on](theme-editor.md#operate-theme-editor-visibility){ title="Drag-and-Drop Theme Site Settings" } the label types you need:

        ![Product label list](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品標籤列表.en.png)

    3. Click an item in the label list to open its settings page and choose a **display style** for each label:

        - **Text:** Enter the label text you want to show.
        - **Image:** Upload a label image and choose the image label size (**large / small**).
        - **Discount Rate:** Available only for the "Discount Label." Shows the discount automatically based on the sale price and list price.

        === "Text"
            ![Text](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品標籤呈現方式-文字.en.png)

        === "Image"
            ![Image](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品標籤呈現方式-圖片.en.png)

        === "Discount Rate"
            ![Discount rate](../../../assets/images/ec-網站外觀-拖拉版型編輯器-全站設定-商品標籤呈現方式-折扣折數.en.png)

    !!! info "The label background uses the accent color from "[Color Settings](#operate-global-settings-color)" by default. When several labels apply at once, they appear side by side in a fixed system order."

    [^2]: If there are more than 5, the storefront shows only the first 5 in order. The 6th and later aren't shown. This limit counts only custom labels. System default labels (sale, out of stock, subscription) don't count toward it, and a product can show both. For example, if a product qualifies for 3 system default labels and 6 custom labels, the storefront shows the 3 default labels plus the first 5 custom labels, 8 in total.

---

## Next Steps { #next-steps-global-settings }

<div class="grid cards" markdown>

- :lucide-palette:{ .lg }  
  [__Drag-and-Drop Theme Site Settings__](theme-editor.md){ title="Drag-and-Drop Theme Site Settings" }  
  Learn how to open the drag-and-drop theme editor and set up your website

- :lucide-menu:{ .lg }  
  [__Set Up Menus and the Navigation Bar__](../navigation/setup-menus-navigation.md){ title="Set Up Menus and the Navigation Bar" }  
  Set the menu layout and footer display

- :lucide-gamepad-2:{ .lg }  
  [__Interactive Games (EC)__](../../marketing/other-tools/interactive-games.md){ title="Interactive Games (EC)" }  
  Create Spin the Wheel or Red Envelope Draw campaigns

- :lucide-images:{ .lg }  
  [__Create and Manage Scheduled Carousels__](configure-scheduled-carousels.md){ title="Create and Manage Scheduled Carousels" }  
  Set publish and unpublish times for ad campaigns

</div>

## References { #reference-global-settings }

- [Block Types You Can Add Reference](../references/theme-editor-sections.md)
