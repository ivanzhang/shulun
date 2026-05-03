#!/usr/bin/env python3
"""FSC-II 长层扫描：分解 m>P 单点层与 m<=P 长层覆盖、重叠、空洞。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
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

def fac(n:int,spf):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n:int,small): return all(n%p for p in small)

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); spf=spf_sieve(P*P+P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    rows=[]
    for k in range(1,P+1):
        U=set(); single=set(); long=set(); both=set(); primes_cols=set()
        long_m=set(); single_m=set()
        for c in range(1,P+1):
            n=k*P+c
            if not rough(n,small): continue
            if any(n%p==0 for p in locks): continue
            U.add(c)
            if spf[n]==n:
                primes_cols.add(c); continue
            hit_s=False; hit_l=False
            for q in fac(n,spf):
                if D<q<P:
                    m=n//q
                    if rough(m,small):
                        if m>P:
                            hit_s=True; single_m.add(m)
                        else:
                            hit_l=True; long_m.add(m)
            if hit_s: single.add(c)
            if hit_l: long.add(c)
            if hit_s and hit_l: both.add(c)
        covered=single|long
        rows.append({'row':k,'U':len(U),'single':len(single),'long':len(long),'both':len(both),'union':len(covered),'holes':len(U)-len(covered),'prime_holes':len(primes_cols-set(covered)),'single_share':len(single)/len(U) if U else 0,'long_share':len(long)/len(U) if U else 0,'union_share':len(covered)/len(U) if U else 0,'overlap_share':len(both)/len(U) if U else 0,'long_m_count':len(long_m),'single_m_count':len(single_m)})
    top_union=sorted(rows,key=lambda r:(-r['union_share'],-r['U']))[:8]
    top_long=sorted(rows,key=lambda r:(-r['long_share'],-r['U']))[:8]
    return {'P':P,'D':D,'top_union':top_union,'top_long':top_long}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,503,997,2003')
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',')]
    res=[analyze(P) for P in ps]
    audit={'certificate_type':'fsc_ii_long_layer_scan','status':'single_long_layer_decomposition','results':res}
    (DOCS/'fsc-ii-long-layer-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC-II 长层覆盖分解扫描','','**状态：** `single_long_layer_decomposition`','','## 摘要']
    for it in res:
        u=it['top_union'][0]; l=it['top_long'][0]
        lines.append(f"- P={it['P']} topUnion row={u['row']} U={u['U']} union={u['union_share']:.3f} single={u['single_share']:.3f} long={u['long_share']:.3f} overlap={u['overlap_share']:.3f} holes={u['holes']} primeHoles={u['prime_holes']}; topLong row={l['row']} long={l['long_share']:.3f} union={l['union_share']:.3f}")
    lines+=['','## top union rows']
    for it in res:
        lines.append(f"- P={it['P']}")
        for r in it['top_union'][:5]:
            lines.append(f"  - row={r['row']} U={r['U']} union={r['union_share']:.3f} single={r['single_share']:.3f} long={r['long_share']:.3f} both={r['overlap_share']:.3f} holes={r['holes']} longM={r['long_m_count']} singleM={r['single_m_count']}")
    (DOCS/'fsc-ii-long-layer-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-ii-long-layer-scan.md')
if __name__=='__main__': main()
