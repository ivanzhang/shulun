#!/usr/bin/env python3
"""长期路径中重复补丁素数对应的高度间距结构。

用法示例：
  python3 experiments/repeat_prime_gap_structure.py --P 64007 --K 30 --y 11 --top 20
"""
import argparse, math, sys
from collections import defaultdict, Counter
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=30); p.add_argument('--top',type=int,default=20)
args=p.parse_args()
items=[]
for group in template_groups(args.P,args.A,args.y,args.K):
    states=[(a,[],[]) for a in group['anchors']]
    for idx,r in enumerate(group['holes'],start=1):
        new=[]
        for a,qs,rs in states:
            n=a+r*args.P
            patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
            if patches: new.append((a,qs+[min(patches)],rs+[r]))
            else:
                if qs: items.append((idx,a,qs,rs,group['pattern']))
        states=new
    for a,qs,rs in states:
        if qs: items.append((args.K+1,a,qs,rs,group['pattern']))
print('death a q occurrences gaps positions rs pattern')
count=0
for death,a,qs,rs,pat in sorted(items, reverse=True):
    pos=defaultdict(list)
    for q,r in zip(qs,rs): pos[q].append(r)
    reps={q:v for q,v in pos.items() if len(v)>=2}
    if reps:
        for q,v in reps.items():
            gaps=[v[j]-v[i] for i in range(len(v)) for j in range(i+1,len(v))]
            print(death,a,q,len(v),gaps,v,rs,pat)
            count+=1
            if count>=args.top: raise SystemExit
