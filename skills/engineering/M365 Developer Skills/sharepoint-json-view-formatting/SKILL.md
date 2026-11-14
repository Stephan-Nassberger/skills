---
name: sharepoint-json-view-formatting
description: "Create and debug SharePoint and Microsoft Lists JSON view formatting for rows, tiles and supported layout surfaces. Not single-column formatting or Power Apps forms."
license: MIT
metadata:
  version: "0.1.0"
---

# Sharepoint Json View Formatting

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Identify the host version, list/library, view layout, field internal names and desired row/tile behavior. Export the existing formatter and view configuration before editing.
2. Consult the current view-formatting documentation and choose the schema for the actual layout. Distinguish additionalRowClass from rowFormatter and tile formatting. Do not assume column schema accepts view properties.
3. Prefer additionalRowClass for simple row highlighting; introduce a rowFormatter only when the requested structure needs it. Preserve useful links, selection behavior and existing actions.
4. Reference actual internal names and data types. Confirm referenced fields are available in the view. Use documented expressions for people, lookups, multi-values and dates, including empty-value handling.
5. Use supported customRowAction definitions and documented grouping/header features only for the chosen layout. No JavaScript, unsupported event handlers or SharePoint DOM selectors. A formatter does not grant access or change stored data.
6. Deliver the formatter and required view fields/layout together. Validate JSON and the correct schema, then test representative populated/empty rows, grouping, links, keyboard interaction, themes and narrow screens in the target host. Restore the exported formatter if the change breaks selection or navigation.

## Sources to consult

- https://learn.microsoft.com/sharepoint/dev/declarative-customization/view-formatting
- https://learn.microsoft.com/sharepoint/dev/declarative-customization/formatting-syntax-reference
- https://github.com/pnp/List-Formatting

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
