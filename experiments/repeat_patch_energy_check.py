#!/usr/bin/env python3
"""检查长期路径重复补丁次数与洞距共享能量。

用法示例：
  python3 experiments/repeat_patch_energy_check.py --P 64007 --K 30 --y 11 --top 12
"""
import argparse, math, sys
from collections import Counter
sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def omega_gt_y(n,y):
    x=n; c=0
    for p in primes_upto(math.isqrt(x)+1):
        if p*p>x: break
        if x%p==0:
            if p>y: c+=1
            while x%p==0: x//=p
    if x>1 and x>y: c+=1
    return c

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=30); p.add_argument('--top',type=int,default=12)
args=p.parse_args()
records=[]
for group in template_groups(args.P,args.A,args.y,args.K):
    states=[(a,[],[]) for a in group['anchors']] # a, qs, rs
    for idx,r in enumerate(group['holes'],start=1):
        new=[]
        for a,qs,rs in states:
            n=a+r*args.P
            patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
            if patches:
                new.append((a,qs+[min(patches)],rs+[r]))
            else:
                if qs: records.append((idx,a,qs,rs,group['pattern']))
        states=new
    for a,qs,rs in states:
        if qs: records.append((args.K+1,a,qs,rs,group['pattern']))

def energy(rs):
    return sum(omega_gt_y(abs(rs[j]-rs[i]),args.y) for i in range(len(rs)) for j in range(i+1,len(rs)))
print('death a T distinct repeats repeat_pairs energy distinct_ratio path pattern')
for death,a,qs,rs,pat in sorted(records, reverse=True)[:args.top]:
    counts=Counter(qs); repeat_pairs=sum(math.comb(v,2) for v in counts.values() if v>=2)
    repeats=len(qs)-len(counts); E=energy(rs)
    print(death,a,len(qs),len(counts),repeats,repeat_pairs,E,f'{len(counts)/len(qs):.3f}',qs,pat)
