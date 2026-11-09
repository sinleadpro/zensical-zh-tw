---
description: "CYBERBIZ Help Center home: entry points for Brand Website, Smart Warehouse, Smart POS, add-ons, and the Resource Center."
title: Home
lang: en-US
author: Jase
reviewers: []
products: [EC, POS, WMS]
plan_options: []
notes: []
hide:
  - description
  - feedback
  - navigation
  - toc
permalink: "https://help.cyberbiz.io/"
---

<div style="display: flex; gap: 2rem; flex-wrap: wrap; padding: 3rem 0 4rem;" markdown>

<div style="flex: 1 1 380px; min-width: 0;" markdown>

<h1 style="margin-top: 0; font-size: 1.5rem;">
  Start your ecommerce success journey
  <!-- <span style="white-space: nowrap;"> -->
  <!--   <span style="color: #03328e;">CYBERB</span> -->
  <!--   <span style="color: #ff7d00;">⋮</span> -->
  <!--   <span style="color: #03328e;">Z</span> -->
  <!-- </span> -->
</h1>

<p style="font-size: 0.95rem; line-height: 1.7;">
Complete steps from account signup and product listing to marketing.<br>We prepared a full digital-transformation guide to help your brand shine.
</p>

[:lucide-arrow-right: Start exploring](ec/){ title="Brand website" .md-button .md-button--primary }

</div>

<div style="flex: 1 1 380px; min-width: 0;">

<style>
[data-md-color-scheme="default"] {
  --callout-bg: #f2f6fc;
  --callout-hover: #e2e8f0;
  --badge-color: #6674c4;
  --text-color: #111;
  --divider-color: #e6e8ee;
  --border-color: #e6e8ee;
}
[data-md-color-scheme="slate"] {
  --callout-bg: #1e1e1e;
  --callout-hover: #383838;
  --badge-color: #6674c4;
  --text-color: #eee;
  --divider-color: #333;
  --border-color: #333;
}
.hero-callout {
  box-sizing: border-box;
  background-color: var(--callout-bg);
  border-radius: 12px;
  padding: 1rem 1.5rem;
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
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
.badge {
  background-color: var(--badge-color);
  color: white;
  border-radius: 4px;
  font-size: 0.65rem;
  padding: 0.1rem 0.4rem;
  font-weight: 600;
  white-space: nowrap;
}
@media (max-width: 640px) {
  .hero-callout {
    padding: 0.75rem 1rem;
  }
  .tab-buttons {
    overflow-x: auto;
    flex-direction: row;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  .tab-buttons::-webkit-scrollbar {
    display: none;
  }
  .tab-btn {
    flex: 0 0 auto;
    white-space: nowrap;
    width: auto;
    text-align: center;
  }
  .tab-content a {
    padding: 0.5rem 0.5rem;
  }
}
</style>

<div class="hero-callout">

  <div role="tablist" class="tab-buttons">
    <button role="tab" aria-selected="true" class="tab-btn active"
      onclick="openTab(event, 'announcement')">Latest announcements</button>
    <button role="tab" aria-selected="false" class="tab-btn"
      onclick="openTab(event, 'latest')">Latest docs</button>
    <button role="tab" aria-selected="false" class="tab-btn"
      onclick="openTab(event, 'popular')">Popular articles</button>
  </div>

  <div id="announcement" role="tabpanel" class="tab-content" style="display:flex">
    <a href="/ec/products/create-and-manage/create-update-products/?tour=1"><span class="badge">New features</span>New Help Center navigation is live <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="lucide lucide-circle-arrow-right" viewBox="0 0 24 24" width="1em" height="1em" style="vertical-align:middle;margin-left:2px"><circle cx="12" cy="12" r="10"/><path d="m12 16 4-4-4-4M8 12h8"/></svg></a>
    <a href="/ec/website-management/security-settings/#operate-security-sms-bot-protection"><span class="badge">New features</span>Member signup SMS adds bot protection</a>
    <!-- <a href="#"><span class="badge">Notice</span>CYBERBIZ payment service upgrade notice</a> -->
    <!-- <a href="#"><span class="badge">New features</span>Omnichannel inventory sync is generally available</a> -->
  </div>

  <div id="latest" role="tabpanel" class="tab-content">
    <a href="/resources/new-release/2026-10/"><span class="badge">New</span>October 2026 Release Notes <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="lucide lucide-circle-arrow-right" viewBox="0 0 24 24" width="1em" height="1em" style="vertical-align:middle;margin-left:2px"><circle cx="12" cy="12" r="10"/><path d="m12 16 4-4-4-4M8 12h8"/></svg> </a>
    <a href="/resources/new-release/2026-09/"><span class="badge">New</span>September 2026 Release Notes <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="lucide lucide-circle-arrow-right" viewBox="0 0 24 24" width="1em" height="1em" style="vertical-align:middle;margin-left:2px"><circle cx="12" cy="12" r="10"/><path d="m12 16 4-4-4-4M8 12h8"/></svg> </a>
    <a href="/resources/new-release/2026-08/"><span class="badge">New</span>August 2026 Release Notes <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="lucide lucide-circle-arrow-right" viewBox="0 0 24 24" width="1em" height="1em" style="vertical-align:middle;margin-left:2px"><circle cx="12" cy="12" r="10"/><path d="m12 16 4-4-4-4M8 12h8"/></svg> </a>
    <!-- <a href="#"><span class="badge">Updated</span>EC product listing flow</a> -->
    <!-- <a href="#"><span class="badge">New</span>New payments and logistics setup guide</a> -->
  </div>

  <div id="popular" role="tabpanel" class="tab-content">
    <!-- <a href="#"><span class="badge">FAQ</span>EC payment flow FAQ</a> -->
    <!-- <a href="#"><span class="badge">FAQ</span>Product management FAQ roundup</a> -->
    <!-- <a href="#"><span class="badge">Guide</span>Store permission setup practice guide</a> -->
  </div>

</div>

<script>
function openTab(evt, tabName) {
  document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('active');
    btn.setAttribute('aria-selected', 'false');
  });
  document.getElementById(tabName).style.display = 'flex';
  evt.currentTarget.classList.add('active');
  evt.currentTarget.setAttribute('aria-selected', 'true');
}

</script>
</div>

</div>


## Brand Website { #overview-home-ec }

<div class="grid cards" markdown>

<!-- -   :lucide-rocket:{ .lg }
    [__Get started__](ec/){ title="Brand website" }

    ---

    Build your brand website from scratch and learn admin basics quickly. -->

-   :lucide-store:{ .lg }
    [__Store settings__](ec/website-management/){ title="Admin center" }

    ---

    Manage website appearance, domains, SEO, invoicing, and admin permissions.

-   :lucide-package:{ .lg }
    [__Product management__](ec/products/){ title="Product management" }

    ---

    Create categories, list products, and set variants and selling methods.

-   :lucide-truck:{ .lg }
    [__Orders and shipping__](ec/orders/){ title="Orders overview" }

    ---

    Fulfill orders, handle returns and refunds, and connect convenience-store and home-delivery shipping.

-   :lucide-megaphone:{ .lg }
    [__Marketing campaigns__](ec/marketing/){ title="Marketing campaigns" }

    ---

    Set up promotions, Bonus Mall, one-page stores, and interactive games.

-   :lucide-credit-card:{ .lg }
    [__Payments and logistics__](ec/payments-and-logistics/){ title="Payments" }

    ---

    Configure multiple payment and shipping methods for domestic and cross-border flows.

</div>

---

## Smart Warehouse { #overview-home-wms }

<div class="grid cards" markdown>

-   :lucide-log-in:{ .lg }
    [__Apply and activate__](wms/application-process-and-activation.md){ title="Warehouse connection application and activation" }

    ---

    Learn the Smart Warehouse application flow, activation settings, and connection rules.

-   :lucide-package:{ .lg }
    [__Product management__](wms/single-items.md){ title="Single items" }

    ---

    Manage single items, processed goods, and seasonal groups.

-   :lucide-arrow-right-left:{ .lg }
    [__Inbound and outbound__](wms/inbound-orders.md){ title="Inbound orders" }

    ---

    Create inbound, transfer, and return orders to manage stock moves.

-   :lucide-bar-chart-3:{ .lg }
    [__Inventory management__](wms/inventory-records.md){ title="Inventory records" }

    ---

    Look up inventory and activity records and set report notifications.

</div>

---

## Smart POS { #overview-home-pos }

<div class="grid cards" markdown>

-   :lucide-rocket:{ .lg }
    [__Get started__](pos/get-started/){ title="Get started" }

    ---

    Hardware install, software setup, and a quick go-live guide.

-   :lucide-monitor:{ .lg }
    [__Hardware setup__](pos/hardware/){ title="System hardware and environment requirements" }

    ---

    Set up customer displays, label printers, invoice printers, card terminals, and more.

-   :lucide-shopping-cart:{ .lg }
    [__Checkout features__](pos/check/){ title="Checkout" }

    ---

    Multiple payment methods, offline checkout, guest checkout, and label printing.

<!-- -   :lucide-bar-chart-3:{ .lg }
    [__Inventory management__](pos/inventory/)

    ---

     Inbound/outbound orders, stock adjustments, counts, and omnichannel inventory. -->


</div>

---

## Add-Ons and Integrations { #overview-home-extensions }

<div class="grid cards" markdown>

-   :lucide-layout-grid:{ .lg }
    [__APP MARKET__](ec/app-market/){ title="APP MARKET overview" }

-   :lucide-cog:{ .lg }
    [__Automation__](ec/app-market/automation/automation-push-flow.md){ title="Build automated messaging flows with AUTOMATION" }

-   :lucide-ticket:{ .lg }
    [__E-tickets__](ec/e-ticket/e-ticket-setup-guide.md){ title="E-ticket setup guide" }

-   :lucide-zap:{ .lg }
    [__Quick delivery__](ec/payments-and-logistics/cyberbiz-now/index.md){ title="CYBERBIZ NOW quick delivery" }

-   :lucide-credit-card:{ .lg }
    [__Payments__](ec/payments-and-logistics/){ title="Payments" }

-   :lucide-message-circle:{ .lg }
    [__Messaging hub__](ec/app-market/chatbox/){ title="CHAT BOX messaging hub" }

-   :lucide-link-2:{ .lg }
    [__Omnichannel assistant__](ec/app-market/cyberbiz-channel-bridge/shopee-integration/step1-install-and-activate.md){ title="Step 1 Install and authorize the store" }

-   :lucide-shopping-cart:{ .lg }
    [__Store assistant__](ec/app-market/storepal/){ title="Store assistant" }

-   :lucide-arrow-right-from-line:{ .lg }
    [__EXPRESS__](ec/app-market/express/cyberbiz-express-japan-to-taiwan-delivery.md){ title="CYBERBIZ EXPRESS Japan-to-Taiwan cross-border delivery" }

</div>

---

## Cross-Border Ecommerce

<div class="grid cards" markdown>

-   :lucide-rocket:{ .lg }
    __Cross-border payments__

    ---

    [:octicons-arrow-right-24: Go to North America site](ec/payments-and-logistics/north-america-payment-services/)<br>
    [:octicons-arrow-right-24: Go to Japan site](ec/payments-and-logistics/japan-payment-services/)<br>
    [:octicons-arrow-right-24: Go to Southeast Asia site](ec/payments-and-logistics/southeast-asia-payment-services/)<br>
    [:octicons-arrow-right-24: Go to Australia local edition](ec/payments-and-logistics/australia-local-payment-services/)<br>

-   :lucide-monitor:{ .lg }
    __Cross-border logistics__

    ---

    [:octicons-arrow-right-24: Go to DHL logistics](ec/payments-and-logistics/dhl-cross-border-logistics/)<br>
    [:octicons-arrow-right-24: Go to LINEX logistics](ec/payments-and-logistics/linex-cross-border-logistics/)<br>
    [:octicons-arrow-right-24: Go to SF Express overseas logistics](ec/payments-and-logistics/sf-express-overseas-logistics/)<br>
    [:octicons-arrow-right-24: Go to Amazon FBA logistics](ec/payments-and-logistics/amazon-fba-cross-border-logistics/)<br>

-   :lucide-shopping-cart:{ .lg }
    __Returns and refunds__

    ---

    [:octicons-arrow-right-24: Order return process](ec/orders/cross-border-return-process/)<br>
    [:octicons-arrow-right-24: Order refund process](ec/orders/cross-border-refund-process/)

-   :lucide-arrow-right-from-line:{ .lg }
    [__Storefront multi-language and multi-currency__](ec/website-management/setup-multi-language-and-multi-currency/)

    ---

    Set up localized storefront languages and currency display to improve the shopping experience for overseas customers.

-   :lucide-arrow-right-from-line:{ .lg }
    [__Redirect to country-specific websites__](ec/website-management/setup-country-site-redirect/)

    ---

    Show a notice bar on your storefront based on the country of the customer's IP address, guiding customers to the website for their country.

</div>


---
<!---->
<!-- ## AI-assisted search -->
<!---->
<!-- <div class="grid cards" markdown> -->
<!---->
<!-- -   :simple-notebooklm:{ .lg } -->
<!--     [__NotebookLM__](https://notebooklm.google.com/notebook/20277bb4-f8ae-4d7b-b2d9-3b8db845c761/preview){ target="_blank" } -->
<!---->
<!--     --- -->
<!---->
<!--     Search CYBERBIZ docs with NotebookLM for AI-assisted Q&A and analysis. -->
<!---->
<!-- -   :lucide-file-text:{ .lg } -->
<!--     [__LLM-readable docs (llms.txt)__](llms.txt) -->
<!---->
<!--     --- -->
<!---->
<!--     Markdown optimized for LLMs to improve RAG retrieval and context accuracy. -->
<!---->
<!-- </div> -->
<!---->
<!-- --- -->

## Resource Center { #overview-home-resources }

<div class="grid cards" markdown>

-   :lucide-bookmark:{ .lg }
    [__Glossary__](resources/glossary/){ title="Glossary" }

    ---

    From marketing strategy to payment integrations, essential ecommerce know-how lives here.

-   :lucide-video:{ .lg }
    [__Video tutorials__](resources/video-tutorials/){ title="Video Tutorials Overview" }

    ---

    Progressive audiovisual guidance to help you learn each smart system feature quickly.

-   :lucide-download:{ .lg }
    [__Downloads__](resources/downloads/){ title="Downloads" }

    ---

    CYBERBIZ learning resources and document downloads in one place.

</div>
