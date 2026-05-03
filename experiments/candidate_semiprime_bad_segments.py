#!/usr/bin/env python3
"""只扫描无素数连续段/最长坏段内候选半素数比例。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def classify(P,row,start,end,flags,plist,small,B):
    cand=prime=rough=semi=multi=0
    for c in range(start,end+1):
        n=(row-1)*P+c
        if all(n%q for q in small):
            cand+=1
            if flags[n]: prime+=1
            else:
                fac=factor_distinct(n,plist)
                if all(q>B for q in fac):
                    rough+=1
                    if len(fac)==2: semi+=1
                    else: multi+=1
    return cand,prime,rough,semi,multi


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--top',type=int,default=10); args=ap.parse_args()
    print('P B row start end L ratio cand prime rough semi multi semi/cand')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        rec=[]
        for row in range(1,P+1):
            segs=find_bad_segments(P,row,flags,small)
            for L,start,end,cands in segs[:3]:
                cand,prime,rough,semi,multi=classify(P,row,start,end,flags,plist,small,B)
                if cand: rec.append((L/math.sqrt(P),L,row,start,end,cand,prime,rough,semi,multi))
        for ratio,L,row,start,end,cand,prime,rough,semi,multi in sorted(rec, reverse=True)[:args.top]:
            print(P,B,row,start,end,L,f'{ratio:.3f}',cand,prime,rough,semi,multi,f'{semi/cand:.3f}')

if __name__=='__main__': main()
