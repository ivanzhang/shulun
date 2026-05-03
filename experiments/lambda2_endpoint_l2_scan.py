#!/usr/bin/env python3
"""Λ² 端点误差加权 L2 扫描。"""
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

def intervals(P,k):
    D=math.isqrt(P); qs=[q for q in primes_upto(k) if D<q<=k]
    return [(q,k*P//q+1,(k*P+P)//q) for q in qs if k*P//q+1 <= (k*P+P)//q]

def err_l(ints,l,P):
    return sum((b//l-(a-1)//l)-P/(q*l) for q,a,b in ints)

def coeff_keys(P,rho):
    D=math.isqrt(P); R=int(P**rho); small=primes_upto(D); mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    keys=set()
    ds=list(lamb)
    for d in ds:
        for e in ds: keys.add(d//gcd(d,e)*e)
    return keys

def analyze(P,k,rho):
    D=math.isqrt(P); ints=intervals(P,k); W=sum(b-a+1 for _,a,b in ints)
    V=1.0
    for p in primes_upto(D): V*=1-1/p
    keys=coeff_keys(P,rho)
    val=sum(l*err_l(ints,l,P)**2 for l in keys)
    return {'P':P,'row':k,'rho':rho,'D':D,'W':W,'V':V,'l_count':len(keys),'weighted_l2':val,'sqrt_weighted_l2':math.sqrt(val),'sqrt_over_VW':math.sqrt(val)/(V*W) if W else 0,'scaled':val*math.log(D)/((V*W)**2) if W else 0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:486,2003:782,5003:2500,10007:4700'); ap.add_argument('--rho',type=float,default=0.57)
    args=ap.parse_args(); res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.rho))
    audit={'certificate_type':'lambda2_endpoint_l2_scan','status':'endpoint_weighted_l2_profile','results':res}
    (DOCS/'lambda2-endpoint-l2-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Λ² 端点误差加权 L2 扫描','','**状态：** `endpoint_weighted_l2_profile`','','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} l={r['l_count']} sqrtL2/(VW)={r['sqrt_over_VW']:.3f} scaled=C_e? {r['scaled']:.3f}")
    (DOCS/'lambda2-endpoint-l2-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'lambda2-endpoint-l2-scan.md')
if __name__=='__main__': main()
