#!/usr/bin/env python3
"""Λ² 主项常数扫描：M_R/V_D 随 P 的变化。"""
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

def main_constant(P:int,rho:float):
    D=math.isqrt(P); R=max(2,int(P**rho)); small=primes_upto(D)
    V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    ds=list(lamb); M=0.0
    for d in ds:
        for e in ds:
            M += lamb[d]*lamb[e]/(d//gcd(d,e)*e)
    return {'P':P,'D':D,'R':R,'rho':rho,'lambda_count':len(ds),'V':V,'M':M,'M_over_V':M/V}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--max-p',type=int,default=20000); ap.add_argument('--rhos',default='0.45,0.5,0.55')
    args=ap.parse_args(); rhos=[float(x) for x in args.rhos.split(',')]
    ps=[p for p in primes_upto(args.max_p) if p>=101]
    chosen=[]
    for target in [101,997,10007,99991,999983,2000003,5000011,9999991]:
        candidates=[p for p in ps if p<=target]
        if candidates: chosen.append(candidates[-1])
    chosen=sorted(set(chosen))
    res=[main_constant(P,rho) for P in chosen for rho in rhos]
    audit={'certificate_type':'lambda2_main_constant_scan','status':'main_constant_profile','results':res}
    (DOCS/'lambda2-main-constant-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Λ² 主项常数扫描','','**状态：** `main_constant_profile`','','## 摘要']
    for P in chosen:
        items=[r for r in res if r['P']==P]
        lines.append(f"- P={P}: "+'; '.join(f"rho={r['rho']:.2f},R={r['R']},M/V={r['M_over_V']:.4f},n={r['lambda_count']}" for r in items))
    (DOCS/'lambda2-main-constant-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'lambda2-main-constant-scan.md')
if __name__=='__main__': main()
