#!/usr/bin/env python3
"""候选淘汰证书。

对固定 P,y，找到每个曾经进入候选集合的 a 第一次被淘汰的高度 R，
并记录导致失败的未补洞列表。用于把候选收缩变成可证明的局部证书。

用法示例：
    python3 experiments/candidate_elimination_certificate.py --P 461 --y 13 --Rmax 90 --top 30
"""
import argparse
from collections import Counter
from a_space_candidate_decay import candidate_as
from positive_negative_congruence import stats_for_a


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--P',type=int,default=461)
    ap.add_argument('--y',type=int,default=13)
    ap.add_argument('--Rmax',type=int,default=90)
    ap.add_argument('--top',type=int,default=30)
    args=ap.parse_args()
    prev=set()
    ever=set()
    born={}
    death={}
    cert={}
    for R in range(1,args.Rmax+1):
        aset={a for a,*_ in candidate_as(args.P,R,args.y)}
        for a in aset-prev:
            born.setdefault(a,R)
        for a in prev-aset:
            if a not in death:
                st=stats_for_a(args.P,a,R,args.y)
                death[a]=R
                cert[a]=(st['unpatched'],st['unpatched_list'],st['holes'])
        ever |= aset
        prev=aset
    for a in prev:
        death.setdefault(a,None)
        cert.setdefault(a,None)
    rows=[]
    for a in sorted(ever):
        rows.append((death[a] if death[a] is not None else 10**9,born[a],a,cert[a]))
    rows.sort()
    dc=Counter(d for d,_,_,_ in rows if d!=10**9)
    print(f"P={args.P},y={args.y},Rmax={args.Rmax},ever={len(ever)},survivors={sum(1 for d,_,_,_ in rows if d==10**9)}")
    print('death_counter=', sorted(dc.items()))
    print('first deaths: death born a cert(unpatched, list, holes)')
    for d,b,a,c in rows[:args.top]:
        print(d,b,a,c)
    print('last deaths/survivors:')
    for d,b,a,c in rows[-args.top:]:
        print(d,b,a,c)

if __name__=='__main__': main()
