#!/usr/bin/env python3
"""Beta-multisample 相位区制扫描：按 dyadic Q 与 l 统计相位变化 A/(lQ)。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from math import gcd

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

def mu_squarefree_products(primes,limit):
    out={1:1}
    for p in primes:
        for x,mu in list(out.items()):
            y=x*p
            if y<=limit: out[y]=-mu
    return out

def coeffs(P,rho):
    D=math.isqrt(P); R=int(P**rho); small=primes_upto(D); mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    c={}; ds=list(lamb)
    for d in ds:
        for e in ds:
            l=d//gcd(d,e)*e; c[l]=c.get(l,0.0)+lamb[d]*lamb[e]
    return c

def analyze(P,k,rho):
    D=math.isqrt(P); c=coeffs(P,rho); primes=primes_upto(k); A=k*P
    blocks=[]; Q=1
    while Q<=k:
        qcnt=sum(1 for q in primes if max(D,Q)<q<=min(2*Q,k))
        if qcnt:
            # phase variation across block roughly A/(l Q)
            mass_low=mass_mid=mass_high=0.0; total_abs=0.0
            examples=[]
            for l,cl in c.items():
                phase=A/(l*Q)
                total_abs += abs(cl)
                if phase<1: mass_low += abs(cl)
                elif phase<10: mass_mid += abs(cl)
                else: mass_high += abs(cl)
            blocks.append({'Q':Q,'hi':min(2*Q,k),'q_count':qcnt,'abs_c':total_abs,'phase_lt1_share':mass_low/total_abs if total_abs else 0,'phase_1_10_share':mass_mid/total_abs if total_abs else 0,'phase_gt10_share':mass_high/total_abs if total_abs else 0})
        Q*=2
    return {'P':P,'row':k,'rho':rho,'D':D,'blocks':blocks}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:486,2003:782,5003:2500,10007:4700,99991:40000'); ap.add_argument('--rho',type=float,default=0.57)
    args=ap.parse_args(); res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.rho))
    audit={'certificate_type':'beta_multisample_phase_regime','status':'phase_variation_by_Q_l','results':res}
    (DOCS/'beta-multisample-phase-regime.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Beta-multisample 相位区制扫描','','**状态：** `phase_variation_by_Q_l`','','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']}")
        for b in r['blocks']:
            lines.append(f"  - Q=({b['Q']},{b['hi']}], q={b['q_count']}, phase<1 mass={b['phase_lt1_share']:.2f}, 1-10={b['phase_1_10_share']:.2f}, >10={b['phase_gt10_share']:.2f}")
    (DOCS/'beta-multisample-phase-regime.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'beta-multisample-phase-regime.md')
if __name__=='__main__': main()
