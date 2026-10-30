---
title: "Change the Storefront Label for Valid Orders from Other Channels"
description: "Add a key to the dictionary file to customize the storefront label for 'Valid Orders from Other Channels' so the wording better fits your brand or channel."
created: 2026-08-17 14:22
last_modified: 2026-08-17 14:22
lang: en-US
type: guide
status: ""
author: Ann
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
  - developer
difficulty: intermediate
tnb: branch
plans: 
  - Enterprise
plan_options: []
cyb_extensions: []
intents: 
  - 變更其他通路有效訂單名稱
  - 自訂字典檔顯示文字
features: 
  - 字典檔
  - 其他通路有效訂單
  - 樣板編輯器
prerequisites:
  - "商店已啟用其他通路有效訂單功能"
related:
  - ec/members/manage-member-profiles/
  - ec/website-appearance/code-customization/restore-code-theme-editor/
  - ec/website-appearance/site-settings/setup-storefront-language-text-customization/
  - ec/website-appearance/code-customization/theme-editor-complete-guide/
tags: 
  - "Dictionary File"
  - "Storefront Text"
acoiv: configure
apis: []
devices: 
  - desktop
ui_components: 
  - CSS/HTML 編輯器
  - 字典檔
paths: 
  - 網站外觀 > 套版主題管理 > 選擇操作 > CSS/HTML 編輯器
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-appearance/code-customization/customize-other-channel-order-label/"
comments: false
search:
  exclude: false
icon: lucide/text-cursor-input
hide: []
---

# Change the Storefront Display Name for "Valid Orders from Other Channels"

Add a key to the dictionary file to customize the storefront display name of "Valid Orders from Other Channels," so the wording better fits your brand or channel.
{ .subtitle }

[:lucide-tag:{ title="Available Plans" }](../../../resources/conventions.md#適用方案) | Enterprise
{ .doc-badge }

![](../../../assets/images/EC-前台-會員中心-編輯其他通路有效訂單名稱01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Consistent customer-facing wording**: Change the default "Valid Orders from Other Channels" to a name you normally use, such as "Store Purchase History" or "Offline Purchases."
    - **Fewer member questions**: Storefront copy matches what your customer service says, so members are less confused about where orders came from.


## Before You Start { #prerequisites-channel-label }

- **What changes**: Only the name members see on the storefront changes. How the admin member page works and how amounts are accumulated stay the same. To add or manage orders from other channels, see [Manage Member Profiles: Orders from Other Channels](../../members/manage-member-profiles.md#operate-member-profiles-other-orders).
- **Editing risk**: Editing `.yml` is an advanced task. Back up first, or make sure you can [restore a template version](restore-code-theme-editor.md), before you save.


## Steps { #operate-channel-label }

1. Sign in to the CYBERBIZ admin and go to **Website Appearance > Theme Setting**.
2. On your current theme, click **Actions > CSS/HTML Editor**.

    ![](../../../assets/images/EC-後台-網站外觀-套版主題管理-編輯語法01.en.png){ .screenshot }

3. In the template editor search box, enter **zh-TW.yml** to open the dictionary file.

    ![](../../../assets/images/EC-後台-網站外觀-套版主題管理-編輯其他通路有效訂單名稱01.en.png){ .screenshot }

4. Find the **`general`** section.

    ![](../../../assets/images/EC-後台-網站外觀-套版主題管理-編輯其他通路有效訂單名稱02.en.png){ .screenshot }

5. Add the following key to the section, and change the text on the right to the name you want to show:

    ```yaml
    customize_other_valid_order: Display name
    ```

    !!! warning "Format"
        The structure is: `customize_other_valid_order` (do not change) `:` (half-width colon) ` ` (half-width space) `Display name` (customizable).

        - Correct: `customize_other_valid_order: 門市消費紀錄`
        - Incorrect: `customize_other_valid_order:門市消費紀錄` (missing space)

    ![](../../../assets/images/EC-後台-網站外觀-套版主題管理-編輯其他通路有效訂單名稱03.en.png){ .screenshot }

6. Click **Save**. When members view orders from other channels on the storefront, they see your custom name.

    ![](../../../assets/images/EC-前台-會員中心-編輯其他通路有效訂單名稱01.en.png){ .screenshot }

!!! info "Multilingual Stores"
    If your store has dictionary files for other languages (such as `en.yml`), in the `general` section of each matching language file, add `customize_other_valid_order` as well and enter the display text in that language.


## FAQ { #faq-channel-label }

??? quote "I added the key and saved, but the storefront name did not change."
    Check the following:

    1. Your store's version supports the **Valid Orders from Other Channels** feature.
    2. The key name is spelled `customize_other_valid_order` (do not change the English key).
    3. The key is in the `general` section, and the YAML indentation and the space after the colon are correct.
    4. You saved the dictionary file. If needed, refresh the storefront or clear the cache and check again.

??? quote "Can I delete the key to restore the default name?"
    Yes. Remove the `customize_other_valid_order` line from the dictionary file and save. The storefront then goes back to the system default name, "Valid Orders from Other Channels." If the theme breaks after you save, [restore a template version](restore-code-theme-editor.md).


## Related Articles { #reference-channel-label }

<div class="grid cards" markdown>

- :lucide-languages:{ .lg }  
  [__Set Up Storefront Language and Text Customization__](../site-settings/setup-storefront-language-text-customization.md)  
  Use dictionary files and the template editor to adjust the storefront language and system default text.

- :lucide-code:{ .lg }  
  [__Template Editor Complete Guide__](theme-editor-complete-guide.md)  
  Learn the basics of the template editor, how to use special syntax, and what to watch out for.

</div>