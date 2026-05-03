#!/usr/bin/env python3
"""三点 cumulant 按小素数碰撞类分组。

分类：是否存在 p<=B 使三个 offset 模 p 全相同/两两碰撞/全覆盖 p=2或3导致权重0。
"""
import argparse, math
from collections import defaultdict
from high_threshold_margin_fast import sieve, primes


def weight(offsets, small):
    w=1.0
    zero=False
    for p in small:
        nu=len({o%p for o in offsets})
        if nu>=p: return 0.0
        w*=1-nu/p
    return w


def cls(a,b,small):
    triple=0; pair=0; zero2=False; zero3=False
    for p in small:
        residues={0%p,a%p,b%p}
        nu=len(residues)
        if nu>=p:
            if p==2: zero2=True
            if p==3: zero3=True
        if nu==1: triple+=1
        elif nu==2: pair+=1
    if zero2: return 'zero_p2'
    if zero3: return 'zero_p3'
    if triple: return 'has_triple_collision'
    if pair>=3: return 'many_pair_collision'
    if pair: return 'few_pair_collision'
    return 'generic'


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); small=primes(sieve(B),B)
    pB=1.0
    for p in small: pB*=1-1/p
    stats=defaultdict(lambda:[0,0.0,0.0,0.0])
    for a in range(1,L+1):
        w01=weight([0,a],small)/(pB*pB)
        for b in range(a+1,L+1):
            w02=weight([0,b],small)/(pB*pB); w12=weight([a,b],small)/(pB*pB); w3=weight([0,a,b],small)/(pB**3)
            k3=w3-w01-w02-w12+2; key=cls(a,b,small)
            st=stats[key]; st[0]+=1; st[1]+=k3; st[2]+=abs(k3); st[3]=max(st[3],abs(k3))
    print('P B L class count meanK3 meanAbsK3 sumK3 maxAbs')
    for key,st in sorted(stats.items()):
        print(P,B,L,key,st[0],f'{st[1]/st[0]:.6f}',f'{st[2]/st[0]:.6f}',f'{st[1]:.3f}',f'{st[3]:.3f}')
if __name__=='__main__': main()
