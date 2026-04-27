#!/usr/bin/env python3
"""固定小高度集合 H 的失败规则扫描。

对边界素数 a，检查小高度 H 中每个 r 的状态：
- blocked: 被小骨架覆盖，不是洞；
- patched: 是洞且有 y<q<=a 的补丁；
- fail: 是洞但无 y<q<=a 的补丁。
寻找是否存在简单规则：例如前 N 个洞中必有失败洞。

用法示例：
    python3 experiments/small_height_failure_rule.py --P 461 --y 7 --Rmax 120 --H 40
"""
import argparse, math
from collections import Counter, defaultdict

from fixed_anchor_sieve_remainder import sieve, primes_upto
from zero_repair_boundary_scan import boundary_events


def status(P,a,y,r):
    n=a+r*P
    for p in primes_upto(y):
        if n%p==0:
            return ('blocked', [])
    qs=[q for q in primes_upto(a) if q>y and n%q==0]
    return ('patched' if qs else 'fail', qs)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=120); ap.add_argument('--H',type=int,default=40); ap.add_argument('--only-fail-boundary',action='store_true')
    args=ap.parse_args(); rows=boundary_events(args.P,args.y,args.Rmax)
    # 只看边界 a 较大且非零未补失败/或全部
    selected=[x for x in rows if x['a']>83]
    if args.only_fail_boundary:
        selected=[x for x in selected if not x['success_nonzero']]
    print(f"P={args.P},y={args.y},selected={len(selected)},H={args.H}")
    first_fail=Counter(); first_hole=Counter(); pattern=defaultdict(Counter)
    for x in selected:
        a=x['a']; states=[]; first_fail_r=None; first_hole_r=None
        for r in range(1,args.H+1):
            st,qs=status(args.P,a,args.y,r)
            states.append((r,st,qs))
            if st!='blocked' and first_hole_r is None: first_hole_r=r
            if st=='fail' and first_fail_r is None: first_fail_r=r
        first_fail[first_fail_r]+=1; first_hole[first_hole_r]+=1
        for r,st,qs in states: pattern[r][st]+=1
        print(f"a={a},R={x['R']},first_hole={first_hole_r},first_fail={first_fail_r},boundary_fail={not x['success_nonzero']},unpatched={x['nonzero_unpatched'][:8]}")
        print('  states=', [(r,st,qs[:3]) for r,st,qs in states if st!='blocked'][:12])
    print('first_hole=',first_hole.most_common())
    print('first_fail=',first_fail.most_common())
    print('per_r fail/patched/hole rates:')
    for r in range(1,args.H+1):
        c=pattern[r]
        holes=c['patched']+c['fail']
        if holes:
            print(r, 'holes',holes,'fail',c['fail'],'patched',c['patched'],'blocked',c['blocked'])

if __name__=='__main__': main()
