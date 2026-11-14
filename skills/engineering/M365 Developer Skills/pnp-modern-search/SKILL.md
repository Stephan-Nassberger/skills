---
name: pnp-modern-search
description: "Configure and troubleshoot PnP Modern Search v4 web parts, KQL, managed properties, filters and Handlebars layouts. Not Microsoft Search administration in general."
license: MIT
metadata:
  version: "0.1.0"
---

# Pnp Modern Search

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Inventory the installed Modern Search package version, SharePoint host, web-part properties and reproduction. Use documentation matching that version; do not mix v3 layouts with v4 configuration.
2. Reproduce the query with the same signed-in identity. Separate missing indexed content, access trimming, query syntax, result-source scope and rendering defects. Never suggest changing permissions merely to make a result visible.
3. For a missing field, trace source column -> crawled property -> managed property -> query selection -> result slot -> template binding. Check searchable/queryable/retrievable/refinable requirements separately. Schema changes and reindexing take time; report indexing uncertainty.
4. Inspect connections among Search Box, Results, Filters and Verticals, including dynamic data and URL/query-string inputs. Keep a known-working query and property export before changing connections.
5. Build the smallest Handlebars layout against a sanitized real result shape. Escape user data; do not use unescaped HTML for untrusted values. Use only helpers and web components documented for the installed version.
6. For extensibility, distinguish layout templates from a custom extensibility library, data source or web component. Verify the exact package interface and SPFx compatibility before coding.
7. Deliver the property delta, KQL, selected properties, slot mapping and layout together. Test no results, missing metadata, multiple verticals, mobile layout and an identity with fewer permissions. Mark tenant checks unexecuted when unavailable.

## Sources to consult

- https://microsoft-search.github.io/pnp-modern-search/
- https://github.com/microsoft-search/pnp-modern-search

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
