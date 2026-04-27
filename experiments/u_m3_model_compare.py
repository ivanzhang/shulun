#!/usr/bin/env python3
"""比较 U 与 M3 的粗模型：U≈1-exp(-lambda), M3≈lambda^3/6。

用法示例：
  python3 experiments/u_m3_model_compare.py --Ps 8009,16001,32003 --K 8
"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='8009,16001,32003'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=7); p.add_argument('--K',type=int,default=8); p.add_argument('--minN',type=int,default=100)
args=p.parse_args()
print('P step N avg_lambda U_rate U_model M3_rate M3_model sum_model')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        avg_lambda=st['lam_sum']/N
        U=N-dist[0]
        M3=sum(math.comb(d,3)*c for d,c in dist.items() if d>=3)
        u_model=1-math.exp(-avg_lambda)
        m3_model=avg_lambda**3/6
        print(P,idx,N,f'{avg_lambda:.3f}',f'{U/N:.4f}',f'{u_model:.4f}',f'{M3/N:.4f}',f'{m3_model:.4f}',f'{u_model+m3_model:.4f}')
