#!/usr/bin/env python3
"""必要列 CRT 逐步合并增长分析。"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def inv(a,m): return pow(a,-1,m)
def crt_pair(a,m,b,n):
    t=((b-a)%n)*inv(m%n,n)%n
    return (a+m*t)%(m*n),m*n

def main():
    rows=json.loads((DOCS/'essential-crt-min-solution.json').read_text())['rows']
    out=[]
    for row in rows:
        x=0; mod=1; steps=[]
        for cg in row['congruences']:
            prev_x,prev_mod=x,mod
            x,mod=crt_pair(x,mod,cg['a'],cg['q'])
            steps.append({'q':cg['q'],'c':cg['c'],'a':cg['a'],'prev_x':prev_x,'prev_mod':prev_mod,'new_x':x,'new_mod':mod,'crosses_P':prev_x<row['P']<=x})
        out.append({'P':row['P'],'full_x':row['full_x'],'steps':steps,'first_cross_step':next((s for s in steps if s['new_x']>=row['P']),None)})
    audit={'certificate_type':'essential_crt_growth_steps','status':'CRT_delay_crosses_P_when_medium_prime_constraints_added','rows':out,'structural_conclusion':'必要列 CRT 解通常在加入中等或大素数约束时越过 P；P=23 特别早，但也是加入 q=7 后跨过 P，再由 13,17,19 精调到 x=58。','next_obligations':['证明必要列链中必存在一个中大素数约束使 CRT 代表跨过 P。','分析跨越前的模数骨架与新增 q 的相对位置。','将“跨越 P”转化为一般不等式。']}
    (DOCS/'essential-crt-growth-steps.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 必要列 CRT 逐步增长分析','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in out:
        lines.append(f"- P={r['P']} full_x={r['full_x']} first_cross={r['first_cross_step']}")
        lines.append('  steps=' + str([(s['q'],s['new_x'],s['new_mod']) for s in r['steps']]))
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'essential-crt-growth-steps.md').write_text('\n'.join(lines))
    print(DOCS/'essential-crt-growth-steps.json'); print(DOCS/'essential-crt-growth-steps.md')
if __name__=='__main__': main()
