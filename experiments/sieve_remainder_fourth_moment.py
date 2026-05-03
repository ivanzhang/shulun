#!/usr/bin/env python3
"""H_c(P,a) 的四阶/六阶中心矩扫描。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001,8009'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P mean var m4 m4/var2 m6 m6/var3 highMomentBoundRatio')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_count(P,a,y,small) for a in range(1,P)]
        mu=mean(vals); centered=[v-mu for v in vals]
        var=mean([x*x for x in centered]); m4=mean([x**4 for x in centered]); m6=mean([x**6 for x in centered])
        # 高矩猜想 k=2: m4 <= (Ck)^k mu^k = (2C)^2 mu^2；输出 m4/mu^2
        print(f'{P} {mu:.3f} {var:.3f} {m4:.2f} {m4/(var*var):.3f} {m6:.2f} {m6/(var**3):.3f} {m4/(mu*mu):.4f}')
if __name__=='__main__': main()
