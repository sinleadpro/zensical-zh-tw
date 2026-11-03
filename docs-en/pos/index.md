---
description: "CYBERBIZ Smart POS Product Center provides operating guides for hardware installation, checkout features, and inventory management."
author: ""
reviewers: []
products: [POS]
plan_options: []
notes: []
title: "Smart POS Product Center"
lang: en-US
hide:
  - description
  - path
  - toc
  - feedback
permalink: "https://help.cyberbiz.io/pos/"
---

<div class="hero-wrapper" style="
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 2rem;
    flex-wrap: wrap;
    margin-top: -2.2rem;
    padding: 4rem 0rem;
">

  <!-- LEFT: Hero -->
  <div class="homepage-hero" style="
      flex: 1 1 380px;
      min-width: 360px;
      max-width: 680px;
  ">
    <h1>
      Smart
      <span style="white-space: nowrap;">
        <span style="color: #03328e; font-size: 1.2em;">POS</span>
      </span>
    </h1>

    <p>
      <big><strong>All-in-One Omnichannel Retail Management Solution</strong></big><br>
      From basic checkout to omnichannel member integration, we offer a complete all-in-one retail solution.<br>
      Help merchants build member assets and run precise marketing, seamlessly connecting online and offline operations.
    </p>

    <div class="custom-button-group" style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
    ">
      <a href="get-started/index.md" class="md-button md-button--primary">Getting Started ➜</a>
      <a href="hardware/index.md" class="md-button">Hardware Installation</a>
    </div>
  </div>

  <!-- RIGHT: POS Callout -->
  <style>
	/* Light/Dark mode colors */
	[data-md-color-scheme="default"] {
	  --callout-bg: #f2f6fc;
	  --callout-hover: #FAFBFC;
	  --badge-color: #6674c4;
	  --text-color: #111;
	  --divider-color: #e6e8ee;
	  --border-color: #e6e8ee;
	}
	[data-md-color-scheme="slate"] {
	  --callout-bg: #1e1e1e;
	  --callout-hover: #2a2a2a;
	  --badge-color: #6674c4;
	  --text-color: #eee;
	  --divider-color: #333;
	  --border-color: #333;
	}

	/* Container */
	.hero-callout {
	  background-color: var(--callout-bg);
	  border-radius: 12px;
	  padding: 1rem 1.5rem;
	  border: 1px solid var(--border-color);
	  display: flex;
	  flex-direction: column;
	  gap: 1rem;
	  flex: 1 1 380px;
	  min-width: 360px;
	  max-width: 680px;
	}

	/* Tabs */
	.tab-buttons {
	  display: flex;
	  gap: 0.5rem;
	  border-bottom: 1px solid var(--divider-color);
	  padding-bottom: 2px;
	}

	.tab-btn {
	  flex: 1 1 auto;
	  background: transparent;
	  border: none;
	  font-weight: 600;
	  cursor: pointer;
	  padding: 0.5rem 1rem;
	  color: var(--text-color);
	  position: relative;
	  transition: color 0.2s;
	}

	.tab-btn:hover {
	  color: var(--badge-color);
	}

	.tab-btn::after {
	  content: "";
	  position: absolute;
	  left: 0;
	  bottom: -2px;
	  width: 100%;
	  height: 2px;
	  background: transparent;
	  transition: background 0.2s;
	}

	.tab-btn.active {
	  color: var(--badge-color);
	  font-weight: 700;
	}

	.tab-btn.active::after {
	  background: var(--badge-color);
	}

	/* Content list */
	.tab-content {
	  display: none;
	  flex-direction: column;
	  gap: 0.25rem;
	}

	.tab-content a {
	  display: flex;
	  align-items: center;
	  gap: 0.5rem;
	  padding: 0.3rem 0.5rem;
	  font-size: 0.8rem;
	  line-height: 1.4;
	  color: var(--text-color);
	  text-decoration: none;
	  border-radius: 6px;
	  transition: background 0.15s;
	}

	.tab-content a:hover {
	  background-color: var(--callout-hover);
	}

	/* Badge */
	.badge {
	  background-color: var(--badge-color);
	  color: white;
	  border-radius: 4px;
	  font-size: 0.65rem;
	  padding: 0.1rem 0.4rem;
	  font-weight: 600;
	  white-space: nowrap;
	}

	/* Mobile */
	@media (max-width: 640px) {
	  .tab-buttons {
	    flex-direction: column;
	  }
	  .tab-btn {
	    width: 100%;
	    text-align: center;
	  }
	}
  </style>

  <div class="hero-callout">
    <!-- Tabs -->
    <div role="tablist" class="tab-buttons">
      <button role="tab" aria-selected="true" class="tab-btn active"
        onclick="openTab(event, 'latest')">Latest Docs</button>
      <button role="tab" aria-selected="false" class="tab-btn"
        onclick="openTab(event, 'popular')">Popular Articles</button>
    </div>

    <!-- Latest -->
    <div id="latest" role="tabpanel" class="tab-content" style="display:flex">
      <a href="hardware/epson-tm-m30iii-invoice-printer.md"><span class="badge">New</span>EPSON TM-M30III Invoice Printer Installation Guide (Wi-Fi Connection)</a>
      <a href="others/daily-closing.md"><span class="badge">Updated</span>Print Subtotal and Close-Out Reports on Paper</a>
	  <a href="../ec/marketing/coupon/multiple-coupons.md"><span class="badge">New</span>POS Multi-coupon Checkout Features</a>
    </div>

    <!-- Popular -->
    <div id="popular" role="tabpanel" class="tab-content">
      <a href="software/drivers.md"><span class="badge">Updated</span>Install Drivers</a>
      <a href="store/renewal-and-add-on-plans.md"><span class="badge">Updated</span>Renewal and Add-On Plans</a>
    </div>
  </div>

  <script>
    function openTab(evt, tabName) {
      document.querySelectorAll('.tab-content')
        .forEach(el => el.style.display = 'none');

      document.querySelectorAll('.tab-btn')
        .forEach(btn => {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        });

      document.getElementById(tabName).style.display = 'flex';
      evt.currentTarget.classList.add('active');
      evt.currentTarget.setAttribute('aria-selected', 'true');
    }
  </script>

</div>

---

## Core Features Overview

<div class="grid cards" markdown>

-   :lucide-credit-card: __Seamless Checkout__

    ---
    Supports multiple payment methods and e-invoice issuance

    [:octicons-arrow-right-24: Set Up Payment Tools](check/payment-method/index.md)<br>
    [:octicons-arrow-right-24: Mirle E-Invoice](third-party/monolith-e-invoice.md)<br>
    [:octicons-arrow-right-24: Xingyixin E-Invoice](third-party/wixtar-e-invoice.md)<br>


-   :lucide-package-check: __Precise Inventory__

    ---
    Get real-time visibility into inventory across stores and e-commerce channels

    [:octicons-arrow-right-24: Inventory Management](inventory/index.md)

-   :lucide-users: __Member Management__

    ---
    Integrate Bonus Mall, customer display interactive games, and offline commissions

    [:octicons-arrow-right-24: Bonus Mall](check/bonus-point-mall.md)<br>
    [:octicons-arrow-right-24: Customer Display Games](check/customer-display-interactive-games.md)<br>
    [:octicons-arrow-right-24: Referral Program](../ec/profit-sharing/referrer-profit-sharing.md)<br>
    [:octicons-arrow-right-24: Registrant Profit Sharing](../ec/profit-sharing/registrant-profit-sharing.md)<br>
    [:octicons-arrow-right-24: Store Pickup Staff Commissions](store/pos-store-pickup-staff-commission.md)

-   :lucide-bar-chart-3: __Business Analytics__

    ---
    Multi-dimensional reports help you track sales trends

    [:octicons-arrow-right-24: Report Analysis](store/business-intelligence/pos-revenue-analysis/)

</div>

---

## Core Operations Scenarios

<div class="grid" markdown>

<div>
<br>  
<big><strong>All-in-One Counter Operations Workflow</strong></big><br>
Keep your checkout counter running smoothly. Covers card reader and invoice printer setup, plus advanced features such as offline checkout and sub-terminal binding.
<br><br>

<a href="check/index.md" class="md-button md-button--primary">View the Full Checkout Guide ➜</a>
</div>


![](../assets/images/POS-前台-結帳-付款方式01.en.png)

</div>

---

## Explore by Role

<div class="grid cards" markdown>

-   :lucide-user: __Store Staff__

    ---
    Focused on daily sales and customer service

    [:octicons-arrow-right-24: Front-Desk Staff Sign-In](store/staff-login.md)<br>
    [:octicons-arrow-right-24: Manage Regular Orders](orders/manage-general-orders.md)<br>
    [:octicons-arrow-right-24: Create a Front-Desk Product Menu](check/pos-frontend-menu-settings.md)<br>
    [:octicons-arrow-right-24: Scale Product Checkout](others/scale-settings.md)


-   :lucide-user-cog: __Store Managers and Administrators__

    ---
    Focused on store performance and resource allocation

    [:octicons-arrow-right-24: Manage Staff Permissions](store/staff-permissions-and-account-management.md)<br>
    [:octicons-arrow-right-24: Create Announcements](store/announcement-system.md)<br>
    [:octicons-arrow-right-24: Security and System Settings](store/pos-security-settings.md)<b>

</div>
