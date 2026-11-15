# Generate Variations: Produce 3+ Design Options

Produce multiple distinct design variations of a screen, component, or flow so the user can mix and match the strongest pieces. Use this when the user asks for options, alternatives, "different takes," or when they say "show me a few."

**Variations are the cheapest path to good design.** A single design is one bet. Three variations let the user reject what they don't want and combine what they do.

## Phase 1: Establish the baseline

Confirm:

- **What is being varied.** A single screen, a component, a whole flow, a visual treatment? The scope determines how many variations are useful.
- **Existing design context.** Always `{{design_doc}}` + `{{tokens_css}}` (`{{system_name}}`). Every variation roots in those tokens and components — you are varying *structure and composition*, not the brand.
- **Number of variations.** Default to 3 if the user didn't specify. 5–6 is a healthy ceiling. More than that and the user can't hold them all in mind.
- **Axis preference.** Does the user care most about visuals, interactions, layout, or copy/tone? You can vary on multiple axes, but knowing the user's priority helps you weight the explorations.

## Phase 2: Pick the axes

Common variation dimensions — pick 2–4 to vary across:

- **Visual treatment** — density, tonal layering, border radius, type weight, emphasis — all *within* the fixed palette (don't invent colors or fonts)
- **Layout** — centered vs asymmetric, single-column vs multi-column, full-bleed vs inset, grid-heavy vs flowing
- **Interaction model** — single page vs multi-step, modal vs inline, hover-revealed vs always-visible
- **Information hierarchy** — what's elevated, what's secondary
- **Tone** — minimal / formal / expressive / editorial, within what the system allows
- **Component composition** — which of the `## Signature patterns` you reach for, and how they nest

For each variation, write down which axis (or axes) you're flexing. This makes the comparison legible to the user.

## Phase 3: Build with intent — basic to bold

Order matters. Start with the most by-the-book, end with the most novel:

1. **Variation 1 — by the book.** Matches existing patterns and conventions. The "safe" option. The user knows this works because it looks like things that already work.

2. **Variation 2 — refined.** Takes the safe option and pushes one or two dimensions. Same overall structure, but bolder type, a more confident layout, or a more decisive hierarchy. This is often the user's actual pick.

3. **Variation 3 — novel.** A genuinely different take. Might use an unconventional layout, a strong visual metaphor, or an unexpected interaction. The user may not pick it, but it stretches the conversation and surfaces preferences they didn't know they had.

4. **Variation 4–6 (if requested).** Hybrid points along the spectrum, or a wildcard exploration on a different axis.

**Cover both ends.** A set of 3 variations that are all "safe" wastes the user's time. A set that's all "wild" feels like you didn't take the brief seriously.

## Phase 4: Vary substantively, not cosmetically

A variation is not "the same design with a different color." Each variation should differ on something that actually matters:

✅ Variations differ in: layout, hierarchy, what's primary vs secondary, density, interaction approach, copy strategy
❌ Variations are the same except: button color, accent shade, shadow opacity

If two variations are too close, drop one and replace it with a more substantive alternative. The user should be able to articulate the difference between any two variations in one sentence.

**Specify each variation concretely before building it** — distinct layout skeleton, distinct hierarchy, distinct interaction model, written down per variation. Variety must be designed, not hoped for: left unspecified, variations drift toward one default look (typically generic SaaS). Vary layout / density / composition / interaction — **not** the palette or fonts, which are fixed. For the novel variation, push the layout or interaction off-distribution while staying on-system.

## Phase 5: Present in a single file

Save it in `{{output_dir}}/`. Lay the variations out side-by-side yourself in one HTML file (a labeled flex/grid of cells), or use **tweaks** (see `make-tweakable.md`; panel anchored bottom-right, hidden when off) if the variations share most of the structure and differ on a few axes.

For a flow or multi-screen variation, build each variation as a small storyboard within the canvas.

**Do not produce `v1.html` / `v2.html` / `v3.html` for one surface.** One file with all variations visible (or toggle-able) is far more useful for comparison than three separate files. This applies to *variations of the same surface*; genuinely **distinct cases** (different scenarios, states, or flows) are separate files instead — one per case in `{{output_dir}}/`, each named for its case.

## Phase 6: Annotate

For each variation, add a short caption (one or two sentences):

```
Variation 1 — Conventional. Standard shell, single primary action, high contrast.
Variation 2 — Refined. Same structure, stronger type hierarchy, denser table.
Variation 3 — Editorial. Asymmetric layout, oversized leading metric, progressive disclosure.
```

The captions are a thinking tool. They force you to articulate what makes each variation distinct. If you can't write a clear caption, the variation isn't distinct enough.

## Phase 7: Recommend

End with a clear recommendation. The user is the decider, but a designer offers an opinion:

- "Variation 2 is my pick — it keeps the safety of Variation 1 but adds visual confidence."
- "Variation 3 is the most interesting bet, but it's higher risk for a customer-facing surface."
- "Variations 1 and 2 are close — pick based on whether you want dense or airy."

Be direct. Don't hedge by saying all options are equally good. They aren't.

## Phase 8: Hand off

After the user picks (or asks for another round), suggest the next step:

- A single-direction iteration if the user wants to refine the chosen variation
- A second variation round on a different axis if the user wants to keep exploring
- `make-a-prototype.md` to take a chosen variation to interactive
- `polish-pass.md` if the user is ready to ship the chosen variation
