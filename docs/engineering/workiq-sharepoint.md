Quickstart:

```bash
npx skills add Stephan-Nassberger/skills --skill=workiq-sharepoint
```

```bash
npx skills update workiq-sharepoint
```

[Source](https://github.com/Stephan-Nassberger/skills/tree/main/skills/engineering/M365%20Developer%20Skills/workiq-sharepoint)

## What it does

Uses Work IQ to discover SharePoint lists, formatting, libraries and workflow actions. Actual runtime schemas and the signed-in user's permissions determine what it can do; adding the skill alone grants no tenant access.

## When to reach for it

Type `/workiq-sharepoint`, or the agent selects it for SharePoint Online tenant actions. For public product documentation use Microsoft Learn instead.

## Prerequisites

A working delegated OAuth connection to the official Work IQ MCP endpoint, required admin consent and effective tenant policy. SharePoint Tools are public preview; authenticated path discovery is required before use.

## Where it fits

A standalone SharePoint operations workflow alongside the JSON-formatting and SPFx skills. [ask-matt](https://github.com/Stephan-Nassberger/skills/blob/main/skills/engineering/ask-matt/SKILL.md) maps the engineering flows. Work IQ does not replace SPFx builds, local PnP tooling or a Power Platform authoring service.
