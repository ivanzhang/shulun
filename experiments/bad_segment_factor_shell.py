#!/usr/bin/env python3
"""解剖局部振荡最长坏段中的小筛候选洞及粗合数因子结构。"""
import argparse, math
from collections import Counter
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from local_oscillation_lemma_scan import row_stats


def find_bad_segments(P,row,flags,small):
    is_prime=[]; is_cand=[]
    for c in range(1,P+1):
        n=(row-1)*P+c
        is_prime.append(bool(flags[n])); is_cand.append(all(n%q for q in small))
    segs=[]; c=1
    while c<=P:
        if is_prime[c-1]: c+=1; continue
        start=c; cand=[]
        while c<=P and not is_prime[c-1]:
            if is_cand[c-1]: cand.append(c)
            c+=1
        end=c-1
        if cand: segs.append((end-start+1,start,end,cand))
    return sorted(segs, reverse=True)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--rows',default=''); ap.add_argument('--top',type=int,default=3); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
    if args.rows: rows=[int(x) for x in args.rows.split(',') if x.strip()]
    else:
        best=[]
        for r in range(1,P+1):
            mb,ex,pc,cc=row_stats(P,r,flags,small); best.append((mb,r,pc,cc,ex))
        rows=[r for _,r,_,_,_ in sorted(best, reverse=True)[:args.top]]
        print('topBadRows', sorted(best, reverse=True)[:args.top])
    print(f'P={P} B={B}')
    for r in rows:
        segs=find_bad_segments(P,r,flags,small)
        L,start,end,cands=segs[0]
        print(f'row={r} longestBad={start}-{end} L={L} ratio={L/math.sqrt(P):.3f} candidates={len(cands)}')
        size_counter=Counter(); minfac=[]; maxfac=[]; factor_samples=[]; shared=Counter()
        for c in cands:
            n=(r-1)*P+c
            fac=factor_distinct(n,plist)
            size_counter[len(fac)]+=1
            minfac.append(min(fac)); maxfac.append(max(fac))
            for q in fac: shared[q]+=1
            factor_samples.append((c,n,fac))
        print(' factorCountDist', dict(size_counter), 'minFactorRange', (min(minfac),max(minfac)), 'maxFactorRange', (min(maxfac),max(maxfac)))
        print(' topSharedFactors', [(q,v) for q,v in shared.most_common(8) if v>1])
        print(' samples')
        for item in factor_samples[:12]: print('  c,n,fac=',item)

if __name__=='__main__': main()
