#!/usr/bin/env python3
"""Λ² β 权在 dyadic q 块上的偏差扫描。"""
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

def build_lambda(P,rho):
    D=math.isqrt(P); R=int(P**rho); small=primes_upto(D)
    mu=mu_squarefree_products(small,R)
    lamb={d:mud*math.log(R/d)/math.log(R) for d,mud in mu.items()}
    V=1.0
    for p in small: V*=1-1/p
    # 主项直接按支撑均值公式近似 M=sum lambda lambda/lcm
    from math import gcd
    ds=list(lamb); M=0.0
    for d in ds:
        for e in ds: M += lamb[d]*lamb[e]/(d//gcd(d,e)*e)
    return D,R,lamb,V,M

def beta(m,lamb):
    s=0.0
    for d,ld in lamb.items():
        if m%d==0: s+=ld
    return s*s

def analyze(P,k,rho):
    D,R,lamb,V,M=build_lambda(P,rho); primes=primes_upto(k)
    blocks=[]; Q=1; total_bias=0; total_len=0; total_abs=0
    while Q<=k:
        bqs=[q for q in primes if max(D,Q)<q<=min(2*Q,k)]
        if bqs:
            length=0; bsum=0.0; intervals=0
            for q in bqs:
                a=k*P//q+1; b=(k*P+P)//q
                if a<=b:
                    intervals+=1
                    for m in range(a,b+1):
                        length+=1; bsum += beta(m,lamb)-M
            if length:
                bias=bsum; total_bias+=bias; total_len+=length; total_abs+=abs(bias)
                blocks.append({'Q':Q,'hi':min(2*Q,k),'q_count':len(bqs),'intervals':intervals,'length':length,'bias':bias,'bias_over_VMlen':bias/(V*length) if length else 0,'abs_bias_over_VMlen':abs(bias)/(V*length) if length else 0})
        Q*=2
    return {'P':P,'row':k,'rho':rho,'D':D,'R':R,'V':V,'M':M,'M_over_V':M/V,'total_len':total_len,'total_bias':total_bias,'total_bias_over_VW':total_bias/(V*total_len) if total_len else 0,'sum_abs_block_bias_over_VW':total_abs/(V*total_len) if total_len else 0,'blocks':blocks}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:486,2003:782,5003:2500,10007:4700'); ap.add_argument('--rho',type=float,default=0.57)
    args=ap.parse_args(); res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.rho))
    audit={'certificate_type':'lambda2_beta_block_bias_scan','status':'beta_block_bias_profile','results':res}
    (DOCS/'lambda2-beta-block-bias-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Λ² β 权 dyadic 块偏差扫描','','**状态：** `beta_block_bias_profile`',f"rho={args.rho}",'','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} M/V={r['M_over_V']:.3f} totalBias/(VW)={r['total_bias_over_VW']:.3f} sumAbsBlock/(VW)={r['sum_abs_block_bias_over_VW']:.3f}")
        lines.append('  - blocks: '+ '; '.join(f"Q=({b['Q']},{b['hi']}],len={b['length']},bias/Vlen={b['bias_over_VMlen']:.2f}" for b in r['blocks']))
    (DOCS/'lambda2-beta-block-bias-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'lambda2-beta-block-bias-scan.md')
if __name__=='__main__': main()
