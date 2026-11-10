---
title: "Set up LINE OA Audience Integration"
description: "Sync filtered member UIDs to LINE OA to create audiences for message push and LAP ad targeting."
created: 2026-03-06 11:46
last_modified: 2026-07-22 15:48
lang: en-US
permalink: "https://help.cyberbiz.io/ec/integrations/line/marketing/setup-line-oa-audience/"
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
difficulty: beginner
intents:
  - 將會員 UID 打包傳送至 LINE 後台建立受眾
  - 進行 LINE 精準訊息推播
  - 進行 LINE LAP 廣告投放
features:
  - LINE OA 受眾串接
  - 會員篩選器
  - 會員分群
  - LINE Messaging API
prerequisites:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
related:
  - ec/integrations/line/account-integration/connect-line-messaging-api/
tags:
  - "LINE OA"
  - "audience integration"
  - "member segmentation"
  - LAP
  - "ad targeting"
  - "Messaging API"
  - "targeted marketing"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > 所有會員
  - 會員 > 會員分群
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=5631
  - https://www.cyberbiz.io/support/?p=28387
search:
  exclude: false
icon: lucide/split
hide:
comments: false
---

![LINE Audience Integration](../../../../assets/images/ec-會員-所有會員-line受眾.en.png){ .hero-page title="LINE Audience Integration" }

## LINE Audience Integration Guide { #operate-line-audience }

**LINE OA Audience Integration** lets merchants use the admin member filter to package the UIDs of members who used "LINE quick login" or "linked LINE OA" and send them to the LINE backend to create an audience. This is useful for later **targeted message push** or **LAP ad targeting**.

Below are the detailed steps and instructions:

## Prerequisites and Restrictions { #prerequisites-line-audience }

- [x] **Required setup**: Merchants must first complete the [**LINE Messaging API** setup](../account-integration/connect-line-messaging-api.md){ title="Connect LINE Messaging API" }  before they can use this feature.
- [x] **Admin permissions**: Audiences created by CYBERBIZ **cannot be updated or deleted directly in the LINE backend**. You must sync them through the CYBERBIZ admin dashboard.

## Steps to Create an Audience in LINE Backend { #operate-line-audience-create-line-backend-step }

1. **Access path**: Go to the admin dashboard **Customer Management > All Customers**.
2. **Set filter conditions**: Click the search bar to open the "Filter" panel. You **must** add at least one of the following conditions. Otherwise, the audience cannot be sent to LINE:
    - LINE login completed
    - LINE linking completed
    - LINE login or LINE linking completed

	![Member filter - LINE audience condition](../../../../assets/images/ec-會員-所有會員-會員篩選器-line受眾條件.en.png){ title="Member filter - LINE audience condition" }

3. **Apply and save**: After you finish the settings, click **Apply**. After you confirm the list is correct, click **Save** in the section on the right.
4. **Enter information**: Enter the audience's "Name" and "Description", **check the boxes below**, and then click "Confirm".

	![LINE audience segment creation](../../../../assets/images/ec-會員-所有會員-會員篩選器-line受眾分群建立.en.png){ title="LINE audience segment creation" }

5. **View segments**: Click the **Customer Grouping** menu to view the LINE audience segments you created. Click **Add to LINE Backend** to add the audience to the LINE backend.

	![Add to LINE Backend](../../../../assets/images/ec-會員-line受眾-新增至line後台.en.png){ title="Add to LINE Backend" }

6. **Check the result**: In the LINE OA admin dashboard (Page > Data Management > Audiences), check that successfully linked Audience names are displayed as **(filter condition name)_CYBERBIZ upload**.

	![Audience view in LINE backend](../../../../assets/images/ec-會員-會員群組-line受眾-line後台.en.png){ title="Audience view in LINE backend" }

## Audience Management <small>Update and Delete</small> { #operate-line-audience-manage }

- **Update the audience**: If the member list changes, go to the "All Members" page and click "**Update Audience to LINE**". The system syncs the latest filter results to LINE.
- **Delete the audience**: In the filter condition list, click the "**Delete**" button next to the audience you want to remove.
    - _Note: After you click delete, the filter condition in CYBERBIZ and the audience in the LINE OA backend will be **deleted together**._

!!! warning "Audiences created by CYBERBIZ **cannot be updated or deleted directly in the LINE backend**. You must sync them through the CYBERBIZ admin dashboard."

![Update audience in LINE backend](../../../../assets/images/ec-會員-line受眾-更新至line後台.en.png){ title="Update audience in LINE backend" }

## How to Use LINE Audiences { #intro-line-audience }

### LINE OA Message Push { #intro-line-audience-line-oa-message }

- In the LINE OA backend, when you create a broadcast, select "**Filter target**" as the recipients, then click the edit button :lucide-pencil: to add an audience.

	![Add audience in LINE backend](../../../../assets/images/ec-會員-會員分群-line受眾-line後台新增受眾.en.png){ title="Add audience in LINE backend" }

- Add an audience, select the name that CYBERBIZ sends, and set it to "Include" or "Exclude" for that audience.

### Ad Manager (LAP) Ad Targeting { #intro-line-audience-ad-manager-lap }

- In [Ad Manager :lucide-external-link:](https://admanager.line.biz/home/), click "Audiences" > "Create Audience", and select "**Audience shared from LINE Official Account user identifiers (UID)**".

	![Create audience in Ad Manager](../../../../assets/images/ec-會員-會員分群-line受眾-ad-manager-建立受眾.en.png){ title="Create audience in Ad Manager" }

- Afterward, when you create an ad group, you can select this audience to run targeted ads.

	![Create audience in ad group](../../../../assets/images/line-ad-manager-廣告群組-建立受眾.en.png){ title="Create audience in ad group" }

!!! info "Learn more about [What is LINE Performance-Based Ad Targeting (LAP)? :lucide-external-link:](https://tw.linebiz.com/service/display-solutions/line-ads-platform/)."

## FAQ { #faq-line-audience }

??? quote "Why can't I see the synced audience in the LINE backend?"
	Check the following:

	- **Integration status**: Check `Third-Party Integration` > `LINE OA` **Messaging API** related fields: confirm they are set correctly.
	- **Permission check**: Make sure your LINE OA admin permissions are sufficient, and that you clicked the "Add to LINE Backend" button in the CYBERBIZ backend.
	- **Processing time**: After LINE receives the data, processing usually takes **15 - 60 minutes**. If the status shows "Preparing", check again later.

??? quote "Why is the number of synced audience members lower than the number filtered in CYBERBIZ?"
	This is due to the **UID matching restriction**: **An audience can only include members who have "authorized LINE login" or "linked the LINE Official Account."** If a member has only a phone number and has never authorized LINE, their data cannot be packaged as a UID and sent to LINE. The LINE system filters out invalid or blocked UIDs.

??? quote "Does the audience list update automatically?"
	**It does not sync automatically.** Audience sync in CYBERBIZ is a **manual update** mechanism. If your member list changes (for example, new members match the filter criteria), go to `Members` > `All Customers` > `Customer Segment menu`, select the relevant segment, and click **Update Audience to LINE**. The system sends the latest data to LINE only after you click it.

??? quote "What happens if I manually delete the audience in the LINE backend?"
	**We do not recommend this.** Because CYBERBIZ API created this audience, deleting it directly in the LINE backend may put the two systems out of sync (a broken link). Make sure to delete it from the **CYBERBIZ admin dashboard**. The system then automatically sends a command to delete the LINE audience as well.

??? quote "Why do I get the "Insufficient audience size" error when I sync an audience?"
	According to LINE's official limit, an audience must include at least **50 valid UIDs**. If your filter results contain fewer than 50 people, the LINE backend may fail to create the audience, or it may not be usable for message push.
