#!/usr/bin/env python3
"""四点中心化奇异级数 cumulant 采样。

用局部模型 P(S)=prod_q(1-nu_q(S)/q)，单点 p=prod_q(1-1/q)。
对四个 distinct r，计算中心化组合：
E prod (X_i-p) = sum_{S subset [4]} (-p)^(4-|S|) P(S)。
按碰撞图（是否由小素数碰撞连通）分类。
"""
import argparse, random, itertools, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def prob_subset(R, idxs, small):
    if not idxs: return 1.0
    prob=1.0
    for q in small:
        nu=len({R[i] % q for i in idxs})
        if nu>=q: return 0.0
        prob *= (1-nu/q)
    return prob

def cumulant4(R, small, p):
    total=0.0
    inds=range(4)
    for mask in range(16):
        idxs=[i for i in inds if mask>>i & 1]
        total += ((-p)**(4-len(idxs))) * prob_subset(R, idxs, small)
    return total

def collision_components(R, small_limit_primes):
    parent=list(range(4))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    edges=0
    for q in small_limit_primes:
        buckets={}
        for i,r in enumerate(R): buckets.setdefault(r%q,[]).append(i)
        for group in buckets.values():
            if len(group)>=2:
                for i in range(len(group)-1): union(group[i],group[i+1]); edges+=1
    comps=len({find(i) for i in range(4)})
    return comps, edges

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--samples',type=int,default=20000); ap.add_argument('--seed',type=int,default=1); ap.add_argument('--collision-prime-limit',type=int,default=31); args=ap.parse_args()
    random.seed(args.seed); flags=sieve(args.P); root=primes(flags,args.P); y=int(args.c*args.P); small=[q for q in root if q<=y]; coll=[q for q in root if q<=args.collision_prime_limit]
    p=1.0
    for q in small: p*=1-1/q
    buckets={}
    vals=[]
    for _ in range(args.samples):
        R=tuple(random.sample(range(args.P),4))
        val=cumulant4(R,small,p)
        comps,edges=collision_components(R,coll)
        key=(comps, min(edges,6))
        buckets.setdefault(key,[]).append(val/(p**4) if p else 0)
        vals.append(val)
    print(f'P={args.P} c={args.c} p={p:.6g} samples={args.samples} meanCum={mean(vals):.6g} meanNorm={mean(vals)/(p**4):.4f}')
    for key,arr in sorted(buckets.items()):
        print('class',key,'n',len(arr),'meanNorm',round(mean(arr),4),'meanAbsNorm',round(mean(abs(x) for x in arr),4),'maxAbsNorm',round(max(abs(x) for x in arr),2))
if __name__=='__main__': main()
