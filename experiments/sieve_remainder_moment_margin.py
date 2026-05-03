#!/usr/bin/env python3
"""检查 mean-k*std 是否超过尾部上界常数。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001,8009'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--ks',default='3,3.5,4'); args=ap.parse_args()
    print('P k mean-kstd tailBound margin constBound')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_count(P,a,y,small) for a in range(1,P)]
        mu=mean(vals); sd=pstdev(vals); tail=2*sum(1 for q in root if y<q<P); scale=P/math.log(P)
        for k in [float(x) for x in args.ks.split(',') if x.strip()]:
            b=mu-k*sd
            print(f'{P} {k:.1f} {b:.2f} {tail} {b-tail:.2f} {b/scale:.4f}')
if __name__=='__main__': main()
