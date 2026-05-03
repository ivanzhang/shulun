#!/usr/bin/env python3
"""分析最长坏段中半素数证书链的较小因子 u_i 结构。"""
import argparse, math
from collections import Counter
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def profile(P,row,flags,plist,small,B):
    L,start,end,cands=find_bad_segments(P,row,flags,small)[0]
    records=[]
    for c in cands:
        n=(row-1)*P+c
        fac=factor_distinct(n,plist)
        records.append((c,n,fac,min(fac),max(fac),len(fac)))
    semis=[r for r in records if r[5]==2]
    us=[r[3] for r in semis]
    cs=[r[0] for r in semis]
    ugaps=[b-a for a,b in zip(sorted(us), sorted(us)[1:])]
    cgaps=[b-a for a,b in zip(sorted(cs), sorted(cs)[1:])]
    return L,start,end,records,us,ugaps,cgaps


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--top',type=int,default=4); args=ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        best=[]
        for row in range(1,P+1):
            segs=find_bad_segments(P,row,flags,small)
            if segs:
                L,start,end,cands=segs[0]
                best.append((L/math.sqrt(P),L,row,start,end,len(cands)))
        print(f'P={P} B={B}')
        for ratio,L,row,start,end,cnum in sorted(best, reverse=True)[:args.top]:
            L,start,end,records,us,ugaps,cgaps=profile(P,row,flags,plist,small,B)
            print(f' row={row} seg={start}-{end} L={L} ratio={L/math.sqrt(P):.3f} cand={len(records)} semi={len(us)}')
            if us:
                print('  u min/avg/max distinct', min(us), round(mean(us),1), max(us), len(set(us)), 'u<=L', sum(1 for u in us if u<=L), 'u<=2L', sum(1 for u in us if u<=2*L))
                print('  uGaps min/avg/max', (min(ugaps), round(mean(ugaps),1), max(ugaps)) if ugaps else None, 'cGaps', (min(cgaps), round(mean(cgaps),1), max(cgaps)) if cgaps else None)
                print('  u sorted', sorted(us)[:20])

if __name__=='__main__': main()
