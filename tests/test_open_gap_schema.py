from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def test_manifest_and_skills():
    a=yaml.safe_load((ROOT/'agent.yaml').read_text()); assert a['spec_version']=='0.1.0'; assert (ROOT/'SOUL.md').exists()
    for s in a['skills']:
        p=ROOT/'skills'/s/'SKILL.md'; assert p.exists(); assert p.read_text().startswith('---\n')
        data=yaml.safe_load(p.read_text().split('---',2)[1]); assert data['name']==s and data['description']
    for t in a['tools']:
        p=ROOT/'tools'/f'{t}.yaml'; assert p.exists(); data=yaml.safe_load(p.read_text()); assert data['name']==t; assert 'input_schema' in data
