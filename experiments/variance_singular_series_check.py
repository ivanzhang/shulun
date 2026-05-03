#!/usr/bin/env python3
"""验证 H(a) 方差与差分二点相关/奇异级数的关系。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count
from sieve_remainder_pair_correlation import alive_matrix


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P mean var var/mean pairSumDiag pairSumOff reconstructedVar')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        A=alive_matrix(P,args.c)
        H=[sum(row) for row in A]
        mu=mean(H); var=mean([(h-mu)**2 for h in H])
        # E_a H^2 = sum_r E Xr + 2 sum_d sum_r E Xr Xr+d
        EH2=mean([h*h for h in H])
        diag=sum(sum(row[r] for row in A)/(P-1) for r in range(P))
        off=0.0
        for d in range(1,P):
            for r in range(P-d):
                off += 2*sum(row[r] & row[r+d] for row in A)/(P-1)
        rec_var=diag+off-mu*mu
        print(f'{P} {mu:.4f} {var:.4f} {var/mu:.4f} {diag:.4f} {off:.4f} {rec_var:.4f}')
if __name__=='__main__': main()
