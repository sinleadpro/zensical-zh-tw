---
title: "Tiered Documentation Information Architecture"
created: "2026-03-05 10:50"
last-modified: 2026-03-05 11:18
type: manual
tags:
---

## Purpose

This document defines the **information architecture (IA)** for maintaining a **single documentation site that supports multiple product tiers/plans**.

The goal is to:

- Maintain **one canonical documentation source**
- Avoid **content duplication and drift**
- Provide **clear visibility of feature availability per plan**
- Reduce **user friction when navigating between tiers**
- Ensure documentation remains **scalable as plans evolve**

This architecture follows a **Single Source of Truth (SSOT)** model with **conditional audience segmentation**.

---

## Core Architecture Principles

### 1. Single Source of Truth (SSOT)

All documentation lives in **one unified doc site (zensical)** rather than separate sites per plan.

Benefits:

- Prevents content divergence
- Reduces maintenance overhead
- Simplifies search and navigation
- Improves long-term maintainability

---

### 2. Trunk vs Branch Content Model

Documentation content is divided into two conceptual layers.

#### Trunk Content

Content applicable to **all plans**.

Characteristics:

- Default content on the page
- Represents the **common workflow**
- Should make up the **majority of the document**

Rule:

> Trunk content should represent **at least 70% of the page**.

Examples:

- Feature overview
- Basic configuration steps
- Common workflows

---

#### Branch Content

Content that applies only to **specific tiers/plans**.

Characteristics:

- Highlighted with **tier indicators**
- Clearly separated from trunk content
- Used only where feature differences exist

Examples:

- Enterprise-only features
- Plan-specific limits
- Advanced configuration options

---

## Multi-Dimensional Documentation Strategy

Documentation must account for **multiple types of variation**.

These variations are handled using **two mechanisms**:

| Variation Type | Mechanism |
|----------------|-----------|
| Workflow differences | Tabs |
| Plan entitlement | Tier blocks |

---

## Tabs (Workflow Variations)

Tabs are used when **users must choose between different procedures**.

Example scenarios:

- Different authentication methods
- Different deployment environments
- Different integration types

Example:
```

=== “SAML”

```
Steps for configuring SAML.
```

=== “OAuth”

```
Steps for configuring OAuth.
```

```
Guidelines:

- Use when **workflows are mutually exclusive**
- Maximum **2–3 tabs recommended**
- Avoid using tabs for **pricing tier differences**

---

## Tier Blocks (Plan Differences)

Tier blocks are used when **features are available only in specific plans**.

Example:
```

::: tier enterprise master-plus

Advanced SAML configuration options are available.

:::

```
Purpose:

- Inform users which plans support a feature
- Avoid duplicating entire workflows
- Preserve trunk content integrity

---

## Tier Badges

Tier badges appear **under the page title** to indicate feature availability.

Example metadata:
```

---

## title: SSO Configuration

##   

## tiers: [enterprise, master-plus]

```
This allows users to quickly identify:

- Which plans support the feature
- Whether an upgrade may be required

---

## When to Use Each Pattern

### Use Trunk Content When

- Instructions apply to all users
- Feature is universally available
- Differences are minimal

---

### Use Tier Blocks When

- Only a **small section differs**
- Feature is **plan-gated**
- Additional options exist for higher tiers

---

### Use Tabs When

- Workflows are **fundamentally different**
- Users must select **one path**
- Steps differ significantly

---

## Architecture Rules

### Rule 1 — Limit Tab Count

Tabs should not exceed:

> **3 per page**

Too many tabs increase cognitive load.

---

### Rule 2 — Protect Trunk Dominance

Branch content should remain limited.

If tier-specific content exceeds **30% of the page**, consider:

- Splitting the page
- Creating a dedicated advanced guide

---

### Rule 3 — Avoid Content Duplication

The same instructions should **never appear in multiple tier sections**.

Instead:

- Place shared content in trunk
- Add tier blocks for differences

---

### Rule 4 — Ensure Edit Efficiency

If a workflow step changes, it should require editing **no more than two locations**.

If more edits are required, the architecture needs restructuring.

---

## Example Page Structure
```

# SSO Configuration

  

[ Tier Badges ]

  

## Overview

  

Trunk explanation of SSO configuration.

  

## Authentication Method

  

=== “SAML”

```
Base SAML setup steps.

::: tier enterprise master-plus
Advanced SAML configuration options.
:::
```

=== “OAuth”

```
OAuth setup instructions.
```

```
This structure ensures:

- Shared explanation remains centralized
- Tier differences remain explicit
- Workflow differences remain clear

---

## Benefits of This Architecture

- Reduces documentation duplication
- Prevents content drift
- Improves readability
- Scales as plans evolve
- Supports automated processing and future tooling

---

## Future Scalability

This architecture supports future improvements such as:

- Tier-aware documentation generation
- Automated content validation
- AI-assisted documentation search
- Conditional content filtering

By structuring documentation around **semantic content blocks**, the system remains flexible for future tooling and automation.

---

## Summary

The documentation architecture follows three core concepts:

1. **Single Source of Truth**
2. **Trunk and Branch Content Model**
3. **Hybrid Variation Handling (Tabs + Tier Blocks)**

This approach enables scalable, maintainable documentation for **multi-tier SaaS products** while preserving clarity for users across all plans.



