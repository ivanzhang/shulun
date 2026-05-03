#!/usr/bin/env python3
"""局部小筛候选 H 的高阶矩。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--Cs',default='4,5,6'); args=ap.parse_args()
    print('P C L mean var var/mean m4/var2 m6/var3 min minSigma')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); small=primes(sieve(B),B)
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8); vals=[]
            for row in range(1,P+1):
                pref=[0]*(P+1); N0=(row-1)*P
                for c in range(1,P+1):
                    n=N0+c; pref[c]=pref[c-1]+(1 if all(n%q for q in small) else 0)
                for start in range(1,P-L+2,step): vals.append(pref[start+L-1]-pref[start-1])
            mu=mean(vals); cen=[v-mu for v in vals]; var=mean(x*x for x in cen); m4=mean(x**4 for x in cen); m6=mean(x**6 for x in cen); sig=math.sqrt(var)
            print(P,C,L,f'{mu:.3f}',f'{var:.3f}',f'{var/mu:.3f}',f'{m4/(var*var):.3f}',f'{m6/(var**3):.3f}',min(vals),f'{(mu-min(vals))/sig:.3f}')
if __name__=='__main__': main()
