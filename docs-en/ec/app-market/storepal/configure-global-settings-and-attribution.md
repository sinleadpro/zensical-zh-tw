---
title: "Configure Global Settings and Sales Attribution"
description: "Help headquarters admins configure brand-wide Store Assistant feature switches, and guide admins at each level to set the sales attribution level for individual stores."
created: 2026-06-22 10:11
last_modified: 2026-06-22 10:11
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
  - APP MARKET
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: branch
plans:
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
plan_options: []
cyb_extensions:
  - STORE PAL
intents:
  - 設定業績歸因規則
  - 編輯簡訊通知模板
features:
  - "Store Assistant"
  - 權限管理
  - "Sales Attribution"
  - QR Code
prerequisites: []
related: []
tags:
  - 門市助理
  - 業績歸因
acoiv: configure
apis: []
devices: []
ui_components:
  - 前台功能設定
  - 業績歸因設定
  - 通知設定
paths:
  - 設定 > 功能設定 > 前台功能設定
  - 設定 > 功能設定 > 業績歸因設定
  - 設定 > 通知設定
  - 設定 > 操作紀錄
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=40979
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/configure-global-settings-and-attribution/"
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---
# Configure Global Settings and Sales Attribution
Help headquarters admins configure brand-wide Store Assistant feature switches, and guide admins at each level to set the sales attribution level for individual stores.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }

## Global Settings { #operate-storepal-settings }

**Headquarters admins** can set rules for all stores.

### Frontend Feature Switches { #operate-storepal-settings-section }

Go to **設定 > 功能設定 > 前台功能設定** to turn each **Store Assistant frontend** feature on or off.

* coupon

    When turned on, store staff across the brand can view and use the coupon section in the frontend interface.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定17.png){ .screenshot }



* Storewide coupon

    When turned on, store staff across the brand can view and use the storewide coupon section in the frontend interface.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定25.png){ .screenshot }



* bonus points

    This has two options: "Show bonus points" and "Use bonus points". When turned on, store staff across the brand can view or use the bonus points section in the frontend interface.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定18.png){ .screenshot }



* Recommended Products

    When turned on, store staff across the brand can use the recommended products feature in the frontend interface.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定19.png){ .screenshot }



* Sales Report

    When turned on, store staff across the brand can view the store's sales overview report in the frontend interface.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定20.png){ .screenshot }



* Member Tags

    - **Specify Display Member Tags**

        When turned on, headquarters admins can select up to 10 member tags to show on the Store Assistant frontend. When a member has a matching tag set in the EC admin, store staff across the brand can see that tag in the frontend.

    - **Tag Group Settings**

        * When turned on, custom store tags appear on the Store Assistant frontend. Also make sure the feature is turned on for the stores that will use it on the **Roles and Permissions settings page**.
        * When store staff select tags on the member information page in the frontend, store staff across the brand can see that member's tags in the frontend, and the offline tags also appear on the member page in EC.
        * You can set up to 5 tag groups, with up to 10 tags in each group.

    ![Member Tags](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定21.png){ .screenshot }

### Global Sales Attribution Rules { #operate-storepal-settings-global-rules }

Go to **設定 > 功能設定 > 業績歸因設定** to set the **brand-wide sales attribution** rules.

- Attribution Period

    Set the linking attribution period based on your business needs. During this period, valid orders members place on their own on the online store are automatically attributed to the linked store or staff member.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定22.png){ .screenshot }


- Recommended Product Attribution

    Choose who gets credit for **orders placed through recommendation links**:

    - Linked store referrer
    - Product referrer

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定23.png){ .screenshot }

!!! warning "Change Limitation"
    You can change the sales attribution fields yourself only **once**. To make more changes, contact CYBERBIZ customer service.

### SMS Notification Switches { #operate-storepal-settings-sms-toggle }

Go to **設定 > 通知設定** to turn **notification types** on or off and edit SMS templates.

#### SMS Notification Types { #operate-storepal-settings-sms-types }

- Registration notification: On by default and cannot be turned off
- Account activation notification: On by default and cannot be turned off
- Store referrer linking notification
- Product recommendation notification: Used as both the SMS template for **Send SMS** and the link template for **Share Product Link**.

After a notification is turned on, store staff can send that type of SMS to customers.

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-設定-通知設定-簡訊列表01.png){ .screenshot }

#### Edit SMS Templates { #operate-storepal-settings-sms-template }

1. Click the title of a notification type to open the edit page and customize the SMS template.
2. Enter the SMS content you want in the text editor. You can adjust the tone and style freely.
3. Click **Save** to apply it to newly sent SMS messages immediately.
4. To restore it, use **Reset to default**.

!!! warning "System Parameter Editing Limitation"
    {{...}} are system parameters. You can move or delete them, but **you cannot change parameter names**.

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-設定-通知設定-編輯簡訊模板01.png){ .screenshot }

### View Activity Logs { #operate-storepal-settings-operation-logs }

Headquarters admins can monitor all staff login records and actions to keep operations secure.

1. Go to **設定 > 操作紀錄**.
2. The system lists login records and actions for group admins, store managers, and store staff.

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-設定-操作紀錄-查看操作紀錄01.png){ .screenshot }

## Manage Stores { #operate-store-management }

### Set Store Sales Attribution { #operate-store-management-store-attribution }

The store management list shows the stores you can configure based on your role:

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定02.png){ .screenshot }

| Role | Stores Shown |
| -------- | ------- |
| Headquarters admin | All stores |
| Group admin | Stores in the account's group |
| Store manager | The single store assigned to the account |
| Store staff | None |




1. In the **Store Sales Attribution Settings** section of the store page, select the attribution level (Store/Staff).
    - With store-level attribution, staff sales are combined at the store level (store sales).
    - With staff-level attribution, sales are calculated separately for each staff account (personal sales).

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定03.png){ .screenshot }

2. Click **Save** to finish.



!!! warning "Attribution Level Change Limitation"
    You can change the attribution level yourself once. To make more changes, contact CYBERBIZ customer service.