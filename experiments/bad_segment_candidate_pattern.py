#!/usr/bin/env python3
"""分析最长坏段内小筛候选洞的位置间隔与半素数因子薄壳。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=2003); ap.add_argument('--row',type=int,default=1004); args=ap.parse_args()
    P=args.P; row=args.row; B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
    L,start,end,cands=find_bad_segments(P,row,flags,small)[0]
    gaps=[b-a for a,b in zip(cands,cands[1:])]
    small_factors=[]; large_factors=[]; balanced=0; semis=0
    for c in cands:
        fac=factor_distinct((row-1)*P+c,plist)
        if len(fac)==2:
            semis+=1; small_factors.append(min(fac)); large_factors.append(max(fac))
            if max(fac)/min(fac)<4: balanced+=1
    print(f'P={P} row={row} seg={start}-{end} L={L} candidates={len(cands)} density={len(cands)/L:.3f}')
    print('candidate positions', cands)
    print('gaps', gaps, 'avgGap', mean(gaps) if gaps else None, 'minmaxGap', (min(gaps),max(gaps)) if gaps else None)
    print(f'semiprime={semis} balancedRatio={balanced}/{semis}')
    if small_factors:
        print('smallFactor min/avg/max', min(small_factors), round(mean(small_factors),1), max(small_factors))
        print('largeFactor min/avg/max', min(large_factors), round(mean(large_factors),1), max(large_factors))
        print('small factors sorted', sorted(small_factors))

if __name__=='__main__': main()
