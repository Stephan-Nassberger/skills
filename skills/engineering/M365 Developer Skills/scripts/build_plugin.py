from pathlib import Path
import argparse,hashlib,json,zipfile,posixpath,re,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args();out=Path(args.output).resolve()
 if out.is_relative_to(ROOT):raise SystemExit('Choose an output outside the source repository')
 entries={};prefix='m365-developer-skills/'
 for skill in json.loads((ROOT/'sources.lock.json').read_text())['sources']:
  for p in (ROOT/skill['name']).rglob('*'):
   if not p.is_file():continue
   rel=p.relative_to(ROOT)
   if p.name in ['plugin.json','.markdownlint.json','README.md'] or 'evals' in rel.parts:continue
   entries[prefix+'skills/'+rel.as_posix()]=p.read_bytes()
 for p in (ROOT.parent/'common').rglob('*'):
  if p.is_file():entries[prefix+'common/'+p.relative_to(ROOT.parent/'common').as_posix()]=p.read_bytes()
 for name in ['LICENSE','THIRD_PARTY_NOTICES.md','sources.lock.json']:
  entries[prefix+name]=(ROOT/name).read_bytes()
 entries[prefix+'plugin.json']=(ROOT/'plugin-preparation/plugin.json').read_bytes()
 entries[prefix+'mcp.json']=(ROOT/'plugin-preparation/mcp.json').read_bytes()
 for name,data in entries.items():
  if not name.endswith('.md'):continue
  for target in re.findall(r'\]\(([^)]+)\)',data.decode('utf-8')):
   target=target.split('#')[0].split(' "')[0].strip('<>')
   if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target) or '${' in target:continue
   dest=posixpath.normpath(posixpath.join(posixpath.dirname(name),urllib.parse.unquote(target)))
   if dest not in entries and not any(n.startswith(dest.rstrip('/')+'/') for n in entries):
    raise SystemExit(f'Broken packaged reference: {name} -> {target}')
 entries[prefix+'package-files.json']=(json.dumps({p:hashlib.sha256(b).hexdigest() for p,b in sorted(entries.items())},indent=2)+'\n').encode()
 out.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for name,b in sorted(entries.items()):
   info=zipfile.ZipInfo(name,date_time=(2026,11,14,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,b)
 with zipfile.ZipFile(out) as z:
  if z.testzip():raise SystemExit('Corrupt archive')
  manifest=json.loads(z.read(prefix+'plugin.json'));names=[n for n in z.namelist() if n.endswith('/SKILL.md')];assert len(names)==len(json.loads((ROOT/'sources.lock.json').read_text())['sources'])
  for name in names:assert len(name.split('/'))==4
 print(json.dumps({'archive':str(out),'skills':len(names),'files':len(entries),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'status':'packaged; not imported or runtime-tested'},indent=2))
if __name__=='__main__':main()

