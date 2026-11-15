# Make a Prototype: Interactive Clickable Prototype

Build a working interactive prototype — clickable, navigable, with real state and feedback. Use this when the user asks for a prototype, mockup, demo, or "make it interactive."

**Prototypes interact.** Static screenshots strung together with `<a>` tags don't count. The point of a prototype is to test the flow with real interaction — clicking, typing, validating, succeeding, failing.

## Phase 1: Discovery

Confirm before building:

- **The flow.** What screens? What's the entry point? What's the goal state? Map it as a list.
- **Fidelity.** Hi-fi (real visuals, real components, real feel) or mid-fi (wireframe-level, focused on flow not polish)?
- **What it becomes.** This prototype previews something that will be built in `{{target_framework}}`. Favour structures that map cleanly onto that — component boundaries where real components exist, state shapes that a real implementation would keep. A prototype that can't be translated is a prototype that gets thrown away.
- **No browser chrome.** Never wrap the prototype in a simulated browser window or device frame (URL bar, tabs, traffic-light buttons, window controls). Deliver the clean app UI only — reproduce the app's own navigation chrome, nothing around it.
- **Variations.** Does the user want one flow or several to compare? Distinct *cases* (different scenarios, states, or flows) become separate files in `{{output_dir}}/`; multiple takes on the *same* surface stay in one file.
- **Design system.** Already fixed: read `{{design_doc}}` + `{{tokens_css}}` and apply `{{system_name}}`. Wire the real project CSS (`SKILL.md` chapter 12) — compile and link the output, don't hand-copy tokens — then `{{font_text}}` + `{{font_numeric}}` and `{{icon_library}}`.
- **Real content, not invented.** Pull actual navigation labels, entity names, and product taxonomy from the app source (`{{content_sources}}` and `## Real-content sources`) — never guess or predict them. Avoid Lorem ipsum. Sample *data values* may be plausible stand-ins; labels, names, and terms must match the real app.

## Phase 2: Map screens and state

Before building, write down the flow:

```
Screens:
  1. Welcome — "Get started" CTA → goes to 2
  2. Email entry — validate format → goes to 3 on valid, shows error on invalid
  3. Verification — "Check your email" + "Skip" → goes to 4
  4. Profile — name, photo upload → goes to 5
  5. Success — "You're in" + "Get started" → goes to 1 (loop demo)

State:
  - currentScreen: 1
  - email: ""
  - emailError: null
  - name: ""
```

Drop this into the file as a comment block at the top so the user can see your plan.

## Phase 3: Build screen-by-screen

For each screen:

1. **Mount in the DOM** — use display toggling (`display: none` / `display: block`) or component state to switch screens within a single page.
2. **Hi-fi visuals.** Match `{{system_name}}` exactly: real project classes off the compiled CSS (`SKILL.md` chapter 12 — not hand-copied tokens), `{{font_text}}` for words + `{{font_numeric}}` (with `'tnum' 1`) for all numbers, `{{icon_library}}`-style inline SVGs. Reproduce the real component shapes listed under `## Signature patterns`. No generic boxes; no invented components.
3. **Real content, sourced not guessed.** Navigation labels, section names, and product taxonomy come from the actual app — never invented. Data *values* may be plausible stand-ins, but every label and term must match what the app really uses. No Lorem ipsum.
4. **One primary CTA per screen.** Secondary actions are smaller and de-emphasized.

Do not add a simulated browser window or device frame around the prototype — no URL bar, tabs, or window controls. The prototype is the clean app UI itself: the app's own navigation chrome on the system's substrate, and nothing wrapping it.

## Phase 4: Wire up interactions

A real prototype has **every interaction wired**, not just the happy path:

- **Navigation.** Clicking the primary CTA moves to the next screen. Back button moves backward. State persists across screens.
- **Form validation.** Empty submission → inline error. Bad format → specific error tied to the field. Valid input → proceed.
- **Loading states.** Async actions (sign-up, save) show a loading indicator. Buttons disable during the request to prevent double-submit.
- **Success feedback.** Whatever `## UX nuances` says this app uses — toast, inline confirmation, or page transition.
- **Error feedback.** Errors are clear and tied to the field or action that caused them.
- **State changes.** Toggling, selecting, filtering — all update the UI immediately.

If the prototype is a small slice, fake the async work with `setTimeout` to simulate latency. Don't skip the loading state because the work is fake — the loading state is part of what the prototype is testing.

## Phase 5: Wire up sub-state

Many real flows have meaningful sub-state:

- **Selection state** — which item is selected in a list
- **Filter / sort state** — how the data is currently arranged
- **Modal / dropdown state** — open or closed
- **Form state** — values, errors, dirty/pristine

Make these all reactive. If the user clicks a filter chip, the list re-renders. If they open a modal, focus moves to the modal and Escape closes it.

## Phase 6: Persist what matters

Some state should survive a page reload:

- **Current screen** — store in `localStorage`, restore on load
- **Form drafts** — if the user is mid-flow and refreshes, they should pick up where they left off
- **Tweak values** — see `make-tweakable.md`

Refreshing during iterative design is one of the most common user actions. State that doesn't survive reload makes the prototype feel broken.

## Phase 7: Verify

Walk through the full flow in the preview:

- Every CTA leads somewhere
- Every form validates
- Every error is clear and recoverable
- Every async action shows feedback
- Every state change is visible
- Keyboard navigation works (Tab through, Enter to submit, Escape to close modals)
- Focus is visible

If you can't verify a UI behavior, say so explicitly in the summary rather than claiming success.

## Phase 8: Variations (if requested)

If the user asked for variations of the *same* flow, layout, or visual treatment, expose them in one file as:

- **Tweaks** — a floating panel toggled from the bottom-right corner, hidden when off (see `make-tweakable.md`)
- **A canvas** — multiple variants side-by-side, laid out yourself in one HTML file
- **Toggles in the prototype** — the user clicks between options

Don't scatter `v1.html` / `v2.html` / `v3.html` for one surface — collapse those into a single file. **Distinct cases** (different scenarios, states, or flows) are the exception: one descriptively-named file each in `{{output_dir}}/`.

Summarize briefly: what flows work, what's faked (e.g., "submit calls a setTimeout fake"), what's open for the user to decide.
