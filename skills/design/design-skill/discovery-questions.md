# Discovery Questions: Kickoff Question Protocol

Run a structured question round at the start of new or ambiguous design work. Use this whenever the user asks for something new and you don't already have what you need to start. **Asking good questions is the single biggest lever for design quality.** Bad designs come from missing context, not missing skill.

## Phase 1: Read what's already attached

Before asking anything, **read the design system and every attached resource:**

- `{{design_doc}}` + `{{tokens_css}}` — always, first. `{{system_name}}` is the standing answer to "what brand / tokens / components."
- Codebases or files the user points at (the route or component you're mocking)
- Screenshots
- The user's stated brief

Your questions should be informed by what's already there. Asking "do you have a brand guide?" when they just attached one is the fastest way to lose the user's confidence.

## Phase 2: Decide whether to ask

**Ask when:**

- The work is new or ambiguous
- The output, audience, or fidelity are unclear
- You don't know which app surface is in play
- The user hasn't specified how many variations they want
- The task spans multiple non-trivial dimensions (audience + format + tone + content all unspecified)

**Skip asking when:**

- The user gave you everything you need
- It's a small tweak or follow-up to existing work
- The user is explicit about scope, audience, and constraints
- The task is "recreate this exact thing" (a clear reference)

If the open question changes the design's direction (audience, format, scope), ask. If it's a minor choice you can defensibly make yourself (a label, a default value, two equivalent approaches), decide, build, and note the decision in your summary instead of asking.

## Phase 3: Build the question set

Every question round should include the following **always-ask** questions, plus the problem-specific questions the brief actually leaves open (typically 3–6).

### Always-ask: which surface

- **Starting point.** The design system is fixed (`{{system_name}}`) — don't ask "is there a brand." Ask instead *which* app surface this is (route / feature), and which existing page(s) it should resemble, so you read the right neighbours first.
- Confirm via a question, not your own assumption, when the surface is ambiguous.

### Always-ask: variations

- **How many variations of the overall design?** (1, 2, 3, more)
- **What axes should I vary on?** (Visual, layout, interaction, copy, tone)
- **Variations of specific elements?** ("How many variations of the header?" "Of the CTA button?")

### Always-ask: novelty

- **By-the-book or novel?** "Do you want options that match existing patterns, novel/creative ideas, or a mix?"

### Always-ask: tweaks

- **What should be tweakable in the final design?** (Copy, layout, density, light/dark — what does the user want to be able to adjust live?)

### Always-ask: focus axis

- **What do you care about most — flows, copy, or visuals?** This tells you where to spend exploration effort.

### Problem-specific (4+)

These vary by the task. Examples:

**For an app screen:**
- Which route or feature does this live in, and what's next to it?
- What's the empty state, and does it need its own file?
- Which real entities and labels should appear?
- Desktop-only or does it need a narrow breakpoint?

**For a landing or marketing page:**
- What action do you want users to take?
- Who is the primary persona?
- What competitors or references inspire you (positively or negatively)?
- Mobile-first or desktop-first?

**For an interactive prototype:**
- What flow / what screens?
- Hi-fi or mid-fi?
- One case, or several distinct cases? (distinct cases → separate files in `{{output_dir}}/`)
- What's the goal state of the flow?
- Which real app surface should this match? (nav labels, names, and taxonomy come from the app — never invented)

**For a data-dense surface:**
- What's the primary number or comparison the user is here for?
- What's the realistic row count / date range?
- Which states matter — loading, empty, error, partial data?

**For a brand or aesthetic exploration** (rare — only when the project has no established system yet, or the user explicitly wants an off-system artifact):
- Mood / tone in 3 adjectives?
- Existing brands or designs you admire (and what specifically about them)?
- Anything explicitly off-limits?
- Industry / context (B2B SaaS, consumer, editorial, government)?

If the project *does* have a system and the user isn't explicitly asking to depart from it, don't ask these — the answers are already committed.

Size the round to the ambiguity: a genuinely open brief may warrant ~10 questions; a half-specified one may need only 3–4. Never pad the round to hit a number — a question whose answer wouldn't change what you build is noise.

## Phase 4: Format the question round

Ask via your harness's structured-question mechanism. In Claude Code that is the `AskUserQuestion` tool, which renders a multiple-choice form (1–4 questions per call, 2–4 options each; an "Other" free-text choice is added automatically). With no such tool, ask the same questions as a numbered plain-text list.

For each question:

- **Prefer multiple choice** — easier for the user than open-ended text. Use `multiSelect: true` when the options aren't mutually exclusive.
- **Make one option a recommendation** — put it first and append "(Recommended)" — for choices that have a sensible default. "Decide for me" / "Explore a few options" make good escape-hatch options when relevant.
- The auto-added **"Other"** covers the open-ended fallback; you don't add it yourself.
- Keep each `header` chip short (≤12 chars) and each question specific.

A structured-question form has no sliders, SVG swatches, or file-pickers. For a numeric range, ask in plain prose; to have the user attach an asset, ask them in text to drag it in.

## Phase 5: Read the answers

Structured-question tools return the user's selections directly in the tool result — read every answer (including any "Other" free-text) before starting to design. Don't anticipate answers or design ahead of the response.

## Phase 6: Confirm and proceed

Once the user has answered:

- Briefly recap the choices that will most affect the design ("OK — settings page, existing sidebar shell, three variations on layout density, single primary action, no novel ideas")
- Note any answers that surprised you or that you'd push back on (gently — the user is the manager)
- Then proceed to the appropriate building procedure (`make-a-prototype.md`, `wireframe.md`, `generate-variations.md`) and execute autonomously. This round was your chance to ask — don't come back with follow-up questions for minor decisions; make them and list them in your summary.

## Phase 7: Re-question on signal change

If during the design work you discover that an early answer was wrong (e.g., the user said "no novel ideas" but their feedback shows they actually want bolder choices), re-question. Don't carry on with the wrong assumption — surface the contradiction and confirm.

## Anti-patterns

- **Don't skip asking.** "I'll just start building" produces designs that miss the brief.
- **Don't ask everything.** A 30-question form is hostile. Cap around 10–15 for most work.
- **Don't ask one at a time across multiple turns.** Bundle into one form.
- **Don't ask about details you can derive.** The design system, tokens, and component shapes are already in the context file — never ask for them.
- **Don't ask to be safe.** A question is justified by the design impact of its answer, not by your uncertainty.
