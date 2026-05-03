#!/usr/bin/env python3
"""DSIU-density-cap 二阶证书扫描：统计 w 二阶矩与粗性偏差。"""
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

def rough(n,small): return all(n%p for p in small)

def analyze(P,k):
    D=math.isqrt(P); small=primes_upto(D); primes=primes_upto(k)
    V=1.0
    for p in small: V*=1-1/p
    weights={}
    H=0.0
    for q in primes:
        if D<q<=k:
            H+=1/q
            a=k*P//q+1; b=(k*P+P)//q
            for m in range(a,b+1): weights[m]=weights.get(m,0)+1
    W=sum(weights.values()); W2=sum(v*v for v in weights.values())
    B=sum(v for m,v in weights.items() if rough(m,small))
    supp=len(weights)
    bias=B-V*W
    return {'P':P,'row':k,'D':D,'H':H,'V':V,'W':W,'supp':supp,'W2':W2,'W2_over_W':W2/W if W else 0,'B':B,'theta':B/(V*W) if W else 0,'bias_over_VW':bias/(V*W) if W else 0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='251:123,503:252,997:569,2003:916,5003:2500')
    args=ap.parse_args()
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k))
    audit={'certificate_type':'dsiu_density_cauchy_scan','status':'density_bias_second_moment_profile','results':res}
    (DOCS/'dsiu-density-cauchy-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU 密度二阶证书扫描','','**状态：** `density_bias_second_moment_profile`','','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} H={r['H']:.3f} V={r['V']:.3f} W={r['W']} supp={r['supp']} W2/W={r['W2_over_W']:.3f} theta={r['theta']:.3f} bias/(VW)={r['bias_over_VW']:.3f}")
    (DOCS/'dsiu-density-cauchy-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-density-cauchy-scan.md')
if __name__=='__main__': main()
