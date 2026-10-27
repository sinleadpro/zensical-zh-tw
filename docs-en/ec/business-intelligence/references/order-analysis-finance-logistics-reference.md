---
title: "Order Payment and Shipping Analysis Charts Reference"
description: "Chart types and display conditions for the three analysis groups on the order payment and shipping analysis tab."
created: 2026-06-15 00:00
last_modified: 2026-07-10 11:23
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
  - "Order Analysis"
  - "Payment and Shipping Analysis"
  - "Payment Methods"
  - "Shipping Methods"
  - "Third-Party Referrals"
  - "Average Order Value"
  - "Return Rate"
permalink: "https://help.cyberbiz.io/ec/business-intelligence/references/order-analysis-finance-logistics-reference/"
icon: lucide/table
hide:
---

### Three Analysis Groups { #reference-order-analysis-finance-logistics }

=== "Payment Method"
    | Chart | What It Means | Calculation |
    | :-- | :-- | :-- |
    | Orders (Monthly Trend) | Orders per payment method per month | Sum of orders per payment method per month |
    | Share (Monthly Trend) | Share of orders per payment method per month | (Orders with one payment method in the month ÷ total orders in the month) × 100% |
    | Share (Period) | Share of orders per payment method in the period | (Orders with one payment method in the period ÷ total orders in the period) × 100% |
    | Average Order Value (Monthly Trend) | Average order amount per payment method per month | Total order amount per payment method per month ÷ orders with that payment method |
    | Average Order Value (Period) | Average order amount per payment method in the period | Total order amount per payment method ÷ total orders with that payment method |
    | Return Rate (Monthly Trend) | Return rate per payment method per month | (Returned orders with the payment method in the month ÷ non-canceled orders with the payment method in the month) × 100% |
    | Return Rate (Period) | Return rate per payment method in the period | (Returned orders with the payment method ÷ non-canceled orders with the payment method) × 100% |

=== "Shipping Method"
    | Chart | What It Means | Calculation |
    | :-- | :-- | :-- |
    | Orders (Monthly Trend) | Orders per shipping method per month | Sum of orders per shipping method per month |
    | Share (Monthly Trend) | Share of recognized orders per shipping method per month | (Recognized orders per shipping method in the month ÷ all recognized orders in the month) × 100% |
    | Share (Period) | Share of recognized orders per shipping method in the period | (Recognized orders per shipping method ÷ all recognized orders) × 100% |
    | Average Order Value (Monthly Trend) | Average order amount per shipping method per month | Average amount of recognized orders per shipping method per month (calculated separately for each shipping method) |
    | Average Order Value (Period) | Average order amount per shipping method in the period | Total amount of recognized orders per shipping method ÷ recognized orders with that shipping method |
    | Return Rate (Monthly Trend) | Return rate per shipping method per month | (Returned orders with the shipping method in the month ÷ non-canceled orders with the shipping method in the month) × 100% |
    | Return Rate (Period) | Return rate per shipping method in the period | (Returned orders with the shipping method ÷ non-canceled orders with the shipping method) × 100% |

=== "Third-Party Referrals"
    | Chart | What It Means | Calculation |
    | :-- | :-- | :-- |
    | Orders (Monthly Trend) | Orders per source per month | Sum of orders per source per month |
    | Share (Period) | Share of recognized orders per source in the period | (Recognized orders per source ÷ all recognized orders) × 100% |
    | Average Order Value (Monthly Trend) | Average order amount per source per month | Total amount of recognized orders per source in the month ÷ recognized orders per source in the month |
    | Average Order Value (Period) | Average order amount per source in the period | Total amount of recognized orders per source ÷ recognized orders per source |
    | Return Rate (Monthly Trend) | Return rate per source per month | (Returned orders per source in the month ÷ non-canceled orders per source in the month) × 100% |
    | Return Rate (Period) | Return rate per source in the period | (Returned orders per source ÷ non-canceled orders per source) × 100% |

!!! note "Note"
    * "Recognized orders" are orders that are not canceled and whose return status is no return needed or return rejected. See [Recognized Order Definition](../order-analysis.md#prerequisites-order-analysis-recognized-order){ title="Recognized Order Definition" } in the main article.
    * Payment method shares use "total orders" as the base. Shipping method and third-party referral shares and average order values use "recognized orders" as the base.
    * For every dimension, the return rate's denominator is "non-canceled orders."
    * Average order value is the average within "that dimension itself" (calculated separately for each method or source), not divided by all orders.
    * **Third-party referrals** are orders brought in through connected referral platforms (such as LINE Shopping or Market America). The chart shows each source based on the platforms actually connected.

<!---->
<!---->
<!-- The "Order Payment & Logistics Analysis" tab breaks orders down from three angles, and each angle provides four kinds of charts: order trend, order share, average order value, and return rate. -->
<!---->
<!-- | Analysis Group | Charts Provided | What It Means for Merchants | When It Appears | -->
<!-- | :-- | :-- | :-- | :-- | -->
<!-- | Payment Method | Order trend, order share, average order value, return rate | Compare order volume, share, and returns across payment methods (such as credit card, cash on delivery, LINE Pay, and convenience store payment) to find high-performing or high-risk payment channels. | Shown when you open this tab. Options reflect the payment methods the merchant has actually enabled. | -->
<!-- | Shipping Method | Order trend, order share, average order value, return rate | Compare order performance across shipping methods (such as home delivery, convenience store pickup, and store-to-store) to help assess logistics costs and customer convenience. | Shown when you open this tab. Options reflect the shipping methods the merchant has actually enabled. | -->
<!-- | Third-Party Referrals | Order trend, order share, average order value, return rate | See the number, share, and average order value of orders from referral platforms to assess referral performance. | Appears only if the store has connected a referral platform. See the note below. | -->
<!---->
<!-- !!! note "Note" -->
<!--     * **Third-party referral** charts appear only if the store meets any of these conditions: "Market America Partner Store" is set up, "iChannels" is connected, or "LINE Shopping" is connected. If none is enabled, the whole group of third-party referral charts does not appear. -->
<!--     * "Average order value" in each chart is that group's revenue divided by the corresponding number of orders. -->
<!--     * Return rate and cancellation exclusion rules are the same as for the overall report. See "Important Rules and Limitations" in the main article for definitions. -->
