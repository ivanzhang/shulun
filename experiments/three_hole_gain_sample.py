#!/usr/bin/env python3
"""三洞新增抽样扫描。"""
import argparse
from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from three_hole_gain_analysis import events_for, print_event

ap=argparse.ArgumentParser(); ap.add_argument('--maxP',type=int,default=700); ap.add_argument('--step',type=int,default=7); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=80)
args=ap.parse_args(); flags=sieve(args.maxP*args.maxP); all_events=[]
for P in primes_upto(args.maxP)[::args.step]:
    if P<=args.y: continue
    worst_R=-1
    for a in range(1,P+1):
        r0=first_prime_r(P,a,flags)
        if r0 is not None and r0>worst_R: worst_R=r0
    evs=events_for(P,args.y,min(args.Rmax,worst_R+5)); all_events.extend(evs)
    if evs:
        print('--- P',P,'worst_R',worst_R,'events',len(evs))
        for ev in evs: print_event(ev,False)
print('total',len(all_events))
