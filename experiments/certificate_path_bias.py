#!/usr/bin/env python3
"""证书路径偏聚：前几步最小补丁路径与下一步覆盖率的关系。

用法示例：
  python3 experiments/certificate_path_bias.py --P 64007 --step 4 --y 11 --top 20
"""
import argparse, math, sys
from collections import defaultdict, Counter
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--step',type=int,default=4); p.add_argument('--top',type=int,default=20)
args=p.parse_args()
paths=defaultdict(lambda:[0,0])
for group in template_groups(args.P,args.A,args.y,args.K):
    states=[(a,()) for a in group['anchors']]
    for idx,r in enumerate(group['holes'],start=1):
        new=[]
        for a,path in states:
            n=a+r*args.P
            patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
            if idx<args.step:
                if patches:
                    new.append((a,path+(min(patches),)))
            elif idx==args.step:
                rec=paths[path]
                rec[0]+=1
                if patches: rec[1]+=1
        states=new
        if idx>=args.step: break
print('P',args.P,'step',args.step,'paths',len(paths))
print('path size covered rate')
rows=[]
for path,(n,u) in paths.items(): rows.append((n,u/n if n else 0,u,path))
for n,rate,u,path in sorted(rows,reverse=True)[:args.top]: print(path,n,u,f'{rate:.3f}')
# weighted variance around global
N=sum(n for n,_,_,_ in rows); U=sum(u for _,_,u,_ in rows); g=U/N if N else 0
var=sum(n*(rate-g)**2 for n,rate,u,path in rows)/N if N else 0
print('global',N,U,f'{g:.4f}','weighted_sd',f'{var**0.5:.4f}')
