#!/usr/bin/env python3
"""
Restructure ec/marketing/ docs into subdirectories matching index.md categories.
Moves files, updates permalinks, fixes all cross-references.
"""
import os
import re
import sys

MARKETING = os.path.join(
    "/Users/jason.ke/Documents/DocCenter/zensical-zh-tw",
    "docs/ec/marketing"
)

# filename -> target subdirectory
MOVE_MAP = {
    "flash-sale-single-product.md": "discounts",
    "mix-and-match-discounts.md": "discounts",
    "red-and-green-bundle-discounts.md": "discounts",
    "threshold-gifts-and-quantity-gifts.md": "discounts",
    "multi-level-category-discount.md": "discounts",
    "checkout-discount-calculation-order.md": "discounts",
    "setup-product-upsell.md": "upsells",
    "setup-order-upsell.md": "upsells",
    "setup-bonus-points.md": "bonus-and-gifts",
    "bonus-point-mall.md": "bonus-and-gifts",
    "setup-registration-gift.md": "bonus-and-gifts",
    "setup-birthday-gift.md": "bonus-and-gifts",
    "limited-time-first-purchase-gift.md": "bonus-and-gifts",
    "send-coupons-for-specific-products.md": "conditional-send",
    "send-bonus-points-for-specific-products.md": "conditional-send",
    "send-bonus-points-for-specific-payment-methods.md": "conditional-send",
    "send-bonus-points-for-specific-logistics.md": "conditional-send",
    "send-event-serials-for-specific-products.md": "conditional-send",
    "exclude-products-from-promotions.md": "purchase-restrictions",
    "purchase-limit.md": "purchase-restrictions",
    "coupon-and-bonus-points-expiry-notification.md": "purchase-restrictions",
    "one-page-store.md": "one-page-store",
    "one-page-store-youtube-autoplay.md": "one-page-store",
    "create-cart-link-specific-products.md": "one-page-store",
    "interactive-games.md": "other-tools",
    "subscription-campaign-page.md": "other-tools",
}


def fix_all_links(content, own_subdir):
    """Fix every markdown link in the file for the depth change."""

    def replace_link(match):
        target = match.group(1)

        # Skip non-relative links
        if target.startswith("#") or target.startswith("http"):
            return match.group(0)

        # Strip ./ prefix
        clean = target[2:] if target.startswith("./") else target

        # Pattern A: starts with ../ — add one more ../
        if clean.startswith("../"):
            return f"](../../{clean[3:]})"

        # Pattern B: in a known subdirectory (coupon/, references/)
        if clean.startswith("coupon/") or clean.startswith("references/"):
            return f"](../{clean})"

        # Pattern C: same-directory link to a file being moved
        for f, s in MOVE_MAP.items():
            if clean == f:
                if s == own_subdir:
                    return f"]({f})"  # same subdir
                else:
                    return f"](../{s}/{f})"  # different subdir

        # Pattern D: same-directory link to a root-level file
        return f"](../{clean})"

    return re.sub(r'\]\(([^)]+)\)', replace_link, content)


def fix_wikilinks(content, own_subdir):
    """Fix wikilinks [[target]] in frontmatter."""

    def replace_wiki(match):
        target = match.group(1)
        if "/" in target:
            return match.group(0)  # already has path

        for f, s in MOVE_MAP.items():
            stem = f.replace(".md", "")
            if target == stem:
                if s == own_subdir:
                    return f"[[{target}]]"
                else:
                    return f"[[{s}/{target}]]"
        return match.group(0)

    return re.sub(r'\[\[([^\]]+)\]\]', replace_wiki, content)


def update_permalink(content, filename, subdir):
    stem = filename.replace(".md", "")
    old = f"permalink: https://help.cyberbiz.io/ec/marketing/{stem}"
    new = f"permalink: https://help.cyberbiz.io/ec/marketing/{subdir}/{stem}"
    content = content.replace(old, new)
    # Handle empty permalink:
    content = re.sub(
        r'^permalink:\s*$',
        f'permalink: https://help.cyberbiz.io/ec/marketing/{subdir}/{stem}',
        content,
        flags=re.MULTILINE
    )
    return content


def main():
    errors = []

    for filename, subdir in MOVE_MAP.items():
        old_path = os.path.join(MARKETING, filename)
        new_path = os.path.join(MARKETING, subdir, filename)

        if not os.path.exists(old_path):
            errors.append(f"NOT FOUND: {old_path}")
            continue

        print(f"  {filename} → {subdir}/")

        with open(old_path, encoding="utf-8") as f:
            content = f.read()

        content = update_permalink(content, filename, subdir)
        content = fix_wikilinks(content, subdir)
        content = fix_all_links(content, subdir)

        with open(new_path, "w", encoding="utf-8") as f:
            f.write(content)

        os.remove(old_path)

    if errors:
        print("\n❌ ERRORS:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)

    print(f"\n✅ All {len(MOVE_MAP)} files moved successfully.")


if __name__ == "__main__":
    main()
