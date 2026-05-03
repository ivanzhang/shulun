#!/usr/bin/env python3
"""研究行内 sqrt(P)-粗合数的大因子互斥结构。"""
import argparse, math
from collections import Counter, defaultdict
from high_threshold_margin_fast import sieve, primes


def factor_distinct(n, plist):
    out=[]; x=n
    for q in plist:
        if q*q>x: break
        if x%q==0:
            out.append(q)
            while x%q==0: x//=q
        if x==1: break
    if x>1: out.append(x)
    return out


def analyze_row(P, row, plist, flags):
    # row: 1-based. entries n=(row-1)*P+c, c=1..P
    B=int(math.isqrt(P))
    rough=[]
    composites=[]
    for c in range(1,P+1):
        n=(row-1)*P+c
        if flags[n]:
            continue
        fac=factor_distinct(n, plist)
        if all(q>B for q in fac):
            rough.append((c,n,fac))
        composites.append((c,n,fac))
    # 检查距离 <B 是否共享 >B 因子
    violations=[]
    large_share_pairs=0
    for i in range(len(rough)):
        c1,n1,f1=rough[i]; s1={q for q in f1 if q>B}
        for j in range(i+1,len(rough)):
            c2,n2,f2=rough[j]
            inter=s1 & {q for q in f2 if q>B}
            if inter:
                large_share_pairs += 1
                if abs(c1-c2)<B:
                    violations.append((c1,c2,sorted(inter)))
    # block stats length B
    blocks=[]
    for start in range(1,P+1,B):
        end=min(P,start+B-1)
        pts=[x for x in rough if start<=x[0]<=end]
        large_factors=[]
        for c,n,fac in pts:
            large_factors.extend([q for q in fac if q>B])
        blocks.append((start,end,len(pts),len(set(large_factors)),len(large_factors)))
    return rough, violations, large_share_pairs, blocks


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--P',type=int,default=503)
    ap.add_argument('--rows',default='')
    ap.add_argument('--top',type=int,default=8)
    args=ap.parse_args()
    N=args.P*args.P+args.P
    flags=sieve(N)
    plist=primes(flags,N)
    P=args.P; B=int(math.isqrt(P))
    if args.rows:
        rows=[int(x) for x in args.rows.split(',') if x.strip()]
    else:
        # 选择素数最少的若干行
        rec=[]
        for r in range(1,P+1):
            pc=sum(1 for c in range(1,P+1) if flags[(r-1)*P+c])
            rec.append((pc,r))
        rows=[r for pc,r in sorted(rec)[:args.top]]
        print('low-prime rows', sorted(rec)[:args.top])
    print(f'P={P} sqrtFloor={B}')
    for r in rows:
        pc=sum(1 for c in range(1,P+1) if flags[(r-1)*P+c])
        rough,viol,share,blocks=analyze_row(P,r,plist,flags)
        max_block=max((b[2] for b in blocks), default=0)
        tight=[b for b in blocks if b[2]>=max_block-1][:5]
        print(f'row={r} primes={pc} roughComposite={len(rough)} sharePairsLarge={share} closeViolations={len(viol)} maxRoughInBlock={max_block}')
        print(' tightBlocks start-end rough distinctLarge totalLarge:', tight)
        if viol[:3]: print(' violations', viol[:3])

if __name__=='__main__': main()
