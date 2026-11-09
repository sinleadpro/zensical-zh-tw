---
title: Glossary
description: "Definitions of CYBERBIZ system terms across product management, orders and logistics, marketing analytics, and platform plans. Each entry includes an English gloss and links to related docs."
lang: en-US
icon: lucide/book-marked
last_modified: 2026-07-15 13:30
type: reference
author: Jase
reviewers: []
notes: []
tags:
  - EC
  - POS
  - WMS
  - SEO
  - GA4
  - Glossary
  - Glossary
  - "System terms"
permalink: "https://help.cyberbiz.io/resources/glossary/"
plan_options: []
---
<!-- [PDF :lucide-download:](#){ .md-button .md-button--primary } -->

## Products

### Product Information

All product settings and content in the system—basics, images, videos, and variant management—used for storefront display, selling, and marketing.

- **See also**: [Manage products in the product management interface](../ec/products/create-and-manage/product-management-interface.md){ title="Manage products in the product management interface" }

### Product Name

A required field when creating a product. It identifies and shows the main title on product pages, order details, campaigns, and reports.

- **See also**: [Create and update products](../ec/products/create-and-manage/create-update-products.md){ title="Create and update products" }

### Product Slogan

Short text on the product page that quickly communicates selling points or campaign messages.

- **See also**: [Edit product short description and slogan](../ec/products/create-and-manage/edit-product-slogan-and-description.md){ title="Edit product short description and slogan" }

### Product Short Description

Blurb on the product page that introduces key points, features, or highlights so shoppers quickly understand the product.

- **See also**: [Edit product short description and slogan](../ec/products/create-and-manage/edit-product-slogan-and-description.md){ title="Edit product short description and slogan" }

### Product Page

Storefront page for one product’s details—name, price, images, specs, stock, shipping options, and buy button.

- **See also**: [Edit product description and settings](../ec/products/create-and-manage/edit-product-description-settings.md){ title="Edit product description and settings" }

### Product URL

Dedicated URL for the product page, used for storefront access and search indexing.

### Product Link

System-generated unique URL that opens the storefront product page for promotion, sharing, or quick access from other systems.

### Image Host

External service that stores and serves image URLs so you can embed images on sites, docs, or systems.

### Preorder Products

When stock hits zero, set Out-of-stock handling to Continue selling so orders keep coming—preorder behavior without a separate product type.

- **See also**: [Create and update products](../ec/products/create-and-manage/create-update-products.md#setup-preorder-products){ title="Preorder product settings" }

## Product Structure and Specs

### Bundles

A product type made of two or more child products sold as one item with its own bundle price.

- **See also**: [Create and configure bundles](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="Create and configure bundles" }

### Child Products

Single products that make up a bundle. They have their own list price but are not sold alone inside the bundle.

- **See also**: [Bundles](#Bundles) | [Create and configure bundles](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="Create and configure bundles" }

### Fixed Bundles

Bundles with a fixed set of items chosen by the merchant; shoppers cannot swap items.

- **See also**: [Bundles](#Bundles) | [Create and configure bundles](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="Create and configure bundles" }

### Pick-Any Bundles

Bundles where the merchant sets an allowed range and shoppers pick child products and quantities.

- **See also**: [Bundles](#Bundles) | [Create and configure bundles](../ec/products/create-and-manage/create-and-setup-combo-products.md){ title="Create and configure bundles" }

### Pick-Any Total Quantity

Total number of child products a shopper must select in a pick-any bundle.

- **See also**: [Pick-any bundles](#Pick-any-bundles)

### Bundle Price Difference

Price discount a child product gets by being sold in a bundle.

- **See also**: [Bundles](#Bundles)

### Add-on Price

Extra price to buy a designated add-on when the shopper purchases a qualifying trigger product.

### Options

Attribute labels that distinguish product traits such as color, size, capacity, or material.

- **See also**: [Set product swatches and variant images](../ec/products/create-and-manage/product-swatches-variant-images-default.md){ title="Set product swatches and variant images (default theme)" }

### Option Values

Concrete values shoppers can choose under an option.

- **See also**: [Options](#Options)

### Variants

A sellable unit formed by combining option values.

- **See also**: [Set product swatches and variant images](../ec/products/create-and-manage/product-swatches-variant-images-default.md){ title="Set product swatches and variant images (default theme)" }

### Product Channel

Attribute that defines fulfillment source. When one product ships from different warehouses, stores, or suppliers, this setting separates those sources.

- **See also**: [Set product shipping conditions](../ec/products/shipping/setup-product-shipping-conditions.md){ title="Set product shipping conditions (shipping, temperature zone and fulfillment channels)" }

### Product Channel Settings

Defines the actual fulfillment source or sales channel for a product.

- **See also**: [Product channel](#Product-channel)

### Related Product Groups

Merchants manually relate products by attributes or strategy to improve discovery and sales.

- **See also**: [Create and update products](../ec/products/create-and-manage/create-update-products.md#operate-product-edit-settings){ title="Related product group settings" } | [Product page settings](../ec/website-appearance/theme-and-layout/setup-theme-page-settings.md#相關商品){ title="Set related product display" }

### Google Product Category

Google product taxonomy used in the Google Merchant Center product feed.

- **See also**: [GMC](#gmc)

### SKU

**Stock Keeping Unit**, a unique code that identifies a product for inventory tracking, product data, and sales stats.

## Orders, Payments, and Shipping

### Credit Card One-Time Payment

When a shopper pays by card, the full amount is captured in one billing cycle.

### 3D Secure

**3D Secure**, extra identity verification for online card payments. Cardholders confirm with an SMS OTP or bank page at checkout to reduce fraud.

- **See also**: [OTP](#otp)

### OTP

**One-Time Password**, a temporary code from the system or bank for online payment or identity checks. It works once and expires quickly.

- **See also**: [3D Secure](#3D-Secure)

### COD

**Cash on Delivery**, pay when the goods arrive—common with home delivery and couriers.

### Shipping Conditions

Attribute set that drives fulfillment and shipping-fee rules (such as temperature zone, shipping method, and fulfillment channel). It affects order splitting and shipping flow.

- **See also**: [Set product shipping conditions](../ec/products/shipping/setup-product-shipping-conditions.md){ title="Set product shipping conditions (shipping, temperature zone and fulfillment channels)" }

### Shipping Condition Binding

Set a product to Allow or Only allow specific carriers, shipping temperature zone or fulfillment channels.

- **See also**: [Shipping conditions](#Shipping-conditions) | [Set product shipping conditions](../ec/products/shipping/setup-product-shipping-conditions.md){ title="Set product shipping conditions (shipping, temperature zone and fulfillment channels)" }

### Shipping Temperature Zonesettings

Defines which shipping temperature zone types a product can use.

- **See also**: [Shipping conditions](#Shipping-conditions)

### Shipping Fee Settings

Defines available carriers and their shipping-fee rules.

### Outbound Logistics

Moving goods from the merchant or warehouse to the customer—the normal fulfillment flow.

- **See also**: [Reverse logistics](#Reverse-logistics) | [Order fulfillment flow](../ec/orders/basics/order-fulfillment-flow.md){ title="Order fulfillment flow" }

### Reverse Logistics

Moving goods from the customer back to the merchant or warehouse—returns, exchanges, repairs, and similar.

- **See also**: [Outbound logistics](#Outbound-logistics) | [Order return flow](../ec/orders/order-return-process.md){ title="Order return flow" }

### Return Window

Longest period the merchant allows for return requests, counted from delivery.

- **See also**: [Handle orders past the return deadline](../ec/orders/returns-refunds/overdue-return-handling.md){ title="Handle orders past the return deadline" }

### Pickup Service

Carrier sends a driver to a merchant location to collect parcels for fulfillment.

### Bulk Drop-off

Seller skips the convenience-store counter and drops a full batch of parcels at the convenience-store logistics hub.

- **See also**: [Ship with convenience-store B2C bulk drop-off](../ec/orders/cvs-shipping/cvs-b2c-bulk-shipping.md){ title="Ship with convenience-store B2C bulk drop-off" }

### WMS

**Warehouse Management System**, software that manages and optimizes warehouse operations—inbound, outbound, inventory, picking, and shipping.

- **See also**: [Warehouse connection](#Warehouse-connection)

### Warehouse Connection

Operating model that connects the ecommerce platform (EC) with a WMS so orders sync automatically for picking and shipping.

- **See also**: [WMS](#wms)

### POS

**Point of Sale**, in-store sales system for checkout, payment, and receipts, while syncing sales data, inventory changes, and revenue.

## Marketing and Growth

### Coupon

Account-bound (member-only) marketing tool. The system assigns vouchers to specific member accounts for discounts, free shipping, or gifts.

- **See also**: [Coupons](#Coupons)

### Coupons

Enterable discount codes used as non-account-bound marketing tools for discounts, free shipping, or gifts.

- **See also**: [coupon](#coupon)

### EDM

**Electronic Direct Mail**, permission-based marketing email with rich layout and performance tracking sent to a selected audience.

- **See also**: [Set up and send EDM newsletters](../ec/notifications/send-edm-newsletters-v2.md){ title="Set up and send EDM newsletters" }

### SEO

**Search Engine Optimization**, improving a site’s visibility and ranking in search engines.

### GA

**Google Analytics**, Google’s web analytics tool for tracking user behavior and engagement.

- **See also**: [GA4](#ga4)

### GA4

**Google Analytics 4**, the latest Google Analytics with an event-based model, stronger cross-platform analysis, and privacy controls.

- **See also**: [GA](#ga)

### GSC

**Google Search Console**, Google’s free site tool for search performance, index status, and SEO diagnostics.

- **See also**: [SEO](#seo)

### GMC

**Google Merchant Center**, Google’s product-data platform for storing, validating, and submitting catalog data so products appear across Google services.

- **See also**: [Google product category](#Google-product-category)

### MBE

**Meta Business Extension**, Meta merchant integration that connects Facebook Conversions API, Pixel, product catalog, Instagram Shopping, Facebook Pages, and more in one flow.

### FBE

**Facebook Business Extension**, the former name of MBE.

- **See also**: [MBE](#mbe)

### Profit Sharing

After a sale, the platform or merchant shares revenue with partners or stakeholders by a preset rate.

- **See also**: [About profit sharing](../ec/profit-sharing/index.md){ title="About profit sharing" }

### CTR

**Click-Through Rate**, share of people who see a link and click through to the site.

### SERP

**Search Engine Results Page**, the list of results after a user searches a keyword.

- **See also**: [SEO](#seo) | [GSC](#gsc)

### OG Image

**Open Graph Image**, the preview image social platforms fetch when a page link is shared, used to attract attention and clicks.

### LAP

**LINE Ads Platform**, LINE’s performance ad platform.

- **See also**: [LINE OA](#line-oa)

### GTM

**Google Tag Manager**, free tag manager for deploying and updating marketing tags without changing site source code.

- **See also**: [GA4](#ga4)

### CPA

**Cost Per Action**, ad efficiency metric calculated as total ad spend ÷ conversions.

### UTM

**Urchin Tracking Module**, tracking parameters appended to a URL to analyze entry path and source.

### ROAS

**Return on Ad Spend**, metric of ad efficiency; higher values mean better performance.

### LINE OA

**LINE Official Account**, a brand account on LINE for customer chat, marketing messages, and support.

- **See also**: [LAP](#lap)

### LIFF

**LINE Front-end Framework**, framework for web apps that run inside the LINE app.

- **See also**: [LINE OA](#line-oa)

## Platform, Plans, and Other

### Standard Plans

Professional, Expert, and Advanced plan versions.

- **See also**: [PLUS plans](#PLUS-plans)

### PLUS Plans

**PLUS Plan**—Professional, Advanced PLUS, and Expert PLUS.

- **See also**: [Standard plans](#Standard-plans)

### PLUS and Above

**PLUS Plan and above**—Professional PLUS, Advanced PLUS, Expert PLUS, Enterprise, and higher.

- **See also**: [PLUS plans](#PLUS-plans) | [Expert and above](#Expert-and-above)

### Expert and Above

Expert, Professional PLUS, Advanced PLUS, Expert PLUS, Enterprise, and higher.

- **See also**: [PLUS plans](#PLUS-plans) | [Advanced and above](#Advanced-and-above)

### Advanced and Above

Includes Advanced, Expert, Professional PLUS, Advanced PLUS, Expert PLUS, and Enterprise.

- **See also**: [Standard plans](#Standard-plans) | [PLUS plans](#PLUS-plans) | [Expert and above](#Expert-and-above)

### CYBER Coin

**CYBER COIN**, virtual billing points in CYBERBIZ used for payment/shipping service fees and certain system features.

### EC

**E-commerce**, selling products or services online—including display, transactions, payment, and fulfillment—as a full system and operating model.

### B2C

**Business to Consumer**, merchants selling products or services directly to end customers.

- **See also**: [C2C](#c2c) | [EC](#ec)

### C2C

**Consumer to Consumer**, shoppers trading products or services with each other.

- **See also**: [B2C](#b2c) | [EC](#ec)

### Split Tickets

Split one QR Code into multiple independent tickets; each can be used or gifted separately.

### Comment out Code

Wrap code so it does not run—temporarily disable features for testing while keeping the original code for later restore.

### UID

**Unique Identifier**, a unique string or number assigned to one entity (user, device, order, or file) for unambiguous identification.

### 2FA

**Two-Factor Authentication**, security that requires a second factor beyond the password (often a phone code) to stop easy takeovers.

### RWD

**Responsive Web Design**, layouts that adapt to desktop, tablet, and phone screens for a consistent, readable experience.

- **See also**: [Switch between edit and preview](../ec/website-appearance/theme-and-layout/theme-editor.md#operate-theme-editor-preview){ title="Switch between edit and preview" }
