#!/usr/bin/env python3
"""FSC-I q 尺度分解：把单点层覆盖按 q/P^a 尺度拆开。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from collections import defaultdict

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
                if spf[j]==j: spf[j]=i
    return spf

def fac(n:int,spf:list[int]):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n:int,small:list[int]): return all(n%p for p in small)

def bucket_q(q:int,P:int):
    # 指数桶：sqrtP, P^.6, P^.7, P^.8, P^.9, P
    exps=[0.6,0.7,0.8,0.9,1.0]
    for e in exps:
        if q <= P**e:
            return f"<=P^{e:.1f}"
    return '>P'

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); spf=spf_sieve(P*P+P); primes=primes_upto(P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    rows=[]
    for k in range(1,P+1):
        U=[]; col_buckets=defaultdict(set); hit_buckets=defaultdict(int)
        for c in range(1,P+1):
            n=k*P+c
            if not rough(n,small): continue
            if any(n%p==0 for p in locks): continue
            U.append(c)
            if spf[n]==n: continue
            for q in fac(n,spf):
                if D<q<=k: # 单点层必要 q<=k；此时 m>P 自动等价于 q<=k 对 n<=kP+P
                    m=n//q
                    if m>P and rough(m,small):
                        b=bucket_q(q,P)
                        col_buckets[b].add(c); hit_buckets[b]+=1
        if not U: continue
        covered=set().union(*col_buckets.values()) if col_buckets else set()
        # 调和容量同桶
        h=defaultdict(float)
        for q in primes:
            if D<q<=k:
                h[bucket_q(q,P)] += 1/q
        rows.append({'row':k,'U':len(U),'share':len(covered)/len(U),'covered':len(covered),'bucket_cols':{b:len(s) for b,s in col_buckets.items()},'bucket_hits':dict(hit_buckets),'bucket_hsum':dict(h)})
    top=sorted(rows,key=lambda r:(-r['share'],r['U']))[:5]
    return {'P':P,'D':D,'top':top}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='503,997,2003')
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',') if x.strip()]
    res=[analyze(P) for P in ps]
    audit={'certificate_type':'fsc_i_q_scale_decomposition','status':'q_scale_contribution_profile','results':res}
    (DOCS/'fsc-i-q-scale-decomposition.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC-I q 尺度分解','','**状态：** `q_scale_contribution_profile`','','## 最高单点覆盖行']
    for it in res:
        r=it['top'][0]
        lines.append(f"- P={it['P']} row={r['row']} U={r['U']} share={r['share']:.3f} covered={r['covered']}")
        lines.append(f"  - cols={r['bucket_cols']}")
        lines.append(f"  - hsum={{{', '.join(f'{k}:{v:.3f}' for k,v in sorted(r['bucket_hsum'].items()))}}}")
    (DOCS/'fsc-i-q-scale-decomposition.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-i-q-scale-decomposition.md')
if __name__=='__main__': main()
