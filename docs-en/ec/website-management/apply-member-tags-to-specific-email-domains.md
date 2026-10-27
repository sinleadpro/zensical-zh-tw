---
title: "Apply Member Tags to Specific Email Domains"
description: "With email domain settings, the system can automatically tag members from specific organizations (such as company employees or school members) when they finish registering, so you can offer them exclusive promotions or segmented services later."
created: 2026-02-03 00:00
last_modified: 2026-06-04 17:59
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
  - 管理中心
  - 會員
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
  - 設定自動貼標規則
  - 管理網域信箱條件
features:
  - 會員標籤
  - 自動貼標
  - 網域限制
prerequisites:
  - "需預先規劃欲使用的會員標籤名稱"
related:
  - ec/members/batch-import-and-edit-members/
  - ec/members/manage-member-profiles/
tags:
  - "Employee Group Buying"
  - "Preferred Partner"
acoiv: configure
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 管理中心 > 網域信箱標籤設定
  - 會員 > 所有會員
layouts: []
wp_url:
  - https://www.cyberbiz.io/support/?p=11515
permalink: "https://help.cyberbiz.io/ec/website-management/apply-member-tags-to-specific-email-domains/"
comments: false
search:
  exclude: false
icon: lucide/mail
hide: []
---
# Apply Member Tags to Specific Email Domains

With email domain settings, the system can automatically tag members from specific organizations (such as company employees or school members) when they finish registering. You can then offer them exclusive promotions or segmented services.
{ .subtitle }

[:lucide-tag:{ title="Applicable Plans" }](../../resources/conventions#適用方案) | Enterprise
{ .doc-badge }

![](../../assets/images/EC-後台-管理中心-網域信箱標籤設定-畫面總覽01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Employee purchase programs**: Set your company domain (such as `@cyberbiz.at`) so that employees are automatically tagged **Employee Purchase** when they register and get exclusive discounts.
    - **Partner organization management**: Automatically tag members from partner or specific educational institution domains for segmented push notifications.
    - **Brand ambassador tracking**: Automatically group members from specific partner domains when they register, which simplifies list management.


## Before You Start { #prerequisites-domain-tags }

Before you set up domain tag rules, note the following limits:

- **Who it applies to**: Only members who **register after** the rule is set up. The system does not go back and tag members who existed before the rule was set.
- **Import limits**: Customer data added through **Excel bulk import** does **not** support automatic tagging.

     > When you use [Excel bulk import members](../members/batch-import-and-edit-members.md#specs-batch-members){ title="Bulk import or edit members" }, just fill in the tag field in the template, and the tags are applied automatically when you import.

- **Effect of changes**: Changing or deleting an existing domain tag setting does not affect members who already have the tag.
- **Format rules**: Make sure to enter the correct email domain (the text after @). Spaces or typos will cause automatic tagging to fail.



## Steps { #operate-domain-tags }

### Step 1: Create a Tag Condition { #operate-domain-tags-create }

1. Log in to the CYBERBIZ admin panel and go to **Website Management > Email Domain Tag Settings**.
2. Click **Add mappings** in the upper-right corner of the page.

![](../../assets/images/EC-後台-管理中心-網域信箱標籤設定-新增網域信箱01.en.png)

### Step 2: Enter the Settings { #operate-domain-tags-fill }

Enter the following information in the pop-up window or edit page:

1. **Title**: Enter a name to identify the rule (for example, 2024 Corporate Partnership). This field is only used to identify the rule in the admin panel.
2. **Member tag**: Enter the tag name the system should apply automatically (for example, Employee Purchase or Partner).
    - If the tag does not exist yet, it is created when you enter it.
3. **Email domain**: Enter the domain string to match.
    - **Format**: Enter only the part after `@`.
    - **Example**: For `name@gmail.com`, enter `gmail.com`.

### Step 3: Save and Verify { #operate-domain-tags-save }

1. After you check the information, click **Confirm** to save the setting.
2. **Testing tip**: Register a test account with an email address in that domain, and then go to **Customer Management > All Customers** to check that the account has the correct tag.



## FAQ { #faq-domain-tags }

??? quote "If a member matches more than one domain condition, are all the tags applied?"
    If the email domain a member registers with matches several rules (for example, a subdomain rule and a parent domain rule), the system applies all the tags from the matching rules.

??? quote "If I change a domain tag setting, do existing members' tags change too?"
    No. Domain tag settings are triggered **at the time of registration**. Once a member has registered and been tagged, later changes to or deletion of the rule do not change the tags that member already has.




## Related Reading { #reference-domain-tags }

<div class="grid cards" markdown>

- :lucide-tags:{ .lg }
  [__Manage Tags for Individual Members__](../members/manage-member-profiles.md#operate-member-profiles-tags){ title="Manage member profiles" }
  Learn how to manually add tags to or remove tags from individual members.


</div>
