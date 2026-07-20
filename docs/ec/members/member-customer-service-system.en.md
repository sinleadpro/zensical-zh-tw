---
title: 會員客服系統
description: 學習如何配置官網內建的客服問答系統，包含設定問題主題、處理會員與訪客留言，以及管理訂單內的諮詢訊息。
created: 2026-02-12 00:00
last_modified: 2026-06-30 12:30
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes:
  - 內部連結：導覽列頁腳新增聯絡我們
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 會員
sites:
  - TW
audiences:
  - admin
difficulty: beginner
tnb: trunk
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 設定客服問題主題
  - 回覆會員詢問
  - 處理非會員留言
  - 匯出客服問答紀錄
features:
  - 客服問答系統
  - 訂單留言
  - 顧客回饋建議
prerequisites: []
related: []
tags:
  - 客服管理
  - 顧客關係
  - 售後服務
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 會員 > 客服問題分類
  - 會員 > 所有客服問題
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=275
  - https://www.cyberbiz.io/support/?p=2754
permalink: https://help.cyberbiz.io/ec/members/member-customer-service-system
comments: false
search:
  exclude: false
icon: lucide/headset
hide: []
---

# Membership Call Center System

Learn how to configure the Official Website&#39;s built-in Customer_Service_Q&amp;A system, Contains Setting question subjects, Process Membership and visitor Comment , and managing inquiry Message within Orders .
{ .subtitle }

![](../../assets/images/EC-Backend- Membership- All Customer Service Issue-Screen Overview){ .hero-page }

!!! tip &quot;Application Context&quot;
    - **Precise Triage Process**: Setting subjects such as &quot;Logistics Progress&quot; and &quot; Replace Apply &quot; to allow Call Center staff to quickly identify the core issues.
    - ** Create a communication history:** Message are linked to Membership Account, allowing you to track past communication details even if you Change Call Center windows.
    - **Data Optimization Suggestions**: Analyze common problems through the Export feature to serve as a basis for product Description optimization or FAQ creation.


## Mon Feature Guide

The Official Website &#39;Customer_Service_Q&amp;A mainly cover the less communication paths:

1. **Contact Us (Site-wide)**: Visitors can Comment via the form, whether Login in or not.
2. ** Orders Inquiry (Membership Only)**: Membership Comment on the Detailed page for a specific Orders , and the Message will be automatically marked with the order number.

## Tues.. Front-end setup and interactive scenarios

The less presents the interactive flow of ** Customer_Service_Q&amp;A**:


### 1. Contact Us Form

=== &quot;Customers Perspective&quot;

    Click **Contact the Store** in the Official Website navigation bar or footer, Select the subjects of your question, fill in Name, Email , and inquiry Value, and then submit it.
    The &quot;Contact Merchant&quot; field is a system-preset text; Store can manually Edit Name. After Setting it, please ensure that Customers are guided to click on the Specify text on the Pages to ensure a clear contact path.

    ![](../../assets/images/EC-Front-End-Contact UsForm01.png)

=== &quot;Store Perspective&quot;

    **Notification:** An orange point(s) has appeared next to the ** Membership ** option in the left-hand menu.
    - ** To Process this issue:** Goto shop to** Membership&gt; All Customer Service Issue** and click on :lucide-pencil: to reply.


### 2. Dedicated Orders inquiry

=== &quot;Customers Perspective&quot;

    After Login in, go to ** My Order(s)** and enter your question in the **Send a Message to the Store** section at the bottom of the Order Details .

    ![](../../assets/images/EC-Front-end- Menber Center- My Order(s)- Inquiry Call Center Questions 01.gif)

=== &quot;Store Perspective&quot;

    **Notification:** An orange point(s) has appeared next to the ** Membership ** option in the left-hand menu.
    - ** To Process this issue:** Goto shop to** Membership&gt; All Customer Service Issue** and click on :lucide-pencil: to reply.
      This Message will automatically populate the corresponding ** Order Number**. Click on it to View the Order content directly.


## We. Settings Call Center Subjects

Before Open the front-end Comment, you can Setting Problem Categories to distribute and Process Message accordingly.

1. Login in to the management backend and goto shop to** Membership&gt; Message Categories**.
2. Click ** Add Message Category**.
3. ** Subject Title**: Enter the item you want to show in the front-end menu (e.g., logistics progress, wholesale demand, Refund Apply).
4. Click ** Save**.

![](../../assets/images/EC-Backend- Membership- Message Categories- Create Message Categories Topic01.png)

## Th. Message Reply and Management

### 1. Respond to Membership inquiries

1. Goto shop to** Membership&gt; All Customer Service Issue**.
2. Point(S)** Edit** for the item that needs a reply.
3. Enter text in the reply box.
4. **Key Logic Select**:
    - **Click Save**: Officially Send your Value. The system will Send a notification email to the Membership.
    - **Clicking &quot;Close&quot;**: This only marks the Page publish status as ** Replied** and Remove the background notification number; **it will not Save or Send Message Content**.

!!! warning &quot;Operation restrictions&quot;
    Once you click ** Save** and submit Value reply, the system **cannot edit or delete it **. Please Enter the Value is correct before Send .

![](../../assets/images/EC-back- Membership- All Customer Service Issue-response and Close Call Center-issues01.png)

### 2. Process visitor (non- Membership) Comment

1. If the system none find the Membership Account in the Email address left by the visitor, please goto shop to** Membership&gt; Customer Feedback&amp; Suggestions**.
2. You need to use the Contact information left by the Customers (such as manually sending an Email or Phone Number) to reply externally.

![](../../assets/images/EC-Backstage- Membership- Customer Feedback and Suggestions- Overview)

### 3. Export Records and Analysis

1. Goto shop to** Membership&gt; Call Center Issues – By Membership Category**.
2. Select the Membership you want to analyze.
3. Point(S) on ** Select Operation&gt; Export messages ** at the top of the Pages . The system will generate an Excel file for you to download and analyze.

![](../../assets/images/EC-Backend- Membership- Message Sort by Member- Export messages Issues01.png)


## Frequently Asked Questions

Why did the Customers report not To a reply after clicking &quot; Close &quot;?
    ** Close** is a backend management Page publish status switch sent in Process issues that have already been resolved through Other channels (such as Phone Number). To ensure Customers To the response on the Official Website , they must enter the response text and click ** Save**.

Where can Customers To their response history?
    Membership can Login in to the Official Website and go to ** My Account&gt; Questions** to View 所有 their Value with the Contact Us .

Can I recall a Message if it&#39;s sent by mistake?
    The system currently does not support recalling or Edit Send Call Center replies. It is recommended to Create a**standard reply template** or a **pre-reply check process** to reduce errors.

Why To the &quot;All Customer Service Issue&quot; menu in the backend, and only To&quot;Message Management&quot;?
    This is a dynamic design implemented by the system to simplify the management interface; the path will automatically switch based on whether there are ** Process issues**.

    - ** When there are pending questions**: Please go to ** Membership&gt; All Customer Service Issue** to Process.
    - ** None are Any questions pending:** This menu will automatically switch to ** Message Management**.