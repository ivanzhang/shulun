#!/usr/bin/env python3
"""用特征 1_{d1|a}1_{d2|b}1_{d3|a-b} 验证 K3 投影结构的小模数展开可表达性。"""
import argparse, math
from itertools import product
from high_threshold_margin_fast import sieve, primes
from three_point_singular_cumulant import weight


def K3(a,b,small,pB):
    return weight([0,a,b],small)/(pB**3)-weight([0,a],small)/(pB*pB)-weight([0,b],small)/(pB*pB)-weight([a,b],small)/(pB*pB)+2

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--mods',default='2,3,5'); args=ap.parse_args()
    mods=[int(x) for x in args.mods.split(',')]; Q=1
    for p in mods: Q*=p
    small=mods; pB=1.0
    for p in small: pB*=1-1/p
    # 投影完整周期验证：固定 a mod Q，对 b mod Q 求和。
    print('Q a sum_b_K3 mean')
    for a in range(Q):
        vals=[K3(a,b,small,pB) for b in range(Q)]
        print(Q,a,f'{sum(vals):.12g}',f'{sum(vals)/Q:.12g}')
if __name__=='__main__': main()
