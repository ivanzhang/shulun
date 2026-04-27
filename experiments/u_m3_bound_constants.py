#!/usr/bin/env python3
"""寻找 U 乘法筛上界和 M3 三因子上界的安全常数。

用法示例：
  python3 experiments/u_m3_bound_constants.py --Ps 8009,16001,32003 --K 10 --minN 200
"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='8009,16001,32003'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=7); p.add_argument('--K',type=int,default=10); p.add_argument('--minN',type=int,default=200)
args=p.parse_args()
rows=[]
print('P step N lambda U U_model U/model M3 L3 M3/L3 sum')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        lam=st['lam_sum']/N
        U=N-dist[0]
        M3=sum(math.comb(d,3)*c for d,c in dist.items() if d>=3)
        u_model=1-math.exp(-lam)
        L3=st['lam_sum']*0 # placeholder
        # 使用逐点 lambda^3/6
        # d_distribution_m2_global 没存 lam3，重新用模型近似 avg_lambda^3/6 给常数参考。
        m3_model=lam**3/6
        rows.append((U/N/u_model if u_model else 0, M3/N/m3_model if m3_model else 0, (U+M3)/N, P, idx, N, lam))
        print(P,idx,N,f'{lam:.3f}',f'{U/N:.4f}',f'{u_model:.4f}',f'{U/N/u_model if u_model else 0:.3f}',f'{M3/N:.4f}',f'{m3_model:.4f}',f'{M3/N/m3_model if m3_model else 0:.3f}',f'{(U+M3)/N:.4f}')
print('max_U_model_ratio',max(rows,key=lambda x:x[0]) if rows else None)
print('max_M3_model_ratio',max(rows,key=lambda x:x[1]) if rows else None)
print('max_sum',max(rows,key=lambda x:x[2]) if rows else None)
