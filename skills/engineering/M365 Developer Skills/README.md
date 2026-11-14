# M365 Developer Skills

Kuratierte Sammlung für Microsoft 365 und SharePoint. Stand: **14.11.2026**. **18 Skills: 6 übernommene Pakete, 12 eigene Ergänzungen.** Kein Microsoft-zertifiziertes Produkt; kein Zugriff auf einen Tenant und keine automatische Bereitstellung.

## Schnellzugriff

- [Alle Skills und Herkunft](CATALOG.md)
- [Recherche, Lizenz- und Qualitätsprüfung](RESEARCH.md)
- [Attribution und Lizenzgrenzen](THIRD_PARTY_NOTICES.md)
- [Commit- und Datei-Nachweise](sources.lock.json)
- [Plugin-Vorbereitung](plugin-preparation/README.md)
- [Ausgeführte Prüfungen und Grenzen](VALIDATION.md)

## Abdeckung

| Thema | Skill |
|---|---|
| Aktuelle Microsoft-Dokumentation und Codebeispiele | `microsoft-learn` + offizieller Learn-MCP-Dienst |
| PnP PowerShell, Provisionierung, CLI, PnPjs | `martix-sharepoint-pnp` |
| PnP Modern Search v4 | `pnp-modern-search` |
| JSON Column Formatting | `sharepoint-json-column-formatting` |
| JSON View Formatting | `sharepoint-json-view-formatting` |
| SPFx Webparts, Upgrade, React, PnPjs | `spfx` |
| Application Customizer, Field/Command/Form Customizer, HTML | `sharepoint-html-spfx-extensions` + `spfx` |
| Teams Apps, Bots, SSO, Migration | `teams-dev` |
| Adaptive Cards, hostbezogene Aktionen | `adaptive-cards-m365` |
| Power Automate | `power-automate-development` |
| Power Apps und SharePoint-Formulare | `power-apps-development` |
| Power BI/Fabric Semantic Models | `semantic-model-authoring` |
| Microsoft Graph SDK | `msgraph-sdk` |
| Azure Functions für M365 | `azure-functions-m365` |
| Fluent UI | `martix-fluent-ui` |
| Microsoft Forms | `microsoft-forms-integration` |
| Planner | `planner-development` |

Power BI-Berichtsdesign ist noch kein eigenes installiertes Skill-Paket; zusätzliche echte Kandidaten sind in RESEARCH.md verlinkt. Anleitungen ersetzen keine CLI, MCP-Verbindung, Anmeldung, Lizenz oder Berechtigung. Bestehende Architektur und explizite Nutzeranweisungen gehen den Meinungen einzelner Upstream-Skills vor.

## Warum kuratieren statt alles forken?

Die Quellen sind verschieden geschnitten: einzelne Skills, große Plugin-Marktplätze, Produktquellcode oder reine Beispielsammlungen. Ein Sammel-Fork würde diese Unterschiede und Abhängigkeiten nicht lösen. Deshalb gezielte, versionierte Übernahmen samt unterstützenden Dateien und Lizenztexten; keine Forks angelegt. Für spätere Beiträge am Upstream wäre ein gezielter Fork sinnvoll.

## Verwendung

Die Sammlung unter `skills/engineering/M365 Developer Skills` ist die nachvollziehbare Quelle. Er ist wegen des zusätzlichen Ordnerlevels **kein direkt importierbares ChatGPT-Plugin**. Die Plugin-Vorbereitung erzeugt daraus die portable Struktur `skills/<name>/SKILL.md` und erhält gemeinsame Referenzen und Lizenzen. Das private Plugin ist angelegt; Version 0.2.0 ergänzt die Microsoft-Learn-MCP-Konfiguration. Der konkrete Verbindungsstatus steht in der Validierungsdokumentation.

## Pflege

Neue Quellen erst nach Prüfung von echtem SKILL.md, passendem Anwendungsbereich, Lizenztext, relativen Abhängigkeiten und Tool-Voraussetzungen aufnehmen. Updates gezielt über Branch/PR mit neuem Upstream-Commit, Hashes und Änderungsprüfung; keine automatischen Updates auf ungeprüftes `main`. Ursprungsdateien nicht als eigene Arbeit ausgeben. Keine Tenant-Daten oder Zugangsdaten veröffentlichen.

Originale Inhalte stehen unter MIT; übernommene Pakete behalten ihre jeweiligen MIT-/Apache-2.0-Bedingungen. Siehe THIRD_PARTY_NOTICES.md.

## Microsoft Learn ab 0.2.0

[Verbindungskonfiguration](plugin-preparation/mcp.json) für `https://learn.microsoft.com/api/mcp`, ohne Anmeldung. Der neue [Microsoft-Learn-Skill](microsoft-learn/SKILL.md) beschreibt Suche, Artikelabruf, Codebeispiele und PnP-Ergänzungsquellen. Die Verbindung liefert öffentliche Dokumentation, keinen Tenant-Zugriff.

## Repository-Struktur

Diese Sammlung liegt im bestehenden Matt-Pocock-Fork `Stephan-Nassberger/skills` unter `skills/engineering/M365 Developer Skills`. Die 17 Skill-Ordner liegen direkt hier. Gemeinsame Fabric-Referenzen liegen als unterstützende Dateien in `../common`, damit die unveränderten relativen Upstream-Verweise funktionieren. Der Paketbau erhält die bisherige portable Pluginstruktur. Das bisherige Repository `m365-developer-skills` bleibt als Herkunftsstand bestehen; das installierte private Plugin wurde durch diese Ablageänderung nicht neu veröffentlicht.

## Work IQ ab 0.3.0

Zusätzlich zu Microsoft Learn enthält die Konfiguration jetzt `https://workiq.svc.cloud.microsoft/mcp` mit delegiertem OAuth und dem dokumentierten SharePoint-Aktionsscope. Insgesamt 18 Skills (6 Übernahmen, 12 eigene). Der [Work-IQ-SharePoint-Skill](workiq-sharepoint/SKILL.md) beschreibt Schema-Discovery, Lesen/Ändern und Verifikation. Anmeldung, Adminzustimmung und wirksame Tenant-Richtlinien stehen einem konkreten Zugriff voraus; Paketkonfiguration allein bestätigt keinen funktionierenden Schreibzugriff.
