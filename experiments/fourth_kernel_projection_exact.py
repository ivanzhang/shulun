#!/usr/bin/env python3
"""小 P 精确计算四点中心化核的一阶/二阶投影。"""
import argparse
from statistics import mean
from fourth_kernel_projection import prob_subset, kernel
from high_threshold_margin_fast import sieve, primes


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=101); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--r0',type=int,default=0); ap.add_argument('--pair',default='0,2'); args=ap.parse_args()
    P=args.P; flags=sieve(P); root=primes(flags,P); small=[q for q in root if q<=int(args.c*P)]; p=prob_subset([0],small); p4=p**4
    r0=args.r0
    vals=[]
    for b in range(P):
        for c in range(P):
            for d in range(P):
                vals.append(kernel([r0,b,c,d],small,p))
    one=mean(vals)/p4
    a,b=[int(x) for x in args.pair.split(',')]
    vals=[]
    for c in range(P):
        for d in range(P): vals.append(kernel([a,b,c,d],small,p))
    two=mean(vals)/p4
    allv=[]
    for a0 in range(P):
        for b0 in range(P):
            for c0 in range(P):
                for d0 in range(P):
                    allv.append(kernel([a0,b0,c0,d0],small,p))
    allmean=mean(allv)/p4
    print(f'P={P} p={p:.8g} oneProj/p4={one:.12g} twoProj/p4={two:.12g} allMean/p4={allmean:.12g}')

if __name__=='__main__': main()
