#!/usr/bin/env python3
"""局部窗口 T3 粗三因子误差的高矩与极值。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def moments(vals):
    mu=mean(vals); cen=[v-mu for v in vals]; var=mean(x*x for x in cen); m4=mean(x**4 for x in cen); m6=mean(x**6 for x in cen)
    return mu,var,m4/(var*var) if var else 0,m6/(var**3) if var else 0,min(vals),max(vals)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cs',default='4,5,6'); args=ap.parse_args()
    print('P C L meanT varT var/mean m4/var2 m6/var3 minT maxT maxT/mean')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8); Ts=[]
            for row in range(1,P+1):
                pref=[0]*(P+1)
                for c in range(1,P+1):
                    n=(row-1)*P+c; T=0
                    if all(n%q for q in small) and not flags[n]:
                        fac=factor_distinct(n,plist)
                        if all(q>B for q in fac) and len(fac)==3: T=1
                    pref[c]=pref[c-1]+T
                for start in range(1,P-L+2,step):
                    Ts.append(pref[start+L-1]-pref[start-1])
            mu,var,k4,k6,mn,mx=moments(Ts)
            print(P,C,L,f'{mu:.4f}',f'{var:.4f}',f'{var/mu if mu else 0:.3f}',f'{k4:.3f}',f'{k6:.3f}',mn,mx,f'{mx/mu if mu else 0:.2f}')

if __name__=='__main__': main()
