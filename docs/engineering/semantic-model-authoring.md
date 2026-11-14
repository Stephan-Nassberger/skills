Quickstart:

```bash
npx skills add Stephan-Nassberger/skills --skill=semantic-model-authoring
```

```bash
npx skills update semantic-model-authoring
```

[Source](https://github.com/Stephan-Nassberger/skills/tree/main/skills/engineering/M365%20Developer%20Skills/semantic-model-authoring)

## What it does

Manages Power BI semantic models, including tables, columns, measures, relationships, field parameters, DAX, Import, DirectQuery and Direct Lake designs, sources, connections, permissions, refresh, and deployment. Load this skill before acting on a semantic model, unless it is part of publishing a PBIP project, which powerbi-report-cli owns. For natural-language data questions use fabriciq; for visuals use powerbi-report-cli.

This workflow follows the target project's actual version and available tools. It does not grant tenant permissions or deploy a solution merely because the skill is installed.

## When to reach for it

Type `/semantic-model-authoring`, or the agent can select it when the task fits. Use its documented product boundary; combine it with Microsoft Learn for current Microsoft API and compatibility evidence.

## Prerequisites

For implementation, provide the target project and the tools appropriate to that product. Live documentation search uses the official Microsoft Learn MCP connection; M365 tenant access remains separate. This folder is part of a curated collection, not a new Microsoft certification or tool entitlement.

## Where it fits

A standalone domain workflow in Stephan Nassberger's M365 Developer Skills collection. It complements the existing engineering flow instead of replacing it. [ask-matt](https://github.com/Stephan-Nassberger/skills/blob/main/skills/engineering/ask-matt/SKILL.md) maps the other workflows; [the M365 catalog](https://github.com/Stephan-Nassberger/skills/blob/main/skills/engineering/M365%20Developer%20Skills/CATALOG.md) records source, license and version for this skill.
