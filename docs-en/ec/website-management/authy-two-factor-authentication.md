---
title: "Enable Two-Step Verification with Authy"
description: "Use the Authy app to set up two-step verification (2FA) for your CYBERBIZ account and improve account security."
created: "2026-03-16 21:41"
last_modified: 2026-07-02 19:21
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
  - "Two-Step Verification"
  - "Account Security"
  - 登入驗證
features:
  - Authy
  - 二階段驗證
  - 2FA
prerequisites: []
related:
  - ec/website-management/setup-manage-two-factor-auth/
tags:
  - 二階段驗證
  - Authy
  - 帳號安全
  - "Login Security"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 安全性設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=12873
permalink: "https://help.cyberbiz.io/ec/website-management/authy-two-factor-authentication/"
comments: false
search:
  exclude: false
icon: lucide/shield-ellipsis
hide: []
---

## About Authy { #intro-authy }

There are many authenticator apps on the market (such as Google Authenticator), but Authy has these advantages:

- **Multi-device sync**: Supports iOS, Android, Windows, macOS, and a Chrome extension, so you can access the same codes on several devices.
- **Backup and restore**: Provides encrypted backups, so you can restore your accounts quickly even if you lose your phone.
- **High compatibility**: Fully compatible with every website that supports Google Authenticator.

---

## Steps { #operate-authy }

### Step 1: Download and Register { #operate-authy-install }

1.  Download the **Authy app** from the [official website :lucide-external-link:](https://authy.com/download/) or your app store.
2.  **Register with your mobile number**: Open the app, select your country code (+886 for Taiwan), and enter your mobile number.
3.  **Verify your identity**: Choose to receive a verification code by SMS or phone call, and enter it to finish creating your account.

![Authy registration page](../../assets/images/ec-管理中心-安全性設定-二階段驗證-authy-註冊.en.png){ title="Authy registration page" }

---

### Step 2: Add Your CYBERBIZ Account { #operate-authy-add-account }

1.  Open the Authy app and tap **+ Add Account**.
2.  **Scan the code**: Use your phone camera to scan the **QR code** shown on the [Security Setting](setup-manage-two-factor-auth.md){ title="Set up and manage two-step verification" } page in the CYBERBIZ admin panel.
3.  **Enter the key manually**: If you can't scan the code, tap Enter key manually and enter the key shown in the admin panel.
4.  **Save the account**: When you finish, the website's verification account appears at the bottom of the app.

![Authy add account](../../assets/images/ec-管理中心-安全性設定-二階段驗證-authy-add-cyb-account.en.png){ title="Authy add account" }

---

### Step 3: Get a One-Time Code { #operate-authy-code }

1.  Tap the account icon in the app to show a **6-digit verification code**.
2.  **Time limit**: The code refreshes every **30 seconds**. Enter it on the login page before the countdown ends.

![Authy one-time code](../../assets/images/ec-管理中心-安全性設定-二階段驗證-authy-動態驗證碼.en.png){ title="Authy one-time code" }

---

### Step 4: Turn on Backups <small>Strongly recommended</small> { #operate-authy-backup }

1.  Go to your account settings, find **Authenticator Backups**, and turn it on.
2.  **Set a backup password**: This password encrypts your backup data.
3.  **Important**: The backup password is **not** stored on Authy's servers. If you lose it, it can't be recovered or reset, so be sure to record it and keep it safe.

![Authy backup settings](../../assets/images/ec-管理中心-安全性設定-二階段驗證-authy-backup.en.png){ title="Authy backup settings" }

---

## Notes { #prerequisites-authy }
*   **Keep your backup codes**: After you turn on 2FA in the CYBERBIZ admin panel, the system provides **10 backup codes**. Download them and write them down so you can log in in an emergency if you lose your phone.
*   **Time sync**: If you enter the correct code but still can't log in, check that your phone's date and time are set to sync automatically. A time difference makes codes invalid.

## FAQ { #faq-authy }

??? quote "Which devices does Authy support?"

    Authy supports iOS, Android, Windows, macOS, and a Chrome extension, so you can access your codes on several devices.

??? quote "How do I log in if I lose my phone?"

    When you turn on 2FA, the system provides 10 backup codes. Use a backup code to log in in an emergency. Keep your backup codes in a safe place.

??? quote "How long is a verification code valid?"

    The code refreshes every 30 seconds. Enter it on the login page before the countdown ends.

