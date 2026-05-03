#!/usr/bin/env python3
"""按 shared/disjoint 和 R/S 类型统计窗口内 S2 pair 二阶贡献。"""
import argparse, math
from collections import Counter, defaultdict
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def row_semis(P,row,flags,plist,small,B):
    out=[]
    for c in range(1,P+1):
        n=(row-1)*P+c
        if all(n%q for q in small) and not flags[n]:
            fac=factor_distinct(n,plist)
            if all(q>B for q in fac) and len(fac)==2:
                out.append((c,min(fac),max(fac)))
    return out


def classify_pair(a,b,L):
    c1,u1,v1=a; c2,u2,v2=b
    t1='R' if u1<=L else 'S'; t2='R' if u2<=L else 'S'
    base=''.join(sorted(t1+t2))
    shared=bool({u1,v1}&{u2,v2})
    return base + ('_shared' if shared else '_disjoint')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); step=max(1,L//4)
    flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
    Svals=[]; class_counts=defaultdict(list)
    for row in range(1,P+1):
        semis=row_semis(P,row,flags,plist,small,B)
        for start in range(1,P-L+2,step):
            end=start+L-1
            items=[x for x in semis if start<=x[0]<=end]
            S=len(items); Svals.append(S)
            cnt=Counter()
            for i in range(len(items)):
                for j in range(i+1,len(items)):
                    cnt[classify_pair(items[i],items[j],L)] += 1
            for key in ['RR_shared','RR_disjoint','RS_disjoint','SS_disjoint','RS_shared','SS_shared']:
                class_counts[key].append(cnt.get(key,0))
    mu=mean(Svals); var=mean((s-mu)**2 for s in Svals); ES2=mean(s*s for s in Svals)
    print(f'P={P} C={args.C} L={L} windows={len(Svals)} meanS={mu:.6f} varS={var:.6f} ES2={ES2:.6f} meanPairs={(ES2-mu)/2:.6f}')
    total_pair_mean=sum(mean(v) for v in class_counts.values())
    for key,vals in sorted(class_counts.items()):
        m=mean(vals); cov=mean((x-m)*(s-mu) for x,s in zip(vals,Svals))
        print(key,'meanPairs',f'{m:.6f}','frac',f'{m/total_pair_mean if total_pair_mean else 0:.4f}','covWithS',f'{cov:.6f}')

if __name__=='__main__': main()
