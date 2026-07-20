---
title: 批次匯入 / 編輯會員
description: 透過 Excel 檔案，您可以快速完成大量會員的資料建立或內容異動，包含聯絡資訊、紅利點數初始化及行銷標籤管理。
created: 2026-02-11 00:00
last_modified: 2026-06-30 12:30
lang: zh-TW
type: tutorial
status: ""
version: 1.1.1
author: Ann
reviewers: []
notes: []
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
difficulty: intermediate
tnb: trunk
plans:
  - 企業
  - 專業
  - 進階
  - 高手
cyb_extensions: []
intents:
  - 大量導入新會員
  - 批次更新會員資料
  - 整理會員行銷標籤
features:
  - 會員匯入
  - 批次修改
  - Excel範本
prerequisites:
  - [[需準備 Excel 軟體或支援 .xlsx 之工具]]
related: []
tags:
  - Excel匯入
  - 批次操作
acoiv: activate
apis: []
devices:
  - desktop
ui_components: []
paths:
  - 會員 > 所有會員
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=264
  - https://www.cyberbiz.io/helpcenter/?p=6879
  - https://www.cyberbiz.io/support/?p=24549
  - https://www.cyberbiz.io/support/?p=36678
permalink: https://help.cyberbiz.io/ec/members/batch-import-and-edit-members
comments: false
search:
  exclude: false
icon: lucide/user-plus
hide: []
---

# Times import/ Edit Membership

With Excel files, You can quickly Create or Value a large number of Membership data, Contains Contact information, Bonus Points initialization, and marketing Tags management.
{ .subtitle }


![](../../assets/images/EC-Backend- Membership- All Customers- Times Import and Edit Membership Screen Overview){ .hero-page }

!!! tip &quot;Application Context&quot;
    - **System Migration**: During the initial stage of opening the store, the Membership list of the old platform will be migrated to CYBERBIZ in one go.
    - **Data Completion**: For Membership with missing Address 1 or Birthday , times Export in batches and then re- Upload after the missing information is completed.



## Instructions for Use

Before performing a large number of import or Update Operation, please be sure to understand the less limitations and guidelines:

**Testing Recommendation:** Times Delete is not possible after data is imported. Before performing large-scale Operation, please test with 3-5 orders to Enter the correct format.
**Formatting Guidelines:** Please do not change the Value or order of the Mon row Vip collection title in the Excel template, otherwise the Import Failed.
- **Field Limitation**:
    - ** Bonus Points **: Only applicable when adding Create Membership . Existing Membership who need to adjust their bonuses must Update manually on their individual Membership Edit pages.
    - ** Password :** It is recommended to Setting a default Value based on the Membership needs to avoid overly simple passwords that could pose a security risk.


## Operation procedures

### Task Mon: Inject a large number of New Members

This is suitable for Create new lists that do not yet exist in the system.

1. Login in to the management backend and goto shop to** Membership&gt; All Customers**.
2. Click **Import Membership ** in the upper right corner of the Pages .
3. In the pop-up window, point(s)** Download Customer_Import_Sample**.
4. Fill in the information according to the template format, and Delete the preset &quot;Zhang Xiaomei&quot; example column.
5. Point(S)** Select File** to Upload the completed file, and press ** Enter** to execute.

    The system sent in execute the import schedule in the background and send an Email notification of the result upon completion.

![](../../assets/images/EC-Backend- Membership- All Customers- Membership)

### Task Tues.: Times Update of existing Membership information

This tool is suitable for Update Membership information already in the system (such as: adding Birthday, Update Phone Number, Update Tags).

1. Goto shop to** Membership&gt; All Customers ** and filter for the Membership you want to Update .

    === &quot;Use Membership Filter&quot;

          1. Click ** Create Filter Rules**.
          2. Select the Specify conditions as needed.
          3. The system will automatically filter and show the list of Membership who meet the criteria in the List below.
          4. Click:lucide-square: **0 Membership Selected ** to select 所有 Membership who meet the criteria.

          ![](../../assets/images/EC - Backend- Membership- All Customers- Membership )
    
    === &quot;Manually select&quot;

          1. **Select Specify Membership **: Directly select Specify Membership from the List .
          2. **Select All Customers **: Click:lucide-square: **0 Membership Selected **, **Select All Membership**.

          ![](../../assets/images/EC-Backend- Membership- All Customers - Export )


2. Click ** Export** and Agree to the data protection terms.

      The file will be sent to your Login Account Email.

3. Open Excel to Edit the data.
    - ** Update fields**: Name, Email Address, Phone Number, Birthday, Gender, Remark, Tags, Company, Phone Number, Address 1, Whether to Accept Newsletters, Allow CVS Pickup.
4. Return to the backend ** Membership&gt; All Customers**, and click ** Times Update customer information Information**.
    ![](../../assets/images/EC-Backend- Membership- All Customers- Times Update customer information)
5. Upload the Edit file and press ** Enter**.

     The system will compare the data with either an ** Email** or a ** Phone Number ** and then overwrite the existing data. An Email notification will be Send Updated successfully! or Fail .



## Excel Core Column Explanation

Please ensure that the less key fields are filled in correctly:

| Field Name| Formatting Requirements | Explanation |
| :--- | :--- | :--- |
| ** Name** | Text | Membership&#39;s Show Name |
| ** Email Address Email** | Text (Email) | The system identifies the Membership&#39;s main index; the format must Contains`@` and the domain name.
| ** Phone Number** | Number | The system identifies the Membership&#39;s main index. For Overseas, please add the country code, such as Hong Kong: +85261234567 |
| ** Birthday** | Date Range(YYYY/MM/DD) | Gregorian calendar only, e.g., `1990/01/01` |
| ** Remaining Bonus Points ** | Positive Integer | **Valid Only for Import New Member Data ** |
| ** Tags** | Text (comma-separated) | A single Membership can be tagged with multiple Tags, for example: `VIP, Physical (Once you want to add more than one POS store, Potential Customer` |
| ** Bonus of Birthday Gift** | Yes/ No | Birthday gifts for Marketing Campaign are Bonus . VIP Birthday gifts are not eligible. |

For adding Orders from Other Channels(manage-member-profiles/#2- Orders from Other Channels ), please Select the appropriate Operation Method according to your system Plan :

=== &quot;Enterprise&quot;

      Please switch to the **Orders from Other Channels** tab and enter the relevant information.
      ![](../../assets/images/EXCEL范本-Membership进入范本-Other频道页条-Enterprise01.png)

=== &quot;Other Plan&quot;
      Please enter the information directly in the ** Price accumulated from other distributions** and ** Spending accumulated since** fields.
      ![](../../assets/images/EXCEL范本-Membership进口入范本-一般版01.png)

!!! info &quot; Plan compatible with the Birthday gift feature &quot;
    This feature is only available in the Plus and Enterprise; other Plan none this field.

## Website building and integration

###  Phone Number and Email are Required Setting

If you set ** Email** and ** Phone Number** as ** Required ** in[Member Registration Setting-flow-and-fields/#Step- Setting Default Field Attributes), then both will need to be filled in when importing data.

- ** Phone Number Field Setting**:
    - ** Boss and Advance**: These are required fields by can&#39;t be blank with cannot be changed.
    - **Other Plan:** Support Store to Setting required or optional fields themselves.

### Marketing Campaign

If you plan to Send** Bonus Points, Coupon , or Birthday gifts** when Membership join, **it is recommended to complete the website setup and Activate first.**

A well-designed shopping environment ensures that Membership are successfully directed to the site to place orders after To notifications; if the website is not yet ready, it may lead to disappointment and wasted Flow, affecting their willingness to repurchase in the future.



## Frequently Asked Questions

Will times data Update result in duplicate Account Create ?
    No. The system will Use** Email Address Email** and ** Phone Number** as the primary comparison Fulfillment ID. If the Email or Phone Number existed!! , the information will be Update .

How do I Login in to a new Account that has received a large influx of data via Excel without a default Password ?
    If a new Account was Not set with a Password Hour import, please point(s)**Forgot Password ** Membership sent in Login . The system will then guide Membership through initializing Password. Once Setting , you can Login in Issue .
