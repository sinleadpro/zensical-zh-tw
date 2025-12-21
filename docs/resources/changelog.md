---
title: 更新紀錄
icon: lucide/history
---


# 更新紀錄

## EC

### 9.7.0 <small>November 11, 2025</small> { id="9.7.0" }

This release includes all features that were previously exclusive to the
Insiders edition. These features are now freely available to everyone.

__Note on deprecated plugins__: The [projects] and [typeset] plugins are
included in this release, but must be considered deprecated. Both plugins
proved unsustainable to maintain and represent architectural dead ends. They
are provided as-is without ongoing support.

__Changes__:

- Added support for projects plugin (for compat, now deprecated)
- Added support for typeset plugin (for compat, now deprecated)
- Added support for pinned blog posts and author profiles
- Added support for customizing pagination for blog index pages
- Added support for customizing blog category sort order
- Added support for staying on page when switching languages
- Added support for disabling tags in table of contents
- Added support for nested tags and shadow tags
- Added support for footnote tooltips
- Added support for instant previews
- Added support for instant prefetching
- Added support for custom social card layouts
- Added support for custom social card background images
- Added support for selectable rangs in code blocks
- Added support for custom selectors for code annotations
- Added support for configurable log level in privacy plugin
- Added support for processing of external links in privacy plugin
- Added support for automatic image optimization via optimize plugin
- Added support for navigation paths (breadcrumbs)
- Fixed #8519: Vector accents do not render when using KaTeX

  [Zensical]: https://zensical.org
  [Read the full announcement on our blog]: ../blog/posts/zensical.md
  [projects]: ../plugins/projects.md
  [typeset]: ../plugins/typeset.md

### 9.6.23 <small>November 1, 2025</small> { id="9.6.23" }

- Updated Burmese translation

### 9.6.22 <small>October 15, 2025</small> { id="9.6.22" }

- Updated Georgian translation

### 9.6.21 <small>September 30, 2025</small> { id="9.6.21" }

- Updated Serbian translations
- Fixed #8458: Temporary pin of click dependency

### 9.6.20 <small>September 15, 2025</small> { id="9.6.20" }

- Fixed #8446: Deprecation warning as of Python 3.14 in Emoji extension
- Fixed #8440: `&` character not escaped in search highlighting
- Fixed #8439: FontAwesome icons color not set in social cards (regression)

### 9.6.19 <small>September 7, 2025</small> { id="9.6.19" }

- Added support for Python 3.14
- Updated Bahasa Malaysia translations

### 9.6.18 <small>August 22, 2025</small> { id="9.6.18" }

- Updated Azerbaijani translations
- Fixed last compat issues with [minijinja], now 100% compatible

### 9.6.17 <small>August 15, 2025</small> { id="9.6.17" }

- Fixed #8396: Videos do not autoplay when inside a content tab
- Fixed #8394: Stroke width not effective in Mermaid.js diagrams
- Fixed disappearing version selector when hiding page title

### 9.6.16 <small>July 26, 2025</small> { id="9.6.16" }

- Fixed #8349: Info plugin doesn't correctly detect virtualenv in some cases
- Fixed #8334: Find-in-page detects matches in hidden search result list

### 9.6.15 <small>July 1, 2025</small> { id="9.6.15" }

- Updated Mongolian translations
- Improved semantic markup of "edit this page" button
- Improved info plugin virtual environment resolution
- Fixed #8291: Large font size setting throws of breakpoints in JavaScript

### 9.6.14 <small>May 13, 2025</small> { id="9.6.14" }

- Fixed #8215: Social plugin crashes when CairoSVG is updated to 2.8

### 9.6.13 <small>May 10, 2025</small> { id="9.6.13" }

- Fixed #8204: Annotations showing list markers in print view
- Fixed #8153: Improve style of cardinality symbols in Mermaid.js ER diagrams

### 9.6.12 <small>April 17, 2025</small> { id="9.6.12" }

- Fixed #8158: Flip footnote back reference icon for right-to-left languages

### 9.6.11 <small>April 1, 2025</small> { id="9.6.11" }

- Updated Docker image to latest Alpine Linux
- Bump required Jinja version to 3.1
- Fixed #8133: Jinja filter `items` not available (9.6.10 regression)
- Fixed #8128: Search plugin not entirely disabled via enabled setting

### 9.6.10 <small>March 30, 2025</small> { id="9.6.10" }

This version is a pure refactoring release, and does not contain new features
or bug fixes. It strives to improve the compatibility of our templates with
alternative Jinja-like template engines that we're currently exploring,
including [minijinja].

Additionally, it replaces several instances of Python function invocations
with idiomatic use of template filters. All instances where variables have
been mutated inside templates have been replaced. Most changes have been made
in partials, and only a few in blocks, and all of them are fully backward
compatible, so no changes to overrides are necessary.

Note that this release does not replace the Jinja template engine with
minijinja. However, our templates are now 99% compatible with minijinja,
which means we can explore alternative Jinja-compatible implementations.
Additionally, immutability and removal of almost all Python function
invocations means much more idiomatic templating.

  [minijinja]: https://github.com/mitsuhiko/minijinja

## POS

## WMS