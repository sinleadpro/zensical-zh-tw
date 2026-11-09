---
title: "Filter and Use LINE OA Bound Member Lists"
description: "Use the member filter to find LINE OA bound members, then export them or use them for marketing audiences."
created: 2026-03-06 11:20
last_modified: 2026-06-26 10:05
lang: en-US
permalink: "https://help.cyberbiz.io/ec/integrations/line/account-integration/filter-use-line-oa-bound-members/"
type: guide
author: Jase
reviewers: []
notes:
  - add CRL 會員名單篩選相關
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
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions: []
audiences:
  - merchant
difficulty: beginner
intents:
  - 篩選已完成 LINE 綁定的會員名單
  - 匯出 LINE 綁定會員名單至電子信箱
  - 打包 LINE 受眾並同步至 LINE OA 後台
  - 針對未綁定會員進行行銷應用
features:
  - 會員篩選器
  - 已完成 LINE 綁定篩選
  - 會員名單匯出
  - LINE 受眾打包
  - LINE OA 同步
prerequisites: []
related:
  - ec/integrations/line/account-integration/bind-line-oa-store-members/
  - ec/integrations/line/marketing/setup-line-oa-audience/
  - ec/notifications/send-line-friend-invitation/
tags:
  - "LINE Binding"
  - "Member Filter"
  - "Segmented Marketing"
  - "Audience Bundling"
  - "LINE OA Integration"
  - "List Export"
  - "Member Tags"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > 所有會員
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=721
comments: false
search:
  exclude: false
icon: lucide/user-check
hide:
---

![Member filter with completed LINE binding](../../../../assets/images/ec-會員-所有會員-篩選器-已完成line綁定.en.png){ .hero-page title="Member filter - LINE binding completed" }

## Filter LINE Bound Members Guide { #operate-use-line }

You can use the member filter in the admin panel to quickly identify which members have completed [**LINE OA and website member binding**](bind-line-oa-store-members.md){ title="Bind LINE OA with website members" }, so you can run follow-up segmented marketing or audience bundling.

Detailed instructions are below:

## Filter Bound Member List { #operate-use-line-bind }

1. **Access path**: Go to **Customer Management > All Customers** in the admin panel.
2. **Open the filter**: Click **Add Filter** in the search field or click the keyword input area. The system displays the filter criteria menu.
3. **Set filter criteria**:
    - In the dropdown menu, find the **Completed LINE Binding** (or **LINE@ Binding**) option.
    - Select **Yes** (to find bound members) or **No** (to find members who have not yet bound).
4. **Apply the filter**: Click **Apply**. The list below displays the members that match the criteria.

![Filter members with completed LINE binding](../../../../assets/images/ec-會員-會員篩選器-已完成line綁定-操作.en.gif){ title="Filter members with completed LINE binding" }

## Export and Use Member Lists { #operate-use-line-export }

1. **Export to email:**:
    - After filtering, select the members you want to export individually, or select all members on the current page at once, then click the **Export** button.
    - Read the notes, select the consent checkbox, and click **Agree to Export Data**.
    - The system sends the **Excel file** for this list to the specified email address.

	![Export member list](../../../../assets/images/ec-會員-所有會員-匯出.en.png){ title="Export member list" }

2. **Bundle LINE audience (Enterprise / PLUS only)**:
    - If you filter for bound members, when saving the segment you can choose to [**sync this audience package to the LINE OA admin panel**](../marketing/setup-line-oa-audience.md){ title="Set up LINE OA audience sync" }, for precise message pushes or ad campaigns.

## Next Steps { #next-steps-use-line }

<div class="grid cards" markdown>

- :lucide-user-round-plus:{ .lg }   
  [__Send LINE friend invitation__](../../../notifications/send-line-friend-invitation.md){ title="Send LINE friend invitation" }       
  For members who have not bound, merchants can use SMS or email to send a "LINE OA friend invitation" and provide coupon to improve the binding rate.

<!--
- :lucide-ban:{ .lg }     
  [____]()  
  .
-->

</div>

## FAQ { #faq-use-line }

??? quote "What is LINE binding?"
	In the filter, "Completed LINE Binding" means the member has linked their website member account with their LINE OA account.

??? quote "What is the difference between LINE binding and LINE quick login?"
	Members who sign in with "LINE quick login" have not necessarily completed "LINE OA binding." Merchants should guide members through the binding process before they can use advanced features such as LINE push notifications.

??? quote "Why does the number of "bound" members in the filter differ from the friend count in the LINE OA admin panel?"
	This is usually because the two use different definitions:

	- **Website admin:** Shows members who have completed linking their website member account with their LINE account.
	- **LINE OA admin:** Shows the total number of friends (including people who have not registered as website members, or who only follow the account without binding). In addition, if a member **blocks** your LINE Official Account after binding, the website admin may still show them as "bound," but the LINE admin excludes them from the valid audience.

??? quote "I just finished the LINE OA integration, but the filter does not find any bound members. Why?"
	Check the following two points:

	1. **Historical data:** Friends who added the LINE account before the integration was completed must click the "Member Binding" link in the menu again so the system can complete identity matching.
	2. **Sync time:** If you have just completed audience bundling, data sync to the LINE admin panel takes about **15-30 minutes**. We recommend checking LINE Official Account Manager later.

??? quote "Can I use "mobile number" or "Email" to filter LINE members who have not yet bound?"
	Yes. You can first use the filter in "All Members" and set "Completed LINE Binding: **No**," then export the list. This list contains the contact information for all members who have not bound, and you can use it to drive traffic through SMS or EDM.

??? quote "Why don't I see the "Sync to LINE OA" option in my admin panel?"
	This feature is exclusive to **Advanced PLUS / Expert PLUS / Enterprise**. If your plan qualifies but you still do not see the option, check the following:

	1. Whether you have correctly connected the **Messaging API** for LINE OA under "Third-party Integration."
	2. Whether your admin account has the "Member Export" or "Marketing Audience Bundling" permission.
