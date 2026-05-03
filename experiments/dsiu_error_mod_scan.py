#!/usr/bin/env python3
"""DSIU Err_d 扫描：统计 A_d-W/d 的真实规模与端点复杂度。"""
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
        new=[]
        for x in out:
            y=x*p
            if y<=limit: new.append(y)
        out += new
    return sorted(set(out))

def intervals_for(P,k):
    D=math.isqrt(P); qs=[q for q in primes_upto(k) if D<q<=k]
    intervals=[]
    for q in qs:
        a=k*P//q+1; b=(k*P+P)//q
        if a<=b: intervals.append((a,b))
    return intervals

def count_divisible(intervals,d):
    total=0
    for a,b in intervals:
        total += b//d - (a-1)//d
    return total

def analyze(P,k,R_exp):
    D=math.isqrt(P); small=primes_upto(D); R=int(P**R_exp)
    intervals=intervals_for(P,k); W=sum(b-a+1 for a,b in intervals)
    ds=[d for d in squarefree_products(small,R) if d>1]
    recs=[]
    for d in ds:
        A=count_divisible(intervals,d); exp=W/d; err=A-exp
        recs.append({'d':d,'A':A,'exp':exp,'err':err,'abs_err':abs(err),'rel_to_exp':abs(err)/exp if exp else 0})
    top=sorted(recs,key=lambda r:-r['abs_err'])[:15]
    top_rel=sorted(recs,key=lambda r:-r['rel_to_exp'])[:15]
    l1=sum(r['abs_err'] for r in recs); l2=sum(r['err']*r['err'] for r in recs)**0.5
    return {'P':P,'row':k,'D':D,'R':R,'intervals':len(intervals),'W':W,'d_count':len(ds),'l1_abs_err':l1,'l2_err':l2,'top_abs':top,'top_rel':top_rel}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:916,2003:1877,5003:4700'); ap.add_argument('--R-exp',type=float,default=0.25)
    args=ap.parse_args()
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.R_exp))
    audit={'certificate_type':'dsiu_error_mod_scan','status':'mod_error_size_profile','R_exp':args.R_exp,'results':res}
    (DOCS/'dsiu-error-mod-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU Err_d 模误差扫描','',f"**状态：** `{audit['status']}`",f"筛层级 `R=P^{args.R_exp}`。",'','## 摘要']
    for r in res:
        ta=r['top_abs'][0] if r['top_abs'] else {'d':None,'abs_err':0,'rel_to_exp':0}
        tr=r['top_rel'][0] if r['top_rel'] else {'d':None,'abs_err':0,'rel_to_exp':0}
        lines.append(f"- P={r['P']} row={r['row']} W={r['W']} intervals={r['intervals']} dCount={r['d_count']} L1={r['l1_abs_err']:.1f} L2={r['l2_err']:.1f} topAbs d={ta['d']} err={ta['abs_err']:.2f} rel={ta['rel_to_exp']:.2f}; topRel d={tr['d']} err={tr['abs_err']:.2f} rel={tr['rel_to_exp']:.2f}")
    lines+=['','## 最大绝对误差 d']
    for r in res:
        lines.append(f"- P={r['P']}: "+'; '.join(f"d={x['d']},err={x['err']:.2f},rel={x['rel_to_exp']:.2f}" for x in r['top_abs'][:8]))
    (DOCS/'dsiu-error-mod-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-error-mod-scan.md')
if __name__=='__main__': main()
