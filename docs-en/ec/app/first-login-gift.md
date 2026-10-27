---
title: "Set up the App First-Login Gift"
description: "Set up the coupon or bonus points that members receive automatically the first time they log in to the CYBERBIZ APP, to boost app downloads and member activity."
created: 2026-08-17 11:41
last_modified: 2026-08-17 11:41
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
  - APP 功能
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: 
  - "CYBERBIZ APP"
intents:
  - 設定_APP_首登禮
  - APP_首次登入發放優惠券
  - APP_首次登入發放紅利
features:
  - APP_首登禮
  - coupon
  - "bonus points"
  - APP_引導彈窗
prerequisites:
  - ec/app/setup-cyberbiz-app/
related:
  - ec/marketing/bonus-and-gifts/limited-time-first-purchase-gift/
  - ec/marketing/bonus-and-gifts/setup-registration-gift/
tags:
  - 優惠券
  - 紅利點數
  - CYBERBIZ APP
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - APP_首登禮總開關
  - 活動期間
  - 優惠券設定
  - 紅利設定
  - 彈窗圖片
paths:
  - APP 功能 > APP 首登禮
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/app/first-login-gift/"
comments: false
search:
  exclude: false
icon: lucide/gift
hide: []
---

# Set up the App First-Login Gift

Set up the coupon or bonus points that members receive automatically the first time they log in to the CYBERBIZ APP, to boost app downloads and member activity.
{ .subtitle }

[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions.md#適用擴充) | CYBERBIZ APP
{ .doc-badge }

!!! tip "Use Cases"
    - **Encourage Downloads**: Offer real rewards to get members to download and open your brand app.
    - **Drive First Purchases**: Set a usage threshold for the coupon to guide members to complete a purchase.
    - **Give Members a Reason to Return**: Pair it with bonus points to encourage repeat purchases.


## Before You Start { #prerequisites-app-first-gift }

- **Separate from Other Gifts**: The app first-login gift is issued when **a member account logs in to the app successfully for the first time**. It works separately from the [limited-time first-purchase gift](../marketing/bonus-and-gifts/limited-time-first-purchase-gift.md) and the [registration gift](../marketing/bonus-and-gifts/setup-registration-gift.md).
- **Eligibility**: When all of the following conditions are met, the system issues the first-login gift after the member logs in to the app successfully.

    1. The app first-login gift master switch is turned on.
    2. The member account is logging in to the app for the first time.
    3. At least one of the coupon or bonus sub-switches is turned on.

- **Automatic Issuing**: When the conditions are met, the system issues the gift automatically, so members don't need to claim it manually. A failed login doesn't trigger issuing.
- **One per Member**: Each member account can claim the gift only once, regardless of how many devices it uses.
- **Reward Content**: Turn on at least one of coupon or bonus points. You can issue either one or both.
- **Where to Use**: The issued coupon and bonus points aren't limited to one device and can also be used at checkout on the online store (Web).
- **Recommended Timing**: Before you promote app downloads to customers, finish the first-login gift setup and turn on the master switch. This way, members get the offer on their first login, and nothing is left unissued during the promotion.



## Steps { #operate-app-first-gift }

### Set up and Turn on the App First-Login Gift { #operate-app-first-gift-enable }

1. Log in to CYBERBIZ admin and go to **APP 功能 > APP 首登禮**.
2. Turn on the **App First Login Reward** master switch.
3. **Set the Activity Period**: Choose no end date, or specify a start and end time (future times are allowed).
4. **Set the Reward Content**:

    === "coupon"
        After you turn it on, set the usage threshold, validity period, number of uses, and rules for combining it with other discounts.

    === "Bonus Points"
        After you turn it on, set the number of points to give and their validity period.

    ![](../../assets/images/EC-後台-APP功能-APP首登禮設定-建立首登禮01.en.png){ .screenshot }

5. **Upload a Pop-Up Image**: This image guides members when they open the app. If you don't upload one, the system default image is shown. (Optional)

    ![](../../assets/images/EC-後台-APP功能-APP首登禮設定-建立首登禮02.en.png){ .screenshot }

    !!! tip "About the Pop-Up"
        The guide pop-up supports custom images only. When the feature is on and a member isn't logged in, the app shows this pop-up when it opens, guiding the member to log in and claim the first-login gift.

        ![](../../assets/images/APP-前台-首登禮彈窗01.en.png){ .mini-image }


6. Click **Save**.



### Turn off the App First-Login Gift { #operate-app-first-gift-disable }

1. Go to **APP 功能 > APP 首登禮**.
2. Turn off the **App First Login Reward** master switch.
3. Click **Save**.

!!! info "Settings After Turning It Off"
    When you turn off the master switch, the campaign stops issuing gifts. Your existing settings are kept, so you can turn the switch back on and save to resume.


## How Members Claim the Gift { #operate-app-first-gift-member }

Members get the first-login gift after completing these steps:

1. Download and install your brand's CYBERBIZ APP.
2. **Open the App**: If the merchant has turned on the first-login gift and the member isn't logged in yet, the system shows a guide pop-up.

    ![](../../assets/images/APP-前台-首登禮彈窗01.en.png){ .mini-image }

3. **Log In**: When the system confirms that the account has logged in to the app successfully for the first time, it automatically issues the enabled coupon and/or bonus points.

4. **Check Right Away**: After login, the system opens the **My coupon** / **My bonus points** page, where members can confirm the coupon or bonus points credited to their account.

    === "coupon"

        ![](../../assets/images/APP-前台-會員優惠券01.en.png){ .mini-image }

    === "Bonus Points"

        ![](../../assets/images/APP-前台-會員紅利點數01.en.png){ .mini-image }

    !!! tip "Check Manually"
        Members can also go to **會員中心 > 優惠券** or **會員中心 > 紅利點數** to see the first-login gifts they have claimed.

        ![](../../assets/images/APP-前台-會員中心01.en.png){ .mini-image }

At checkout on the online store or in the app, members can apply the coupon or use bonus redemption under the standard rules.


## Special Cases { #specs-app-first-gift-special }

| Scenario | System Behavior |
| --- | --- |
| The same member uses multiple devices | Can claim only once |
| Logs out and logs in again | Not issued again if already claimed |
| Changes phones but keeps the same account | Not issued again if the account has already logged in to the app |
| Newly registered member | Registration completes the login, so it counts as the first login and the gift is issued |
| Login fails | Not issued |
| An existing member who logged in to the app before the feature launched logs in again after the feature is turned on | Issuing is triggered |




## FAQ { #faq-app-first-gift }

??? quote "How is the app first-login gift different from the first-purchase gift and the registration gift?"
    The app first-login gift is issued when a member logs in to the app successfully for the first time, and it doesn't require a first order. The first-purchase gift is issued based on the conditions of the first paid order. The registration gift is issued when registration on the online store or in admin is complete. All three can run at the same time, so set up each one according to your marketing goals.

??? quote "Can the coupon only be used in the app?"
    No. The coupon and bonus points issued as the first-login gift aren't limited to one channel. When the conditions are met, they can be used at checkout on the online store or in the app.

??? quote "Are my settings deleted when I turn off the first-login gift?"
    No. Turning off the master switch only stops issuing. Your settings are kept, and you can turn the switch back on later.

??? quote "How is the first-login gift determined after members are merged?"
    After a merge, the claim record of the **surviving member** determines whether the account can still claim the first-login gift:

    - **Surviving member has claimed it, merged member hasn't**: Treated as claimed. The gift isn't issued after the merge.
    - **Surviving member hasn't claimed it, merged member has**: Treated as not claimed. After the merge, the gift is still issued if conditions such as the first login are met.

    > The member merge feature must be activated separately and isn't available to all merchants by default. If you need it, contact CYBERBIZ Customer Service to confirm.

??? quote "Can I give only a coupon and no bonus points?"
    Yes. You can turn on the coupon, bonus points, or both, but at least one must be on.


