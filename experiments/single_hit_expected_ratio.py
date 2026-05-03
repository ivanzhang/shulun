#!/usr/bin/env python3
"""比较坏段单命中证书 dyadic 层真实 R_U 与期望模型 E_U。"""
import argparse, math
from collections import Counter
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def layer_key(u,L):
    k=0; bound=L
    while u>2*bound:
        bound*=2; k+=1
    return k, bound, 2*bound


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cmin',type=float,default=2.5); ap.add_argument('--top',type=int,default=5); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        segments=[]
        for row in range(1,P+1):
            for L,start,end,cands in find_bad_segments(P,row,flags,small):
                if L/math.sqrt(P)<args.Cmin: continue
                layers=Counter(); A=len(cands); semi=0
                for c in cands:
                    n=(row-1)*P+c
                    if flags[n]: continue
                    fac=factor_distinct(n,plist)
                    if all(q>B for q in fac) and len(fac)==2:
                        semi+=1; u=min(fac)
                        if u>L:
                            k,lo,hi=layer_key(u,L); layers[(k,lo,hi)] += 1
                if layers:
                    segments.append((L/math.sqrt(P),row,start,end,L,A,semi,layers))
        print(f'P={P} B={B}')
        for ratio,row,start,end,L,A,semi,layers in sorted(segments, reverse=True)[:args.top]:
            print(f' seg row={row} {start}-{end} L={L} ratio={ratio:.3f} A={A} semi={semi}')
            totalR=0; totalE=0.0
            for (k,lo,hi),R in sorted(layers.items()):
                U=lo
                logU=max(1.0,math.log(U)); logP=math.log(P); logV=max(1.0, math.log((P*P)/max(U,1)))
                E=L/(logU*logP*logV)
                totalR+=R; totalE+=E
                print(f'  layer ({lo},{hi}] R={R} E={E:.3f} R/E={R/E if E else 0:.1f}')
            print(f'  total single R={totalR} E={totalE:.3f} R/E={totalR/totalE if totalE else 0:.1f} R/A={totalR/A:.3f}')

if __name__=='__main__': main()
