#!/usr/bin/env python3
"""动态自洽覆盖增长分析 C_a(R)。

C_a(R)=q<=sqrt(a+(R-1)P) 的锚点在 [0,R) 中覆盖的点数。
分析 R 增长时：
- Q(R) 何时引入新素数；
- 新高度 R-1 是否被旧模数覆盖；
- 满覆盖前缀如何维持。

用法示例：
  python3 experiments/dynamic_cover_growth.py --P 461 --a 22 --detail
  python3 experiments/dynamic_cover_growth.py --scan --maxP 1000
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

def anchors(P,a,qs):
    return {q:(-a*pow(P,-1,q))%q for q in qs if q!=P}

def covered_prefix(P,a,R,prime_list):
    if R<=0: return [],[]
    Q=math.isqrt(a+(R-1)*P)
    qs=[q for q in prime_list if q<=min(P,Q) and q!=P]
    anc=anchors(P,a,qs)
    cover=[[] for _ in range(R)]
    for q,b in anc.items():
        for r in range(b,R,q): cover[r].append(q)
    holes=[r for r,x in enumerate(cover) if not x and a+r*P>1]
    return cover,holes

def first_prime_r(P,a,flags):
    return next((r for r in range(P) if flags[a+r*P]), None)

def record_for(P,a):
    flags=sieve(P*P)
    prime_list=primes_upto(P)
    first=first_prime_r(P,a,flags)
    rows=[]
    prev_Q=0; prev_qset=set(); first_failure=None
    for R in range(1,P+1):
        Q=math.isqrt(a+(R-1)*P)
        qset={q for q in prime_list if q<=min(P,Q) and q!=P}
        new_q=sorted(qset-prev_qset)
        cover,holes=covered_prefix(P,a,R,prime_list)
        full=(len(holes)==0)
        if not full and first_failure is None: first_failure=R
        new_height=R-1
        new_height_cover=cover[-1] if cover else []
        rows.append({
            'R':R,'Q':Q,'q_count':len(qset),'new_q':new_q,'new_q_count':len(new_q),
            'covered':R-len(holes),'holes':len(holes),'full':full,
            'new_height':new_height,'new_height_cover':new_height_cover,'new_height_degree':len(new_height_cover),
        })
        prev_Q=Q; prev_qset=qset
    # 满覆盖维持区间直到首素数高度 first：R=first 表示 [0,first) 满覆盖。
    sustain_rows=[row for row in rows if first is not None and row['R']<=first]
    degree_counter=Counter(row['new_height_degree'] for row in sustain_rows)
    new_q_total=sum(row['new_q_count'] for row in sustain_rows)
    zero_new_q_steps=sum(1 for row in sustain_rows if row['new_q_count']==0)
    return {'P':P,'a':a,'first':first,'first_failure':first_failure,'rows':rows,
            'sustain_len':len(sustain_rows),'degree_counter':degree_counter,
            'new_q_total':new_q_total,'zero_new_q_steps':zero_new_q_steps}

def print_record(rec,detail=False):
    print(f"P={rec['P']},a={rec['a']},first={rec['first']},first_failure={rec['first_failure']},sustain_len={rec['sustain_len']},new_q_total={rec['new_q_total']},zero_new_q_steps={rec['zero_new_q_steps']},degree_counter={sorted(rec['degree_counter'].items())}")
    if detail:
        print('R,Q,q_count,new_q,holes,full,new_height_degree,new_height_cover')
        for row in rec['rows'][:max(120,(rec['first'] or 0)+5)]:
            print(row['R'],row['Q'],row['q_count'],row['new_q'],row['holes'],row['full'],row['new_height_degree'],row['new_height_cover'])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--scan',action='store_true')
    ap.add_argument('--P',type=int,default=461); ap.add_argument('--a',type=int,default=22); ap.add_argument('--maxP',type=int,default=1000); ap.add_argument('--detail',action='store_true')
    args=ap.parse_args()
    if args.scan:
        flags=sieve(args.maxP*args.maxP); rows=[]
        plist=primes_upto(args.maxP)
        for P in plist:
            worst_a=1; worst_R=-1
            for a in range(1,P+1):
                R=first_prime_r(P,a,flags)
                if R is not None and R>worst_R: worst_R=R; worst_a=a
            rows.append(record_for(P,worst_a))
        rows.sort(key=lambda x:-(x['first'] or -1))
        for rec in rows[:30]: print_record(rec)
    else: print_record(record_for(args.P,args.a),args.detail)
if __name__=='__main__': main()
