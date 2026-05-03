#!/usr/bin/env python3
"""采样块级旧区 dyadic 收缩。"""
from __future__ import annotations
import argparse, math
G=0.5772156649015328606

def build(n):
    tau=[0]*(n+1)
    for d in range(1,n+1):
        for m in range(d,n+1,d): tau[m]+=1
    A=[0]*(n+1); s=0
    for i in range(1,n+1): s+=tau[i]; A[i]=s
    return tau,A

def delta(A,y): return A[int(y)]-y*(math.log(y)+2*G-1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--x',type=int,default=1008000)
    ap.add_argument('--block',type=int,default=200)
    args=ap.parse_args()
    tau,A=build(2*args.x)
    rows=[]
    for lo in range(1,math.isqrt(args.x)+1,args.block):
        hi=min(math.isqrt(args.x),lo+args.block-1)
        c=2*sum(tau[a]*delta(A,args.x/a) for a in range(lo,hi+1))/(args.x**0.75)
        old=2*sum(tau[a]*delta(A,2*args.x/a) for a in range(lo,hi+1))/((2*args.x)**0.75)
        rows.append((old-c,lo,hi,c,old,old/c if abs(c)>1e-9 else None))
    for row in sorted(rows, reverse=True)[:10]: print(row)
    print('sum c',sum(r[3] for r in rows),'sum old',sum(r[4] for r in rows))
if __name__=='__main__': main()
