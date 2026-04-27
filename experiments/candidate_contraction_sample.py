#!/usr/bin/env python3
"""候选收缩轻量抽样扫描。"""
import argparse
from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from a_space_candidate_decay import candidate_as


def analyze_one(P, y, Rmax):
    prev_size = None
    last_increase = None
    last_gain = None
    one_R = None
    zero_R = None
    prev_set = set()
    sizes = []
    for R in range(1, Rmax + 1):
        aset = {a for a, *_ in candidate_as(P, R, y)}
        size = len(aset)
        if prev_size is not None and size > prev_size:
            last_increase = R
        if aset - prev_set:
            last_gain = R
        if one_R is None and size <= 1:
            one_R = R
        if zero_R is None and size == 0:
            zero_R = R
            sizes.append(size)
            break
        sizes.append(size)
        prev_size = size
        prev_set = aset
    return one_R, zero_R, last_increase, last_gain, max(sizes), sizes[-1]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--maxP',type=int,default=500)
    ap.add_argument('--y',type=int,default=13)
    ap.add_argument('--Rcap',type=int,default=100)
    ap.add_argument('--step',type=int,default=1)
    args=ap.parse_args()
    flags=sieve(args.maxP*args.maxP)
    ps=primes_upto(args.maxP)[::args.step]
    for P in ps:
        if P<47: continue
        worst_R=-1
        for a in range(1,P+1):
            r0=first_prime_r(P,a,flags)
            if r0 is not None and r0>worst_R: worst_R=r0
        one,zero,inc,gain,mx,last=analyze_one(P,args.y,min(args.Rcap,worst_R+5))
        print(f"P={P},worst_R={worst_R},one_R={one},zero_R={zero},last_increase={inc},last_gain={gain},maxA={mx},lastA={last}")
if __name__=='__main__': main()
