#!/usr/bin/env python3
"""全范围 DSIU 扫描：q in (D,P) 的乘子区间粗数计数。"""
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

def spf_sieve(n:int):
    spf=list(range(n+1))
    if n>=0:spf[0]=0
    if n>=1:spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j:spf[j]=i
    return spf

def rough(n:int,small): return all(n%p for p in small)

def analyze(P:int):
    D=math.isqrt(P); small=primes_upto(D); primes=primes_upto(P-1); spf=spf_sieve(P*P+P)
    V=1.0
    for p in small: V*=1-1/p
    rows=[]
    H_total=sum(1/q for q in primes if D<q<P)
    for k in range(1,P+1):
        U=sum(1 for c in range(1,P+1) if rough(k*P+c,small))
        B=0; W=0; B_left=B_right=0; W_left=W_right=0
        for q in primes:
            if not (D<q<P): continue
            a=k*P//q+1; b=(k*P+P)//q
            if a>b: continue
            length=b-a+1; W+=length
            cnt=sum(1 for m in range(a,b+1) if rough(m,small))
            B+=cnt
            if q<=k:
                W_left+=length; B_left+=cnt
            else:
                W_right+=length; B_right+=cnt
        rows.append({'row':k,'U':U,'B':B,'W':W,'B_over_U':B/U if U else 0,'theta':B/(V*W) if W else 0,'left_share':B_left/U if U else 0,'right_share':B_right/U if U else 0,'H_total':H_total,'VW_over_U':V*W/U if U else 0})
    top=sorted(rows,key=lambda r:-r['B_over_U'])[:10]
    return {'P':P,'D':D,'V':V,'H_total':H_total,'top':top}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ps',default='251,503,997')
    args=ap.parse_args(); res=[analyze(int(x)) for x in args.ps.split(',')]
    audit={'certificate_type':'full_range_dsiu_scan','status':'full_q_range_multiplier_sieve_profile','results':res}
    (DOCS/'full-range-dsiu-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# 全范围 DSIU 扫描','','**状态：** `full_q_range_multiplier_sieve_profile`','','## 摘要']
    for it in res:
        t=it['top'][0]
        lines.append(f"- P={it['P']} Htotal={it['H_total']:.3f} top row={t['row']} B/U={t['B_over_U']:.3f} theta={t['theta']:.3f} VW/U={t['VW_over_U']:.3f} left={t['left_share']:.3f} right={t['right_share']:.3f}")
    lines+=['','## top rows']
    for it in res:
        lines.append(f"- P={it['P']}")
        for r in it['top'][:5]:
            lines.append(f"  - row={r['row']} B/U={r['B_over_U']:.3f} theta={r['theta']:.3f} VW/U={r['VW_over_U']:.3f} left={r['left_share']:.3f} right={r['right_share']:.3f}")
    (DOCS/'full-range-dsiu-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'full-range-dsiu-scan.md')
if __name__=='__main__': main()
