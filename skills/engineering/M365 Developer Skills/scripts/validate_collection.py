from pathlib import Path
import argparse,hashlib,json,re,sys,urllib.parse
import yaml
ROOT=Path(__file__).resolve().parents[1]
def validate():
 errors=[]; lock=json.loads((ROOT/'sources.lock.json').read_text());names=[];count=0
 for source in lock['sources']:
  p=ROOT/source['name']/'SKILL.md'; text=p.read_text(encoding='utf-8'); meta=yaml.safe_load(text.split('---',2)[1]);names.append(meta.get('name'))
  if meta.get('name')!=p.parent.name or not isinstance(meta.get('description'),str) or not meta['description'].strip():errors.append(f'Invalid skill metadata: {p}')
  if p.stat().st_size>1048576:errors.append(f'Oversized skill: {p}')
  if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',meta['name']):errors.append(f'Invalid name: {p}')
  if source['origin']=='original' and not (p.parent/'LICENSE').exists():errors.append(f'Missing original license: {p}')
  if source['origin']!='original' and not any('LICENSE' in f.name.upper() for f in p.parent.iterdir()):errors.append(f'Missing upstream license: {p}')
  for f in source['files']+source.get('collection_files',[]):
   target=(ROOT/f['path']).resolve()
   if not (target.is_relative_to(ROOT) or target.is_relative_to(ROOT.parent/'common')):errors.append('Unsafe source path');continue
   if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=f['sha256']:errors.append(f'Integrity mismatch: {target}')
   count+=1
 if len(names)!=len(set(names)):errors.append('Duplicate names')
 # Validate every local reference in imported/original skill docs and shared dependencies.
 for folder in [*[ROOT/s['name'] for s in lock['sources']],ROOT.parent/'common']:
  for p in folder.rglob('*.md'):
   for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
    target=target.split('#')[0].split(' "')[0].strip('<>')
    if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target) or '${' in target:continue
    resolved=(p.parent/urllib.parse.unquote(target)).resolve()
    if not (resolved.is_relative_to(ROOT) or resolved.is_relative_to(ROOT.parent/'common')) or not resolved.exists():errors.append(f'Broken/escaping reference: {p} -> {target}')
 manifest=json.loads((ROOT/'plugin-preparation/plugin.json').read_text(encoding='utf-8'))
 if manifest['$schema']!='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':errors.append('Invalid plugin schema identifier')
 if len(manifest['extensions']['com.openai']['interface']['shortDescription'])>30:errors.append('Subtitle too long')
 mcp=json.loads((ROOT/'plugin-preparation/mcp.json').read_text())
 if mcp.get('$schema')!='https://agent-plugins.org/schemas/1.0.0/mcp.schema.json':errors.append('Invalid MCP schema identifier')
 server=mcp.get('mcpServers',{}).get('microsoft-learn',{})
 if server.get('type')!='streamable-http' or server.get('url')!='https://learn.microsoft.com/api/mcp':errors.append('Unexpected Learn endpoint or transport')
 if server.get('extensions',{}).get('com.openai',{}).get('auth',{}).get('type')!='none':errors.append('Unexpected Learn authentication')
 wiq=mcp.get('mcpServers',{}).get('workiq',{})
 if wiq.get('url')!='https://workiq.svc.cloud.microsoft/mcp' or wiq.get('type')!='streamable-http':errors.append('Invalid Work IQ endpoint/transport')
 auth=wiq.get('extensions',{}).get('com.openai',{}).get('auth',{})
 if auth.get('type')!='oauth' or auth.get('defaultScopes')!=['api://workiq.svc.cloud.microsoft/WorkIQ.Act']:errors.append('Invalid Work IQ delegated action scope')
 for p in ROOT.rglob('*.json'):
  if '.git' not in p.parts:json.loads(p.read_text(encoding='utf-8'))
 print(json.dumps({'skills':len(names),'locked_files_checked':count,'errors':errors},indent=2))
 return not errors
if __name__=='__main__':sys.exit(0 if validate() else 1)
