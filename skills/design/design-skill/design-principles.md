# Design Principles (Reference)

General design craft, loaded on demand by `SKILL.md`. Read this when building or reviewing a substantial artifact.

**For this project's specifics, `{{design_doc}}` is authoritative — not repeated here:** the type scale, color tokens, elevation, and component patterns live there and in `{{tokens_css}}`. This file covers the general principles that sit *on top* of that system.

## Content — what counts as filler

**Every element must earn its place. One thousand no's for every yes.** Cut anything that doesn't communicate something essential, advance the narrative, or create necessary visual structure. Common filler:

- **Placeholder/dummy content** — lorem ipsum where real copy belongs, made-up stats ("47% of users"), "Learn more" with no destination, "Coming soon" sections.
- **Unnecessary sections** — a "Why choose us?" panel when benefits are already covered; navigation duplicates.
- **Redundant elements** — headline + subhead + paragraph saying the same thing; icons that just repeat the text.
- **Decorative cruft** — background patterns with no purpose, emoji for color, gradient overlays that don't improve legibility.
- **Data slop** — numbers that don't support the message, charts with too many points, tables with columns no one reads.

The actionable version is the **five-question test** in `SKILL.md` chapter 5. If a section feels empty, that's a layout problem — solve it with composition, not invented content.

## Visual hierarchy and rhythm

**Hierarchy guides the eye:** what to look at first, second, third. **Rhythm makes it feel intentional:** repetition with strategic variation.

Hierarchy signals — combine them for strength:

- **Size.** Largest = most important. Similar sizes flatten hierarchy. (Use the type roles from `{{design_doc}}`, not arbitrary sizes.)
- **Color.** `{{color_primary_token}}` / the foreground token for emphasis, the muted-foreground token for support. (An accent reserved for a specific role — charts, links — is never the general emphasis color.)
- **Weight.** Bold headings, regular body. Everything bold = nothing stands out.
- **Position.** Top-left first (LTR). Put primary content where eyes start.
- **Density.** Loose spacing signals "pay attention"; tight signals "supporting."

Rhythm:

- **Snap to a spacing scale** (`{{spacing_scale}}`). Random margins (`margin-bottom: 7px`) feel chaotic.
- **Repeat patterns, then break them strategically** — three identical cards then a fourth that differs creates emphasis. All-identical is monotony; all-different is chaos.
- **Limit background colors** to the system's surface tokens; changes follow a pattern, never random.

The audit checklist is `hierarchy-rhythm-review.md`.

## Typography

The faces and scale are fixed — see `{{design_doc}}` (`{{font_text}}` for words, `{{font_numeric}}` for numerals, base `{{base_font_size}}`, and the role table). Universal craft on top of it:

- **`text-wrap: pretty`** on body copy to avoid widows/orphans.
- **No all-caps for large blocks** — reading relies on word shapes. All-caps is fine for short labels.
- **Tabular numerals** (`'tnum' 1`) on every number column so digits align.

## Color

The palette is fixed — see `{{design_doc}}` + `{{tokens_css}}`. Universal craft on top of it:

- **Don't rely on color alone.** Pair red/green with a `+`/`−` sign, icon, or label — 8% of men are colorblind, and grayscale/high-contrast modes need a second signal.
- **Avoid difficult combinations:** red+green, blue+yellow at similar brightness, light gray on white, colored text on colored backgrounds of similar lightness.

## Accessibility

Foundational, not an afterthought. Good accessibility is good design. The full audit is `accessibility-audit.md`; the essentials:

- **Contrast (WCAG AA):** normal text 4.5:1, large text (18px+ bold / 24px+) 3:1, UI components 3:1.
- **Semantic HTML:** `<button>` not `<div onclick>`, `<a>` for links, `<label for>` tied to `<input id>`, landmarks (`<nav>`/`<main>`/`<section>`). Proper heading order, no skipped levels. (Check `## UX nuances` in the context file — some apps deliberately render no visible page-title heading, which changes what a correct mockup looks like.)
- **Keyboard:** everything reachable and operable by keyboard. Modals close on Escape; dropdowns open with Enter/Space, navigate with arrows. Never `outline: none` without a replacement — this system's is in `## State contract`.
- **Screen readers:** alt text on meaningful images (`alt=""` on decorative), labels on every input (placeholder ≠ label), ARIA only when semantic HTML can't express the role.
- **Motion:** respect `prefers-reduced-motion`; never flash more than 3×/second.
- **Forms:** specific error messages tied to the field; required fields marked with text, not color alone.

## Interaction and feedback

Every interaction gives feedback — hover, click, submit, load, succeed, fail. The full pass is `interaction-states-pass.md`; the authoritative values are in `## State contract`:

- **Every interactive element** has default, hover, active, focus, and disabled states (plus loading for async actions).
- **Follow the system's conventions exactly** — the hover treatment, the pressed treatment, the focus ring, and the transition timing are recorded in `## State contract`, not chosen per artifact.
- **Form feedback:** errored inputs change to the destructive token with a field-tied message; async buttons disable + show progress; success/error surface the way `## UX nuances` says this app surfaces them.
- **State visibility:** the current page/tab/selection/filter must be visually distinct.

## Simplicity and one clear action

**A screen has one primary action.** Everything else supports it. Competing CTAs cause decision paralysis.

- **Navigation:** 4–6 top-level items; push depth into the sidebar tree or sub-pages.
- **Forms:** ask for what you need now; multi-step beats a wall of fields.
- **Filters:** show the most-used few; hide the rest behind "More filters."
- **Hide secondary options** behind tabs, progressive disclosure, or a sheet — keep the primary surface clean.

The 5-second test: a first-time user should grasp the screen's main action within 5 seconds. If the eye has to hunt, the hierarchy is wrong.

## System thinking

**Design components, not pages.** A page is an arrangement of components; redesigning the button on every page yields a pile of one-offs, not a design.

For this project the components and tokens already exist — compose from `{{component_dirs}}`, use `{{tokens_css}}` tokens (never arbitrary values), and reproduce the named shapes in `## Signature patterns`. When you genuinely need a new component, document it: usage (when/when not), variants, states, accessibility notes, do's and don'ts.

## Respecting the medium

HTML/CSS/JS/SVG are powerful — don't try to recreate a design tool in code. Use the web's strengths:

- **CSS:** Grid for complex layout, Flexbox for simple; custom properties for tokens; transitions for state; `text-wrap: pretty`; `oklch()`; `@media (prefers-reduced-motion)`; the project's own dark-mode mechanism (`{{dark_mode}}`); container queries.
- **SVG for icons and simple graphics** — scalable, colorable via CSS. No raster icons.
- **Real interactions, not screenshot soup.** Click → navigate. Submit → validate → succeed/fail. Real state.
- **Persist what matters** — slide/screen index, form drafts, tweak values — in `localStorage`, so a refresh restores state.
- **Canonical HTML** — explicit closing tags, double-quoted attributes, no self-closing on non-void elements. Clean markup is direct-editable.
- **Surprise the user** with what the medium can do: `oklch()` interpolation, scroll-driven animation, view transitions, container queries, SVG masks — within the system's aesthetic.

## Understanding users

**Design for the user, not for yourself.** For new work, confirm: who is the audience (`{{product_context}}`), the primary goal (decide, inform, act?), and the reading context. Design for one primary persona, not "everyone."

When the user has a hypothesis about what their audience wants, surface options that test it — a wireframe round on different bets beats four hi-fi takes on the same bet.

## Quality over quantity

**Show fewer ideas, polished.** One strong, fully-realized design beats ten half-baked ones.

- **Polish every visible detail:** spacing on the scale, real or honestly-placeholder'd imagery, all interactive states present, type on the scale, copy proofread, accessibility verified.
- **Depth over breadth:** asked for 5 things, deliver 3 done well. Core first, then iterate.
- **One strong choice beats many safe ones:** within the fixed aesthetic, pick the layout/hierarchy/interaction to be bold on and execute with conviction. A missing focus state or an arbitrary 17px margin signals you don't care.
