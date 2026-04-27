#!/usr/bin/env python3
"""高 cover 分支摘要：cover>theta*T 时 singles 与 q_count 范围。"""
import argparse, sys
sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c, min_cover_fast


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Tlist',default='20,25,30,36,40'); ap.add_argument('--theta',type=float,default=0.5)
    args=ap.parse_args()
    print('T theta high_count cover_range q_range singles_range saving_range min_singles max_singles')
    for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
        arr=[]
        for c in range(M):
            holes=holes_for_c(c,T); b=min_cover_fast(holes)
            cover=b['cover']; q=len(b['chosen']); singles=T-b['covered']; saving=b['saving']
            if cover>args.theta*T: arr.append((cover,q,singles,saving,c))
        if not arr:
            print(T,args.theta,0); continue
        print(T,args.theta,len(arr),(min(x[0] for x in arr),max(x[0] for x in arr)),(min(x[1] for x in arr),max(x[1] for x in arr)),(min(x[2] for x in arr),max(x[2] for x in arr)),(min(x[3] for x in arr),max(x[3] for x in arr)),min(arr,key=lambda x:x[2]),max(arr,key=lambda x:x[2]),flush=True)
if __name__=='__main__': main()
