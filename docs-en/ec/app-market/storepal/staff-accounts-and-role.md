---
title: "Staff Accounts and Roles"
description: "Learn how to set up basic features, account permissions, and sales attribution rules in the Store Assistant admin, and manage staff accounts and personal QR codes."
created: 2026-05-08 10:11
last_modified: 2026-06-18 10:11
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
  - 設定門市助理帳號權限
  - 建立門市人員帳號
  - 設定業績歸因規則
  - 編輯簡訊通知模板
features: 
  - "Store Assistant"
  - "Permission Management"
  - "Sales Attribution"
  - QR Code
prerequisites: []
related: []
tags: 
  - 門市助理
  - "Account Settings"
  - 權限管理
  - 業績歸因
acoiv: configure
apis: []
devices: []
ui_components: 
  - 門市角色與權限
  - 新增門市人員帳號
  - 專屬綁定 QRcode
  - 前台功能設定
  - 業績歸因設定
  - 通知設定
paths:
  - 設定 > 管理帳號設定
  - 設定 > 操作紀錄
layouts: []
wp_url: 
  - https://www.cyberbiz.io/support/?p=40979
permalink: "https://help.cyberbiz.io/ec/app-market/storepal/staff-accounts-and-role/"
comments: false
search:
  exclude: false
icon: lucide/settings
hide: []
---

# Staff Accounts and Roles
Store Assistant lets you manage store sales attribution, account permissions, and staff accounts, helping you build a complete store operations system.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | All PLUS / Enterprise<br>
[:lucide-grid-2x2-plus:{ title="Applicable Add-ons" }](../../resources/conventions#適用擴充) | Store Assistant
{ .doc-badge }


!!! tip "Use Cases"
	- **Permission Control**: Assign management permissions by level, such as headquarters, region, or store, to keep data secure.
	- **Sales Attribution**: Attribute sales to a store or individual staff members as the basis for bonuses or performance reviews.
	- **Digital Linking**: With each staff member's personal QR code, customers can register as members and link a referrer while adding your LINE account as a friend.


## Before You Start { #prerequisites-staff-access }

- Store Assistant is a paid add-on. Contact CYBERBIZ customer service to activate it.
- Each store can have only one **Active** store manager. Deactivate the current store manager account before adding a new one.
- Activated accounts cannot be deleted. You can only stop using them with **Deactivate**.
- We recommend having LINE Certified Provider status so customers can register and link with a single QR code scan.

## Role Login Permissions { #prerequisites-role-permissions }

Store Assistant has four roles. Their login permissions are shown below:

| Role | Admin Login | Frontend Login | Description |
| :--- | :---: | :---: | :--- |
| **Headquarters Manager** | V | | Manages all brand stores in the admin |
| **Group Manager** | V | | Manages stores in their group in the admin |
| **Store Manager** | V | V | Manages their store in the admin and uses the frontend |
| **Store Staff** | | V | Uses the frontend only for member service and referral sales |


## Manage Accounts { #operate-staff-access }

### Role Hierarchy Authorization Table { #operate-staff-access-manage-role-authorize }

| **Account Permission \ Roles It Can Create** | Headquarters Manager | Group Manager | Store Manager | Store Staff |
| ------------------------- | --------- | --------- | ------- | -------- |
| **Headquarters Manager** | V | V | V | V |
| **Group Manager** |  | V | V | V |
| **Store Manager** |  |  |  | V |
| **Store Staff** |  |  |  |  |

### Create Manager Roles { #operate-staff-access-create-manage-role }

1. Go to **設定 > 管理帳號設定**.
2. Click **Add Manage Account**, set the account and password, and assign a role.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定13.png){ .screenshot }

    - If the role is **Group Manager**, also select the store group they manage.
    - After a role is added, you can edit the person's role and name, but not the email address.

        ![](https://www.cyberbiz.io/support/wp-content/uploads/POS-後台-門市管理-門市人員帳號-新增管理者帳號01.png){ .screenshot }



### Create Store Staff { #operate-staff-access-create-store }

1. Go to **Store Management**. The system shows the stores available to your role.
2. Click **[a specific store]** to open its management page.
3. Click the **Store Staff Accounts** tab, then click **Add Store Staff Account**.

![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定05.png){ .screenshot }

### Manage Store Staff { #operate-staff-access-manage-store }

1. **Edit**
    Edit the person's role and name. The email address cannot be changed.
2. **Deactivate**
    Deactivated store staff can no longer log in.
3. **Use the Personal Binding QR Code**
    - **How to Use**: Click **Download** to save the QR code image, or click **Copy** to get the personal binding link.
    - **Use Case**: Staff guide customers to scan the code in store, so customers are linked to the staff member automatically when they register.


![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定09.png){ .screenshot }


#### Bulk Creation { #operate-staff-access-create }

Use Excel to create or edit staff accounts for all brand stores in bulk.

1. Go to **Store Management** and click **匯入 > 人員帳號與修改權限**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員01.png){ .screenshot }

2. Click **Download Excel Sample**, fill in the data, and click **Upload File**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員02.png){ .screenshot }

3. View upload records in **Upload Progress**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員03.png){ .screenshot }


!!! warning "Import Notes"
    - Do not change the Excel column headers.
    - Store: Only existing, active stores are accepted.
    - Role: Enter the role name for store manager or store staff exactly as defined in the template.
    - Name: Required.
    - Email: Required. Emails cannot be duplicated for the same role in the same store.
    - Password: Enter at least 6 characters.

#### Bulk Edit Staff Permissions { #operate-staff-access-edit-permissions }

If you manage staff and permissions for multiple stores, use Excel to edit role permissions in bulk and save time.

1. Click **Export**. The system sends an Excel file to your login email.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員04.png){ .screenshot }

2. Open the downloaded file and adjust the permission settings for each store (on/off).

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員05.png){ .screenshot }

3. Go back to **Store Management** and click **匯入 > 人員帳號與修改權限**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員01.png){ .screenshot }

4. Click **Upload File** and select **Roles and Permissions**.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員06.png){ .screenshot }

5. Select the edited file and click **Confirm**.


6. View upload records in Upload Progress.
    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-後台-門市管理-批次建立修改門市人員03.png){ .screenshot }

### Set Role Permissions { #operate-staff-access-settings-role-permissions }

You can set different feature permissions for the store manager and staff roles in each store based on your business needs.


- Member Basic Information

    When turned on, the role can edit **Member Basic Information** on the member information page.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-1.png){ .screenshot }

* Member Notes

    When turned on, the role can edit Member Notes in the member notes section.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-2.png){ .screenshot }

* Store Tags

    When turned on, the role can edit Store Tags in the member notes section.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-5.png){ .screenshot }

* coupon Redemption

    When turned on, the role can use coupon on the member information page.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-3.png){ .screenshot }

* Enter Store Purchases

    When turned on, the role sees the Add Store Purchase button in member features.

    ![](https://www.cyberbiz.io/support/wp-content/uploads/門市助理-功能與帳號設定04-4.png){ .screenshot }



## FAQ { #faq-staff-access }

??? quote "Why can't I add a second store manager?"
    Each store can have only one active store manager. To replace the store manager, change the current store manager's account status to Deactivated first, then add the new one.

??? quote "Can staff accounts be deleted?"
    To keep operation history and sales data, accounts cannot be deleted. When staff leave, use Deactivate.

??? quote "How do I view staff activity logs?"
    Headquarters managers can go to **設定 > 操作紀錄** to view login records and frontend and admin actions for all staff.

