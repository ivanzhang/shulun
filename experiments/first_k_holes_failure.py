#!/usr/bin/env python3
"""检验边界素数前 K 个非零小骨架洞是否必有失败。"""
import argparse
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=150); ap.add_argument('--H',type=int,default=120)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if x['a']>83]
max_prefix_all_patched=0; worst=[]
for x in rows:
    prefix=0; first_fail=None; hole_seen=0
    for r in range(1,args.H+1):
        st,qs=status(args.P,x['a'],args.y,r)
        if st=='blocked': continue
        hole_seen+=1
        if st=='fail': first_fail=hole_seen; break
        prefix=hole_seen
    if first_fail is None: first_fail=10**9
    if prefix>max_prefix_all_patched:
        max_prefix_all_patched=prefix; worst=[(x,first_fail)]
    elif prefix==max_prefix_all_patched:
        worst.append((x,first_fail))
print(f"P={args.P},rows={len(rows)},max_initial_patched_holes={max_prefix_all_patched},so K={max_prefix_all_patched+1} suffices")
for x,ff in worst[:20]: print('worst',x['a'],x['R'],'holes',x['holes'][:20],'nonzero_unpatched',x['nonzero_unpatched'][:20],'first_fail_hole_index',ff)
