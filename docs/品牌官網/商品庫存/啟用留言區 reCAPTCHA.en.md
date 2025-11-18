---
title: Enable reCAPTCHA for Comment Section
description: Enable Google reCAPTCHA to prevent bots and spam comments
product:
  - EC
module:
  - Website Settings
activ: configure
surfaces:
  - Website Appearance > Manage Product Reviews
  - Members > Customer Feedback & Suggestions
devices: []
apis: []
type: tutorial
features: []
tasks:
  - Prevent spam comments
  - Prevent bot messages
tnb: ""
plans:
  - 專業 PLUS
  - 進階 PLUS
  - 高手 PLUS
  - 企業
lang: en
sites:
  - Taiwan
status: review
doc_next: ""
doc_previous: ""
tags:
  - Security
  - Google
difficulty: ""
sibs: []
notes:
  - verify FAQ
  - update internal links
---

# Enable reCAPTCHA for Comment Section
Enable Google reCAPTCHA to prevent bot messages and spam comments.
{ .page-subtitle }

[:material-tag-text:](){ .badge-icon title="Applicable Plans" }[PLUS | Enterprise](){ .badge-text } 
[:material-toggle-switch:](){ .badge-icon title="Applicable Features" }[Drag-and-Drop Theme](){ .badge-text } 
[:material-arrow-left-circle:](){ .badge-icon title="Related Operations" }[[Using the Product Review Feature]]{ .badge-text }

---

## Overview
??? example "AI Summary"
    ![[Setting up reCAPTCHA for comment section audio.mp4]]{ .audio-small }
### Why Use reCAPTCHA
Pages that allow customer comments are vulnerable to bot attacks and spam. Enabling Google reCAPTCHA verification can effectively identify non-human operations, protecting your website from spam, abuse, and fraud, thereby maintaining the quality of the comment section. For more information on reCAPTCHA features, please refer to the [official website :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=en).

!!! quote "Why use reCAPTCHA?"
	Pages that allow customer comments can be subject to bot attacks and spam. Enabling Google reCAPTCHA verification can effectively identify non-human operations, protecting the website from spam, abuse, and fraud, and maintaining the quality of the comment section. To learn more about reCAPTCHA features, please refer to the [official website :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=en).
=== ":material-information-outline: Notes"
    - [x] Google reCAPTCHA provides a free usage quota. If you exceed the free quota[^Exceeding the free reCAPTCHA quota], customers will not be able to leave comments. For details, please see [Quotas and limits :material-open-in-new:](https://cloud.google.com/recaptcha/quotas?hl=en).
    - [x] Supports the review section on "Product Pages" and the `Contact Us` page. 

	<div class="grid cards" markdown>
	
	- ![Establish reCAPTCHA security verification for the product review section](https://www.cyberbiz.io/support/wp-content/uploads/商品評論00.png){ title="Product Page Review Section" }
	- ![Establish reCAPTCHA security verification on the Contact Us page](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA01.png){ title="Contact Us Page" }
	- 
	</div>

=== ":material-lightbulb-outline: Scenarios"
    - Prevent spam comments: Protect your website's product review section and Contact Us page from spam messages automatically sent by bots.
    - Enhance website security: Effectively identify non-human operations through the reCAPTCHA verification mechanism, increasing the website's protection level.
    - Maintain customer interaction quality: Ensure that the content in the comment sections is genuine and valid, improving the customer interaction experience.



---

## Steps
### Step 1: Apply for Google reCAPTCHA Keys
=== ":material-numeric-1-circle: Access the Console"
    - [ ] Go to the [Google reCAPTCHA Admin Console :material-open-in-new:](https://www.google.com/recaptcha/admin/) and log in to your Google account.
=== ":material-numeric-2-circle: Register a New Site"
    - [ ] Fill in the registration information sequentially.
    - Label: Name this reCAPTCHA according to your needs (e.g., `Your_Store_Name_reCAPTCHA`).
	 - reCAPTCHA type: Choose "Challenge (v2)" and check "Invisible reCAPTCHA badge[^Invisible reCAPTCHA]".
    - Domains: Enter your official website URL.
    ??? warning "Domain Entry Notes"
        Do not include the prefix `https://` or any suffix `/...`. For example, if your website URL is `https://_demo1234.cyberbiz.co_ /en-us`, please enter only `_demo1234.cyberbiz.co_`.
    - Google Cloud Platform: Choose a project according to your needs.
    - [ ] Click the "Submit" button, and you will obtain the Google reCAPTCHA "Site Key" and "Secret Key".
    ![[Google reCAPTCHA Settings Fields.png]]
=== ":material-numeric-3-circle: Copy the Keys"

    Copy and securely save the "Site Key" and "Secret Key". They will be used later to [[enable-comment-recaptcha#step-2-bind-recaptcha-keys-to-the-product-review-section|bind to your website pages]].

    ![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA03.png){ .screenshot }


### Step 2: Bind reCAPTCHA Keys to the Product Review Section :material-lock-outline:
??? note "The product review feature is only available for `Enterprise` and `PLUS` plan merchants. If you need to use this feature, please contact customer service to have it enabled. Learn how to [[Using the Product Review Feature]]."

![](https://www.cyberbiz.io/support/wp-content/uploads/EC-後台網站外觀-管理商品評論-設定Google-reCAPTCHA04.png){ .screenshot }

=== ":material-numeric-1-circle: Go to the Operation Page"
    - [ ] Log in to the CYBERBIZ e-commerce backend, go to "Website Appearance" → "Manage Product Reviews".
=== ":material-numeric-2-circle: Enable the Feature"
    - [ ] Click the Google reCAPTCHA switch :material-toggle-switch: to turn it on (ON).
=== ":material-numeric-3-circle: Paste the Keys"
    - [ ] reCAPTCHA sitekey: Enter the "Site Key" you obtained in Step 1 into this field.
    - [ ] reCAPTCHA secretkey: Enter the "Secret Key" you obtained in Step 1 into this field.
=== ":material-numeric-4-circle: Save Changes"
    - [ ] Click "Update" to apply the changes.
### Step 3: Bind reCAPTCHA Keys to the Contact Us Page
![[EC-會員-顧客回饋-reCAPTCHA 啟用.png]]
=== ":material-numeric-1-circle: Go to the Operation Page"
    - [ ] Log in to the CYBERBIZ e-commerce backend, go to "Members" → "Customer Feedback & Suggestions".
=== ":material-numeric-2-circle: Enable the Feature"
    - [ ] Click the "Enable bot protection" switch :material-toggle-switch: to turn it on (ON).
=== ":material-numeric-3-circle: Paste the Keys"
    - [ ] `sitekey`: Enter the "Site Key" you obtained in Step 1 into this field.
    - [ ] `secret key`: Enter the "Secret Key" you obtained in Step 1 into this field.
=== ":material-numeric-4-circle: Save Changes"
    - [ ] Click "Save all settings" to apply the changes.

---

## FAQ
??? question "Can one Google reCAPTCHA account be bound to multiple domains?"
    Yes, one Google reCAPTCHA account can be linked to multiple domains. You can use the same set of keys for both the product review and Contact Us pages.
??? question "Does Google reCAPTCHA have a free usage quota?"
    Google reCAPTCHA offers a free usage quota. Google will notify merchants via email before the free usage limit is reached. If the free quota is exceeded, customers will not be able to leave comments. You will need to upgrade your plan with Google. For details, refer to [reCAPTCHA - Quotas and limits](https://cloud.google.com/recaptcha/quotas?hl=en).

??? question "What happens if the keys are entered incorrectly?"
    Please ensure the keys are entered correctly; otherwise, the comment feature will not function properly. If you see an error message (as shown below), please check if the keys are correct.

    [![reCAPTCHA key entry error](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)](https://www.cyberbiz.io/support/wp-content/uploads/EC-前台-聯絡我們-設定reCAPTCHA02.png)
??? question "Is this reCAPTCHA feature applicable to all website themes?"
    This feature is only available for drag-and-drop themes.

---

## Further Reading
=== ":material-page-next-outline: Outgoing Links"
    - [[Setting Up the Product Review Feature]]
    - [Google reCAPTCHA Admin Console :material-open-in-new:](https://www.google.com/recaptcha/admin/)
    - [Google reCAPTCHA Features :material-open-in-new:](https://cloud.google.com/security/products/recaptcha?hl=en)
    - [Google reCAPTCHA Quotas and limits :material-open-in-new:](https://cloud.google.com/recaptcha/quotas?hl=en)
=== ":material-page-previous-outline: Backlinks"
=== ":material-update: Updates"
=== ":material-book-outline: Glossary"
=== ":material-map-outline: Diagrams"


[^Exceeding the free reCAPTCHA quota]: Google will notify merchants via email before the free usage limit is reached.
[^Invisible reCAPTCHA]: Invisible reCAPTCHA automatically determines if a user is a bot during interaction, typically without interrupting the customer's actions. A verification challenge only appears when the system deems the activity suspicious. This reduces customer friction while enhancing website protection.