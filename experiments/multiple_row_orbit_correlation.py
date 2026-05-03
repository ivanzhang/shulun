#!/usr/bin/env python3
"""量化倍数行 H(k) 与 H(mk) 的相关性。"""
import argparse, math
from statistics import mean, pstdev
from multiple_row_orbit_scan import H_row
from high_threshold_margin_fast import sieve, primes


def corr(xs,ys):
    mx=mean(xs); my=mean(ys); sx=pstdev(xs); sy=pstdev(ys)
    if sx==0 or sy==0: return 0
    return mean([(x-mx)*(y-my) for x,y in zip(xs,ys)])/(sx*sy)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--ms',default='2,3,4,5,6,10'); args=ap.parse_args()
    print('P m count corr meanBase meanMult minBaseAt baseH multH')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_row(P,k,y,small) for k in range(1,P+1)]
        for m in [int(x) for x in args.ms.split(',') if x.strip()]:
            xs=[]; ys=[]; ks=[]
            for k in range(2, P//m + 1): # 排除第1行平凡异常
                xs.append(vals[k-1]); ys.append(vals[m*k-1]); ks.append(k)
            if not xs: continue
            idx=min(range(len(xs)), key=lambda i: xs[i])
            print(f'{P} {m} {len(xs)} {corr(xs,ys):.3f} {mean(xs):.2f} {mean(ys):.2f} {ks[idx]} {xs[idx]} {ys[idx]}')
if __name__=='__main__': main()
