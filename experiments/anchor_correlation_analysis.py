#!/usr/bin/env python3
"""固定剩余类覆盖的锚点相关性分析。

真实锚点 b_q(a)=-aP^{-1} mod q 由同一个 a 决定。本脚本比较：
- 真实锚点覆盖；
- 随机独立锚点覆盖；
- 小模数骨架覆盖与大模数补洞。

用法示例：
  python3 experiments/anchor_correlation_analysis.py --P 461 --a 22 --trials 200 --detail
  python3 experiments/anchor_correlation_analysis.py --scan --maxP 1000 --trials 50
"""
import argparse
import math
import random
from collections import Counter


def sieve(n):
    arr=bytearray(b"\x01")*(n+1)
    if n>=0: arr[0]=0
    if n>=1: arr[1]=0
    for p in range(2, math.isqrt(n)+1):
        if arr[p]: arr[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return arr


def primes_upto(n):
    f=sieve(n)
    return [i for i in range(2,n+1) if f[i]]


def cover_from_anchors(P, anchors):
    covered=[0]*P
    for q,b in anchors.items():
        if b is None: continue
        for r in range(b,P,q): covered[r]+=1
    first=next((i for i,x in enumerate(covered) if x==0), None)
    return covered, first


def true_anchors(P,a,qs):
    out={}
    for q in qs:
        if q==P:
            out[q]=None if a%P else 0
        else:
            out[q]=(-a*pow(P,-1,q))%q
    return out


def random_anchors(P,qs,rng):
    return {q:(None if q==P else rng.randrange(q)) for q in qs}


def skeleton_stats(P, anchors, cut):
    small={q:b for q,b in anchors.items() if q<=cut}
    large={q:b for q,b in anchors.items() if q>cut and b is not None}
    covered, first=cover_from_anchors(P, small)
    holes=[i for i,x in enumerate(covered) if x==0]
    filled_by_large=0
    large_hit_counter=Counter()
    for h in holes:
        hits=[q for q,b in large.items() if h%q==b]
        if hits:
            filled_by_large+=1
            for q in hits: large_hit_counter[q]+=1
    return {
        'cut':cut,'small_first':first,'small_holes':len(holes),'filled_by_large':filled_by_large,
        'final_holes':len(holes)-filled_by_large,'large_used':len(large_hit_counter),
        'top_large':large_hit_counter.most_common(10),'holes_prefix':holes[:50],
    }


def record_for(P,a,trials,seed=1):
    qs=[q for q in primes_upto(P) if q!=P or a%P==0]
    anchors=true_anchors(P,a,qs)
    covered, first=cover_from_anchors(P,anchors)
    rng=random.Random(seed+P*1000003+a)
    random_first=[]
    for _ in range(trials):
        _, f=cover_from_anchors(P, random_anchors(P,qs,rng))
        random_first.append(P if f is None else f)
    cuts=[]
    for cut in [3,5,7,11,13,17,19,23,29,31,37,43,47,53,61,71,83,97,113,127,151,181,211,251,307,367,431]:
        if cut<P: cuts.append(skeleton_stats(P,anchors,cut))
    mult=Counter(covered)
    return {
        'P':P,'a':a,'first':first,'uncovered':sum(1 for x in covered if x==0),
        'overlap':sum(covered)-sum(1 for x in covered if x),'multiplicity':mult,
        'random_min':min(random_first) if random_first else None,
        'random_median':sorted(random_first)[len(random_first)//2] if random_first else None,
        'random_max':max(random_first) if random_first else None,
        'random_mean':sum(random_first)/len(random_first) if random_first else None,
        'cuts':cuts,'anchors':anchors,'covered':covered,
    }


def print_record(rec,detail=False):
    print(f"P={rec['P']},a={rec['a']},true_first={rec['first']},uncovered={rec['uncovered']},overlap={rec['overlap']},random_min={rec['random_min']},random_median={rec['random_median']},random_mean={rec['random_mean']:.2f},random_max={rec['random_max']}")
    print(f"multiplicity={sorted(rec['multiplicity'].items())}")
    best=min(rec['cuts'], key=lambda x:x['final_holes']) if rec['cuts'] else None
    if best: print(f"best_cut={best}")
    if detail:
        print('cut,small_first,small_holes,filled_by_large,final_holes,large_used,top_large')
        for row in rec['cuts']:
            print(row)
        print('anchors_top=', sorted(list(rec['anchors'].items()))[:80])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scan',action='store_true')
    ap.add_argument('--P',type=int,default=461); ap.add_argument('--a',type=int,default=22)
    ap.add_argument('--maxP',type=int,default=1000); ap.add_argument('--trials',type=int,default=100)
    ap.add_argument('--detail',action='store_true')
    args=ap.parse_args()
    if args.scan:
        rows=[]
        for P in primes_upto(args.maxP):
            # 只取每个 P 的最坏 a，降低成本。
            flags=sieve(P*P)
            worst_a=1; worst_r=-1
            for a in range(1,P+1):
                first=next((r for r in range(P) if flags[a+r*P]), None)
                if first is not None and first>worst_r:
                    worst_r=first; worst_a=a
            rows.append(record_for(P,worst_a,args.trials))
        rows.sort(key=lambda x:-(x['first'] or -1))
        for rec in rows[:20]: print_record(rec,False)
    else:
        print_record(record_for(args.P,args.a,args.trials),args.detail)

if __name__=='__main__': main()
