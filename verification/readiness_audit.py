from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
required=['agent.yaml','SOUL.md','README.md','EXPLAINABILITY.md','RULES.md','DUTIES.md','AGENTS.md']
missing=[x for x in required if not (ROOT/x).exists()]
if missing: print('READINESS AUDIT: FAIL'); print('Missing:', ', '.join(missing)); sys.exit(1)
a=yaml.safe_load((ROOT/'agent.yaml').read_text())
errors=[]
for s in a.get('skills',[]):
 p=ROOT/'skills'/s/'SKILL.md'
 if not p.exists() or not p.read_text().startswith('---\n'): errors.append(f'skill {s}')
for t in a.get('tools',[]):
 for ext in ('.yaml', '.py'):
  if not (ROOT/'tools'/f'{t}{ext}').exists(): errors.append(f'tool {t}{ext}')
if errors: print('READINESS AUDIT: FAIL'); print('\n'.join(errors)); sys.exit(1)
print('READINESS AUDIT: PASS')
print('Checked required manifest, documentation, skills, and tools.')
