#!/usr/bin/env python3
"""统计局部窗口内 S2 半素数对的结构：共享因子、可复用/单命中。"""
import argparse, math
from collections import Counter
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def row_semis(P,row,flags,plist,small,B):
    semis=[]
    for c in range(1,P+1):
        n=(row-1)*P+c
        if all(n%q for q in small) and not flags[n]:
            fac=factor_distinct(n,plist)
            if all(q>B for q in fac) and len(fac)==2:
                u=min(fac); v=max(fac); semis.append((c,u,v))
    return semis


def classify_window(items,L):
    cnt=Counter(); n=len(items)
    for i in range(n):
        c1,u1,v1=items[i]
        type1='R' if u1<=L else 'S'
        for j in range(i+1,n):
            c2,u2,v2=items[j]
            type2='R' if u2<=L else 'S'
            shared=bool({u1,v1}&{u2,v2})
            key=''.join(sorted(type1+type2)) + ('_shared' if shared else '_disjoint')
            cnt[key]+=1
    return cnt


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--sample-step',type=int,default=0); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B); step=args.sample_step or max(1,L//4)
    total=Counter(); win_count=0; s_counts=[]; pair_counts=[]
    maxwin=None
    for row in range(1,P+1):
        semis=row_semis(P,row,flags,plist,small,B)
        # two pointer for windows sampled by start
        for start in range(1,P-L+2,step):
            end=start+L-1
            items=[x for x in semis if start<=x[0]<=end]
            cnt=classify_window(items,L)
            total.update(cnt); win_count+=1; s_counts.append(len(items)); pair_counts.append(len(items)*(len(items)-1)//2)
            if maxwin is None or len(items)>maxwin[0]: maxwin=(len(items),row,start,end,cnt,items[:12])
    print(f'P={P} C={args.C} L={L} windows={win_count} meanS={sum(s_counts)/win_count:.3f} meanPairs={sum(pair_counts)/win_count:.3f}')
    print('pair structure totals', dict(total))
    denom=sum(total.values()) or 1
    print('fractions', {k:round(v/denom,4) for k,v in sorted(total.items())})
    print('maxwin', maxwin)

if __name__=='__main__': main()
