---
name: sharepoint-json-column-formatting
description: "Create, review and troubleshoot SharePoint and Microsoft Lists JSON column formatting, field expressions and supported actions. Use view-formatting for whole rows or tiles."
license: MIT
metadata:
  version: "0.1.0"
---

# Sharepoint Json Column Formatting

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Obtain the column type, internal name, sample values, other referenced field types and target host (SharePoint Online or an exact server version). Formatting changes presentation, not stored values or permissions.
2. Read the current Microsoft column-formatting reference and syntax reference. Select the schema for the actual host. Use the column-formatting schema for a field formatter; do not paste a view formatter into a column.
3. Use @currentField for the formatted field and [$InternalName] for other fields, confirming internal names and inclusion in the view where required. Treat people, lookup and multi-value fields according to their actual shapes; never assume display strings.
4. Build a minimal elmType tree using documented attributes, style expressions and supported actions. JSON is not arbitrary HTML, CSS or JavaScript. Never insert script, event-handler code or unsupported DOM access.
5. Handle empty values and type differences explicitly. Compare numbers as numbers; confirm date conversion, time zone and locale behavior from the reference. Do not compose an unsupported expression from JavaScript syntax.
6. For executeFlow or other customRowAction operations, verify action parameters and the target flow/list; formatting itself does not authorize running a flow or updating an item.
7. Return valid JSON plus where to paste it and the internal-name assumptions. Parse JSON and validate against the chosen schema. Preview with empty, long, zero/negative and multi-value data as applicable; check keyboard labels, contrast and theme. Schema validation alone does not prove rendering.

## Sources to consult

- https://learn.microsoft.com/sharepoint/dev/declarative-customization/column-formatting
- https://learn.microsoft.com/sharepoint/dev/declarative-customization/formatting-syntax-reference
- https://github.com/pnp/List-Formatting

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
