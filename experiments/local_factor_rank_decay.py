#!/usr/bin/env python3
"""枚举局部 connected cumulant 因子按分区秩的 p 衰减。"""
import argparse, itertools, math
from local_partition_connected_factor import local_cumulant, pattern


def rank_of_residues(residues):
    return len(residues)-len(set(residues))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--r',type=int,default=4); ap.add_argument('--ps',default='5,7,11,13,17,19'); args=ap.parse_args()
    print('r p rank count maxAbs scaled_p_rank scaled_p_rank_plus1 meanAbs')
    for p in [int(x) for x in args.ps.split(',') if x.strip()]:
        by={}
        for residues in itertools.product(range(p), repeat=args.r):
            rk=rank_of_residues(residues); val=abs(local_cumulant(residues,p))
            if rk not in by: by[rk]=[0,0.0,0.0]
            by[rk][0]+=1; by[rk][1]=max(by[rk][1],val); by[rk][2]+=val
        for rk,st in sorted(by.items()):
            cnt,mx,sm=st
            print(args.r,p,rk,cnt,f'{mx:.8g}',f'{mx*(p**rk):.6g}',f'{mx*(p**(rk+1)):.6g}',f'{sm/cnt:.8g}')
if __name__=='__main__': main()
