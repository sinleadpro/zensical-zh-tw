---
title: "Embed a Google Form in a Custom Page"
description: "Embed a Google Form in a CYBERBIZ custom page and optimize its responsive width and height for mobile."
created: 2024-05-23 00:00
last_modified: 2026-06-30 11:01
lang: en-US
permalink: "https://help.cyberbiz.io/ec/website-appearance/pages-and-content/embed-google-form-custom-page/"
type: guide
author: Jase
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 網站外觀
sites:
  - TW
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 嵌入 Google 表單至自訂頁面
  - 優化表單行動版顯示比例
  - 調整嵌入表單的顯示高度
  - 解決 Google 表單權限存取問題
features:
  - 自訂頁面
  - 自訂 HTML 區塊
  - Google 表單嵌入
prerequisites:
  - 已製作完成的 Google 表單
related: []
tags:
  - "Google Forms"
  - "Embed Code"
  - "Responsive Design"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 網站外觀 > 自訂頁面管理
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=3688
  - https://www.cyberbiz.io/support/?p=18247
comments: false
search:
  exclude: false
icon: lucide/form-input
hide: 
---

![Embed a Google Form](../../../assets/images/ec-網站外觀-自訂頁面-嵌入google表單.en.png){ title="Embed a Google Form" .hero-page }

## About Embedding a Google Form { #intro-google-form }

Embed a Google Form in a CYBERBIZ page to easily handle **reservations, inquiries, surveys, or warranty registration**, so customers can respond right on your website.

## Before You Start <small>Get the Form Code</small> { #prerequisites-google-form }

1. Create your form in Google Forms.
2. Click the "More" menu :lucide-ellipsis-vertical: at the top right.
3. Switch to the "Embed" tab (the `< >` icon).
4. Copy the **HTML embed code** that Google generates.

![Google Form embed code](../../../assets/images/google-forum-embed-html.en.png){ title="Google Form Embed Code" }

!!! note "For detailed steps, see the [official help article :lucide-external-link:](https://support.google.com/docs/answer/2839588#zippy=%2C%E5%8F%96%E5%BE%97%E8%A1%A8%E5%96%AE%E9%80%A3%E7%B5%90%2C%E5%9C%A8%E7%B6%B2%E7%AB%99%E6%88%96%E7%B6%B2%E8%AA%8C%E4%B8%AD%E5%B5%8C%E5%85%A5%E8%A1%A8%E5%96%AE)."

## Steps { #operate-google-form }

!!! warning "Code Editing Notice"
    CYBERBIZ gives you access to edit the code but does not provide coding tutorials or code-writing services. Have your own technical staff make these changes.

1. **Open the editing page:** Sign in to the CYBERBIZ admin, go to **Website Appearance > Customized Pages Management**, and select the page where you want to add the form.
2. **Add a block:** Click **Add Block**, select **Custom HTML**, and click it to open the editing page.
3. **Paste the code:** Click **Edit** to open the editor, and paste the Google Form code you copied into the blank area.
4. **Make it responsive (important):** In the pasted code, find the `width` attribute and change its value (such as 640) to **`100%`**. This makes the form fit the screen width and display in full on both mobile and desktop.
5. **Save and preview:** Click Save when you finish. The Google Form now appears on your website page, ready to fill in.

![Embedding a Google Form](../../../assets/images/ec-網站外觀-自訂頁面-嵌入google表單.en.gif){ title="Embedding a Google Form" }


## FAQ { #faq-google-form }

??? quote "Why is the right side of the form cut off on mobile?"
	This usually happens because `width` is set to a fixed pixel value (such as `width="640"`).
	
	**Solution:** Check the embed code and change the value of `width` to `100%`. The form then scales automatically to the screen width of the shopper's device.

??? quote "The embedded form is too short and shows an inner scroll bar. What should I do?"
	The default embed height of a Google Form may not be tall enough to show every question.
	
	**Solution:** In the HTML code, find the `height` attribute and increase its value manually (for example, to `height="1200"` or higher) until the whole form shows without an inner scroll bar.

??? quote "Why do customers see "You need permission" and can't fill in the form?"
	This happens because the Google Form's privacy settings restrict who can access it.
	
	**Solution:**
	
	1. Go back to the Google Form editing page.
	2. Click the "Settings" tab.
	3. Under the "Responses" section, turn off the **"Restrict to users in (your organization name)"** option.
	4. Make sure "Limit to 1 response" is also turned off (unless you require customers to sign in to a Google account).

??? quote "Can the form send shoppers back to a specific page on my website after they submit it?"
	A natively embedded Google Form does not support "automatic redirects" to an external URL after submission.
	
	
	**Alternative:** In the Google Form, go to "Settings" > "Presentation" > "Confirmation message" and paste a link to your website so respondents can click to go back.
