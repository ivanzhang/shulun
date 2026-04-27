#!/usr/bin/env python3
"""B11 大集合阈值敏感性：max(U+M3+H4) 随 minN 变化。

用法示例：
  python3 experiments/b11_threshold_sensitivity.py --Ps 16001,32003,64007 --K 12
"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='16001,32003,64007'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=11); p.add_argument('--K',type=int,default=12); p.add_argument('--thresholds',default='50,100,200,300,500')
args=p.parse_args()
thresholds=[int(x) for x in args.thresholds.split(',')]
rows=[]
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if not N: continue
        U=N-dist[0]
        M3=sum(math.comb(d,3)*c for d,c in dist.items() if d>=3)
        H4=sum(math.comb(d,4)*c for d,c in dist.items() if d>=4)
        rows.append({'P':P,'idx':idx,'N':N,'sum':(U+M3+H4)/N,'U':U/N,'M3':M3/N,'H4':H4/N})
print('threshold max_sum row')
for th in thresholds:
    eligible=[r for r in rows if r['N']>=th]
    if not eligible:
        print(th,'none')
        continue
    worst=max(eligible,key=lambda r:r['sum'])
    print(th,f'{worst["sum"]:.4f}',worst)
