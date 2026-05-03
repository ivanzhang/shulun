#!/usr/bin/env python3
"""U dyadic 层保守上界和式。

对较小因子 u>L 的半素数，因 n<P^2 且余因子 v>=u，故 u<P。
每层用素数倒数和 sum_{U<u<=2U}1/u 作为极粗锚点上界，观察总和。
"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001,8009'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P B L layers primeRecipSum capped045?')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P)))
        flags=sieve(P+1); ps=primes(flags,P+1)
        total=0.0; layers=[]; lo=L
        while lo < P:
            hi=min(2*lo,P)
            s=sum(1/q for q in ps if lo < q <= hi)
            if s>0: layers.append((lo,hi,s)); total+=s
            lo*=2
        print(P,B,L,[(a,b,round(s,4)) for a,b,s in layers],f'{total:.4f}', total<0.45)
if __name__=='__main__': main()
