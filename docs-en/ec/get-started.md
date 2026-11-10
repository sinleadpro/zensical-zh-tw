---
title: "Quick Start Guide for New Stores"
description: "A guided tour of initial CYBERBIZ site setup and core features to help merchants get their store ready quickly."
last_modified: 2026-07-22 17:33
lang: en-US
permalink: "https://help.cyberbiz.io/ec/get-started/"
wp_url:
  - https://www.cyberbiz.io/helpcenter/?page_id=3610
  - https://www.cyberbiz.io/helpcenter/?page_id=1933
  - https://www.cyberbiz.io/support/?page_id=17972
  - https://www.cyberbiz.io/support/?page_id=29441 
type: guide
author: Jase
reviewers: []
notes: []
products:
  - EC
modules:
  - 管理中心
  - 金物流
  - 商品
  - 網站外觀
  - 行銷活動
  - 第三方整合
  - 訂單
  - 會員
  - 訊息推播
  - 分析報表
  - 分潤
sites:
  - TW
audiences:
  - merchant
difficulty: beginner
tnb: trunk
plans: []
plan_options: []
devices:
  - desktop
paths: []
intents:
  - 快速開店
  - 系統初步設定
features: []
prerequisites: []
related:
  - ec/website-management/setup-store-basic-info/
  - ec/notifications/manage-email-templates/
  - ec/website-management/domain-management/
  - ec/payments-and-logistics/payments/
  - ec/payments-and-logistics/
  - ec/payments-and-logistics/payments/order-settings/
  - ec/payments-and-logistics/setup-home-delivery-non-cod-custom-logistics/
  - ec/payments-and-logistics/setup-cvs-c2c-shipping/
  - ec/payments-and-logistics/setup-cvs-b2c-bulk-shipping/
  - ec/payments-and-logistics/home-delivery-cash-on-delivery/
  - ec/orders/tcat-quick-store/tcat-express-payment-settings/
  - ec/products/create-and-manage/create-update-products/
  - ec/products/bulk-operations/excel-import-products/
  - ec/products/shipping/cvs-shipping-restrictions-exclusions/
  - ec/products/categories-and-tags/custom-collections/
  - ec/products/categories-and-tags/smart-collections/
  - ec/website-appearance/theme-and-layout/apply-and-switch-theme/
  - ec/website-appearance/navigation/setup-menus-navigation/
  - ec/website-appearance/customer-interaction/setup-edit-customer-service-info/
  - ec/website-management/seo/submit-sitemap-to-gsc/
  - ec/website-appearance/pages-and-content/blog-management-publishing-guide/
  - ec/marketing/discounts/storewide-discounts/
  - ec/marketing/coupon/setup-coupons/
  - ec/marketing/bonus-and-gifts/setup-bonus-points/
  - ec/marketing/bonus-and-gifts/setup-birthday-gift/
  - ec/marketing/bonus-and-gifts/setup-registration-gift/
  - ec/members/vip/setup-store-wide-vip-system/
  - ec/integrations/fb/
  - ec/integrations/google/
  - ec/integrations/line/
  - ec/integrations/setup-shop-com/
  - ec/orders/basics/order-fulfillment-flow/
  - ec/orders/basics/search-filter-orders/
  - ec/orders/basics/order-management-interface/
  - ec/payments-and-logistics/setup-print-tcat-waybill-v2/
  - ec/orders/basics/cancel-order/
  - ec/orders/order-settings/manual-order-close/
  - ec/orders/order-return-process/
  - ec/orders/order-refund-process/
  - ec/orders/returns-refunds/cvs-unclaimed-order/
  - ec/orders/returns-refunds/overdue-return-handling/
  - ec/members/member-customer-service-system/
  - ec/notifications/send-sms-notifications-v2/
  - ec/notifications/send-edm-newsletters-v2/
  - ec/business-intelligence/
  - ec/marketing/one-page-store/one-page-store/
  - ec/marketing/other-tools/subscription-campaign-page/
  - ec/profit-sharing/referrer-profit-sharing/
  - ec/profit-sharing/registrant-profit-sharing/
tags:
  - "Store setup guide"
  - "Beginner tutorial"
  - "Quick setup"
icon: lucide/rocket
hide:
search:
  exclude: false
---

This guide walks you from basic info, domain setup, payments and shipping, product listing, and site design through marketing, third-party integrations, and order management so you can finish initial CYBERBIZ EC setup quickly.

<!-- For video tutorials, go to [Video Tutorials Overview](../resources/video-tutorials.md){ title="Video Tutorials Overview" }. While you use CYBERBIZ services, CYBERBIZ provides a customer-only login that unlocks some paid courses for free. -->

## Initial Setup { #operate-get-started }

### Step 1: Set Basic Information { #operate-get-started-basic }

- Admin center > General settings: fill in "[Company contact info](../ec/website-management/setup-store-basic-info.md#operate-general-preferences-company-info)」
- Admin center > Site permissions / plan: set Invoice type and Admin list
- Message push > [Email notification templates](../ec/notifications/manage-email-templates.md) to let other admins receive emails such as new-order notices

<div class="grid cards" markdown>

- :lucide-store:{ .lg } [__Site profile settings__](website-management/setup-store-basic-info.md){ title="Set basic site information" }

</div>

!!! tip "Invoice reminder"
    When you top up or renew in the admin, invoices are emailed using your selected invoice type.

---

### Step 2: Domain and SSL Certificate { #operate-get-started-domain }

- Admin center > Domains: confirm the primary domain
- The free domain from CYBERBIZ `_____.cyberbiz.co` already includes SSL—no extra install needed
- To use another domain name, register it on [Gandi](https://www.gandi.net/zh-Hant)、[GoDaddy](https://tw.godaddy.com/)
- After DNS points correctly, the system installs an SSL certificate within 24 hours

<div class="grid cards" markdown>

- :lucide-globe:{ .lg } [__Domain setup guide__](website-management/domain-management.md){ title="Domain management" }

</div>

---

### Step 3: Set up Payments { #operate-get-started-payments }

Payments & logistics > Checkout & shipping settings

<div class="grid cards" markdown>

- :lucide-credit-card:{ .lg } [__Payment settings guide__](payments-and-logistics/payments/index.md){ title="Checkout and shipping settings overview" }
<!-- - :lucide-wallet:{ .lg } [__Payment method amount limits__](payments-and-logistics/index.md){ title="Payments" } -->
<!-- - :lucide-coins:{ .lg } [__Store-wide minimum order amount__](payments-and-logistics/payments/order-settings.md){ title="Order-related settings" } -->

</div>

!!! tip "What are payments?"
    Payments are the ways you collect money from shoppers—credit card, virtual ATM, convenience-store code pay, LINE Pay, JKOPay, and more. Choose which methods to offer.

---

### Step 4: Set up Shipping { #operate-get-started-logistics }

- Payments & logistics > Home delivery: set home-delivery shipping rules
- Payments & logistics > Convenience-store shipping: set convenience-store pickup

<div class="grid cards" markdown>

- :lucide-truck:{ .lg } [__How to set shipping fees__](payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md){ title="Create home delivery without cash on delivery / custom shipping" }
- :lucide-store:{ .lg } [__Convenience-store C2C shipping setup__](payments-and-logistics/setup-cvs-c2c-shipping.md){ title="Set up convenience-store C2C shipping" }
- :lucide-warehouse:{ .lg } [__Convenience-store B2C bulk shipping setup__](payments-and-logistics/setup-cvs-b2c-bulk-shipping.md){ title="Set up convenience-store B2C bulk shipping" }
- :lucide-banknote:{ .lg } [__Tcat / Pelican cash-on-delivery setup__](payments-and-logistics/home-delivery-cash-on-delivery.md){ title="Home-delivery COD (Tcat / Pelican / HCT)" }
- :lucide-truck:{ .lg } [__Tcat home-to-store COD setup__](orders/tcat-quick-store/tcat-express-payment-settings.md){ title="Set up Tcat quick store-pickup payment" }
- :lucide-settings-2:{ .lg } [__Home delivery without COD (custom shipping)__](payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md){ title="Create home delivery without cash on delivery / custom shipping" }

</div>

!!! tip "What is shipping?"
    Shipping is how you deliver goods to shoppers—home delivery, convenience-store pickup, and more. Choose carriers such as Tcat, Pelican, 7-11, and FamilyMart.

---

### Step 5: Create Products { #operate-get-started-products }

- Products > All products: add your products
- Marketing: set promotions for specific products
- or use custom product categories and conditional product categories (often used in homepage link lists)

<div class="grid cards" markdown>

- :lucide-package:{ .lg } [__List products one by one__](products/create-and-manage/create-update-products.md){ title="Create and update products" }
- :lucide-file-spreadsheet:{ .lg } [__Bulk list products__](products/bulk-operations/excel-import-products.md){ title="Import products in bulk with Excel" }
- :lucide-ruler:{ .lg } [__Convenience-store size limits and shipping exclusions__](products/shipping/cvs-shipping-restrictions-exclusions.md){ title="Set convenience-store shipping limits and exclusions" }
- :lucide-folder-tree:{ .lg } [__Custom product categories__](products/categories-and-tags/custom-collections.md){ title="Set custom product category groups" }
- :lucide-list-filter:{ .lg } [__Conditional product categories__](products/categories-and-tags/smart-collections.md){ title="Set conditional product category groups" }

</div>

!!! tip "Pair with marketing"
    Many product-specific promotions—pick-any discounts, add-ons, spend gifts, buy-X-get-Y, bonus boosts, purchase limits, Bonus Mall、first-purchase gift, and more—are set under Marketing. Design campaigns that fit your products.

---

### Step 6: Website Appearance and Content { #operate-get-started-appearance }

- Website appearance > Theme editor: choose a site design
- Website appearance > Theme editor > Site settings: edit homepage images and text
- Website appearance > CSS/HTML editor: edit code (optional)
- For top homepage menu links, go to Website appearance > Menu / navigation settings

<div class="grid cards" markdown>

- :lucide-palette:{ .lg } [__Apply or change a theme__](website-appearance/theme-and-layout/apply-and-switch-theme.md){ title="Apply and change site themes" }
- :lucide-menu:{ .lg } [__Top homepage menu links (link lists)__](website-appearance/navigation/setup-menus-navigation.md){ title="Set menus and navigation" }
- :lucide-map-pin:{ .lg } [__Add a Google Map in the site footer__](website-appearance/customer-interaction/setup-edit-customer-service-info.md){ title="Set and edit customer service info" }
- :material-sitemap:{ .lg } [__Set up a sitemap for more discovery__](website-management/seo/submit-sitemap-to-gsc.md){ title="Submit your sitemap to Google Search Console" }
- :lucide-file-text:{ .lg } [__Edit blog posts__](website-appearance/pages-and-content/blog-management-publishing-guide.md){ title="Blog management and publishing guide" }

</div>

!!! tip "Value-added service needs"
    For creative assets or custom site code, CYBERBIZ can match you with partner vendors—ask your store consultant.

---

### Step 7: Set Store-Wide Marketing { #operate-get-started-marketing }

- Marketing > [store-wide discount-Bonus & coupon] set store-wide campaigns (discounts / coupons / member bonus points, and more)
- Payments & logistics > Home-delivery shipping fees: set store-wide free shipping
- Members > VIP settings: set member VIP offers

<div class="grid cards" markdown>

- :lucide-percent:{ .lg } [__Set store-wide discount__](marketing/discounts/storewide-discounts.md){ title="Setstore-wide discount" }
<!-- - :lucide-truck:{ .lg } [__Set store-wide free shipping__](payments-and-logistics/setup-home-delivery-non-cod-custom-logistics.md){ title="Create home delivery without cash on delivery / custom shipping" } -->
- :lucide-ticket:{ .lg } [__Set store-wide gift coupon__](marketing/coupon/setup-coupons.md){ title="Setcoupon" }
- :lucide-gift:{ .lg } [__Set store-wide gift member bonus__](marketing/bonus-and-gifts/setup-bonus-points.md){ title="Setbonus points" }
- :lucide-cake:{ .lg } [__Set birthday gift bonus points__](marketing/bonus-and-gifts/setup-birthday-gift.md){ title="Setbirthday gift" }
- :lucide-user-plus:{ .lg } [__Set registration gift bonus points__](marketing/bonus-and-gifts/setup-registration-gift.md){ title="Setregistration gift" }
- :lucide-crown:{ .lg } [__Member VIP program setup__](members/vip/setup-store-wide-vip-system.md){ title="Create a store-wide VIP program" }

</div>

---

### Step 8: Integrate Third-Party Services { #operate-get-started-integrations }

Integrations: choose what to set up:

<div class="grid cards" markdown>

- :lucide-share-2:{ .lg } [__Facebook settings__](integrations/fb/index.md){ title="Facebook overview" }
- :simple-google:{ .lg } [__Google settings__](integrations/google/index.md){ title="Google integrations" }
- :lucide-message-circle:{ .lg } [__LINE settings__](integrations/line/index.md){ title="LINE integrations overview" }
- :lucide-shopping-bag:{ .lg } [__Shop.com (Meian) settings__](integrations/setup-shop-com.md){ title="Connect the Shop.com channel" }

</div>

!!! tip "Initial setup complete"
    Through Step 8 you finished initial site setup. Steps 9–13 cover features you will use often after go-live—keep reading below.

## Advanced Setup { #operate-get-started-advanced }

### Step 9: Learn the Order Workflow { #operate-get-started-orders }

Orders: review orders and run fulfillment and return flows here:

<div class="grid cards" markdown>

- :lucide-truck:{ .lg } [__Single / batch order fulfillment__](orders/basics/order-fulfillment-flow.md){ title="Order fulfillment flow" }
- :lucide-help-circle:{ .lg } [__Fulfillment methods and FAQ__](orders/basics/order-fulfillment-flow.md){ title="Order fulfillment flow" }
- :lucide-search:{ .lg } [__Search and filter orders__](orders/basics/search-filter-orders.md){ title="How to search and filter orders" }
- :lucide-clipboard-list:{ .lg } [__Single order page overview__](orders/basics/order-management-interface.md){ title="Order management interface" }
- :lucide-printer:{ .lg } [__Reprint shipping labels__](payments-and-logistics/setup-print-tcat-waybill-v2.md){ title="Set up and reprint Tcat shipping labels" }
- :lucide-x-circle:{ .lg } [__Cancel orders__](orders/basics/cancel-order.md){ title="How to cancel an order" }
- :lucide-check-circle:{ .lg } [__Close orders__](orders/order-settings/manual-order-close.md){ title="How to close an order manually" }
- :lucide-undo-2:{ .lg } [__Standard return and refund flow__](orders/order-return-process.md){ title="Order return and refund flow" }
- :lucide-rotate-ccw:{ .lg } [__Refund methods and operations__](orders/order-refund-process.md){ title="Refund methods and operations" }
- :lucide-truck:{ .lg } [__Request carrier pickup for returns (Tcat / Pelican)__](orders/order-return-process.md){ title="Order return flow" }
- :lucide-clock-alert:{ .lg } [__Overdue convenience-store pickup returns__](orders/returns-refunds/cvs-unclaimed-order.md){ title="Handle overdue convenience-store pickup orders" }
- :lucide-calendar-x:{ .lg } [__Returns past your return-request deadline__](orders/returns-refunds/overdue-return-handling.md){ title="Handle orders past the return deadline" }

</div>

---

### Step 10: Learn Customer Q&A { #operate-get-started-cs }

Members > All support questions: messages from Contact us and order comments land here so you can reply and manage them.

<div class="grid cards" markdown>

- :lucide-headset:{ .lg } [__Customer Q&A feature guide__](members/member-customer-service-system.md){ title="Member support system" }

</div>

---

### Step 11: Learn EDM and SMS Messaging { #operate-get-started-push }

Go to Message push > Send SMS and Send EDM to notify customers about promotions, important reminders, and more.

<div class="grid cards" markdown>

- :lucide-smartphone:{ .lg } [__SMS sending setup__](notifications/send-sms-notifications-v2.md){ title="Set up and send SMS notifications" }
- :lucide-mail:{ .lg } [__EDM sending setup__](notifications/send-edm-newsletters-v2.md){ title="Set up and send EDM newsletters" }

</div>

---

### Step 12: Learn Analytics Reports { #operate-get-started-reports }

Open Reports and analytics to understand store performance by metric:

<div class="grid cards" markdown>

- :lucide-chart-no-axes-column:{ .lg } [__Operations charts guide__](business-intelligence/index.md){ title="Reports and analytics" }

</div>

### Step 13: Other Special Features { #operate-get-started-other }

- Marketing > One-page store: create quick purchase links for selected products

<div class="grid cards" markdown>

- :lucide-shopping-bag:{ .lg } [__One-page store setup__](marketing/one-page-store/one-page-store.md){ title="One-page store" }

</div>

- Marketing > Subscription campaign pages: let shoppers buy on a recurring subscription

<div class="grid cards" markdown>

- :lucide-repeat:{ .lg } [__Subscription campaign setup__](marketing/other-tools/subscription-campaign-page.md){ title="Subscription campaign pages" }

</div>

- Profit sharing: set plans with partners, employees, and customers

<div class="grid cards" markdown>

- :lucide-share-2:{ .lg } [__Referral profit sharing – partners__](profit-sharing/referrer-profit-sharing.md){ title="Referrer profit sharing" }
- :lucide-user-check:{ .lg } [__Referral profit sharing – employees__](profit-sharing/referrer-profit-sharing.md){ title="Referrer profit sharing" }
- :lucide-users:{ .lg } [__Referral profit sharing – customers__](profit-sharing/referrer-profit-sharing.md){ title="Referrer profit sharing" }
- :lucide-user-plus:{ .lg } [__Signup profit sharing – employees__](profit-sharing/registrant-profit-sharing.md){ title="Signup profit sharing" }

</div>

!!! tip "Profit sharing use cases"
    When you work with influencers or group-buy leaders, create unique links and discount codes; partners can check performance and earnings with a password. You can also reward members or staff with bonuses or bonus points for orders they help create.
