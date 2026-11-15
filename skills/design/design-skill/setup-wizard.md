# Setup Wizard: Bind the Design Skill to This Project

Write `.claude/design-context.md` — the file that tells this skill what this project's design system is, where its sources of truth live, and what it rejects. Run this when the file is missing, when the user asks to set up or reconfigure the design skill, or when the design system has changed.

**Detect first, ask second.** Most of what this file needs is already in the repo. Every question you ask that the codebase could have answered costs the user's patience and your credibility. Aim to arrive at the question round with defaults already filled in, asking the user to *confirm and name*, not to *supply*.

**Never guess into the file.** Anything you can neither detect nor get answered goes in the `## Unresolved` section, not into a plausible-looking value. A wrong path in this file silently corrupts every mockup built afterwards.

## Phase 1: Detect the stack

Run these searches concurrently. Read what you find — don't just note that it exists.

**Package manager and framework**
- Lockfile at the repo root: `pnpm-lock.yaml` → pnpm, `yarn.lock` → yarn, `bun.lockb` / `bun.lock` → bun, `package-lock.json` → npm.
- `package.json` dependencies: `react` / `vue` / `svelte` / `@angular/core` / none → `target_framework`. Note the meta-framework too (Next, Remix, React Router, Nuxt, SvelteKit) — it tells you where routes live.
- `tailwindcss` version → `css_framework`: `^4` → `tailwind-v4`, `^3` → `tailwind-v3`. No Tailwind but CSS custom properties present → `css-vars`. Neither → `other`.

**Design documentation**
- Repo root and `docs/`: `DESIGN.md`, `DESIGN-SYSTEM.md`, `STYLEGUIDE.md`, `BRAND.md`, `UI.md`, `docs/design*.md`, `docs/ui*.md`.
- Also check `.cursor/rules/`, `.github/`, and any `CLAUDE.md` / `AGENTS.md` for a design section — projects often keep the design rules inside an agent-instruction file rather than a standalone doc.
- Storybook config (`.storybook/`) is a strong signal that a component catalogue exists.

**Token definitions**
- Candidate files: `**/globals.css`, `**/tailwind.css`, `**/tokens.css`, `**/theme.css`, `**/app.css`, `**/index.css`, `tailwind.config.{js,ts}`.
- Confirm by content, not filename: grep for `@theme`, `:root {`, `--background`, `--foreground`, `--primary`, `oklch(`, `hsl(` inside them. The file that *defines* the custom properties is `tokens_css`.
- `tokens_entry_css` is the file an app actually imports — it may `@import` the token file and add `@font-face` / `@plugin` lines. If only one file exists, both fields are that file.

**Components**
- Directories: `packages/ui/`, `src/components/`, `app/components/`, `components/`, `lib/components/`.
- Detect a component library from `package.json`: shadcn/ui (a `components.json` at root), Radix, MUI, Chakra, Mantine, Ant. Note which — it constrains what "match the real component" means.

**Real-content sources**
- Route registries: `routes.ts`, `routes.tsx`, `app/router.*`, `pages/`, `app/` directory conventions, `src/routes/`.
- Navigation components: grep for `nav`, `sidebar`, `menu` in component filenames.
- i18n catalogues: `locales/`, `messages/`, `*.po`, `en.json`.

**Fonts**
- `@font-face` blocks in the CSS files found above; `next/font` imports; Google Fonts `<link>` in the HTML shell or root layout; `fontFamily` in `tailwind.config.*` or a `@theme` block.
- Note which face is used for numerals if a mono/tabular face is configured — many design systems set one deliberately.

**Icons**
- `package.json` dependencies: `lucide-react`, `@heroicons/*`, `@phosphor-icons/*`, `react-icons`, `@tabler/icons-*`, or an internal package (a workspace dep whose name contains `icon`).
- Grep an existing component for the actual import to confirm which one is really used.
- If a linter or agent-instruction file bans a set, capture that for `icon_banned`.

**Dark mode**
- `.dark` class selectors or `@custom-variant dark` → `class`. `@media (prefers-color-scheme: dark)` → `media`. Neither → `none`.

**Ignore rules**
- Read `.gitignore` to see whether a mockup output directory is already ignored.

## Phase 2: Report what you found

Before asking anything, show the user a compact table of detections with the evidence — the file that proved each one. Six to twelve rows, no prose.

```
design doc      docs/DESIGN.md                    found
tokens          src/styles/theme.css              defines --background, --primary (oklch)
entry css       src/app.css                       imports theme.css + 2 @font-face
components      src/components/, packages/ui/     shadcn (components.json at root)
routes          src/routes/index.ts               42 route entries
fonts           Söhne (text), JetBrains Mono      @font-face in src/app.css
icons           lucide-react                      package.json + 31 imports
css framework   tailwind v4                       package.json ^4.0.3
dark mode       class                             @custom-variant dark in theme.css
package mgr     pnpm                              pnpm-lock.yaml
```

If a row is missing or ambiguous, mark it `—` and carry it into the question round. This table is what earns you the right to ask a short set of questions instead of a long one.

## Phase 3: Branch on whether a design system exists

**Path A — the project has a design system** (a design doc, or a token file with a real palette).
This is the common case. The wizard's job is to *bind* to it. Go to Phase 4.

**Path B — tokens exist but no design doc.**
The tokens are the values; what's missing is the *intent* that sits above them. Bind to the tokens, then **run `write-design-doc.md`** after the question round — it reads the tokens and the real components and derives the document, rather than leaving the project without one. The user still approves the file before it lands (Phase 5 of that procedure), but the wizard produces a draft rather than an offer.

Sequence: Phase 4 question round first (the system's name and character are inputs to the document), then `write-design-doc.md`, then Phase 5 here with `design_doc` pointing at the new file.

**Path C — neither exists (greenfield).**
Say so plainly. The design skill needs a system to root artifacts in, and inventing one silently is exactly the failure this skill exists to prevent. Offer two routes and let the user pick:
- **Establish a minimal system now** — a short round on fonts, base palette, radius, density, and elevation. Write the agreed values to a token file the project actually imports, then run `write-design-doc.md` to produce the document from them. Then bind to it.
- **Bind loosely** — record what little exists, mark the rest `## Unresolved`, and let artifacts be explicitly exploratory until a system is decided. Every mockup carries the caveat.

Do not proceed past this phase in Path C without the user choosing.

## Phase 4: Ask what you could not detect

Ask via your harness's structured-question mechanism (`AskUserQuestion` in Claude Code; a numbered plain-text list otherwise). Batch into at most three rounds of up to four questions each. **Skip any question Phase 1 already answered** — instead, fold the detection into the option text so the user is confirming, not supplying.

### Round 1 — identity (always ask)

1. **What is this design system called?** This is the name the skill will use in every artifact and review ("matches {{system_name}}", "violates the {{system_name}} rejects"). Offer 2–3 suggestions derived from the tokens and product, plus "Other" for their own. If the design doc already names it, present that as the recommended option.
2. **Describe its character in one line.** Offer options drawn from what you read — e.g. "flat and tonal, restrained color, dense", "high-contrast, generous whitespace, editorial", "soft and rounded, warm neutrals, consumer". This becomes `system_character` and drives every judgment call the skill makes.
3. **What is the product and who reads these screens?** Audience and reading context (dense desktop dashboard / mobile-first consumer / marketing surface). Becomes `product_context`.

### Round 2 — sources of truth (ask only for unresolved rows)

Confirm, with your detected value as the recommended first option:
- Design doc path (or "none — derive from tokens").
- Token CSS path, and the entry CSS to compile against if different.
- Component directories to mirror.
- Route/nav files that supply real labels and taxonomy.

Where you found multiple candidates, list them as options rather than picking silently.

### Round 3 — visual constants and boundaries

- **Fonts** — confirm the detected text face and numeral face. If no separate numeral face exists, ask whether numbers should use the text face or a mono face; systems that display a lot of data usually want tabular figures.
- **Icon library** — confirm the detected one; ask whether any sets are banned.
- **Output directory** — default `design-mockups`; confirm, and confirm it may be added to `.gitignore`.
- **Rejects** — the highest-value question in the wizard. Ask which looks this system explicitly rejects. Seed the options from the design doc if it has a rejects/anti-patterns section; otherwise offer the universal starter set (side-stripe cards, gradient text, glassmorphism, hero-metric rings, raw palette classes, pure black/white) as a multi-select and invite additions via "Other". A design system without a stated set of rejects gives the skill nothing to enforce.

**Do not pad the round.** If detection settled a field, don't ask about it. If the user's first-round answers make a later question moot, drop it.

## Phase 5: Write the binding file

Copy `assets/design-context.template.md` to `.claude/design-context.md` and fill it in.

Rules for filling it:

- **Frontmatter takes resolved values only.** Paths are repo-root-relative, no leading `./`. Empty string for anything genuinely unknown — never a plausible guess.
- **Prose sections carry the judgment.** `## Rejects`, `## Signature patterns`, `## UX nuances`, `## State contract`, `## Real-content sources` are where a mockup gets its fidelity. Fill them from what you read, quoting real class strings and real component names. Replace every commented example with real content, and delete the comment blocks — a leftover example is worse than an empty section because the skill will treat it as fact.
- **`## Signature patterns`** — name the components a mockup must reproduce rather than reinvent, with their file location and their shape in one line. Read the components to write these; do not summarize from their filenames.
- **`## State contract`** — lift the real hover/active/focus/disabled values from the button and input components. These are what `interaction-states-pass.md` will check against, so they must be the project's actual values.
- **`## Unresolved`** — every field you could not settle, with what would resolve it. This section is a feature; an honest gap beats a confident error.
- Set `build_command` to the exact command that works for this project's stack, as verified in Phase 6.

## Phase 6: Wire and verify the CSS build

1. **Add the output directory to `.gitignore`** if it isn't already, with the user's confirmation from Round 3.
2. **Run the build helper**: `bash .claude/skills/design/scripts/build-mockup-css.sh`. It reads the binding file you just wrote, so this is also a test that the file parses.
3. **If it fails, fix the binding file, not the script.** A failure here almost always means `tokens_entry_css`, `css_framework`, or `package_manager` is wrong. Re-detect and correct.
4. **Smoke-test the tokens actually resolve.** Write `{{output_dir}}/_smoke-test.html` linking the compiled CSS and using six to eight real token classes plus both font faces — a card with a bordered header band, a primary button, a muted caption, a number in the numeral face. Serve over http and screenshot it.
5. **Confirm what the screenshot shows**: the surfaces are the system's colors and not browser defaults; both fonts render as themselves and not as fallbacks; dark mode toggles via the project's real mechanism. If the fonts fall back, resolve the font loading now — it is the single most common thing that quietly wrecks later mockups.
6. Delete `_smoke-test.html` once it passes, or keep it if the user wants a reference file.

Never report the wizard as complete on an unverified build. If the build cannot run (no network for a CLI download, missing dependencies), say so, record it under `## Unresolved`, and note that artifacts will need Approach B or C from `SKILL.md` chapter 12 until it's fixed.

## Phase 7: Report

Keep it short:

- Where the binding file was written.
- The three or four values that most shape future artifacts — system name, tokens path, fonts, output dir.
- Whether the CSS build verified, and what the smoke test showed.
- What's in `## Unresolved` and what would resolve it.
- The next step: the user asks for a mockup, and the skill runs `discovery-questions.md`.

Do not recap the question round or list every field you wrote.

## Update mode

When `.claude/design-context.md` already exists and the user asks to re-run the wizard:

1. Read the existing file first. Treat its answers as defaults, not as things to re-ask.
2. Re-run Phase 1 detection and **diff** against the recorded values. Paths that no longer resolve, a changed Tailwind major version, a swapped icon library, and new token names are the findings that matter.
3. Show the user only the diff, and ask only about fields where detection and the recorded value disagree.
4. Preserve the prose sections unless the user asks to change them — `## Rejects`, `## Signature patterns`, and `## UX nuances` encode human judgment that detection cannot regenerate. Never overwrite them wholesale on an update.
5. Re-verify the build (Phase 6) before reporting.

## Anti-patterns

- **Don't ask what the repo already says.** Detection first, always.
- **Don't write a plausible path.** An unverified path in this file is a silent failure that surfaces three mockups later.
- **Don't leave template examples in place.** The commented examples are a writing guide for you, not content — delete them.
- **Don't skip the smoke test.** "The build command exited 0" is not evidence that tokens and fonts resolve in a browser.
- **Don't invent a design system in Path C.** Offer to establish one explicitly; never assume one into being.
