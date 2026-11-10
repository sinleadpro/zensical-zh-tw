---
title: "Edit the Product Brief and Product Slogan"
description: "Customize the text style of the product slogan and product brief and edit product copy."
created: 2026-01-08 00:00
last_modified: 2026-07-22 17:25
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - verify FAQ
  - update internal links
  - update 產品頁文字修改09
  - add 樣板編輯器
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 商品
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
  - 如何客製化商品簡述文字樣式
  - 如何客製化商品標語文字樣式
  - 如何修改商品文案
features:
  - 商品簡述與標語個別樣式修改
  - 全站 CSS 樣式調整
  - HTML 語法編輯支援
  - 開發人員工具應用
  - 樣板編輯器
  - 版本回溯功能
prerequisites: []
related:
  - ec/website-appearance/code-customization/restore-code-theme-editor/
tags:
  - CSS
  - HTML
  - "Product Page"
  - "Text Style"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 商品 > 所有商品
  - 網站外觀 > 套版主題管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1060
  - https://www.cyberbiz.io/helpcenter/?p=3545
  - https://www.cyberbiz.io/support/?p=16893
permalink: "https://help.cyberbiz.io/ec/products/create-and-manage/edit-product-slogan-and-description/"
comments: false
search:
  exclude: false
icon: lucide/align-left
hide: []
---

![Product brief and slogan](../../../assets/images/ec-product-brief-n-slogan.zh-tw.en.png){ title="Product Brief and Slogan" .hero-page }

## About the Product Brief and Product Slogan { #intro-product-slogan }

The product brief and product slogan are text fields shown on the product page to highlight product features and key information. You can customize how the **Product slogan** and **Product brief** text appears on the product page, including the text color, font, size, and line breaks.

??? info-clean "Where They Appear on the Storefront"

    - Product brief: Made with select premium cream cheese and baked at low temperature to lock in the aroma and moist texture. Every bite is smooth and rich with a creamy flavor, with a light sweetness in its gentle tang. Perfect for afternoon tea, birthday parties, or holiday gifts, it is a comforting and elegant dessert choice.
    - Product slogan: Rich and smooth, a taste of happiness that melts in your mouth.

    !!! quote ""
      ![Where the product brief and slogan appear on the storefront](../../../assets/images/ec-product-slogan-product-brief.zh-tw.en.png){ title="Where the Product Brief and Slogan Appear on the Storefront" }


## Prerequisites and Limits { #prerequisites-product-slogan }

- **Theme limits**: The **drag-and-drop theme** may not support some code editing. Follow the features actually available in your admin.
- **Responsibility**: CYBERBIZ provides open code editing access but **does not provide modification guidance, syntax tutorials, or coding services beyond the existing documentation**. We recommend hiring a professional engineer.
- **Recovery**: If a change breaks the layout or causes problems, use the "**View a previous version**" feature in the Template Editor to [restore a previous version](../../website-appearance/code-customization/restore-code-theme-editor.md#operate-restore-theme).
- **Common causes of broken layouts**: Usually an HTML tag is not closed correctly (for example, a missing closing tag `</span>`), which affects how the page displays.
- **Storefront display order**: In some themes, the "Product slogan" and "Product brief" may appear on the storefront in the reverse order of the admin fields.

## Steps { #operate-product-slogan }

You can customize the text style of the product brief and product slogan in the following two ways to keep your brand consistent and strengthen your marketing:

- [Change the text style of individual products](#operate-product-slogan-style): Change the copy style of an individual product
- [Adjust text display site-wide](#operate-product-slogan-global): Change the site-wide CSS file

!!! info "Product Code Priority Rules"
    Code in the product slogan and product brief fields takes **priority** over the site-wide styles in the Template Editor. If you change both the Template Editor and an individual product, the individual product's setting applies.

### Change the Text Style of Individual Products { #operate-product-slogan-style }

Because the "Product slogan" and "Product brief" fields in the admin don't support a formatting editor, you can use the "Product Introduction" editor as a tool to generate the code.

1. **Open the edit page**: Go to "Products" > "All Products" and click the product you want to edit.
2. **Generate the code**:
    - In the "Product Description" editor, change the format from "Normal" to "**Normal (DIV)**".
    - Enter the text you want and set the color, size, bold, and other styles.
    - Click the "**Source**" button in the upper-left corner of the editor.

    ![Generate HTML code](../../../assets/images/ec-generate-text-html-syntax.zh-tw.en.gif){ title="Generate HTML Code" }

3. **Apply the style**:
    - Copy the HTML code that appears, then delete the content in the editor (to keep the product description clean).
    - Paste the copied code into the "**Product slogan**" or "**Product brief**" field above.
    - Click "Save" to see the change on the product page.

    ![Product slogan and brief fields](../../../assets/images/ec-product-slogan-product-brief-fields.zh-tw.en.png){ title="Product Slogan and Brief Fields" }

    !!! info "Code in this field takes **priority over** the Template Editor, so individual settings override site-wide settings."

---

### Adjust Text Display Site-Wide { #operate-product-slogan-global }

!!! warning "Notes on Code Changes"

	- The drag-and-drop theme doesn't support some code editing features. Follow the features available in the admin to avoid ineffective or incorrect changes.
	- You can adjust the code of public themes yourself, but **always back up the original files first**. The Template Editor has a View a previous version feature that lets you [restore a previous version](../../website-appearance/code-customization/restore-code-theme-editor.md).
	- For further customization, hire an experienced engineer to keep the system stable.

To change the slogan or brief color and size for all products on the site at once, you can use CSS.

1. **Find the style code**:
    - On a product page of your website, click "Tools" > "Developer Tools" in the upper-right corner of the browser. Or press ++ctrl+shift+c++ (Windows/Linux) or ++cmd+option+c++ (Mac) to open Developer Tools with element selection mode enabled.  
    - Use the arrow tool to select the text you want to change, then find and copy the matching CSS code in the **Styles** pane at the lower right.

    ![View CSS in Developer Tools](../../../assets/images/ec-check-css-style-shortcut.zh-tw.en.gif){ title="View CSS in Developer Tools" }

2. **Make the change in the admin**:
    - Go to "Website Appearance" > "Theme Setting" > "Select action: CSS/HTML Editor".
    - Open the file **`css/theme_main.css`**.
    - Paste the copied code at the end of the file, then change the color code after `color:` or the value of `font-size:`. You can refer to a [color code chart :material-open-in-new:](https://www.ifreesite.com/color/) to choose a suitable color code.  

    ![CSS editor theme_main.css](../../../assets/images/ec-product-css-editor-theme-main.zh-tw.en.png){ title="CSS Editor theme_main.css" }

3. **Save and preview**: After you save, the text in that position changes color or size for all products on the site.

!!! tip "Recovery"
    If you're not happy with the result, you can [restore a previous version](../../website-appearance/code-customization/restore-code-theme-editor.md).

## FAQ { #faq-product-slogan }
??? quote "Why is the layout of my collection page broken?"
    This is usually caused by an HTML editing error, such as a tag that isn't closed correctly, as in the incorrect example below.

    - :material-check: **Correct**: `<span style="color:black;">Zhejiang flavor, savory and great with rice</span>`
    - :material-close: **Incorrect**: `<span style="color:black;">Zhejiang flavor, savory and great with rice>`
    - :material-fire: **Recommendation**: Have a professional handle HTML issues. CYBERBIZ cannot provide individual assistance.

    ![Broken layout example](https://www.cyberbiz.io/support/wp-content/uploads/2021/12/常見問題跑版.png){ title="Broken Layout Example" .screenshot }

??? quote "Does CYBERBIZ provide help with individual code changes?"
    CYBERBIZ provides only the modification information in the existing documentation and cannot help with code changes beyond it. For further changes, you can contact external design vendors through the [APP MARKET](https://appmarket.cyberbiz.io/category/store_design).
