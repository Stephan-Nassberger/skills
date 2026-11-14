---
name: power-apps-development
description: "Build and review Power Apps canvas and model-driven apps, Power Fx, SharePoint forms, delegation and solution ALM using the actual authoring tools available."
license: MIT
metadata:
  version: "0.1.0"
---

# Power Apps Development

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Identify canvas, model-driven, code app or SharePoint-integrated form, along with environment, data sources and existing solution. Preserve existing app/control names and bindings during focused changes.
2. Inspect current control metadata and connector schemas before writing properties or formulas. If a Canvas Authoring MCP server is unavailable, provide verifiable formulas and instructions instead of claiming to have authored or compiled an app.
3. For SharePoint forms, handle new/edit/view integration and record identity explicitly. Verify internal field names, person/lookup/choice shapes, required fields and attachments rather than converting every value to text.
4. Check delegation for each formula against the actual data source. Never use the local row limit as a fix for incomplete results. Use delegable filters, explicit sort/search behavior and test data larger than the limit.
5. Use clear loading, empty, error and save states. Keep authorization in the data source; hidden controls and client variables are not access controls. Use accessible controls and responsive containers within the installed app generation.
6. For model-driven apps, design Dataverse tables, relationships, forms, views and security separately from canvas formulas. Use PCF only when a concrete requirement exceeds supported controls; verify PAC and framework versions.
7. Deliver the smallest app delta, formulas, data contracts and test steps. Run the available compiler/checker, verify read/write behavior and required-field errors with real non-production data. Document save, publish and share as separate outcomes.

## Sources to consult

- https://learn.microsoft.com/power-apps/maker/canvas-apps/
- https://learn.microsoft.com/power-apps/maker/model-driven-apps/
- https://github.com/microsoft/power-platform-skills

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
