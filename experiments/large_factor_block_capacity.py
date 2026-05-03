#!/usr/bin/env python3
"""基于大因子互斥的短块容量统计。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def block_stats(P,row,flags,plist,B):
    out=[]
    for start in range(1,P+1,B):
        end=min(P,start+B-1)
        prime=small_comp=rough=0; large_factors=[]; entries=[]
        for c in range(start,end+1):
            n=(row-1)*P+c
            if flags[n]: prime+=1; continue
            fac=factor_distinct(n,plist)
            if any(q<=B for q in fac): small_comp+=1
            else:
                rough+=1; large_factors += [q for q in fac if q>B]; entries.append((c,n,fac))
        out.append((start,end,prime,small_comp,rough,len(set(large_factors)),len(large_factors),entries))
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--top',type=int,default=8); ap.add_argument('--Bmul',type=float,default=1.0); args=ap.parse_args()
    P=args.P; N=P*P+P; flags=sieve(N); plist=primes(flags,N); B=max(2,int(args.Bmul*math.isqrt(P)))
    rec=[]
    for r in range(1,P+1):
        pc=sum(1 for c in range(1,P+1) if flags[(r-1)*P+c])
        rec.append((pc,r))
    rows=[r for _,r in sorted(rec)[:args.top]]
    print(f'P={P} B={B} lowRows={sorted(rec)[:args.top]}')
    for r in rows:
        blocks=block_stats(P,r,flags,plist,B)
        # pressure: rough positions require at least rough distinct >B factors in block; actually semiprimes give 2 each.
        worst=sorted(blocks,key=lambda x:(x[4],x[2]),reverse=True)[:5]
        print('row',r,'rowPrimes',sum(1 for c in range(1,P+1) if flags[(r-1)*P+c]))
        for st,en,pr,sm,ro,dl,tl,entries in worst:
            print(f' block {st}-{en} prime={pr} smallComp={sm} rough={ro} distinctLarge={dl} totalLarge={tl}')
            print('  roughSample', [(c,fac[:3]) for c,n,fac in entries[:4]])

if __name__=='__main__': main()
