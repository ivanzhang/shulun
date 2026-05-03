#!/usr/bin/env python3
"""列高阈值筛余 H_alpha(P,c) 的均值、方差和高矩。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='1009,2003,4001'); ap.add_argument('--alphas',default='0.8,0.85,0.9'); args=ap.parse_args()
    print('P alpha y n mean var min minSigma m4/var2 m6/var3 zeroLowerMargin')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        root=primes(sieve(P),P)
        for alpha in [float(x) for x in args.alphas.split(',') if x.strip()]:
            y=int(alpha*P); small=[q for q in root if q<=y]
            vals=[H_count(P,c,y,small) for c in range(1,P)]
            mu=mean(vals); cen=[v-mu for v in vals]; var=mean(x*x for x in cen); sig=math.sqrt(var)
            m4=mean(x**4 for x in cen); m6=mean(x**6 for x in cen)
            tail=2*sum(1 for q in root if y<q<P)
            print(P,alpha,y,len(vals),f'{mu:.3f}',f'{var:.3f}',min(vals),f'{(mu-min(vals))/sig if sig else 0:.3f}',f'{m4/(var*var) if var else 0:.3f}',f'{m6/(var**3) if var else 0:.3f}',min(vals)-tail)
if __name__=='__main__': main()
