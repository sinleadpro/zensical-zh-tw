---
title: "Meta Ad Account Idle Reclaim Policy and Retention Notes"
description: "Learn the conditions that flag a CYBERBIZ Meta ad account as idle, how to reactivate it, and what happens after release, including how to reapply."
created: 2026-04-27 14:15
last_modified: 2026-07-02 11:44
lang: en-US
type: explanation
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 第三方整合
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
  - 避免廣告帳號被釋出
  - 閒置帳號復原
  - 廣告帳號回收機制
features:
  - 閒置帳號提醒
  - 帳號釋出流程
  - 儲值激活機制
prerequisites:
  - ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/
  - ec/integrations/fb/meta-ads/setup-meta-ad-campaign/
tags:
  - "Meta Ads"
  - "Idle Account"
  - "Account Release"
  - "Ad Account Management"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12881
  - https://www.cyberbiz.io/support/?p=52679
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/meta-ad-idle-account-reclaim/"
comments: ""
search:
  exclude: false
icon: lucide/user-x
hide:
---

![Meta Ad Idle](../../../../assets/images/ec-第三方整合-fb-mbe-meta廣告閒置.en.png){ .hero-page }

## Meta Ad Account Idle Policy { #overview-meta-reclaim }

In CYBERBIZ, if a merchant creates a Meta ad account and does not top up or use it for an extended period, the account enters the idle account handling process.

## Idle Account Definition { #intro-meta-reclaim }

An ad account must **meet both** of the following conditions to be classified as idle:

- [x] **Has never topped up ad spend**: The total ad budget record is 0 or only the system's initial value.
- [x] **Six months since creation without a top-up**: More than six months have passed since the account was created without any actual top-up record.

An idle account means the account has gone unused for an extended period. The system then starts the release process to reclaim resources.

## Account Release Rules and Reminders { #specs-meta-reclaim }

!!! path "Admin Path"
    Merchants can check the status at: **"Third-Party Integrations"** > **"Facebook Settings (Ads / Registration and Login)"** > **"Ad Account Settings"**.

### Expiry Notifications { #specs-meta-reclaim-notifications }

Starting **30, 15, 7, and 1 days** before the account reaches six months, CYBERBIZ sends an email and shows a reminder banner in the admin.

=== ":lucide-mail: Email"

    ![Meta Ad Account Idle Notice - Email](../../../../assets/images/ec-第三方整合-meta廣告帳號閒置通知-電郵.en.png)

=== ":lucide-panel-top: Admin"

    ![Meta Ad Account Idle Notice - Admin](../../../../assets/images/ec-第三方整合-meta廣告帳號閒置通知-後台.en.png)

---

### How to Reactivate { #specs-meta-reclaim-overview-meta-reclaim }

After receiving a reminder, to keep the account's permissions, make sure to [top up](create-meta-ad-account-top-up.md#operate-meta-account-steps-ads){ title="Create a Meta ad account and complete a top-up" } before the deadline. Once the top-up is complete, the account is reactivated and related warnings are cleared automatically.

---

### Turn off Reminders { #specs-meta-reclaim-operate }

If a merchant selects "Don't Remind Me," the system stops sending reminder emails and hides the admin banner. However, **this does not change the release rules**. If the six-month deadline passes without a top-up, the system still releases the account automatically.

![Meta Ad Idle Notice - Turn Off Reminders](../../../../assets/images/ec-第三方整合-meta廣告帳號閒置通知-不再提醒.en.png)

## Impact of Account Release and Reapplication { #operate-meta-reclaim }

Once an account enters the release process and is reclaimed:

*   **Loss of access**: The original merchant **permanently loses operating access to the ad account**.
*   **Reapplication**: If you still need to run ads later, you must **repeat the application process** to create a new ad account. For details, see the "[Create a Meta Ad Account and Complete a Top-Up](create-meta-ad-account-top-up.md){ title="Create a Meta ad account and top up" }" tutorial.

!!! warning "Important"
    We recommend that merchants complete the minimum-threshold top-up soon after creating the account to keep the ad account stable and avoid losing account assets and permissions due to expiration.

## Next Steps { #next-steps-meta-reclaim }

<div class="grid cards" markdown>

- :lucide-wallet:{ .lg }   
  [__Create an Ad Account and Top Up__](create-meta-ad-account-top-up.md){ title="Create a Meta ad account and top up" }       
  Learn the full ad account creation process to avoid the account entering the idle reclaim process.

- :lucide-rocket:{ .lg }   
  [__Launch Ad Campaigns__](setup-meta-ad-campaign.md){ title="Set Up a Meta Ad Campaign" }       
  After the account is reactivated, you can start creating ad campaigns to keep the account active.       

</div>

## FAQ { #faq-meta-reclaim }

??? quote "How can I prevent my ad account from being released?"

    Make sure to complete your first [top up](create-meta-ad-account-top-up.md#operate-meta-account-steps-ads){ title="Create a Meta ad account and complete a top-up" } within six months. Merchants are advised to complete the minimum-threshold top-up soon after creating the account to avoid having the account released due to prolonged inactivity.

??? quote "Can a released account be restored?"

    This cannot be undone. Once an account enters the release process and is reclaimed, the original merchant **permanently loses operating access to the ad account**. If you still need to run ads later, you must **repeat the application process** to create a new account. For details, see the "[Create a Meta Ad Account and Complete a Top-Up](create-meta-ad-account-top-up.md){ title="Create a Meta ad account and top up" }" tutorial.

??? quote "Will selecting "Don't Remind Me" stop my account from being released?"

    No. "Don't Remind Me" only stops reminder emails and hides the admin banner. It **does not change the release rules**. If the six-month deadline passes without a top-up, the system still releases the account automatically.

