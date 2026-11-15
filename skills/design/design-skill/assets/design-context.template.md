---
system_name: ""
system_character: ""
product_context: ""
target_framework: ""

design_doc: ""
tokens_css: ""
tokens_entry_css: ""
component_dirs: []
content_sources: []

css_framework: ""
package_manager: ""
output_dir: "design-mockups"
dark_mode: ""
build_command: ""

font_text: ""
font_numeric: ""
base_font_size: ""

icon_library: ""
icon_browse_url: ""
icon_banned: []

color_primary_token: ""
color_accent_token: ""
neutral_hue: ""
radius_scale: ""
elevation_rule: ""
spacing_scale: ""
---

# Design context

Binding file for the `design` skill. The skill reads this before every artifact; each
double-braced name referenced in `SKILL.md` and the procedure files resolves from the
frontmatter above or the sections below.

Regenerate or update it by asking the skill to **re-run the design setup wizard**.

## Rejects

Looks this system explicitly rejects. Each is a defect on sight, not a judgment call.
The skill flags these during `ai-slop-check.md` and `polish-pass.md`.

- Side-stripe borders — a `border-l-4` colored stripe used as the default card or alert treatment
- `background-clip: text` gradient text
- Glassmorphism — `backdrop-blur` on decorative cards, neon-on-black, hero gradients
- Raw palette classes that break dark-mode parity (`bg-gray-200`, `text-blue-500`, `dark:bg-gray-700`)
- Pure `#FFFFFF` / `#000000` where a toned token exists
- Off-scale spacing (`padding: 7px`, `margin: 18px`, `gap: 13px`)

<!-- Add the looks specific to this product. Examples of the shape to write:
- Hero-metric dashboards — giant number + colored ring + "↑12% from last week"
- Warm-editorial template look — cream background, serif display, terracotta accents
- 2010s enterprise chrome — gradient module tabs, treetable affordances
-->

## Signature patterns

Named components and layout shapes a mockup must reproduce rather than reinvent. Give the
component name, where it lives, and the shape in one line each.

<!-- Examples of the shape to write:
- `PageShell` (components/layout/) — panel-on-substrate; every routed page sits inside it
- `DataTable` (components/table/) — never a raw <table> for record lists
- Section card — muted-band header (`bg-muted rounded-t-xl border-b px-4 py-2`) over a bordered body
-->

## UX nuances

Product-specific conventions that override the general design rules. These are the details
that make a mockup read as *this* app rather than a generic one.

<!-- Examples of the shape to write:
- Routed pages render no visible page-title heading — the breadcrumb is the title. Mockups use a
  visually-hidden <h1> and start visible headings at the in-panel section level.
- Success/error feedback is a toast, never an inline banner.
- Navigation is a persistent left sidebar plus a breadcrumb header; mockups reproduce both.
-->

## State contract

The interactive-state conventions for this system. `interaction-states-pass.md` verifies
against these exact values.

<!-- Examples of the shape to write:
- Hover (outline/ghost): `bg-accent`. No transform, no lift — flat at rest.
- Active / pressed: `opacity-60`.
- Disabled: opacity ~0.6 + `cursor: not-allowed`, no hover effect.
- Focus: `ring-[3px]` at `--ring/50`; inputs also add `border-ring`. Never `outline: none` alone.
- Transition: `transition-all` at 0.15–0.3s ease.
-->

## Real-content sources

Where the mockup's navigation labels, entity names, and product taxonomy come from. Labels
and terms are lifted from these files, never invented. Sample *data values* may be realistic
stand-ins; labels, names, and terms may not.

<!-- List the route registry, nav/menu components, and any copy or i18n catalog. -->

## Unresolved

Anything the wizard could not determine and the user has not yet answered. The skill surfaces
these instead of guessing. Delete entries as they are resolved.
