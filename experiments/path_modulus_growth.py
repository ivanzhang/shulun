#!/usr/bin/env python3
"""证书路径乘积模增长与路径大小统计。

用法示例：
  python3 experiments/path_modulus_growth.py --P 64007 --step 7 --y 11
"""
import argparse, math, sys
from collections import Counter, defaultdict
sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

p=argparse.ArgumentParser(); p.add_argument('--P',type=int,default=64007); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--step',type=int,default=7)
args=p.parse_args()
paths=defaultdict(int)
for group in template_groups(args.P,args.A,args.y,args.K):
    states=[(a,()) for a in group['anchors']]
    for idx,r in enumerate(group['holes'],start=1):
        new=[]
        for a,path in states:
            if idx==args.step:
                paths[path]+=1; continue
            n=a+r*args.P
            patches=[q for q,_ in factor(n) if q>args.y and q<=math.isqrt(n) and q!=args.P]
            if patches: new.append((a,path+(min(patches),)))
        states=new
        if idx>=args.step: break
bucket=Counter(); sizes=Counter(); total=sum(paths.values())
for path,n in paths.items():
    prod=math.prod(path) if path else 1
    b=1<<(prod.bit_length()-1)
    bucket[b]+=n
    sizes[n]+=1
print('P',args.P,'step',args.step,'path_count',len(paths),'total_points',total)
print('path_size_distribution',sizes.most_common(20))
print('prod_bucket points avg_path_count')
for b,pts in sorted(bucket.items()):
    cnt=sum(1 for path,n in paths.items() if (1<<((math.prod(path) if path else 1).bit_length()-1))==b)
    print(b,pts,cnt,f'{pts/cnt:.3f}')
