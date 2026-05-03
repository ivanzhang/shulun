#!/usr/bin/env python3
"""计算 U 渐近积分常数收敛到 (e^gamma/4)log3 的情况。"""
import math

def integral_const(C=4, logP=1000, steps=200000):
    # 保留 L=C sqrt(P) 导致下限 a0=1/2+log C/log P。
    a0=0.5+math.log(C)/logP
    if a0>=1: return 0.0
    dx=(1-a0)/steps
    s=0.0
    for i in range(steps):
        a=a0+(i+0.5)*dx
        s += 1/(a*(2-a))*dx
    return math.exp(0.5772156649015329)/2 * s  # 1/(2 e^-gamma) * integral

print('target', math.exp(0.5772156649015329)/4*math.log(3))
for lp in [10,20,50,100,200,500,1000]:
    print(lp, integral_const(4, lp, 50000))
