#!/usr/bin/env python3
"""Full-DSIU 全范围 Λ² majorant 扫描。"""
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

def rough(n,small): return all(n%p for p in small)

def build(P,rho):
    D=math.isqrt(P); R=int(P**rho); small=primes_upto(D); V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    ds=list(lamb); M=0.0
    for d in ds:
        for e in ds: M += lamb[d]*lamb[e]/(d//gcd(d,e)*e)
    return D,R,small,V,lamb,M

def beta(m,lamb):
    s=0.0
    for d,ld in lamb.items():
        if m%d==0: s+=ld
    return s*s

def analyze(P,k,rhos):
    primes=primes_upto(P-1); out=[]
    for rho in rhos:
        D,R,small,V,lamb,M=build(P,rho)
        W=0; B=0; beta_sum=0.0
        for q in primes:
            if not (D<q<P): continue
            a=k*P//q+1; b=(k*P+P)//q
            if a>b: continue
            for m in range(a,b+1):
                W+=1
                if rough(m,small): B+=1
                beta_sum += beta(m,lamb)
        out.append({'rho':rho,'R':R,'V':V,'W':W,'B':B,'M_over_V':M/V,'B_over_VW':B/(V*W) if W else 0,'beta_over_VW':beta_sum/(V*W) if W else 0,'E_over_VW':(beta_sum-W*M)/(V*W) if W else 0})
    return {'P':P,'row':k,'records':out}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='251:160,503:37,997:35,2003:34'); ap.add_argument('--rhos',default='0.57,0.60,0.63,0.66')
    args=ap.parse_args(); rhos=[float(x) for x in args.rhos.split(',')]
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,rhos))
    audit={'certificate_type':'full_range_lambda2_scan','status':'full_range_lambda2_majorant_profile','results':res}
    (DOCS/'full-range-lambda2-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Full-DSIU 全范围 Λ² 扫描','','**状态：** `full_range_lambda2_majorant_profile`','','## 摘要']
    for it in res:
        lines.append(f"- P={it['P']} row={it['row']}")
        for r in it['records']:
            lines.append(f"  - rho={r['rho']:.2f} R={r['R']} M/V={r['M_over_V']:.3f} E/(VW)={r['E_over_VW']:.3f} beta/(VW)={r['beta_over_VW']:.3f} B/(VW)={r['B_over_VW']:.3f}")
    (DOCS/'full-range-lambda2-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'full-range-lambda2-scan.md')
if __name__=='__main__': main()
