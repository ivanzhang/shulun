#!/usr/bin/env python3
"""Beta-short-mean 块长度区制扫描：W_Q 与 R、R^2、sqrt区间关系。"""
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

def analyze(P,k,rho):
    D=math.isqrt(P); R=P**rho; primes=primes_upto(k)
    blocks=[]; Q=1; total=0; short_total=0
    while Q<=k:
        bqs=[q for q in primes if max(D,Q)<q<=min(2*Q,k)]
        if bqs:
            W=0; comp=0
            for q in bqs:
                a=k*P//q+1; b=(k*P+P)//q
                if a<=b:
                    W+=b-a+1; comp+=1
            if W:
                total+=W
                # 短块：总长度小于 R；中块：R到R^2；长块：大于R^2
                regime='long' if W>=R*R else ('medium' if W>=R else 'short')
                if regime=='short': short_total+=W
                blocks.append({'Q':Q,'hi':min(2*Q,k),'q_count':len(bqs),'W':W,'W_over_R':W/R,'W_over_R2':W/(R*R),'regime':regime})
        Q*=2
    return {'P':P,'row':k,'rho':rho,'R':R,'total_W':total,'short_total':short_total,'short_share':short_total/total if total else 0,'blocks':blocks}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:486,2003:782,5003:2500,10007:4700,99991:40000'); ap.add_argument('--rho',type=float,default=0.57)
    args=ap.parse_args(); res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.rho))
    audit={'certificate_type':'beta_block_length_regime_scan','status':'block_length_vs_R_profile','results':res}
    (DOCS/'beta-block-length-regime-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# Beta 块长度区制扫描','','**状态：** `block_length_vs_R_profile`',f"rho={args.rho}",'','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} R={r['R']:.1f} totalW={r['total_W']} shortShare={r['short_share']:.3f}")
        lines.append('  - '+ '; '.join(f"Q=({b['Q']},{b['hi']}],W={b['W']},W/R={b['W_over_R']:.2f},{b['regime']}" for b in r['blocks']))
    (DOCS/'beta-block-length-regime-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'beta-block-length-regime-scan.md')
if __name__=='__main__': main()
