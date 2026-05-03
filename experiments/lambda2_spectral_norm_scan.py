#!/usr/bin/env python3
"""Λ² 谱范数扫描：统计 c_l 的 L2/L1/加权范数随 P,rho 的变化。"""
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
    D=math.isqrt(P); R=max(2,int(P**rho)); small=primes_upto(D)
    V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    c={}
    ds=list(lamb)
    for d in ds:
        for e in ds:
            l=d//gcd(d,e)*e
            c[l]=c.get(l,0.0)+lamb[d]*lamb[e]
    vals=list(c.items())
    l2=sum(v*v for _,v in vals)
    l1=sum(abs(v) for _,v in vals)
    wl2=sum(v*v*l for l,v in vals)
    inv_l2=sum(v*v/max(l,1) for l,v in vals)
    return {'P':P,'D':D,'R':R,'rho':rho,'V':V,'lambda_count':len(ds),'coeff_count':len(vals),'l1':l1,'l2':l2,'l2_sqrt':math.sqrt(l2),'wl2':wl2,'inv_l2':inv_l2,'l2_over_V2':l2/(V*V),'sqrt_l2_over_V':math.sqrt(l2)/V,'top':sorted(([l,v] for l,v in vals), key=lambda x:-abs(x[1]))[:15]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='997,10007,99991,999983'); ap.add_argument('--rhos',default='0.55,0.57,0.6')
    args=ap.parse_args(); ps=[int(x) for x in args.ps.split(',')]; rhos=[float(x) for x in args.rhos.split(',')]
    res=[coeffs(P,rho) for P in ps for rho in rhos]
    audit={'certificate_type':'lambda2_spectral_norm_scan','status':'coefficient_l2_profile','results':res}
    (DOCS/'lambda2-spectral-norm-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Λ² 谱范数扫描','','**状态：** `coefficient_l2_profile`','','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} rho={r['rho']:.2f} R={r['R']} coeffs={r['coeff_count']} L1={r['l1']:.1f} sqrtL2={r['l2_sqrt']:.2f} sqrtL2/V={r['sqrt_l2_over_V']:.2f} invL2={r['inv_l2']:.3f} top={r['top'][:5]}")
    (DOCS/'lambda2-spectral-norm-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'lambda2-spectral-norm-scan.md')
if __name__=='__main__': main()
