---
title: "Coupon Metric Definitions Reference"
description: "Definitions and calculation methods for metrics on the coupon analysis page, covering type analysis and specific coupon analysis, including discount amount, usage rate, and average usage period."
created: 2026-06-16 00:00
last_modified: 2026-07-12 19:18
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
plans: []
plan_options: []
tags:
  - "Report Analysis"
  - "Marketing Campaign Analysis"
  - coupon
  - "Discount Amount"
  - "Usage Rate"
  - "Issued Quantity"
  - "Used Quantity"
  - "Average Usage Period"
  - "Metrics Reference"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/marketing-activity-coupon-metrics-reference/"
icon: lucide/table
hide:
---

# Coupon Metric Definitions Reference

The metric cards on the "Coupon Analysis" tab are defined below, in two groups: "Type Analysis" and "Specific Coupon Analysis." All metrics count **valid orders** only.

### Coupon Type Analysis Metrics { #reference-marketing-activity-coupon-metrics-category }

| Metric | Definition |
| :-- | :-- |
| Average Discount Amount | Total discount from coupons in the category ÷ total number of orders using coupons in the category. |
| Discount Amount | Total discount from coupons in the category. |
| Average Discount Rate | Total discount from coupons in the category ÷ total amount, before marketing discounts and excluding shipping, of orders using coupons in the category. |
| Coupon Usage Times | Number of times coupons in the category were used (if an order is canceled, the coupon is returned and that use is not counted). |
| Average Order Value | Total revenue of orders using coupons in the category ÷ total number of orders using coupons in the category. |
| Coupon Order Revenue | Total revenue of orders using coupons in the category. |
| Average Usage Period (Days) | Average number of days between when a coupon in the category is sent to a member's account and when it is used. |
| Coupons Issued | Number of coupons "available for use" on your online store that day. The system automatically counts these sources daily: coupons issued today, and coupons issued before today that are still valid today. |
| Coupons Used | Number of coupons on your online store that day that are "within their validity period and recognized as used." When a customer successfully uses a coupon during its validity period, it counts toward the used quantity (quantity 1) on every day from the day of use until the coupon expires. Once the coupon expires, it is no longer counted as used on later dates. |

---

### Specific Coupon Analysis Metrics { #reference-marketing-activity-coupon-metrics-specific }

| Metric | Definition |
| :-- | :-- |
| Discount Amount | Total discount from this coupon. |
| Average Discount Rate | Total discount from this coupon ÷ total amount, before marketing discounts and excluding shipping, of orders using this coupon. |
| Average Order Value | Total revenue of orders using this coupon ÷ total number of orders using this coupon. |
| Coupon Order Revenue | Total revenue of orders using this coupon. |
| Coupon Usage Times | Number of times this coupon was used (if an order is canceled, the coupon is returned and that use is not counted). |
| Coupon Usage Rate | Number of times this coupon was used ÷ number of times this coupon was issued. |
| Average Usage Period (Days) | Average number of days between when this coupon is sent to a member's account and when it is used. |
| Number of Target Customers | Number of members who hold this coupon (each member is counted once for the same coupon). |
| Total Revenue of Target Customers | Total spending in this period by members who hold this coupon (counted whether or not they used the coupon). |
