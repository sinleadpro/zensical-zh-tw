---
title: "Automated Ads System (Google Shopping Ads)"
description: "Connect Google Shopping ads and use the CYBERBIZ automated ads system to manage ad delivery, budgets, and performance tracking."
created: 2026-01-15 10:00
last_modified: 2026-07-02 14:22
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
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 建立 Google 購物廣告活動
  - 串接 GMC 帳號
  - 管理廣告預算與儲值
features:
  - 自動化廣告系統
  - Google 購物廣告
  - GMC 帳號代管
  - 廣告成效分析
prerequisites:
  - 需有 Google 帳號
  - 需完成廣告儲值
related:
  - ec/website-management/setup-store-basic-info/
  - ec/integrations/google/setup-google-merchant-center/
  - ec/integrations/references/automated-ads-statuses/
  - ec/products/create-and-manage/create-update-products/
  - ec/business-intelligence/ad-analytics-guide/
tags:
  - GMC
  - Google
  - "Google Ads"
  - "Ad Delivery"
  - ROAS
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 自動化廣告系統。
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=8203
  - https://www.cyberbiz.io/support/?p=34930
permalink: "https://help.cyberbiz.io/ec/integrations/google/automated-ads-system/"
comments: false
search:
  exclude: false
icon: lucide/bot
hide: []
---

![Automated Ads System](../../../assets/images/ec-第三方整合-自動化廣告系統.en.png){ .hero-page }

## Automated Ads Overview { #intro-automated-ads }

**Automated Advertising System** integrates mainly with **Google Shopping Ads**, so merchants do not need to create their own ad creatives. The system automatically syncs storefront product information to Google, so products appear as image cards in search results for related keywords. This helps attract targeted traffic and drive purchases.

??? example "Google Shopping Ad Results"
    1. When a customer searches for a keyword on Google and Google determines that the keyword is relevant to your products, the products appear as image cards on the search results page.
    2. After the customer clicks the ad, they go to the product page to complete the purchase.

    ![Google Shopping ad example](../../../assets/images/ec-google-ads.zh-tw.en.png)

## Page Features Overview { #overview-automated-ads }

After activation, the automated ads system provides three tabs:

| Tab | Purpose |
| :-- | :-- |
| [Google Ads Settings](#operate-automated-ads-campaign) | Set the campaign name and daily budget, and control the delivery status (pause/resume) |
| [Campaign Management](#operate-automated-ads-manage) | View ad budget progress and total ad spend, and set top-up reminders |
| [Ad Top-Up](#operate-automated-ads-charge) | Add ad funds and view the current remaining ad balance and top-up details |

## Prerequisites and Limitations { #prerequisites-automated-ads }

- [x] **Company Contact Information**: Before activation, complete your [company contact information](../../website-management/setup-store-basic-info.md#operate-general-preferences-company-info){ title="Set Up Basic Site Information" } in **General Settings**; otherwise, you cannot complete the GMC integration.
- [x] **GMC Account**: Select **CYBERBIZ Managed** or provide **Merchant-owned account**. Choose one of the two options to complete the integration.

## Billing Rules { #pricing-automated-ads }

| Item | Rule |
| :-- | :-- |
| Minimum Top-Up Amount | When applying for activation for the first time, the minimum ad fund top-up is $9,000 |
| Service Fee | No service fee for the first top-up. After activation, a 5% service fee applies to each top-up.[^fee] |
| Suggested Daily Budget | We recommend at least NT$300 per day. During marketing periods, you can raise it 2 to 4 times. |

[^fee]: After activation, a 5% service fee applies to each top-up. Credit card top-ups incur an additional 2.5% card processing fee.

## Setup Steps { #operate-automated-ads }

### Apply for Activation and First Top-Up { #operate-automated-ads-apply }

1. **Go to the page**: Go to the back office and click <strong class="inline-path">Third-Party Integrations > Automated Ads System</strong>.
2. **Apply for enabling**: On the page, click **Apply for enabling** to go to the activation settings.
3. **Complete the First Top-Up**: Enter the ad fund amount as prompted on the screen and complete the payment. The first top-up has **no service fee**.
4. **Wait for Activation**: After a successful top-up, the system starts the activation process, which takes about 3 to 5 business days. You will be notified by email when it is complete.

![Automated ads activation and top-up](../../../assets/images/ec-第三方整合-自動化廣告系統-開通儲值.en.gif)

---

### Select GMC Integration Method { #operate-automated-ads-gmc }

After the first top-up succeeds, the system asks you to choose how to connect your Google Merchant Center (GMC) account. Each website can declare only one GMC ownership, so choose carefully and do not change it arbitrarily.

![Select GMC integration method](../../../assets/images/ec-第三方整合-自動化廣告系統-選擇串接gmc方式.en.png)

=== "CYBERBIZ Managed (Best for Beginners)"
    !!! tip "Select CYBERBIZ Managed. If ad delivery has issues, the system can quickly troubleshoot them, so you do not need to do anything yourself."

    Best for merchants who do not yet have a GMC account. CYBERBIZ automatically creates the account and manages it on their behalf.

    1. In the GMC integration method, select **CYBERBIZ Managed**.
    2. If the screen shows that website ownership has already been declared, click **Confirm** to continue (click **Back** to choose your own account instead).
    3. CYBERBIZ will transfer the GMC declaration rights. Wait for activation to complete.

    ![Automated ads CYBERBIZ managed activation in progress](../../../assets/images/ec-第三方整合-自動化廣告系統-CYBERBIZ代管開通中.en.png)

    !!! warning "After you select CYBERBIZ Managed, do not apply for a separate GMC account yourself, to avoid ad delivery issues. You cannot log in to view GMC data for the managed account."

=== "Merchant's Own Account"
    Best for merchants who already have a GMC account.

    1. In the GMC integration method, select **Merchant-owned account**.
    2. Enter your GMC account (the nine-digit number in the upper-right corner of the GMC back office). (See the [GMC Integration Setup Guide](setup-google-merchant-center.md){ title="Set Up Google Merchant Center and Sync CYBERBIZ Products" })
    3. Follow the on-screen prompts to share access with CYBERBIZ's Google Ads account from the GMC back office and complete the Google Ads ID binding.

    ![Automated ads own account activation in progress](../../../assets/images/ec-第三方整合-自動化廣告系統-自有帳號開通中.en.png)

    !!! info "The system checks the binding status daily. Once binding is complete, activation happens automatically."

---

### Set up Google Ad Campaign { #operate-automated-ads-campaign }

After activation, go to the **Google Ads Settings** tab to set up your Shopping ad campaign:

1. **Enter the Campaign Name**: In the **Ad Campaign Name** field, enter the campaign name.
2. **Set the Daily Budget**: In the **Set Budget** field, enter your average daily budget (we recommend at least NT$300[^budget]).
3. **Confirm and Save**: Click **Confirm and Save**. The system automatically creates an ad account and connects GMC product data. Ad delivery starts after Google approves the campaign (about 2 to 3 days).
4. **Adjust Delivery Status**: In the **Shopping Ad Status** section, you can click **Pause Ad** or **Resume Ad** at any time to control the [ad delivery status](../references/automated-ads-statuses.md#automated-ads-delivery-status){ data-preview }.

![Google Ads settings](../../../assets/images/ec-第三方整合-自動化廣告-google廣告設定.en.png)

[^budget]: During marketing campaign periods, we recommend raising the daily budget 2 to 4 times so ads can deliver a stronger combined effect.

---

### Ad Top-Up { #operate-automated-ads-charge }

Remember to top up before ad funds run out to avoid ads being paused:

1. Go to the **Ad Top-Up** tab and view **Remaining advertising fee**.
2. Enter the top-up amount (the system shows the actual available ad funds and service fee), then click **Confirm Deposit**. (A window will pop up for you to enter information after you click.)
3. After payment is complete, the invoice is automatically emailed to your email address, and the top-up record appears in **Charge List**.

![Ad top-up](../../../assets/images/ec-第三方整合-自動化廣告-廣告儲值.en.png)

---

### View Performance and Set Top-Up Reminders { #operate-automated-ads-manage }

In the **Campaign Management** tab, monitor ad spend and budget:

1. **View Ad Budget**: The **Ads Budget** section shows the start date, amount used, and total budget.
2. **View All Ads**: The **All Ads** list shows each ad's daily budget, ad spend, and delivery status.
3. **Set Top-Up Reminders**: In **Top-up Notification**, set a budget usage percentage. When spend exceeds that percentage, the system notifies you to top up as soon as possible.

![Campaign management](../../../assets/images/ec-第三方整合-自動化廣告-活動管理.en.png)

## Important Rules and Limitations { #specs-automated-ads }

!!! warning "Each website can declare only one GMC ownership. Do not apply repeatedly or change it arbitrarily, to avoid ad delivery errors. To change the connected GMC source, contact customer support."

Product information is the ad content. Follow these guidelines to help pass Google review:

- [x] **Product Images**: Do not include promotional text, slogans, or brand watermarks. Use [clean product images](../../products/create-and-manage/create-update-products.md#gmc-picture-specs). [Learn about GMC image requirements :lucide-external-link:](https://support.google.com/merchants/answer/6324350#Image_guidelines)
- [x] **Product Name**: Make it clear and include key information such as brand and specifications (size, color, model).
- [x] **Prohibited Products**: Do not advertise adult content, alcoholic beverages, copyrighted content, gambling, or unapproved medicinal supplements. [Learn about prohibited content :lucide-external-link:](https://support.google.com/merchants/answer/6149970?hl=zh-Hant#con)

## Next Steps { #next-steps-automated-ads }

<div class="grid cards" markdown>

- :lucide-chart-column-increasing:{ .lg }  
  [__Ad Analysis Guide__](../../business-intelligence/ad-analytics-guide.md)  
  View real-time Google Shopping ad performance data in the Ad Analysis Report.

- :lucide-store:{ .lg }  
  [__GMC Integration Settings__](setup-google-merchant-center.md)  
  Set up Google Merchant Center and sync CYBERBIZ product data.

</div>

## FAQ { #faq-automated-ads }

??? quote "How long after applying for activation before ad delivery can start?"
    [](){ #faq-automated-ads-activation-time }
    After a successful top-up, activation takes about 3 to 5 business days, and you will be notified by email when it is complete. After you finish and save the ad settings, you still need to wait for Google to approve the ads (about 2 to 3 days) before delivery begins.

??? quote "Why haven't I seen any ad data after my ads started running?"
    - Google ad review takes about 3 to 5 days. Once the ads pass review, they start running automatically, so please allow time for them to start. (If your ads still do not start running, contact customer support.)
    - If you are using your own GMC account, log in to your GMC back office to check.

        1. In the left menu, go to **Products > Diagnostics** and check whether valid product items were uploaded successfully.
        2. In the left menu, go to **Products > Feeds** and check whether the product addition method is correct. See [GMC Integration Settings](setup-google-merchant-center.md){ title="Set up Google Merchant Center and sync CYBERBIZ products" }
        3. In the left menu, go to **Growth > Manage Programs > Shopping Ads** and click **Get Started / Fix Incomplete Items**. Also confirm that all items in the Shopping ad plan are checked *except* **Add Billing Details** and **Create Ad Campaign**.

??? quote "What should the daily ad budget be?"
    [](){ #faq-automated-ads-budget }
    We recommend a daily budget of at least NT$300. If you have marketing campaigns planned, raise the budget 2 to 4 times during the campaign period so ads can deliver a stronger combined effect.

??? quote "Why does ad spend exceed the daily budget on some days?"
    [](){ #faq-automated-ads-overspend }
    Google optimizes your spend based on daily traffic changes and cumulative spend for the month. A single day can reach up to twice the budget, but total monthly spend will not exceed “daily budget × 30.4”. For details, see [Google Help Documentation :lucide-external-link:](https://support.google.com/google-ads/answer/1704443).

??? quote "Do ad top-up funds expire?"
    [](){ #faq-automated-ads-expiry }
    There is no expiration date, but keep an eye on your remaining ad funds to avoid ads being paused due to insufficient balance. You can set a budget usage percentage notification in **Top-up Notification**.

??? quote "Can I use my own Google Ads account?"
    [](){ #faq-automated-ads-own-ads }
    No. When you use the automated ads system, CYBERBIZ creates a dedicated ad account for you.

??? quote "Can I use my own GMC account?"
    [](){ #faq-automated-ads-own-gmc }
    Yes. Select **Merchant-owned account**, then share GMC access with CYBERBIZ's Google Ads account to complete the binding.

## References { #reference-automated-ads }

- [Ad Delivery and Activation Status Reference](../references/automated-ads-statuses.md)
- [Google Shopping Ads Policies (Official Documentation) :lucide-external-link:](https://support.google.com/merchants/answer/6149970?hl=zh-Hant)

<!---->
<!-- --- -->
<!---->
<!-- ## Automated Ads System Overview -->
<!---->
<!-- **Automated Advertising System** integrates mainly with **Google Shopping Ads**. Its core advantage is that merchants do not need to create extra ad creatives. The system automatically syncs storefront product information to Google, so products appear as image cards in related keyword search results, which helps attract targeted traffic and drive purchases. -->
<!---->
<!-- ### Google Shopping Ad Results -->
<!---->
<!-- 1. When someone searches for a keyword on Google and Google determines that the keyword is related to your product, your product appears on the search results page as a product image card.   -->
<!-- 2. After a user clicks the ad, they go to the product page to shop.  -->
<!---->
<!-- ![](../../../assets/images/ec-google-ads.zh-tw.en.png) -->
<!---->
<!-- ## Activation Steps -->
<!---->
<!-- 1.  **Access path**: Go to the admin back office and click <strong class="inline-path">Third-Party Integrations > Automated Ads System</strong>. -->
<!-- 2.  **Activate**: Click the Apply for Activation button and complete an **ad fund top-up** to start the next setup steps. After topping up, return to the settings page to continue. -->
<!---->
<!--     ![Third-party integration automated ads activation and top-up](../../../assets/images/ec-第三方整合-自動化廣告系統-開通儲值.en.gif) -->
<!---->
<!--     !!! info "The first top-up has no service fee. A 5% service fee applies starting from the second top-up." -->
<!---->
<!-- 3.  **Choose a Google Merchant Center (GMC) integration method**: -->
<!--     *   [**Create a CYBERBIZ Managed GMC Account**](#cyberbiz-代管): Best for beginners. If ad delivery has issues, the system can troubleshoot quickly, but merchants cannot log in to that GMC account to view its data. -->
<!--     *   [**Connect Your Existing GMC Account**](#商家自有帳號): Manually enter your own GMC number, then follow the guide to complete the Google Ads ID binding. -->
<!---->
<!--     ![Third-party integration automated ads select integration method](../../../assets/images/ec-第三方整合-自動化廣告系統-選擇串接gmc方式.en.png) -->
<!---->
<!--     !!! warning "Each website can declare only one GMC ownership. Do not change it arbitrarily or apply repeatedly, to avoid ad errors." -->
<!---->
<!-- --- -->
<!---->
<!-- #### CYBERBIZ Managed -->
<!---->
<!-- 1. Enable setup: Click **CYBERBIZ Managed**.   -->
<!-- 2. If the **Website ownership has already been declared** message appears, click **Confirm** to continue. Click **Back** to use your own merchant account instead.   -->
<!-- 3. CYBERBIZ will complete the subsequent GMC declaration rights transfer. Merchants should wait for activation.  -->
<!---->
<!-- ![Automated ads system CYBERBIZ managed activation in progress](../../../assets/images/ec-第三方整合-自動化廣告系統-CYBERBIZ代管開通中.en.png) -->
<!---->
<!-- !!! warning "After the CYBERBIZ managed GMC account is created, do not apply for a separate GMC account yourself, to avoid ad delivery issues." -->
<!-- --- -->
<!---->
<!-- #### Merchant's Own Account -->
<!---->
<!-- 1.  Enable setup: Click **Merchant-owned account**. -->
<!-- 2.  **GMC account**: Enter your own GMC account number (a nine-digit code, which you can find in the upper-right corner of the GMC back office). If you have not created a GMC account yet, see the [GMC Integration Setup Guide](setup-google-merchant-center.md). -->
<!-- 3. Follow the back office prompts to complete the Google Ads ID binding in the GMC back office. -->
<!---->
<!-- ![Automated ads system own account activation in progress](../../../assets/images/ec-第三方整合-自動化廣告系統-自有帳號開通中.en.png) -->
<!---->
<!-- !!! info "The system checks daily whether the merchant has completed binding. Activation happens once binding is complete." -->
<!---->
<!-- ## Ad and Top-Up Settings -->
<!---->
<!-- The automated ads system currently supports Google Shopping ad campaigns. [After activation](#申請開通步驟), configure the following settings from these paths: -->
<!---->
<!-- 1. Log in to the CYBERBIZ admin back office and go to **Third-Party Integration > Automated Ads System.** -->
<!-- 2. Configure the related tabs in order: [Google Ads Settings](#google-廣告設定), [Campaign Management](#活動管理), and [Ad Top-Up](#廣告儲值). -->
<!---->
<!-- ### Google Ads Settings   -->
<!---->
<!-- After activation, you can customize the campaign name on this page, set the average daily budget, and switch the delivery status (on or off) at any time. -->
<!---->
<!-- - Campaign name: Enter the campaign name. -->
<!-- - Budget: The daily ad budget. If you have marketing campaigns planned, consider raising the budget 2 to 4 times during the campaign period so ads can deliver a stronger combined effect. -->
<!-- - Delivery status: Turn the ad campaign on or off. -->
<!---->
<!-- ![Automated ads Google Ads settings](../../../assets/images/ec-第三方整合-自動化廣告-google廣告設定.en.png) -->
<!---->
<!-- --- -->
<!---->
<!-- ### Campaign Management   -->
<!---->
<!-- View budget spend progress.   -->
<!---->
<!-- - Ad budget: View the ad budget. -->
<!-- - All ads: View ad setting information. -->
<!---->
<!-- ![](../../../assets/images/ec-第三方整合-自動化廣告-活動管理.en.png) -->
<!---->
<!-- --- -->
<!---->
<!-- ### Ad Top-Up   -->
<!---->
<!-- - Top up ad funds.  -->
<!-- - After topping up, the invoice is automatically emailed to the address you provided. -->
<!---->
<!-- !!! info "The first top-up has no service fee. Starting with the second top-up, the service fee is 5%." -->
<!---->
<!-- ![](../../../assets/images/ec-第三方整合-自動化廣告-廣告儲值.en.png) -->
<!---->
<!-- ## Google Ads Product Setup Best Practices -->
<!---->
<!-- Product information is the ad content. Follow these guidelines to help ensure approval: -->
<!---->
<!-- - [x] **Product images**: Do not include promotional text, slogans, or brand watermarks. Use [clean product images](../../products/create-and-manage/新增單一商品.md#google-圖片規範){ data-preview }. [Learn about GMC image requirements :lucide-external-link:](https://support.google.com/merchants/answer/6324350#Image_guidelines) -->
<!-- - [x] **Product name**: Must be clear and include key information such as brand name and specifications (size, color, model). -->
<!-- - [x] **Prohibited products**: The system prohibits ads for adult content, alcoholic beverages, copyrighted content, gambling, and unapproved medicinal supplements. [Learn about GMC prohibited content :lucide-external-link:](https://support.google.com/merchants/answer/6149970?hl=zh-Hant#con) -->
<!-- ## Next Steps -->
<!---->
<!-- <div class="grid cards" markdown> -->
<!---->
<!-- - :lucide-chart-column-increasing:{ .lg }    -->
<!--   ](../../business-intelligence/ad-analytics-guide.md)s/廣告分析指南.md){ title="Ad Analysis Guide" }      -->
<!--   Merchants can view real-time data in the Ad Analysis Report. -->
<!---->
<!-- </div> -->
<!---->
<!-- ## FAQ -->
<!---->
<!-- ??? quote "How long after applying for activation before ad delivery can start?" -->
<!-- 	After you apply for activation of the automated ads system in the back office, activation takes about 3 to 5 business days. You will also be notified by email when it is activated. -->
<!---->
<!-- ??? quote "Why haven't I seen any ad data after my ads started running?" -->
<!--     - Google ad review takes about 3 to 5 days. Once approved, ads start running automatically, so please allow time for them to start. (If your ads still do not start running, contact customer support.) -->
<!--     - If you use your own GMC account, log in to the GMC back office to check.  -->
<!---->
<!--         1. In the left menu, go to **Products > Diagnostics** and confirm that valid product items were uploaded successfully. -->
<!--         2. In the left menu, go to **Products > Feeds** and confirm that the product addition method is correct. See [GMC Integration Setup Guide](setup-google-merchant-center.md){ tit](setup-google-merchant-center.md)} -->
<!--         3. In the left menu, go to **成長 > Manage Programs > Shopping Ads** and click **Get Started / Fix Incomplete Items**. Also confirm that all items in the Shopping ad plan are checked *except* **Add Billing Details** and **Create Ad Campaign**. -->
<!---->
<!-- ??? quote "How should I set the daily ad budget?" -->
<!-- 	To help ads perform well, we recommend a daily budget of at least NT$300. If you have marketing campaigns planned, consider raising the budget 2 to 4 times during the campaign period so ads can deliver a stronger combined effect! -->
<!---->
<!-- ??? quote "Why does ad spend exceed the daily budget on some days?" -->
<!-- 	Google optimizes your spend based on factors such as daily traffic changes and month-to-date spend, so a single day can reach up to twice the budget. However, total monthly spend will not exceed daily spend x 30.4. For details, see [Google Help Documentation :lucide-external-link:](https://support.google.com/google-ads/answer/1704443) -->
<!---->
<!-- ??? quote "How long do ad top-up funds last?" -->
<!-- 	There is no expiration date, but check your remaining ad budget to avoid ads being paused. -->
<!---->
<!---->
<!-- ??? quote "Can I use my own Google Ads account?" -->
<!-- 	No. When using the automated ads system, CYBERBIZ creates a dedicated ad account for you. -->
<!---->
<!-- ??? quote "Can I use my own GMC (Google Merchant Center) account?" -->
<!-- 	Yes. If you want to use your own GMC account, share your GMC access with CYBERBIZ's Google Ads account. -->
