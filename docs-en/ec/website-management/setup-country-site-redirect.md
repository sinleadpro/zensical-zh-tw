---
title: "Redirect Shoppers to a Country-Specific Online Store"
description: "When you run separate online stores by country, show a storefront banner based on the shopper IP country and guide them to the matching site."
created: 2026-10-23 10:30
last_modified: 2026-10-27 18:10
lang: en-US
type: guide
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
  - JP
  - US
  - MY
  - SG
  - AU
  - SEA
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans: 
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
  - Pro
  - Business
  - global_advanced
plan_options: []
cyb_extensions: []
intents:
  - 多個國家官網之間如何導流
  - 依國家跳轉到另一個官網
  - 設定跳轉至其他國家指定官網
features:
  - 跳轉至其他國家指定官網
  - IP_國家判斷
  - 前台提示列
prerequisites:
  - 同時經營兩個以上獨立網域的官網
  - 需具備「設置」權限
related:
  - ec/website-management/member-security-settings/
  - ec/website-management/setup-multi-language-and-multi-currency/
  - ec/website-management/add-admin-set-permissions/
tags:
  - "Country redirect"
  - "Multi-country stores"
  - "Cross-border ecommerce"
  - "Member security"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 後台 > 管理中心 > 安全性設定 > 會員安全
  - 前台頂端提示列
paths:
  - 管理中心 > 安全性設定 > 會員安全
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/website-management/setup-country-site-redirect/"
comments: false
search:
  exclude: false
icon: lucide/globe-2
hide: []
---

# Redirect Shoppers to a Country-Specific Online Store

[:lucide-layers:{ title="Applicable products" }](../../resources/conventions#適用產品){ title="Icon guide" } | Brand online store
[:lucide-tag:{ title="Applicable plans" }](../../resources/conventions#適用方案){ title="Icon guide" } | All PLUS / Enterprise
<br>
[:lucide-layers:{ title="Applicable products" }](../../../resources/conventions#適用產品) | Cross-border ecommerce (North America / Japan / Southeast Asia)
[:lucide-tag:{ title="Applicable plans" }](../../resources/conventions#適用方案) | Pro / Business
<br>
[:lucide-layers:{ title="Applicable products" }](../../../resources/conventions#適用產品) | Cross-border ecommerce (Singapore local / Malaysia local / Australia local)
{ .doc-badge }


![Storefront top redirect banner](../../assets/images/EC-前台-官網首頁-頂端提示列-顯示跳轉提示01.en.png){ title="Storefront top redirect banner" .hero-page }

## Overview { #intro-country-redirect }

When you **run a separate online store for each country**, the system can show a storefront banner based on the shopper IP country and guide them to the matching store.

When shoppers reach a non-local store from search, ads, or social links, they may see the wrong currency, shipping, or prices. After you set this up, matching shoppers see a banner at the top of the site; only after they click **Go to** do they go to the other store you specified.

!!! tip "Use cases"
    A shopper in Japan opens your Taiwan store from social (`www.twstore.com`) and at checkout finds only NT$ and shipping that cannot reach Japan.

    If you also run a separate Japan store (`www.jpstore.com`), enable this on the Taiwan store: after the system detects the country from IP and shows the banner, the shopper clicks **Go to** to switch to the Japan store.

    :lucide-triangle-alert: This does not switch the same store from Traditional Chinese to Japanese. For language switching inside the same `www.example.com` , use [Multi-language and multi-currency](setup-multi-language-and-multi-currency/).


!!! warning "The system does not auto-redirect shoppers"
    - Shoppers go to the store URL you set only after they click **Go to**.
    - Shoppers can dismiss the banner anytime and keep shopping on the current store.
    - Shoppers who match no country rule see the site unchanged.


## Before You Start { #prerequisites-country-redirect }

- **Who this is for**: Confirm you already run **two or more online stores on separate domains**. If you only need multiple languages on one store, use [Multi-language and multi-currency](setup-multi-language-and-multi-currency.md){ title="Set storefront multi-language and multi-currency" }.
- **Allowed URLs**: You can send shoppers to a CYBERBIZ store or to another website.
- **Permissions**: The account needs the **Settings** permission to edit the **Member Safety** tab. See [Add website admins and set permissions](add-admin-set-permissions.md){ title="Add website admins and set permissions" }.
- **When changes take effect**: New, edited, or deleted rules apply immediately for first-time visitors; returning visitors may take up to **2 hours** to get the latest rules.
- **Detection limits**: With **VPN, corporate, or mobile networks**, the detected country may differ from the shopper physical location.

## Steps { #operate-country-redirect }

### Add a Redirect Rule { #operate-country-redirect-add }

1. Sign in to the CYBERBIZ admin, go to **Website Management > Security Setting**, and open the **Member Safety** tab at the top.
2. Scroll to the bottom and find the **Redirect to a country-specific online store** section.

    ![Country store redirect settings](../../assets/images/EC-後台-管理中心-安全性設定-跳轉國家官網新增區塊01.en.png){ title="Redirect to a country-specific online store settings" }

3. Click **Add** to open the settings dialog.
4. In **Target store URL**, enter the destination store URL.

    ![Select redirect countries](../../assets/images/EC-後台-管理中心-安全性設定-跳轉國家官網勾選國家01.en.png){ .small-image title="Set the redirect store URL and countries" }

5. Select the countries/regions that should go to this URL.

    !!! info "Rules"
        - **One rule = one store URL + multiple countries/regions**. Every selected country goes to the same URL.
        - **Countries cannot repeat**: Each country can belong to only one rule. Already selected countries show a gray, disabled checkbox.
        - **Home-country cannot be selected**: The CYBERBIZ home country for this store cannot be selected, so shoppers are not sent back to the current store.

            **Example**: You are signed in to the CYBERBIZ Taiwan admin: the store country is Taiwan, so Taiwan is grayed out. You can set Malaysia -> Malaysia store, but not Taiwan -> Taiwan store.

6. After the URL and at least one country are filled in, click **Save**.

    ![Save success](../../assets/images/EC-後台-管理中心-安全性設定-跳轉國家官網儲存成功01.en.png){ title="Settings updated successfully" }


!!! tip "Add more rules"
    When different regions should go to different stores (for example Asia -> store A, Europe -> store B), click **Add** again. There is no limit; you cannot add more once every selectable country is assigned.


### Review Existing Rules { #operate-country-redirect-list }

After rules exist, the section becomes a list. Each row is one rule:

| Position | Display |
| --- | --- |
| Left | **Target store URL**: Click to open in a new tab; long URLs are truncated—hover to see the full URL. |
| Right | **Selected countries/regions**: <br>whole region selected -> show the region name (for example Nordics); <br>partial selection -> show Region: [country, country]. <br>Long text is truncated with …; hover to see all. |
| Row end | Red is **Delete**, blue is **Edit**. |

![Redirect rule list](../../assets/images/EC-後台-管理中心-安全性設定-跳轉國家官網設定列表01.en.png){ title="Configured redirect countries and store URLs" }

### Edit a Rule { #operate-country-redirect-edit }

1. Click the blue **Edit** icon on the right of the row.
2. The dialog loads the current URL and countries; you can change the URL or clear/keep selected countries in this rule.
3. Countries taken by other rules, and this store home country, stay gray and cannot be selected.
4. Click **Save** to finish updating.

![Edit redirect rule](../../assets/images/EC-後台-管理中心-安全性設定-跳轉國家官網編輯設定01.en.png){ .small-image title="Edit redirect to a country-specific online store" }

### Delete a Rule { #operate-country-redirect-delete }

1. Click the red **Delete** icon on the right of the row.
2. Confirm to delete. Shoppers in that region no longer see the banner that points to this URL.

![Delete redirect confirm](../../assets/images/EC-後台-管理中心-安全性設定-跳轉國家官網刪除確認01.en.png){ title="Confirm delete redirect rule" }

## What Shoppers See on the Storefront { #overview-country-redirect-storefront }

### Top Banner { #overview-country-redirect-banner }

When the shopper country has another store configured, a banner appears at the very top of the site.

- Banner text uses the **language of the shopper country**, not the language of your current store. For example, a Japan shopper who lands on the Taiwan store sees the banner in Japanese.
- Only after the shopper clicks **Go to** does the target store URL you set open.
- Shoppers can click **X** to dismiss the banner.

![Storefront top redirect banner](../../assets/images/EC-前台-官網首頁-頂端提示列-顯示跳轉提示01.en.png){ title="Storefront top country-redirect banner" }

### After the Banner Is Dismissed { #overview-country-redirect-dismiss }

- After the shopper clicks **X**, the banner stays hidden for the rest of that browsing session, including page changes and refreshes.
- For the same country, it also stays hidden for **30 days** on later visits.
- If the shopper later visits from **another country** that also has a rule, the banner still shows normally.


## Using with the Restricted Regions Blacklist { #specs-country-redirect-blacklist }

You can use this with the [Restricted regions blacklist](member-security-settings.md#operate-security-restricted-locations){ title="Set member security and site protection" } . Two common cases follow.

### The Shopper Country Is Blocked on the Current Store { #specs-country-redirect-blocked-here }

Example: the Taiwan store blocks Malaysia IPs via the region blacklist and also sends Malaysia IPs to the Malaysia store. Malaysia shoppers who open the Taiwan store still see the block page, but the **top banner still shows**; after they click **Go to** they can enter the Malaysia store instead of staying on the block page.


### The Shopper Country Is Blocked on the Destination Store { #specs-country-redirect-blocked-target }

Example: the Australia store sends Malaysia IPs to the Taiwan store, but the Taiwan store blocks Malaysia IPs. Malaysia shoppers still see the banner on the Australia store; clicking **Go to** opens the Taiwan store and then its block page. The system does not detect this conflict—keep each store settings aligned.

![Block page still shows redirect banner](../../assets/images/EC-前台-官網首頁-訪問限制頁-封鎖與跳轉提示01.en.png){ title="Block page with country-redirect banner" }

!!! warning "Keep cross-store settings consistent"
    If store A sends a country to store B and store B sends the same country back to store A, the system does not block it. Shoppers may see banners bouncing between stores—confirm the redirect direction for each country is consistent across stores.

## Next Steps { #next-steps-country-redirect }

<div class="grid cards" markdown>

- :lucide-user-check:{ .lg }
  [__Set member security and site protection__](member-security-settings.md){ title="Set member security and site protection" }
  Adjust the site password, PII masking, and restricted regions blacklist.

- :lucide-languages:{ .lg }
  [__Set storefront multi-language and multi-currency__](setup-multi-language-and-multi-currency.md){ title="Set storefront multi-language and multi-currency" }
  If you need language and currency switching on the **same store**, use that guide instead of this feature.

</div>

## FAQ { #faq-country-redirect }

??? quote "Does the system auto-send shoppers to another store?"
    No. The system only shows the banner; shoppers choose whether to go.

??? quote "Is IP detection always accurate?"
    Not always. With VPN, corporate, or mobile networks, the detected country may differ from the physical location. That is why the banner can always be dismissed and never auto-redirects.

??? quote "Can I send shoppers to a non-CYBERBIZ site?"
    Yes. Any URL works.

??? quote "Why are some countries gray and unavailable?"
    Either (1) another rule already selected them, or (2) they are this store home country. To move a country to another rule, clear it or delete it in the original rule first.
