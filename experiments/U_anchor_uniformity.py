#!/usr/bin/env python3
"""单命中 U 的 dyadic 锚点均匀性：u>L 锚点落入J、A、primeV。"""
import argparse, math
from collections import defaultdict
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); step=max(1,L//4); flags=sieve(P*P+P); small=primes(sieve(B),B); uplist=[q for q in primes(sieve(P),P) if q>L]
    buckets=defaultdict(lambda: [0,0,0,0]) # windows,totalAnchors,inA,primeV
    for row in range(1,P+1):
        N0=(row-1)*P
        for start in range(1,P-L+2,step):
            end=start+L-1
            # 按窗口统计各层；为了简单逐 u，P<=2003 可接受
            seen_window_layers=set()
            for u in uplist:
                # 只考虑较小因子 u，因此 u<=sqrt(N0+end) 可更精确；先不加，作为上界/锚模型
                r=(-N0)%u; c=start+((r-start)%u)
                if c<=end:
                    ratio=u/L; k=0
                    while ratio>2: ratio/=2; k+=1
                    key=k; buckets[key][1]+=1; seen_window_layers.add(key)
                    n=N0+c
                    if all(n%q for q in small):
                        buckets[key][2]+=1
                        v=n//u
                        if v>=u and flags[v]: buckets[key][3]+=1
            for key in seen_window_layers: buckets[key][0]+=1
    pB=1.0
    for q in small: pB*=1-1/q
    print(f'P={P} C={args.C} L={L} pB={pB:.5f}')
    print('layer totalAnch inA primeV inA/total primeV/inA expectedInA')
    for k,(wins,total,inA,pv) in sorted(buckets.items()):
        print(f'({2**k}L,{2**(k+1)}L] {total} {inA} {pv} {inA/total if total else 0:.4f} {pv/inA if inA else 0:.4f} {total*pB:.1f}')

if __name__=='__main__': main()
