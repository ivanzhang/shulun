#!/usr/bin/env python3
"""D4/R5 stable-capacity 支付账本审计。"""
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    data=json.load(open('docs/d4-r5-stable-identity-audit.json'))
    classif=json.load(open('docs/d4-r5-recursive-transitivity-classification.json'))
    kinds={(s['x'],step['from_hi'],step['to_hi']):step['kind'] for s in classif['rows'] for step in s['steps']}
    rows=[]; byx={}
    for r in data['rows']:
        kind=kinds[(r['x'],r['from_hi'],r['to_hi'])]
        neg=max(0,-r['dD'])
        pay=max(0, r['oldL']*max(0,r['dL'])/10)
        item={**r,'kind':kind,'negative_D_drop':neg,'capacity_payment':pay,'covered_by_payment': neg <= pay + 1e-15}
        rows.append(item); byx.setdefault(r['x'],[]).append(item)
    summaries=[]
    for x,items in byx.items():
        stable=[i for i in items if i['kind']=='stable']
        summaries.append({
            'x':x,
            'stable_steps':len(stable),
            'sum_negative_D_drop':sum(i['negative_D_drop'] for i in stable),
            'sum_capacity_payment':sum(i['capacity_payment'] for i in stable),
            'all_drops_covered':all(i['covered_by_payment'] for i in stable),
            'final_L': items[-1]['oldL']+items[-1]['dL'],
        })
    payload={'certificate_type':'D4-R5-capacity-payment-audit','identity':'negative D drops are paid by L_old*dL/10 on stable positive-mass steps','summaries':summaries,'rows':rows,'all_stable_drops_covered':all(i['covered_by_payment'] for i in rows if i['kind']=='stable')}
    Path('docs/d4-r5-capacity-payment-audit.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in payload.items() if k!='rows'},ensure_ascii=False,indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
