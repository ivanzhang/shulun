#!/usr/bin/env python3
"""DSIU Selberg 平方权扫描：用简化 Selberg 权 λ_d=μ(d)log(R/d)/log R 评估上界常数。"""
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

def mu_squarefree_products(primes,limit):
    out={1:1}
    for p in primes:
        for x,mu in list(out.items()):
            y=x*p
            if y<=limit: out[y]=-mu
    return out

def rough(n,small): return all(n%p for p in small)

def intervals(P,k):
    D=math.isqrt(P); qs=[q for q in primes_upto(k) if D<q<=k]
    out=[]
    for q in qs:
        a=k*P//q+1; b=(k*P+P)//q
        if a<=b: out.append((a,b))
    return out

def analyze(P,k,rhos):
    D=math.isqrt(P); small=primes_upto(D); ints=intervals(P,k)
    W=sum(b-a+1 for a,b in ints)
    V=1.0
    for p in small: V*=1-1/p
    # 枚举支撑上的 m 权重，容量区通常无重叠。
    weights={}
    for a,b in ints:
        for m in range(a,b+1): weights[m]=weights.get(m,0)+1
    B=sum(w for m,w in weights.items() if rough(m,small))
    recs=[]
    for rho in rhos:
        R=max(2,int(P**rho)); mu=mu_squarefree_products(small,R)
        lamb={d:(mud*math.log(R/d)/math.log(R) if d<=R else 0.0) for d,mud in mu.items()}
        beta_sum=0.0
        # 直接在支撑上算 beta；若 beta 是 majorant，则 beta_sum 是可用上界。
        min_rough_beta=10.0
        for m,w in weights.items():
            s=0.0
            for d,lam in lamb.items():
                if m%d==0: s+=lam
            beta=s*s
            beta_sum += w*beta
            if rough(m,small) and beta<min_rough_beta: min_rough_beta=beta
        recs.append({'rho':rho,'R':R,'lambda_count':len(lamb),'beta_sum':beta_sum,'beta_over_VW':beta_sum/(V*W) if W else 0,'B_over_VW':B/(V*W) if W else 0,'min_rough_beta':min_rough_beta})
    return {'P':P,'row':k,'D':D,'W':W,'V':V,'B':B,'B_over_VW':B/(V*W) if W else 0,'records':recs}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='251:123,503:252,997:569,2003:916'); ap.add_argument('--rhos',default='0.25,0.33,0.4,0.5')
    args=ap.parse_args(); rhos=[float(x) for x in args.rhos.split(',')]
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,rhos))
    audit={'certificate_type':'dsiu_selberg_weight_scan','status':'simplified_selberg_weight_profile','results':res,'warning':'λ_d=μ(d)log(R/d)/logR 是简化 Selberg/Λ^2 权；仅作数值方向，不等于最优 Selberg 权。'}
    (DOCS/'dsiu-selberg-weight-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU Selberg 平方权扫描','','**状态：** `simplified_selberg_weight_profile`','','注意：这里用简化权 `λ_d=μ(d)log(R/d)/log R`，不是最优 Selberg 权。','','## 摘要']
    for it in res:
        lines.append(f"- P={it['P']} row={it['row']} W={it['W']} B/(VW)={it['B_over_VW']:.3f}")
        for r in it['records']:
            lines.append(f"  - rho={r['rho']:.2f} R={r['R']} beta/(VW)={r['beta_over_VW']:.3f} minRoughBeta={r['min_rough_beta']:.3f} lambdas={r['lambda_count']}")
    (DOCS/'dsiu-selberg-weight-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-selberg-weight-scan.md')
if __name__=='__main__': main()
