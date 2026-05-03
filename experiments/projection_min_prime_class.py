#!/usr/bin/env python3
"""单变量投影按连接 h 的最小小素数分类。

以 K3(a,b) 固定 a，对 b 求和。分类 b 与 {0,a} 发生碰撞的最小 p：p|b 或 p|b-a。
"""
import argparse, math
from collections import defaultdict
from high_threshold_margin_fast import sieve, primes
from three_point_singular_cumulant import weight


def K3(a,b,small,pB):
    return weight([0,a,b],small)/(pB**3)-weight([0,a],small)/(pB*pB)-weight([0,b],small)/(pB*pB)-weight([a,b],small)/(pB*pB)+2

def min_conn_prime(a,b,small):
    for p in small:
        if b%p==0 or (b-a)%p==0:
            return p
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--a',type=int,default=48); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); small=primes(sieve(B),B); pB=1.0
    for p in small: pB*=1-1/p
    stats=defaultdict(lambda:[0,0.0,0.0])
    for b in range(1,L+1):
        if b==args.a: continue
        key=min_conn_prime(args.a,b,small)
        val=K3(args.a,b,small,pB)
        stats[key][0]+=1; stats[key][1]+=val; stats[key][2]+=abs(val)
    print('P L a class count sum mean absMean')
    for key in sorted(stats, key=lambda x: 999 if x is None else x):
        c,s,ab=stats[key]
        print(P,L,args.a,key,c,f'{s:.6f}',f'{s/c:.6f}',f'{ab/c:.6f}')
if __name__=='__main__': main()
