---
name: workiq-sharepoint
description: Use the official Work IQ MCP service for authorized SharePoint Online lists, columns, views, JSON formatting, libraries, files, versions, approvals and quick steps. Discover live /sharepoint paths and schemas before reading or changing tenant resources.
license: MIT
metadata:
  version: "0.1.0"
---

# SharePoint actions through Work IQ

Original integration workflow for this collection. The service is Microsoft's; this skill is not a Microsoft-authored package. Use Microsoft Learn for public documentation and Work IQ for tenant operations.

## Establish the connection

- Use the configured `https://workiq.svc.cloud.microsoft/mcp` service and host-managed Microsoft Entra delegated OAuth. Do not extract browser tokens, store credentials in this repository, or substitute an unrelated service when authentication fails.
- Discover the authorization metadata URL from the actual HTTP authentication challenge. The observed challenge points to `https://workiq.svc.cloud.microsoft/.well-known/oauth-protected-resource/mcp`; do not assume the suffix-free URL works.
- For SharePoint tools, current Microsoft documentation specifies `api://workiq.svc.cloud.microsoft/WorkIQ.Read` for reads and `api://workiq.svc.cloud.microsoft/WorkIQ.Act` for changes (including reads). `WorkIQAgent.Ask` alone hides /sharepoint paths. User permissions and tenant policy remain additional constraints.
- The observed public metadata currently advertises only an Ask scope, while current documentation describes Read/Act. Record this difference if it blocks sign-in or path discovery; do not silently downgrade to Ask and claim SharePoint actions are enabled.
- Check the actual signed-in organization and authorized site before accessing content. Admin consent, tenant enablement, policy or licensing may require user/admin action. This skill does not authorize changing any of those settings.

## Discover before operating

1. Load current MCP tool definitions from the connected service. Use its advertised `search_paths` and `get_schema` to discover the relevant /sharepoint resource paths and method schemas. Do not fabricate per-operation tool names or copy an assumed Graph URL into a SharePoint-IQ path.
2. Resolve the user's site, list/library, field, view, item or file to the exact returned identity. Read current state and relevant metadata before proposing the smallest change. Preserve internal field names, existing data, required columns, view settings and unrelated configuration.
3. For column or view formatting, use the corresponding JSON-formatting skill to build and validate the formatter against real field types. Present the concrete JSON/change when review is needed, then apply it only through an advertised, authorized update operation. Read back the saved formatter.
4. For list/library schema, files, folders, metadata and versions, inspect each operation's preconditions, concurrency and response contract. Use ETags/version checks where specified. On conflicts, reread and reconcile; do not blindly overwrite. Follow supported pagination and distinguish incomplete results from empty collections.
5. For approvals, eSignature tracking and quick steps, use only currently discovered capabilities and the user's requested scope. Do not equate tracking signature requests with authority to sign a legal agreement or assume every workflow can be initiated.
6. Use the discovered entity/action tool matching the method. Never interpret endpoint setup as permission to execute a write, send a sharing notification, change access or deploy an SPFx package. Existing explicit authorization persists; request only genuinely missing decisions or action-time approvals required by the host.
7. For a timeout or ambiguous write, inspect saved state before retrying. An accepted/pending response is not completion. Report partial batch success and unresolved operations accurately.
8. Finish with the actual affected resource links, read-back evidence and remaining limitations. Never claim tenant write access merely because the plugin manifest contains an OAuth scope.

## Test without changing tenant data

After sign-in, verify tool discovery, then discover /sharepoint paths and inspect a user-selected site's list/library schema. Do not create lists, alter formatting or start approvals merely to test connectivity. A write test needs a named test target and authorized intended change.

## Sources

- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/sharepoint-iq
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/tool-reference
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/permissions
