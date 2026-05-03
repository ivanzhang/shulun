#!/usr/bin/env python3
"""Λ² 误差系数 c_l 剖面：按 l=[d,e] 合并并统计贡献。"""
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
        if a<=b: out.append((q,a,b))
    return out

def err_l(ints,l,P):
    e=0.0
    for q,a,b in ints:
        e += (b//l - (a-1)//l) - P/(q*l)
    return e

def analyze(P,k,rho):
    D=math.isqrt(P); R=max(2,int(P**rho)); small=primes_upto(D); ints=intervals(P,k)
    W=sum(b-a+1 for _,a,b in ints); V=1.0
    for p in small: V*=1-1/p
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    coeff={}
    ds=list(lamb)
    for d in ds:
        for e in ds:
            l=d//gcd(d,e)*e
            coeff[l]=coeff.get(l,0.0)+lamb[d]*lamb[e]
    recs=[]; E=0.0
    for l,c in coeff.items():
        er=err_l(ints,l,P); contrib=c*er; E+=contrib
        recs.append({'l':l,'c':c,'abs_c':abs(c),'err':er,'contrib':contrib,'abs_contrib':abs(contrib)})
    recs_abs=sorted(recs,key=lambda r:-r['abs_contrib'])[:20]
    return {'P':P,'row':k,'rho':rho,'R':R,'W':W,'V':V,'coeff_count':len(coeff),'sum_abs_c':sum(r['abs_c'] for r in recs),'l2_c':sum(r['c']*r['c'] for r in recs)**0.5,'E':E,'E_over_VW':E/(V*W) if W else 0,'sum_abs_contrib_over_VW':sum(r['abs_contrib'] for r in recs)/(V*W) if W else 0,'top_contrib':recs_abs}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:486,2003:782,5003:2500'); ap.add_argument('--rho',type=float,default=0.57)
    args=ap.parse_args(); res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.rho))
    audit={'certificate_type':'lambda2_error_coefficient_scan','status':'coefficient_contribution_profile','results':res}
    (DOCS/'lambda2-error-coefficient-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Λ² 误差系数剖面','','**状态：** `coefficient_contribution_profile`',f"rho={args.rho}",'','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} R={r['R']} coeffs={r['coeff_count']} sum|c|={r['sum_abs_c']:.2f} l2c={r['l2_c']:.2f} E/(VW)={r['E_over_VW']:.3f} sumAbsContr/(VW)={r['sum_abs_contrib_over_VW']:.3f}")
        lines.append('  - top: '+ '; '.join(f"l={x['l']},c={x['c']:.3f},err={x['err']:.2f},contr={x['contrib']:.2f}" for x in r['top_contrib'][:8]))
    (DOCS/'lambda2-error-coefficient-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'lambda2-error-coefficient-scan.md')
if __name__=='__main__': main()
