---
title: "Create a Meta Ad Account and Top Up"
description: "Create a Meta ad account through CYBERBIZ and complete the top-up."
created: 2026-04-17 17:10
last_modified: 2026-09-07 10:15
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
  - 建立 Meta 廣告帳號
  - 儲值廣告金
  - 設定低餘額提醒
features:
  - 廣告帳號建立
  - 廣告費儲值
  - 儲值提醒
prerequisites:
  - 需先擁有 Meta 企業管理帳號 (Business Manager)
related:
  - ec/integrations/fb/meta-ads/setup-meta-ad-campaign/
tags:
  - Meta
  - Facebook
  - "Ad Account"
  - Top-Up
  - "Business Manager"
acoiv: activate
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 臉書 Facebook 設定（廣告/註冊登入）> 廣告帳戶設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5621
  - https://www.cyberbiz.io/support/?p=17882
permalink: "https://help.cyberbiz.io/ec/integrations/fb/meta-ads/create-meta-ad-account-top-up/"
comments: false
search:
  exclude: false
icon: lucide/circle-plus
hide: []
---

![Meta Ad Settings-CYB Back Office](../../../../assets/images/ec-第三方整合-fb-meta廣告設定.en.png){ .hero-page }

## About Creating a Meta Ad Account { #operate-meta-account }

Create a Meta ad account through CYBERBIZ. The system can issue advertising fee invoices on the merchant's behalf and handle the payment, so you do not need to file overseas taxes with the National Taxation Bureau yourself.

## Steps { #operate-meta-account-steps }

### Create an Ad Account { #operate-meta-account-steps-ads-account-create }

!!! warning "Prerequisites"
    Before you create an ad account, make sure you have **Business Manager account and related asset permissions**. If you have not created one yet, first [register at Meta Business Manager](https://business.facebook.com/).

1. **Admin path**: Go to the admin dashboard and click **"Third-Party Integrations"** > **"Facebook Settings (Ads/Registration Login)"** > **"Ad Account Settings"**.
2. **Start the process**: Click **Get Started**.
3. **Enter your Business Manager ID**: In the pop-up window, enter your [Business Manager ID](#operate-meta-account-steps-query-manage){ data-preview }.
4. **Agree to the terms**: Read the terms, select "I have read", and click **I agree and continue** to finish creating the account.
5. **Naming rule**: The system names the new ad account **"CYBERBIZ registered domain name_儲值"** by default.

![Activate Meta Ad Account](../../../../assets/images/ec-第三方整合-fb-meta廣告帳號-啟用.en.png)

---

### Share Ad Account Permissions { #operate-meta-account-steps-ads-account-perm }

After you create the ad account, share operating permissions with the merchant's Business Manager:

1. **Admin path**: **"Third-Party Integrations"** > **"Facebook Settings (Ads/Registration Login)"** > **"Ad Account Settings"**.
2. **Share the account**: Click **Share Account ID**, then enter the [Business Manager ID](#operate-meta-account-steps-query-manage){ data-preview } you want to share with.

    ![Meta Ad Share Account ID](../../../../assets/images/ec-第三方整合-fb-meta廣告設定-分享帳號編號.en.png)

3. **Confirm the connection**: After sharing, go to [**Business Manager**](https://business.facebook.com/latest/settings) > **"Accounts"** > **Ad Account**, and confirm that the ad account named **"CYBERBIZ registered domain name_儲值"** appears. If it does, the connection is successful.

    ![Meta Business Manager Linked Ad Account](../../../../assets/images/ec-第三方整合-fb-meta企業管理平台-已連結廣告帳號.en.png)

    !!! tip "To assign operating or management permissions to people in Business Manager, configure them on this page."

4. **Operating restriction**: **Before you complete the top-up, the account can only view performance and cannot run ads**. After the top-up is complete, you can assign people to run ads.

    ![Meta Business Manager Ad Account Assign Users](../../../../assets/images/ec-第三方整合-fb-meta企業管理平台-廣告帳號-指派相關人員.en.png)

---

### Find Your Business Manager ID { #operate-meta-account-steps-query-manage }

1. Log in to the [Business Manager settings page](https://business.facebook.com/latest/settings).
2. Click **"Settings"** > **"Business Info"**.
3. The Business Asset Group ID (Business Manager ID) appears below the name.

![Meta Business Asset Group ID](../../../../assets/images/ec-第三方整合-fb-meta企業管理平台-資產管理組合編號.en.png)

!!! note "Related resources: [Meta official documentation](https://zh-tw.facebook.com/business/help/1181250022022158)."

---

### Pixel Setup <small>Pixel</small> { #operate-meta-account-steps-settings-pixel }

To track customer behavior, you need to manually link your existing pixel to the newly created ad account:

1. **Go to Business Manager**: Go to [Settings :lucide-external-link:](https://business.facebook.com/latest/settings), select **Data Source**, then select **"Datasets or Pixels"**.
2. **Add Assets**: Select the pixel to link, then select **Connected Assets** > **"Add Assets"**.
3. **Complete the link**: Select the ad account named "Store Name_儲值" and confirm.

![Business Manager Link Pixel to Ad Account](../../../../assets/images/ec-第三方整合-fb-meta企業管理平台-廣告帳號-連結像素.en.gif)

---

### Top up Ad Funds { #operate-meta-account-steps-ads }

!!! info "Top-Up Rules and Fee Calculation"

    - **Top-up limit**: **The minimum top-up amount is NT$9,000**.
    - **Fee calculation**: Total charge = Ad budget × Service fee N% × Tax 5%.
        - **Enterprise plan**: 4% service fee
        - **Standard plan**: 5% service fee
    - **Validity period**: Ad budget has **no time limit** after you top up. It will not expire if it is unused for one month.
    - **Idle account reminder**: If an account has **not been topped up for six months** after it is created, it is considered an "idle account" and will be released by the system. The merchant will then lose operating permissions for that account.

Merchants must top up funds in the admin dashboard before they can start running ads:

1. **Go to the settings page**: Log in to the CYBERBIZ admin dashboard and go to **Third-Party Integration > Facebook> Ad Account Settings**.
2. **Set the top-up amount**: In the **Top-up advertising fee** amount field, enter the amount you want to top up, then click **Confirm** to apply the changes.
3. **(Optional) Set a low-balance reminder**: In the **Top-up Notification** section at the top of the same page, customize the reminder threshold as needed.

    * **Custom ratio**: Enter the percentage of the budget that triggers a notification (for example, 80% to send a notification).
    * **Turn on notifications**: Make sure the toggle is set to **On** to avoid ads being interrupted when the budget runs out.

![Meta Ad Top-Up](../../../../assets/images/ec-第三方整合-fb-廣告帳號設定-廣告費儲值.en.png)

## Next Steps { #next-steps-meta-account }

<div class="grid cards" markdown>

- :lucide-megaphone:{ .lg }  
  [Set up an ad campaign](setup-meta-ad-campaign.md){ title="Set Up Meta Ad Campaign" }  
  After you complete the steps above, you can set up an ad campaign and run ads directly in the CYBERBIZ admin dashboard.

</div>

## FAQ { #faq-meta-account }

??? quote "Will ad budget expire after I top up?"

    Ad budget has **no time limit** after you top up. It will not expire if it is unused for one month.

??? quote "Will an idle ad account be released?"

    If an account has **not been topped up for six months** after it is created, it is considered an "idle account" and will be released by the system. The merchant will then lose operating permissions for that account.

??? quote "What should I do if my account was released?"

    After an account is released, merchants need to [create a new ad account](#operate-meta-account-steps-ads-account-create) and complete a top-up before they can use Meta ad delivery again.

