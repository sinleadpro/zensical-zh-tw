---
description: "The CYBERBIZ Smart Warehousing (WMS) product center covers application and activation, product management, inbound and outbound operations, and inventory management."
author: ""
reviewers: []
products: 
  - WMS
plan_options: []
notes: []
title: "Smart Warehousing (WMS) Product Center"
lang: en-US
permalink: "https://help.cyberbiz.io/wms/"
hide:
  - description
  - path
  - toc
  - feedback
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
        <span style="color: #03328e; font-size: 1.2em;">Warehousing</span>
      </span>
    </h1>

    <p>
      <big><strong>Professional E-commerce Warehouse Management</strong></big><br>
      From receiving and storage to systematic shipping and returns, we handle the last mile of logistics so you can focus on your brand.
    </p>

    <div class="custom-button-group" style="
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-top: 1rem;
    ">
      <a href="merchant-inbound-operation-rules.md" class="md-button md-button--primary">Merchant Inbound Operation Rules ➜</a>
      <a href="application-process-and-activation.md" class="md-button">Online Store Warehouse Integration Guide</a>
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
      <a href="processed-products.md"><span class="badge">Updated</span>Bundle Products</a>
	  <a href="duplicate-order.md"><span class="badge">New</span>Clone Orders</a>
    </div>

    <!-- Popular -->
    <div id="popular" role="tabpanel" class="tab-content">
      <a href="returns-and-vehicle-dispatch.md"><span class="badge">Updated</span>Returns and Vehicle Dispatch</a>
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

## Core Features { #overview-wms-core }

<div class="grid cards" markdown>

-   :lucide-package: __Product Management__

    ---
    Manage single products, bundle products, and season groups

    [:octicons-arrow-right-24: Single Products](single-items.md)<br>
    [:octicons-arrow-right-24: Bundle Products](processed-products.md)

-   :lucide-arrow-right-left: __Warehouse Operations__

    ---
    Full document flows for receiving, outbound, and transfers

    [:octicons-arrow-right-24: Receipt Orders](inbound-orders.md)<br>
    [:octicons-arrow-right-24: Transfer Orders](transfer-orders.md)

-   :lucide-shopping-cart: __Order Processing__

    ---
    Sync Online Store orders automatically, with manual order creation and POD tracking

    [:octicons-arrow-right-24: Order List](list.md)<br>
    [:octicons-arrow-right-24: Manual Order Creation](manual-order-creation.md)

-   :lucide-settings: __System Settings__

    ---
    Store information, account permissions, and report notifications

    [:octicons-arrow-right-24: Permission Settings](permission-settings.md)<br>
    [:octicons-arrow-right-24: Store Settings](store-settings.md)

</div>

---

## Core Operating Scenarios { #intro-wms-scenarios }

<div class="grid" markdown>

<div>
<big><strong>Automatic Sync Between Online Store and Warehouse</strong></big><br>
Sync stock in real time and split or combine orders automatically, so Online Store orders reach the warehouse system for shipping quickly and accurately.
<br><br>


<a href="site-and-warehouse-sync-rules.md" class="md-button md-button--primary">Site and Warehouse Sync Rules ➜</a><br><br>
<a href="enable-partial-warehouse-integration-and-order-splitting.md" class="md-button">Enable Partial Warehouse Integration and Order Splitting ➜</a>  
<a href="enable-partial-warehouse-integration-and-mixed-orders.md" class="md-button">Enable Partial Warehouse Integration and Mixed Orders ➜</a>
</div>

![](../assets/images/EC-後台-金物流-宅配物流-拆單畫面總覽01.en.png)

</div>

---

## Explore by Role { #next-steps-wms-roles }

<div class="grid cards" markdown>

-   :lucide-user: __Warehouse Staff__

    ---
    Focus on floor operations and stock changes

    [:octicons-arrow-right-24: Create Receipt Orders](inbound-orders.md)<br>
    [:octicons-arrow-right-24: Create Return Orders](return-orders.md)<br>
    [:octicons-arrow-right-24: Look Up Inventory Records](inventory-records.md)

-   :lucide-user-cog: __Operations Managers__

    ---
    Focus on system integration and data monitoring

    [:octicons-arrow-right-24: Set Up Staff Accounts](account-management.md)<br>
    [:octicons-arrow-right-24: Operation Logs](operation-logs.md)<br>
    [:octicons-arrow-right-24: Report Notification Settings](report-notification-settings.md)

</div>
