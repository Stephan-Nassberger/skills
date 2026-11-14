---
name: azure-functions-m365
description: "Build and troubleshoot Azure Functions backends for Microsoft 365 integrations, Graph webhooks, timers and queue-based processing."
license: MIT
metadata:
  version: "0.1.0"
---

# Azure Functions M365

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Inspect runtime/language, programming model, hosting plan and existing project. Use supported versions and official migration guidance; do not mix Node programming models or .NET in-process and isolated worker examples.
2. Specify the trigger, input contract, caller identity and downstream permissions. Use managed identity for suitable app-only Azure workloads; use OBO when delegated user context is required. Verify endpoint permission support before choosing authentication.
3. Function keys are not user authorization. Validate Entra tokens and the intended audience/roles when serving protected app requests. Use Key Vault or supported configuration for secrets; never commit local.settings.json.
4. For Graph webhooks, verify the validation handshake, clientState, subscription expiry and renewal from the current API reference. Validate notifications and queue work promptly; process duplicates idempotently and account for out-of-order events.
5. Choose timeouts, retries, poison/dead-letter handling and concurrency for the actual trigger and hosting plan. Avoid retrying non-idempotent Graph writes without a deduplication strategy. Handle 429 and Retry-After.
6. Keep logs useful without tokens or private payloads. Add correlation IDs and actionable failure records. Use local mocks or a permitted test subscription to verify auth failure, duplicate input and downstream throttling.
7. Deliver focused code/config changes, local test results, required settings and deployment/rollback instructions. Resource provisioning, consent and production deployment require authorization beyond merely preparing source.

## Sources to consult

- https://learn.microsoft.com/azure/azure-functions/functions-overview
- https://learn.microsoft.com/graph/change-notifications-overview
- https://learn.microsoft.com/azure/azure-functions/functions-reference

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
