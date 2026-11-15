# Hierarchy and Rhythm Review

Review the current design for visual hierarchy and rhythm — the two qualities that most distinguish "intentional" from "AI-generated." Fix issues found.

**Hierarchy guides the eye:** what gets looked at first, second, third.
**Rhythm makes the design feel intentional:** repetition with strategic variation.

When hierarchy and rhythm are right, the design feels effortless to scan. When they're wrong, even well-intentioned content feels confusing or boring.

## Phase 1: Identify the surface

Find what to review. In order:

1. The HTML/CSS file the user just edited or asked about.
2. The most recently modified design file in the session.
3. If unclear, ask.

Read the file and the styles it references. Read the type scale and spacing scale from `{{design_doc}}` and `{{tokens_css}}` so "off-scale" means off *this* project's scale, not a generic one. Note the medium (page / mobile / dashboard) — hierarchy and rhythm rules vary by context.

## Phase 2: Launch two review agents in parallel

Launch both reviewers concurrently — in Claude Code, the `Agent` tool in a single message; sequentially if your harness has no subagents (see *Harness capabilities* in `SKILL.md`).

Instruct both agents explicitly: report every issue found, including uncertain and low-severity ones, with a confidence and severity estimate. Coverage is the agent's job; filtering happens at aggregation (Phase 3).

### Agent 1: Hierarchy review

For every screen or major section:

1. **Identify the primary, secondary, and tertiary elements.** What is the user supposed to look at first? Second? Third? If you can't tell, the hierarchy is broken.

2. **Check size differentiation.** Headings should be visibly larger than body text. The primary action should be more prominent than secondary actions. Flag cases where similar content is at very different sizes (inconsistent), and cases where different-importance content is at similar sizes (flat hierarchy).

3. **Check color hierarchy.** Primary actions use `{{color_primary_token}}`. Secondary actions use the neutral/outline treatment. De-emphasized content uses the muted-foreground token. Flag cases where everything is the same color (no signal), where unimportant elements are brightest (wrong signal), or where `{{color_accent_token}}` is used outside its documented role.

4. **Check weight hierarchy.** Headlines bold, body regular, captions regular-and-light. Flag everything-bold (nothing stands out) or everything-regular (no emphasis).

5. **Check position.** In left-to-right languages, eyes start at top-left. The most important content should be in the prime real estate. Flag layouts where the primary element is buried in the bottom-right.

6. **Check density signals.** Loose spacing around important elements signals "pay attention." Tight spacing signals "supporting." Flag cases where the most important content is crammed and unimportant content has lots of breathing room — that's reversed.

7. **Verify "the 5-second test."** A first-time user should understand what to look at and what to do within 5 seconds. If you can't, the eye doesn't have a clear path through the design.

### Agent 2: Rhythm review

For the document as a whole:

1. **Check the spacing scale.** All padding, margin, and gap values should snap to `{{spacing_scale}}`. Flag every off-scale value (`padding: 7px`, `margin: 18px`, `gap: 13px`). List the spacing values actually used and identify the outliers.

2. **Check the type scale.** Every font size should come from the scale in `{{design_doc}}`. Flag arbitrary sizes (`font-size: 17px` or `23px` when the system defines 15/18/24).

3. **Check repetition.** Sections that should look like each other (cards in a grid, list items, table rows) should share padding, gap, font sizes, and structure. Flag near-duplicates that are subtly different — either they should be identical or they should be deliberately different.

4. **Check strategic variation.** A long page should break its pattern occasionally — a background shift, a wider section, a centered action — to create rhythm. Flag pages that are completely uniform (monotonous) and pages that vary every section (chaotic).

5. **Check color palette discipline.** The design should draw from the system's tokens and no more. Flag cases where 8+ distinct colors appear, or where slightly different blues/grays are used in different places.

6. **Check section structure.** Sections should be visually distinguishable (background change, divider, padding shift) but follow a consistent pattern — the one in `## Signature patterns`. Flag sections with no visual separation (content blurs together) and sections using several different separation styles (no rhythm).

7. **Check alignment.** Elements should align to a grid. Flag elements that are off by a few pixels in a way that suggests inconsistent margins rather than intentional offset.

## Phase 3: Aggregate and fix

Wait for both agents. Aggregate findings.

For each issue:

- **Off-scale spacing → snap to `{{spacing_scale}}`.**
- **Off-scale font sizes → snap to the documented type scale.**
- **Flat hierarchy → introduce contrast.** Make headlines bigger, primary actions more prominent, body text consistently neutral.
- **Reversed hierarchy → swap signals.** If the unimportant element is brightest, mute it. If the important element is buried, reposition.
- **Monotony → introduce a strategic break** that the system supports — don't invent a new section treatment to create one.
- **Chaos → consolidate.** Pick the strongest pattern (preferring one already in `## Signature patterns`) and make others match it.

Apply fixes directly. For ambiguous cases, lean toward the more aggressive hierarchy — a too-strong hierarchy is easier to dial back than a too-weak one to dial up.

## Phase 4: Summarize

Report:
- Hierarchy issues found and fixed
- Rhythm issues found and fixed
- Any judgment calls that the user should review (e.g., "I made the primary action significantly larger — adjust if too aggressive")
- Open recommendations (e.g., "the file mixes 4px and 6px increments; the system's scale is 4px — worth a sweep")
