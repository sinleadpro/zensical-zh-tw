---
title: "Permission Settings"
description: "Create custom job roles and assign module-based permissions to control exactly what each account can do in the system. This keeps core data safe and keeps duties clearly divided."
created: 2026-03-25 20:15
last_modified: 2026-06-30 22:04
lang: en-US
type: guide
author: Ann
reviewers: []
notes: []
ga_views: 0
feedback: 0
products:
  - WMS
modules:
  - 設定
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
intents:
  - 如何建立WMS角色
  - 設定員工功能權限
  - 限制帳號匯出權限
  - 配置倉庫人員操作範圍
features:
  - 角色權限管理
  - 模組化權限控管
  - 讀取/寫入/刪除維度
prerequisites: []
related: []
tags:
  - "Permission Settings"
  - "Role Management"
  - WMS
  - "Security Control"
  - "Division of Duties"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 角色名稱
  - 權限列表
  - 讀取/寫入/刪除/匯出
paths:
  - 設定 > 權限設定
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/permission-settings/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Permission Settings
Create custom job roles and assign module-based permissions to control exactly what each account can do in the system. This keeps core data safe and keeps duties clearly divided.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Smart Warehousing
{ .doc-badge }

![](../assets/images/WMS-後台-設定-權限設定-畫面總覽01.en.png){ .hero-page }


!!! tip "Use Cases"
    - **Separate duties**: Let warehouse staff work only with receipt orders and inventory management, and keep them out of sensitive areas such as Account Management.
    - **Data security**: Give junior store staff Read permission only, so they cannot delete product data by mistake or export order lists that contain personal data.
    - **Team operations**: Create a manager role with full Write permission to review and correct documents.


## Before You Start { #prerequisites-permissions }

- **Required field**: Role Name is required when you create a role.
- **Permission types**: The system offers four permission types: Read, Write, Delete, and Export. Select each one you want to grant.
- **Management limits**: Only roles with Write permission for permission management can change what other roles can access.


## Steps { #operate-permissions }

### Step 1: Open the Role Edit Page { #operate-permissions-enter }

1. Log in to the CYBERBIZ e-commerce warehouse admin panel and go to **設定 > 權限設定**.
2. Click **Create Role**, or click **Edit** for an existing role.


### Step 2: Set Role Details and Permissions { #operate-permissions-configure }

1. Enter the job title in the **Role Name** field (such as Warehouse Staff or Operations Manager).
2. In the **Assign accounts with this role** drop-down list, select the staff accounts to assign.
3. In the **Permission List**, select the permission types for each feature based on the job's duties.

![](../assets/images/WMS-後台-設定-權限設定-編輯角色01.en.png){ .screenshot }


!!! note "Permission Types"
    - **Read**: Can only view page information and lists.
    - **Write**: Can add, edit, or update data.
    - **Delete**: Can remove data.
    - **Export**: Can download system data as Excel or CSV files.


### Step 3: Save the Settings { #operate-permissions-save }

1. Check your selections, and then click **Save** at the bottom of the page.
2. The new permissions take effect as soon as the assigned accounts log in again.

