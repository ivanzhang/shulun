#!/usr/bin/env python3
"""DSIU Λ² 权主项/误差分离扫描。"""
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
    out=[]
    for q in qs:
        a=k*P//q+1; b=(k*P+P)//q
        if a<=b: out.append((a,b))
    return out

def count_div(ints,l):
    return sum(b//l-(a-1)//l for a,b in ints)

def rough(n,small): return all(n%p for p in small)

def analyze(P,k,rho):
    D=math.isqrt(P); small=primes_upto(D); R=max(2,int(P**rho)); ints=intervals(P,k)
    W=sum(b-a+1 for a,b in ints)
    V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    ds=list(lamb)
    M=0.0; E=0.0
    cache={}
    for d in ds:
        ld=lamb[d]
        for e in ds:
            le=lamb[e]
            l=d//gcd(d,e)*e
            coeff=ld*le
            M += coeff/l
            if l not in cache:
                A=count_div(ints,l); cache[l]=A-W/l
            E += coeff*cache[l]
    # direct beta for sanity
    weights={}
    for a,b in ints:
        for m in range(a,b+1): weights[m]=weights.get(m,0)+1
    beta_sum=0.0; B=0
    for m,w in weights.items():
        s=0.0
        for d,ld in lamb.items():
            if m%d==0: s+=ld
        beta_sum += w*s*s
        if rough(m,small): B+=w
    return {'P':P,'row':k,'D':D,'rho':rho,'R':R,'W':W,'V':V,'lambda_count':len(ds),'lcm_count':len(cache),'M':M,'M_over_V':M/V if V else 0,'E':E,'E_over_VW':E/(V*W) if W else 0,'total_over_VW':(W*M+E)/(V*W) if W else 0,'direct_over_VW':beta_sum/(V*W) if W else 0,'B_over_VW':B/(V*W) if W else 0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='503:252,997:569,2003:916,5003:2500'); ap.add_argument('--rhos',default='0.45,0.5,0.55')
    args=ap.parse_args(); rhos=[float(x) for x in args.rhos.split(',')]
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':'))
        for rho in rhos: res.append(analyze(P,k,rho))
    audit={'certificate_type':'dsiu_lambda2_main_error_scan','status':'lambda2_main_error_decomposition','results':res}
    (DOCS/'dsiu-lambda2-main-error-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU Λ² 主项/误差分离扫描','','**状态：** `lambda2_main_error_decomposition`','','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} rho={r['rho']:.2f} R={r['R']} M/V={r['M_over_V']:.3f} E/(VW)={r['E_over_VW']:.3f} total={r['total_over_VW']:.3f} direct={r['direct_over_VW']:.3f} B/(VW)={r['B_over_VW']:.3f} lcms={r['lcm_count']}")
    (DOCS/'dsiu-lambda2-main-error-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-lambda2-main-error-scan.md')
if __name__=='__main__': main()
