#!/usr/bin/env python3
"""检验 d 分布是否被 Poisson(lambda) 常数倍尾支配。

用法示例：
  python3 experiments/d_tail_dominance.py --Ps 16001,32003,64007 --K 12 --y 11
"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]
def pois_tail(lam,k):
    s=0.0; prob=math.exp(-lam)
    for d in range(0,80):
        if d>0: prob*=lam/d
        if d>=k: s+=prob
    return s
p=argparse.ArgumentParser(); p.add_argument('--Ps',default='16001,32003,64007'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--minN',type=int,default=200)
args=p.parse_args()
rows=[]
print('P step N lambda tail1 ratio1 tail2 ratio2 tail3 ratio3 tail4 ratio4')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        lam=st['lam_sum']/N
        out=[P,idx,N,f'{lam:.4f}']
        maxratio=0
        for k in [1,2,3,4]:
            actual=sum(c for d,c in dist.items() if d>=k)/N
            model=pois_tail(lam,k)
            ratio=actual/model if model else 0
            maxratio=max(maxratio,ratio)
            out += [f'{actual:.4f}', f'{ratio:.3f}']
        rows.append((maxratio,P,idx,N,lam))
        print(*out)
print('worst_tail_ratio',max(rows) if rows else None)
