# Write Design Doc: Derive a Design System Document from the Code

Produce the design document that `{{design_doc}}` points at — the source of truth for *intent* that sits above the token file's *values*. Run this from the setup wizard when a project has tokens but no design doc (Path B), or when a greenfield project has just agreed a starter system (Path C).

**Derive, don't invent.** Every statement in this document must trace to a file you read — a token definition, a component's class list, a config value. A design doc full of plausible-sounding assertions is worse than no design doc, because the skill will then enforce them.

**Mark what you couldn't determine.** A section that says "not established — decide before this is enforced" is honest and useful. A section that quietly makes something up corrupts every artifact and every review that follows.

## Phase 1: Read the sources

Read, concurrently:

- `{{tokens_css}}` end to end — every custom property in every scope. This is the value inventory.
- The framework config (`tailwind.config.*`, `@theme` block) — the scales: spacing, radius, font families, breakpoints.
- Six to ten real components from `{{component_dirs}}`, chosen to span the vocabulary: button, input, card/panel, table, navigation, dialog/popover, badge/status. Read their actual class strings — that's where the real conventions live.
- Any font loading (`@font-face`, framework font imports, webfont links).
- A route or page component, to see how the pieces compose into a screen.

## Phase 2: Extract the inventory

Build these lists before writing prose. Each entry carries the file it came from.

**Color tokens.** Every token, grouped by role: surfaces (background, card, popover, sidebar), text (foreground, muted-foreground), interactive (primary, secondary, accent, ring), semantic (destructive, success, warning, info), data-viz scales. Record light and dark values side by side. Note the color space and, if neutrals are tinted toward a hue, that hue.

**Type.** The faces and what each is for. Whether a separate numeral face exists. The size scale and which sizes appear in which roles. Base body size.

**Geometry.** Radius scale, spacing scale, border widths, and whether elevation comes from shadow or from tonal layering — read this off the card and dialog components rather than assuming.

**States.** From the button and input components: the exact hover, active/pressed, focus, and disabled treatments, plus transition property and duration. These become the State contract.

**Components.** The named shapes a mockup must reproduce: what it's called, where it lives, and its structural signature in one line.

## Phase 3: Infer the aesthetic direction

This is the one section that is judgment rather than extraction — so ground it and label it.

From the inventory, characterize the system: is it flat or elevated, dense or airy, restrained or saturated, neutral or warm? Point at the evidence ("elevation is tonal — no shadow utilities appear on any card component; depth comes from `bg-muted` over `bg-background`").

Then state what the system therefore **rejects**. Rejects derived from real constraints are the most valuable thing in this document, because they're what the review passes enforce. A system with tinted neutrals rejects raw gray. A flat system rejects shadow-at-rest and hover lift. A system with one reserved accent rejects a second one.

Bring the user's answers from the wizard's identity round — the system name and character line — into this section verbatim. They are the human intent this document exists to record.

## Phase 4: Write the document

Structure, in this order:

1. **Aesthetic direction** — name, character, the evidence, and the Rejects list.
2. **Color** — the token table by role, light and dark, with the tint rule and the reserved-accent rule stated as rules.
3. **Typography** — faces, roles, scale, base size, numeral handling.
4. **Geometry and elevation** — radius, spacing, borders, and how depth is expressed.
5. **Component patterns** — the named shapes, each with location and structural signature.
6. **Interactive states** — the full contract, as concrete values.
7. **Do's and don'ts** — short, concrete, each traceable to something above.

Write it for an agent to read and apply, not for a designer to be inspired by:

- Quote real token names, class strings, and file paths; don't describe them.
- Rules in one or two lines. No preamble, no persuasion.
- Examples only where the rule is ambiguous without one.
- Every unresolved item explicitly marked, in place.

## Phase 5: Confirm before writing to disk

Show the user the proposed path (`DESIGN.md` at the repo root unless they say otherwise) and a compact outline — the section headings plus the Rejects list, since that's the part that will be enforced.

Get their confirmation, then write it. This creates a new file in their repo that other tools and humans will treat as authoritative; it is theirs to approve.

If they decline, keep the derived inventory in the binding file's prose sections instead — `## Rejects`, `## Signature patterns`, `## State contract` — so the work isn't lost, and set `design_doc` to empty.

## Phase 6: Wire it back

After writing:

- Set `design_doc` in `.claude/design-context.md` to the new path.
- Fill `## Rejects`, `## Signature patterns`, and `## State contract` from the same inventory, so the binding file and the design doc agree.
- List every "not established" item under `## Unresolved`.

## Phase 7: Report

- Where the doc was written, and its section count.
- The Rejects list — this is what the review passes will now enforce, so the user should read it.
- What you marked unresolved, and what would settle it.

Do not summarize the document's contents back to the user; they can read it.
