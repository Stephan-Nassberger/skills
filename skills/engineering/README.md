# Engineering

Skills I use daily for code work.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ask-matt](./ask-matt/SKILL.md)** — Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.
- **[grill-with-docs](./grill-with-docs/SKILL.md)** — Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs inline.
- **[triage](./triage/SKILL.md)** — Move issues through a state machine of triage roles.
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)** — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)** — Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo.
- **[to-spec](./to-spec/SKILL.md)** — Turn the current conversation into a spec and publish it to the issue tracker.
- **[to-tickets](./to-tickets/SKILL.md)** — Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges — text in a local file, or native blocking links on a real tracker.
- **[implement](./implement/SKILL.md)** — Build the work described by a spec or set of tickets, driving `/tdd` at pre-agreed seams and closing out with `/code-review` before committing.
- **[wayfinder](./wayfinder/SKILL.md)** — Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision tickets on the issue tracker, resolved one at a time until the way to the destination is clear.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[prototype](./prototype/SKILL.md)** — Build a throwaway prototype to answer a design question: a runnable terminal app for state/logic, or several toggleable UI variations.

- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)** — Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test.
- **[research](./research/SKILL.md)** — Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.
- **[tdd](./tdd/SKILL.md)** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **[domain-modeling](./domain-modeling/SKILL.md)** — Actively build and sharpen a project's domain model — challenge terms, stress-test with scenarios, update `CONTEXT.md` and ADRs inline.
- **[codebase-design](./codebase-design/SKILL.md)** — Shared discipline and vocabulary for designing deep modules: small interfaces, clean seams, testable through the interface.
- **[code-review](./code-review/SKILL.md)** — Two-axis review of the diff since a fixed point: **Standards** (does it follow the repo's coding standards, plus a Fowler smell baseline?) and **Spec** (does it faithfully implement the originating issue/PRD?), run as parallel sub-agents.
- **[resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md)** — Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation — never `--abort`.

## M365 Developer Skills — Model-invoked

- **[spfx](./M365%20Developer%20Skills/spfx/SKILL.md)** — SharePoint Framework (SPFx) development.
- **[msgraph-sdk](./M365%20Developer%20Skills/msgraph-sdk/SKILL.md)** — Integrate Microsoft Graph SDK into any project — .NET, TypeScript/JavaScript, or Python.
- **[teams-dev](./M365%20Developer%20Skills/teams-dev/SKILL.md)** — Use this skill whenever the user mentions Microsoft Teams in a development context — whether they're building, integrating, configuring, debugging, porting a Slack bot to Teams, or just asking questions.
- **[semantic-model-authoring](./M365%20Developer%20Skills/semantic-model-authoring/SKILL.md)** — Manages Power BI semantic models, including tables, columns, measures, relationships, field parameters, DAX, Import, DirectQuery and Direct Lake designs, sources, connections, permissions, refresh, and deployment.
- **[martix-sharepoint-pnp](./M365%20Developer%20Skills/martix-sharepoint-pnp/SKILL.md)** — Standalone-first SharePoint PnP guidance for tool selection, provisioning, automation, authentication, and cross-tool delivery using PnP PowerShell, CLI for Microsoft 365, and PnPjs.
- **[martix-fluent-ui](./M365%20Developer%20Skills/martix-fluent-ui/SKILL.md)** — Fluent UI React v9 engineering for packages, providers, themes, tokens, Griffel, public component and slot composition, accessibility and focus, Next.js SSR, icons, motion, charts, legacy Fabric/v8/v0 migration, and rare Vue integration through @fluentui/web-components.
- **[pnp-modern-search](./M365%20Developer%20Skills/pnp-modern-search/SKILL.md)** — Configure and troubleshoot PnP Modern Search v4 web parts, KQL, managed properties, filters and Handlebars layouts.
- **[sharepoint-json-column-formatting](./M365%20Developer%20Skills/sharepoint-json-column-formatting/SKILL.md)** — Create, review and troubleshoot SharePoint and Microsoft Lists JSON column formatting, field expressions and supported actions.
- **[sharepoint-json-view-formatting](./M365%20Developer%20Skills/sharepoint-json-view-formatting/SKILL.md)** — Create and debug SharePoint and Microsoft Lists JSON view formatting for rows, tiles and supported layout surfaces.
- **[adaptive-cards-m365](./M365%20Developer%20Skills/adaptive-cards-m365/SKILL.md)** — Design and validate Adaptive Cards for Teams, Power Automate or SPFx Adaptive Card Extensions with host-specific actions and data binding..
- **[power-automate-development](./M365%20Developer%20Skills/power-automate-development/SKILL.md)** — Design, review and troubleshoot Power Automate cloud flows, SharePoint integrations, expressions, connection references and solution ALM.
- **[power-apps-development](./M365%20Developer%20Skills/power-apps-development/SKILL.md)** — Build and review Power Apps canvas and model-driven apps, Power Fx, SharePoint forms, delegation and solution ALM using the actual authoring tools available..
- **[planner-development](./M365%20Developer%20Skills/planner-development/SKILL.md)** — Develop Microsoft Planner basic-plan integrations through Microsoft Graph, including tasks, buckets, details, assignments and concurrency.
- **[microsoft-forms-integration](./M365%20Developer%20Skills/microsoft-forms-integration/SKILL.md)** — Integrate Microsoft Forms responses with Power Automate and SharePoint using documented connectors, ownership and response mappings.
- **[sharepoint-html-spfx-extensions](./M365%20Developer%20Skills/sharepoint-html-spfx-extensions/SKILL.md)** — Choose and implement supported SharePoint HTML rendering and SPFx Application Customizer, Field Customizer, Command Set or Form Customizer extensions..
- **[azure-functions-m365](./M365%20Developer%20Skills/azure-functions-m365/SKILL.md)** — Build and troubleshoot Azure Functions backends for Microsoft 365 integrations, Graph webhooks, timers and queue-based processing..
- **[microsoft-learn](./M365%20Developer%20Skills/microsoft-learn/SKILL.md)** — Search current Microsoft Learn documentation and official code samples before implementing or troubleshooting Microsoft 365, SharePoint, SPFx, Graph, Teams, Power Platform, Power BI, Fluent UI or Azure integrations.

- **[workiq-sharepoint](./M365%20Developer%20Skills/workiq-sharepoint/SKILL.md)** — SharePoint Online über Work IQ lesen und bearbeiten; echte Schemas und delegierte Berechtigungen prüfen.
