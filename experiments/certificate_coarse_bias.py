#!/usr/bin/env python3
"""粗证书特征与下一步覆盖率：按前证书最小因子/乘积大小分桶。

用法示例：
  python3 experiments/certificate_coarse_bias.py --P 64007 --step 4 --y 11
"""
import argparse, math, sys
from collections import defaultdict
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--step',type=int,default=4)
args=p.parse_args()
buckets=defaultdict(lambda:[0,0])
for group in template_groups(args.P,args.A,args.y,args.K):
    states=[(a,[]) for a in group['anchors']]
    for idx,r in enumerate(group['holes'],start=1):
        new=[]
        for a,path in states:
            n=a+r*args.P
            patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
            if idx<args.step:
                if patches: new.append((a,path+[min(patches)]))
            elif idx==args.step:
                if path:
                    prod=math.prod(path); mn=min(path)
                    key=(1<<(mn.bit_length()-1), 1<<(prod.bit_length()-1), len(path))
                else:
                    key=(0,0,0)
                buckets[key][0]+=1
                if patches: buckets[key][1]+=1
        states=new
        if idx>=args.step: break
print('P',args.P,'step',args.step,'bucket minq_pow2 prod_pow2 len size covered rate')
for key,(n,u) in sorted(buckets.items(), key=lambda kv:(kv[0][2],kv[0][1],kv[0][0])):
    if n>=10:
        print(key,n,u,f'{u/n:.3f}')
