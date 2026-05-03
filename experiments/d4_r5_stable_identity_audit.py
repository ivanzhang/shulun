#!/usr/bin/env python3
"""D4/R5 stable 递推恒等式审计。"""
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    data = json.loads(Path("docs/d4-r5-recursive-peeling-probe.json").read_text())
    rows=[]
    worst=None
    for row in data['rows']:
        for prev, cur in zip(row['stats'], row['stats'][1:]):
            dL=cur['L']-prev['L']; dE=cur['E2']-prev['E2']
            shell_def=dE-dL*dL/20
            cross=-(prev['L']*dL)/10
            dD=cur['potential']-prev['potential']
            residual=dD-(shell_def+cross)
            item={'x':row['x'],'from_hi':prev['hi'],'to_hi':cur['hi'],'oldL':prev['L'],'dL':dL,'dE2':dE,'shell_def':shell_def,'cross':cross,'dD':dD,'identity_residual':residual,'needed_shell_minus_cross':shell_def+cross}
            rows.append(item)
            if worst is None or item['needed_shell_minus_cross']<worst['needed_shell_minus_cross']:
                worst=item
    payload={'certificate_type':'D4-R5-stable-identity-audit','identity':'D_new-D_old = shell_def - L_old*dL/10','rows':rows,'worst_shell_plus_cross':worst}
    Path('docs/d4-r5-stable-identity-audit.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
    print('worst', json.dumps(worst,ensure_ascii=False,indent=2))
    print('max residual', max(abs(r['identity_residual']) for r in rows))
    return 0
if __name__=='__main__': raise SystemExit(main())
