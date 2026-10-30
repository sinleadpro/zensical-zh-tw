---
title: "Set Up a Cookie Consent Banner"
description: "Generate a cookie consent banner with a third-party tool and paste the code into your theme's theme.liquid to help your store comply with GDPR and EU cookie rules."
created: 2026-07-03 00:00
last_modified: 2026-07-03 15:56
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
  - 網站外觀
sites:
  - TW
audiences:
  - merchant
difficulty: advanced
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 在官網顯示 Cookie 同意提示彈窗
  - 符合 GDPR 與歐盟 Cookie 法規範
  - 在版型中嵌入第三方程式碼
features:
  - Cookie 提示彈窗
  - CSS/HTML 編輯器
prerequisites:
  - 支援程式碼編輯的版型
  - 後台操作權限（外觀編輯權限）
related:
  - ec/website-appearance/theme-and-layout/apply-and-switch-theme/
  - ec/website-appearance/site-settings/business-disclosure/
tags:
  - "Cookie Consent"
  - GDPR
  - "CSS/HTML Editor"
  - theme.liquid
  - "Theme Editing"
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 網站外觀 > 套版主題管理
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-appearance/code-customization/setup-cookie-consent-banner/"
comments: false
search:
  exclude: false
icon: lucide/cookie
hide:
---

![Set up a cookie consent banner](../../../assets/images/cookie-consent-banner-hero.en.png){ .hero-page }

## About the Cookie Consent Banner { #intro-cookie-consent }

To comply with **GDPR privacy rules** and the **EU Cookie Law**, your website needs a privacy policy page. It should also tell shoppers how the website uses cookies when they arrive, and get their consent.

CYBERBIZ websites do not have a built-in cookie consent banner. Instead, generate the banner code with a third-party tool, and then paste it into your theme's "template editor (CSS/HTML editing)" to show the banner on your storefront.

!!! info "Tip"
    This article covers only the basic way to paste the code. The banner's position, text, and style are set by the third-party tool or the code you paste. For more advanced customization, consult someone with a coding background.

---

## Prerequisites and Limitations { #prerequisites-cookie-consent }

Before you start, check these two things:

- [x] **A theme that supports code editing**: This setup requires editing the theme's `theme.liquid` file, so make sure your current theme allows code editing. If you see the **CSS/HTML Editor** option in the theme's "Actions" menu in "Theme Management," it is supported.
- [x] **Admin permissions**: Your account needs admin editing permissions for "Appearance" to open the template editor. A store administrator can assign them in the admin's permission settings.

---

## Steps { #operate-cookie-consent }

The process has two stages: first generate the banner code with a third-party tool, and then go back to the CYBERBIZ admin and paste the code into your theme file.

### Generate the Cookie Consent Banner Code { #operate-cookie-consent-generate }

1. **Go to a generator:** Use a third-party cookie consent banner generator, such as [WebsitePolicies' Cookie Consent Banner generator](https://www.websitepolicies.com/create/cookie-consent-banner).
2. **Set the banner style:** Set the banner's position, layout, text, and colors as needed.
3. **Copy the code:** When you finish, expand the code field and copy the entire code.

!!! info "Third-Party Tool's Official Guide"
    WebsitePolicies offers a complete [guide to adding a cookie consent banner :lucide-external-link:](https://www.websitepolicies.com/support/how-to-add-cookie-consent-banner-to-website). See its official documentation for details on each setting.

---

### Paste the Code into Your Theme { #operate-cookie-consent-paste }

!!! warning "Responsibility for Your Own Code Changes"
    CYBERBIZ makes theme code available for you to adjust freely, but does not offer free code editing or related tutorials. If code you changed yourself causes storefront problems, CYBERBIZ **is not responsible for fixing it**. For help with customization, contact online customer service.

1. **Open Theme Management:** In the left menu of the admin, go to "Website Appearance" > "Theme Management."
2. **Open the CSS/HTML Editor:** On the **Published Theme** tab, click the **Actions** drop-down menu on the current theme card and select **CSS/HTML Editor**.
3. **Agree to the terms of use:** The first time you open it, an **"About Using the Template Editor"** window appears. Select **I have read and agree to the above**, and then click **"I Agree"** to open the editor[^disclaimer].
4. **Open the main template file:** In the **"Layout"** list on the left, click the `theme.liquid` file. Its code loads on the right[^findfile].
5. **Paste the code:** Find the `</head>` line and paste the code you copied in step one **directly above** it.
6. **Save and check:** Click **Save** at the top right. Go back to your storefront and refresh to see the cookie consent banner.

``` html title="theme.liquid" hl_lines="12"
  <!-- for footer --> 
  {{ 'css/footer.css' | cyberbiz_theme_asset_url | stylesheet_tag }}
  <!-- theme assets -->
  {{ 'css/main.css' | cyberbiz_theme_asset_url | stylesheet_tag }}
  <!-- for vendor -->
  {{ 'js/vendor.js' | cyberbiz_theme_asset_url | script_tag }}

  {{ content_for_header }}

  {% section 'color_settings' %}

  <script src="https://cdnapp.websitepolicies.net/widgets/cookies/rnxkuwlv.js" defer></script> <!-- (1)! -->
</head>
```

1.  Paste the cookie consent banner code you copied.

!!! tip "Stores Using "Express Delivery""
    If your store has the "Express Delivery" feature turned on, that page uses a separate theme file. In the "Layout" list, also open `express_delivery.liquid`, paste the code directly above `</head>` in the same way, and save. The cookie banner then also applies to the express delivery page.

[^disclaimer]: The window notes that CYBERBIZ makes theme code available for you to adjust freely, but does not offer free code editing. If your own changes cause problems, use the editor's version control to restore an earlier version.
[^findfile]: When there are many files, type a keyword in the "Find a file?" box at the top left to filter quickly.

---

## Important Rules and Limitations { #specs-cookie-consent }

- **Responsibility for your own code changes**: CYBERBIZ makes theme code available for you to adjust freely, but does not offer free code editing or related tutorials. If code you changed yourself causes storefront problems, CYBERBIZ is not responsible for fixing it. For help with customization, contact online customer service.
- **Switching themes or versions does not sync automatically**: The cookie banner code you pasted exists only in "this current theme." If you later switch to another theme or update the theme version, your earlier changes do not carry over. Paste the code again in the new theme.
- **Use version control to restore**: The template editor has built-in version control. If the storefront looks wrong after a change, click **"View Previous Versions"** while editing the file and restore an earlier version, which lowers the risk of breaking your theme.

---

## Next Steps { #next-steps-cookie-consent }

<div class="grid cards" markdown>

- :lucide-palette:{ .lg }  
  [__Apply and Switch Website Themes__](../theme-and-layout/apply-and-switch-theme.md)  
  Download, switch, and publish themes to manage your website's overall look.

- :lucide-file-text:{ .lg }  
  [__Business Disclosure Settings__](../site-settings/business-disclosure.md)  
  Set up footer information such as your privacy policy to go with the cookie banner.

</div>

## FAQ { #faq-cookie-consent }

??? quote "The banner doesn't appear on the storefront after I paste the code"
    [](){ #faq-cookie-consent-not-showing }
    Check the following in order:

    - The code is pasted **directly above** `</head>`, and you clicked "Save."
    - You edited the **currently published** theme (unpublished themes do not affect the storefront).
    - Clear your browser cache or refresh in a private (incognito) window to rule out display delays caused by caching.

??? quote "The banner disappeared after I switched or updated my theme"
    [](){ #faq-cookie-consent-lost-after-switch }
    Code you paste yourself is saved only in the original theme and does not carry over when you switch or update themes. In the new theme, open `theme.liquid` again and paste the code once more.

??? quote "I can't find the "CSS/HTML Editor" option and can't edit code"
    [](){ #faq-cookie-consent-no-editor }
    This usually means your current theme does not support code editing, or your account lacks "Appearance" editing permissions. Check the following:

    - The theme's "Actions" menu includes **CSS/HTML Editor**.
    - Your account has admin editing permissions for "Appearance." If not, ask a store administrator to assign them.

??? quote "I want to change the banner's text or style"
    [](){ #faq-cookie-consent-edit-style }
    Go back to the third-party tool, change the settings, and generate new code. Then overwrite the code you pasted earlier using the same steps. Or edit the pasted code directly in the template editor. For more advanced interactions or customization, consult someone with a coding background or CYBERBIZ online customer service.

## References { #reference-cookie-consent }

- [WebsitePolicies Cookie Consent Banner Generator](https://www.websitepolicies.com/create/cookie-consent-banner)
