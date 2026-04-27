#!/usr/bin/env python3
"""边界素数前 K 洞补丁系统分析。"""
import argparse
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=120); ap.add_argument('--K',type=int,default=5)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if x['a']>83]
for x in rows:
    holes=[]; patched=[]; failed=[]
    r=1
    while len(holes)<args.K and r<=200:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked':
            holes.append(r)
            if st=='patched': patched.append((r,qs))
            else: failed.append(r)
        r+=1
    print(f"a={x['a']},R={x['R']},front={holes},patched={patched},failed={failed},all_front_patched={not failed}")
