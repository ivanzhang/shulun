#!/usr/bin/env python3
"""四点小模数 connected cumulant 小网格实验。

对 offsets {0,a,b,c} 计算归一化变量 Y=1_A/pB-1 的四阶 cumulant：
  cum4 = E[Y0YaYbYc] - E[Y0Ya]E[YbYc] - E[Y0Yb]E[YaYc] - E[Y0Yc]E[YaYb]
扫描 1<=a<b<c<=L 的子范围或采样。
"""
import argparse, math, random
from itertools import combinations
from high_threshold_margin_fast import sieve, primes


def weight(offsets, small):
    w=1.0
    for p in small:
        nu=len({o%p for o in offsets})
        if nu>=p: return 0.0
        w*=1-nu/p
    return w


def EY(offsets, small, pB):
    r=len(offsets)
    # E prod (I/pB -1) = sum_{T subset offsets} (-1)^{r-|T|} W(T)/pB^|T|
    offs=list(offsets); total=0.0
    for mask in range(1<<r):
        subset=[offs[i] for i in range(r) if mask>>i & 1]
        sign=(-1)**(r-len(subset))
        if subset:
            total += sign*weight(subset,small)/(pB**len(subset))
        else:
            total += sign
    return total


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--limit',type=int,default=70); ap.add_argument('--samples',type=int,default=0); ap.add_argument('--seed',type=int,default=1); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=min(max(1,int(args.C*math.sqrt(P))), args.limit); small=primes(sieve(B),B)
    pB=1.0
    for p in small: pB*=1-1/p
    triples=list(combinations(range(1,L+1),3))
    if args.samples and args.samples<len(triples):
        random.seed(args.seed); triples=random.sample(triples,args.samples)
    vals=[]; raw4=[]; pairpart=[]
    for a,b,c in triples:
        e4=EY([0,a,b,c],small,pB)
        e01=EY([0,a],small,pB); e23=EY([b,c],small,pB)
        e02=EY([0,b],small,pB); e13=EY([a,c],small,pB)
        e03=EY([0,c],small,pB); e12=EY([a,b],small,pB)
        pp=e01*e23+e02*e13+e03*e12
        vals.append(e4-pp); raw4.append(e4); pairpart.append(pp)
    print('P B L count meanCum4 meanAbsCum4 sumCum4 maxAbsCum4 meanRaw4 meanPairPart')
    print(P,B,L,len(vals),f'{sum(vals)/len(vals):.6f}',f'{sum(abs(x) for x in vals)/len(vals):.6f}',f'{sum(vals):.3f}',f'{max(abs(x) for x in vals):.3f}',f'{sum(raw4)/len(raw4):.6f}',f'{sum(pairpart)/len(pairpart):.6f}')
if __name__=='__main__': main()
