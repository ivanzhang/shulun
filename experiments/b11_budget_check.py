#!/usr/bin/env python3
"""B11 大集合收缩预算检查：U、M3、H4 分项是否满足固定预算。

用法示例：
  python3 experiments/b11_budget_check.py --Ps 16001,32003,64007 --K 12 --minN 200
"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='16001,32003,64007'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--minN',type=int,default=200); p.add_argument('--budgetU',type=float,default=0.70); p.add_argument('--budgetM3',type=float,default=0.13); p.add_argument('--budgetH4',type=float,default=0.02)
args=p.parse_args()
viol=[]
print('P step N U M3 H4 total passU passM3 passH4 passTotal')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        U=(N-dist[0])/N
        M3=sum(math.comb(d,3)*c for d,c in dist.items() if d>=3)/N
        H4=sum(math.comb(d,4)*c for d,c in dist.items() if d>=4)/N
        total=U+M3+H4
        flags=(U<=args.budgetU,M3<=args.budgetM3,H4<=args.budgetH4,total<=args.budgetU+args.budgetM3+args.budgetH4)
        print(P,idx,N,f'{U:.4f}',f'{M3:.4f}',f'{H4:.4f}',f'{total:.4f}',*flags)
        if not all(flags): viol.append((P,idx,N,U,M3,H4,total,flags))
print('violations',viol)
