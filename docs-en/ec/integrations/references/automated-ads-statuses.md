---
title: "Automated Ads Activation and Delivery Status Reference"
description: "Describes the activation process and delivery statuses for automated ads, including pending and completed activation states and notification methods."
created: 2026-06-11 10:19
last_modified: 2026-06-11 12:30
lang: en-US
type: reference
author: Jase
reviewers: []
notes: []
ga_views:
feedback:
products:
  - EC
modules: []
sites:
  - TW
audiences:
  - merchant
difficulty: ""
tnb: ""
plans:
plan_options: []
cyb_extensions: []
intents: []
features: []
prerequisites: []
related: []
tags: []
acoiv: ""
apis: []
devices:
  - desktop
  - mobile
ui_components: []
paths: []
layouts: []
wp_url: []
permalink: "https://help.cyberbiz.io/ec/integrations/references/automated-ads-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


 Automated Ads Activation and Delivery Status Reference

## Activation Status Reference { #automated-ads-apply-status }

| Status | Description |
| :-- | :-- |
| Pending Activation | The first top-up is complete. CYBERBIZ is creating your account and setting up the GMC connection, which takes about 3 to 5 business days. |
| Activated | Your account and GMC connection are set up. You can start configuring and running ads. |

!!! note "Note"
    * Activation progress is sent by email, and you can also check it in the activation prompt at the top of the page.
    * If you use a **Merchant-Owned Account**, the system checks the Google Ads connection status daily and activates the account only after the connection is complete.

## Ad Delivery Status Reference { #automated-ads-delivery-status }

| Delivery Status | Description |
| :-- | :-- |
| Running | Ads are delivering normally. View real-time spend in **Campaign Management**. |
| Paused | Ads have stopped showing. This commonly happens when the merchant pauses them manually or when the ad spend balance is insufficient and ads pause automatically. |

!!! note "Note"
    * When the ad spend balance is insufficient, the system automatically pauses ad delivery. Ads resume after you top up the balance.
    * Switch the status manually in **Google Ads Settings** by clicking **Pause Delivery** or **Resume Delivery**.
