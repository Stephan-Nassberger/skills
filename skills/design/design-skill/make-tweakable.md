# Make Tweakable: Add In-Design Tweak Controls

Add a floating control panel to a finished design that lets the user adjust selected aspects live — density, copy, layout variants, light/dark, feature flags. Use this when the user wants to "play with options," "see different versions," or compare visual choices side-by-side.

**One file, many variants.** Tweaks let a single design hold multiple visual exploration paths without scattering v1.html / v2.html / v3.html across the project.

## Phase 1: Identify what should be tweakable

Confirm with the user — or propose and check — which aspects to expose. Common candidates:

- **Light / dark** — toggle the project's real dark-mode mechanism (`{{dark_mode}}`)
- **Density** — spacing scale (tight / normal / loose)
- **Layout variant** — centered vs left-aligned, single-column vs multi-column
- **Component variants** — button treatment, card treatment, table density
- **Copy** — headline, subhead, CTA text
- **Feature flags** — show/hide a section, empty vs populated state

**Colors and fonts are not tweak axes.** The palette and faces are fixed by `{{system_name}}`; exposing them invites the user to design a second system by accident. The exception is an artifact the user explicitly asked to be off-system.

Resist exposing every possible knob. **Keep the tweak surface small** — 3–8 controls is a healthy range. The point is to give the user a few meaningful axes to explore, not to recreate a design tool.

If the user didn't ask for tweaks but the design has obvious axes of variation, add 1–2 by default to surface interesting possibilities.

## Phase 2: Design the tweak panel

The tweak panel lives **inside the prototype**, anchored to the **bottom-right corner** (always — not top, not left), with a subtle border built from the system's card and border tokens, not arbitrary translucency. Title it **"Tweaks"** to match the toggle you add in Phase 4. This placement is a hard rule: any control chrome that drives the prototype — sidebar, tooltip, or tweak panel — sits bottom-right.

Each control should be the right type for the value:

- **Variant / layout / density** → dropdown or button group
- **Number (spacing, count)** → slider with sensible min/max
- **Boolean (show/hide section, dark mode)** → toggle
- **Copy** → text input or textarea

Keep controls compact. A narrow column of tightly stacked controls is better than a sprawling panel.

## Phase 3: Wire up the live updates

The base palette already comes from the linked project CSS (`SKILL.md` chapter 12) — don't re-declare it. Tweaks that map to CSS values override tokens at runtime on the root element, and everything referencing a token updates instantly:

```js
document.documentElement.style.setProperty('--spacing-unit', newValue);
```

For light/dark, drive the project's real mechanism rather than a hand-rolled one — if `{{dark_mode}}` is `class`, toggle that class on the root element; if it's `media`, simulate it with a class override and say so in your summary, since a media query can't be toggled from the page.

For non-CSS values (copy, layout variants, feature flags), use JS state with re-render or DOM manipulation.

## Phase 4: Make the panel self-contained

These mockups open as plain HTML files in a browser — there is no host/iframe edit-mode protocol. Wire the toggle yourself:

1. **Add a small toggle control** in the **bottom-right corner** (a gear or "Tweaks" button) that shows/hides the panel. The panel opens as a popup over that corner and is fully hidden when off.
2. **Bind each control to its target** with a plain `input` / `change` listener that updates a CSS custom property, a text node, or a class.
3. **Keyboard-reachable:** the toggle and every control must be focusable and operable by keyboard, with a visible focus ring matching `## State contract`.

Keep the panel's own logic in one inline `<script>` — no external JS dependencies, no `postMessage`. (The stylesheet is the shared compiled CSS from chapter 12; that link stays.)

## Phase 5: Persist across reload with localStorage

The host won't rewrite the file for you — persist tweak values yourself:

```js
const TWEAK_DEFAULTS = { density: "normal", dark: false };
const tweaks = { ...TWEAK_DEFAULTS, ...JSON.parse(localStorage.getItem("tweaks") || "{}") };
// on every change:
localStorage.setItem("tweaks", JSON.stringify(tweaks));
```

Apply the stored values on load (before first paint where possible) so a refresh restores the user's last state. Refreshing during iterative design is one of the most common user actions.

## Phase 6: Hide the controls when off

The design should look final when Tweaks is toggled off. The panel should be entirely hidden — not just dimmed, not just collapsed to a corner. The user should see the design as a polished artifact with no visible tweak chrome.

This is non-negotiable: any "edit mode UI" left visible when tweaks are off makes the design look unfinished.

## Phase 7: Verify

In the user's preview:

- Toggle the panel on and off via your toggle control — it shows/hides cleanly
- Change each tweak — it updates live
- Reload the page — the tweaked values persist
- Check the design with the panel off — it looks like a finished design, no tweak chrome visible

## Phase 8: Summarize

Report:

- Tweaks exposed and their value types
- Defaults
- Any tweaks you considered but excluded (and why)
- Whether the tweak set covers the user's intended exploration axes
