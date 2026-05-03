#!/usr/bin/env python3
"""H_c(P,a) 的精确一二阶矩（按 a 扫描）与差分公式探索。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P mean second var min lowerCheb1 lowerCheb2 scaleMean')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_count(P,a,y,small) for a in range(1,P)]
        mu=mean(vals); second=mean([v*v for v in vals]); var=second-mu*mu; mn=min(vals); scale=P/math.log(P)
        # 粗 Chebyshev：min >= mu - sqrt((P-2)*var)，很弱；输出看看。
        lower1=mu-math.sqrt((P-2)*var)
        lower2=mu-4*math.sqrt(var)
        print(f'{P} {mu:.4f} {second:.2f} {var:.2f} {mn} {lower1:.2f} {lower2:.2f} {mu/scale:.4f}')
if __name__=='__main__': main()
