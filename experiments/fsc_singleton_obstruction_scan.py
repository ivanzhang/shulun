#!/usr/bin/env python3
"""FSC-I 单点层障碍扫描：分析最高覆盖行中单点双粗匹配的 q,m 分布与互斥约束。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i):s[j]=False
    return [i for i,v in enumerate(s) if v]

def spf_sieve(n:int):
    spf=list(range(n+1))
    if n>=0:spf[0]=0
    if n>=1:spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j:spf[j]=i
    return spf

def fac(n:int,spf:list[int]):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n:int,small:list[int]): return all(n%p for p in small)

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); spf=spf_sieve(P*P+P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    rows=[]
    for k in range(1,P+1):
        U=[]; covered={}; qcnt=Counter(); mcnt=Counter(); qbands=Counter(); mbands=Counter()
        for c in range(1,P+1):
            n=k*P+c
            if not rough(n,small): continue
            if any(n%p==0 for p in locks): continue
            U.append(c)
            if spf[n]==n: continue
            hits=[]
            for q in fac(n,spf):
                if D<q<P:
                    m=n//q
                    if rough(m,small):
                        hits.append((q,m))
                        qcnt[q]+=1; mcnt[m]+=1
                        qbands[int(10*q/P)]+=1
                        mbands[int(10*m/P)]+=1
            if hits: covered[c]=hits
        if not U: continue
        singleton_m=sum(1 for m,v in mcnt.items() if v==1)
        singleton_q=sum(1 for q,v in qcnt.items() if v==1)
        rows.append({
            'row':k,'U':len(U),'covered':len(covered),'holes':len(U)-len(covered),'share':len(covered)/len(U),
            'hit_count':sum(len(v) for v in covered.values()),
            'distinct_q':len(qcnt),'distinct_m':len(mcnt),
            'singleton_m_share':singleton_m/len(mcnt) if mcnt else 0,
            'singleton_q_share':singleton_q/len(qcnt) if qcnt else 0,
            'max_m_reuse':max(mcnt.values()) if mcnt else 0,
            'max_q_reuse':max(qcnt.values()) if qcnt else 0,
            'multi_hit_cols':sum(1 for v in covered.values() if len(v)>1),
            'qbands':dict(qbands),'mbands':dict(mbands),
            'sample_holes':U[:5] if len(covered)==0 else [c for c in U if c not in covered][:10],
        })
    top=sorted(rows,key=lambda r:(-r['share'],-r['U']))[:5]
    return {'P':P,'D':D,'top_cover':top}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,331,503,701,997')
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',') if x.strip()]
    res=[analyze(P) for P in ps]
    audit={'certificate_type':'fsc_singleton_obstruction_scan','status':'singleton_layers_are_injective_but_not_contradictory_yet','results':res}
    (DOCS/'fsc-singleton-obstruction-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC-I 单点层障碍扫描','','**状态：** `singleton_layers_are_injective_but_not_contradictory_yet`','','## 摘要']
    for it in res:
        r=it['top_cover'][0]
        lines.append(f"- P={it['P']} row={r['row']} share={r['share']:.3f} U={r['U']} holes={r['holes']} hits={r['hit_count']} q={r['distinct_q']} m={r['distinct_m']} singM={r['singleton_m_share']:.2f} singQ={r['singleton_q_share']:.2f} maxReuse(m,q)=({r['max_m_reuse']},{r['max_q_reuse']}) multiCols={r['multi_hit_cols']}")
    lines+=['','## 最高覆盖行分带']
    for it in res:
        r=it['top_cover'][0]
        lines.append(f"- P={it['P']} row={r['row']} qbands={r['qbands']} mbands={r['mbands']} holes={r['sample_holes']}")
    (DOCS/'fsc-singleton-obstruction-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-singleton-obstruction-scan.md')
if __name__=='__main__': main()
