import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    p=ROOT/'tools'/name
    s=importlib.util.spec_from_file_location(p.stem.replace('-','_'),p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_mobility():
    m=load('analyze-mobility-status.py'); assert m.analyze({'mode':'bus','availability':'available','delay_minutes':5,'occupancy_percent':40})['status']=='normal'

def test_traffic():
    m=load('analyze-traffic-conditions.py'); assert m.analyze({'average_speed_kmh':20,'reference_speed_kmh':50,'incidents':0})['condition']=='congested'

def test_plan():
    m=load('plan-mobility-option.py'); r=m.plan({'options':[{'name':'A','time_minutes':20,'cost':10,'congestion':50},{'name':'B','time_minutes':40,'cost':5,'congestion':80}], 'weights':{'time':2,'cost':1,'congestion':1}}); assert r['selected']=='A'

def test_reject_unexpected():
    m=load('analyze-mobility-status.py')
    try: m.analyze({'mode':'bus','availability':'available','delay_minutes':0,'occupancy_percent':0,'x':1}); assert False
    except ValueError: pass
