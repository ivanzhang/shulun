#!/usr/bin/env python3
"""按相等模式分解真实 H 的四阶中心矩贡献（枚举 P 小样本）。"""
import argparse, itertools, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes, H_count
from sieve_remainder_pair_correlation import alive_matrix


def pattern_type(tup):
    counts=sorted([tup.count(x) for x in set(tup)], reverse=True)
    return tuple(counts)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=101); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); H=[sum(row) for row in A]; mu=mean(H)
    # Y values by a,r using p_r mean over a for exact centering per r
    pr=[mean(row[r] for row in A) for r in range(P)]
    contrib={}; counts={}
    for tup in itertools.product(range(P), repeat=4):
        typ=pattern_type(list(tup)); s=0.0
        for row in A:
            prod=1.0
            for r in tup: prod *= (row[r]-pr[r])
            s += prod
        val=s/(P-1)
        contrib[typ]=contrib.get(typ,0.0)+val; counts[typ]=counts.get(typ,0)+1
    total=sum(contrib.values())
    print(f'P={P} c={args.c} Hmean={mu:.3f} fourth={total:.3f}')
    for typ in sorted(contrib): print(typ,'count',counts[typ],'contrib',round(contrib[typ],3),'frac',round(contrib[typ]/total if total else 0,3))
if __name__=='__main__': main()
