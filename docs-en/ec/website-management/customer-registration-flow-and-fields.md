---
title: "Customer Registration Flow and Fields"
description: "A good registration flow can greatly improve new customer conversion. Choose the Registration Required or Quick Checkout mode based on your business strategy, and use custom fields to collect more detailed member information."
created: 2026-02-12 00:00
last_modified: 2026-06-04 17:59
lang: en-US
type: guide
author: Ann
reviewers: []
notes:
  - 內部連結：樣板設定
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
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 選擇註冊結帳模式
  - 設定預設與自訂欄位
  - 開啟電子郵件或手機驗證
  - 設定註冊完成跳轉頁
features:
  - 顧客註冊設定
  - 自訂註冊欄位
  - 註冊後跳轉
prerequisites: []
related:
  - ec/members/batch-import-and-edit-members/
  - ec/notifications/manage-email-templates/
tags: []
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths:
  - 管理中心 > 顧客註冊設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=7209
  - https://www.cyberbiz.io/support/?p=36853
permalink: "https://help.cyberbiz.io/ec/website-management/customer-registration-flow-and-fields/"
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---
# Customer Registration Flow and Fields

A good registration flow can greatly improve new customer conversion. Choose the Registration Required or Quick Checkout mode based on your business strategy, and use custom fields to collect more detailed member information.
{ .subtitle }

![](../../assets/images/EC-前台-會員註冊頁01.en.png){ .hero-page }

!!! tip "Use Cases"
    - **Improve the checkout experience**: Turn on Quick Checkout and Register to lower the barrier to a first purchase and shorten the path to buying.
    - **Build fuller member profiles**: For industries such as beauty or pets, use custom fields to collect skin type or pet type for targeted marketing.
    - **Strengthen security**: Turn on email or mobile verification to make sure member data is genuine and reduce ghost accounts.


## Before You Start { #prerequisites-customer-reg }

Before you change registration settings, note the differences and limits between plans:

- **Required field rule**: The system requires **at least one** of **Email** or **mobile number** to be required.


## Step 1: Choose the Customer Registration and Checkout Mode { #operate-customer-reg-mode }

Choose the checkout flow that best fits your business model.

1. Log in to the admin panel and go to **Website Management > Member Registration Setting**.
2. In the **Member Registration** section, choose a mode:
    - **Fast checkout with registration**: Customers can go to the checkout page first and log in during checkout, or register when they place the order.
    - **Registration required**: Customers must register and log in before they can check out.
3. Click **Save**.

![](../../assets/images/EC-後台-管理中心-顧客註冊設定-選擇註冊方式01.en.png)

## Step 2: Set Default Field Properties { #operate-customer-reg-fields }

The field options you can set depend on your plan:

=== "Enterprise"

    The Enterprise plan offers a highly flexible field management interface:

    - **Default field control**: Set name, email, mobile number, birthday, and gender as **required or optional** and **shown or hidden on the storefront** one by one.
    - **Advanced property settings**: Choose whether each field appears on the **Registration Page**, the **Checkout Page**, or the **member profile page**, and whether members can edit it themselves after registering.


    !!! warning "System Limits"
        Some settings for default fields are defined by the system and can't be changed.

    ![](../../assets/images/EC-後台-管理中心-顧客註冊設定-企業版-註冊欄位設定01.en.png)

=== "Other Plans"

    Other plans provide a basic, standard registration setup:

    - **Default field properties**: Supports basic fields such as name, email, mobile number, birthday, and gender.
    - **Required**: You can make the email or mobile account field required.

    ![](../../assets/images/EC-後台-管理中心-顧客註冊設定-一般版-註冊欄位設定01.en.png)


## Step 3: Set up Account Verification and Redirects { #operate-customer-reg-verify }

### 1. Turn on Customer Verification { #operate-customer-reg-enable }

To improve the quality of your member list, turn on verification.

1. Turn on **Email Verification** or **Mobile Verification**.
    - If both are on, the system sends the email verification first by default.
2. With verification on, members receive an **account activation notification** by email or SMS when they register, and must open it and click the link to finish verification.

    > **Template path**: Go to **Push Notifications > 通知樣板 > 顧客相關** to edit the **Customer Account Activation Reminder** template.



### 2. Redirect After Registration { #operate-customer-reg-redirect }

1. Find the **Registration page redirect setting** section and turn on the switch.
2. Enter the link you want to send members to.

!!! info "Plan Availability"
    Redirect after registration is only available on **Expert PLUS and Enterprise** plans.

![](../../assets/images/EC-後台-管理中心-顧客註冊設定-設定驗證與跳轉01.en.png)

## Step 4: Create and Manage Custom Fields { #operate-customer-reg-custom }

### Feature Limits { #prerequisites-customer-reg-custom }

- **Plan availability**: This feature is only available to **Expert PLUS and Enterprise** customers.
- **Theme limits**: Custom fields only work with **drag-and-drop** themes.
- **Quantity and editing limits**: You can create **up to 10** custom fields. Once a field is created, it can't be deleted or edited. If you don't want to show it, you can only set it to **Hidden**.
- **Security and personal data protection**: If you use custom fields to collect sensitive personal data (such as national ID numbers or medical information), make sure your website's **privacy policy** clearly explains why you collect it.

### Add a Custom Field { #operate-customer-reg-add-field }

1. Click the **Add new custom field** button.
2. Choose a field type. The system supports these five types:
    - **Image upload**: For uploading warranty cards, certificates, or receipts.
    - **Text box**: Lets members enter short text freely.
    - **Checkbox**: Supports multiple selections.
    - **Dropdown**: Preset options for members to choose one.
    - **Date picker**: A standard year/month/day picker.
3. Enter the **Field Name** and click **Confirm**.

![](../../assets/images/EC-後台-管理中心-顧客註冊設定-新增自訂欄位01.en.png){ .hero-page }

### Bulk Import Custom Data { #operate-customer-reg-import }

To include custom field data when you import members in bulk, follow these rules:

- **Supported types**: Text box, dropdown, and date picker.
- **Unsupported types**: Image upload and checkbox.

To edit the Excel template:

1. In the member import template, manually add a column header in the format `[0]自訂欄位名稱` (for example, `[0]會員編號`).
2. Enter the information that matches each field type.
  - Date format: Always use YYYY/MM/DD.
  - Dropdown: The value must exactly match the option text set in the admin panel.
3. To download the member template and upload the file, see [Bulk Import New Members](../members/batch-import-and-edit-members.md).

!!! tip "Bulk Edit Custom Fields for Existing Members"
    - **Applicable plans**: Only the **Enterprise** plan can overwrite or change custom fields for existing members in bulk.
    - **Other plans**: Custom fields can only be included when you bulk import new members. You can't update custom fields for existing members with bulk edits.
    - **Related steps**: On the Enterprise plan, go to [Bulk Edit Existing Member Data](../members/batch-import-and-edit-members.md#operate-batch-members-edit).


![](../../assets/images/EC-後台-會員-所有會員-新會員匯入範本新增自訂欄位01.en.png)


## Related Reading { #reference-customer-reg }

<div class="grid cards" markdown>

- :lucide-user-plus:{ .lg }
  [__Bulk Import New Members__](../members/batch-import-and-edit-members.md#operate-batch-members-import)
  Learn how to download the Excel template and upload member lists in bulk.

- :lucide-mail:{ .lg }
  [__Set Up Email Notification Templates__](../notifications/manage-email-templates.md)
  Customize the account activation email to improve your first message to new members.

</div>
