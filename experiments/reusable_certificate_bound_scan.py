#!/usr/bin/env python3
"""扫描坏段中可复用证书 R_{<=L}，并与 u 层容量比较。"""
import argparse, math
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from bad_segment_factor_shell import find_bad_segments


def analyze(P,row,start,end,cands,flags,plist,small,B):
    L=end-start+1
    A=[]
    for c in cands:
        n=(row-1)*P+c
        if all(n%q for q in small): A.append(c)
    reusable=[]; allsemi=[]
    for c in A:
        n=(row-1)*P+c
        if flags[n]: continue
        fac=factor_distinct(n,plist)
        if all(q>B for q in fac) and len(fac)==2:
            u=min(fac); v=max(fac); allsemi.append((c,u,v))
            if u<=L: reusable.append((c,u,v))
    # 容量：素数 u in (B,L] 在段内的锚点数；以及锚点落入 A 的个数；以及余因子素数的个数
    u_primes=[q for q in primes(sieve(L),L) if q>B]
    anchor_total=0; anchor_in_A=0; anchor_prime_v=0
    Aset=set(A); N0=(row-1)*P
    for u in u_primes:
        # c ≡ -N0 mod u, c in [start,end]
        r=(-N0)%u
        # 列 c 从1开始；找 >=start 的同余 r mod u，注意 r=0 表示 u
        # n=N0+c, u|n iff c≡-N0 mod u
        first=start + ((r-start)%u)
        for c in range(first,end+1,u):
            anchor_total+=1
            if c in Aset:
                anchor_in_A+=1
                v=(N0+c)//u
                if flags[v]: anchor_prime_v+=1
    return len(A),len(allsemi),len(reusable),anchor_total,anchor_in_A,anchor_prime_v,reusable[:6]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001'); ap.add_argument('--Cmin',type=float,default=2.5); ap.add_argument('--top',type=int,default=12); args=ap.parse_args()
    print('P row start end L ratio A semi reusable reusable/A anchorTotal anchorInA anchorPrimeV sample')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        rec=[]
        for row in range(1,P+1):
            for L,start,end,cands in find_bad_segments(P,row,flags,small):
                if L/math.sqrt(P) < args.Cmin: continue
                A,semi,reuse,at,ai,apv,samp=analyze(P,row,start,end,cands,flags,plist,small,B)
                if A: rec.append((reuse/A,L/math.sqrt(P),P,row,start,end,L,A,semi,reuse,at,ai,apv,samp))
        for _,ratio,P,row,start,end,L,A,semi,reuse,at,ai,apv,samp in sorted(rec, reverse=True)[:args.top]:
            print(P,row,start,end,L,f'{ratio:.3f}',A,semi,reuse,f'{reuse/A:.3f}',at,ai,apv,samp)

if __name__=='__main__': main()
