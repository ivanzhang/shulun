#!/usr/bin/env python3
"""固定剩余类 a mod P 的一维斜线覆盖分析。

S_a={a+rP:0<=r<P}。根基素数 q<=P 覆盖满足 a+rP≡0 mod q 的 r。
未覆盖点即素数候选；若 N>1 且未被任何 q<=P 整除，则 N<=P^2 时为素数。

用法示例：
  python3 experiments/fixed_residue_cover.py --P 461 --a 22 --detail
  python3 experiments/fixed_residue_cover.py --scan --maxP 1000
"""
import argparse
import math
from collections import Counter, defaultdict


def sieve(n):
    arr=bytearray(b"\x01")*(n+1)
    if n>=0: arr[0]=0
    if n>=1: arr[1]=0
    for p in range(2, math.isqrt(n)+1):
        if arr[p]:
            arr[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return arr


def primes_upto(n):
    flags=sieve(n)
    return [i for i in range(2,n+1) if flags[i]]


def record_for(P,a):
    root=primes_upto(P)
    flags=sieve(P*P)
    covered=[[] for _ in range(P)]
    q_hits={}
    for q in root:
        if q==P:
            if a%P==0:
                ns=list(range(P))
            else:
                ns=[]
        else:
            inv=pow(P,-1,q)
            residue=(-a*inv)%q
            ns=list(range(residue,P,q))
        q_hits[q]=ns
        for r in ns:
            covered[r].append(q)
    uncovered=[r for r in range(P) if not covered[r]]
    primes=[r for r in range(P) if flags[a+r*P]]
    first_uncovered=uncovered[0] if uncovered else None
    first_prime=primes[0] if primes else None
    cover_count=sum(1 for r in range(P) if covered[r])
    total_hits=sum(len(v) for v in q_hits.values())
    multiplicities=Counter(len(covered[r]) for r in range(P))
    top_q=Counter({q:len(ns) for q,ns in q_hits.items() if ns}).most_common(20)
    return {
        'P':P,'a':a,'first_uncovered':first_uncovered,'first_prime':first_prime,
        'uncovered_count':len(uncovered),'prime_count':len(primes),'cover_count':cover_count,
        'total_hits':total_hits,'overlap':total_hits-cover_count,
        'multiplicities':multiplicities,'top_q':top_q,'uncovered':uncovered,'primes':primes,
        'covered':covered,'q_hits':q_hits,
    }


def print_record(rec,detail=False):
    print(f"P={rec['P']},a={rec['a']},first_uncovered={rec['first_uncovered']},first_prime={rec['first_prime']},uncovered_count={rec['uncovered_count']},prime_count={rec['prime_count']},cover_count={rec['cover_count']},total_hits={rec['total_hits']},overlap={rec['overlap']}")
    print(f"multiplicities={sorted(rec['multiplicities'].items())}")
    print(f"top_q={rec['top_q']}")
    if detail:
        print(f"uncovered={rec['uncovered'][:200]}")
        print(f"primes={rec['primes'][:200]}")
        print("r,N,covered_by,is_prime")
        flags=sieve(rec['P']*rec['P'])
        for r in range(rec['P']):
            N=rec['a']+r*rec['P']
            print(f"{r},{N},{rec['covered'][r]},{bool(flags[N])}")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scan',action='store_true')
    parser.add_argument('--P',type=int,default=461)
    parser.add_argument('--a',type=int,default=22)
    parser.add_argument('--maxP',type=int,default=1000)
    parser.add_argument('--detail',action='store_true')
    args=parser.parse_args()
    if args.scan:
        rows=[]
        for P in primes_upto(args.maxP):
            for a in range(1,P+1):
                rows.append(record_for(P,a))
        rows.sort(key=lambda x:(-(x['first_uncovered'] if x['first_uncovered'] is not None else 10**9), x['uncovered_count'], -x['P']))
        for rec in rows[:30]: print_record(rec,False)
        print('checked',len(rows),'missing_uncovered',sum(1 for r in rows if r['first_uncovered'] is None),'max_first_uncovered',rows[0]['first_uncovered'])
    else:
        print_record(record_for(args.P,args.a), args.detail)

if __name__=='__main__': main()
