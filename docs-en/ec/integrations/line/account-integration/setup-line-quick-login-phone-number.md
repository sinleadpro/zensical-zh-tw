---
title: "Set up Member Phone Number Retrieval in LINE Quick Login"
description: "Connect LINE verified permissions to automatically retrieve and verify member phone numbers during quick login, improving account matching accuracy and data completeness."
created: 2026-02-16 00:00
last_modified: 2026-08-05 11:20
lang: en-US
permalink: "https://help.cyberbiz.io/ec/integrations/line/account-integration/setup-line-quick-login-phone-number/"
type: guide
author: Jase
reviewers: []
notes:
  - verify oc_phone_number 功能的版本差異
ga_views: 0
feedback: 0
products:
  - EC
modules:
  - 第三方整合
sites: []
audiences:
  - merchant
  - merchant
difficulty: intermediate
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 取得 LINE 用戶手機號碼
  - 透過 LINE Login 更新會員資料
  - 啟用手機號碼比對功能
  - 設定 LINE LIFF phone scope
features:
  - LINE 快速登入取得手機號碼
  - LINE Certified Provider 需求
  - LINE OA 認證帳號需求
  - 手機號碼優先比對
  - LIFF phone scope 整合
  - 非追溯性資料取得
  - SMS 驗證整合
  - 隱碼手機號碼顯示
prerequisites:
  - 完成 LINE 快速登入串接
  - LINE Provider 認證 (LINE Certified Provider)
  - LINE 官方帳號認證 (藍色盾牌或綠色盾牌)
related:
  - ec/integrations/line/account-integration/setup-line-quick-login/
  - ec/integrations/line/account-integration/setup-liff-auto-login-member-binding/
tags:
  - LINE
  - Quick_Login
  - Phone_Number
  - Member_Data
  - Third_Party_Integration
  - LIFF
  - LINE_OA
  - Certification
acoiv: ""
apis:
  - LINE Login API
  - LINE LIFF
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=6674
  - https://www.cyberbiz.io/support/?p=35740
comments: false
search:
  exclude: false
icon: lucide/phone-forwarded
hide: []
---

![LINE Quick Login Phone Number](../../../../assets/images/ec-第三方整合-line login-oc-phone-number.en.png){ title="LINE Quick Login Phone Number" .hero-page }

## What Is Member Phone Number Retrieval in LINE Quick Login? { #intro-line-phone-login }

**Member Phone Number Retrieval in LINE Quick Login** is an advanced feature that helps merchants obtain phone number authorization when customers sign in with LINE, so they can create or update storefront member profiles.

The following sections explain the feature in detail and provide setup steps:

## Prerequisites { #prerequisites-line-phone-login }

Merchants must meet all three of the following conditions to use this feature:

- [x] [**Complete LINE Quick Login Integration**](setup-line-quick-login.md){ title="Set Up LINE Quick Login" }: Basic LINE login setup is already complete in the storefront admin.

- [x] **LINE Provider Certification**: Your LINE Provider must be certified as a **LINE Certified Provider**.

	- If you do not yet have LINE Certified Provider status, contact your [LINE partner :lucide-external-link:](https://tw.linebiz.com/partner/sales-partner/), or see the [application instructions](https://drive.google.com/file/d/1oSF07fHFdx_s4gXVhDv0zw81Su3usQKY/view?usp=sharing).
	-  Note: Under LINE policy, only companies, trading firms, and business entities can apply for certification. Individuals, farms, and foundations cannot apply.

- [x] **LINE Official Account Verification**: Your LINE Official Account must have a **blue shield (Verified Account)** or a **green shield (Premium Account)**.
	- Learn about [LINE account tier differences :lucide-external-link:](https://tw.linebiz.com/column/lac-verified/).
	- See [LINE verified official account application process :lucide-external-link:](https://tw.linebiz.com/column/line-lac-id-0418/).

## Verify Eligibility in LINE Developers { #intro-line-phone-login-line-backend }

Log in to [LINE Developers :lucide-external-link:](https://developers.line.biz/) and check the following:

1. **Check Provider Status**: On the Provider home page, check whether a certification badge (green checkmark) appears next to the item.

	![LINE OA Verification Badge](../../../../assets/images/ec-第三方整合-line oa 認證盾牌.en.png){ title="LINE OA Verification Badge" }

2. **Check Permission Settings**:

	- Click the **LINE Login Channel** integrated to your storefront.

	- Go to the **Basic Settings** tab and scroll down to **Permissions**.

	- Confirm that the permissions list includes **OC_PHONE_NUMBER**.

	![LINE Login Permission Settings](../../../../assets/images/ec-第三方整合-line-login-permissions.en.png){ title="LINE Login Permission Settings" }

## System Matching Logic and Scenarios { #specs-line-phone-login }

Standard LINE quick login matches accounts only by the member's email address. When this feature is turned on, the system's logic changes as follows:

- **Matching order**: The system **first matches by phone number**. If there is no match, it matches by email.

- **Applies to**: This feature applies to members whose phone numbers are or are not already registered on the storefront.


??? note-clean "Logic Flow Diagram"

    This diagram shows the order of priority the system uses:**Mobile Number (Priority 1) > Email (Priority 2) > Create New Account**.

    ```mermaid
    graph LR
        Start([User starts LINE Quick Login]) --> CheckPhone{EC Does the system have<br/>Same mobile number?}

        %% Case A
        CheckPhone -- Yes (Member A) --> BindA[Bind LINE UID to Member A]
        BindA --> EndA([Future login as Member A])

        %% Case B
        CheckPhone -- No --> CheckEmail{EC Does the system have<br/>Same Email?}

        CheckEmail -- Yes (Member B) --> BindB[Bind LINE UID to Member B]
        BindB --> EndB([Future login as Member B])

        CheckEmail -- No --> CreateNew[Create new Member C]
        CreateNew --> EndC([Future login as new Member C])
    ```

??? example "Scenario A: Phone Number Already Exists in the EC System"

	When the phone number on the LINE account matches the phone number of **Member A** in the EC system:

	|**Trigger Scenario**|**LINE Account Email Status**|**System Action (UID Binding)**|**Future Login Status**|**Notes**|
	|---|---|---|---|---|
	|**Scenario 1**|Registered in EC and belongs to **Member A** |Link the LINE UID to **Member A**|Same as **Member A** login|The ideal, fully matched state.|
	|**Scenario 2**|Registered in EC but belongs to **another person**|Link the LINE UID to **Member A**|Same as **Member A** login|**Does not access** the LINE email. Matches by phone number.|
	|**Scenario 3**|Not registered in EC|Link the LINE UID to **Member A**|Same as **Member A** login|**Does not access** the LINE email.|

??? example "Scenario B: Phone Number Does Not Exist in the EC System"

	When the phone number on the LINE account has not yet been registered in the EC system:

	|**Trigger Scenario**|**LINE Account Email Status**|**System Action (UID Binding)**|**Future Login Status**|**Notes**|
	|---|---|---|---|---|
	|**Scenario 1**|Registered in EC (belongs to **Member B**)|Link the LINE UID to **Member B**|Same as **Member B** login| **Does not access** the LINE phone number. Matches by email.|
	|**Scenario 2**|Not registered in EC|**Create new Member C**|Same as **new Member C** login|Accesses the LINE email, phone number, and UID at the same time to create a new record.|


## Use with LIFF Apps { #intro-line-phone-login-liff }

[:lucide-tag:{ title="Applicable plans" }](../../../resources/conventions#適用方案) | PLUS / Enterprise
{ .doc-badge }

If you have LINE Certified Provider status, you can also use the **LIFF** feature to collect phone number information:

1. Go to the [LINE Developers console :lucide-external-link:](https://developers.line.biz/).
2. Go to the corresponding channel and switch to the **LIFF** tab.

	![LIFF Tab](../../../../assets/images/ec-第三方整合-line developer-liff tab.en.png){ title="LIFF Tab" }

3. In the **Scopes** section, select the **phone** option.

	![LIFF Scopes Settings](../../../../assets/images/ec-第三方整合-line login-liff-scope.en.png){ title="LIFF Scopes Settings" }

4. **Actual effect after setup:**

	- **Customer side:** When a member clicks the LIFF link, the authorization screen shows an additional "Request phone number" item.

	- **Merchant side:** The system automatically retrieves the phone number linked to the member's LINE account, enabling a fast flow with **automatic login and synced storefront member binding**.

!!! info "For complete LIFF setup instructions, see [How to Set Up LIFF Auto-Login](setup-liff-auto-login-member-binding.md){ title="Set Up LIFF Auto-Login and Member Binding" }."

## Important Notes { #intro-line-phone-login-overview-line-phone-login }

- **Non-retroactive**: This feature **does not include** phone numbers for members who completed LINE quick login before the feature was set up.

- **Verification notice**: If the merchant has turned on "Verify phone number during registration" in customer registration settings, the system sends an SMS verification code to help verify the account.

- **Masked display**: When printing order details, if the merchant has enabled security settings, retrieved phone numbers appear masked (for example, `093******3`) to protect personal data.


## FAQ { #faq-line-phone-login }

??? quote "How does the system handle a phone number on LINE that does not match the storefront record?"
	The system follows a **"phone number first"** policy. If the phone number provided by LINE already exists in the system (Member A), it is always linked to Member A, regardless of the email. If the number has no record and the email is also unregistered, the user is treated as a new customer and a new record is created.

??? quote "After the feature is turned on, will existing LINE login members automatically have their phone numbers filled in?"
	**No.** This feature is not retroactive. After the feature is enabled, the system can only retrieve the current phone number through the API when the member authorizes login again.

??? quote "Why doesn't the LINE Developers console show the `OC_PHONE_NUMBER` option?"
	This permission has a hard requirement: your Provider must have **LINE Certified Provider** status (shown by a green checkmark badge). If you do not meet this requirement, the permission field does not appear in the management console.

??? quote "Will login fail if a customer declines phone number authorization?"
	**No.** The login flow still completes. However, because the system cannot retrieve the phone number, it automatically falls back to the standard mode, which matches accounts by email only.

??? quote "Does using this feature incur additional fees?"
	The feature itself is free. However, if the merchant has turned on the "Verify phone number during registration" setting, the system sends a verification SMS when creating a new member account.

