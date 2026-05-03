#!/usr/bin/env python3
"""DSIU 全尺度密度扫描：单点层乘子集合总长度与 D-粗密度。"""
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

def rough(n:int,small:list[int]): return all(n%p for p in small)

def merge(intervals):
    if not intervals: return []
    intervals=sorted(intervals); out=[list(intervals[0])]
    for a,b in intervals[1:]:
        if a<=out[-1][1]+1: out[-1][1]=max(out[-1][1],b)
        else: out.append([a,b])
    return [(a,b) for a,b in out]

def analyze(P,k):
    D=math.isqrt(P); small=primes_upto(D); primes=primes_upto(k)
    intervals=[]; sum_len=0; qcnt=0
    hsum=0.0
    for q in primes:
        if D<q<=k:
            a=k*P//q+1; b=(k*P+P)//q
            if a<=b:
                intervals.append((a,b)); sum_len+=b-a+1; qcnt+=1; hsum+=1/q
    merged=merge(intervals)
    union_len=sum(b-a+1 for a,b in merged)
    rough_weighted=0
    # 加权计数：按每个区间分别计；并集计数：合并后计。
    for a,b in intervals:
        rough_weighted += sum(1 for m in range(a,b+1) if rough(m,small))
    rough_union=sum(1 for a,b in merged for m in range(a,b+1) if rough(m,small))
    V=1.0
    for p in small: V*=1-1/p
    return {'P':P,'row':k,'D':D,'qcnt':qcnt,'hsum':hsum,'sum_len':sum_len,'union_len':union_len,'components':len(merged),'overlap':sum_len/union_len if union_len else 0,'V':V,'rough_weighted':rough_weighted,'rough_union':rough_union,'weighted_ratio':rough_weighted/(V*sum_len) if sum_len else 0,'union_ratio':rough_union/(V*union_len) if union_len else 0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:916,2003:1877,5003:4700')
    args=ap.parse_args()
    res=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':')); res.append(analyze(P,k))
    audit={'certificate_type':'dsiu_global_sieve_density_scan','status':'global_weighted_rough_density_profile','results':res}
    (DOCS/'dsiu-global-sieve-density-scan.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# DSIU 全尺度筛密度扫描','','**状态：** `global_weighted_rough_density_profile`','','## 摘要']
    for r in res:
        lines.append(f"- P={r['P']} row={r['row']} D={r['D']} q={r['qcnt']} H={r['hsum']:.3f} sumLen={r['sum_len']} unionLen={r['union_len']} comp={r['components']} overlap={r['overlap']:.2f} V={r['V']:.3f} weightedRough={r['rough_weighted']} ratio={r['weighted_ratio']:.3f} unionRough={r['rough_union']} unionRatio={r['union_ratio']:.3f}")
    (DOCS/'dsiu-global-sieve-density-scan.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'dsiu-global-sieve-density-scan.md')
if __name__=='__main__': main()
