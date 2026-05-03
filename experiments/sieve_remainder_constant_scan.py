#!/usr/bin/env python3
"""扫描 min_a |H_c(P,a)| / (P/log P) 的常数。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001,8009'); ap.add_argument('--cs',default='0.75,0.78,0.8,0.82,0.85,0.9'); args=ap.parse_args()
    print('P c y minH const minA tailConst needConst margin')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P)
        scale=P/math.log(P)
        for c in [float(x) for x in args.cs.split(',') if x.strip()]:
            y=int(c*P); small=[q for q in root if q<=y]
            minH=10**9; mina=None
            for a in range(1,P):
                H=H_count(P,a,y,small)
                if H<minH: minH=H; mina=a
            tail=2*sum(1 for q in root if y<q<P)
            print(f'{P} {c:.3f} {y} {minH} {minH/scale:.4f} {mina} {tail/scale:.4f} {2*(1-c):.4f} {minH-tail}')
if __name__=='__main__': main()
