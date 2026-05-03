#!/usr/bin/env python3
"""单点补丁全列聚合摘要。"""
import argparse
import math
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def summarize(P, y):
    flags=sieve(P*P); root=primes_from_flags(flags,P)
    best=None; total_single=total_reuse=total_comp=total_prime=0; max_reuse=0; worst_ratio=0
    for a in range(1,P):
        rec=record_for(P,a,y,flags,root)
        qs=[]
        for r, facs in rec['patch_factors_by_r'].items():
            if len(facs)==1: qs.append(facs[0])
        reuse=len(qs)-len(set(qs)); total_reuse+=reuse; total_single+=len(qs); total_comp+=rec['composite_holes']; total_prime+=rec['prime_holes']; max_reuse=max(max_reuse,reuse)
        ratio=len(qs)/rec['composite_holes'] if rec['composite_holes'] else 0
        worst_ratio=max(worst_ratio,ratio)
        key=(rec['prime_holes'], -ratio, reuse, rec['holes'])
        if best is None or key < best[0]: best=(key,a,rec,len(qs),reuse,ratio)
    n=P-1
    print(f"P={P} y={y} avgPrime={total_prime/n:.2f} avgComp={total_comp/n:.2f} avgSingle={total_single/n:.2f} avgReuse={total_reuse/n:.3f} maxReuse={max_reuse} worstSingleRatio={worst_ratio:.3f}")
    _,a,rec,single,reuse,ratio=best
    print(f"  dangerous a={a} H={rec['holes']} prime={rec['prime_holes']} comp={rec['composite_holes']} single={single} reuse={reuse} singleRatio={ratio:.3f} sharedEdges={rec['shared_edges']} maxhit={rec['max_q_hit']}")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003'); ap.add_argument('--ys',default='101,173,293,503'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for y in [int(x) for x in args.ys.split(',') if x.strip() and int(x)<P]: summarize(P,y)
if __name__=='__main__': main()
