---
title: "Set up FB and IG Stores"
description: "Set up Facebook and Instagram stores to create social sales channels and sync products."
created: 2026-04-13 16:31
last_modified: 2026-07-20 17:30
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
  - 設定_FB_商店
  - 設定_IG_商店
  - Facebook_Instagram_商店同步
features:
  - Facebook 商店
  - Instagram 商店
  - 商品同步
prerequisites:
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/mbe/setup-fbe-domain-verification/
related:
  - ec/integrations/fb/mbe/setup-fbe-authorization/
  - ec/integrations/fb/mbe/setup-fbe-domain-verification/
  - ec/products/categories-and-tags/manage-product-tags/
  - ec/integrations/fb/mbe/exclude-products-fb-instagram-sync/
  - ec/products/create-and-manage/product-swatches-variant-images-drag-drop/
tags:
  - FB_Store
  - IG_Store
  - Product_Sync
  - Business_Extensions
  - FBE
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 第三方整合 > 臉書_Facebook_設定
layouts:
  - draggable
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3113
  - https://www.cyberbiz.io/support/?p=11757
  - https://www.cyberbiz.io/support/?p=24676
permalink: "https://help.cyberbiz.io/ec/integrations/fb/mbe/setup-fb-instagram-shop/"
comments: false
search:
  exclude: false
icon: lucide/store
hide: []
---

## FB and IG Store Setup Guide { #operate-fb-instagram }

**FB and IG Store Setup** helps brands build social stores, reach more traffic through Facebook and Instagram, and direct potential customers to the official website to make purchases.

!!! warning "Setup Guide and Support Scope"
    Facebook system interfaces and policies are updated from time to time. This guide is for reference only. For actual operations, follow the latest official Facebook guidelines. For advanced third-party platform settings or technical troubleshooting, contact Facebook Official Support. CYBERBIZ cannot provide technical support.

    For more information, see the Meta official tutorial: [Set up a store on Facebook and Instagram :lucide-external-link:](https://zh-tw.facebook.com/business/help/268860861184453).

## Prerequisites and Limitations { #prerequisites-fb-instagram }

Before you connect your Facebook and Instagram stores, complete the following setup steps in order:

- [x] **[Account Authorization and Asset Linking](setup-fbe-authorization.md){ title="Set up FBE account authorization and asset linking" }** - Link pixels, Facebook Pages, catalogs, and ad accounts to the CYBERBIZ admin
- [x] **[Domain Verification](setup-fbe-domain-verification.md){ title="Set up FBE domain verification" }** - Complete domain verification to set up 8 aggregated events and ensure accurate ad conversion data

After you complete both settings above, the system automatically fills in related information (such as linked catalogs) when you connect your store. Follow the on-screen prompts to finish setting up the store.

## Steps { #operate-fb-instagram-steps }

### Connect a Facebook Store { #operate-fb-instagram-steps-connect-facebook }

First, sign in to your Facebook account and make sure you have the relevant admin permissions in Business Manager.

1.  **Open Business Suite**: Go to [Business Manager Settings](https://business.facebook.com/), click **Settings ** > ** Data Sources ** > ** Catalogs**, select the matching catalog, and then click **Open in Business Suite**.

    ![Open Business Suite](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-進入商務管理工具.en.png)

2.  **Start the Store Setup**: In the left menu of Business Suite, click **Shops**, and then click Go to store page.

    ![Go to Shops](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-前往商店.en.png)

3.  **Create a Business Account**: If you have not created a business account yet, click **Add Account** to continue to the next steps.

    ![Create a business account](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-建立商務帳號.en.png)

4. **Create a Store**: Follow the on-screen prompts to complete the store creation steps.

    - **Select a Market**: Select the **Country/Region** where your store mainly sells (for example, Taiwan), and then click Start Now.
    - **Select a Sales Channel**: The system automatically fills in your linked Facebook Page. Select the **Sales Channel** to use (Facebook Page).
    - **Select a Catalog**: Select the **Product Catalog** for your store (the system automatically fills in the catalog created in the earlier steps, such as the CYBERBIZ-FBE catalog).
    - **Confirm and Finish**: Review your store settings. After you confirm they are correct, select the checkbox to agree to the Seller Agreement, and then click **Finish Setup**.

    ![Connect a store](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-建立串接商店.en.gif)

8. **View the Store**: Click **Shops** to see the connected store. Click **Edit Store** to make changes to it.

    ![View a store](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-檢視商店.en.png)

---

### Connect an IG Store { #operate-fb-instagram-steps-connect-ig }

Instagram stores require a business account and must first be linked to a Facebook Page and catalog.

1.  **Add an IG Account**: Go to [Business Manager Settings](https://business.facebook.com/), click **Settings ** > ** Accounts ** > ** Instagram ** > ** Add**, and sign in to your IG account.

    ![Business Manager - Add IG account](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-新增ig帳號.en.png)

2.  **Confirm the Account Type**: Make sure your IG account is switched to the **Business** type.

    ![Business Manager - Claim IG account](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-認領ig帳號.en.png)

3. **Create a Professional IG Account**: For the account type, select **Business**, choose a category that fits your needs, and click **Confirm** to create the professional account.

    ![Create a professional IG account](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-建立專意ig帳號.en.gif)

4.  **Link Assets**: Go to Business Suite, then go to **Settings > General > Sales Channel**. In the section for connecting other Facebook Pages or Instagram accounts to your store, click **Link** and select your IG account.

    ![Link IG assets](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-連結資產.en.png)

5.  **[Enter Domain Verification](setup-fbe-domain-verification.md){ title="Set up FBE domain verification" }**: The system usually fills in your verified domain automatically. If it does not, enter your website domain (for example, `yourstore.com`) to complete the verification link.
6.  **View the Sales Channel**: After setup, you can see the linked IG account under Sales Channels.

    ![View the linked IG store](../../../../assets/images/ec-第三方整合-fbe-串接fb-ig商店-完成驗證.en.png)

!!! note "For further IG store setup and use, see the Meta official tutorial: [Instagram Shopping :lucide-external-link:](https://zh-tw.facebook.com/business/help/582645198813984)."

## Product Sync and Display Management { #operate-fb-instagram-product-sync-manage }

!!! info "Automatic Update Time"
    Product information on your official website automatically syncs to the Facebook store every day at **2:00 AM or 2:30 AM**.

After the connection is complete, the system automatically syncs products through the Product Feed.

<div class="grid cards" markdown>

- :lucide-package-x:{ .lg }   
  [__Exclude Store Products__](../../../products/categories-and-tags/manage-product-tags.md#operate-product-tags-exclude){ title="Manage product tags" }       
  If you do not want certain products, such as free gifts or test products, to sync to your Facebook and Instagram stores, filter them by setting product tags.

- :lucide-eye-off:{ .lg }   
  [__Hide Stores or Products__](exclude-products-fb-instagram-sync.md#operate-exclude-products-manage){ title="Exclude products from syncing to Facebook and Instagram stores" }
  You can hide an entire store or a single product in Business Suite.

</div>

## Next Steps { #next-steps-fb-instagram }

<div class="grid cards" markdown>

- :lucide-swatch-book:{ .lg }   
  [__Product Swatch Settings__](../../../products/create-and-manage/product-swatches-variant-images-drag-drop.md){ title="Set up product swatches and style images - drag-and-drop layout" }       
  Turn on the swatch feature and place images in color order so that product images in the Facebook store change correctly with each style.

</div>

## FAQ { #faq-fb-instagram }

??? quote "Why does the IG store link show a 404 or encoding error?"

    If your website works normally but you see a 404 error or a failed redirect when you navigate from the IG store, the cause is usually related to URL encoding (character encoding).

    - **Cause**: When a link contains certain parameters (such as ? or = in an affiliate link), the built-in Instagram browser sometimes incorrectly encodes them as hexadecimal codes (such as %3F or %3D), which makes the target URL invalid.
    - **Solution**:

        - Use a short link: Convert the original long link into a short URL (such as bit.ly or reurl) to avoid special characters in the URL and prevent garbled text during transmission.
        - Report to the platform: This issue is a compilation logic limitation on the social platform side. We recommend that merchants also send feedback to Instagram.

??? quote "When do products sync to the FB and IG stores?"

    Product information on your official website syncs automatically to the Facebook store every day at **2:00 AM or 2:30 AM**. Content updated during the day appears only after the sync is complete.

??? quote "How do I exclude specific products from syncing to the store?"

    If you do not want free gifts or test products to upload to the store, enter **贈品** or **排除product feed** in the product tags field in your website admin (do not add a space between 排除 and "product"). The system automatically filters out that product. For detailed steps, see [Tags to Exclude Products from Third-Party Platforms](../../../products/categories-and-tags/manage-product-tags.md#operate-product-tags-exclude){ title="Manage product tags" }.
