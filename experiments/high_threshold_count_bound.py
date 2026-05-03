#!/usr/bin/env python3
"""高阈值半素数计数上界探索。

对 y=cP，比较：
- H_y(a) 实际小筛洞数；
- C_y(a) 实际被 q in (y,P) proper multiple 覆盖的洞数；
- naive upper = sum_{y<q<P} ceil(P/q)，太弱；
- one-per-q upper = #q in (y,P)，当 q>P/2 以外不总成立但给尺度参考；
- pair window heuristic: composites q*m with q,m>y imply n in column and m<P^2/q。
"""
import argparse, math
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003'); ap.add_argument('--ratios',default='0.3,0.5,0.7,0.9'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P*P); root=primes_from_flags(flags,P)
        for c in [float(x) for x in args.ratios.split(',') if x.strip()]:
            y=int(c*P); big=[q for q in root if y<q<P]
            naive=sum(math.ceil(P/q) for q in big); one=len(big)
            # 实际最坏覆盖比例列
            best=None
            for a in range(1,P):
                rec=record_for(P,a,y,flags,root)
                covered=rec['holes']-rec['prime_holes'] # for y high enough, should be composites rough; actual comp
                cov_ratio=covered/rec['holes'] if rec['holes'] else 0
                key=(cov_ratio, covered, -rec['holes'])
                if best is None or key>best[0]: best=(key,a,rec)
            _,a,rec=best
            print(f"P={P} c={c:.2f} y={y} bigQ={len(big)} naiveHits={naive} oneQ={one} worst a={a} H={rec['holes']} comp={rec['composite_holes']} prime={rec['prime_holes']} comp/H={rec['composite_holes']/rec['holes'] if rec['holes'] else 0:.3f} naive/H={naive/rec['holes']:.2f} one/H={one/rec['holes']:.2f}")
if __name__=='__main__': main()
