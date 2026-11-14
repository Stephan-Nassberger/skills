---
name: planner-development
description: "Develop Microsoft Planner basic-plan integrations through Microsoft Graph, including tasks, buckets, details, assignments and concurrency. Verify premium-plan paths separately."
license: MIT
metadata:
  version: "0.1.0"
---

# Planner Development

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Determine basic versus premium plan, container, tenant and intended caller. Check the current Planner API scope; do not assume Graph Planner endpoints cover premium plans.
2. Verify each operation, API version, delegated/application permission support and resource ID in current Graph documentation. Support is endpoint-specific; never generalize that Planner is delegated-only or that every endpoint supports app-only.
3. Model plans, buckets, tasks and task details separately. Read the exact assignment/checklist/reference schema before creating payloads. Resolve identities from authorized directory data.
4. Follow pagination and throttling guidance. Before an update, obtain the relevant resource ETag and use the documented If-Match contract. On conflict, reread and reconcile; do not overwrite another user's changes blindly.
5. Avoid duplicate tasks on retry by recording a stable source-to-task mapping. Treat creation, assignment and notification as separate effects where applicable.
6. Return endpoint/permission evidence, payloads, mapping and conflict handling. Test creation/readback, duplicate retry, permission denial and concurrent modification only within authorized scope. Use the documented alternative for premium plans instead of fabricating Graph endpoints.

## Sources to consult

- https://learn.microsoft.com/graph/api/resources/planner-overview
- https://learn.microsoft.com/graph/api/resources/planner-task

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
