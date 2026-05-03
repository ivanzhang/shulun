#!/usr/bin/env python3
"""三点小模数 singular cumulant 平均实验。

对 offsets {0,a,b} 计算小筛局部权重 W3 与低阶项组合：
  K3 = W3 - W12*W3? 用归一化变量 Y_h=1_{rough}/pB - 1 的三阶中心矩代理。
即 E[Y0 Ya Yb] = W3/pB^3 - W2(0,a)/pB^2 - W2(0,b)/pB^2 - W2(a,b)/pB^2 + 2.
扫描 1<=a<b<=L 的平均与绝对平均。
"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def weight(offsets, small):
    w=1.0
    for p in small:
        nu=len({o%p for o in offsets})
        if nu>=p: return 0.0
        w*=1-nu/p
    return w


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P B L pB count meanK3 meanAbsK3 sumK3 sumAbsK3 maxAbsK3')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); small=primes(sieve(B),B)
        pB=1.0
        for p in small: pB*=1-1/p
        vals=[]
        for a in range(1,L+1):
            w01=weight([0,a],small)/(pB*pB)
            for b in range(a+1,L+1):
                w02=weight([0,b],small)/(pB*pB)
                w12=weight([a,b],small)/(pB*pB)
                w3=weight([0,a,b],small)/(pB**3)
                k3=w3-w01-w02-w12+2
                vals.append(k3)
        print(P,B,L,f'{pB:.6f}',len(vals),f'{sum(vals)/len(vals):.6f}',f'{sum(abs(x) for x in vals)/len(vals):.6f}',f'{sum(vals):.3f}',f'{sum(abs(x) for x in vals):.3f}',f'{max(abs(x) for x in vals):.3f}')
if __name__=='__main__': main()
