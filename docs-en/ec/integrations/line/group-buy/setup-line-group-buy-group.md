---
title: "Set up LINE Group-Buy Group"
description: "Set up commission plans, product categories, and campaign times for LINE group buying so group leaders can run group-buy campaigns inside LINE groups."
created: "2026-03-12 12:14"
last_modified: 2026-07-02 10:26
lang: en-US
type: guide
author: Jase
reviewers: []
notes: 
  - WP 上有影片之後看要不要搬
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
tnb: branch
plans:
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 設定_LINE_團購群組
  - LINE_團購分潤設定
  - 團購活動管理
features:
  - LINE 團購
  - 團購群組
  - 分潤方案
  - 推薦碼
prerequisites:
  - ec/integrations/line/group-buy/setup-line-group-bot/
  - ec/integrations/line/group-buy/setup-line-group-buy-products/
related:
  - ec/integrations/line/group-buy/setup-line-group-bot/
  - ec/profit-sharing/referrer-profit-sharing/
  - ec/integrations/line/group-buy/setup-line-group-buy-products/
  - ec/profit-sharing/query-profit-sharing-partners-and-codes/
tags:
  - "LINE OA"
  - "LINE Group-Buy"
  - "Group-Buy Group"
  - Commission
acoiv:
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=29174&page=4
permalink: "https://help.cyberbiz.io/ec/integrations/line/group-buy/setup-line-group-buy-group/"
comments: false
search:
  exclude: false
icon: lucide/messages-square
hide: []
---

![LINE Group-Buy Group Setup](../../../../assets/images/ec-第三方整合-line團購群組.en.png){ title="LINE Group-Buy Group Setup" .hero-page }

## LINE Group-Buy Group Overview { #overview-line-group }

**"LINE Group-Buy Group Setup"** is the core step of the LINE group-buy feature. Merchants can configure each group's commission plan and referral code here, manage campaign content, and view history records.

## Prerequisites { #prerequisites-line-group }

Before editing group content, merchants must complete the following three setup steps in order:

- [x] [**LINE Group-Buy Bot Setup**](setup-line-group-bot.md){ title="Set Up LINE Group-Buy Bot" }: Create a dedicated bot and complete the Messaging API and LIFF integration.
- [x] [**Referral Commission Code Setup**](../../../profit-sharing/referrer-profit-sharing.md){ title="Referrer Commission" }: Set up the "Referrer Commission" plan in the commission system.
- [x] [**Group-Buy Product Category Setup**](setup-line-group-buy-products.md){ title="Set Up LINE Group-Buy Products" }: Select the products to sell and set the group-buy price.

## Add a LINE Group-Buy Group { #operate-line-group }

1.  Merchants must first ask the group leader to add the "Group-Buy Bot" as a friend of the LINE Official Account.
2.  The group leader invites the **Group-Buy Bot** into the specific LINE group-buy group.
3.  After the bot joins the group, the system **automatically adds** the group name and group ID to the back-end "Group List" (the bot status shows `Already added`).
4.  Note that **each LINE group can have only one bot at a time**.

![Bot Joined Group](../../../../assets/images/ec-第三方整合-line團購群組-機器人已加入.en.png){ title="Bot Joined Group" }

## Edit Group Campaign Content { #operate-line-group-edit-content }

1.  **Open settings**: In the back-end group-buy group list, select the target group, then click "Edit":lucide-square-pen: to go to the "Basic Settings" page.
2.  **Bind commission**: Select the **"Referral Commission Plan", "Referrer", and "Referral Code"** for the group's campaign.
3.  **Apply products**: Select the "**Group-Buy Product Category**" to apply to the campaign.
4.  **Set the time**: Set the campaign start time. If you don't change the default "Specified Start Time," the campaign starts from the moment you click "Save."
    *   *Note: You can update the time at any time before the campaign starts. After it starts, the time can't be changed. You can only end it early.*

![Edit Group Campaign Content](../../../../assets/images/ec-第三方整合-line團購群組-編輯頁.en.png){ title="Edit Group Campaign Content" }

## When a Group-Buy Campaign Ends { #intro-line-group }

A group-buy campaign ends in the following three cases:

-  **Manual end**: In "Basic Settings," click "End Group-Buy Campaign."
    *   *After a manual end, the system keeps only the group name and ID. To restart the campaign, you must set the other fields again.*
-  **Time expires**: The campaign reaches the "Specified End Time" you set.
-  **Bot leaves group**: When the group-buy bot is removed from the LINE group, the campaign also ends.

![End Group-Buy Campaign](../../../../assets/images/ec-第三方整合-line團購群組-結束團購活動.en.png){ title="End Group-Buy Campaign" }

## Viewing Orders and Managing Records { #reference-line-group }

*  **View orders**: Merchants can go to "**Orders**** > ****All Orders**", expand the filter, and select "**LINE Group-Buy**" to view the related orders.

    ![Filter LINE Group-Buy Orders](../../../../assets/images/ec-訂單-所有訂單-篩選line團購訂單.en.gif){ title="Filter LINE Group-Buy Orders" }

*  **Campaign history**: After a campaign ends, its data moves to the "Group-Buy History" section on the edit page, so merchants can review the group's past campaign performance at any time.

    ![Group-Buy History](../../../../assets/images/ec-第三方整合-line團購群組-編輯頁-團購歷史紀錄.en.png){ title="Group-Buy History" }

*  **Commission lookup**: If the group leader wants to check order activity, merchants can provide the [commission report download link](../../../profit-sharing/query-profit-sharing-partners-and-codes.md#operate-ps-query-external){ title="Look Up Commission Partners and Codes" } for them to review.


## FAQ { #faq-line-group }

??? quote "Why doesn't my LINE group appear in the back-end list?"

    Check the following two points:

    1. Has the bot successfully joined the LINE group? (It must be invited in by the group leader.)
    2. After the bot joins, type any text in the group (for example: `Hello`) to trigger the first connection between the bot and the system. Only then does the system sync the group ID to the back end.

??? quote "If the group leader accidentally removes the bot from the group, does the campaign disappear?"
    After the bot leaves the group, **the current campaign ends immediately**. Past order records are kept in "Group-Buy History," but to restart, you must invite the bot back into the group and set up "Basic Settings" and "Bind Products" again.

??? quote "Can one LINE group-buy group run multiple commission plans at the same time?"
    **No.** A group can link only one "Referral Code" and one "Group-Buy Product Category" at a time. If you need a new campaign period, end the old campaign first, then set it up again.
