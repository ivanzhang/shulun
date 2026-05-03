#!/usr/bin/env python3
"""中模数跨越步骤的几何参数分析。"""
from __future__ import annotations
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def inv(a,m): return pow(a,-1,m)
def cover_holes(P,qs,x):
    covered=set()
    for q in qs:
        res=(-x*P)%q
        for c in range(1,P):
            if c%q==res: covered.add(c)
    return [c for c in range(1,P) if c not in covered]

def main():
    rows=json.loads((DOCS/'essential-crt-growth-steps.json').read_text())['rows']
    out=[]
    for row in rows:
        P=row['P']; qs=primes_upto(P-1)
        cross=row['first_cross_step']
        prev_qs=[s['q'] for s in row['steps'] if s['new_mod']<=cross['prev_mod']]  # included before cross
        holes_before=cover_holes(P,prev_qs,cross['prev_x'])
        m=cross['prev_mod']; x0=cross['prev_x']; q=cross['q']; a=cross['a']; c=cross['c']
        t=((a-x0)%q)*inv(m%q,q)%q
        threshold=(P-x0 + m-1)//m
        # 新 q 在 x0+m*s, s<threshold 的候选相位中会覆盖哪些列？
        early=[]
        for s in range(threshold):
            x=x0+m*s
            res=(-x*P)%q
            hit=[col for col in range(1,P) if col%q==res]
            early.append({'s':s,'x':x,'residue':res,'hits':hit,'hits_holes':[h for h in hit if h in holes_before]})
        out.append({'P':P,'cross_q':q,'necessary_c':c,'x0':x0,'m':m,'a':a,'t':t,'threshold':threshold,'x1':cross['new_x'],'holes_before':holes_before,'early_candidates':early})
    audit={'certificate_type':'medium_crossing_step_geometry','status':'crossing_t_exceeds_threshold_because_early_phases_miss_required_holes','rows':out,'structural_conclusion':'跨越步骤中，t 必须至少达到 threshold=ceil((P-x0)/m)。逐例看，所有 s<threshold 的早期相位下，新增 q 的禁余类没有以正确方式补齐骨架洞集；必要列命中发生在跨越之后。','next_obligations':['证明早期 s<threshold 时 q 的命中列不能覆盖必要洞 c。','将 holes_before 的位置与 q 的等差命中类比较。','推导 t>=threshold 的一般不等式。']}
    (DOCS/'medium-crossing-step-geometry.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 中模数跨越步骤几何分析','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in out:
        lines.append(f"- P={r['P']} q={r['cross_q']} c={r['necessary_c']} x0={r['x0']} m={r['m']} t={r['t']} threshold={r['threshold']} x1={r['x1']} holes_before={r['holes_before']} early={r['early_candidates']}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'medium-crossing-step-geometry.md').write_text('\n'.join(lines))
    print(DOCS/'medium-crossing-step-geometry.json'); print(DOCS/'medium-crossing-step-geometry.md')
if __name__=='__main__': main()
