---
title: "Set up Dual Email and Mobile Verification for Customers"
description: "Require new customers to pass both email and SMS verification when they register. This keeps member data genuine and lowers the risk of empty accounts and malicious sign-ups."
created: 2026-05-27 14:58
last_modified: 2026-09-29 15:30
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
  - "Website Management"
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 設定 Email 驗證
  - 設定手機驗證
  - 啟用雙重驗證
  - 管理顧客註冊欄位
features:
  - "Email Verification"
  - 手機 OTP 驗證
  - "Dual Verification"
  - 資料欄位設定
  - 顧客驗證方式
  - 快速結帳並註冊
  - 必須註冊
prerequisites: []
related:
  - ec/website-management/references/customer-field-validation-reference/
  - ec/website-management/references/customer-registration-modes-reference/
  - ec/notifications/manage-email-templates/
  - ec/notifications/manage-sms-templates-v2/
  - ec/website-management/customer-registration-flow-and-fields/
  - ec/members/manage-member-profiles/
tags:
  - 雙重驗證
  - Email 驗證
  - "Mobile Verification"
  - "Customer Verification"
  - "Member Registration"
  - "CYBER Coins"
  - "SMS Verification"
  - "Account Security"
  - OTP
  - 管理中心
  - "Customer Registration Settings"
acoiv: configure
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 驗證開關
  - 資料欄位設定
  - 必選填設定
paths:
  - 管理中心 > 顧客註冊設定
  - 訊息推播 > Email通知樣板 
  - 訊息推播 > 簡訊通知樣板 
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=1865
  - https://www.cyberbiz.io/helpcenter/?p=1871
permalink: "https://help.cyberbiz.io/ec/website-management/setup-customer-email-phone-verification/"
comments: false
search:
  exclude: false
icon: lucide/shield-user
hide: []
---


![Member Registration Setting](../../assets/images/EC-管理中心-顧客註冊設定-hero.en.png){ title="Member Registration Setting" .hero-page }

## About Customer Registration Verification { #intro-customer-verification }

The customer verification setting decides if new customers must verify who they are by email and SMS when they sign up or check out. Each of the two checks has its own switch. You can turn on either one, or turn on both for dual verification:

* **Email Verification**: The system sends an account activation email. The customer clicks the link in it to activate the account.
* **Mobile Verification**: The system sends a 4-digit SMS verification code, and the customer must enter it correctly to activate the account.

!!! info "Tip"
    Verification settings only apply to **newly registered customers**. Existing members are not forced to verify again.

## Requirements and Limits { #prerequisites-customer-verification }

- [x] **The field must be required first**: If the email or mobile field is optional, its verification switch is locked. First go to the **Member Field Setting** section on the same page and set the field to **Required**.
- [x] **Mobile verification incurs SMS charges**: See [Pricing](#specs-customer-verification-pricing).
- [x] **At least one field must be required**: Email or mobile must be required. The system doesn't allow both to be optional.

!!! plan "Plans and Activation"
    * **Mobile verification (customer mobile verification)**: Built into most plans and activated by default for new stores.
    * **New field settings**: The new **Member Field Setting** and customer verification interface only appear on the **Enterprise plan**.

## Pricing { #specs-customer-verification-pricing }

* **Email Verification**: Free.
* You can customize both the SMS and email templates under **Push Notifications** > **Email / SMS Notification Template** > **Customers** > **Customer Account Activation Reminder**.

## Steps { #operate-customer-verification }

### Open the Settings Page { #operate-customer-verification-entry }

In the admin panel, go to **Website Management** > **Member Registration Setting**.

The settings page has three main sections. The steps below focus on the last two (Member Field Setting and customer verification).

---

### Step 1: Set the Fields to Required { #operate-customer-verification-set-required }

1. In the **Member Field Setting** section, find the two default fields, **Email** and **Mobile**.
2. Set the fields to **Required**.
3. The system saves automatically.

=== "Standard / PLUS Plans"

    In the **Member registration field setting** list, select the **Compulsory** checkbox for the field.

    ![Member registration field setting](../../assets/images/EC-管理中心-顧客註冊設定-顧客註冊欄位設定.en.png){ title="Member Registration Field Setting" }

    ??? warning "If You Can't Make the Mobile Field Required"
        This means your store doesn't have **customer mobile verification** activated. In this case, the mobile field can only stay optional, and **you can only set up email verification**. Skip the mobile steps below, or ask Customer Service if mobile verification can be turned on for you.

=== "Enterprise Plan"

    1. In the **Member Field Setting** section, click the **edit icon** on the right of the field row.
    2. In the **Edit Field** window that opens, set **Required/Optional Setting** to **Required**.
    3. Click **Confirm** to save.

    ![Member field setting](../../assets/images/EC-管理中心-顧客註冊設定-資料欄位設定.en.png){ title="Member Field Setting" }

!!! note "Note"
    If both fields are optional, a message appears at the top of the customer verification section: "The email or mobile field must be required to enable verification." The switches below then turn gray and can't be clicked.


---

### Step 2: Turn on the Verification Switches { #operate-customer-verification-enable-switch }

[:lucide-tag:{ title="Applicable Plans" }](../../../resources/conventions#適用方案) | Enterprise
{ doc-badge }


1. Find the **Member Verification Setting** section.
2. Turn the switches **on** as needed:
    * **Email Verification**: When this is on, customers who register receive an account activation email to verify their account.
    * **Mobile Verification**: When this is on, customers who register receive an account activation SMS to verify their account[^1].
3. (Mobile verification only) You can select **Mobile verification while registration**[^2].

Turning a switch on puts that field in the **Required and must be verified** state. See the [field validation mode reference](references/customer-field-validation-reference.md){ title="Customer Field Validation Mode Reference" data-preview }.

![Customer verification](../../assets/images/EC-管理中心-顧客註冊設定-顧客驗證方式.en.png){ title="Customer Verification" }

[^1]: Turning on mobile verification also turns on the **Customer requests verification code notification** SMS template. Sending SMS costs CYBER coins, based on message length.
[^2]: By default, customers first register an account and then complete mobile verification on the member page. When you select this option, customers enter the verification code directly on the registration page and must pass it to finish registering.

---

### Step 3: Check the Customer Experience { #operate-customer-verification-frontend }

After you turn on dual verification, the steps for customers depend on the **Member Registration** section at the top of the same page. It is set to either **Fast checkout with registration** or **Registration required**. For a comparison of the two modes, see the [registration mode reference](references/customer-registration-modes-reference.md){ title="Customer Registration Mode Reference" data-preview }.

![Customer registration](../../assets/images/EC-管理中心-顧客註冊設定-顧客註冊.en.png){ title="Customer Registration" }

=== "Fast Checkout with Registration"
    * **Customers who are not logged in**: They pass email and mobile verification on the **cart checkout page**. Then they can submit the order.
    * **Logged in but not verified**: The system shows "You need to verify your account before you can check out" and takes the customer to the member page to verify. They can continue checkout after verifying.

=== "Registration Required"
    Customers must register and verify before they can shop. The flow is:

    1. The customer fills in the registration page and submits it → the system creates the account with the status **Not activated**.
    2. The customer is taken to the member page automatically, which shows:
        * "Your email is not verified yet. Check your inbox and activate your account."
        * "Your mobile number is not verified yet. Check your SMS and activate your account."
    3. **Verify the mobile number**:
        * Click **Click here to send a verification SMS**.
        * Enter the 4-digit SMS verification code and click **Submit**.
        * The system shows "**Congratulations, your mobile number has been verified!**"
    4. **Verify the email**:
        * Open the account activation email in your inbox.
        * Click the **Activate Account** link in the email.
        * The system takes the customer back to the member page, and the field shows as verified.
    5. Customers can only check out after both verifications are complete. If they try to check out before that, they are stopped with the message "**You need to verify your account before you can check out**".

    !!! tip "Tip"
        If **Mobile verification while registration** is selected, customers enter the mobile code right on the registration page. So they skip the mobile check on the member page in step 3.

## Important Rules and Limits { #specs-customer-verification }

### Verification Email and SMS Notification Switches { #specs-customer-verification-notify }

After you turn on email verification, make sure the switch for **Push Notifications > Email Notification Template > 顧客相關 > 顧客請求發送驗證碼** stays on. Don't turn it off.

If you turn on mobile verification, also make sure **Push Notifications > 簡訊通知樣板 > 顧客相關 > 顧客請求發送驗證碼通知** stays on so that verification SMS messages can be sent.

![Verification notification switches](../../assets/images/EC-後台-訊息推播-Email通知樣板-驗證碼通知信件開關01.en.png){ title="Verification Notification Switches" }

---

### Existing Members Are Not Affected { #specs-customer-verification-existing-members }

The verification switches only affect **newly registered** customers. Existing members never have to verify again, whatever their status. They log in and shop just as before.

---

### Special Handling for Members Added by Excel Import { #specs-customer-verification-import }

When both email verification and mobile verification are on, new customers added through Excel import are handled as follows:

* **Only the email activation message is sent.** The system doesn't send an SMS verification code automatically.
* After the customer clicks the email activation link, the email is verified, but **the mobile number stays unverified**.
* After logging in for the first time, the customer must go to the member page and click **Click here to send a verification SMS** to verify the mobile number.

!!! info "Why It Works This Way"
    This prevents large SMS charges by accident when you import many members.

---

### Third-Party Login <small>(FB / LINE / Google)</small> { #specs-customer-verification-sso }

| Login platform | Email verification | Mobile verification |
|:--|:--|:--|
| LINE | Treated as verified automatically | **Treated as verified automatically** (no OTP needed) |
| Facebook | Treated as verified automatically | Still needs separate verification |
| Google | Treated as verified automatically | Still needs separate verification |

Because a LINE account is already linked to a mobile number, the system skips OTP SMS verification for LINE logins. After customers register with Facebook or Google, the system asks them to add a mobile number and click **Send verification SMS** to verify it.

## Next Steps { #next-steps-customer-verification }

<div class="grid cards" markdown>

- :lucide-mail:{ .lg }
  [__Customize the Activation Email__](../notifications/manage-email-templates.md){ title="Set Up and Manage Email Notification Templates" } ·[__Customize the SMS__](../notifications/manage-sms-templates-v2.md){ title="Set Up and Manage SMS Notification Templates" }
  Edit them under **Push Notifications > Email / SMS Notification Template > Customers > Customer Account Activation Reminder**.

- :lucide-user-cog:{ .lg }
  [__Manage Customer Registration Fields__](customer-registration-flow-and-fields.md){ title="Customer Registration Flow and Fields" }
  Add custom fields, change required fields, and choose whether fields appear on the registration page and member page.

- :lucide-shield-check:{ .lg }
  [__View Member Verification Status__](../members/manage-member-profiles.md){ title="Manage Member Profiles" }
  See each member's email and mobile verification status in the customer list.

</div>

## FAQ { #faq-customer-verification }

??? quote "What if a customer says they didn't receive the verification SMS?"
    [](){ #faq-customer-verification-sms-not-received }
    Possible reasons:

    * The phone number is set to reject business SMS messages.
    * The mobile number was entered incorrectly.
    * SMS service is not available in that region (some international country codes may not be supported).

    Ask the customer to check that the number is correct, and then click **Click here to send a verification SMS** again on the member page.

??? quote "Can I require new customers to verify only their email and not their mobile number?"
    [](){ #faq-customer-verification-email-only }
    Yes. The email verification and mobile verification switches are **independent**, so you can combine them any way you like:

    * Email verification only (free, good for stores that don't need mobile numbers)
    * Mobile verification only (costs CYBER coins)
    * Dual email and mobile verification (the strictest)

??? quote "Will an Excel import of many members send lots of SMS messages?"
    [](){ #faq-customer-verification-bulk-import-sms }
    No. By design, when new customers are added by Excel import, **only the email activation message is sent**, even if mobile verification is on. No SMS verification code is sent automatically. Customers start mobile verification themselves on the member page after their first login.

??? quote "If a customer logged in with LINE, do they still need to verify their mobile number?"
    [](){ #faq-customer-verification-line-login }
    No. For customers who log in with LINE, the system treats their mobile number as verified and skips the OTP step. Customers who register with other third-party logins (Facebook or Google) still need to add and verify a mobile number.

??? quote "Why is the verification switch grayed out?"
    [](){ #faq-customer-verification-disabled-switch }
    The verification switch can only be turned on when the field is required. First go to the **Member Field Setting** section and change **Required/Optional Setting** for email or mobile to **Required**. The verification switch then unlocks.

??? quote "How are the setup steps different on the Standard and Enterprise plans?"
    [](){ #faq-customer-verification-edition-diff }

    The main difference is the **Member Field Setting** interface:

    - **Standard / PLUS plans**: Select the **Compulsory** checkbox directly in the **Member registration field setting** list.
    - **Enterprise plan**: Click the field's edit icon, change **Required/Optional Setting** to **Required** in the window that opens, and click **Confirm**.

    The underlying logic is the same in both: you must make email or mobile required before you can turn on the verification switch.

??? quote "What difference does selecting Mobile Verification While Registration make?"
    [](){ #faq-customer-verification-verify-at-registration }

    This option controls when customers verify their mobile number:

    - **Not selected (default)**: Customers first register an account, and then click **Click here to send a verification SMS** on the member page to verify.
    - **Selected**: Customers enter the SMS verification code directly on the registration page and must pass it to finish registering.

    Selecting it reduces the steps for customers, but adds a verification step to the registration flow.

## References { #reference-customer-verification }

- [Customer Registration Mode Reference](references/customer-registration-modes-reference.md){ title="Customer Registration Mode Reference" }
- [Customer Field Validation Mode Reference](references/customer-field-validation-reference.md){ title="Customer Field Validation Mode Reference" }

