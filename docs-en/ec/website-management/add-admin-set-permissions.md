---
title: "Add Website Admins and Set Permissions"
description: "Add website admins, set admin permissions, and manage account security and two-step verification."
created: "2026-03-13 12:29"
last_modified: 2026-07-02 19:47
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
  - 管理中心
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 新增管理員
  - 設定權限
  - 管理權限
features:
  - 網站權限
  - 管理者列表
  - 二階段驗證
prerequisites: []
related:
  - ec/website-management/references/admin-permissions-menu-reference/
tags:
  - "Website Admin"
  - "Permission Settings"
  - "Information Security"
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 網站權限 > 管理者列表
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1209
  - https://www.cyberbiz.io/support/?p=2881
permalink: "https://help.cyberbiz.io/ec/website-management/add-admin-set-permissions/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

![User Account Settings page](../../assets/images/ec-管理中心-網站權限.en.png){ title="User Account Settings page" .hero-page }

## Website Admins and Permissions { #intro-admin-perms }

Adding website admins and setting their permissions lets you divide admin panel work efficiently and strictly limit what each staff member can view or change based on their role.

## Steps { #operate-admin-perms }

### Add a Website Admin { #operate-admin-perms-add }

1.  **Go to the page**: Log in to the CYBERBIZ admin panel and go to **Website Management > User Account Settings > 管理者列表**.
2.  **Add an admin**: Click the **Add Admin** button on the page.
3. **Select permissions**: Select the [permissions](#specs-admin-perms){ data-preview } the new user should have.
4.  **Enter details**: Enter the new admin's name, email, password, and other required information, and then click **Add** to save.

![Add admin](../../assets/images/ec-管理中心-網站權限-新增管理員.en.gif){ title="Add admin" }

---

### Set and Change Admin Permissions { #operate-admin-perms-edit }

To change the permissions of an existing admin, follow these steps:

1.  **Open the editor**: In the admin list, **click the name of the admin you want to edit** to open the permission settings page.
2.  **Adjust the scope**: Based on your internal policies, select or clear the features this account can use. Permissions cover both storefront display and admin panel operations.
3.  **Save the settings**: When you finish, click **Save** to apply the changes.

![Change admin permissions](../../assets/images/ec-管理中心-修改管理者權限.en.gif){ title="Change admin permissions" }

## Permission Categories and Details { #specs-admin-perms }

System permissions fall into the following core categories, and each category can be broken down into specific features:

*   **Overview**: Whether the admin can view the admin panel dashboard overview.
*   **Customers**: Viewing all member data, VIP settings, and importing new members.
*   **Orders**: Can be split into management permissions for regular orders, subscription orders, e-ticket orders, and each type of shipping label.
*   **Products and product groups**: Whether the admin can edit all products, tags, and inventory, or specific promotion groups (such as Flash Sale for Single Product or Buy X Get Y Discount).
*   **Data export (security focus)**: Keep **Customer Export and Order Export** permissions to a minimum and grant them only to staff who need them, to lower security risks.
*   **Website settings**: Core system settings, including general settings, domain management, and email/SMS notification templates.

!!! note "For details, see [Admin Permissions and Admin Panel Menu Reference](references/admin-permissions-menu-reference.md){ title="Admin permissions and admin panel menu reference" data-preview }."

## Key Permission Rules and Security Reminders { #prerequisites-admin-perms }

1.  **Role levels**:
    *   **Website owner (Owner)**: Has the highest permissions, can manage all staff, and has no inventory management restrictions.
    *   **Co-Manager**: Can use most EC features, but POS store admin features are usually restricted, and this role cannot log in to the POS frontend.
2.  **Two-step verification (2FA)**: The website owner can check which staff have turned it on in Admin Security Verification, and can **require all staff to turn on two-step verification** to protect account security.
3.  **Removing and suspending staff**: When an employee leaves, suspend their account to close it. Once suspended, that person can no longer log in to the system.

## FAQ { #faq-admin-perms }

??? quote "Why can't a new admin log in to the admin panel?"
    Possible reasons:

    - **The account was not fully created**: Make sure the email and password were entered correctly and saved when the admin was added.
    - **The account is suspended**: A suspended user cannot log in.
    - **Two-step verification is not set up**: If the website requires **two-step verification (2FA)**, the admin must finish setting it up before logging in.

    Ask the **website owner (Owner)** or someone with admin permissions to check the account status.

??? quote "How do I change an existing admin's permissions?"
    Follow these steps:

    1. Go to **Website Management > User Account Settings > 管理者列表**.
    2. Click the **admin name** you want to change.
    3. Select or clear the feature permissions you need.
    4. Click **Save** to finish the update.

    The new permissions take effect immediately.

??? quote "Can I limit an admin to only some features?"
    Yes. When you add or edit an admin, **select specific feature permissions** based on your needs, for example:

    - Allow viewing **Orders** only
    - Allow managing **Product** only
    - Do not allow **Data export**

    Detailed permission settings make sure each employee can only access the system features related to their work.

??? quote "Which permissions are high-risk?"
    The following permissions involve **large-scale data access or core system settings** and should be granted only to staff who need them:

    - **Customer data export**
    - **Order data export**
    - **Website settings**
    - **Admin management**

    Limiting highly sensitive permissions lowers the risk of data leaks and mistakes.

??? quote "What is the difference between the website owner (Owner) and a regular admin?"
    The **website owner (Owner)** is the role with the highest permissions and can:

    - Manage all admin accounts
    - Set all system permissions
    - Require **two-step verification (2FA)**
    - Access all admin panel features

    Regular admins can only use the features they are authorized for and cannot change the system's top-level permission settings.
