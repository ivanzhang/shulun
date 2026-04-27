#!/usr/bin/env python3
"""长期幸存路径的不同补丁素数 CRT 模数统计。

用法示例：
  python3 experiments/singleton_tail_distinct_modulus.py --P 64007 --K 30 --y 11
"""
import argparse, math, sys
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=30); p.add_argument('--top',type=int,default=12)
args=p.parse_args()
records=[]
for group in template_groups(args.P,args.A,args.y,args.K):
    states=[(a,()) for a in group['anchors']]
    for idx,r in enumerate(group['holes'],start=1):
        new=[]
        for a,path in states:
            n=a+r*args.P
            patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
            if patches:
                new.append((a,path+(min(patches),)))
            else:
                if path: records.append((idx,a,path,group['pattern'],group['holes'][:idx]))
        states=new
    for a,path in states:
        if path: records.append((args.K+1,a,path,group['pattern'],group['holes']))
print('death a len distinct_len distinct_modulus repeated_count path pattern')
for death,a,path,pat,holes in sorted(records, reverse=True)[:args.top]:
    distinct=sorted(set(path)); mod=math.prod(distinct); repeats=len(path)-len(distinct)
    print(death,a,len(path),len(distinct),mod,repeats,path,pat)
