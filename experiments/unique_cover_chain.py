#!/usr/bin/env python3
"""唯一覆盖链分析。

对首素数前缀 [0,R) 中恰被一个自洽小因子 q 覆盖的点进行分组，分析：
- 唯一覆盖点数量；
- 每个 q 支撑哪些唯一点；
- 唯一点间距与 q 周期是否刚性；
- 唯一覆盖点是否形成长连续链。
"""
import argparse, math
from collections import Counter, defaultdict


def sieve(n):
    arr=bytearray(b"\x01")*(n+1); arr[0:2]=b"\x00\x00"
    for p in range(2, math.isqrt(n)+1):
        if arr[p]: arr[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return arr

def primes_upto(n):
    f=sieve(n); return [i for i in range(2,n+1) if f[i]]

def first_prime_r(P,a,flags): return next((r for r in range(P) if flags[a+r*P]), None)

def cover_prefix(P,a,R):
    Q=math.isqrt(a+max(0,R-1)*P)
    qs=[q for q in primes_upto(min(P,Q)) if q!=P]
    cover=[[] for _ in range(R)]
    for q in qs:
        b=(-a*pow(P,-1,q))%q
        for r in range(b,R,q): cover[r].append(q)
    return cover,qs,Q

def runs_of_positions(pos):
    runs=[]; cur=[]; prev=None
    for x in pos:
        if prev is None or x==prev+1: cur.append(x)
        else: runs.append(cur); cur=[x]
        prev=x
    if cur: runs.append(cur)
    return runs

def record_for(P,a):
    flags=sieve(P*P)
    R=first_prime_r(P,a,flags)
    if R is None: R=P
    cover,qs,Q=cover_prefix(P,a,R)
    unique=[]; byq=defaultdict(list)
    for r,xs in enumerate(cover):
        if a+r*P==1: continue
        if len(xs)==1:
            q=xs[0]; unique.append((r,q)); byq[q].append(r)
    unique_positions=[r for r,_ in unique]
    runs=runs_of_positions(unique_positions)
    q_rows=[]
    for q,rs in byq.items():
        rs=sorted(rs)
        gaps=[b-a for a,b in zip(rs,rs[1:])]
        q_rows.append({'q':q,'count':len(rs),'rs':rs,'gaps':gaps,'period_ok':all(g%q==0 for g in gaps)})
    q_rows.sort(key=lambda x:(-x['count'],x['q']))
    # 唯一支撑 q 的锚点必须正好是这些点的同余类；同一 q 多点间距必为 q 的倍数，这是 sanity check。
    return {'P':P,'a':a,'R':R,'Q':Q,'q_count':len(qs),'unique_count':len(unique),'unique_ratio':len(unique)/max(1,R),
            'max_unique_run':max((len(run) for run in runs),default=0),'run_count':len(runs),
            'q_support_count':len(byq),'max_q_support':max((len(v) for v in byq.values()),default=0),
            'period_bad':sum(1 for row in q_rows if not row['period_ok']),
            'q_rows':q_rows,'runs':runs,'cover':cover}

def print_record(rec,detail=False):
    print(f"P={rec['P']},a={rec['a']},R={rec['R']},Q={rec['Q']},q_count={rec['q_count']},unique_count={rec['unique_count']},unique_ratio={rec['unique_ratio']:.3f},max_unique_run={rec['max_unique_run']},run_count={rec['run_count']},q_support_count={rec['q_support_count']},max_q_support={rec['max_q_support']},period_bad={rec['period_bad']}")
    print('top_q_support=',[(r['q'],r['count'],r['rs'][:10]) for r in rec['q_rows'][:20]])
    if detail:
        print('unique_runs=',rec['runs'][:50])
        print('q_rows=q,count,rs,gaps')
        for row in rec['q_rows']:
            print(row['q'],row['count'],row['rs'],row['gaps'])
        print('r,cover')
        for r,xs in enumerate(rec['cover']): print(r,xs)

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
        rows.sort(key=lambda x:(-x['unique_count'],-x['R']))
        for rec in rows[:30]: print_record(rec)
    else: print_record(record_for(args.P,args.a),args.detail)
if __name__=='__main__': main()
