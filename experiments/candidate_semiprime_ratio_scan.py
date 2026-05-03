#!/usr/bin/env python3
"""扫描长度 C sqrt(P) 段内，小筛候选洞中粗半素数/粗合数比例。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def classify_segment(P,row,start,L,flags,plist,small,B):
    cand=prime=rough_comp=rough_semi=rough_multi=0
    for c in range(start,min(P,start+L-1)+1):
        n=(row-1)*P+c
        if all(n%q for q in small):
            cand+=1
            if flags[n]: prime+=1
            else:
                fac=factor_distinct(n,plist)
                if all(q>B for q in fac):
                    rough_comp+=1
                    if len(fac)==2: rough_semi+=1
                    else: rough_multi+=1
    return cand,prime,rough_comp,rough_semi,rough_multi


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--top',type=int,default=10); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
    rec=[]
    for row in range(1,P+1):
        for start in range(1,P-L+2):
            cand,prime,rough,semi,multi=classify_segment(P,row,start,L,flags,plist,small,B)
            if cand:
                rec.append((prime/cand, prime, cand, rough, semi, multi, row, start))
    rec.sort()
    print(f'P={P} B={B} L={L} segments={len(rec)}')
    print('worst primeRatio prime cand rough semi multi row start semi/cand rough/cand')
    for pr,prime,cand,rough,semi,multi,row,start in rec[:args.top]:
        print(f'{pr:.3f} {prime} {cand} {rough} {semi} {multi} {row} {start} {semi/cand:.3f} {rough/cand:.3f}')

if __name__=='__main__': main()
