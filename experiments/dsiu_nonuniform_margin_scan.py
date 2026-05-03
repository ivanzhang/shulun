#!/usr/bin/env python3
"""DSIU 非均匀余量扫描：统计 B/|U|、H_k、theta=B/(V W)。"""
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
    if n>=0: spf[0]=0
    if n>=1: spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j: spf[j]=i
    return spf

def fac(n:int,spf):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n:int,small): return all(n%p for p in small)

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); primes=primes_upto(P); spf=spf_sieve(P*P+P)
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    V=1.0
    for p in small: V*=1-1/p
    rows=[]
    h_prefix=[]; h=0.0; pi=0
    prime_set=set(primes)
    for k in range(1,P+1):
        if k in prime_set and D<k: h += 1/k
        h_prefix.append(h)
    for k in range(1,P+1):
        U=0; B=0; W=0
        for c in range(1,P+1):
            n=k*P+c
            if rough(n,small) and not any(n%p==0 for p in locks): U+=1
        for q in primes:
            if not (D<q<=k): continue
            a=k*P//q+1; b=(k*P+P)//q
            if a>b: continue
            W += b-a+1
            for m in range(a,b+1):
                if rough(m,small): B+=1
        H=h_prefix[k-1]
        theta=B/(V*W) if W else 0
        rows.append({'row':k,'U':U,'B':B,'W':W,'H':H,'theta':theta,'BH':B/U if U else 0,'thetaH':theta*H})
    top_BH=sorted(rows,key=lambda r:-r['BH'])[:10]
    top_thetaH=sorted(rows,key=lambda r:-r['thetaH'])[:10]
    buckets=[]
    for b in range(10):
        lo=b*P/10; hi=(b+1)*P/10
        rr=[r for r in rows if lo<r['row']<=hi]
        if rr:
            mx=max(rr,key=lambda r:r['BH'])
            buckets.append({'bucket':b,'row':mx['row'],'BH':mx['BH'],'H':mx['H'],'theta':mx['theta'],'thetaH':mx['thetaH'],'U':mx['U']})
    return {'P':P,'D':D,'V':V,'top_B_over_U':top_BH,'top_thetaH':top_thetaH,'buckets':buckets}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--max-p',type=int,default=1009)
    args=ap.parse_args()
    ps=[p for p in primes_upto(args.max_p) if p>=101]
    # 取若干代表，避免过慢。
    chosen=[p for p in ps if p in {101,251,503,997}] or ps[-4:]
    res=[analyze(P) for P in chosen]
    audit={'certificate_type':'dsiu_nonuniform_margin_scan','status':'nonuniform_margin_profile','results':res}
    (DOCS/'dsiu-nonuniform-margin-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU 非均匀余量扫描','','**状态：** `nonuniform_margin_profile`','','## 摘要']
    for it in res:
        t=it['top_B_over_U'][0]; th=it['top_thetaH'][0]
        lines.append(f"- P={it['P']} top B/U row={t['row']} B/U={t['BH']:.3f} H={t['H']:.3f} theta={t['theta']:.3f} thetaH={t['thetaH']:.3f}; top thetaH row={th['row']} thetaH={th['thetaH']:.3f} B/U={th['BH']:.3f}")
    lines+=['','## k/P 分桶 top B/U']
    for it in res:
        lines.append(f"- P={it['P']}: "+'; '.join(f"b{b['bucket']}:r={b['row']},B/U={b['BH']:.2f},H={b['H']:.2f},thH={b['thetaH']:.2f}" for b in it['buckets']))
    (DOCS/'dsiu-nonuniform-margin-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-nonuniform-margin-scan.md')
if __name__=='__main__': main()
