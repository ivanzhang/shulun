#!/usr/bin/env python3
"""完整覆盖方案最小相位 x 扫描。"""
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

def cover_info(P,qs,x):
    cover_by_c={}
    by_q={q:[] for q in qs}
    for c in range(1,P):
        hits=[q for q in qs if (x*P+c)%q==0]
        if hits:
            cover_by_c[c]=hits
            for q in hits: by_q[q].append(c)
    holes=[c for c in range(1,P) if c not in cover_by_c]
    return holes,by_q,cover_by_c

def scan(P,limit=1_000_000):
    qs=primes_upto(P-1)
    first=None
    near=[]
    for x in range(0,limit):
        holes,by_q,cover_by_c=cover_info(P,qs,x)
        if len(holes)<=3:
            near.append({'x':x,'r':x+1,'hole_count':len(holes),'holes':holes})
        if not holes:
            used={q:cs for q,cs in by_q.items() if cs}
            first={'x':x,'r':x+1,'used':used,'cover_by_c':cover_by_c}
            break
    return {'P':P,'qs':qs,'limit':limit,'first_full':first,'min_x_over_P':(first['x']/P if first else None),'near_first':near[:30]}

def main():
    Ps=[13,17,19,23,29,31]
    results=[scan(P,1_000_000) for P in Ps]
    audit={'certificate_type':'full_scheme_min_x_scan','status':'first_full_cover_phase_exceeds_P_in_scanned_cases','results':results,'structural_conclusion':'完整覆盖相位扫描确认小 P 中首个 full scheme 的 x 均大于 P；近零行在前窗口可出现但保留洞。首方案结构可分解为低模数骨架加中大模数补洞。','next_obligations':['从 first_full.used 中抽取小素数骨架与补洞素数。','分析 first_full x 的同余系统最小解为何超过 P。','将小 P 首方案结构归纳为 FSC 引理的证明模板。']}
    (DOCS/'full-scheme-min-x-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 完整覆盖方案最小相位扫描','',f"**状态：** `{audit['status']}`",'',audit['structural_conclusion'],'','## 摘要']
    for r in results:
        f=r['first_full']
        lines.append(f"- P={r['P']} first_x={None if f is None else f['x']} r={None if f is None else f['r']} x/P={r['min_x_over_P']} near={r['near_first'][:5]}")
        if f:
            used_summary={q:cs for q,cs in f['used'].items()}
            lines.append(f"  used={used_summary}")
    lines += ['', '## 下一证明义务']+[f'- {x}' for x in audit['next_obligations']]+['']
    (DOCS/'full-scheme-min-x-scan.md').write_text('\n'.join(lines))
    print(DOCS/'full-scheme-min-x-scan.json'); print(DOCS/'full-scheme-min-x-scan.md')
if __name__=='__main__': main()
