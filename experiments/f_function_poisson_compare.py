#!/usr/bin/env python3
"""比较 B11 大集合中 F(d) 实际平均与 Poisson(lambda) 模型。
F(d)=1_{d>=1}+C(d,3)+C(d,4)+...

用法示例：
  python3 experiments/f_function_poisson_compare.py --Ps 8009,16001,32003,64007 --K 12
"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]
def F(d): return (1 if d>=1 else 0) + sum(math.comb(d,j) for j in range(3,d+1))
def poisson_F(lam, maxd=30):
    s=0.0; p=math.exp(-lam)
    prob=p
    for d in range(0,maxd+1):
        if d>0: prob*=lam/d
        s+=F(d)*prob
    return s
p=argparse.ArgumentParser(); p.add_argument('--Ps',default='8009,16001,32003,64007'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--minN',type=int,default=200)
args=p.parse_args()
rows=[]
print('P step N avg_lambda avgF poissonF ratio dist_tail')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        avg_lam=st['lam_sum']/N
        avgF=sum(F(d)*c for d,c in dist.items())/N
        pf=poisson_F(avg_lam)
        tail={d:c for d,c in sorted(dist.items()) if d>=3}
        rows.append((avgF,pf,avg_lam,P,idx,N))
        print(P,idx,N,f'{avg_lam:.4f}',f'{avgF:.4f}',f'{pf:.4f}',f'{avgF/pf if pf else 0:.3f}',tail)
print('worst_avgF',max(rows,key=lambda x:x[0]) if rows else None)
print('worst_ratio',max(rows,key=lambda x:x[0]/x[1]) if rows else None)
