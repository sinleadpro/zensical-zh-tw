---
title: "Ad Schedule Statuses Reference"
description: "The schedule statuses of scheduled carousel placements (default, live, scheduled, ended), which the system determines automatically based on the current time."
created: 2026-06-10 15:45
last_modified: 2026-06-10 15:49
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
permalink: "https://help.cyberbiz.io/ec/website-appearance/references/scheduled-carousel-statuses/"
comments: ""
search:
  exclude: false
icon: lucide/table
hide:
---


### Ad Schedule Statuses Reference { #reference-scheduled-carousel-statuses }

| Status | Description |
| :-- | :-- |
| Default | The permanent image for a placement. It shows when no other scheduled period is live in that placement. |
| Live | A scheduled period currently showing on the storefront (its start time has passed and its end time has not). |
| Scheduled | A scheduled period that has been created but has not reached its start time. It goes live automatically when the time comes. |
| Ended | A period whose end time has passed and whose schedule has ended. You can adjust its times and put it live again at any time. |

!!! note "Note"
    * The system sets the status automatically by comparing the current time with each period's start and end times. You do not need to switch it manually.
    * The "Default" image has no time limit and can coexist with other scheduled periods in the same placement.
