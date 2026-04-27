#!/usr/bin/env python3
"""小骨架低洞数阈值的严格周期计算。

对固定 y，小骨架洞集由素数 p<=y 的禁余类决定。
由于 P 与所有 p<=y 互素，随着 a 变化，洞集等价于一个模 M=prod(p<=y) 的平移可约化集合。
本脚本在周期 M 上计算：任意长度 R 的连续窗口中，最少有多少个洞。
找出保证 min_holes>=k 的最小 R。

用法示例：
    python3 experiments/skeleton_low_hole_threshold.py --y 13 --k 3
    python3 experiments/skeleton_low_hole_threshold.py --y 17 --k 3
"""
import argparse
import math
from fixed_anchor_sieve_remainder import primes_upto


def period_pattern(y):
    ps = primes_upto(y)
    M = 1
    for p in ps:
        M *= p
    # 标准洞模式：r 不等于 0 mod p 对所有 p<=y；任意 a,P 只会给每个 p 一个禁余类，CRT 等价于平移/单位变换。
    # 为了得到“任意禁余类系统”的最坏窗口，需要枚举 CRT 平移吗？每个 p 禁一个类，乘以 P^{-1} 并平移 a 后等价于 r mod p != c_p。
    # 通过 CRT，任意 (c_p) 对应模 M 的一个 c；洞模式为 gcd(r-c, M)=1。
    # 因此所有情况都是 reduced residues 的平移。
    arr = [1 if math.gcd(r, M) == 1 else 0 for r in range(M)]
    return ps, M, arr


def min_window_count_cyclic(arr, R):
    M = len(arr)
    if R >= M:
        full = sum(arr) * (R // M)
        rem = R % M
        if rem == 0:
            return full, 0
        mrem, pos = min_window_count_cyclic(arr, rem)
        return full + mrem, pos
    ext = arr + arr[:R]
    s = sum(ext[:R])
    best = s; bestpos = 0
    for i in range(1, M):
        s += ext[i+R-1] - ext[i-1]
        if s < best:
            best = s; bestpos = i
    return best, bestpos


def threshold(y, k, Rmax=None):
    ps, M, arr = period_pattern(y)
    if Rmax is None:
        Rmax = M
    for R in range(1, Rmax + 1):
        m, pos = min_window_count_cyclic(arr, R)
        if m >= k:
            return R, m, pos, ps, M, sum(arr)
    return None, None, None, ps, M, sum(arr)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--y',type=int,default=13); ap.add_argument('--k',type=int,default=3); ap.add_argument('--Rmax',type=int,default=0); ap.add_argument('--table',action='store_true')
    args=ap.parse_args()
    ps,M,arr=period_pattern(args.y)
    print(f"y={args.y},primes={ps},M={M},phi={sum(arr)},density={sum(arr)/M:.6f}")
    if args.table:
        for R in range(1,(args.Rmax or 100)+1):
            m,pos=min_window_count_cyclic(arr,R)
            print(f"R={R},min_holes={m},pos={pos}")
    R,m,pos,_,_,_=threshold(args.y,args.k,args.Rmax or None)
    print(f"threshold_k={args.k}: R={R},min_holes={m},worst_pos={pos}")
    if R:
        for t in range(max(1,R-5),R+6):
            m2,pos2=min_window_count_cyclic(arr,t)
            print(f"near R={t},min_holes={m2},pos={pos2}")

if __name__=='__main__': main()
