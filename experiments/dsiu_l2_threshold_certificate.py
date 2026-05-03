#!/usr/bin/env python3
"""DSIU L2 阈值证书：比较模误差 L2 与闭合容量区所需偏差。"""
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

def squarefree_products(primes,limit):
    out=[1]
    for p in primes:
        base=list(out)
        for x in base:
            y=x*p
            if y<=limit: out.append(y)
    return sorted(set(out))

def intervals(P,k):
    D=math.isqrt(P); qs=[q for q in primes_upto(k) if D<q<=k]
    out=[]
    for q in qs:
        a=k*P//q+1; b=(k*P+P)//q
        if a<=b: out.append((a,b))
    return out

def count_div(intervals,d):
    return sum(b//d-(a-1)//d for a,b in intervals)

def rough(n,small): return all(n%p for p in small)

def analyze(P,k,R_exp):
    D=math.isqrt(P); small=primes_upto(D); R=int(P**R_exp)
    ints=intervals(P,k); W=sum(b-a+1 for a,b in ints)
    V=1.0
    for p in small: V*=1-1/p
    B=sum(1 for a,b in ints for m in range(a,b+1) if rough(m,small))
    ds=[d for d in squarefree_products(small,R) if d>1]
    errs=[]
    for d in ds:
        A=count_div(ints,d); err=A-W/d; errs.append(err)
    l2=sum(e*e for e in errs)**0.5
    l1=sum(abs(e) for e in errs)
    allowed_1818=(1.818*V*W-B) # remaining before weak threshold
    allowed_16=(1.6*V*W-B)
    return {'P':P,'row':k,'D':D,'R':R,'R_exp':R_exp,'W':W,'V':V,'B':B,'theta':B/(V*W) if W else 0,'d_count':len(ds),'L2':l2,'L1':l1,'L2_over_VW':l2/(V*W) if W else 0,'L1_over_VW':l1/(V*W) if W else 0,'allowed_to_1p818':allowed_1818,'allowed_to_1p6':allowed_16,'allowed1818_over_VW':allowed_1818/(V*W) if W else 0,'allowed16_over_VW':allowed_16/(V*W) if W else 0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='251:123,503:252,997:569,2003:916,5003:2500'); ap.add_argument('--R-exp',type=float,default=0.5)
    args=ap.parse_args(); res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.R_exp))
    audit={'certificate_type':'dsiu_l2_threshold_certificate','status':'l2_error_vs_density_margin','results':res}
    (DOCS/'dsiu-l2-threshold-certificate.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU L2 阈值证书','',f"**状态：** `{audit['status']}`",f"R=P^{args.R_exp}。",'','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} theta={r['theta']:.3f} W={r['W']} d={r['d_count']} L2/(VW)={r['L2_over_VW']:.3f} L1/(VW)={r['L1_over_VW']:.3f} margin1.818={r['allowed1818_over_VW']:.3f} margin1.6={r['allowed16_over_VW']:.3f}")
    (DOCS/'dsiu-l2-threshold-certificate.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-l2-threshold-certificate.md')
if __name__=='__main__': main()
