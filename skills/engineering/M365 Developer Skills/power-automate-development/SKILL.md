---
name: power-automate-development
description: "Design, review and troubleshoot Power Automate cloud flows, SharePoint integrations, expressions, connection references and solution ALM. Not unattended deployment without authorized environment access."
license: MIT
metadata:
  version: "0.1.0"
---

# Power Automate Development

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Identify the environment, owner, existing solution/flow, trigger, connectors and licensing. Export or inspect the current definition when editing; preserve connection references and environment variables.
2. Discover exact trigger/action schemas through the installed supported connector tooling or Microsoft connector documentation. Do not invent connector operation IDs or assume a generic Logic Apps action is accepted unchanged by Power Automate.
3. Specify expressions, input/output shapes, null handling, pagination and concurrency explicitly. Verify internal SharePoint field names. Prevent update-trigger loops with precise trigger conditions or a state transition.
4. Make external side effects idempotent. Handle duplicate triggers and partial failure using a business key or recorded operation state. Distinguish transient retries from authentication or validation failures; use scopes/run-after for error reporting.
5. For approvals or post-and-wait cards, account for timeouts and durable state. For child flows, confirm solution requirements, trigger type and connection behavior in current documentation.
6. Use solution-aware flows, connection references and environment variables where the project requires ALM. Check DLP and premium requirements without treating this skill as a license entitlement.
7. Deliver the flow design or focused definition change, connections, test payloads and rollback steps. Creation, enabling and running are distinct external actions; perform only authorized ones and read back saved state. A successful import does not prove a trigger ran.

## Sources to consult

- https://learn.microsoft.com/power-automate/
- https://learn.microsoft.com/connectors/
- https://github.com/microsoft/power-platform-skills

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
