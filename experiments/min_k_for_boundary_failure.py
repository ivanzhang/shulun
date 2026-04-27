#!/usr/bin/env python3
import argparse
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status
ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=500); ap.add_argument('--A',type=int,default=83); ap.add_argument('--H',type=int,default=600)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if x['a']>args.A]
max_prefix=0; worst=[]
for x in rows:
    prefix=0; hole_seen=0; first_fail=None
    for r in range(1,args.H+1):
        st,qs=status(args.P,x['a'],args.y,r)
        if st=='blocked': continue
        hole_seen+=1
        if st=='fail': first_fail=hole_seen; break
        prefix=hole_seen
    if first_fail is None: first_fail=10**9
    if prefix>max_prefix: max_prefix=prefix; worst=[(x,first_fail)]
    elif prefix==max_prefix: worst.append((x,first_fail))
print(f"rows={len(rows)},max_initial_patched_holes={max_prefix},K_needed={max_prefix+1}")
for x,ff in worst[:20]: print('worst',x['a'],x['R'],'first_fail_index',ff,'holes_first',x['holes'][:30],'unpatched_first',x['nonzero_unpatched'][:30])
