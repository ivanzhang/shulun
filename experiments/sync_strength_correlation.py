#!/usr/bin/env python3
"""同步强度 sum_{q|t}1/q 与 H 的相关性。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes
from multiple_row_orbit_scan import H_row
from truncated_mobius_predictor import corr


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P corrSyncH corrOmegaH meanSync topSyncRows')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        H=[]; strength=[]; omega=[]; rows=[]
        for k in range(1,P+1):
            t=k-1
            sync=small if t==0 else [q for q in small if t%q==0]
            s=sum(1/q for q in sync); om=len(sync); h=H_row(P,k,y,small)
            H.append(h); strength.append(s); omega.append(om); rows.append((s,om,h,k,t))
        rows.sort(reverse=True)
        print(f'{P} {corr(strength,H):.3f} {corr(omega,H):.3f} {mean(strength):.3f} {[(round(s,3),om,h,k) for s,om,h,k,t in rows[:8]]}')
if __name__=='__main__': main()
