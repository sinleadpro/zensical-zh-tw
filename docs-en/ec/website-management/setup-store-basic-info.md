---
title: "Set up Basic Website Information"
description: "Configure core settings such as basic website information, company contact details, shipping address, and admin panel language."
created:
last_modified: 2026-07-06 17:39
lang: en-US
permalink: "https://help.cyberbiz.io/ec/website-management/setup-store-basic-info/"
type: guide
author: Jase
reviewers: []
notes:
  - verify feature validity 註冊跳轉頁面
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 管理中心
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定網站名稱
  - 設定退貨通知信箱
  - 填寫公司聯絡資訊
  - 設定帳務通知信箱
  - 填寫公司物流地址
  - 自訂訂單編號格式
  - 設定後台貨幣
  - 設定後台語言
  - 設定前台商店語言
  - 設定前台商店幣值
features:
  - "Basic Website Information"
  - 公司聯絡資訊
  - 公司物流地址
  - 訂單編號格式自訂
  - 後台顯示貨幣設定
  - 後台語言顯示設定
  - 前台商店語言顯示
  - 前台商店幣值顯示
prerequisites:
  - 後台管理員權限
related:
  - ec/website-management/references/general-preferences-order-format-variables/
  - ec/website-appearance/site-settings/business-disclosure/
  - ec/website-appearance/theme-and-layout/apply-and-switch-theme/
tags:
  - 網站基本資訊
  - "Website Settings"
  - "Company Information"
  - "Shipping Address"
  - "Order Number"
  - "Language Settings"
  - "Currency Settings"
  - "Admin Panel Management"
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 一般設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8314
  - https://www.cyberbiz.io/support/?p=33987
  - https://www.cyberbiz.io/support/?p=5598
comments: false
search:
  exclude: false
icon: lucide/store
hide:
---

![General settings page](../../assets/images/ec-general-preferences-hero.en.png){ title="General Settings Page" .hero-page }

## About General Settings { #intro-general-preferences }

**General** (admin panel path: **Website Management > General**) is where you set up your store's basic information. The website name and company contact and invoice information you enter here appear on your website and invoices. You can also customize the order number format and adjust how languages and currencies display in the admin panel and on the storefront.

The whole page is a single form divided into collapsible sections. All settings share the **Save All Settings** button at the bottom of the page. After you fill in any section, you must click this button for the changes to take effect.

!!! info "Tip"
    The sections you see depend on your plan and activated features. If you can't find a section mentioned in this guide, see [Requirements and Limits](#prerequisites-general-preferences) to check the activation conditions.

---

## Page Overview { #overview-general-preferences }

| Section | Settings | Activation conditions |
| :-- | :-- | :-- |
| [About Your Website](#operate-general-preferences-company-info) | Website name, contact email | All plans |
| [Company Contact Information](#operate-general-preferences-company-info) | Address, phone, tax ID number, full company name, billing notification email | All plans |
| [Company Logistics Address](#operate-general-preferences-return-address) | Return address for convenience store parcels sent back by cash-on-delivery home delivery | All plans (hidden if you use the e-commerce warehousing service) |
| [Standards and Formats](#operate-general-preferences-order-format) | Order number format; currency display format | Order number format: all plans; currency display format: requires activation |
| Admin panel display currency | Shows the currency the admin panel currently settles in (read-only) | All plans |
| [Admin Panel Language Display](#operate-general-preferences-admin-language) | Switch the language of the admin panel interface | All plans |
| [Storefront Language Display](#operate-general-preferences-frontend-locale) | Set the languages shoppers can switch to on the storefront | Requires activation and a drag-and-drop theme |
| [Storefront Currency Display](#operate-general-preferences-frontend-locale) | Set the currencies shoppers can switch to on the storefront | Requires activation and a drag-and-drop theme |

---

## Requirements and Limits { #prerequisites-general-preferences }

Before you start, check the following:

- [x] **Admin panel permission**: You need admin panel permission for Website Management.
- [x] **Invoice fields**: If you issue e-invoices, **Full company name**, **Phone**, **Detailed address**, and **Tax ID number** are required. If you delete them, the system automatically switches invoices to the member carrier (personal).

Some sections only appear with certain plans or activated features:

??? plan "Plans and Activated Features"
    - **Order number format, company contact information, admin panel language, and admin panel display currency**: Available on all plans with no extra activation.
    - **Currency display format** (how amounts appear on web pages and in emails): Appears in the **Standards and Formats** section only after the feature is activated.
    - **Storefront language display / storefront currency display**: These two sections appear only when the features are activated and your website uses a drag-and-drop theme.
    - **Company English name**: For cross-border or export merchants. Only certain plans and cross-border stores see this field.
    - To activate these features, contact your store consultant or Customer Service.

---

## Steps { #operate-general-preferences }

The steps below are grouped by common tasks. All sections share the **Save All Settings** button at the bottom of the page, so you can fill in several sections and save them together.

### Set the Website Name and Company Contact Information { #operate-general-preferences-company-info }

Fill in the basic information shown on your website and invoices.

1. **Open General settings:** In the admin panel, go to **Website Management > General**.
2. **Enter the website name:** In the **About Your Website** section, enter your brand or store name in **Website name**[^e] (up to 15 Chinese characters or 30 English characters), and enter a contact **Email**[^f].

    ![About your website](../../assets/images/ec-管理中心-一般設定-關於網站.en.png){ title="About Your Website" }

3. **Enter company contact information:** In the **Company Contact Information** section, enter the **Detailed address**, **Phone**, **Tax ID number**, **Full company name**, and **Billing notification email**[^a].

    ![Company contact information](../../assets/images/EC-管理中心-一般設定-公司聯絡資訊.en.png){ title="Company Contact Information" }

    !!! info "Cross-Border Logistics Settings"

        - **Overseas shipping labels:** Merchants with cross-border or export business may also see a **Company English name** field on some plans. Filling it in also activates overseas shipping labels.
        - **SF Express overseas logistics:** Enter your company's official English name from its business registration in the **English company name registered with the Bureau of Foreign Trade** field.
        - **DHL logistics verification:** Enter the correct **Tax ID** and **English company name registered with the Bureau of Foreign Trade**, and click verify to activate the feature.

4. **Save:** After checking the information, click **Save All Settings** at the bottom of the page.

[^a]: You can enter several billing notification emails separated by commas, for example `mail1@example.com,mail2@example.com`. The tax ID number must be 8 digits.

[^e]: This name appears in the page title and is also used for search engine optimization (SEO) and for merchant identity reviews by payment risk control units. Some settings involve legal compliance (such as **business information disclosure**), so enter your correct brand name and tax ID number.
[^f]: This email is also your login account for the CYBERBIZ online course platform.

---

### Set the Return Address { #operate-general-preferences-return-address }

**Company Logistics Address** is the address the system uses to return store-to-store convenience store parcels by cash-on-delivery home delivery when they are sent back to the original store and not picked up.

1. **Open General settings:** Go to Website Management > General and find the **Company Logistics Address** section.
2. **Enter the return address:** Choose the city or county and district, and enter the detailed address where returned parcels should be delivered.

    ![Company logistics address](../../assets/images/EC-管理中心-一般設定-公司物流地址.en.png){ title="Company Logistics Address" }

3. **Save:** Click **Save All Settings** at the bottom of the page.

[^b]: If you use the CYBERBIZ e-commerce warehousing service, returns go straight back to the warehouse, so this section doesn't appear and you don't need to set it.

---

### Customize the Order Number Format { #operate-general-preferences-order-format }

The default order number format is `#{{ "{{number}}" }}` (displayed as, for example, `#1234`). You can add variables such as dates and random numbers to build a numbering rule that suits how you work. All variables are listed in the [Order Number Format Variable Reference](references/general-preferences-order-format-variables.md){ title="Order Number Format Variable Reference" }.

1. **Open General settings:** Go to Website Management > General and expand the **Standards and Formats** section.
2. **Show the format help:** Click **Custom format** next to **Order number format** to see the available variables.
3. **Enter the new format:** Enter the format you want in the field, for example `CB{{ "{{year}}" }}{{ "{{month}}" }}-{{ "{{number}}" }}` (or `CYBERBIZ{{ "{{number}}" }}`). The system shows a preview right away[^c].

    ![Logistics address and order format](../../assets/images/ec-管理中心-一般設定-物流地址與訂單格式.en.png){ title="Logistics Address and Order Format" }

4. **Save:** Click **Save All Settings** at the bottom of the page.

[^c]: The format **must include** `{{ "{{number}}" }}` and can't be longer than 64 characters. Otherwise, you see the message "The order number format must include number and can't exceed 64 characters" when you save. Changing the format only affects new orders. Numbers of existing orders don't change.

---

### Switch the Admin Panel Interface Language { #operate-general-preferences-admin-language }

Change the language of the management interface you see when you log in to the admin panel.

1. **Open General settings:** Go to Website Management > General and find the **Admin Panel Language Display** section.
2. **Choose a language:** Choose the admin panel language from the dropdown (Traditional Chinese, English, Japanese, or Korean).
3. **Save:** Click **Save All Settings** at the bottom of the page. The interface switches to the selected language.

![Admin panel language display](../../assets/images/ec-general-preferences-admin-language.en.png){ title="Admin Panel Language Display" }

!!! note "Note"
    The admin panel language only affects the management interface you see in the admin panel. It doesn't change the language customers see on your storefront. Set the storefront language in the **Storefront Language Display** section (see [Set Up Storefront Multi-Language and Multi-Currency Display](#operate-general-preferences-frontend-locale)).

---

### Set up Storefront Multi-Language and Multi-Currency Display { #operate-general-preferences-frontend-locale }

Let customers switch the language or currency on your storefront. The **Storefront Language Display** and **Storefront Currency Display** sections appear only when the features are activated and your website uses a drag-and-drop theme.

1. **Open General settings:** Go to Website Management > General and find the **Storefront Language Display** or **Storefront Currency Display** section.
2. **Turn on display:** Select **Show storefront language** or **Show storefront currency**.
3. **Choose languages or currencies to offer:** In the menu below, add the languages or currencies customers can switch to on the storefront (the default language and your store's currency are fixed and can't be removed).

    ![Currency and language display](../../assets/images/ec-管理中心-一般設定-貨幣與語言顯示.en.png){ title="Currency and Language Display" }

4. **Confirm the prompt:** When you turn storefront languages on or off, a confirmation window explains the impact[^d]. Confirm to continue.
5. **Save:** Click **Save All Settings** at the bottom of the page.

[^d]: When you turn on storefront languages, language subdirectories are added to URLs automatically (for example, `/zh-TW` and `/en`), which may affect SEO settings. Before you turn this on, make sure your page content is ready for each language. Turning it off removes the language subdirectories.

---

## Important Rules and Limits { #specs-general-preferences }

- **One save button for all settings:** The page has only one button, **Save All Settings**, at the bottom. Click it after changing any section, and save before you leave the page.
- **Order number format rules:** The format must include `{{ "{{number}}" }}` and can't be longer than 64 characters. Changes only affect new orders.
- **Tax ID number and invoices are linked:** If you issue e-invoices, deleting **Detailed address** or **Tax ID number** switches invoices to the member carrier (personal) automatically.
- **Admin panel display currency can't be changed here:** It only shows the current settlement currency and is read-only. To change it, contact Customer Service.
- **Admin panel and storefront languages are separate:** **Admin Panel Language Display** only changes the admin panel interface. The language customers see on the storefront is set by **Storefront Language Display**.
- **Storefront multi-language and multi-currency need a drag-and-drop theme:** These two settings only appear and take effect with a drag-and-drop theme.

## Next Steps { #next-steps-general-preferences }

<div class="grid cards" markdown>

- :lucide-receipt-text:{ .lg }
  [__Disclose Business Name and Tax ID Number__](../website-appearance/site-settings/business-disclosure.md){ title="Disclose Business Name and Tax ID Number" }
  Show your company name and tax ID number in a visible place on your website to meet legal requirements.

- :lucide-palette:{ .lg }
  [__Apply and Change Website Themes__](../website-appearance/theme-and-layout/apply-and-switch-theme.md){ title="Apply and Change Website Themes" }
  Switch your website theme. Storefront multi-language and multi-currency display need a drag-and-drop theme.

</div>

## FAQ { #faq-general-preferences }

??? quote "If I change the order number format, do existing order numbers change too?"
    [](){ #faq-general-preferences-order-format-existing }
    No. The order number format only applies to new orders. Existing order numbers stay the same.

    - If you see a format error when you save, make sure the format includes `{{ "{{number}}" }}` and is no longer than 64 characters.

??? quote "Why don't I see the Company Logistics Address section?"
    [](){ #faq-general-preferences-no-logistics-address }
    If you use the CYBERBIZ e-commerce warehousing service, returns go straight back to the warehouse, so the **Company Logistics Address** section doesn't appear. This is normal. Other merchants see this section and use it to set the return address for convenience store parcels sent back by cash-on-delivery home delivery.

??? quote "Can't find Storefront Language Display or Storefront Currency Display?"
    [](){ #faq-general-preferences-no-frontend-locale }
    These two sections appear only when both conditions are met:

    - The matching features are activated.
    - Your website uses a drag-and-drop theme.

    If you need them, contact your store consultant or Customer Service to activate them.

??? quote "What happens if I delete the tax ID number or address?"
    [](){ #faq-general-preferences-delete-vat }
    If you issue e-invoices, deleting **Tax ID number** or **Detailed address** makes the system switch invoices to the member carrier (personal) automatically. If you still need to issue company invoices, keep these fields.

??? quote "If I switch the admin panel to English, will customers see my website in English too?"
    [](){ #faq-general-preferences-admin-vs-frontend-language }
    No. **Admin Panel Language Display** only changes the language of the management interface when you log in to the admin panel. It doesn't affect the language customers see on the storefront. Set the storefront language separately in the **Storefront Language Display** section.

??? quote "Why doesn't the storefront show my updated basic website information?"
    [](){ #faq-general-preferences-frontend-not-updated }
    Make sure you clicked the **Save** button at the bottom of the page. Some changes only appear after you refresh the storefront page or clear your browser cache.

??? quote "What if verification of the company tax ID number and English name fails?"
    [](){ #faq-general-preferences-verification-failed }
    Make sure the tax ID number and English company name match the Bureau of Foreign Trade registration, with no extra spaces or special characters, and then click **Verify** again.

??? quote "How do I set a custom order number format?"
    [](){ #faq-general-preferences-order-format-setup }
    Click **Custom format** to enter your own text and variables. The format must include the `{{ "{{number}}" }}` variable, for example `EC{{ "{{number}}" }}`, for order numbers to be generated correctly.

??? quote "Can I set several billing notification emails?"
    [](){ #faq-general-preferences-multiple-emails }
    Yes. Separate the email addresses with **commas (,)**, for example `finance1@company.com,finance2@company.com`.

??? quote "Which themes support storefront language and currency display?"
    [](){ #faq-general-preferences-frontend-locale-version }
    This feature only works with **drag-and-drop themes**. Other themes don't show this option.

??? quote "Is there a length limit for the website name?"
    [](){ #faq-general-preferences-site-name-limit }
    Yes. The limit is **15 Chinese characters** or **30 English characters**. Longer names can't be saved.

---

## References { #reference-general-preferences }

- [Order Number Format Variable Reference](references/general-preferences-order-format-variables.md)

