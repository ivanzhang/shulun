#!/usr/bin/env python3
"""候选新增归因分析。

当 a 从 A_{R-1} 外进入 A_R，分析原因：
- Q 是否增长，引入新可用补丁素数；
- 旧窗口 [0,R-1) 中之前未补的洞，现在是否被新 Q 补上；
- 新高度 R-1 是否为洞且是否被补上。

用法示例：
    python3 experiments/candidate_gain_attribution.py --P 461 --y 13 --Rmax 40
"""
import argparse
from positive_negative_congruence import stats_for_a
from fixed_anchor_sieve_remainder import primes_upto


def patch_set_for(P, a, R, y, r):
    st = stats_for_a(P, a, R, y)
    # 复用 detail 不方便，这里直接试除可用 q。
    import math
    Q = int(math.isqrt(a + (R - 1) * P))
    n = a + r * P
    qs = [q for q in primes_upto(Q) if q > y and q != P and n % q == 0]
    return Q, qs


def is_hole(P, a, y, r):
    for p in primes_upto(y):
        if (a + r * P) % p == 0:
            return False
    return True


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--P',type=int,default=461)
    ap.add_argument('--y',type=int,default=13)
    ap.add_argument('--Rmax',type=int,default=40)
    args=ap.parse_args()
    prev=set()
    for R in range(1,args.Rmax+1):
        cur=set()
        stats={}
        for a in range(1,args.P+1):
            st=stats_for_a(args.P,a,R,args.y)
            stats[a]=st
            if st['holes']>0 and st['unpatched']==0:
                cur.add(a)
        gained=sorted(cur-prev)
        if gained:
            print(f"R={R}, gained={gained}")
            for a in gained:
                prev_st=stats_for_a(args.P,a,R-1,args.y) if R>1 else None
                cur_st=stats[a]
                q_prev = prev_st['Q'] if prev_st else None
                q_cur = cur_st['Q']
                fixed_old=[]
                if prev_st:
                    for r in prev_st['unpatched_list']:
                        Q,qs=patch_set_for(args.P,a,R,args.y,r)
                        if qs: fixed_old.append((r,qs))
                new_r=R-1
                new_is_hole=is_hole(args.P,a,args.y,new_r)
                _,new_qs=patch_set_for(args.P,a,R,args.y,new_r) if new_is_hole else (q_cur,[])
                print(f"  a={a}, Q:{q_prev}->{q_cur}, prev_unpatched={prev_st['unpatched_list'] if prev_st else []}, fixed_old={fixed_old}, new_r={new_r}, new_hole={new_is_hole}, new_qs={new_qs}, holes={cur_st['holes']}, hits={cur_st['patch_hits']}")
        prev=cur

if __name__=='__main__': main()
