#!/usr/bin/env python3
"""单点路径后的后续幸存寿命与补丁证书增长。

用法示例：
  python3 experiments/singleton_tail_life.py --P 64007 --start 7 --K 30 --y 11
"""
import argparse, math, sys
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=30); p.add_argument('--start',type=int,default=7); p.add_argument('--top',type=int,default=10)
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
                if idx>=args.start and path:
                    records.append((idx,args.K,a,path,group['pattern'],group['holes'][:idx]))
        states=new
        if idx==args.start:
            # 记录此时所有单点状态后续由循环自然跟踪；不截断。
            pass
    for a,path in states:
        if path:
            records.append((args.K+1,args.K,a,path,group['pattern'],group['holes']))
# 只看 start 后仍活过来的路径：死亡步越大越坏
bad=sorted(records, reverse=True)[:args.top]
print('P',args.P,'start',args.start,'records',len(records))
print('death_idx a path_len path_prod path pattern holes_prefix')
for death,K,a,path,pat,holes in bad:
    prod=math.prod(path)
    print(death,a,len(path),prod,path,pat,holes[-12:])
