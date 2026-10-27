---
title: "Set Product Purchase Limits"
description: "Limit how many units of a specific product each member can buy. Use it for limited-edition items, to prevent stockpiling, and to make sure more customers can get best-sellers."
created: 2026-06-08 14:19
last_modified: 2026-07-22 15:48
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
  - Marketing
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: branch
plans:
  - Advanced
  - Expert
  - "Professional PLUS"
  - "Advanced PLUS"
  - "Expert PLUS"
  - Enterprise
cyb_extensions: []
intents:
  - 設定商品購買上限
  - 建立限購群組
  - 防止商品囤貨
features:
  - 限購群組
  - 購買頻率限制
  - 最低購買數量
prerequisites: []
related:
  - ec/marketing/references/purchase-limit-account-status.en/
  - ec/marketing/upsells/setup-product-upsell.en/
tags:
  - EC
  - 行銷活動
  - "Purchase Limit"
  - "Limited-Edition Products"
  - "Inventory Management"
acoiv: operation
apis: []
devices:
  - desktop
  - mobile
ui_components:
  - 限購群組設定
paths:
  - 行銷活動 > 商品限購數量設定
layouts: []
wp_url:
  - https://www.cyberbiz.io/helpcenter/?p=6451
  - https://www.cyberbiz.io/support/?p=3354
permalink: "https://help.cyberbiz.io/ec/marketing/purchase-restrictions/purchase-limit.en/"
comments: false
search:
  exclude: false
icon: lucide/package-minus
hide: []
---

![Limited Purchase Setting](../../../assets/images/ec-行銷活動-商品限購數量-hero.png){ .hero-page }

## About Product Purchase Limits

Limited Purchase Setting lets you put products into purchase-limit Collections and set a purchase cap for each of the Collections. When customers check out on the storefront or at POS,
the system checks quantities against the Collections rules and blocks checkout if the cap is exceeded. Customers **must log in** to buy limited products, which stops one person from placing many repeat orders.

!!! info "Tip"
    Purchase limits are checked **at checkout**, not when items are added to the cart. A member's past completed orders also count (within the period set by "Frequency").

---

## Requirements And Limits { #prerequisites-purchase-limit }

- [x] **Plan activation**: Limited Purchase Setting appears in the admin menu only after it's activated. Some plans don't include it by default, so contact support to check.
- [x] **Login required**: Customers must log in to buy limited products. Guests can't check out.

Some advanced features depend on your plan:

??? plan "Features by Plan"
    | Feature | Description | Availability |
    | :-- | :-- | :-- |
    | Create purchase-limit Collections and set limits | Core feature of Limited Purchase Setting in the admin | Advanced plan and above |
    | Show limits on the storefront | Show a "Limit N per order" notice on the product and checkout pages | Higher plans such as Enterprise |
    | Minimum purchase quantity | Set the minimum quantity of a product per order | Higher plans such as Enterprise |

    If you're not sure what your plan includes, contact support.

---

## Steps { #operate-purchase-limit }

> !!! path "Admin path: Marketing Limited Purchase Setting."

### Create Collections And Add Products { #operate-purchase-limit-create }

1. **Create a collection:** On the Limited Purchase Setting page, enter a Collections Name in the field below the Collections list (Collections), then click **Add a new collection**.
2. **Add products:** Expand the collection (Collections), click the option to add products, find the product in the search list, and click **Add** on its row.
3. **Confirm:** In the **Add to Collections** window, click **Confirm**[^1].
4. **Remove products:** To remove a product from the Collections, click **Remove** in the search list, or click the remove icon in the Collections product list.

![Add Purchase-Limit Collections](../../../assets/images/ec-行銷活動-商品限購數量-新增群組.png)

??? tip "Use Filters to Find Products"
      In the product search window, use the keyword field at the top (search by **Name** or **SKU**), or click **Filter Options** to narrow results by **custom category**, **smart category**, **product tag**, **Vendor**, **Type**, or **publish status**. Then select products and add them to the Collections at once. To reset filters, click **Clear Options**.

      ![Filter Products](../../../assets/images/ec-行銷活動-商品限購數量-篩選商品.png)

[^1]: Each product can belong to only one set of purchase-limit Collections. If a product is already in other Collections, it moves from the original Collections to the current Collections after you confirm.

---

### Set Limit Rules { #operate-purchase-limit-rules }

Set these fields in the Collections edit section. Changes take effect right away:

1. **Frequency:** Choose the period for counting purchases: **Permanent**, **Monthly**, **Yearly**, or **Per Order**.
2. **Calculation:** Choose **By Collections Products** or **By Individual Product** to set whether products in the Collections share one cap or each have their own.
3. **Maximum Quantity:** Enter the purchase cap. Leave it blank for **no limit**[^2].
4. **Minimum Quantity:** Set the minimum quantity of the product per order. You can only fill this in when Frequency is **Per Order** and Calculation is **By Individual Product**, and your plan must include this feature.

![Set Limit Rules](../../../assets/images/ec-行銷活動-商品限購數量-設定限購條件.png)

[^2]: The admin field hint reads "If maximum quantity is empty, there is no limit."

---

### Manage Collections { #operate-purchase-limit-manage }

1. **Edit Collections:** Click the **Collections Name** in the Collections list to expand its settings. You can change the Name, limit rules, and **Bulk Reorder** products in the Collections.
2. **Show or hide:** Click :lucide-eye: to switch the visibility of the Collections. The status shows "This Collections is currently public" or "This Collections is currently hidden"[^3].

    ![Set Visibility](../../../assets/images/ec-行銷活動-商品限購數量-設定群組公開狀態.png)

3. **Delete Collections:** Click **:lucide-x: Delete This Collections**, then confirm "Are you sure you want to delete Collections" to delete it.

    ![Delete Collections](../../../assets/images/ec-行銷活動-商品限購數量-刪除群組.png)

4. **Sort Collections:** Use the sort menu to order the Collections list by Collections Name or creation date.

    ![Sort Collections](../../../assets/images/ec-行銷活動-商品限購數量-排序群組.png)

[^3]: When Collections are hidden or deleted, their limit rules stop working immediately. If you later add the same product to new Collections, the new Collections rules apply.

## Storefront Display <Small>Customer View</small>

Once purchase limits are on, the system checks Collections rules when customers place an order. If the quantity exceeds the cap or the account status doesn't qualify (such as not logged in, not activated, or disabled), checkout is blocked with a message such as "These products: '…
  ' can only be purchased up to N…". For how account status is checked, see [Account Status and Purchase Permissions](../references/purchase-limit-account-status.md){ title="帳號狀態與購買權限對照表" }. This check applies to all frequencies (Permanent, Monthly, Yearly, Per Order).

<div class="grid cards" markdown>

-   ![Over-Limit Message](../../../assets/images/ec-行銷活動-商品限購數量-前台-超過數量.png){ title="超過數量提示" }

    __Over-Limit Message__

-   ![Login Required Message](../../../assets/images/ec-行銷活動-商品限購數量-前台-非會員.png){ title="未登入提示" }

    __Login Required Message__

</div>

??? plan "Storefront Limit Notices and Cart Alerts"
    Showing "Limit N per order" on the product and checkout pages, and showing a cart alert ("Product '…' has reached the purchase limit. The quantity will be adjusted automatically.") with automatic correction, is an **Enterprise** feature. It only applies to Collections with **Per Order** frequency. Other plans still block over-limit orders at checkout, but don't show limits on the storefront or alert in the cart.

## Key Rules And Limits { #specs-purchase-limit }

!!! note "Purchase Limit Key Points"
    * **One group per product**: A product can be in only **one** set of purchase-limit Collections. Adding it again moves it to the new Collections.
    * **Collections limit**: Each Shop can create up to **30** purchase-limit Collections. When you reach the limit, delete unused Collections first.
    * **Login required**: Guests can't buy limited products. The storefront asks them to log in first.
    * **Past orders count**: Limits include the member's "completed" orders within the period, not just the current cart.

!!! tip "Common Setups"
    * **Limited item, 2 per person**: Frequency = Permanent, Calculation = By Individual Product, Maximum Quantity = 2.
    * **Whole series, 5 per month in total**: Add the series to the same Collections, Frequency = Monthly, Calculation = By Collections Products, Maximum Quantity = 5.
    * **At least 3 and at most 10 of each item per order**: Frequency = Per Order, Calculation = By Individual Product, Minimum Quantity = 3, Maximum Quantity = 10.

---

## Next Steps

<div class="grid cards" markdown>

- :lucide-circle-plus:{ .lg }
  [__Set Up Product Upsells__](../upsells/setup-product-upsell.md)
  Besides limiting purchases, you can set up upsells that recommend related add-ons at checkout to raise order value.

</div>

---

## FAQ { #faq-purchase-limit }

??? quote "Customers can't check out and see "You must log in to purchase""
    [](){ #faq-purchase-limit-login-required }
    This is expected. Limited products always require a member login, so guests are asked to log in first. Remind customers to log in or sign up before checking out.

??? quote "Can a product be in more than one set of purchase-limit Collections?"
    [](){ #faq-purchase-limit-single-group }
    No. Each product can belong to only one set of purchase-limit Collections. If you add a product that's in other Collections to new Collections, it moves to the new Collections after you confirm, and the new Collections rules apply.

??? quote "When do monthly and yearly limits reset?"
    [](){ #faq-purchase-limit-reset-cycle }
    They follow the calendar, not the date the Collections were created.

    - **Monthly**: Resets on the 1st of each month.
    - **Yearly**: Resets on January 1 each year.

??? quote "I set a purchase limit, but the product and checkout pages don't show it"
    [](){ #faq-purchase-limit-no-frontend-hint }
    The limit still applies at checkout, but showing limits on the storefront is only available on higher plans. To show a "Limit N" notice on the product and checkout pages, contact support about your plan.

??? quote "I can't fill in "Minimum Quantity""
    [](){ #faq-purchase-limit-min-count-disabled }
    "Minimum Quantity" can only be set when Frequency is **Per Order** and Calculation is **By Individual Product**, and your plan must include this feature. The admin field hint reads "This feature is only for per-order / individual product use."

??? quote "How many sets of purchase-limit Collections can I create?"
    [](){ #faq-purchase-limit-max-groups }
    Each Shop can create up to 30 purchase-limit Collections. If you reach the limit, delete unused Collections before adding more.

---

## References { #reference-purchase-limit }

- [Account Status and Purchase Permissions](../references/purchase-limit-account-status.md){ title="帳號狀態與購買權限對照表" }


