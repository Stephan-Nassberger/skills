# Plugin 0.2.0: Microsoft Learn

Das bestehende private Plugin wird um den offiziellen Microsoft-Learn-MCP-Dienst und einen eigenen Dokumentations-Skill ergänzt. Die 16 bisherigen Skills bleiben erhalten; insgesamt 17. Name, private Sichtbarkeit und Benutzerzuordnung bleiben gleich.

- Endpunkt: https://learn.microsoft.com/api/mcp
- Transport: Streamable HTTP
- Anmeldung: keine
- Fähigkeiten laut Microsoft: Dokumentationssuche, Artikelabruf, Codebeispielsuche. Tools und Schemas beim Verbindungsaufbau dynamisch ermitteln.
- Keine M365-Tenant-Berechtigungen, kein Graph-/SharePoint-Schreibzugriff.

Konfiguration: `mcp.json` in diesem Ordner; beim Paketbau liegt sie am Plugin-Wurzelverzeichnis. Nicht als gewöhnliche Webadresse im Browser testen.

```text
python scripts/validate_collection.py
python scripts/build_plugin.py --output ../m365-developer-skills-plugin.zip
```

Der Paketbau erhält Referenzen, Lizenzen und Herkunftsnachweise. Die Originale liegen weiterhin unter `skills/engineering/M365 Developer Skills`. Der Agent-Plugins-Importer kann zusätzliche Kompatibilitätsdateien erzeugen.

Ein gespeichertes Update ist noch kein Nachweis, dass der Host den neuen MCP-Dienst verbunden hat. Verbindungs- und Funktionstests getrennt dokumentieren; bei Bedarf Plugin im Host aktualisieren und einen neuen Chat öffnen. Zugang zu weiteren Power-Platform-/M365-Tools bleibt separat.

## Work IQ 0.3.0

Zweiter MCP-Dienst: `https://workiq.svc.cloud.microsoft/mcp`, delegiertes Microsoft-Entra-OAuth. Der aktuelle dokumentierte Scope für SharePoint-Änderungen ist `api://workiq.svc.cloud.microsoft/WorkIQ.Act` und enthält Lesen. `Ask` allein reicht nicht für `/sharepoint`-Pfade. Der öffentliche OAuth-Clientbezeichner stammt aus Microsofts eigenem OpenAI-Paket; der Host muss die Anmeldung und Zustimmung dennoch erfolgreich durchführen. Keine Credentials im Paket.

Nach Anmeldung zuerst Tools und `/sharepoint`-Schemas entdecken und die tatsächlich sichtbaren Pfade prüfen. Kein automatisches Aktivieren von Tenant-Richtlinien, keine Adminzustimmung durch dieses Paket und kein probeweises Schreiben. Live-Endpunkt liefert erwartungsgemäß 401 ohne Token. Die Discovery kündigt derzeit nur Ask an; ein eventuell fehlschlagender Act-Consent benötigt Klärung durch Microsoft/Tenant-Admin statt stiller Scope-Reduktion.
