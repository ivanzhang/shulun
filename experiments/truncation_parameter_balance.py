#!/usr/bin/env python3
"""PV1 截断参数平衡：Q0=prod_{p<=y}p 的边界大小与尾部素数规模。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ls',default='89,127,179,253,357,1000,10000'); args=ap.parse_args()
    print('L y Q0 boundaryRatio tailSum_p_gt_y_to_L')
    for L in [int(x) for x in args.Ls.split(',') if x.strip()]:
        ps=primes(sieve(max(L,10)), max(L,10))
        for y in [2,3,5,7,11,13,17,19,23,29,31]:
            if y>L: continue
            Q=1
            for p in ps:
                if p<=y: Q*=p
            tail=sum(1/p for p in ps if y<p<=L)
            print(L,y,Q,f'{Q/L:.4f}',f'{tail:.4f}')
        print('-')
if __name__=='__main__': main()
