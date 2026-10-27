---
title: "Set up Admin Login Security"
description: "Strengthen admin account security with an IP allowlist, two-step verification (2FA), automatic logout, and password rules to prevent unauthorized logins and account theft."
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
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 加強後台安全性
  - 防範後台帳號盜用
  - 設定登入驗證
  - 設定 IP 白名單
features:
  - 管理員登入安全
  - IP白名單
  - 瀏覽器Cookie驗證
  - 自動登出時間
  - reCAPTCHA驗證
  - 二階段驗證(2FA)
  - 管理員密碼規則
prerequisites:
  - 先確認自己的 IP
related:
  - ec/website-management/member-security-settings/
  - ec/website-management/bot-protection-settings/
  - ec/website-management/add-admin-set-permissions/
  - ec/website-management/setup-manage-two-factor-auth/
tags:
  - "Admin Security"
  - "IP Allowlist"
  - 2FA
  - "Two-Step Verification"
  - "Automatic Logout"
acoiv: operation
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 安全性設定 > 管理員登入
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3214
  - https://www.cyberbiz.io/support/?p=14334
  - https://www.cyberbiz.io/support/?p=472
permalink: "https://help.cyberbiz.io/ec/website-management/admin-security-settings/"
comments: false
search:
  exclude: false
icon: lucide/shield-check
hide: []
---

# Set up Admin Login Security

The Admin Login settings provide multiple layers of protection so that only authorized people can access your store's admin panel.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All plans
{ .doc-badge }

![Security Setting page hero](../../assets/images/ec-管理中心-安全性設定.en.png){ .hero-page }

## About Security Setting { #intro-security }

Security Setting is the security control center of the CYBERBIZ admin panel. It helps lower the risk of account theft, customer data leaks, and malicious visits. The page is under **Website Management > Security Setting** in the admin panel and covers three main areas:

- **[Member Security](member-security-settings/)**: Protects your website and customer data.
- **Admin Login**: Protects how you and your staff log in to the admin panel.
- **[Bot Protection](bot-protection-settings/)**: Filters out malicious visitors and sets up the first line of defense before SMS messages are sent.


## Prerequisites and Limitations { #prerequisites-security }

Before you start, check the following:

- [x] **Settings permission**: Except for two-step verification (which every admin can set up for themselves), all sections require your account to have the **Settings** permission in **User Account Settings** to view and edit them. You can [change admin permissions](add-admin-set-permissions/#operate-admin-perms-edit).


## Steps { #operate-security }

In the admin panel, go to **Website Management > Security Setting**, and then click the **Admin Login** tab at the top to start.

### Set up an IP Allowlist { #operate-security-ip-whitelist }

After you turn this on, only IP addresses on the list can log in to the admin panel. This suits merchants who work from a fixed office or a fixed network.

1. **Find the section:** On the **Admin Login** tab, find the **Whitelist** section.
2. **Check your current IP:** The section shows **your current IP**. Write it down and make sure to add it to the list later so you don't lock yourself out.
3. **Add a trusted IP:** Click **Add IP address**, enter the address to allow in the **Add IP address** window, and click **Add**.[^ip-format]

    - Always **add your current IP to the list** first. Otherwise, you will be logged out immediately after turning this on and won't be able to log in.

        !!! warning "Engineering Rescue Fee"
            If the allowlist locks you out of the admin panel, contact CYBERBIZ Customer Service for help. If you have allowed Customer Service to access your admin panel, no engineering work is needed. If engineering work is necessary, a service fee of NT$2,000 will be charged.

    - If your company uses a dynamic IP, **do not add a dynamic IP** to the allowlist (for example, a mobile Wi-Fi hotspot). Add a **static IP** to the allowlist instead. Otherwise, you may not be able to log in later.

4. **Enable Whitelist** Turn on the **Enable Whitelist** switch. If your current IP is not on the list, the system shows a warning[^whitelist-lockout], and the setting takes effect only after you confirm.
5. **Manage the list:** The list appears as a table (5 entries per page). Click the delete icon in a row to remove that address.

![](../../assets/images/ec-管理中心-安全性設定-白名單.en.png)

[^ip-format]: IPv4, IPv6, and CIDR ranges are supported. If the format is wrong, the field shows "Invalid IP address format."
[^whitelist-lockout]: The warning reads "Your current IP address is not on the allowlist. After you enable it, you will be logged out immediately and cannot log in to the admin panel. Are you sure you want to enable it?" If you delete the IP you are currently using, the system also asks you to confirm so you don't lock yourself out.



### Browser Cookie IP Allowlist { #operate-security-cookie-whitelist }

This feature is different from the IP allowlist above. It does not limit who can log in. Instead, it lets you add trusted IPs that change often, so you are not forced to log in again when your IP changes while you work in the same browser.

> **Decide whether you need it**: Set this up only if you are logged out repeatedly because your IP changes often after you log in. You don't need it if your IP is static or stable.

1. **Find the section:** On the **Admin Login** tab, find the **Browser Cookie IP Whitelist** section.
2. **Add a trusted IP:** Click **Add IP address**, enter the address in the **Add IP address** window, and click **Add**.
3. **Turn on the feature:** Turn on the **Enable Browser Cookie IP Whitelist** switch.

![](../../assets/images/ec-管理中心-安全性設定-cookie whitelist.en.png)



### Set the Automatic Logout Time { #operate-security-logout-timer }

Set how long the admin panel can be idle before you are logged out automatically. This lowers the risk of someone else using an unattended computer.

> If several people share a computer or you use the admin panel in a public place, choose a shorter idle time (such as 4 hours) for better security.

1. **Find the section:** On the **Admin Login** tab, find the **Inactive Logout** section.
2. **Choose a time:** Select one of five options: **4 hours**, **8 hours**, **1 day**, **3 days**, or **7 days**.
3. **Save the setting:** Click **Change** to apply it.

![](../../assets/images/ec-管理中心-安全性設定-自動登出時間.en.png)


### Admin Login reCAPTCHA Verification { #operate-security-recaptcha }

Add Google reCAPTCHA bot verification to the admin login page to lower the risk of automated scripts trying to break into accounts.

1. **Find the section:** On the **Admin Login** tab, find the **reCAPTCHA Authentication** section.
2. **Turn on verification:** Turn on the **Enable reCAPTCHA Authentication** switch. The setting takes effect immediately, and reCAPTCHA verification appears the next time you log in to the admin panel.

![](../../assets/images/ec-管理中心-安全性設定-reCAPTCHA 驗證.en.png)


### Two-Step Verification { #operate-security-2fa }

Two-step verification (2FA) is the most effective defense against account theft. Even if your password leaks, no one can log in without the one-time code from the authenticator on your phone.

1. **Find the section:** On the **Admin Login** tab, find the **Two-factor Authentication Setting** section.
2. **Turn on the feature:** Turn on the **Enable Two-factor Authentication.** switch, and **Installation Steps** expands on the screen.
3. **Install an authenticator:** Install an Authenticator app on your phone (available for iOS and Android).
4. **Link your account:** Scan the QR code on the screen with the Authenticator app, or enter the code shown on the screen manually.
5. **Finish verification:** Enter the six-digit code shown in the Authenticator app in the **Verification Code** field to finish turning it on.
6. **Save your backup codes:** After you turn it on, the system generates verification backup codes. Keep them safe. You can use them to log in when you can't use your authenticator.

    !!! warning "Saving and Using Backup Codes"
        For security, backup codes are shown only once, so save them as soon as you turn the feature on. Each code can be used only once. If you lose them, click Regenerate Backup Codes in the section. To turn off two-step verification, you must first enter your user password to confirm.

![](../../assets/images/ec-管理中心-安全性設定-2FA.en.png)


<div class="grid cards" markdown>

- :lucide-shield-check:{ .lg } [__Two-Step Verification Setup Guide__](setup-manage-two-factor-auth.md)

</div>




## FAQ { #faq-security }

??? quote "What is the difference between the allowlist and the browser cookie IP allowlist?"
    [](){ #faq-security-two-whitelists }
    They serve completely different purposes:

    - **Whitelist**: Limits who can log in to the admin panel. Only IPs on the list can log in, so it is active access control.
    - **Browser Cookie IP Whitelist**: Stops you from being forced to log in again when your IP changes in the same browser. It is a convenience setting.


??? quote "What should I do if I can't get two-step verification codes after changing phones?"
    [](){ #faq-security-2fa-lost-phone }
    If you changed phones or lost your original verification device, you can't generate 2FA codes yourself. Ask the website owner or an admin with the right permissions to turn off 2FA for your account in **Website Management > Security Setting > Two-Step Verification**. Then link your new device again.
