#!/usr/bin/env python3
"""二部补丁图匹配全列摘要。"""
import argparse
from patch_hall_bipartite import hopcroft_karp
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def summarize(P, y):
    flags=sieve(P*P); root=primes_from_flags(flags,P)
    total_unmatched=0; max_unmatched=0; perfect=0; cols=0; worst=None
    for a in range(1,P):
        rec=record_for(P,a,y,flags,root)
        graph={r:tuple(qs) for r,qs in rec['patch_factors_by_r'].items() if qs}
        if not graph:
            unmatched=0; match=0
        else:
            match,_,_=hopcroft_karp(graph); unmatched=len(graph)-match
        cols+=1; total_unmatched+=unmatched; max_unmatched=max(max_unmatched, unmatched); perfect += unmatched==0
        key=(-unmatched, rec['prime_holes'], rec['holes'])
        if worst is None or key < worst[0]: worst=(key,a,rec,unmatched,match)
    _,a,rec,unmatched,match=worst
    print(f"P={P} y={y} perfectCols={perfect}/{cols} avgUnmatched={total_unmatched/cols:.3f} maxUnmatched={max_unmatched}")
    print(f"  worst a={a} H={rec['holes']} prime={rec['prime_holes']} comp={rec['composite_holes']} match={match} unmatched={unmatched} sharedEdges={rec['shared_edges']} maxhit={rec['max_q_hit']}")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--ys',default='101,173,293'); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for y in [int(x) for x in args.ys.split(',') if x.strip() and int(x)<P]: summarize(P,y)
if __name__=='__main__': main()
