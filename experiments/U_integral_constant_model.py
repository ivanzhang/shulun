#!/usr/bin/env python3
"""U/H 的连续积分常数模型。

U≈∫_{u=L}^{P} (π(P^2/u)-π(u)) dπ(u)
H≈P^2 * prod_{p<=B}(1-1/p)
比较真实二维计数与 PNT 积分代理。
"""
import argparse, math
from high_threshold_margin_fast import sieve, primes


def li_density_integral(P, L, steps=20000):
    # 积分 du/log u * ((P^2/u)/log(P^2/u) - u/log u) 的正部
    lo=L; hi=P
    if hi<=lo: return 0.0
    total=0.0
    dx=(hi-lo)/steps
    for i in range(steps):
        u=lo+(i+0.5)*dx
        maxv=(P*P)/u
        if maxv<u: continue
        val=(1/math.log(u))*((maxv/math.log(maxv))-(u/math.log(u)))
        if val>0: total += val*dx
    return total


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001,8009'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P B L pB Hmodel Uint ratioModel')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P)))
        small=primes(sieve(B),B); pB=1.0
        for p in small: pB*=1-1/p
        Hmodel=P*P*pB
        Uint=li_density_integral(P,L)
        print(P,B,L,f'{pB:.6f}',f'{Hmodel:.1f}',f'{Uint:.1f}',f'{Uint/Hmodel:.4f}')
if __name__=='__main__': main()
