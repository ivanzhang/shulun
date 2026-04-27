#!/usr/bin/env python3
"""零洞修复型新增的边界素数扫描。

边界条件：Q(R-1)<a<=Q(R)，其中 Q(T)=floor(sqrt(a+(T-1)P))。
等价于 a 在 sqrt 边界跨入可用补丁库。扫描这些素数 a，判断：
- r=0 是否旧缺口、新修复；
- 非零洞是否全补；
- 若失败，最早失败洞是什么。

用法示例：
    python3 experiments/zero_repair_boundary_scan.py --P 461 --y 7 --Rmax 90 --detail
    python3 experiments/zero_repair_boundary_scan.py --P 1009 --y 7 --Rmax 100
"""
import argparse, math
from collections import Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto
from positive_negative_congruence import stats_for_a
from skeleton_patch_analysis import analyze as skeleton_analyze


def Q(P,a,R):
    return math.isqrt(a+(R-1)*P) if R>=1 else -1


def boundary_events(P,y,Rmax):
    prime_flags=sieve(P)
    rows=[]
    for R in range(1,Rmax+1):
        for a in range(1,P+1):
            if not prime_flags[a] or a<=y: continue
            if Q(P,a,R-1) < a <= Q(P,a,R):
                prev=stats_for_a(P,a,R-1,y) if R>1 else None
                cur=stats_for_a(P,a,R,y)
                sk=skeleton_analyze(P,a,R,y)
                nonzero_holes=[r for r in sk['holes'] if r!=0]
                nonzero_unpatched=[r for r in nonzero_holes if not sk['patch_by_hole'].get(r)]
                zero_old_unpatched = prev is not None and 0 in prev['unpatched_list']
                rows.append({
                    'R':R,'a':a,'Qprev':Q(P,a,R-1),'Q':Q(P,a,R),
                    'zero_old_unpatched':zero_old_unpatched,
                    'holes':sk['holes'],'hole_count':len(sk['holes']),
                    'nonzero_holes':nonzero_holes,'nonzero_unpatched':nonzero_unpatched,
                    'success_nonzero':len(nonzero_unpatched)==0,
                    'cur_full':cur['holes']>0 and cur['unpatched']==0,
                    'prev_full':prev is not None and prev['holes']>0 and prev['unpatched']==0,
                    'patch_hits':sk['patch_hits'],
                })
    return rows


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=90); ap.add_argument('--detail',action='store_true')
    args=ap.parse_args(); rows=boundary_events(args.P,args.y,args.Rmax)
    print(f"P={args.P},y={args.y},Rmax={args.Rmax},boundary_count={len(rows)}")
    print('success_nonzero=',sum(1 for x in rows if x['success_nonzero']),'cur_full=',sum(1 for x in rows if x['cur_full']),'zero_old=',sum(1 for x in rows if x['zero_old_unpatched']))
    print('hole_count_counter=',Counter(x['hole_count'] for x in rows).most_common())
    print('unpatched_nonzero_counter=',Counter(len(x['nonzero_unpatched']) for x in rows).most_common())
    selected=[x for x in rows if x['success_nonzero'] or x['cur_full'] or x['zero_old_unpatched']]
    for x in selected[:100]:
        print(f"R={x['R']},a={x['a']},Q={x['Qprev']}->{x['Q']},holes={x['holes']},nonzero_unpatched={x['nonzero_unpatched']},zero_old={x['zero_old_unpatched']},success_nonzero={x['success_nonzero']},cur_full={x['cur_full']},hits={x['patch_hits']}")
    if args.detail:
        print('all boundary rows:')
        for x in rows:
            print(x)

if __name__=='__main__': main()
