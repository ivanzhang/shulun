#!/usr/bin/env python3
"""B11 小集合阶段：首次低于阈值后到灭绝还需几步。

用法示例：
  python3 experiments/b11_small_set_tail.py --Ps 8009,16001,32003,64007 --K 30 --threshold 200
"""
import argparse, sys
sys.path.append('experiments')
from template_cover_sieve import template_groups, covered_by_patch

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='8009,16001,32003,64007'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=30); p.add_argument('--threshold',type=int,default=200); p.add_argument('--top',type=int,default=5)
args=p.parse_args()
for P in parse_ps(args.Ps):
    tails=[]
    for group in template_groups(P,args.A,args.y,args.K):
        survivors=set(group['anchors']); first_below=None; extinct=None
        for idx,r in enumerate(group['holes'],start=1):
            if first_below is None and len(survivors)<args.threshold:
                first_below=idx-1
            survivors={a for a in survivors if covered_by_patch(P,a,r,args.y)}
            if not survivors:
                extinct=idx; break
        if first_below is None: first_below=args.K
        if extinct is None: extinct=args.K+1
        tails.append((extinct-first_below, extinct, first_below, len(group['anchors']), group['pattern'], group['holes'][:12]))
    print('P',P,'max_tail',max(tails),'top')
    for rec in sorted(tails,reverse=True)[:args.top]: print(' ',rec)
