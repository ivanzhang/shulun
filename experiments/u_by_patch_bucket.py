#!/usr/bin/env python3
"""诊断 U 覆盖率来源：按最小补丁因子/补丁桶统计。

用法示例：
  python3 experiments/u_by_patch_bucket.py --P 64007 --step 2 --y 11
"""
import argparse, math, sys
from collections import Counter
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups, covered_by_patch

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--step',type=int,default=2)
args=p.parse_args()
minq=Counter(); degree=Counter(); N=0; U=0
for group in template_groups(args.P,args.A,args.y,args.K):
    survivors=set(group['anchors']); target=None
    for idx,r in enumerate(group['holes'],start=1):
        if idx==args.step: target=r; break
        survivors={a for a in survivors if covered_by_patch(args.P,a,r,args.y)}
    for a in survivors:
        N+=1; n=a+target*args.P
        patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
        degree[len(patches)]+=1
        if patches:
            U+=1
            q=min(patches)
            bucket = 1 << (q.bit_length()-1)
            minq[bucket]+=1
print('P',args.P,'step',args.step,'N',N,'U',U,'rate',U/N if N else 0)
print('degree',sorted(degree.items()))
print('min_patch_power2_bucket',sorted(minq.items()))
