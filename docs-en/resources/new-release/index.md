---
title: "Release Notes"
description: "CYBERBIZ release notes organized by month, covering newly shipped features and improvements."
last_modified: 2026-10-27 15:45
type: hub
lang: en-US
author: Ann
reviewers: []
notes: []
related: []
permalink: "https://help.cyberbiz.io/resources/new-release/"
search:
  exclude: false
icon: lucide/megaphone
hide:
  - description
  - navigation
  - toc
  - feedback
  - path
---
<style>
  .release-index {
    --release-blue: #012e9e;
    --release-text: #111827;
    --release-muted: #697386;
    max-width: 1240px;
    margin: 0 auto;
    padding: 58px 40px 90px;
    color: var(--release-text);
  }

  .release-index,
  .release-index * {
    box-sizing: border-box;
  }

  .release-hero {
    display: flex;
    align-items: center;
    gap: 32px;
    margin-bottom: 38px;
  }

  .release-heading {
    min-width: 0;
  }

  .release-heading h1 {
    margin: 0;
    color: var(--release-text);
    font-size: 40px;
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1.2;
  }

  .release-heading p {
    margin: 14px 0 0;
    color: var(--release-muted);
    font-size: 17px;
    line-height: 1.8;
  }

  .release-timeline {
    display: grid;
    gap: 20px;
    margin-left: 0;
    width: 100%;
  }

  .release-month-card {
    display: grid;
    grid-template-columns: 265px 1px minmax(0, 1fr) 64px;
    column-gap: 28px;
    align-items: start;
    width: 100%;
    min-height: 156px;
    padding: 32px;
    border: 1px solid rgba(1, 46, 158, .08);
    border-radius: 28px;
    background: rgba(255, 255, 255, .98);
    box-shadow: 0 16px 42px rgba(1, 46, 158, .07);
    color: inherit;
    text-align: left;
    text-decoration: none;
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
  }

  .release-month-card:hover {
    border-color: rgba(1, 46, 158, .28);
    box-shadow: 0 24px 60px rgba(1, 46, 158, .15);
    color: inherit;
    transform: translateY(-4px);
  }

  .release-month {
    align-self: center;
    color: var(--release-blue);
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 4px;
    line-height: 1.25;
    white-space: nowrap;
  }

  .release-divider {
    align-self: center;
    width: 1px;
    height: 104px;
    border-left: 4px dashed rgba(1, 46, 158, .14);
  }

  .release-features {
    min-width: 0;
    display: grid;
    gap: 14px;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .release-feature-row {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    column-gap: 20px;
    row-gap: 8px;
    min-width: 0;
    min-height: 32px;
    padding: 0;
  }

  .release-feature-tags {
    display: flex;
    flex: 0 1 auto;
    flex-wrap: wrap;
    align-items: center;
    justify-content: flex-end;
    gap: 8px;
    margin-left: auto;
    width: max-content;
    min-width: 0;
    max-width: 100%;
  }

  .release-feature-name {
    flex: 1 1 auto;
    min-width: 0;
    max-width: 100%;
    white-space: normal;
    overflow-wrap: anywhere;
    color: var(--release-text);
    font-size: 17px;
    font-weight: 900;
    letter-spacing: .2px;
    line-height: 1.35;
  }

  .release-version-tag {
    flex: 0 0 auto;
    display: inline-flex;
    align-items: center;
    min-height: 32px;
    padding: 0 12px;
    border: 1px solid rgba(222, 130, 24, .20);
    border-radius: 999px;
    background: rgba(222, 130, 24, .08);
    color: #de8218;
    font-size: 13px;
    font-weight: 900;
    line-height: 1;
    white-space: nowrap;
  }

  .release-version-tag-2 {
    flex: 0 0 auto;
    display: inline-flex;
    align-items: center;
    min-height: 32px;
    padding: 0 12px;
    border: 1px solid rgba(1, 46, 158, .16);
    border-radius: 999px;
    background: rgba(1, 46, 158, .06);
    color: var(--release-blue);
    font-size: 13px;
    font-weight: 900;
    line-height: 1;
    white-space: nowrap;
  }

  .release-arrow {
    display: grid;
    align-self: center;
    place-items: center;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: rgba(1, 46, 158, .06);
    color: var(--release-blue);
    font-size: 38px;
    font-weight: 800;
    line-height: 1;
    transition: .22s ease;
  }

  .release-month-card:hover .release-arrow {
    background: var(--release-blue);
    color: #fff;
    transform: translateX(4px);
  }

  /* Text accents: titles, descriptions, months, feature names, and plan tags. */
  .release-index .release-heading h1,
  .release-index .release-heading p,
  .release-index .release-month,
  .release-index .release-feature-name,
  .release-index .release-version-tag,
  .release-index .release-version-tag-2,
  .release-index .release-arrow {
    text-decoration: none;
  }

  /* Cards are links; remove underlines for links and interactive states. */
  .release-index .release-timeline a.release-month-card,
  .release-index .release-timeline a.release-month-card:link,
  .release-index .release-timeline a.release-month-card:visited,
  .release-index .release-timeline a.release-month-card:hover,
  .release-index .release-timeline a.release-month-card:focus,
  .release-index .release-timeline a.release-month-card:active {
    text-decoration: none;
  }
  @media (max-width: 760px) {
    .release-index {
      padding: 32px 16px 56px;
    }

  .release-hero {
      display: block;
      margin-bottom: 28px;
    }

    .release-heading h1 {
      font-size: 32px;
    }

    .release-heading p {
      font-size: 15px;
    }

    .release-month-card {
      grid-template-columns: 1fr 48px;
      gap: 20px;
      min-height: 0;
      padding: 24px;
      border-radius: 24px;
    }

    .release-month {
      grid-column: 1;
      grid-row: 1;
      font-size: 22px;
      letter-spacing: 3px;
    }

    .release-divider {
      display: none;
    }

    .release-features {
      grid-column: 1 / -1;
      grid-row: 2;
      gap: 12px;
    }

    .release-feature-row {
      column-gap: 10px;
      row-gap: 6px;
      min-height: 29px;
    }

    .release-feature-tags {
      gap: 6px;
    }

    .release-feature-name {
      font-size: 15px;
    }

    .release-version-tag {
      min-height: 29px;
      padding-right: 9px;
      padding-left: 9px;
      font-size: 12px;
    }

    .release-version-tag-2 {
      min-height: 29px;
      padding-right: 9px;
      padding-left: 9px;
      font-size: 12px;
    }

    .release-arrow {
      grid-column: 2;
      grid-row: 1;
      width: 48px;
      height: 48px;
      font-size: 30px;
    }
  }
</style>

<div class="release-index">
  <div class="release-hero">
    <div class="release-heading">
      <h1>Release Notes</h1>
      <p>See the latest shipped features and improvements—CYBERBIZ grows with you</p>
    </div>
  </div>

  <div>
    <div class="release-timeline">
      <a class="release-month-card" href="2026-10.md">
        <div class="release-month">2026 / October updates</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">Entrance animations for homepage blocks</span>
            <span class="release-feature-tags">
              <span class="release-version-tag-2">#Drag-and-drop theme</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Print EZCAT order shipping documents directly</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Storefront site search (magnifier) improvements</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Bot protection for member signup SMS verification codes</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-09.md">
        <div class="release-month">2026 / September updates</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">Shopee order sync and batch shipping #ALPHA</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
              <span class="release-version-tag">#PLUS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Request a new convenience store shipping note number after it expires</span>
            <span class="release-feature-tags">
              <span class="release-version-tag-2">#CYBERBIZ PAYMENTS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Statements include LINE Pay payout details</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
              <span class="release-version-tag">#PLUS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Convenience store code payments</span>
            <span class="release-feature-tags">
              <span class="release-version-tag-2">#CYBERBIZ PAYMENTS</span>
            </span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-08.md">
        <div class="release-month">2026 / August updates</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">Pinned announcements｜Multi-slot scheduled carousel</span>
            <span class="release-feature-tags">
              <span class="release-version-tag-2">#Drag-and-drop theme</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">CHAT BOX｜Mobile admin view</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
              <span class="release-version-tag">#PLUS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Choose auto-refund for overdue convenience-store pickup orders</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
              <span class="release-version-tag">#PLUS</span>
              <span class="release-version-tag-2">#CYBERBIZ PAYMENTS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Edit in-progress store-wide coupons</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
            </span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-07.md">
        <div class="release-month">2026 / July updates</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">CHAT BOX｜Unified chat entry on the brand site</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
              <span class="release-version-tag">#PLUS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Shopper buy-again</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Custom layouts support multi-column mobile display</span>
            <span class="release-feature-tags">
              <span class="release-version-tag-2">#Drag-and-drop theme</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Edit in-progress coupons</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
            </span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-06.md">
        <div class="release-month">2026 / June updates</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">Spend/quantity gifts support member segments</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">VIP tiers support no-expiry settings</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Checkout auto-fill bonus pointsswitch</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Desktop product-image hover effects: more pages supported</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>

      <a class="release-month-card" href="2026-05.md">
        <div class="release-month">2026 / May updates</div>
        <div class="release-divider" aria-hidden="true"></div>
        <ul class="release-features">
          <li class="release-feature-row">
            <span class="release-feature-name">CHAT BOX messaging hub</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
              <span class="release-version-tag">#PLUS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Bundles support fixed and pick-any sections together</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Launch 7-ELEVEN C2C returns from the admin</span>
            <span class="release-feature-tags">
              <span class="release-version-tag-2">#CYBERBIZ PAYMENTS</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Spend/quantity gifts let shoppers pick gift variants</span>
            <span class="release-feature-tags">
              <span class="release-version-tag">#Enterprise</span>
            </span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Storefront navigation supports font-size settings</span>
          </li>
          <li class="release-feature-row">
            <span class="release-feature-name">Storefront product-image corner radius</span>
          </li>
        </ul>
        <span class="release-arrow" aria-hidden="true">›</span>
      </a>
    </div>
  </div>
</div>





