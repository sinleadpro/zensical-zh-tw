---
title: "Set up and Manage Two-Step Verification"
description: "Turn on and manage two-step verification (2FA), including binding an authenticator, using backup codes, and resetting or enforcing verification for staff."
created: 2026-03-16 20:06
last_modified: 2026-07-03 11:44
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
  - 管理中心
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定二階段驗證
  - 啟用2FA
  - "Account Security"
features:
  - "Two-Step Verification"
  - 備用碼
  - 強制開啟
prerequisites: []
related:
  - ec/website-management/authy-two-factor-authentication/
tags:
  - 二階段驗證
  - "Information Security"
  - 帳號安全
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 安全性設定 > 管理員登入
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=12650
permalink: "https://help.cyberbiz.io/ec/website-management/setup-manage-two-factor-auth/"
comments: false
search:
  exclude: false
icon: lucide/monitor-smartphone
hide: []
---

![Two-step verification settings](../../assets/images/ec-管理中心-安全性設定-二階段驗證.en.png){ title="Two-Step Verification Settings" .hero-page }

## About Two-Step Verification { #intro-two-factor }

**Two-step verification (2FA)** is an important security feature. When it is on, logging in to the admin panel or POS storefront requires both your account and password and a dynamic code from a mobile authenticator app. This adds an extra layer of protection to your account even if your password is stolen.

!!! example "When It Is Used"

    Besides login, the system also asks for a two-step verification code when you do the following actions that involve sensitive data:

    - **Exporting order reports**.
    - **Exporting member data**.
    - **Adding a co-admin**.

## Requirements and Limits { #prerequisites-two-factor }

Before you start, install an authenticator app on your phone.

*   **Recommended app**: CYBERBIZ recommends that you [use Authy](authy-two-factor-authentication.md){ title="Enable Two-Step Verification with Authy" }, because it has good backup and recovery features.
*   **Other options**: You can also use [Google Authenticator :lucide-external-link:](https://support.google.com/accounts/topic/2954345?hl=zh-Hant&ref_topic=7667090) or another authenticator app you prefer.

## Steps { #operate-two-factor }

### Turn on Two-Step Verification { #operate-two-factor-enable }

1.  **Open the page**: Log in to the admin panel and go to **Website Management**」>「**Security Setting**」>「**Admin Login**.
2.  **Turn on the feature**: Click the **Two-step verification settings** switch to start setup.
3.  **Scan to link**: Open the authenticator app on your phone and **scan the QR code on the screen** (or enter the key manually) to add the account.
4.  **Enter the code**: Enter the 6-digit code currently shown in the app and confirm.
5.  **Download backup codes (important)**: The system generates **10 backup codes**. Download them and keep them in a safe place.
    *   *Note: The backup codes are only shown this one time. If you lose your phone and can't get a verification code, you need to [log in with a backup code](#operate-two-factor-backup){ data-preview }.*

---

### Manage and Reset Staff Verification { #operate-two-factor-reset }

The website owner can manage security verification for all staff:

*   **View progress**: Click **Staff Security Verification** to see whether each admin has turned on verification and when.

    ![Staff security verification](../../assets/images/ec-管理中心-安全性設定-二階段驗證-管理人員安全驗證.en.gif){ title="Staff Security Verification" }

*   **Help reset**: If a staff member loses their phone, a user with higher permissions can click **Reset** to turn off that person's verification so that they can set it up again.
    *   *Permission levels: Website admins can manage everyone, co-admins can manage POS staff, and POS store managers can manage their own store staff.*
*   **Enforce for everyone**: The owner can turn on **Require all staff to turn on two-step verification**. After this is on, all relevant staff must finish setup before they can keep using the system.

    ![Enforce two-step verification](../../assets/images/ec-管理中心-安全性設定-二階段驗證-強制開啟.en.png){ title="Enforce Two-Step Verification" }

    !!! warning "What Happens When It Is Enforced"

        - Access limits: All relevant staff (including co-admins and POS staff) must link 2FA before they can keep using the system.
        - Can't be turned off by users: After it is enforced, regular users can't turn off 2FA themselves.
        - Resets: If staff need to reset verification, for example because they changed phones, they must contact an admin with higher permissions for help.

---

### Log in to the Admin Panel with a Backup Code { #operate-two-factor-backup }

If you can't get an authenticator code, click to try another login method and log in with a backup code you downloaded and saved earlier.

![Log in with a backup code](../../assets/images/ec-管理中心-安全性設定-二階段驗證-備用碼登入.en.png){ title="Log In with a Backup Code" }


## FAQ { #faq-two-factor }

??? quote "What if I get an error after entering the code and can't log in?"
    This is usually caused by the time being out of sync. Check the following:

    * **Check your phone's time zone**: Make sure your phone's date and time are set to **sync automatically from the network**. Verification codes (TOTP) are very time-sensitive, and a difference of a few seconds can make them invalid.
    * **Check the account**: Make sure the account shown in the authenticator app is the one for this website's admin panel, so you don't use a code for another website by mistake.

??? quote "What if I lose my phone or can't use the authenticator?"

    * **Use a backup code**: If you still have the **10 backup codes** you downloaded during setup, log in with one of them.
    * **Ask an admin to reset it**: If you have no backup codes, contact an admin with higher permissions (such as the website owner) and ask them to click **Reset** for you in **Staff Security Verification** to unlink it.

??? quote "Do I need to set it up again when I get a new phone?"
    Yes. Before you switch phones, while the old phone still works, turn off two-step verification in the admin panel. Then scan the QR code again on the new phone to link it.
    * *Note: If you use Authy with cloud backup turned on, you can log in to your Authy account on the new phone and use it right away.*
