#!/usr/bin/env python3
"""统计长度 sqrt(P) 短块中 q<=sqrt(P) 小筛幸存洞与粗合数。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def block_data(P,row,flags,plist,B,small):
    rows=[]
    for start in range(1,P+1,B):
        end=min(P,start+B-1)
        prime=0; small_comp=0; rough=0; small_survivors=0; survivor_prime=0; survivor_rough=0
        for c in range(start,end+1):
            n=(row-1)*P+c
            small_hit=any(n%q==0 for q in small)
            if not small_hit:
                small_survivors+=1
            if flags[n]:
                prime+=1
                if not small_hit: survivor_prime+=1
            else:
                fac=factor_distinct(n,plist)
                if any(q<=B for q in fac): small_comp+=1
                else:
                    rough+=1
                    if not small_hit: survivor_rough+=1
        rows.append((start,end,end-start+1,prime,small_comp,rough,small_survivors,survivor_prime,survivor_rough))
    return rows


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--top',type=int,default=6); ap.add_argument('--Bmul',type=float,default=1.0); args=ap.parse_args()
    P=args.P; N=P*P+P; flags=sieve(N); plist=primes(flags,N); B=max(2,int(args.Bmul*math.isqrt(P))); small=[q for q in primes(sieve(B),B) if q<P]
    low=[]
    for r in range(1,P+1):
        pc=sum(1 for c in range(1,P+1) if flags[(r-1)*P+c])
        low.append((pc,r))
    rows=[r for _,r in sorted(low)[:args.top]]
    print(f'P={P} B={B} smallPrimes<=B={len(small)} lowRows={sorted(low)[:args.top]}')
    print('row minSurv avgSurv maxSurv zeroPrimeBlocks maxRough maxSurvRough sampleWorst')
    for r in rows:
        data=block_data(P,r,flags,plist,B,small)
        surv=[x[6] for x in data]; zpb=sum(1 for x in data if x[3]==0); maxrough=max(x[5] for x in data); maxsr=max(x[8] for x in data)
        worst=sorted(data,key=lambda x:(x[6],-x[3]))[:5]
        print(r, min(surv), f'{sum(surv)/len(surv):.2f}', max(surv), zpb, maxrough, maxsr, [(w[0],w[1],w[3],w[6],w[8]) for w in worst])

if __name__=='__main__': main()
