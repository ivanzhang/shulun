#!/usr/bin/env python3
"""扫描弱目标 U/|S| 与 M3/|S| 的常数余量。

用法示例：
  python3 experiments/u_m3_weak_targets.py --Ps 4001,8009,16001 --K 12 --minN 50
"""
import argparse
import math
import sys

sys.path.append('experiments')
from d_distribution_m2_global import scan


def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='4001,8009,16001'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=7); p.add_argument('--K',type=int,default=12); p.add_argument('--minN',type=int,default=50)
args=p.parse_args()
rows=[]
print('P step N U_rate M3_rate sum_rate d_ge3_rate d4_rate')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        U=N-dist[0]
        M3=sum(math.comb(d,3)*c for d,c in dist.items() if d>=3)
        dge3=sum(c for d,c in dist.items() if d>=3)
        d4=sum(c for d,c in dist.items() if d>=4)
        row=(U/N,M3/N,(U+M3)/N,P,idx,N,dge3/N,d4/N)
        rows.append(row)
        print(P,idx,N,f'{U/N:.4f}',f'{M3/N:.4f}',f'{(U+M3)/N:.4f}',f'{dge3/N:.4f}',f'{d4/N:.5f}')
print('worst_U',max(rows,key=lambda x:x[0]) if rows else None)
print('worst_M3',max(rows,key=lambda x:x[1]) if rows else None)
print('worst_sum',max(rows,key=lambda x:x[2]) if rows else None)
