---
title: "Shop with LINE Group Buy"
description: "How customers browse products, add items to their cart, and complete checkout through the group buy bot in a LINE group."
created: "2026-03-12 15:40"
last_modified: 2026-07-02 10:30
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
difficulty: beginner
tnb: branch
plans:
  - Enterprise
plan_options: []
cyb_extensions: []
intents:
  - 使用_LINE_團購購物
  - LINE_團購操作流程
  - LINE_團購結帳
features:
  - LINE 團購
  - 團購機器人
  - LIFF
  - 購物車
prerequisites:
  - ec/integrations/line/group-buy/setup-line-group-bot/
  - ec/integrations/line/group-buy/setup-line-group-buy-products/
  - ec/integrations/line/group-buy/setup-line-group-buy-group/
related:
  - ec/integrations/line/group-buy/setup-line-group-bot/
  - ec/integrations/line/group-buy/setup-line-group-buy-products/
  - ec/integrations/line/group-buy/setup-line-group-buy-group/
tags:
  - "LINE OA"
  - "LINE Group Buy"
  - "Group Buy Shopping"
  - LIFF
acoiv:
apis: []
devices:
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=29461
permalink: "https://help.cyberbiz.io/ec/integrations/line/group-buy/line-group-buy-shopping/"
comments: false
search:
  exclude: false
icon: lucide/shopping-cart
hide: []
---

## LINE Group Buy Shopping Guide

Customers who use the group buy feature are **members of a LINE group or multi-person chat room**. They mainly shop and check out by interacting with the **group buy bot**.

## Prerequisites

Before guiding customers to use the group buy feature, make sure the following settings are complete in the merchant back office:

- [x] **Group Buy Bot Setup**: Completed [LINE Group Buy Bot Setup](setup-line-group-bot.md){ title="Set Up LINE Group Buy Bot" }, and added the bot to the target group.
- [x] **Group Buy Product Setup**: Completed [LINE Group Buy Product Setup](setup-line-group-buy-products.md){ title="Set Up LINE Group Buy Products" }, and set the group buy prices.
- [x] **Group Buy Group Setup**: Completed [LINE Group Buy Group Setup](setup-line-group-buy-group.md){ title="Set Up LINE Group Buy Group" }, and configured the product categories, profit sharing, and campaign period.

## How to Trigger the Group Buy Feature

Customers can start shopping in one of two ways:

1.  **Open the Group Buy Bot Menu**:
    *   In the LINE group, type "**團購**". The system opens the group buy bot's rich menu.
    *   Tap "**Group Buy List**" in the menu to view the products in the current campaign.
2.  **Keyword Auto-Reply**: Customers can type specific text to trigger the matching feature:
    *   Type "**選單**" to open the main menu.
    *   Type "**團購**" to go directly to the product browsing page.
    *   Type "**加入好友**" to get a link to add the brand's official account.

![](../../../../assets/images/ec-第三方整合-line團購-喚醒選單.en.png)

## Browse and Select Products

After entering the group buy product list, customers follow these steps:

*   **Browse Products**: Tap the product image you want to buy. If there are many products, tap "**Show More Products**".
*   **View Details**: Tap the magnifying glass button on a product to open its details page and view its specifications and description.
*   **Select an Action**:
    *   Tap "**Add to Cart**" to save the product and keep shopping for other items.
    *   Tap "**Add and Check Out**" to go directly to the checkout page.

![](../../../../assets/images/ec-第三方整合-line團購-搜尋商品並結帳.en.png)

## Checkout and Payment Process

1.  **Go to the Cart/Checkout Page**:
    *   Customers can tap "**Go to Checkout**" in the bot menu.
    *   On the checkout page, customers can go back to continue shopping, or manually change item quantities in the cart.
2.  **Confirm the Amount and Place the Order**:
    *   Scroll to the bottom of the page to confirm the checkout total, then tap Go to Checkout.
    *   **Note**: The product amounts in the group buy cart already reflect group buy prices, so **general marketing campaigns on the website cannot be applied** (such as store-wide discount, gift with purchase, etc.).
3.  **Complete the Order**:
    *   After payment is complete, the system automatically redirects to the "Add Friend" page, which prompts customers to add the brand's LINE Official Account and turn group members into brand friends.

![](../../../../assets/images/ec-第三方整合-line團購-加入好友.en.png)

## Usage Notes

*   **Supported Environments**: This feature is available only in **LINE groups** or **multi-person chat rooms**. Because LINE communities (OpenChat) are anonymous, they are not currently supported.
*   **Account Binding**: The system uses LIFF to automatically apply the customer's LINE account information for quick sign-in, making the shopping process smoother.

## Frequently Asked Questions

??? quote "Why does nothing happen when I type group buy in a LINE community (OpenChat)?"
    The LINE group buy bot currently supports only LINE groups and multi-person chat rooms. Because LINE communities are anonymous, the LINE official API restricts some bot functions and information access in that environment, so the bot cannot be used there.

??? quote "Can group buy orders use website coupons or bonus points?"
    No. Because group buy products already have an exclusive group buy price, the amounts in the group buy cart are final prices to avoid overlapping discounts. Website general marketing campaigns are not supported (such as store-wide discount, gift with purchase, coupons, bonus redemption, etc.).

??? quote "What causes a sign-in failure or blank page after customers tap Go to Checkout?"
    Check the following two points:

    - LIFF setup: Check that LINE login authorization is turned on in the admin back office.
    - Browser environment: Make sure customers open the link directly within the LINE app, not copy the URL into an external browser (such as Safari or Chrome), so that the LIFF automatic sign-in works.

??? quote "Where can merchants view an order after the customer places it?"
    Merchants can sign in to the CYBERBIZ admin back office > Order Management > All Orders, then search and filter by "Order Source" or view order tags to identify orders from the LINE group buy channel. For details, see [](setup-line-group-buy-group.md#訂單查看與紀錄管理).md#order-viewing-and-record-management){ title="Set Up LINE Group Buy Group" }.

??? quote "Can the group buy bot operate in multiple groups at the same time?"
    Yes. As long as the bot has been invited to the group and the merchant back office has completed the group's binding and campaign setup, the bot can provide shopping guidance in multiple groups at the same time.
