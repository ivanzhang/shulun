#!/usr/bin/env python3
"""DSIU 容量区扫描：仅统计 H_k<=阈值区域的 theta 最大值。"""
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
                if spf[j]==j: spf[j]=i
    return spf

def fac(n:int,spf):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0:n//=p
    return out

def rough(n:int,small): return all(n%p for p in small)

def analyze(P:int,H0:float):
    D=math.isqrt(P); small=primes_upto(D); primes=primes_upto(P); spf=spf_sieve(P*P+P)
    V=1.0
    for p in small: V*=1-1/p
    locks=set(fac(P-1,spf)+fac(P+1,spf))
    H=0.0; Hs={}
    prime_set=set(primes)
    for k in range(1,P+1):
        if k in prime_set and D<k: H+=1/k
        Hs[k]=H
    recs=[]
    for k in range(1,P+1):
        if Hs[k]>H0: continue
        U=0; B=0; W=0
        for c in range(1,P+1):
            n=k*P+c
            if rough(n,small) and not any(n%p==0 for p in locks): U+=1
        for q in primes:
            if D<q<=k:
                a=k*P//q+1; b=(k*P+P)//q
                if a<=b:
                    W+=b-a+1
                    for m in range(a,b+1):
                        if rough(m,small): B+=1
        theta=B/(V*W) if W else 0
        recs.append({'row':k,'H':Hs[k],'U':U,'B':B,'W':W,'theta':theta,'BH':B/U if U else 0,'thetaH':theta*Hs[k]})
    top_theta=max(recs,key=lambda r:r['theta']) if recs else None
    top_thetaH=max(recs,key=lambda r:r['thetaH']) if recs else None
    top_BH=max(recs,key=lambda r:r['BH']) if recs else None
    return {'P':P,'D':D,'H0':H0,'count':len(recs),'top_theta':top_theta,'top_thetaH':top_thetaH,'top_BH':top_BH}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,503,997'); ap.add_argument('--H0',type=float,default=0.55)
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',') if x.strip()]
    res=[analyze(P,args.H0) for P in ps]
    audit={'certificate_type':'dsiu_capacity_region_scan','status':'capacity_region_theta_profile','results':res}
    (DOCS/'dsiu-capacity-region-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU 容量区扫描','',f"**状态：** `{audit['status']}`",f"容量阈值 H0={args.H0}。",'','## 摘要']
    for r in res:
        tt=r['top_theta']; th=r['top_thetaH']; tb=r['top_BH']
        lines.append(f"- P={r['P']} rows={r['count']} topTheta row={tt['row']} theta={tt['theta']:.3f} H={tt['H']:.3f}; topThetaH row={th['row']} thetaH={th['thetaH']:.3f}; topB/U row={tb['row']} B/U={tb['BH']:.3f} H={tb['H']:.3f}")
    (DOCS/'dsiu-capacity-region-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-capacity-region-scan.md')
if __name__=='__main__': main()
