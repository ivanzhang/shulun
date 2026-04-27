#!/usr/bin/env python3
"""仅由洞高间距决定的重复容量上界/不同补丁下界。

给定前 T 个洞高度 rs，若同一 q 重复，则重复位置差必须被 q 整除。
计算每个 q 在 rs 中最多能出现多少次，以及覆盖 T 次证书所需的最少不同 q 数。

用法示例：
  python3 experiments/repeat_capacity_bound.py --y 11 --T 20 --patterns 20
"""
import argparse, math
from collections import Counter
from fixed_anchor_sieve_remainder import primes_upto


def holes_for_c(c, y, T):
    small=primes_upto(y); M=math.prod(small); holes=[]; r=1
    while len(holes)<T:
        if math.gcd((r-c)%M,M)==1: holes.append(r)
        r+=1
    return holes

def capacity(rs,y):
    D=max(rs)-min(rs)
    caps=[]
    for q in primes_upto(D+1):
        if q<=y: continue
        # q 可以命中的高度必须同余；最大同余类大小即容量。
        cnt=Counter(r%q for r in rs)
        m=max(cnt.values()) if cnt else 0
        if m>=2: caps.append((m,q))
    caps.sort(reverse=True)
    rem=len(rs); used=0
    for m,q in caps:
        if rem<=0: break
        rem-=m; used+=1
    if rem>0: used+=rem
    return D,caps,used

p=argparse.ArgumentParser(); p.add_argument('--y',type=int,default=11); p.add_argument('--T',type=int,default=20); p.add_argument('--patterns',type=int,default=20)
args=p.parse_args()
M=math.prod(primes_upto(args.y))
records=[]
for c in range(M):
    rs=holes_for_c(c,args.y,args.T)
    D,caps,lb=capacity(rs,args.y)
    records.append((lb,D,c,rs,caps[:10]))
print('y',args.y,'T',args.T,'M',M)
print('worst minimal distinct lower bounds')
for lb,D,c,rs,caps in sorted(records)[:args.patterns]:
    print('c',c,'lb',lb,'ratio',f'{lb/args.T:.3f}','D',D,'rs',rs,'top_caps',caps)
