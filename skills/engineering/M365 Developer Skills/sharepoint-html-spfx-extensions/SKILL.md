---
name: sharepoint-html-spfx-extensions
description: "Choose and implement supported SharePoint HTML rendering and SPFx Application Customizer, Field Customizer, Command Set or Form Customizer extensions."
license: MIT
metadata:
  version: "0.1.0"
---

# Sharepoint Html Spfx Extensions

Original skill authored for this collection, 2026-11-14. Documentation-informed; not copied from the linked documentation. Static review only; no tenant behavior certification.

## Workflow

1. Identify the requested surface: page web part, site-wide header/footer, field rendering, list command or list form. Inspect existing SPFx version, registration, activation scope and package identity.
2. Choose a supported extension point: Application Customizer placeholders for header/footer, Field Customizer for rich field rendering, ListView Command Set for actions, Form Customizer for full form behavior, or a web part for page content. Simple declarative presentation may fit native JSON formatting instead.
3. Use the existing SPFx skill for scaffolding, toolchain and package compatibility. Do not assume arbitrary HTML/script can be pasted into modern SharePoint or mutate undocumented SharePoint DOM to implement a supported extension.
4. For Application Customizers, handle placeholder availability, navigation events and disposal; avoid duplicate React mounts, event handlers or CSS leakage across client navigation. Use installed public SPFx APIs and scoped styles.
5. Sanitize untrusted rich text with an established, project-compatible sanitizer. Do not interpolate raw user HTML, disable escaping, embed secrets or bypass CSP. Verify iframe embedding restrictions separately from SPFx rendering.
6. Preserve solution/component IDs and existing tenant/site/list registration scope. For list extensions, verify the content type, field or command registration and avoid widening activation to all sites.
7. Deliver source, package/build evidence and explicit activation/rollback steps. Test navigation and disposal, read-only users, themes and missing placeholders. Building a package is not App Catalog deployment; deploy only with explicit authorization.

## Sources to consult

- https://learn.microsoft.com/sharepoint/dev/spfx/extensions/overview-extensions
- https://learn.microsoft.com/sharepoint/dev/spfx/extensions/get-started/using-page-placeholder-with-extensions

Consult current primary documentation for the target version before implementation. Report actual validation and remaining limitations; instructions do not supply credentials, permissions or runtime tools.
