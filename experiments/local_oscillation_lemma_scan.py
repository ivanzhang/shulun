#!/usr/bin/env python3
"""扫描局部振荡引理的经验常数。

解释 C_k 为 sqrt(P)-小筛候选集合：行 k 中未被 q<=sqrt(P) 整除的位置。
统计所有连续无素数列段 J，若 J 含候选，则需要的 |J|/sqrt(P) 最大值。
"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def row_stats(P, row, flags, small):
    is_prime=[]; is_cand=[]
    for c in range(1,P+1):
        n=(row-1)*P+c
        is_prime.append(bool(flags[n]))
        is_cand.append(all(n%q for q in small))
    max_bad=0; examples=[]
    c=1
    while c<=P:
        if is_prime[c-1]:
            c+=1; continue
        start=c
        has_cand=False
        while c<=P and not is_prime[c-1]:
            if is_cand[c-1]: has_cand=True
            c+=1
        end=c-1
        if has_cand:
            L=end-start+1
            if L>max_bad:
                max_bad=L; examples=[(start,end,L)]
            elif L==max_bad:
                examples.append((start,end,L))
    return max_bad, examples[:3], sum(is_prime), sum(is_cand)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001,8009'); ap.add_argument('--top',type=int,default=5); args=ap.parse_args()
    print('P sqrt maxBadLen ratio row rowPrimes rowCandidates examples')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P*P+P); small=primes(sieve(math.isqrt(P)), math.isqrt(P))
        best=(0,None,None,None,None)
        low=[]
        for row in range(1,P+1):
            mb,ex,pc,cc=row_stats(P,row,flags,small)
            if mb>best[0]: best=(mb,row,ex,pc,cc)
            low.append((pc,row,mb,cc))
        mb,row,ex,pc,cc=best
        print(P, math.isqrt(P), mb, f'{mb/math.sqrt(P):.3f}', row, pc, cc, ex)
        print(' lowPrimeRows', sorted(low)[:args.top])

if __name__=='__main__': main()
