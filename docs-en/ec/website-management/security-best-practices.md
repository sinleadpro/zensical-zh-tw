---
title: "Security Overview and Best Practices"
description: "An overview of security measures, admin panel settings paths, and an incident response guide to fully protect your website and customer personal data."
created: 2026-06-09 17:07
last_modified: 2026-08-05 17:29
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
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 盤點網站安全防護項目
  - 了解資安事件應變流程
features:
  - "Two-Step Verification"
  - "IP Allowlist"
  - reCAPTCHA
  - 會員註冊簡訊機器人防護
  - Cookie_驗證_IP_白名單
  - 自動登出時間
  - 會員個資部分隱碼
  - 訪問限制地區黑名單
  - 網站密碼
  - 信用卡 3D 驗證
  - SSL 憑證
prerequisites: []
related:
  - ec/website-management/admin-security-settings/
  - ec/website-management/bot-protection-settings/
  - ec/website-management/add-admin-set-permissions/
  - ec/website-management/member-security-settings/
  - ec/payments-and-logistics/setup-credit-card-3d-verification/
  - ec/website-appearance/site-settings/setup-right-click-protection/
tags:
  - "Security Protection"
  - 二階段驗證
  - IP 白名單
  - "Admin Panel Security"
  - "Data Protection"
  - "Information Security"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 網站權限
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3549
  - https://www.cyberbiz.io/support/?p=14216
permalink: "https://help.cyberbiz.io/ec/website-management/security-best-practices/"
comments: false
search:
  exclude: false
icon: lucide/shield
hide: []
---

## About Security Protection { #intro-security-guide }

Information security works best when merchants help by completing each setting. This page is an overview of best practices that helps you see at a glance which protections to set up. For detailed steps for each feature, follow the matching link to its guide. Most features are in the admin panel under **Website Management > Security Setting**, and some are in User Account Settings, payment settings, or domain settings.



## Core Login Protection { #operate-security-guide-core }


!!! tip "Recommended Priority"
    If you are just starting to review your security, do these three things first: turn on **two-step verification**, set up an **IP allowlist**, and turn on **admin panel login reCAPTCHA**. These three are the most effective at preventing account theft.

<div class="grid cards" markdown>

-   :lucide-shield-check:{ .lg .middle } __Two-Step Verification (2FA)__

    ---

    After entering the account and password, users also need a dynamic code from a mobile authenticator to log in. Even if a password leaks, hackers can't get past the second verification step.

    [:lucide-arrow-right: Setup steps](admin-security-settings.md#operate-security-2fa)

-   :lucide-network:{ .lg .middle } __IP Allowlist__

    ---

    Only IP addresses on the list can log in to the admin panel. Don't use dynamic IPs such as a phone's Wi-Fi hotspot, or you may be unable to log in.

    [:lucide-arrow-right: Setup steps](admin-security-settings.md#operate-security-ip-whitelist)

-   :lucide-bot:{ .lg .middle } __Admin Panel Login reCAPTCHA__

    ---

    Add bot verification to the admin panel login page to reduce automated script attacks.

    [:lucide-arrow-right: Setup steps](admin-security-settings.md#operate-security-recaptcha)

</div>

---

## Advanced Access Control { #operate-security-guide-access-control }

After you finish the core protections, strengthen login and access control as needed.

<div class="grid cards" markdown>

-   :lucide-cookie:{ .lg .middle } __Browser Cookie Verification IP Allowlist__

    ---

    If the IP changes while the same browser is in use, the system asks you to log in again, which stops others from stealing cookies to impersonate you. If your network IP changes often and this gets in your way, add trusted IPs to this list.

    [:lucide-arrow-right: Setup steps](admin-security-settings.md#operate-security-cookie-whitelist)

-   :lucide-clock:{ .lg .middle } __Automatic Logout Time__

    ---

    Set how long the admin panel can stay idle before it logs out automatically (4 hours to 7 days). This lowers the risk of someone else using your computer.

    [:lucide-arrow-right: Setup steps](admin-security-settings.md#operate-security-logout-timer)

-   :lucide-globe-off:{ .lg .middle } __Overseas IP Login Restriction__

    ---

    If you run a cross-border business or need to log in from overseas, consider whether to restrict overseas logins. Because this involves account authorization, contact CYBERBIZ Customer Service to confirm how to activate it.

-   :lucide-bot:{ .lg .middle } __Member Registration SMS Verification__

    ---

    Add Cloudflare Turnstile bot verification before a verification code is sent during member registration. This reduces the cost of malicious scripts triggering large numbers of SMS messages (especially international SMS).

    [:lucide-arrow-right: Setup steps](bot-protection-settings.md#operate-security-sms-bot-protection)

</div>

---

## Data Security and Permission Management { #operate-security-guide-data }

Protect customer personal data, limit high-risk permissions, and make audits a habit.

<div class="grid cards" markdown>

-   :lucide-download:{ .lg .middle } __Minimize Export Permissions__

    ---

    Keep the **Customer export** and **Order export** permissions to a minimum, and grant them only to staff who need them.

    [:lucide-arrow-right: Setup steps](add-admin-set-permissions.md#operate-admin-perms-edit)

-   :lucide-eye-off:{ .lg .middle } __Partially Masked Member Information__

    ---

    Mask member names, mobile numbers, addresses, and other details when you print order details.

    [:lucide-arrow-right: Setup steps](member-security-settings.md#operate-security-pdpa)

-   :lucide-search:{ .lg .middle } __Audit Logins Regularly__

    ---

    Regularly check the admin list in User Account Settings, and watch for unusual actions or logins from unknown IPs.

</div>

---

## Transaction and Domain Security { #operate-security-guide-transaction }

Protect the checkout process, your SMS costs, and data transfer on your website.

<div class="grid cards" markdown>

-   :lucide-credit-card:{ .lg .middle } __Credit Card 3D Secure__

    ---

    Shoppers must enter an SMS verification code to complete payment, which lowers the risk of card fraud. Check with CYBERBIZ Customer Service about activation and which payment services support it.

    [:lucide-arrow-right: Setup guide](../payments-and-logistics/setup-credit-card-3d-verification.md)


-   :lucide-lock:{ .lg .middle } __SSL Certificate__

    ---

    Protects data transferred between your website and customers. CYBERBIZ domains already include SSL. If you use your own domain, SSL usually comes with your plan or must be renewed separately.

-   :lucide-copyright:{ .lg .middle } __Copy Protection for Web Pages__

    ---

    Some themes and storefront settings can stop customers from copying text or downloading images to protect your original content. Whether this is available depends on your theme settings.

    [:lucide-arrow-right: Setup guide](../website-appearance/site-settings/setup-right-click-protection.md)

</div>

---

## Incident Response { #operate-security-guide-incident }

If you think your website has been compromised or a security incident has occurred, handle it from both the brand side and your own accounts.

### Brand-Side Response { #operate-incident-brand }

When you confirm a security incident, follow these steps to lower your legal risk:

1. **Post anti-fraud warnings on your pages**: Add preventive warnings to important pages of your website (such as banners and the checkout page). Without these warnings, you may face higher legal risk if a customer sues.
2. **Record affected customer information**: Record the number of reports, when they happened, order numbers, the scam script used, caller ID numbers, and so on.
3. **Confirm financial losses**: Check whether customers actually lost money.
4. **Report to 165 and the police**: Tell customers that your brand will report the case to the 165 Anti-Fraud Hotline and the police, to show that your company takes the fraud seriously.
5. **Warn customers proactively**: Consider sending an extra email or SMS to warn all customers to watch out for scams.

??? example "Example Anti-Fraud Notice"
    ![Anti-fraud notice](../../assets/images/ec-security-best-practices-banner-example.en.png)

---

### Secure Your Own Accounts { #operate-incident-account }

Complete the following recovery steps in order:

1. **Review activity logs**: In the admin panel, check **Overview** for logins from unusual IPs, and keep the records. See [how to check](#faq-security-guide-check).
2. **Change passwords**: Change the passwords of all admin panel accounts right away.
3. **Clear browser data**: Clear cookies and cache to prevent session hijacking.
4. **Confirm protections are on**: Make sure [two-step verification](admin-security-settings.md#operate-security-2fa) and the [IP allowlist](admin-security-settings.md#operate-security-ip-whitelist) are both turned on.
5. **Remove unknown admins**: Go to **Website Management > User Account Settings** to review and remove unauthorized accounts.

??? example "Case Study: Data Leak Risk from a Phishing Email"
    [](){ #specs-security-phishing }

    This case is based on a real incident and shows how a hacker used a phishing email to break in step by step.

    ![Phishing email example](../../assets/images/ec-security-best-practices-phishing-email.en.png)

    **What happened**

    1. **Phishing email**: The merchant received a phishing email with a forged sender, clicked it, and had their login credentials stolen.
    2. **Owner access gained**: The scammer logged in to the merchant's website owner account.
    3. **Co-admin created**: Using the owner's permissions, the scammer added a co-admin account and set it up with their own email address.
    4. **Data exported around protections**: The scammer used the co-admin account to export customer or order data, and **the data was sent straight to the scammer's email**, causing a data leak.

    **Key lessons**

    - Turning on **two-step verification (2FA)** fully blocks step 2 (even if the password is phished, the second verification step stops the login).
    - Setting up an **IP allowlist** further limits where logins can come from.
    - **Audit co-admin permissions regularly**, and remove any unknown admins right away.
    - Relying on "only the owner receives export emails" is not enough, because a co-admin can set their own email to receive export files.

## FAQ { #faq-security-guide }

??? quote "If I only have time for one thing, what is most effective?"
    [](){ #faq-security-guide-priority }
    Turn on **two-step verification** first. Even if a password leaks, no one can log in without the dynamic code from the mobile authenticator, so it is the most cost-effective defense. When you have time, add an IP allowlist and admin panel login reCAPTCHA.

??? quote "Will these protections affect customer shopping or my own admin panel work?"
    [](){ #faq-security-guide-impact }
    It depends on the feature:

    - Affects how you and your staff log in to the admin panel: two-step verification, IP allowlist, automatic logout, and admin panel login reCAPTCHA.
    - Affects how customers browse the storefront: website password and the location blacklist.
    - Affects the customer registration flow: member registration SMS verification (customers must pass bot verification before a code is sent).
    - Check the impact before you change a setting. For example, add your own IP to the list before you turn on the IP allowlist.

??? quote "How can I quickly check whether my account has been compromised?"
    [](){ #faq-security-guide-check }

    Use these three steps to check quickly:

    1. **Check the admin list**: Go to **Website Management > User Account Settings** and make sure every admin is approved by your company. If you find an unknown account, remove it right away.
    2. **Check the Overview activity log**: In the admin panel, go to **Overview** and look for recent logins by unauthorized people or unusual exports.
    3. **Check the log details**: In the activity log, review login IPs, login emails, and export records to spot suspicious IPs or unauthorized data exports.

    ![Admin panel Overview activity log](../../assets/images/ec-overview-operation-records.en.png)

??? quote "What should I do first if I find a suspicious login or think my account was compromised?"
    [](){ #faq-security-guide-incident-first }
    We recommend that you immediately:

    - Change the passwords of all admin panel accounts, and make sure two-step verification and the IP allowlist are turned on.
    - Keep the records of unusual logins, post an anti-fraud warning on your website, and report the case to 165 and the police.
    - Contact CYBERBIZ Customer Service to help check your account status.


