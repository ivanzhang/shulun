#!/usr/bin/env python3
"""r 点 connected cumulant 采样实验，验证 Gallagher Gr。"""
import argparse, math, random, itertools
from high_threshold_margin_fast import sieve, primes


def partitions(seq):
    if not seq:
        yield []
        return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield [[first]]+[b[:] for b in rest]
        for i in range(len(rest)):
            new=[b[:] for b in rest]
            new[i]=[first]+new[i]
            yield new

def mobius_coeff(k):
    return (-1)**(k-1)*math.factorial(k-1)

def weight(offsets, small):
    if not offsets: return 1.0
    w=1.0
    for p in small:
        nu=len({o%p for o in offsets})
        if nu>=p: return 0.0
        w*=1-nu/p
    return w

def EY(offsets, small, pB):
    offs=list(offsets); r=len(offs); total=0.0
    for mask in range(1<<r):
        subset=[offs[i] for i in range(r) if mask>>i & 1]
        sign=(-1)**(r-len(subset))
        total += sign*weight(subset,small)/(pB**len(subset))
    return total

def cumulant(offsets, small, pB):
    idx=list(range(len(offsets))); total=0.0
    for part in partitions(idx):
        prod=1.0
        for block in part:
            prod*=EY([offsets[i] for i in block],small,pB)
        total += mobius_coeff(len(part))*prod
    return total

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--r',type=int,default=5); ap.add_argument('--samples',type=int,default=20000); ap.add_argument('--seed',type=int,default=1); args=ap.parse_args()
    random.seed(args.seed); P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); small=primes(sieve(B),B)
    pB=1.0
    for p in small: pB*=1-1/p
    vals=[]
    for _ in range(args.samples):
        offs=[0]+sorted(random.sample(range(1,L+1),args.r-1))
        vals.append(cumulant(offs,small,pB))
    print('P B L r samples meanCum meanAbsCum sumCum maxAbsCum')
    print(P,B,L,args.r,args.samples,f'{sum(vals)/len(vals):.6f}',f'{sum(abs(x) for x in vals)/len(vals):.6f}',f'{sum(vals):.3f}',f'{max(abs(x) for x in vals):.3f}')
if __name__=='__main__': main()
