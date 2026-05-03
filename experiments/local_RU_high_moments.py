#!/usr/bin/env python3
"""R(可复用) 与 U(单命中) 局部窗口高阶矩。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def moments(vals):
    mu=mean(vals); cen=[v-mu for v in vals]; var=mean(x*x for x in cen); m4=mean(x**4 for x in cen); m6=mean(x**6 for x in cen)
    return mu,var,m4/(var*var) if var else 0,m6/(var**3) if var else 0,min(vals),(mu-min(vals))/math.sqrt(var) if var else 0


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--Cs',default='4,5,6'); args=ap.parse_args()
    print('P C L comp mean var var/mean m4/var2 m6/var3 min minSigma')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8)
            Rs=[]; Us=[]
            for row in range(1,P+1):
                prefR=[0]*(P+1); prefU=[0]*(P+1)
                for c in range(1,P+1):
                    n=(row-1)*P+c; R=U=0
                    if all(n%q for q in small) and not flags[n]:
                        fac=factor_distinct(n,plist)
                        if all(q>B for q in fac) and len(fac)==2:
                            if min(fac)<=L: R=1
                            else: U=1
                    prefR[c]=prefR[c-1]+R; prefU[c]=prefU[c-1]+U
                for start in range(1,P-L+2,step):
                    end=start+L-1; Rs.append(prefR[end]-prefR[start-1]); Us.append(prefU[end]-prefU[start-1])
            for name,vals in [('R',Rs),('U',Us),('S', [r+u for r,u in zip(Rs,Us)])]:
                mu,var,k4,k6,mn,ms=moments(vals)
                print(P,C,L,name,f'{mu:.3f}',f'{var:.3f}',f'{var/mu if mu else 0:.3f}',f'{k4:.3f}',f'{k6:.3f}',mn,f'{ms:.3f}')

if __name__=='__main__': main()
