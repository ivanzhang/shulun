#!/usr/bin/env python3
"""滑动窗口低 cover 块存在引理数值量化。

给定总洞数 N、全局补丁数 C、块长 W，若每个补丁 q 覆盖若干洞，
则它对所有长度W滑动窗口的局部cover贡献等于其命中窗口数。
粗上界：任一补丁若至少命中一个洞，则命中窗口数 <= W + span_hits。
本脚本先验证纯组合平均：若每个全局补丁被计入所有与其覆盖洞相交的窗口，
平均局部cover可能放大；估计放大因子。

简化保守界：每个补丁至多覆盖全段，但其窗口出现数至多 B=N-W+1，太松。
更有用界：若每个 q 的覆盖周期约 q，局部出现窗口数可控。此脚本输出基础滑窗参数。
"""
import argparse, math

PHI2310=480
M=2310

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=100000); ap.add_argument('--W',type=int,default=100)
    args=ap.parse_args()
    N=math.floor(args.P*PHI2310/M)
    C=args.P/(math.log(args.P))-5
    blocks=max(1,N-args.W+1)
    naive_avg=C*args.W/N
    print('P',args.P,'N_B11',N,'W',args.W,'blocks',blocks,'pi_approx_gt11',C)
    print('ideal_local_cover_avg_if_uniform',naive_avg,'ratio',naive_avg/args.W)
    print('target_saving_W_minus_avg',args.W-naive_avg)

if __name__=='__main__': main()
