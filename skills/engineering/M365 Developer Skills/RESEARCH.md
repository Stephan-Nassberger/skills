# Recherche und Qualitätsprüfung

## Methode und Grenzen

Stand 14.11.2026. Öffentliche Websuche nach SKILL.md plus direkte GitHub REST-Prüfung von Repository-Metadaten, Default-Branch-Commit und vollständigem rekursivem Git-Baum (kein ausgewerteter Baum war abgeschnitten). Kandidaten wurden nicht als Anweisungen für diese Arbeit ausgeführt. Repository-Namen, Suchtreffer oder Skill-Verzeichnisse allein genügen nicht als Qualitätsnachweis. Keine vollständige weltweite Suche oder Sicherheitszertifizierung. Keine fremden Installationsskripte ausgeführt.

Die importierten Einstiegstexte und ihre Struktur wurden statisch geprüft, Dateien/Abhängigkeiten vollständig übernommen und lokale Markdown-Verweise maschinell geprüft. Keine vollständige fachliche Zeilenprüfung sämtlicher Referenzen, keine Verhaltens-Evaluation und keine Tests gegen M365.

## Übernommen

### spfx

Microsoft SharePoint; preview. Four useful playbooks (create, upgrade, React/Fluent UI, PnPjs). Repaired one broken upstream toolchain link. Defaults favor PnPjs/Fluent v9; preserve existing architecture and installed versions.

[Versionierte SKILL.md](https://github.com/SharePoint/spfx-dev-skills/tree/31010d241bd84821d32ebfa50eda1fe81a6f0b86/plugins/spfx/skills/spfx/SKILL.md) · Lizenz: MIT.

### msgraph-sdk

GitHub community collection, not the Microsoft Graph product team. Language-specific refs and live-doc verification. Some generalizations (credential order, delta coverage, subscription lifetimes) require endpoint-specific verification; do not treat examples as an API contract.

[Versionierte SKILL.md](https://github.com/github/awesome-copilot/tree/8ecd5b17f02fe5fbebf35eccd1867265eded811f/skills/msgraph-sdk/SKILL.md) · Lizenz: MIT.

### teams-dev

Microsoft Teams SDK repository. Six workflow references retained. Requires Teams CLI 3.x and, for infrastructure, Azure/auth access. Broad routing and restricted source list are upstream choices. Shell examples need platform adaptation.

[Versionierte SKILL.md](https://github.com/microsoft/teams-sdk/tree/64aebb60e8e17c9087f86c16e2cc3672ee302450/plugins/teams-sdk/skills/teams-dev/SKILL.md) · Lizenz: MIT.

### semantic-model-authoring

Microsoft Fabric. Fourteen skill files plus shared common dependencies retained. Covers Power BI semantic models, not complete report visual authoring. Requires model MCP/CLI/permissions for live use; local TMDL paths are conditional.

[Versionierte SKILL.md](https://github.com/microsoft/skills-for-fabric/tree/e31422e7d1045ef3a0906df9ff5991f2338af010/plugins/fabric-skills/skills/semantic-model-authoring/SKILL.md) · Lizenz: MIT.

### martix-sharepoint-pnp

Community package, Apache-2.0 in the skill folder (root API license metadata is empty). Focused authentication/provisioning/PnP PowerShell rules, source maps and eval prompts. No claim that bundled evals were executed. Optional sibling-skill handoffs are not included.

[Versionierte SKILL.md](https://github.com/MartiXDev/skills/tree/7ebf3fc4bf1abe52e35208fe7f9b4486dc634cce/skills/martix-sharepoint-pnp/SKILL.md) · Lizenz: Apache-2.0.

### martix-fluent-ui

Community package, Apache-2.0 in the skill folder. Detailed version, accessibility, tokens, composition and migration guidance. CSS-first and React-v9 preferences are author opinions, not Microsoft requirements. Optional TypeScript sibling not included.

[Versionierte SKILL.md](https://github.com/MartiXDev/skills/tree/7ebf3fc4bf1abe52e35208fe7f9b4486dc634cce/skills/martix-fluent-ui/SKILL.md) · Lizenz: Apache-2.0.

## Weitere verifizierte Quellen / bewusst nicht übernommen

| Repository/Kandidat | Befund und Entscheidung |
|---|---|
| [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) | MIT, echte Skills für Canvas, Model-driven Apps, PCF und Power Automate. `canvas-app` und `build-flow` gelesen. Enge CanvasAuthoringMcpServer-/FlowAgent-Abhängigkeiten, hostbezogene Toolnamen und teils Claude-spezifische Metadaten. Deshalb link-only; keine isolierte SKILL.md-Kopie ohne ihren Plugin-Kontext. Eigene portable Entwicklungs-Workflows sind eingeschränkter und ersetzen diese Authoring-Tools nicht. |
| [Power Automate build-flow](https://github.com/microsoft/power-platform-skills/blob/af779892413ab4516e061663e9a55dbfa60d13fa/plugins/power-automate/skills/build-flow/SKILL.md) | Reale ausführliche Definition-/Validierungsanleitung; nicht als sofort lauffähiges ChatGPT-Tool übernommen. |
| [Power Apps canvas-app](https://github.com/microsoft/power-platform-skills/blob/af779892413ab4516e061663e9a55dbfa60d13fa/plugins/canvas-apps/skills/canvas-app/SKILL.md) | Reales Skill, gekoppelt an Plugin-weite Referenzen und Canvas Authoring MCP; Original-Plugin als Einheit evaluieren. |
| [pnp/powershell](https://github.com/pnp/powershell) | MIT. Echte .agents/skills für Cmdlet-Entwicklung, Review, Dokumentation und Berechtigungsprüfung. Diese betreffen vor allem die Entwicklung des Moduls selbst; kein gleichwertiger allgemeiner Anwender-Skill. Deshalb MartiX-PnP-Paket für Skript-/Provisionierungsarbeit übernommen. |
| [pnp/cli-microsoft365](https://github.com/pnp/cli-microsoft365) | MIT. Reales `skills/clim365/SKILL.md` mit Befehlsindex und verpflichtender --help-Prüfung. Sehr breite Routingregel würde ohne ausdrücklichen Wunsch PowerShell/Graph verdrängen. Als Alternative verlinkt, nicht automatisch eingebunden. |
| [microsoft-search/pnp-modern-search](https://github.com/microsoft-search/pnp-modern-search) | Im vollständig geprüften Baum keine SKILL.md. Produktcode und Dokumentation sind keine fertigen Skills. GitHub meldet NOASSERTION; manuell gelesene LICENSE enthält MIT-Bedingungen. Keine Produktdateien kopiert; eigener Skill mit Primärquellen. |
| [pnp/List-Formatting](https://github.com/pnp/List-Formatting) | MIT; geprüfter Baum enthält keine SKILL.md. Sehr passende JSON-Beispiele, aber eine Beispielsammlung ist kein Skill. Eigene getrennte Column-/View-Skills, keine kopierten Beispiele. |
| [github/awesome-copilot: mcp-create-adaptive-cards](https://github.com/github/awesome-copilot/blob/8ecd5b17f02fe5fbebf35eccd1867265eded811f/skills/mcp-create-adaptive-cards/SKILL.md) | MIT, echte SKILL.md gelesen. Aus Prompt konvertiert, Fokus auf M365-Copilot-API-Plugin-Antwortvorlagen/ai-plugin.json, nicht universelle Teams-/Flow-Karten und nicht das ChatGPT-Pluginformat. Deshalb eigener hostbezogener Adaptive-Card-Skill. |
| [microsoft/skills: teams-app-developer](https://github.com/microsoft/skills/blob/main/.github/plugins/microsoft-365-agents-toolkit/skills/teams-app-developer/SKILL.md) | MIT, echtes Skill gelesen; ca. 148 Dateien im Paket und Beta-CLI-Vorgaben. Für diese Startsammlung das kompaktere Teams-SDK-Paket gewählt; ATK als Alternative, nicht redundant eingebunden. |
| [OfficeDev/microsoft-365-agents-toolkit](https://github.com/OfficeDev/microsoft-365-agents-toolkit) | Echte Skills, aber auch viele Test-Fixtures mit SKILL.md. Root-Lizenzmetadaten NOASSERTION; nicht zur pauschalen Übernahme freigegeben, keine Dateien kopiert. |

Weitere **strukturell gefundene, noch nicht inhaltlich geprüfte** Power-BI-Kandidaten aus dem MIT-Repository github/awesome-copilot: [DAX optimization](https://github.com/github/awesome-copilot/blob/8ecd5b17f02fe5fbebf35eccd1867265eded811f/skills/power-bi-dax-optimization/SKILL.md), [report design consultation](https://github.com/github/awesome-copilot/blob/8ecd5b17f02fe5fbebf35eccd1867265eded811f/skills/power-bi-report-design-consultation/SKILL.md), [model design review](https://github.com/github/awesome-copilot/blob/8ecd5b17f02fe5fbebf35eccd1867265eded811f/skills/power-bi-model-design-review/SKILL.md). Nicht übernommen und nicht als qualitätsgeprüft dargestellt.

## Eigens erstellt

Zehn neue, englischsprachige Skills für klare Agenten-Verwendung: Modern Search, Column Formatting, View Formatting, Adaptive Cards, Power Automate, Power Apps, Planner, Forms, SharePoint HTML/Extensions und Azure Functions. Sie sind neue, dokumentationsgestützte Arbeitsanweisungen unter MIT, keine aus Microsoft-Dokumentation kopierten oder von Microsoft veröffentlichten Skills. Version 0.1.0; reale Host-/Tenant-Evaluation ausstehend.

## Versionsnachweise

`sources.lock.json` bindet jede Übernahme an Repository, vollständigen Git-Commit, ursprünglichen Pfad, Lizenz und SHA-256 pro Datei. `research/repositories.json` bewahrt die abgefragten Repository-Metadaten und Skill-Pfade auch für nicht übernommene Kandidaten. Die Originale werden durch den Git-Commit dieser Sammlung versioniert; bei eigenen Skill-Änderungen Versionsfeld und Hash aktualisieren.

## Ergänzung 0.2.0: Microsoft Learn

Offizielle Endpunkt- und Transportangaben anhand der [Microsoft-Dokumentation](https://learn.microsoft.com/en-us/training/support/mcp-developer-reference) geprüft. Neue eigene Arbeitsanweisung `microsoft-learn`; keine fremden Skills oder Dokumentation kopiert. MCP-Konfiguration mit Streamable HTTP, ohne Authentifizierung. Bestehende 16 Skills unverändert. Live-Testnachweise und Grenzen stehen in `research/microsoft-learn-validation.json`.

## Update 0.3.0: Work IQ

Offizieller MCP-Endpunkt und SharePoint-Funktionen anhand aktueller Microsoft-Learn-Seiten verifiziert. SharePoint Tools sind Public Preview. Client-ID aus dem offiziellen OpenAI-Paket in [microsoft/work-iq, Commit df79ddf](https://github.com/microsoft/work-iq/blob/df79ddf69e6ffd9e0dcc0eaaa40bd7477a3606cd/plugins/workiq/openai-submission/mcp.json). Das dortige Beispiel nennt einen älteren Act-Scope; diese Sammlung verwendet ausdrücklich den aktuellen dokumentierten Scope `api://workiq.svc.cloud.microsoft/WorkIQ.Act`. Dieser Unterschied und die veraltete Ask-only-Discovery werden nicht als bestätigte Schreibberechtigung dargestellt. Keine OAuth-Tokens oder Secrets eingebunden. Eigener Skill `workiq-sharepoint`; keine Kopie des breiten offiziellen WorkIQ-Skills. Anmeldung und authentifizierte Tooltests ausstehend. Die public Client-ID ist ein Bezeichner, kein Secret; ihre Akzeptanz für diese Verbindung muss der Host-Anmeldefluss bestätigen.
