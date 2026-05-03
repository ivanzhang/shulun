#!/usr/bin/env python3
"""高阈值 y=cP 下的小筛洞尾部结构。

当 y>P/2 时，每个 n<P^2 最多含一个 q in (y,P) 的 proper factor。
若小筛洞全合，则每个洞都必须有这样的大因子；实验检验实际覆盖比例。

用法：
  python3 experiments/high_threshold_semiprime_tail.py --Ps 251,503,1009,2003 --ratios 0.3,0.5,0.7,0.9
"""
import argparse, math
from collections import Counter
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for, factor_by_primes


def analyze(P, ratio):
    y=int(P*ratio)
    flags=sieve(P*P); root=primes_from_flags(flags,P)
    rows=[]; cov_ratios=[]; max_big_per_n=0; bad_multi=0
    for a in range(1,P):
        rec=record_for(P,a,y,flags,root)
        covered=0; big_counts=Counter(); q_bucket=Counter(); cofactor_bucket=Counter()
        for r in rec['holes_list']:
            n=a+r*P
            big=[q for q in root if y<q<P and n!=q and n%q==0]
            if big: covered+=1
            max_big_per_n=max(max_big_per_n,len(big))
            if len(big)>1: bad_multi+=1
            big_counts[len(big)]+=1
            for q in big:
                q_bucket[int(10*q/P)/10]+=1
                m=n//q
                if m<P: cofactor_bucket['m<P']+=1
                elif m<2*P: cofactor_bucket['P..2P']+=1
                elif m<4*P: cofactor_bucket['2P..4P']+=1
                else: cofactor_bucket['>=4P']+=1
        cov=covered/rec['holes'] if rec['holes'] else 0
        cov_ratios.append(cov)
        rows.append((cov, rec['prime_holes']/rec['holes'] if rec['holes'] else 0, rec['holes'], rec['prime_holes'], rec['composite_holes'], a, big_counts, q_bucket, cofactor_bucket))
    rows.sort()
    cov_ratios.sort()
    lo=rows[0]; hi=rows[-1]
    med=cov_ratios[len(cov_ratios)//2]
    print(f"P={P} y={y} ratio={ratio:.2f} cov_min={lo[0]:.3f} cov_med={med:.3f} cov_max={hi[0]:.3f} maxBigPerN={max_big_per_n} multiEvents={bad_multi}")
    print(f"  mincov a={lo[5]} H={lo[2]} prime={lo[3]} comp={lo[4]} cov={lo[0]:.3f} primeFrac={lo[1]:.3f} bigCounts={dict(lo[6])}")
    print(f"  maxcov a={hi[5]} H={hi[2]} prime={hi[3]} comp={hi[4]} cov={hi[0]:.3f} primeFrac={hi[1]:.3f} bigCounts={dict(hi[6])}")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--ratios',default='0.3,0.5,0.7,0.9'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for ratio in [float(x) for x in args.ratios.split(',') if x.strip()]: analyze(P,ratio)
if __name__=='__main__': main()
