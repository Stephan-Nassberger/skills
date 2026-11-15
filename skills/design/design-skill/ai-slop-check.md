# AI Slop Check: Detect and Fix Generic AI Aesthetics

Review the current design for the visual tropes that signal "AI-generated template." Fix any found.

These patterns are rejected because they read as default, not intentional. A design that looks like a hundred other AI outputs is a design that fails to look like the user's design.

Each rule below is **positive-first**: lead with the default to reach for, then list the patterns to detect and replace. The order matters — at write-time you should be biased toward the default; at review-time, scan for the detection patterns.

## Phase 1: Identify the surface to review

Find what to review. In order:

1. The HTML/CSS file the user just edited or asked about.
2. Files modified in the current session.
3. If unclear, ask the user which file or component.

Read the file. Read `.claude/design-context.md` — in particular `## Rejects`, which is authoritative for this project and takes precedence over the universal rules below. Skim `{{tokens_css}}` and the referenced component files so you can resolve actual values.

## Phase 2: Single-pass review for AI tropes

Walk through the design and apply each rule below. Single agent — these patterns are obvious enough that parallel dispatch is overkill.

Report every detection, including uncertain or low-severity ones, with a confidence and severity estimate. Your job at this stage is coverage — filtering happens when you fix (Phase 3) or when the findings are aggregated by `polish-pass.md`.

### 1. Gradients — flat or subtle, on-tone

**Default:** flat color from the design system, or a subtle on-tone gradient (two stops, low contrast, same hue family). Flat is almost always stronger. If `{{elevation_rule}}` says the system is flat, flat is the only correct answer.

**Detect & replace:**
- Rainbow / 3+ color gradients (`linear-gradient(135deg, #FF00FF, #00FFFF, #FFFF00)` and similar)
- Saturated purple-to-pink, orange-to-pink, or other "trendy" two-color blends used for hero backgrounds, buttons, or large surfaces
- Gradient overlays on imagery that don't improve legibility or hierarchy

### 2. Emoji — functional or brand-driven only

**Default:** no emoji. Reach for one only if the brand explicitly uses emoji in existing materials, the emoji is functional (a status indicator, a category marker tied to real meaning), or the user asked for them.

**Detect & remove:**
- Emoji prepending headlines, button text, or list items where the brand doesn't use them (`🚀 Get Started`, `✅ Track progress`)
- Repeated emoji used as visual filler (`🎉🎉🎉`)
- Emoji as bullet markers when they don't add meaning

If the layout relied on the emoji for visual weight, replace with a real icon from `{{icon_library}}` (this project's sanctioned set) or improve the typographic hierarchy.

### 3. Cards — separate the way this system separates them

**Default:** the card treatment documented under `## Signature patterns`. Reserve `border-left: 4px solid` for actual semantic emphasis (callouts, alerts, status indicators), never as the default container style.

**Detect & replace** the exact pattern:

```css
.card {
  border-radius: 12px;
  border-left: 4px solid #...;
}
```

…used as the *default* card or container style across the design. This combination is so overused it reads as "default SaaS template."

Keep the left border only if it's purposeful (a callout, an alert, a status indicator), used for that meaning specifically, and not listed under `## Rejects`.

### 4. Imagery — real, licensed, or honest placeholder

**Default, in order of preference:**
- Real photography (brand assets, licensed stock)
- Professional illustration (icon library or commissioned)
- Honest placeholder — striped background with monospace label like `product shot (1200×800)`

A placeholder is better than a bad illustration. It signals "asset needed" without pretending to be the real thing.

**Detect & replace:**
- Custom SVG illustrations of people, scenes, abstract concepts that aren't drawn by a skilled illustrator
- "AI-style" character illustrations (giant heads, flat-color blobs, identical posing)
- Decorative SVG that's clearly placeholder-quality but presented as final

### 5. Type — the system's faces, in their assigned roles

**Default:** the brand fonts are fixed. `{{font_text}}` covers all prose, labels, and headings; `{{font_numeric}}` (with `'tnum' 1` where it applies) covers every metric, change %, currency, and column-aligned count. Base body is `{{base_font_size}}`.

**Detect & replace:**
- Any display/body font that isn't `{{font_text}}` (a substituted Roboto/Arial/Georgia, or a bare system stack used as the visible face)
- Numbers set in the text face instead of `{{font_numeric}}` — especially metric values, change %, and table number columns
- Proportional figures in number columns (missing `'tnum' 1`) so digits don't align

The chosen faces are deliberate, not lazy defaults — do not "improve" them away. The smell is *deviation* from the system's faces, not their presence.

### 6. Color — system tokens only

**Default:** surfaces and text come from the tokens in `{{tokens_css}}`. Neutrals follow the system's tint (`{{neutral_hue}}`) where it defines one. `{{color_primary_token}}` is the emphasis color; `{{color_accent_token}}` stays in its documented role.

**Detect & replace:**
- Exact `#FFFFFF` / `#000000` where a toned token exists
- Raw framework palette classes — `bg-gray-200`, `text-gray-800`, `text-blue-500`, `bg-rose-100`, `dark:bg-gray-700` — they break dark-mode parity
- The accent color used on a primary button when the system reserves it for another role
- Any color that doesn't trace to a token in `{{tokens_css}}`
- A pasted `:root` palette or per-element `style="…var(--…)"` standing in for utility classes — the mockup isn't wired to the real project CSS (`SKILL.md` chapter 12); replace inline token styling with real classes off the compiled stylesheet

### 7. Color values — trace to a token

**Default:** every color value traces back to a token in `{{tokens_css}}`. The palette is already complete and harmonious — don't generate a new one.

**Detect & consolidate:** color values that don't trace anywhere. Five different blues across the file (`#0066CC`, `#0077DD`, `#3498DB`, `#3B82F6`, `#5B8DEF`) is a smell — colors were invented inline instead of using the system's scales.

### 8. Spacing and radius — snap to the system's scales

**Default:** spacing on `{{spacing_scale}}`, corner radii on `{{radius_scale}}`. Values on the scale feel intentional; values off it feel chaotic.

If either is unset, fall back to multiples of 4 or 8 for spacing and to the radii the real components actually use — and say in your summary that the project hasn't recorded a scale, so you enforced a generic one.

**Detect & replace:**
- Off-scale spacing — `padding: 7px 15px`, `margin: 18px`, `gap: 13px`
- Off-scale or inconsistent radii — a `rounded-xl` card next to a `border-radius: 10px` panel next to a `rounded-md` button, with no rule behind the difference

### 9. Rejects — flag on sight

Two lists apply, and both are defects on sight rather than judgment calls.

**Universal baseline — always enforced, regardless of what the project recorded:**

- **Side-stripe borders** — a `border-l-4` colored stripe used as the *default* card or alert treatment (use full borders, background tints, or a leading icon)
- **`background-clip: text`** gradient text
- **Glassmorphism** — `backdrop-blur` on decorative cards; neon-on-black; hero gradients
- **Hero-metric ring/halo panels** — giant number + colored ring + "↑12% from last week", where the system has a real metric component to use instead
- **Drop shadows for elevation at rest** when `{{elevation_rule}}` says the system is flat — depth is a state response, not a resting property

**This project's list:** read `## Rejects` in `.claude/design-context.md` and flag every instance. Replace with the system's equivalent, or surface it to the user when the right replacement isn't obvious.

If `## Rejects` is empty, the universal baseline still applies — but say so in your summary: the project hasn't told the skill what *it* rejects, which is the half of this check with real teeth. Suggest re-running the setup wizard to fill it in.

## Phase 3: Fix and summarize

Apply fixes directly. For decisions where multiple options are reasonable, pick the most defensible default and note the choice in your summary so the user can override.

When done, summarize:
- Tropes found, by category
- Fixes applied
- Open questions for the user (asset replacement, an ambiguous reject, etc.)
