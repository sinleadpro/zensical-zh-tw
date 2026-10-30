---
title: "Enable reCAPTCHA for Comments"
description: "Apply for and connect Google reCAPTCHA keys to block bot attacks and spam comments."
created: 2026-03-05 17:15
last_modified: 2026-07-01 10:40
lang: en-US
type: guide
author: Jase
reviewers: []
notes:
  - update pending
  - verify FAQ
  - update internal links
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
  - 會員
sites:
  - TW
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: intermediate
intents:
  - 防止機器人垃圾留言
  - 設定 Google reCAPTCHA
  - 提升網站安全性
features:
  - reCAPTCHA
  - 商品評論
  - 顧客回饋與建議
prerequisites: []
related:
  - ec/products/engagement/manage-product-reviews/
tags:
  - "Information Security"
  - Google
  - reCAPTCHA
  - "Spam Comments"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - reCAPTCHA 管理控制台
  - 聯絡我們表單
paths:
  - 會員 > 顧客回饋&建議
  - 網站外觀 > 管理商品評論
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=12371
  - https://www.cyberbiz.io/support/?p=50193
permalink: "https://help.cyberbiz.io/ec/website-appearance/customer-interaction/enable-comment-recaptcha/"
comments: false
search:
  exclude: false
icon: lucide/shield-check
hide: []
---

![reCAPTCHA settings](../../../assets/images/ec-google-recaptcha.zh-tw.en.png){ title="reCAPTCHA Settings" .hero-page }

## What Is reCAPTCHA { #intro-recaptcha }

reCAPTCHA is a security verification service from Google that tells real people apart from automated programs. It protects website forms, comment sections, and checkout from bot attacks.

Turning on reCAPTCHA helps you:

- **Prevent spam comments**: Reduce the risk of automated abuse in product review sections and contact forms.  
- **Improve website security**: Detect non-human activity and reduce fraud and malicious behavior.  
- **Keep interactions high quality**: Make sure submitted content is genuine and improve the overall experience.

For more information, see the [official reCAPTCHA documentation :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=zh_tw).

## Before You Start { #prerequisites-recaptcha }

### Where It Applies { #prerequisites-recaptcha-scope }

- [x] Product page review section.
- [x] Contact Us page.

---

### Cost { #specs-recaptcha-fees }
- Google reCAPTCHA offers a free usage quota. If you exceed the free quota[^free-quota-notice], customers cannot post comments.
- For more information, see [Quotas and Limits :material-open-in-new:](https://docs.cloud.google.com/recaptcha/quotas?hl=zh-tw)

[^free-quota-notice]: Google notifies you by email before you reach the free usage limit.

## Steps { #operate-recaptcha }

### Apply for reCAPTCHA Keys { #operate-recaptcha-apply }

1. Go to the [Google reCAPTCHA Admin Console :material-open-in-new:](https://www.google.com/recaptcha/admin/) and sign in to your Google account.
2. Fill in the registration information:
	- **Label**: Name this reCAPTCHA as you like (for example, `YourStoreName_reCAPTCHA`).  
	- **reCAPTCHA type**: Select "Challenge (v2)," and then select "Invisible reCAPTCHA badge"[^invisible-recaptcha].  
	- **Domains**: Enter your website address.
  
        !!! warning "Note"
            Do not include the prefix `https://` or the suffix `/...`. For example, if your website address is `https://_demo1234.cyberbiz.co_ /zh-TW`, enter only `_demo1234.cyberbiz.co_`.

	- **Google Cloud Platform**: Select a project as needed.  

3. Click **Submit** to get the Google reCAPTCHA **site key (sitekey)** and **secret key (secretkey)**.

4. Copy and safely store the **site key** and **secret key**. You need them in the binding steps that follow.

![Applying for reCAPTCHA keys](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA03.png){ title="Applying for reCAPTCHA Keys" .screenshot }


### Bind reCAPTCHA Keys to the Product Review Section { #operate-recaptcha-reviews }
[:lucide-tag:{ title="Available Plans" }](../../../resources/conventions#適用方案){ title="Icon Conventions" } | PLUS / Enterprise

!!! info "Product reviews are available only to *Enterprise* and *PLUS* users. To turn them on, contact customer service. For related settings, see [How to Manage Product Reviews](../../products/engagement/manage-product-reviews.md){ title="Manage Product Reviews" }."

1. Sign in to the CYBERBIZ e-commerce admin and go to **Website Appearance > Product Reviews Management**.
2. Click the **Google reCAPTCHA** toggle to turn it on (ON).
3. Paste the keys:
	- **reCAPTCHA sitekey**: Enter the **site key** you got during the application.  
	- **reCAPTCHA secretkey**: Enter the **secret key** you got during the application.  
4. Click **Update** to apply the changes.

![Binding reCAPTCHA to product reviews](../../../assets/images/ec-product-review-google-recaptcha.zh-tw.en.png){ title="Binding reCAPTCHA to Product Reviews" }

### Bind reCAPTCHA Keys to the Contact Us Page { #operate-recaptcha-contact }

1. Sign in to the CYBERBIZ admin and go to **Customer Management > Member Feedbacks**.
2. Click the **Enable Bot Blocking** toggle to turn it on (ON).
3. Paste the keys:
	- **sitekey**: Enter the **site key** you got during the application.  
	- **secret key**: Enter the **secret key** you got during the application.
4. Click **Save All Settings** to apply the changes.

![Binding reCAPTCHA to Contact Us](../../../assets/images/ec-member-feedback-google-recaptcha.zh-tw.en.png){ title="Binding reCAPTCHA to Contact Us" }

## FAQ { #faq-recaptcha }
??? quote "Can one Google reCAPTCHA account be bound to multiple domains?"
    Yes. One Google reCAPTCHA account can be bound to multiple domains. You can use the same keys for both product reviews and the Contact Us page.

??? quote "Does Google reCAPTCHA have a free usage quota?"
    Yes. Google reCAPTCHA offers a free usage quota, and Google notifies you by email before you reach the limit. If you exceed the free quota, customers cannot post comments, and you need to upgrade your plan with Google yourself. Learn about the [costs](#specs-recaptcha-fees){ data-preview }.

??? quote "What happens if I enter the wrong keys?"
    Make sure the keys are correct, or the comment feature will not work. If you see an error message (as shown below), check that the keys are entered correctly.

    [![Incorrect reCAPTCHA key](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)

??? quote "Does this reCAPTCHA feature work on websites with any theme?"
    This feature is available only on websites that use a drag-and-drop theme.

## Next Steps { #next-steps-recaptcha }

<div class="grid cards" markdown>

- :lucide-message-square-text:{ .lg }  
  [__Set Up Product Reviews__](../../products/engagement/manage-product-reviews.md#operate-product-reviews){ title="Manage Product Reviews" }
  Turn on product reviews, set up moderation, and award points.

</div>

[^invisible-recaptcha]: Invisible reCAPTCHA automatically checks whether a customer is a bot as they interact. It usually does not interrupt customers and shows a challenge only when the system finds something suspicious. This reduces friction for customers while strengthening your website's protection.
