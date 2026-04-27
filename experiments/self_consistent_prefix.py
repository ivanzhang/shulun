#!/usr/bin/env python3
"""首空隙前缀的自洽小因子覆盖分析。

若 r<R 全合数，则每个 N=a+rP 有素因子 <=sqrt(a+(R-1)P)。
所以前缀 [0,R) 必须已经被 q<=sqrt(a+RP) 的锚点覆盖；更大的 q 不可能是这些前缀点的最小必要因子。
"""
import argparse, math
from collections import Counter


def sieve(n):
    arr=bytearray(b"\x01")*(n+1)
    arr[0:2]=b"\x00\x00"
    for p in range(2, math.isqrt(n)+1):
        if arr[p]: arr[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return arr

def primes_upto(n):
    f=sieve(n); return [i for i in range(2,n+1) if f[i]]

def first_prime_r(P,a,flags):
    return next((r for r in range(P) if flags[a+r*P]), None)

def cover_prefix(P,a,R,qs):
    covered=[[] for _ in range(R)]
    for q in qs:
        if q==P: continue
        b=(-a*pow(P,-1,q))%q
        for r in range(b,R,q): covered[r].append(q)
    holes=[i for i,x in enumerate(covered) if not x and a+i*P > 1]
    return covered,holes

def record_for(P,a):
    flags=sieve(P*P)
    R=first_prime_r(P,a,flags)
    if R is None: R=P
    Q=math.isqrt(a+max(0,R-1)*P)
    qs=primes_upto(min(P,Q))
    covered,holes=cover_prefix(P,a,R,qs)
    mult=Counter(len(x) for x in covered)
    used=Counter(q for xs in covered for q in xs)
    return {'P':P,'a':a,'R':R,'Q':Q,'q_count':len(qs),'holes':holes,'hole_count':len(holes),'mult':mult,'used':used,'covered':covered}

def print_record(rec,detail=False):
    print(f"P={rec['P']},a={rec['a']},R={rec['R']},Q={rec['Q']},q_count={rec['q_count']},hole_count={rec['hole_count']},mult={sorted(rec['mult'].items())}")
    print(f"top_used={rec['used'].most_common(20)}")
    if detail:
        print(f"holes={rec['holes']}")
        print('r,covered')
        for r,xs in enumerate(rec['covered']): print(r,xs)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--scan',action='store_true')
    ap.add_argument('--P',type=int,default=461); ap.add_argument('--a',type=int,default=22); ap.add_argument('--maxP',type=int,default=1000); ap.add_argument('--detail',action='store_true')
    args=ap.parse_args()
    if args.scan:
        flags=sieve(args.maxP*args.maxP); rows=[]
        for P in primes_upto(args.maxP):
            worst_a=1; worst_R=-1
            for a in range(1,P+1):
                R=first_prime_r(P,a,flags)
                if R is not None and R>worst_R: worst_R=R; worst_a=a
            rows.append(record_for(P,worst_a))
        rows.sort(key=lambda x:(-x['R'], x['hole_count']))
        for rec in rows[:30]: print_record(rec)
        print('checked',len(rows),'max_R',max(r['R'] for r in rows),'bad_prefix_holes',sum(1 for r in rows if r['hole_count']))
    else: print_record(record_for(args.P,args.a),args.detail)
if __name__=='__main__': main()
