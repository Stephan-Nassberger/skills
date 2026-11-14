---
name: microsoft-forms-integration
description: "Integrate Microsoft Forms responses with Power Automate and SharePoint using documented connectors, ownership and response mappings. Not a promise of a public Forms authoring API."
license: MIT
metadata:
  version: "0.1.0"
---

# Microsoft Forms Integration

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Identify the form owner/group, organizational account, trigger flow, response destination and required questions. Separate creating a form from consuming its responses.
2. Check the current Forms connector actions and limitations. Use the documented response trigger and response-detail action when supported. Do not invent Microsoft Graph Forms CRUD endpoints or reuse undocumented browser network APIs as supported integrations.
3. Group forms may require the explicit form ID rather than a dropdown selection. Resolve the actual ID and access before configuring the flow; do not assume a missing dropdown means the form does not exist.
4. Map stable question identifiers to destination fields and retain response ID as the deduplication key. Handle unanswered questions, multiple selections, anonymous respondents and date/number locale explicitly.
5. Inspect the actual file-upload response shape and OneDrive/SharePoint storage permissions. Do not assume a respondent email exists or publish uploaded-file links beyond the requested audience.
6. Deliver mappings, expressions, connector prerequisites and repeatable tests. Verify duplicate delivery, optional answers and ownership changes. If form authoring is not exposed by a supported tool, provide manual setup instructions and state that no form was created.

## Sources to consult

- https://learn.microsoft.com/connectors/microsoftforms/
- https://learn.microsoft.com/power-automate/forms/overview

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
