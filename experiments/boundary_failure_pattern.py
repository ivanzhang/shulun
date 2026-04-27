#!/usr/bin/env python3
"""边界素数非零洞失败模式。"""
import argparse
from collections import Counter
from zero_repair_boundary_scan import boundary_events

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=120)
args=ap.parse_args(); rows=boundary_events(args.P,args.y,args.Rmax)
fail=[x for x in rows if not x['success_nonzero']]
succ=[x for x in rows if x['success_nonzero']]
print('success a=',[(x['a'],x['R'],x['holes']) for x in succ])
print('first_fail_hole_counter=',Counter(x['nonzero_unpatched'][0] for x in fail if x['nonzero_unpatched']).most_common())
print('all_fail_hole_counter=',Counter(r for x in fail for r in x['nonzero_unpatched']).most_common(30))
for x in fail[:40]:
    print(f"a={x['a']},R={x['R']},holes={x['holes']},fail={x['nonzero_unpatched'][:10]}")
