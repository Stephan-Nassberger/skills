# Ausgeführte Validierung

Stand 14.11.2026.

- Sammlung: 16 eindeutige Skill-Namen und gültige YAML-Einstiegsmetadaten; alle 138 im Quellen-Lock erfassten Dateien stimmen mit ihren SHA-256-Werten überein.
- Alle lokalen Markdown-Dateiverweise in den Skill-Paketen und gemeinsamen Referenzen aufgelöst. URL-Erreichbarkeit und inhaltliche Richtigkeit sämtlicher externer Links sind damit nicht bewiesen.
- Zehn eigene Skills einzeln mit dem installierten skill-creator/quick_validate.py geprüft: 10 bestanden. Upstream-Skills unverändert behalten ihre zusätzlichen Frontmatterfelder; keine vollständige hostübergreifende Validator-Kompatibilität behauptet.
- Alle JSON-Dateien der Sammlung geparst; Manifest-Schema-ID und Untertitellänge geprüft. Das ist keine vollständige Validierung gegen das entfernte Plugin-Schema und kein Importtest.
- Plugin-Archiv erzeugt und wieder geöffnet: 16 SKILL.md-Einstiege auf portabler Ebene, 135 Dateien, ZIP-Integrität und lokale Dateiverweise geprüft.
- Bei der ersten Archivprüfung fehlte eine von MartiX referenzierte metadata.json. Der Paketfilter wurde korrigiert; erneuter Paketbau und Verweisprüfung bestanden. Die Prüfung ist jetzt Bestandteil von build_plugin.py.

## Noch ausstehend

ChatGPT-/Codex-Import, Skill-Routing-Evaluation, M365-/SharePoint-Tenant-Tests, SPFx-Build eines Zielprojekts, CLI-/MCP-Laufzeitprüfungen, Power-BI-Modelltests und produktive Deploymentprüfungen wurden nicht ausgeführt. Vorhandene Upstream-evals wurden nicht ausgeführt. Keine Aussage über funktionierende Tenant-Verbindungen, Berechtigungen, Premium-Lizenzen oder produktive Eignung.

## Wiederholen

```text
python scripts/validate_collection.py
python scripts/build_plugin.py --output ../m365-developer-skills-plugin.zip
```

Die Sammlung wurde statisch untersucht; die mitgelieferten Fremdskripte und Templates wurden nicht ausgeführt. Keine Geheimnisse oder Tenant-Inhalte wurden absichtlich aufgenommen.

## Update 0.2.0: Microsoft Learn

Die obigen Zahlen beziehen sich auf die Erstversion. Mit dem neuen originalen Microsoft-Learn-Skill: 17 Skills und 140 gesperrte Quelldateien. Der Paketbau enthält 138 Dateien einschließlich `mcp.json`. Struktur-/Hashprüfung und Skill-Validator erneut bestanden. Die bisherigen 16 Skill-Dateien wurden nicht geändert.

Das bestehende private Benutzer-Plugin wurde als Version 0.2.0 gespeichert. Portables `mcp.json`, generiertes `.mcp.json`, synchronisiertes Kompatibilitätsmanifest und der neue Skill wurden zurückgelesen. Die Plugin-Seite zeigt 17 Skills und einen Microsoft-Learn-MCP-Server. Das bestätigt die Konfiguration, nicht die Ausführung einer Suche im Host. Im bereits laufenden Agentenchat wurden noch keine neuen Learn-Tools angeboten; gegebenenfalls Desktop-Plugin aktualisieren und neuen Chat verwenden.

Endpunkt-Tests und konkrete Einschränkungen: `research/microsoft-learn-validation.json`. Keine Tenant- oder Work-IQ-Verbindung hinzugefügt.

Live-Endpunkttest mit offiziellem Python MCP SDK 2.3.0: Initialisierung und Tool-Discovery erfolgreich; `microsoft_docs_search` lieferte SharePoint-Formatierungsquellen, `microsoft_docs_fetch` den Column-Formatting-Artikel und `microsoft_code_sample_search` TypeScript-Beispiele zu Azure Functions. Alle drei Aufrufe lieferten Inhalte ohne Toolfehler. Kein Ausführungstest im ChatGPT-Host; die bestehenden Chats müssen die neue Konfiguration erst laden.

## Ablage im skills-Repository und Work IQ 0.3.0

18 Skill-Einstiege, 142 Quelldateien und 18 ergänzte UI-Metadatendateien. Die bisherigen 17 SKILL.md und ihre Upstream-Referenzen bleiben bytegleich; Pfade im Quellen-Lock und Paketbau wurden an die neue Ablage angepasst. Struktur-/Hashprüfung und portabler Paketbau erneut ausführen. Die aktualisierten Claude-Plugin-Verzeichniseinträge wurden statisch geprüft; `claude plugin validate . --strict` konnte mangels installierter Claude-CLI nicht ausgeführt werden. Work-IQ-Probe: 401 ohne Token, Authorization-Metadaten gelesen; authentifizierte Tool-/Pfad-Discovery sowie Tenant-Lese-/Schreibtests stehen aus. Siehe `research/workiq-validation.json`.

Das private Plugin wurde nach ausdrücklicher Zustimmung zum Scope WorkIQ.Act auf Version 0.3.0 aktualisiert. Gespeicherte Konfiguration und private Benutzerzuordnung wurden zurückgelesen. Damit ist die OAuth-Anforderung konfiguriert; eine Microsoft-Anmeldung, Tenant-Pfad-Discovery oder ein erfolgreicher Schreibtest sind damit nicht nachgewiesen.
