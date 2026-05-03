#!/usr/bin/env python3
"""D4/R5 jump 吸收审计。"""
from __future__ import annotations
import json
from pathlib import Path


def badness(s: dict) -> dict:
    """几类坏度：light 超界、高质量势能负、U/V 超界。"""
    return {
        'light_over_026': max(0, s['light_L']-0.26),
        'potential_deficit': max(0, -s['potential']),
        'U_over_0182': max(0, s['U']-0.182),
        'V_over_0074': max(0, s['V']-0.074),
        'L_highmass': max(0, s['L']-0.35),
    }


def main() -> int:
    probe=json.load(open('docs/d4-r5-recursive-peeling-probe.json'))
    cls=json.load(open('docs/d4-r5-recursive-transitivity-classification.json'))
    kind={(r['x'],s['from_hi'],s['to_hi']):s['kind'] for r in cls['rows'] for s in r['steps']}
    jumps=[]
    for row in probe['rows']:
        for prev,cur in zip(row['stats'], row['stats'][1:]):
            if kind[(row['x'],prev['hi'],cur['hi'])]=='jump':
                bp=badness(prev); bc=badness(cur)
                jumps.append({'x':row['x'],'from_hi':prev['hi'],'to_hi':cur['hi'],'before':prev,'after':cur,'bad_before':bp,'bad_after':bc,'bad_delta':{k:bc[k]-bp[k] for k in bp}})
    payload={'certificate_type':'D4-R5-jump-absorption-audit','jumps':jumps,'jump_count':len(jumps),'all_jump_badness_nonincreasing':all(all(v<=1e-15 for v in j['bad_delta'].values()) for j in jumps)}
    Path('docs/d4-r5-jump-absorption-audit.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
    print(json.dumps(payload,ensure_ascii=False,indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
