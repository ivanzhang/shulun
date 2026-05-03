#!/usr/bin/env python3
"""DSIU 倒数指数和扫描：Erdos-Turan 截断后 e(hA/(qd)) 的平均规模。"""
from __future__ import annotations
import argparse, json, math, cmath
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
TAU=2*math.pi

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
        out += [x*p for x in list(out) if x*p<=limit]
    return sorted(set(out))

def expi(x): return complex(math.cos(TAU*x), math.sin(TAU*x))

def analyze(P,k,H,R_exp):
    D=math.isqrt(P); small=primes_upto(D); R=int(P**R_exp)
    ds=[d for d in squarefree_products(small,R) if d>1]
    qs=[q for q in primes_upto(k) if D<q<=k]
    A=k*P; B=(k+1)*P
    recs=[]; total_weighted=0.0
    for d in ds:
        max_norm=0.0; sum_norm=0.0; max_h=0
        for h in range(1,H+1):
            S=0j
            for q in qs:
                S += expi(h*A/(q*d)) - expi(h*B/(q*d))
            norm=abs(S)/len(qs) if qs else 0
            sum_norm += norm/h
            if norm>max_norm: max_norm=norm; max_h=h
        recs.append({'d':d,'max_norm':max_norm,'max_h':max_h,'weighted_norm':sum_norm})
        total_weighted += sum_norm
    top=sorted(recs,key=lambda r:-r['max_norm'])[:12]
    topw=sorted(recs,key=lambda r:-r['weighted_norm'])[:12]
    return {'P':P,'row':k,'D':D,'R':R,'H':H,'q_count':len(qs),'d_count':len(ds),'avg_weighted_norm':total_weighted/len(ds) if ds else 0,'top_max':top,'top_weighted':topw}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:916,5003:4700'); ap.add_argument('--H',type=int,default=16); ap.add_argument('--R-exp',type=float,default=0.5)
    args=ap.parse_args()
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k,args.H,args.R_exp))
    audit={'certificate_type':'dsiu_reciprocal_exp_sum_scan','status':'reciprocal_exponential_sum_norm_profile','results':res}
    (DOCS/'dsiu-reciprocal-exp-sum-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU 倒数指数和扫描','',f"**状态：** `{audit['status']}`",f"Fourier H={args.H}, R=P^{args.R_exp}。",'','## 摘要']
    for r in res:
        tm=r['top_max'][0] if r['top_max'] else {'d':None,'max_norm':0,'max_h':0}
        tw=r['top_weighted'][0] if r['top_weighted'] else {'d':None,'weighted_norm':0}
        lines.append(f"- P={r['P']} row={r['row']} q={r['q_count']} d={r['d_count']} avgWeightedNorm={r['avg_weighted_norm']:.3f} topMax d={tm['d']} norm={tm['max_norm']:.3f} h={tm['max_h']}; topWeighted d={tw['d']} val={tw['weighted_norm']:.3f}")
    lines += ['','## top max']
    for r in res:
        lines.append(f"- P={r['P']}: "+'; '.join(f"d={x['d']},norm={x['max_norm']:.3f},h={x['max_h']}" for x in r['top_max'][:8]))
    (DOCS/'dsiu-reciprocal-exp-sum-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-reciprocal-exp-sum-scan.md')
if __name__=='__main__': main()
