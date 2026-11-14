---
name: adaptive-cards-m365
description: "Design and validate Adaptive Cards for Teams, Power Automate or SPFx Adaptive Card Extensions with host-specific actions and data binding."
license: MIT
metadata:
  version: "0.1.0"
---

# Adaptive Cards M365

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Name the exact host and delivery path: Teams bot, Power Automate post-and-wait, Outlook, Copilot or SPFx ACE. Determine its supported card version and action capabilities from current host documentation; a designer preview does not establish host support.
2. Separate card JSON, template expressions, sample data and the receiving action handler. Do not confuse SharePoint list-formatting JSON with Adaptive Card schema.
3. Choose only actions the host supports. Action.Submit, Action.Execute, refresh and authentication are not interchangeable. Define input IDs, validation, submit payload, authorization and replay/idempotency behavior at the handler.
4. Never trust client-submitted user IDs, permissions, prices or record ownership. Recheck identity and authorization server-side. Keep secrets and private data out of hidden card data.
5. Build accessible text with wrap, meaningful labels, alt text and a readable fallback. Check long/localized content, empty fields, mobile widths and host themes. Treat data binding and escaping as part of the implementation.
6. Return JSON, sanitized sample data, expected submit payload and handler contract. Validate against the schema and test the actual host, including duplicate submission and expired actions. For an ACE, verify the installed SPFx ACE lifecycle separately.

## Sources to consult

- https://learn.microsoft.com/adaptive-cards/
- https://learn.microsoft.com/microsoftteams/platform/task-modules-and-cards/cards/cards-reference
- https://learn.microsoft.com/sharepoint/dev/spfx/viva/overview-viva-connections

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
