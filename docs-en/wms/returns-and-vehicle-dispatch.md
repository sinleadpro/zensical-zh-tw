---
title: "Returns and Vehicle Dispatch"
description: "Learn how returns work between the CYBERBIZ e-commerce warehouse system (WMS) and the EC admin panel, including reverse logistics dispatch, return inspection, unclaimed convenience store parcels, and automatic refunds."
created: 2026-03-31 13:40
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
  - 訂單管理
  - "Return Management"
sites:
  - TW
audiences:
  - merchant
difficulty: intermediate
tnb: ""
plans: []
plan_options: []
cyb_extensions: []
intents:
  - 如何處理倉儲退貨
  - WMS逆物流派車流程
  - 超商逾期未取退回倉庫處理
  - 7-11_C2B逆物流設定
  - 黑貓逆物流退貨地址
features:
  - 逆物流整合
  - 自動退貨單生成
  - 入庫驗收作業
  - 逾期未取自動退款
prerequisites:
  - 帳號管理與角色指派
related:
  - wms/merchant-self-inspection-of-returns/
  - ec/orders/member-return-request-feature/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
  - ec/payments-and-logistics/setup-pelican-waybill-v2/
  - ec/payments-and-logistics/setup-hct-waybill-v2/
  - ec/orders/returns-refunds/cvs-c2b-return/
  - ec/orders/order-refund-process/
  - ec/members/member-customer-service-system/
tags:
  - 退貨管理
  - "Reverse Logistics"
  - "Warehouse Integration"
  - WMS
  - "Vehicle Dispatch"
acoiv: configure
apis: []
devices:
  - desktop
ui_components:
  - 退貨申請功能
  - 宅配逆物流
  - 7-11 C2B
  - 退貨驗收
paths:
  - 訂單管理 > 退貨/退款 > 建立逆物流
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/wms/returns-and-vehicle-dispatch/"
comments: false
search:
  exclude: false
icon: ""
hide: []
---

# Returns and Vehicle Dispatch
Learn how returns work between the CYBERBIZ e-commerce warehouse system (WMS) and the EC admin panel, including reverse logistics dispatch, return inspection, unclaimed convenience store parcels, and automatic refunds.
{ .subtitle }

[:lucide-layers:{ title="Applicable Products" }](../../resources/conventions#適用產品) | Online Store / Smart Warehousing
{ .doc-badge }

## Before You Start { #prerequisites-return-dispatch }


- **Special needs**: Products shipped from the warehouse are returned to the warehouse by default. If you want returns of warehouse-shipped products sent straight to your address for inspection, see [Inspect Returns Yourself](merchant-self-inspection-of-returns.md).



!!! tip "How the Systems Work Together"
    - **EC admin panel**: Controls the front-end process, including **receiving customer requests**, **creating reverse logistics numbers**, and the final **refund**.
    - **WMS system**: Handles the physical work, including receiving return information, creating warehouse return orders, and **inspecting and restocking the goods**.

## Return Handling { #operate-return-dispatch }

### Step 1: Customer Return Request { #operate-return-dispatch-request }

The process depends on whether you turned on [returns on the storefront](../ec/orders/member-return-request-feature.md):

=== "Storefront Returns On"

    - **Process**: The customer requests a return in **我的帳戶 > 訂單查詢** on your online store.
    - **Status change**: The EC order's **return status** changes to **Return Requested** automatically.
    - **Benefit**: Less work for customer service, because the system collects the request details.

=== "Storefront Returns Off"

    - **Process**: The customer contacts you through [order customer service chat](../ec/members/member-customer-service-system/#intro-member-cs-order).
    - **Status change**: After you confirm the reason, you handle it manually in the EC admin panel.
    - **Benefit**: You can screen return reasons first and cut unnecessary return costs.


### Step 2: Reverse Logistics Pickup { #operate-return-dispatch-reverse-logistics }

Choose how to handle the return based on whether the items need to be collected:

=== "Items Need to Be Collected"

    === "Flowchart"

        ```mermaid
            sequenceDiagram

            autonumber

            participant 商家
            participant EC
            participant WMS

            商家 ->> EC: 建立逆物流
            EC ->> WMS: 建立退貨單
            note right of EC: 逆物流派車向消費者收取退貨包裹
            note right of EC: 退貨包裹送至倉庫
            note right of WMS: 進行退貨審查
            WMS ->> EC: 更新退貨結果
            商家 ->> EC: 執行退款
        ```

    === "Detailed Steps"

        1. **Create reverse logistics**: In the EC admin panel, choose the reverse logistics type that applies.

            !!! info "Choose Reverse Logistics"
                Choose the reverse logistics option based on your system type and shipping method:

                | System Type | Full Integration | Partial Integration | Partial Integration | Partial Integration |
                | ------- | ------- | -------- | ------- | ------- |
                | Order Shipping Method | Warehouse shipping | Warehouse shipping | Mixed (self-shipping + warehouse shipping) | Self-shipping |
                | Available Reverse Logistics | T-Cat | T-Cat | T-Cat | T-Cat |
                | | Pelican | Pelican | Pelican | Pelican |
                | | 7-ELEVEN C2B | 7-ELEVEN C2B | | |
                | Return Delivery Address | Warehouse address | Warehouse address | Merchant company address | Merchant company address |

            - Create home delivery reverse logistics: [T-Cat](../ec/payments-and-logistics/setup-print-tcat-waybill-v2/#operate-ezcat-shipping-reverse), [Pelican](../ec/payments-and-logistics/setup-pelican-waybill-v2/#operate-pelican-shipping-reverse), [HCT Logistics](../ec/payments-and-logistics/setup-hct-waybill-v2/#operate-hct-setup-reverse)
            - Create [7-ELEVEN C2B reverse logistics](../ec/orders/returns-refunds/cvs-c2b-return.md)

        2. **Status change**: The order's **return status** changes to **Returning** automatically.
        3. **System sync**: The online store syncs the information to WMS, which creates a **Return Order** and gets a **Tracking Number**.
        4. **Pickup**: The reverse logistics driver collects the parcel at the address (or convenience store) the customer chose.
        5. **Warehouse inspection**: After the warehouse receives the parcel, staff inspect the goods and restock them in WMS.





=== "Items Not Collected (No Dispatch)"

    === "Flowchart"

        ```mermaid
            sequenceDiagram

            autonumber

            participant 商家
            participant EC
            participant WMS

            商家 ->> WMS: 直接向倉儲客服回報訂單編號、退貨數量
            WMS ->> WMS: 產生退貨單
            WMS ->> EC: 更新訂單退貨狀態
            商家 ->> EC: 執行退款
        ```

    === "Detailed Steps"

        Use this for fresh food, damaged or defective items, or when you agree with the customer not to collect the items.

        1. **Report in the group**: Post a screenshot of the order in your chat group with the warehouse, noting "not collected" and the return quantity.
        2. **Do not**: **Do not create any reverse logistics in the EC admin panel**, or the system may dispatch a vehicle twice.
        3. **Manual return order**: Warehouse staff run **EC return without dispatch** in WMS to create the return order manually.
            ![](../assets/images/WMS-操作人員後台-執行EC訂單不派車退貨01.en.png){ .screenshot }
        4. **Linked status**: The EC order's **return status** changes to **Partially Returned**.



### Step 3: Refund the Order { #operate-return-dispatch-refund }

After the warehouse finishes inspection, refund based on the inspection result:

| Inspection Result | Warehouse Return Order Status | EC Order Return Status | Recommended Action |
| :--- | :--- | :--- | :--- |
| **All items returned** | Accepted | Returned | [Refund the order](../ec/orders/order-refund-process.md) |
| **Some items returned** | Partially Accepted | Partially Returned | [Refund the order](../ec/orders/order-refund-process.md) |



## Unclaimed Convenience Store Parcels { #operate-return-dispatch-unclaimed }

For convenience store parcels that are not picked up, the system returns them automatically:

1. **Automatic status updates**:
    - The EC order's **delivery status** changes to **Not Picked Up**.
    - The **return status** changes to **At Transit Center**.
2. **Return order created**: WMS creates the matching return order automatically.
3. **Parcel back to the warehouse**: The convenience store carrier returns the parcel to the warehouse, and staff check and restock it.
4. **Refunds**: Check the order's [refund method](../ec/orders/order-refund-process.md) based on your store's payment provider and the payment method used.

    === "Automatic Refund "

        - The system sends a refund request to the payment provider right away.
        - After the refund succeeds, the **payment status** changes to **Refunded** automatically.

    === "Manual Refund"

        - Contact the member to get their bank account details.
        - The system first changes the **payment status** to **Awaiting Refund**.
        - Processing takes about 7–10 days. The status then changes to **Refunded**.



