#!/usr/bin/env python3
"""枚举 y=7 时模 210 的前洞形状。

小骨架洞为 gcd(r-c,210)=1。对每个平移 c，取前 K 个非零洞形状，统计：
- 形状种类；
- 洞间距离可共享素因子；
- 是否包含很小洞；
用于把“前 K 洞全补”变成有限模式问题。

用法示例：
    python3 experiments/front_hole_shapes_mod210.py --K 5
"""
import argparse, math
from collections import Counter, defaultdict


def prime_factors(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d+=1 if d==2 else 2
    if n>1: out.append(n)
    return out


def front_holes(c,K,M=210,limit=500):
    hs=[]; r=1
    while len(hs)<K and r<limit:
        if math.gcd(r-c,M)==1: hs.append(r)
        r+=1
    return tuple(hs)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--K',type=int,default=5); args=ap.parse_args()
    shapes=defaultdict(list)
    for c in range(210): shapes[front_holes(c,args.K)].append(c)
    print(f"K={args.K},shape_count={len(shapes)}")
    rows=[]
    for shape,cs in shapes.items():
        dists=[]; share_primes=set()
        for i,a in enumerate(shape):
            for b in shape[i+1:]:
                d=b-a; dists.append(d)
                share_primes.update(p for p in prime_factors(d) if p>7)
        rows.append((max(shape), len(cs), shape, sorted(share_primes), sorted(set(dists))))
    rows.sort(key=lambda x:(-x[0], x[2]))
    print('largest-span shapes: maxr count shape share_primes distances')
    for row in rows[:40]: print(row)
    print('most-common shapes:')
    for shape,cs in sorted(shapes.items(), key=lambda kv:(-len(kv[1]), kv[0]))[:40]: print(len(cs),shape,cs[:20])

if __name__=='__main__': main()
