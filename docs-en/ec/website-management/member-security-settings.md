---
title: "Set up Member Security and Website Protection"
description: "Manage member password strength, personal data masking, and region blocklists, and protect your storefront with a password to secure customer data and website access."
created: 2026-08-12 10:59
last_modified: 2026-08-12 10:59
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
  - 保護顧客隱私
  - 設定會員密碼規則
  - 網站密碼保護
  - 限制地區造訪
features:
  - 會員安全設定
  - "Website Password"
  - 會員密碼規則
  - 會員個資部分隱碼
  - 訪問限制地區黑名單
prerequisites:
  - 需具備「設置」權限
related:
  - ec/website-management/admin-security-settings/
  - ec/website-management/bot-protection-settings/
  - ec/website-management/add-admin-set-permissions/
tags:
  - "Member Security"
  - 網站密碼
  - "Personal Data Masking"
  - Blocklist
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 安全性設定 > 會員安全
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3214
comments: false
permalink: "https://help.cyberbiz.io/ec/website-management/member-security-settings/"
search:
  exclude: false
icon: lucide/user-check
hide: []
---

# Set up Member Security and Website Protection

With the Member Safety settings, you can control access to your storefront and strengthen customer data privacy and password strength.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All plans
{ .doc-badge }

![Security Setting page hero](../../assets/images/ec-管理中心-安全性設定.en.png){ .hero-page }

## About Security Setting { #intro-security }

Security Setting is the security control center of the CYBERBIZ admin panel. It helps you lower the risk of account theft, customer data leaks, and malicious visits. You can find it in the admin panel under **Website Management > Security Setting**, and it covers three main areas of protection:

- **Member Safety**: Protects your website and customer data.
- **[Admin Login](admin-security-settings/)**: Protects how you and your staff log in to the admin panel.
- **[Bot Protection](bot-protection-settings/)**: Filters out malicious visitors and sets up a first line of defense before any SMS is sent.


## Requirements and Limits { #prerequisites-security }

Before you start, check the following:

- [x] **Settings permission**: To view and edit this tab, your account needs the **Settings** permission in **User Account Settings**. You can [change admin permissions](add-admin-set-permissions/#operate-admin-perms-edit).
- [x] **Plan or activation**: Some sections only appear with certain plans or after the feature is activated.
- [x] **Staff role**: The Member Safety tab is hidden by default when a **branch staff** account logs in.


## Steps { #operate-security }

In the admin panel, go to **Website Management > Security Setting** and click the **Member Safety** tab at the top to start.

### Set a Website Password { #operate-security-website-password }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All plans

Add a password to your whole storefront so that only customers who know the password can browse it. This is useful for websites that have not launched publicly yet or are only open to specific customer groups.

1. **Open the section:** On the **Member Safety** tab, find the **Website Password** section.
2. **Turn on password protection:** Select **Website Password**.
3. **Set the password:** Enter a password in the **Password** field (up to 64 characters).
4. **(Optional) Leave a message for customers:** Enter a message in **Message to Customers** (up to 255 characters). Customers see this message on the password page.
5. **Save:** Click **Save** to apply.

![](../../assets/images/ec-管理中心-安全性設定-網站密碼.en.gif)

!!! note "What Customers See"
    After you turn on the website password, a password page appears whenever a customer visits any storefront page. Customers must enter the correct password before they can browse the website.
    To switch to **public mode so that all customers can browse freely**, **Cancel** this setting.


### Member Password Rules { #operate-security-customer-password-rule }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | Add-on

Set the required password strength when customers register or set their member password.

1. **Open the section:** On the **Member Safety** tab, find the **Member Password Rule** section.
2. **Set the length limit:** The **length limit** is required. Enter the minimum and maximum number of characters for member passwords.
3. **Add composition rules:** Select **Include numbers.**, **Include uppercase letters.**, **Include lowercase letters.**, or **Include special characters** as needed.
4. **Save:** Click **Save** to apply.

![](../../assets/images/ec-管理中心-安全性設定-會員密碼規則.en.png)


### Mask Member Information in Order Details { #operate-security-pdpa }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | All PLUS plans / Enterprise

Mask customer personal data such as names, mobile numbers, and addresses (for example, with asterisks). This feature only applies to printed order details, and it appears only **after it is activated**.

1. **Open the section:** On the **Member Safety** tab, find the **Partially Masked Member Information** section.
2. **Turn on the feature**: Select **Order Details Printing**.
3. **Save:** Click **Save** to apply.

!!! info "Masking Rules"
    | Field | Masking rule | Example |
    | :-- | :-- | :-- |
    | Name | Keeps the first and last characters | J \*\*\*\* n |
    | Mobile | Keeps the first three digits and the last digit | 093 \*\*\*\*\* 3 |
    | Address | Keeps the postal code, the beginning of the address, and the last character | 10001 Taipei City, Songshan \*\*\*\*\* Rd. |

![](../../assets/images/ec-管理中心-安全性設定-會員個資部分隱碼.en.png)



### Block Visits from Specific Regions { #operate-security-restricted-locations }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | Enterprise / Cross-border

Block customers in specific regions from visiting your storefront. This is often used in cross-border business to exclude certain markets.

1. **Open the section:** On the **Member Safety** tab, find the **Location Blacklist** section.
2. **Choose the regions to block:** Click the **Restricted Locations** field and select the countries or regions to block from the menu.
3. **Save:** Click **Save** to apply. After you save, customers in the listed regions can no longer visit your storefront.

![Location blacklist](../../assets/images/ec-管理中心-安全性設定-會員登入-訪問限制地區黑名單.en.png)


