#!/usr/bin/env python3
"""新增候选的洞数剖面。"""
import argparse
from collections import Counter
from a_space_candidate_decay import candidate_as


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=13); ap.add_argument('--Rmax',type=int,default=90)
    args=ap.parse_args(); prev={}
    all_gain=[]
    for R in range(1,args.Rmax+1):
        cur={a:(holes,patched,hits) for a,holes,patched,hits in candidate_as(args.P,R,args.y)}
        gained={a:v for a,v in cur.items() if a not in prev}
        if gained:
            cnt=Counter(v[0] for v in gained.values())
            print(f"R={R},gained={len(gained)},hole_profile={sorted(cnt.items())},items={sorted((a,)+v for a,v in gained.items())[:40]}")
            all_gain.extend((R,a)+v for a,v in gained.items())
        prev=cur
    print('all_gain_hole_profile=', sorted(Counter(x[2] for x in all_gain).items()))
    print('max_gain_R=', max((x[0] for x in all_gain), default=None), 'max_gain_holes=', max((x[2] for x in all_gain), default=None))
if __name__=='__main__': main()
