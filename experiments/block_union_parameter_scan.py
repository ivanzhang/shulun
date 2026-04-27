#!/usr/bin/env python3
"""块级低 cover 事件窗口并集参数扫描。

对固定 W,S，计算一个代表性 B11 块的骨架并集界 U_block，
再乘窗口数 N≈rho*P，测试 (N-W+1)*U_block 是否 <1。

用法示例：
    python3 experiments/block_union_parameter_scan.py --P 10000000 --c 1213 --params 50:25,80:45,100:55,120:70,150:90,200:136
"""
import argparse, math, sys
sys.path.append('experiments')
from skeleton_union_bound import q_options, union_weight_dp, M
from b11_segment_cover_branch import holes_for_c

RHO=480/2310

def block_bound(c,W,S,P):
    holes=holes_for_c(c,W)
    opts=q_options(holes)
    weight=union_weight_dp(opts,S)
    u_block=P*weight/M
    windows=max(1,math.floor(RHO*P)-W+1)
    return u_block, windows*u_block, weight, len(opts), max(holes)-min(holes)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=10_000_000); ap.add_argument('--c',type=int,default=1213); ap.add_argument('--params',default='50:25,80:45,100:55,120:70,150:90,200:136')
    args=ap.parse_args()
    print('P c W S D qopts U_block windows_times_U raw_weight')
    for item in args.params.split(','):
        W,S=[int(x) for x in item.split(':')]
        ub,total,weight,qopts,D=block_bound(args.c,W,S,args.P)
        print(args.P,args.c,W,S,D,qopts,f'{ub:.6g}',f'{total:.6g}',f'{weight:.6g}',flush=True)
if __name__=='__main__': main()
