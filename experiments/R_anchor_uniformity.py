#!/usr/bin/env python3
"""可复用 R 的锚点二维小筛：anchorTotal -> anchorInA -> primeV 的均匀性。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def row_window_R_stats(P,row,start,L,small,flags):
    B=math.isqrt(P); N0=(row-1)*P; end=start+L-1
    u_primes=[q for q in primes(sieve(L),L) if q>B]
    total=inA=primeV=0
    for u in u_primes:
        r=(-N0)%u; first=start+((r-start)%u)
        for c in range(first,end+1,u):
            total+=1
            n=N0+c
            if all(n%q for q in small):
                inA+=1
                if flags[n//u]: primeV+=1
    return total,inA,primeV


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); step=max(1,L//4); flags=sieve(P*P+P); small=primes(sieve(B),B)
    totals=[]; inAs=[]; pVs=[]
    for row in range(1,P+1):
        for start in range(1,P-L+2,step):
            t,a,pv=row_window_R_stats(P,row,start,L,small,flags)
            totals.append(t); inAs.append(a); pVs.append(pv)
    pB=1.0
    for q in small: pB*=1-1/q
    print(f'P={P} C={args.C} L={L} windows={len(totals)} pB={pB:.5f}')
    print('meanTotal meanInA meanPrimeV inA/total primeV/inA expectedInA minMaxPrimeV')
    print(f'{mean(totals):.3f} {mean(inAs):.3f} {mean(pVs):.3f} {mean(inAs)/mean(totals):.4f} {mean(pVs)/mean(inAs):.4f} {mean(totals)*pB:.3f} {(min(pVs),max(pVs))}')

if __name__=='__main__': main()
