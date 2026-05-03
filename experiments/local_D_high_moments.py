#!/usr/bin/env python3
"""局部 D_J=Z_J 的高阶矩、极值 sigma 距离。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--Cs',default='3,4,5,6'); args=ap.parse_args()
    print('P C L n mean var min minSigma m4/var2 m6/var3 m8/var4 zeroRate bound4Ratio bound6Ratio')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); small=primes(sieve(B),B)
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8)
            vals=[]
            for row in range(1,P+1):
                pref=[0]*(P+1)
                for c in range(1,P+1):
                    n=(row-1)*P+c
                    cand=all(n%q for q in small)
                    pref[c]=pref[c-1]+(1 if cand and flags[n] else 0)
                for start in range(1,P-L+2,step):
                    vals.append(pref[start+L-1]-pref[start-1])
            mu=mean(vals); centered=[v-mu for v in vals]; var=mean(x*x for x in centered); sig=math.sqrt(var)
            m4=mean(x**4 for x in centered); m6=mean(x**6 for x in centered); m8=mean(x**8 for x in centered)
            # bound ratios for E|X|^{2k} <= (C k)^k mu^k, report with C=4 rough
            b4=m4/((4*2)**2 * (mu**2)) if mu else 0
            b6=m6/((4*3)**3 * (mu**3)) if mu else 0
            print(P,C,L,len(vals),f'{mu:.3f}',f'{var:.3f}',min(vals),f'{(mu-min(vals))/sig if sig else 0:.3f}',f'{m4/(var*var) if var else 0:.3f}',f'{m6/(var**3) if var else 0:.3f}',f'{m8/(var**4) if var else 0:.3f}',f'{sum(1 for v in vals if v==0)/len(vals):.5f}',f'{b4:.4f}',f'{b6:.4f}')

if __name__=='__main__': main()
