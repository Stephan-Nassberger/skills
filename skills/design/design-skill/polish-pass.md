# Polish Pass: End-of-Design Quality Gate

Run a comprehensive quality check before a design is shown to stakeholders or shipped. **A polished design and an unpolished design are the same idea executed at different levels of care — and the gap is what people actually see.**

This procedure is the umbrella for the four narrower review procedures. Use it as the final gate before delivery.

## Phase 1: Confirm scope

Determine what to polish:

1. The HTML file the user just finished or asked about.
2. The current main deliverable in the project.
3. If unclear, ask.

Read the file. Take note of:
- The medium (page / mobile / dashboard / animation)
- The deployment context (internal review / customer-facing / marketing)
- Any user-stated constraints or scope boundaries

If the design is clearly mid-flight (broken layout, missing sections, placeholder content the user is still iterating on), say so and ask whether they really want a polish pass now or after the structure is settled.

## Phase 2: Launch four review agents in parallel

Launch all four reviewers concurrently — in Claude Code, the `Agent` tool in a single message; if your harness cannot run subagents, run them sequentially (see *Harness capabilities* in `SKILL.md`). Each reviewer runs the equivalent of one of the standalone review procedures (`accessibility-audit.md`, `ai-slop-check.md`, `hierarchy-rhythm-review.md`, `interaction-states-pass.md`), scoped to this file.

Pass every agent the relevant sections of `.claude/design-context.md` alongside the file — `## Rejects`, `## Signature patterns`, `## UX nuances`, `## State contract`. An agent without them will flag correct-for-this-app patterns as defects and miss the project's real rejects.

Instruct every agent explicitly: **report every issue found, including uncertain and low-severity ones, with a confidence and severity estimate for each.** Coverage is the agent's job; filtering and prioritization happen in Phase 3. An agent that self-censors "minor" findings silently lowers recall.

### Agent 1: Accessibility audit

Run the full `accessibility-audit` review:
- Contrast and color (WCAG AA minimums, color-only signaling, problematic combinations, both themes)
- Semantic HTML and structure (headings, button vs div, labels, alt text, ARIA discipline)
- Keyboard navigation and focus (reachability, tab order, visible focus, skip links)
- Motion, forms, and miscellany (`prefers-reduced-motion`, flash limits, error specificity, hit-target size)

Report findings as a categorized list.

### Agent 2: AI slop check

Run the full `ai-slop-check` review:
- Aggressive gradients
- Emoji-as-decoration
- Side-stripe cards used as a default treatment
- Hand-drawn SVG illustrations
- Fonts deviating from the system's assigned faces, and numbers set in the wrong face
- Colors that don't trace to a token; raw framework palette classes
- Off-scale spacing values
- Every entry in `## Rejects`

Report findings.

### Agent 3: Hierarchy and rhythm review

Run the full `hierarchy-rhythm-review`:
- **Hierarchy:** primary/secondary/tertiary differentiation, size, color, weight, position, density, 5-second test
- **Rhythm:** spacing scale discipline, type scale discipline, repetition, strategic variation, palette discipline, section structure, alignment

Report findings.

### Agent 4: Interaction states pass

Run the full `interaction-states-pass`:
- Inventory of interactive elements
- For each: default, hover, active, disabled, focus, loading — verified against `## State contract`
- Transitions (per the contract; `prefers-reduced-motion` respected)
- Feedback for actions (success/error confirmation, state visibility)

Report findings.

## Phase 3: Aggregate, deduplicate, prioritize

Wait for all four agents. Aggregate findings into one list.

**Deduplicate.** If two agents flagged the same issue (e.g., "focus ring removed" appears in both accessibility and interaction-states), merge into one entry.

**Prioritize.** Group findings into:

1. **Blockers** — accessibility failures (contrast under WCAG, missing keyboard support, removed focus rings, missing labels). These break the design for real users; fix all of them.
2. **Quality issues** — documented Rejects, AI slop tropes, broken hierarchy, missing interaction states. These cheapen the design; fix all of them.
3. **Polish recommendations** — subtler improvements (spacing-scale tightening, a stronger primary action). Apply when in scope; flag when out of scope.

## Phase 4: Fix

Fix every blocker and every quality issue directly, using the system's own tokens and contract values. Apply polish recommendations when they don't conflict with the user's stated direction.

For ambiguous fixes, pick a defensible default and note the choice in the summary so the user can override.

For findings that are clearly false positives or outside scope (e.g., "the third-party embed has low contrast — but it's a third-party widget"), note them and skip.

If a finding implicates the design system itself rather than the mockup (a token pair that can't pass AA, a missing state in the real component), don't paper over it in the mockup — surface it as a design-system finding.

## Phase 5: Re-verify

After fixes, do a quick re-check on the high-risk areas:
- Did the contrast fixes maintain the visual style, or did they push a color off-token?
- Did the focus ring additions overlap with neighboring content?
- Did the hierarchy adjustments make the primary action actually feel primary?
- Does it still hold up in the other theme?

If anything looks off, fix it. If you're unsure, flag it for the user's review.

## Phase 6: Final summary

Report concisely:

- **Verdict** — "Ready to ship" / "Ready after user reviews flagged decisions" / "Needs more iteration before polish makes sense"
- **Blockers fixed** — count by category (accessibility / slop / hierarchy / interaction)
- **Polish applied** — count by category
- **Open decisions** — judgment calls the user should sign off on
- **Design-system findings** — anything that implicates the real system rather than this artifact
- **Out of scope** — anything you noticed but didn't touch (copy edits, content additions, new features)

Keep the summary short. The user can ask for detail if they want it. **Brief summaries — caveats and next steps only.**
