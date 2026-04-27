#!/usr/bin/env python3
"""用 M2>=M1-U 的恒等式下界重写 IE3。\nIE3=M1-M2+M3 <= U+M3。\n若 M3 小且 U 已有粗上界，则闭合。\n"""
import argparse, math, sys
sys.path.append('experiments')
from d_distribution_m2_global import scan

def parse_ps(text): return [int(x.strip()) for x in text.split(',') if x.strip()]

p=argparse.ArgumentParser(); p.add_argument('--Ps',default='4001,8009,16001'); p.add_argument('--A',type=int,default=83); p.add_argument('--y',type=int,default=7); p.add_argument('--K',type=int,default=10); p.add_argument('--minN',type=int,default=50)
args=p.parse_args()
print('P step N U/N M3/N UplusM3/N actualIE3/N')
for P in parse_ps(args.Ps):
    stats=scan(P,args.A,args.y,args.K)
    for idx in range(1,args.K+1):
        st=stats[idx]; dist=st['dist']; N=sum(dist.values())
        if N<args.minN: continue
        U=N-dist[0]
        M1=st['d_sum']; M2=sum(math.comb(d,2)*c for d,c in dist.items() if d>=2); M3=sum(math.comb(d,3)*c for d,c in dist.items() if d>=3)
        print(P,idx,N,f'{U/N:.4f}',f'{M3/N:.4f}',f'{(U+M3)/N:.4f}',f'{(M1-M2+M3)/N:.4f}')
