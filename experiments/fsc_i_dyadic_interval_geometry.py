#!/usr/bin/env python3
"""FSC-I dyadic 乘子区间几何：统计 E_Q 并长度、重叠和粗数密度。"""
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
    intervals=sorted(intervals)
    out=[list(intervals[0])]
    for a,b in intervals[1:]:
        if a<=out[-1][1]+1:
            out[-1][1]=max(out[-1][1],b)
        else: out.append([a,b])
    return [(a,b) for a,b in out]

def analyze_row(P:int,k:int):
    D=math.isqrt(P); small=primes_upto(D); primes=primes_upto(k)
    qs=[q for q in primes if D<q<=k]
    # dyadic by powers of 2 starting above D
    blocks=[]; Q=1
    while Q<=k:
        lo=Q; hi=min(2*Q,k)
        bqs=[q for q in qs if lo<q<=hi]
        if bqs:
            intervals=[]; sum_len=0
            for q in bqs:
                a=k*P//q + 1
                b=(k*P+P)//q
                if a<=b:
                    intervals.append((a,b)); sum_len+=b-a+1
            merged=merge(intervals)
            union_len=sum(b-a+1 for a,b in merged)
            rough_count=sum(1 for a,b in merged for m in range(a,b+1) if rough(m,small))
            blocks.append({'Q':Q,'lo':lo,'hi':hi,'q_count':len(bqs),'intervals':len(intervals),'components':len(merged),'sum_len':sum_len,'union_len':union_len,'overlap_ratio':sum_len/union_len if union_len else 0,'rough_count':rough_count,'rough_density':rough_count/union_len if union_len else 0})
        Q*=2
    return blocks

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pairs',default='997:916,2003:1877')
    args=ap.parse_args()
    results=[]
    for pair in args.pairs.split(','):
        P,k=map(int,pair.split(':'))
        results.append({'P':P,'row':k,'D':math.isqrt(P),'blocks':analyze_row(P,k)})
    audit={'certificate_type':'fsc_i_dyadic_interval_geometry','status':'dyadic_interval_union_geometry','results':results}
    (DOCS/'fsc-i-dyadic-interval-geometry.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    lines=['# FSC-I dyadic 乘子区间几何','','**状态：** `dyadic_interval_union_geometry`','','## 摘要']
    for it in results:
        lines.append(f"- P={it['P']} row={it['row']} D={it['D']}")
        for b in it['blocks']:
            if b['hi']<it['D']: continue
            lines.append(f"  - Q=({b['lo']},{b['hi']}]: q={b['q_count']} comp={b['components']} sumLen={b['sum_len']} unionLen={b['union_len']} overlap={b['overlap_ratio']:.2f} roughDens={b['rough_density']:.3f}")
    (DOCS/'fsc-i-dyadic-interval-geometry.md').write_text('\n'.join(lines)+'\n')
    print(DOCS/'fsc-i-dyadic-interval-geometry.md')
if __name__=='__main__': main()
